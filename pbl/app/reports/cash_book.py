"""
Cash Book report — conversion of GMINE ``w_cashbookreport``.

The ledger of the Cash account: ``daybook`` movements on ``CASH`` between two
dates with receipts (Dr) / payments (Cr) and a running cash balance, opening
with the brought-forward balance. Shared :mod:`app.reports.framework`.
"""

from __future__ import annotations

import datetime

import db
from app import modules
from app.reports.framework import ReportParam, ReportSpec, ReportView

CASH_ACCOUNT = "CASH"
COLUMNS = ["tdate", "slno", "particulars", "receipt", "payment", "balance"]


def _run(values: dict):
    d1 = values.get("rdate1") or "1900-01-01"
    d2 = values.get("rdate2") or str(datetime.date.today())

    opbal = 0.0
    try:
        a = db.fetch_one("SELECT COALESCE(opbal,0) AS o FROM accountm WHERE accode = ?",
                         (CASH_ACCOUNT,))
        opbal = float(a["o"]) if a else 0.0
        pri = db.fetch_one("SELECT COALESCE(SUM(amount),0) AS s FROM daybook "
                           "WHERE accode = ? AND tdate < ?", (CASH_ACCOUNT, d1))
        opbal += float(pri["s"]) if pri else 0.0
    except Exception:
        opbal = 0.0

    try:
        rows = db.fetch_all(
            "SELECT slno, tdate, amount, control, opaccode FROM daybook "
            "WHERE accode = ? AND tdate BETWEEN ? AND ? ORDER BY tdate, slno",
            (CASH_ACCOUNT, d1, d2))
    except Exception:
        rows = []

    out = [{"tdate": d1, "slno": "", "particulars": "Opening Balance",
            "receipt": "", "payment": "", "balance": f"{opbal:.2f}"}]
    running = opbal
    for r in rows:
        amt = float(r.get("amount") or 0)
        running += amt
        out.append({
            "tdate": r.get("tdate"), "slno": r.get("slno"),
            "particulars": f"{r.get('control')} / {r.get('opaccode')}",
            "receipt": f"{amt:.2f}" if amt > 0 else "",
            "payment": f"{-amt:.2f}" if amt < 0 else "",
            "balance": f"{running:.2f}",
        })
    if len(out) > 1:
        out.append({"tdate": "", "slno": "", "particulars": "Closing Balance",
                    "receipt": "", "payment": "", "balance": f"{running:.2f}"})
    return COLUMNS, out


SPEC = ReportSpec(
    title="Cash Book",
    params=[ReportParam("rdate1", "From", "date"),
            ReportParam("rdate2", "To", "date")],
    run=_run,
)


def _factory(window):
    return ReportView(SPEC)


modules.register("w_cashbookreport")(_factory)
