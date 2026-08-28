"""
Purchase Register report — conversion of GMINE ``w_purhregister``.

Document-wise purchases between two dates, querying the ``purchasem`` header the
converted Purchase module writes, with a totals row. Runs on the shared
:mod:`app.reports.framework`.
"""

from __future__ import annotations

import datetime

import db
from app import modules
from app.reports.framework import ReportParam, ReportSpec, ReportView

COLUMNS = ["docno", "billno", "tdate", "name", "netamt",
           "cgst", "sgst", "igst", "round", "total"]


def _run(values: dict):
    d1 = values.get("rdate1") or "1900-01-01"
    d2 = values.get("rdate2") or str(datetime.date.today())
    try:
        rows = db.fetch_all(
            "SELECT docno, billno, tdate, name, netamt, cgst, sgst, igst, "
            "round, total FROM purchasem WHERE tdate BETWEEN ? AND ? "
            "ORDER BY docno", (d1, d2))
    except Exception:
        rows = []
    if rows:
        total = {c: "" for c in COLUMNS}
        total["docno"] = "TOTAL"
        for c in ("netamt", "cgst", "sgst", "igst", "round", "total"):
            total[c] = round(sum(float(r.get(c) or 0) for r in rows), 2)
        rows = list(rows) + [total]
    return COLUMNS, rows


SPEC = ReportSpec(
    title="Purchase Register",
    params=[ReportParam("rdate1", "From", "date"),
            ReportParam("rdate2", "To", "date")],
    run=_run,
)


def _factory(window):
    return ReportView(SPEC)


modules.register("w_purhregister")(_factory)
