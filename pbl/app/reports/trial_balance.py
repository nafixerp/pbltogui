"""
Trial Balance report — conversion of GMINE ``w_trialbal`` (up to a date).

For each account in ``accountm`` the closing balance is the opening balance plus
the signed sum of its ``daybook`` postings up to the chosen date. A positive
balance is shown in the Debit column, negative in Credit. The totals row shows
the trial balance tallies (total debit == total credit). Shared framework.
"""

from __future__ import annotations

import datetime

import db
from app import modules
from app.reports.framework import ReportParam, ReportSpec, ReportView

COLUMNS = ["accode", "name", "debit", "credit"]


def _run(values: dict):
    upto = values.get("upto") or str(datetime.date.today())
    try:
        accounts = db.fetch_all("SELECT accode, name, COALESCE(opbal,0) AS opbal "
                                "FROM accountm ORDER BY accode")
    except Exception:
        accounts = []

    out = []
    tot_dr = tot_cr = 0.0
    for a in accounts:
        try:
            row = db.fetch_one(
                "SELECT COALESCE(SUM(amount),0) AS s FROM daybook "
                "WHERE accode = ? AND tdate <= ?", (a["accode"], upto))
            movement = float(row["s"]) if row else 0.0
        except Exception:
            movement = 0.0
        bal = round(float(a.get("opbal") or 0) + movement, 2)
        if abs(bal) < 0.005:
            continue
        debit = bal if bal > 0 else 0.0
        credit = -bal if bal < 0 else 0.0
        tot_dr += debit
        tot_cr += credit
        out.append({"accode": a["accode"], "name": a.get("name") or "",
                    "debit": f"{debit:.2f}" if debit else "",
                    "credit": f"{credit:.2f}" if credit else ""})
    if out:
        out.append({"accode": "TOTAL", "name": "",
                    "debit": f"{round(tot_dr, 2):.2f}",
                    "credit": f"{round(tot_cr, 2):.2f}"})
    return COLUMNS, out


SPEC = ReportSpec(
    title="Trial Balance",
    params=[ReportParam("upto", "Up to", "date")],
    run=_run,
)


def _factory(window):
    return ReportView(SPEC)


modules.register("w_trialbal")(_factory)
