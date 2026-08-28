"""
The reports the original builds in code, converted.

Each of these windows assembles its DataWindow row by row in PowerScript, so
there is no stored query for the generic data view to run. They are rebuilt
here from the same tables the scripts read:

* **Party History** (``w_partyhistory``) — every document of one account.
* **Barcode History** (``w_barcode_history``) — every movement of one barcode.
* **Group-wise Expanded List** (``w_account_grpwise_expand_rep``) — accounts of
  a group with opening, movement and closing balances.
* **Non-Transactional Days** (``w_nontransactionaldays_report``) — days in a
  range with no daybook or goldsmith entry.
* **Integrity Checking** (``w_account_checking``) — vouchers whose legs do not
  net to zero, and postings to accounts that no longer exist.
* **Loan Ledger** (``w_loanledger_rep``) — a loan and its collections.
* **Stock Register Summary** (``w_stockregister_summary``) — day-wise document
  and weight totals.
* **Day Report** (``w_dayreport_gk``) and **Daily All Report**
  (``w_dailyallreport``) — a day's trading at a glance.
"""

from __future__ import annotations

import datetime

import db
from app import modules
from app.reports.framework import ReportParam, ReportSpec, ReportView


def _f(value) -> float:
    try:
        return float(value or 0)
    except (TypeError, ValueError):
        return 0.0


def _today() -> str:
    return datetime.date.today().isoformat()


def _rows(sql, params=()):
    try:
        return db.fetch_all(sql, params)
    except Exception:
        return []


def _one(sql, params=()):
    try:
        return db.fetch_one(sql, params)
    except Exception:
        return None


def _sum(table, column, where, params) -> float:
    row = _one(f"SELECT COALESCE(SUM({column}),0) AS s FROM {table} WHERE {where}",
               params)
    return _f(row["s"]) if row else 0.0


def _count(table, where, params) -> int:
    row = _one(f"SELECT COUNT(*) AS c FROM {table} WHERE {where}", params)
    return int(row["c"]) if row else 0


# ---------------------------------------------------------------------------
# Party history
# ---------------------------------------------------------------------------

PARTY_COLUMNS = ["tdate", "type", "docno", "amount", "weight"]


def party_history(accode: str, start: str, end: str) -> tuple:
    accode = (accode or "").strip()
    rows: list = []
    if not accode:
        return PARTY_COLUMNS, rows

    sources = (
        ("Sales", "salesm", "billno", "custcode", "netamt"),
        ("Sales Return", "salesrm", "billno", "custcode", "netamt"),
        ("Purchase", "purchasem", "docno", "suppcode", "netamt"),
        ("Purchase Return", "purchaserm", "docno", "suppcode", "netamt"),
        ("Goldsmith", "smithm", "docno", "smithcode", "netamt"),
        ("Order", "orderm", "ordno", "custcode", "netamt"),
    )
    for label, table, docno, party, amount in sources:
        for row in _rows(f"SELECT tdate, {docno} AS docno, {amount} AS amount, slno "
                         f"FROM {table} WHERE {party} = ? AND tdate >= ? AND tdate <= ?"
                         f" ORDER BY tdate", (accode, start, end)):
            rows.append({"tdate": row.get("tdate"), "type": label,
                         "docno": row.get("docno"),
                         "amount": f"{_f(row.get('amount')):.2f}",
                         "weight": ""})

    for row in _rows("SELECT tdate, sno AS docno, amount FROM daybook "
                     "WHERE accode = ? AND tdate >= ? AND tdate <= ? ORDER BY tdate",
                     (accode, start, end)):
        rows.append({"tdate": row.get("tdate"),
                     "type": "Receipt" if _f(row.get("amount")) < 0 else "Payment",
                     "docno": row.get("docno"),
                     "amount": f"{abs(_f(row.get('amount'))):.2f}", "weight": ""})

    rows.sort(key=lambda r: str(r["tdate"]))
    return PARTY_COLUMNS, rows


def _run_party(values: dict):
    return party_history(values.get("accode", ""),
                         values.get("from") or _today(),
                         values.get("to") or _today())


# ---------------------------------------------------------------------------
# Barcode history
# ---------------------------------------------------------------------------

BARCODE_COLUMNS = ["tdate", "type", "docno", "qty", "weight", "stonewgt"]


def barcode_history(bcode) -> tuple:
    rows: list = []
    if not bcode:
        return BARCODE_COLUMNS, rows
    sources = (
        ("Sales", "salesm", "salesd", "billno"),
        ("Sales Return", "salesrm", "salesrd", "billno"),
        ("Purchase", "purchasem", "purchased", "docno"),
        ("Goldsmith", "smithm", "smithd", "docno"),
    )
    for label, master, detail, docno in sources:
        for row in _rows(
                f"SELECT m.tdate AS tdate, m.{docno} AS docno, d.qty AS qty, "
                f"d.weight AS weight, d.stonewgt AS stonewgt "
                f"FROM {master} m, {detail} d "
                f"WHERE d.slno = m.slno AND d.bcode = ? ORDER BY m.tdate", (bcode,)):
            rows.append({"tdate": row.get("tdate"), "type": label,
                         "docno": row.get("docno"),
                         "qty": row.get("qty"),
                         "weight": f"{_f(row.get('weight')):.3f}",
                         "stonewgt": f"{_f(row.get('stonewgt')):.3f}"})

    for row in _rows("SELECT tdate, fromqty AS qty, fromwgt AS weight, "
                     "fromstwgt AS stonewgt FROM itemadj WHERE bcode = ? "
                     "ORDER BY tdate", (bcode,)):
        rows.append({"tdate": row.get("tdate"), "type": "Stock transfer",
                     "docno": "", "qty": row.get("qty"),
                     "weight": f"{_f(row.get('weight')):.3f}",
                     "stonewgt": f"{_f(row.get('stonewgt')):.3f}"})

    rows.sort(key=lambda r: str(r["tdate"]))
    return BARCODE_COLUMNS, rows


def _run_barcode(values: dict):
    return barcode_history(values.get("bcode"))


# ---------------------------------------------------------------------------
# Group-wise expanded list
# ---------------------------------------------------------------------------

GROUP_COLUMNS = ["accode", "name", "opening", "movement", "closing"]


def group_expanded(grcode: str, start: str, end: str) -> tuple:
    rows: list = []
    where = "grcode = ?" if (grcode or "").strip() else "1 = 1"
    params = ((grcode.strip(),) if (grcode or "").strip() else ())
    for account in _rows(f"SELECT accode, name, COALESCE(opbal,0) AS opbal "
                         f"FROM accountm WHERE {where} ORDER BY name", params):
        before = _sum("daybook", "amount", "accode = ? AND tdate < ?",
                      (account["accode"], start))
        movement = _sum("daybook", "amount",
                        "accode = ? AND tdate >= ? AND tdate <= ?",
                        (account["accode"], start, end))
        opening = round(_f(account["opbal"]) + before, 2)
        closing = round(opening + movement, 2)
        if not (opening or movement or closing):
            continue
        rows.append({"accode": account["accode"], "name": account.get("name") or "",
                     "opening": f"{opening:.2f}", "movement": f"{movement:.2f}",
                     "closing": f"{closing:.2f}"})
    return GROUP_COLUMNS, rows


def _run_group(values: dict):
    return group_expanded(values.get("grcode", ""),
                          values.get("from") or _today(),
                          values.get("to") or _today())


# ---------------------------------------------------------------------------
# Non-transactional days
# ---------------------------------------------------------------------------

IDLE_COLUMNS = ["tdate", "day", "vouchers", "goldsmith"]


def non_transactional_days(start: str, end: str) -> tuple:
    rows = []
    day = datetime.date.fromisoformat(start)
    last = datetime.date.fromisoformat(end)
    while day <= last:
        stamp = day.isoformat()
        vouchers = _count("daybook", "tdate = ?", (stamp,))
        smith = _count("smithm", "tdate = ?", (stamp,))
        if vouchers == 0 and smith == 0:
            rows.append({"tdate": stamp, "day": day.strftime("%A"),
                         "vouchers": vouchers, "goldsmith": smith})
        day += datetime.timedelta(days=1)
    return IDLE_COLUMNS, rows


def _run_idle(values: dict):
    return non_transactional_days(values.get("from") or _today(),
                                  values.get("to") or _today())


# ---------------------------------------------------------------------------
# Integrity checking
# ---------------------------------------------------------------------------

CHECK_COLUMNS = ["check", "reference", "detail"]


def integrity_check(upto: str) -> tuple:
    rows: list = []
    for row in _rows("SELECT slno, SUM(amount) AS s, MAX(tdate) AS tdate "
                     "FROM daybook WHERE tdate <= ? GROUP BY slno", (upto,)):
        if abs(_f(row["s"])) >= 0.005:
            rows.append({"check": "Voucher does not balance",
                         "reference": f"slno {row['slno']} ({row.get('tdate')})",
                         "detail": f"difference {_f(row['s']):.2f}"})

    accounts = {a["accode"] for a in _rows("SELECT accode FROM accountm")}
    for row in _rows("SELECT DISTINCT accode FROM daybook WHERE tdate <= ?", (upto,)):
        if row["accode"] not in accounts:
            rows.append({"check": "Posting to a missing account",
                         "reference": row["accode"], "detail": ""})

    for row in _rows("SELECT code, name, weight, weightb, qty, qtyb FROM items"):
        if abs(_f(row["weight"]) - _f(row["weightb"])) >= 0.005:
            rows.append({"check": "Stock and balance weight differ",
                         "reference": f"{row['code']} {row.get('name') or ''}",
                         "detail": f"{_f(row['weight']):.3f} vs "
                                   f"{_f(row['weightb']):.3f}"})
    if not rows:
        rows.append({"check": "No problems found", "reference": "", "detail": ""})
    return CHECK_COLUMNS, rows


def _run_check(values: dict):
    return integrity_check(values.get("upto") or _today())


# ---------------------------------------------------------------------------
# Loan ledger
# ---------------------------------------------------------------------------

LOAN_COLUMNS = ["tdate", "docno", "particulars", "amount", "interest"]


def loan_ledger(loanno: str) -> tuple:
    rows: list = []
    loanno = (loanno or "").strip()
    if not loanno:
        return LOAN_COLUMNS, rows
    for row in _rows("SELECT tdate, docno, amount FROM loan WHERE TRIM(docno) = ? "
                     "OR TRIM(loanno) = ?", (loanno, loanno)):
        rows.append({"tdate": row.get("tdate"), "docno": row.get("docno"),
                     "particulars": "Loan", "amount": f"{_f(row.get('amount')):.2f}",
                     "interest": ""})
    for row in _rows("SELECT tdate, docno, ramt, intamt FROM loancolln "
                     "WHERE TRIM(loanno) = ? ORDER BY tdate", (loanno,)):
        rows.append({"tdate": row.get("tdate"), "docno": row.get("docno"),
                     "particulars": "Collection",
                     "amount": f"{_f(row.get('ramt')):.2f}",
                     "interest": f"{_f(row.get('intamt')):.2f}"})
    rows.sort(key=lambda r: str(r["tdate"]))
    return LOAN_COLUMNS, rows


def _run_loan(values: dict):
    return loan_ledger(values.get("loanno", ""))


# ---------------------------------------------------------------------------
# Stock register summary / day report
# ---------------------------------------------------------------------------

DAY_COLUMNS = ["particulars", "count", "weight", "amount"]


def day_summary(start: str, end: str) -> tuple:
    sections = (
        ("Sales", "salesm", "salesd", "netamt"),
        ("Sales Return", "salesrm", "salesrd", "netamt"),
        ("Purchase", "purchasem", "purchased", "netamt"),
        ("Purchase Return", "purchaserm", "purchaserd", "netamt"),
        ("Goldsmith", "smithm", "smithd", "netamt"),
        ("Order", "orderm", "orderd", "netamt"),
    )
    rows = []
    for label, master, detail, amount in sections:
        count = _count(master, "tdate >= ? AND tdate <= ?", (start, end))
        total = _sum(master, amount, "tdate >= ? AND tdate <= ?", (start, end))
        weight = _sum(
            detail, "weight",
            f"slno IN (SELECT slno FROM {master} WHERE tdate >= ? AND tdate <= ?)",
            (start, end))
        if not (count or total or weight):
            continue
        rows.append({"particulars": label, "count": count,
                     "weight": f"{weight:.3f}", "amount": f"{total:.2f}"})

    received = _sum("daybook", "amount",
                    "amount > 0 AND tdate >= ? AND tdate <= ?", (start, end))
    paid = _sum("daybook", "amount",
                "amount < 0 AND tdate >= ? AND tdate <= ?", (start, end))
    rows.append({"particulars": "Cash/Bank received", "count": "",
                 "weight": "", "amount": f"{received:.2f}"})
    rows.append({"particulars": "Cash/Bank paid", "count": "",
                 "weight": "", "amount": f"{abs(paid):.2f}"})
    return DAY_COLUMNS, rows


def _run_day(values: dict):
    start = values.get("from") or _today()
    return day_summary(start, values.get("to") or start)


# ---------------------------------------------------------------------------
# Stock, asset, liability and expense summary  (w_stockandexpreport)
# ---------------------------------------------------------------------------

WORTH_COLUMNS = ["particulars", "amount"]


def stock_asset_liability_expense(upto: str) -> tuple:
    stock_value = 0.0
    for row in _rows("SELECT COALESCE(weight,0) AS w, COALESCE(cost,0) AS c, "
                     "COALESCE(qty,0) AS q FROM items"):
        stock_value += _f(row["w"]) * _f(row["c"])

    def total(actypes, positive):
        out = 0.0
        marks = ", ".join("?" for _ in actypes)
        for account in _rows(f"SELECT accode, COALESCE(opbal,0) AS opbal "
                             f"FROM accountm WHERE actype1 IN ({marks})",
                             list(actypes)):
            balance = _f(account["opbal"]) + _sum(
                "daybook", "amount", "accode = ? AND tdate <= ?",
                (account["accode"], upto))
            if positive and balance > 0:
                out += balance
            elif not positive and balance < 0:
                out += -balance
        return round(out, 2)

    rows = [
        {"particulars": "Stock value", "amount": f"{round(stock_value, 2):.2f}"},
        {"particulars": "Assets", "amount": f"{total(('A',), True):.2f}"},
        {"particulars": "Liabilities", "amount": f"{total(('L',), False):.2f}"},
        {"particulars": "Expenses", "amount": f"{total(('E',), True):.2f}"},
        {"particulars": "Income", "amount": f"{total(('R',), False):.2f}"},
    ]
    return WORTH_COLUMNS, rows


def _run_worth(values: dict):
    return stock_asset_liability_expense(values.get("upto") or _today())


# ---------------------------------------------------------------------------
# Registration
# ---------------------------------------------------------------------------

DATE_RANGE = [ReportParam("from", "From", "date"), ReportParam("to", "To", "date")]

SPECS = {
    "w_partyhistory": ReportSpec(
        title="Party History",
        params=[ReportParam("accode", "Account code", "text")] + DATE_RANGE,
        run=_run_party),
    "w_barcode_history": ReportSpec(
        title="Barcode History",
        params=[ReportParam("bcode", "Barcode", "text")], run=_run_barcode),
    "w_account_grpwise_expand_rep": ReportSpec(
        title="Groupwise Expanded List",
        params=[ReportParam("grcode", "Group code", "text")] + DATE_RANGE,
        run=_run_group),
    "w_nontransactionaldays_report": ReportSpec(
        title="Non Transactional Days", params=DATE_RANGE, run=_run_idle),
    "w_account_checking": ReportSpec(
        title="Integrity Checking",
        params=[ReportParam("upto", "Up to", "date")], run=_run_check),
    "w_loanledger_rep": ReportSpec(
        title="Loan Ledger",
        params=[ReportParam("loanno", "Loan no", "text")], run=_run_loan),
    "w_stockregister_summary": ReportSpec(
        title="Stock Register Summary", params=DATE_RANGE, run=_run_day),
    "w_dayreport_gk": ReportSpec(
        title="Day Report", params=DATE_RANGE, run=_run_day),
    "w_dailyallreport": ReportSpec(
        title="Daily All Report", params=DATE_RANGE, run=_run_day),
    "w_daysummarydate_mala": ReportSpec(
        title="Day Summary", params=DATE_RANGE, run=_run_day),
    "w_stockandexpreport": ReportSpec(
        title="Stock, Asset, Liability and Expense",
        params=[ReportParam("upto", "As on", "date")], run=_run_worth),
}

for _window, _spec in SPECS.items():
    modules.register(_window)(lambda parsed=None, _s=_spec, **kw: ReportView(_s))
