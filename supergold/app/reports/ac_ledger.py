"""
Account Ledger report — conversion of GMINE ``w_acledger``.

For a chosen account it lists the ``daybook`` movements between two dates with a
running balance (Dr/Cr), preceded by the opening balance brought forward. The
account picker is populated from ``accountm`` when the screen is opened. Shared
:mod:`app.reports.framework`.
"""

from __future__ import annotations

import datetime

import db
from app import modules
from app.reports.framework import ReportParam, ReportSpec, ReportView

COLUMNS = ["tdate", "slno", "particulars", "debit", "credit", "balance"]


def _fmt_balance(bal: float) -> str:
    if abs(bal) < 0.005:
        return "0.00"
    return f"{abs(bal):.2f} {'Dr' if bal > 0 else 'Cr'}"


def _run(values: dict):
    accode = (values.get("accode") or "").split(" - ")[0].strip()
    d1 = values.get("rdate1") or "1900-01-01"
    d2 = values.get("rdate2") or str(datetime.date.today())
    if not accode:
        return COLUMNS, []

    # Opening balance = account opening + movements strictly before d1.
    opbal = 0.0
    try:
        a = db.fetch_one("SELECT COALESCE(opbal,0) AS o FROM accountm WHERE accode = ?",
                         (accode,))
        opbal = float(a["o"]) if a else 0.0
        pri = db.fetch_one("SELECT COALESCE(SUM(amount),0) AS s FROM daybook "
                           "WHERE accode = ? AND tdate < ?", (accode, d1))
        opbal += float(pri["s"]) if pri else 0.0
    except Exception:
        opbal = 0.0

    try:
        rows = db.fetch_all(
            "SELECT slno, tdate, amount, control, opaccode FROM daybook "
            "WHERE accode = ? AND tdate BETWEEN ? AND ? ORDER BY tdate, slno",
            (accode, d1, d2))
    except Exception:
        rows = []

    out = [{"tdate": d1, "slno": "", "particulars": "Opening Balance",
            "debit": "", "credit": "", "balance": _fmt_balance(opbal)}]
    running = opbal
    for r in rows:
        amt = float(r.get("amount") or 0)
        running += amt
        out.append({
            "tdate": r.get("tdate"), "slno": r.get("slno"),
            "particulars": f"{r.get('control')} / {r.get('opaccode')}",
            "debit": f"{amt:.2f}" if amt > 0 else "",
            "credit": f"{-amt:.2f}" if amt < 0 else "",
            "balance": _fmt_balance(running),
        })
    if len(out) > 1:
        out.append({"tdate": "", "slno": "", "particulars": "Closing Balance",
                    "debit": "", "credit": "", "balance": _fmt_balance(running)})
    return COLUMNS, out


def _accounts() -> list[str]:
    try:
        rows = db.fetch_all("SELECT accode, name FROM accountm ORDER BY name")
        return [f"{r['accode']} - {r['name']}" for r in rows]
    except Exception:
        return []


def _factory(window):
    spec = ReportSpec(
        title="Account Ledger",
        params=[
            ReportParam("accode", "Account", "choice", options=_accounts()),
            ReportParam("rdate1", "From", "date"),
            ReportParam("rdate2", "To", "date"),
        ],
        run=_run,
    )
    return ReportView(spec)


modules.register("w_acledger")(_factory)
