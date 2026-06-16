"""
Sales Register report — conversion of GMINE ``w_saleregister`` /
``d_saleregister``.

The original DataWindow retrieves bill-wise sales between ``rdate1`` and
``rdate2``. This report queries the ``salesm`` header table the converted Sales
module writes, over the same date range, and presents the bill-wise register
with a totals row. Filtering and presentation run through the shared
:mod:`app.reports.framework`.
"""

from __future__ import annotations

import datetime

import db
from app import modules
from app.reports.framework import ReportParam, ReportSpec, ReportView

COLUMNS = ["billno", "tdate", "salestype", "custname", "taxable",
           "cgst", "sgst", "igst", "roundoff", "total"]


def _run(values: dict):
    d1 = values.get("rdate1") or "1900-01-01"
    d2 = values.get("rdate2") or str(datetime.date.today())
    btype = (values.get("billtype") or "All").strip()

    sql = ("SELECT billno, tdate, salestype, custname, taxable, cgst, sgst, "
           "igst, roundoff, total FROM salesm WHERE tdate BETWEEN ? AND ?")
    params = [d1, d2]
    if btype in ("S", "E"):
        sql += " AND salestype = ?"
        params.append(btype)
    sql += " ORDER BY billno"

    try:
        rows = db.fetch_all(sql, tuple(params))
    except Exception:
        rows = []

    # Totals row.
    if rows:
        total = {c: "" for c in COLUMNS}
        total["billno"] = "TOTAL"
        for c in ("taxable", "cgst", "sgst", "igst", "roundoff", "total"):
            total[c] = round(sum(float(r.get(c) or 0) for r in rows), 2)
        rows = list(rows) + [total]
    return COLUMNS, rows


SPEC = ReportSpec(
    title="Sales Register",
    params=[
        ReportParam("rdate1", "From", "date"),
        ReportParam("rdate2", "To", "date"),
        ReportParam("billtype", "Type", "choice", default="All",
                    options=["All", "S", "E"]),
    ],
    run=_run,
)


def _factory(window):
    return ReportView(SPEC)


modules.register("w_saleregister")(_factory)
