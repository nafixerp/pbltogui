"""
Stock Register report — conversion of GMINE ``w_stockregister`` /
``d_stockregister``.

For each item it shows the opening balance (movements before the From date),
inward and outward weight/qty within the range, and the closing balance, from
the ``stockledger`` the Sales/Purchase modules post to. Shared framework.
"""

from __future__ import annotations

import datetime

import db
from app import modules
from app.reports.framework import ReportParam, ReportSpec, ReportView

COLUMNS = ["code", "name", "op_wt", "in_wt", "out_wt", "cl_wt",
           "in_qty", "out_qty"]


def _run(values: dict):
    d1 = values.get("rdate1") or "1900-01-01"
    d2 = values.get("rdate2") or str(datetime.date.today())

    try:
        codes = db.fetch_all(
            "SELECT DISTINCT code, name FROM stockledger ORDER BY code")
    except Exception:
        codes = []

    out = []
    t_op = t_in = t_out = 0.0
    for c in codes:
        code = c["code"]

        def agg(where, params):
            r = db.fetch_one(
                "SELECT "
                "COALESCE(SUM(CASE WHEN direction='IN' THEN weight ELSE -weight END),0) AS net_wt, "
                "COALESCE(SUM(CASE WHEN direction='IN' THEN weight ELSE 0 END),0) AS in_wt, "
                "COALESCE(SUM(CASE WHEN direction='OUT' THEN weight ELSE 0 END),0) AS out_wt, "
                "COALESCE(SUM(CASE WHEN direction='IN' THEN qty ELSE 0 END),0) AS in_qty, "
                "COALESCE(SUM(CASE WHEN direction='OUT' THEN qty ELSE 0 END),0) AS out_qty "
                f"FROM stockledger WHERE code = ? AND {where}", (code, *params))
            return r or {}

        opening = agg("tdate < ?", (d1,)).get("net_wt", 0) or 0
        period = agg("tdate BETWEEN ? AND ?", (d1, d2))
        in_wt = period.get("in_wt", 0) or 0
        out_wt = period.get("out_wt", 0) or 0
        closing = round(float(opening) + float(in_wt) - float(out_wt), 3)
        t_op += float(opening); t_in += float(in_wt); t_out += float(out_wt)
        out.append({
            "code": code, "name": c.get("name") or "",
            "op_wt": round(float(opening), 3), "in_wt": round(float(in_wt), 3),
            "out_wt": round(float(out_wt), 3), "cl_wt": closing,
            "in_qty": period.get("in_qty", 0) or 0,
            "out_qty": period.get("out_qty", 0) or 0,
        })
    if out:
        out.append({"code": "TOTAL", "name": "", "op_wt": round(t_op, 3),
                    "in_wt": round(t_in, 3), "out_wt": round(t_out, 3),
                    "cl_wt": round(t_op + t_in - t_out, 3),
                    "in_qty": "", "out_qty": ""})
    return COLUMNS, out


SPEC = ReportSpec(
    title="Stock Register",
    params=[ReportParam("rdate1", "From", "date"),
            ReportParam("rdate2", "To", "date")],
    run=_run,
)


def _factory(window):
    return ReportView(SPEC)


modules.register("w_stockregister")(_factory)
