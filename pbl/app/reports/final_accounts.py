"""
The final accounts: Trading & Profit and Loss, Balance Sheet, Cash Balance.

These windows build their DataWindow in code, so there is no stored query to
run. They are converted here from the original scripts:

* **Trading / Profit & Loss** (``w_pandlac_trading``) — accounts whose
  ``actype1`` is ``E`` or ``R``, split by ``tplpos``: 1 is the Trading account,
  2 is Profit & Loss, anything else is grouped after them. Gross profit comes
  from the Trading section, net profit from Profit & Loss.
* **Balance Sheet** (``w_balsheet``) — accounts whose ``actype1`` is ``A`` or
  ``L``, grouped by ``bshead``, with the net profit carried in.
* **Cash Balance** (``w_cashbal``) and **Yearly Cash Balance**
  (``w_cashbookreport_year``) — the ``CASH`` account's opening balance plus its
  ``daybook`` movement, as on a date and month by month.

A balance is always ``opbal`` (or ``opbalb`` for the balance company) plus the
signed sum of the account's ``daybook`` postings up to the date.
"""

from __future__ import annotations

import calendar
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


def account_balance(accode: str, upto: str, balance_company=False) -> float:
    """Opening balance plus movement up to ``upto``, as the original computes."""
    column = "opbalb" if balance_company else "opbal"
    row = db.fetch_one(f"SELECT {column} AS ob FROM accountm WHERE accode = ?",
                       (accode,))
    opening = _f(row["ob"]) if row else 0.0
    moved = db.fetch_one(
        "SELECT COALESCE(SUM(amount),0) AS s FROM daybook "
        "WHERE accode = ? AND tdate <= ?", (accode, upto))
    return round(opening + (_f(moved["s"]) if moved else 0.0), 2)


def _accounts(actypes: tuple, extra: str = "", params: tuple = ()) -> list:
    marks = ", ".join("?" for _ in actypes)
    try:
        return db.fetch_all(
            f"SELECT accode, name, COALESCE(opbal,0) AS opbal, "
            f"COALESCE(tplpos,0) AS tplpos, COALESCE(bshead,'') AS bshead "
            f"FROM accountm WHERE actype1 IN ({marks}) {extra} ORDER BY name",
            list(actypes) + list(params))
    except Exception:
        return []


def _movement(accode: str, start: str | None, upto: str) -> float:
    if start:
        row = db.fetch_one(
            "SELECT COALESCE(SUM(amount),0) AS s FROM daybook "
            "WHERE accode = ? AND tdate >= ? AND tdate <= ?", (accode, start, upto))
    else:
        row = db.fetch_one(
            "SELECT COALESCE(SUM(amount),0) AS s FROM daybook "
            "WHERE accode = ? AND tdate <= ?", (accode, upto))
    return _f(row["s"]) if row else 0.0


# ---------------------------------------------------------------------------
# Trading and Profit & Loss
# ---------------------------------------------------------------------------

PL_COLUMNS = ["section", "accode", "name", "debit", "credit"]


def trading_and_pl(upto: str, start: str | None = None) -> tuple:
    """(columns, rows) for the Trading and Profit & Loss statement."""
    rows: list = []
    sections = {1: "Trading", 2: "Profit & Loss", 0: "Other"}
    totals = {1: [0.0, 0.0], 2: [0.0, 0.0], 0: [0.0, 0.0]}

    for account in _accounts(("E", "R")):
        balance = round(_f(account["opbal"]) + _movement(account["accode"],
                                                         start, upto), 2)
        if abs(balance) < 0.005:
            continue
        pos = int(_f(account["tplpos"]))
        pos = pos if pos in (1, 2) else 0
        debit = balance if balance > 0 else 0.0
        credit = -balance if balance < 0 else 0.0
        totals[pos][0] += debit
        totals[pos][1] += credit
        rows.append({"section": sections[pos], "accode": account["accode"],
                     "name": account.get("name") or "",
                     "debit": f"{debit:.2f}" if debit else "",
                     "credit": f"{credit:.2f}" if credit else ""})

    gross = round(totals[1][1] - totals[1][0], 2)
    net = round(gross + totals[2][1] - totals[2][0] + totals[0][1] - totals[0][0], 2)
    rows.sort(key=lambda r: (r["section"] != "Trading",
                             r["section"] != "Profit & Loss", r["name"]))
    rows.append({"section": "Trading", "accode": "", "name": "GROSS PROFIT",
                 "debit": f"{gross:.2f}" if gross > 0 else "",
                 "credit": f"{-gross:.2f}" if gross < 0 else ""})
    rows.append({"section": "Profit & Loss", "accode": "", "name": "NET PROFIT",
                 "debit": f"{net:.2f}" if net > 0 else "",
                 "credit": f"{-net:.2f}" if net < 0 else ""})
    return PL_COLUMNS, rows


def net_profit(upto: str, start: str | None = None) -> float:
    total = 0.0
    for account in _accounts(("E", "R")):
        total -= round(_f(account["opbal"]) + _movement(account["accode"],
                                                        start, upto), 2)
    return round(total, 2)


def _run_pl_upto(values: dict):
    return trading_and_pl(values.get("upto") or _today())


def _run_pl_period(values: dict):
    return trading_and_pl(values.get("to") or _today(), values.get("from"))


# ---------------------------------------------------------------------------
# Balance Sheet
# ---------------------------------------------------------------------------

BS_COLUMNS = ["side", "head", "accode", "name", "amount"]


def balance_sheet(upto: str) -> tuple:
    rows: list = []
    assets = liabilities = 0.0
    for account in _accounts(("A", "L")):
        balance = round(_f(account["opbal"]) + _movement(account["accode"],
                                                         None, upto), 2)
        if abs(balance) < 0.005:
            continue
        # The original treats a debit balance as an asset, a credit as a
        # liability (assets are negative in accountm.amount terms).
        side = "Assets" if balance > 0 else "Liabilities"
        if side == "Assets":
            assets += balance
        else:
            liabilities += -balance
        rows.append({"side": side, "head": account.get("bshead") or "",
                     "accode": account["accode"], "name": account.get("name") or "",
                     "amount": f"{abs(balance):.2f}"})

    profit = net_profit(upto)
    if abs(profit) >= 0.005:
        side = "Liabilities" if profit > 0 else "Assets"
        if side == "Liabilities":
            liabilities += abs(profit)
        else:
            assets += abs(profit)
        rows.append({"side": side, "head": "", "accode": "",
                     "name": "NET PROFIT" if profit > 0 else "NET LOSS",
                     "amount": f"{abs(profit):.2f}"})

    rows.sort(key=lambda r: (r["side"] != "Liabilities", r["head"], r["name"]))
    rows.append({"side": "Liabilities", "head": "", "accode": "", "name": "TOTAL",
                 "amount": f"{round(liabilities, 2):.2f}"})
    rows.append({"side": "Assets", "head": "", "accode": "", "name": "TOTAL",
                 "amount": f"{round(assets, 2):.2f}"})
    return BS_COLUMNS, rows


def _run_bs(values: dict):
    return balance_sheet(values.get("upto") or _today())


# ---------------------------------------------------------------------------
# Cash balance
# ---------------------------------------------------------------------------

CASH_COLUMNS = ["particulars", "amount"]


def cash_balance(upto: str) -> tuple:
    balance = account_balance("CASH", upto)
    receipts = db.fetch_one(
        "SELECT COALESCE(SUM(amount),0) AS s FROM daybook "
        "WHERE accode = 'CASH' AND amount > 0 AND tdate = ?", (upto,))
    payments = db.fetch_one(
        "SELECT COALESCE(SUM(amount),0) AS s FROM daybook "
        "WHERE accode = 'CASH' AND amount < 0 AND tdate = ?", (upto,))
    rows = [
        {"particulars": f"Cash balance as on {upto}", "amount": f"{balance:.2f}"},
        {"particulars": "Received today", "amount": f"{_f(receipts['s']):.2f}"},
        {"particulars": "Paid today", "amount": f"{abs(_f(payments['s'])):.2f}"},
    ]
    return CASH_COLUMNS, rows


def _run_cash(values: dict):
    return cash_balance(values.get("upto") or _today())


YEAR_COLUMNS = ["month", "receipts", "payments", "closing"]


def yearly_cash_balance(year: int) -> tuple:
    rows = []
    for month in range(1, 13):
        last = datetime.date(year, month, calendar.monthrange(year, month)[1])
        first = datetime.date(year, month, 1)
        received = db.fetch_one(
            "SELECT COALESCE(SUM(amount),0) AS s FROM daybook WHERE accode='CASH' "
            "AND amount > 0 AND tdate >= ? AND tdate <= ?",
            (first.isoformat(), last.isoformat()))
        paid = db.fetch_one(
            "SELECT COALESCE(SUM(amount),0) AS s FROM daybook WHERE accode='CASH' "
            "AND amount < 0 AND tdate >= ? AND tdate <= ?",
            (first.isoformat(), last.isoformat()))
        rows.append({"month": first.strftime("%b %Y"),
                     "receipts": f"{_f(received['s']):.2f}",
                     "payments": f"{abs(_f(paid['s'])):.2f}",
                     "closing": f"{account_balance('CASH', last.isoformat()):.2f}"})
    return YEAR_COLUMNS, rows


def _run_year(values: dict):
    try:
        year = int(values.get("year") or datetime.date.today().year)
    except (TypeError, ValueError):
        year = datetime.date.today().year
    return yearly_cash_balance(year)


# ---------------------------------------------------------------------------
# Registration
# ---------------------------------------------------------------------------

SPECS = {
    "w_pandlac_trading": ReportSpec(
        title="Trading and Profit & Loss",
        params=[ReportParam("from", "From", "date"), ReportParam("to", "To", "date")],
        run=_run_pl_period),
    "w_balsheet": ReportSpec(
        title="Balance Sheet",
        params=[ReportParam("upto", "As on", "date")], run=_run_bs),
    "w_cashbal": ReportSpec(
        title="Cash Balance",
        params=[ReportParam("upto", "As on", "date")], run=_run_cash),
    "w_cashbookreport_year": ReportSpec(
        title="Yearly Cash Balance",
        params=[ReportParam("year", "Year", "text",
                            default=str(datetime.date.today().year))],
        run=_run_year),
}

for _window, _spec in SPECS.items():
    modules.register(_window)(
        lambda parsed=None, _s=_spec, **kw: ReportView(_s))
