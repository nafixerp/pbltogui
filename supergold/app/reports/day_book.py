"""
Day Book report — conversion of GMINE ``w_daybookreport``.

Lists ``daybook`` postings between two dates with the account name resolved from
``accountm`` and the signed amount split into debit / credit columns. Totals show
that the day book balances (total debit == total credit). Shared framework.
"""

from __future__ import annotations

import datetime

import db
from app import modules
from app.reports.framework import ReportParam, ReportSpec, ReportView

COLUMNS = ["slno", "tdate", "accode", "name", "debit", "credit",
           "control", "opaccode"]


def _run(values: dict):
    d1 = values.get("rdate1") or "1900-01-01"
    d2 = values.get("rdate2") or str(datetime.date.today())
    try:
        rows = db.fetch_all(
            "SELECT d.slno, d.tdate, d.accode, a.name AS name, d.amount, "
            "d.control, d.opaccode FROM daybook d "
            "LEFT JOIN accountm a ON a.accode = d.accode "
            "WHERE d.tdate BETWEEN ? AND ? ORDER BY d.slno, d.amount DESC",
            (d1, d2))
    except Exception:
        rows = []

    out = []
    tot_dr = tot_cr = 0.0
    for r in rows:
        amt = float(r.get("amount") or 0)
        debit = amt if amt > 0 else 0.0
        credit = -amt if amt < 0 else 0.0
        tot_dr += debit
        tot_cr += credit
        out.append({
            "slno": r.get("slno"), "tdate": r.get("tdate"),
            "accode": r.get("accode"), "name": r.get("name") or "",
            "debit": f"{debit:.2f}" if debit else "",
            "credit": f"{credit:.2f}" if credit else "",
            "control": r.get("control"), "opaccode": r.get("opaccode"),
        })
    if out:
        out.append({"slno": "TOTAL", "tdate": "", "accode": "", "name": "",
                    "debit": f"{round(tot_dr, 2):.2f}",
                    "credit": f"{round(tot_cr, 2):.2f}",
                    "control": "", "opaccode": ""})
    return COLUMNS, out


SPEC = ReportSpec(
    title="Day Book",
    params=[ReportParam("rdate1", "From", "date"),
            ReportParam("rdate2", "To", "date")],
    run=_run,
)


def _factory(window):
    return ReportView(SPEC)


modules.register("w_daybookreport")(_factory)
