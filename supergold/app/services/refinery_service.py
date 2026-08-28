"""
Refinery issues and returns  (``w_refnenter``, ``w_refnretdocno``, ``w_refinary``).

Metal is issued to a refiner and comes back refined. The original posts the
movement to stock as it happens, which is what these two routines do — and
exactly what ``w_refncancel`` reverses:

* **issue** — the metal leaves the shop: ``items`` (and ``itemsstk``) lose the
  issued quantity, weight and stone weight;
* **receive** — the refined metal comes back in, and the bottle stock and test
  pieces the refiner reports are added too.

Both write the ``refinerym`` header and ``refineryd`` detail rows the reports
and the cancel screen read.
"""

from __future__ import annotations

import datetime

import db
from app.services.cancel_service import adjust_stock


def _next(table: str, column: str = "slno") -> int:
    try:
        row = db.fetch_one(f"SELECT COALESCE(MAX({column}),0) + 1 AS n FROM {table}")
        return int(float(row["n"])) if row else 1
    except Exception:
        return 1


def _insert(table: str, values: dict):
    columns = {c["name"].lower() for c in db.table_columns(table)}
    usable = {k: v for k, v in values.items() if k in columns}
    if not usable:
        raise ValueError(f"Table '{table}' is not in this database")
    db.execute(f"INSERT INTO {table} ({', '.join(usable)}) "
               f"VALUES ({', '.join('?' for _ in usable)})", list(usable.values()))


def issue(refiner: str, lines: list, *, docno: str = "", tdate=None, control=1,
          note: str = "") -> int:
    """Issue metal to a refiner. ``lines`` are ``{code, qty, weight, stonewgt}``."""
    lines = [l for l in lines if str(l.get("code") or "").strip()]
    if not (refiner or "").strip():
        raise ValueError("Choose the refiner")
    if not lines:
        raise ValueError("Add at least one item to issue")

    tdate = tdate or datetime.date.today().isoformat()
    slno = _next("refinerym")
    docno = docno or f"RF{slno}"
    total = sum(float(l.get("weight") or 0) for l in lines)

    with db.transaction():
        _insert("refinerym", {"slno": slno, "docno": docno, "tdate": tdate,
                              "refcode": refiner.strip(), "control": control,
                              "status": 0, "issuedwgt": total, "note": note})
        for sno, line in enumerate(lines, start=1):
            code = str(line["code"]).strip()
            _insert("refineryd", {
                "slno": slno, "sno": sno, "code": code,
                "issuedqty": line.get("qty") or 0,
                "issuedwgt": line.get("weight") or 0,
                "issuedstwgt": line.get("stonewgt") or 0,
                "stktype": line.get("stktype") or "", "status": 0})
            adjust_stock(code, line.get("stktype") or "", control,
                         qty=line.get("qty"), weight=line.get("weight"),
                         stonewgt=line.get("stonewgt"), sign=-1)
    return slno


def receive(issue_slno, lines: list, *, docno: str = "", tdate=None,
            control=1) -> int:
    """Take refined metal back in against an issue."""
    head = db.fetch_one("SELECT * FROM refinerym WHERE slno = ?", (issue_slno,))
    if head is None:
        raise ValueError(f"Issue {issue_slno} does not exist")
    lines = [l for l in lines if str(l.get("code") or "").strip()]
    if not lines:
        raise ValueError("Enter what came back")

    tdate = tdate or datetime.date.today().isoformat()
    slno = _next("refinerym")
    docno = docno or f"RR{slno}"
    total = sum(float(l.get("weight") or 0) for l in lines)

    with db.transaction():
        _insert("refinerym", {"slno": slno, "docno": docno, "tdate": tdate,
                              "refcode": head.get("refcode"), "control": control,
                              "status": 1, "islno": issue_slno,
                              "rcvdwgt": total})
        for sno, line in enumerate(lines, start=1):
            code = str(line["code"]).strip()
            stktype = line.get("stktype") or ""
            _insert("refineryd", {
                "slno": slno, "sno": sno, "code": code,
                "rcvdqty": line.get("qty") or 0,
                "rcvdwgt": line.get("weight") or 0,
                "bottlestk": line.get("bottlestk") or 0,
                "testpcs": line.get("testpcs") or 0,
                "stktype": stktype, "status": 1})
            adjust_stock(code, stktype, control, qty=line.get("qty"),
                         weight=line.get("weight"), sign=+1)
            for special, weight in (("BS", line.get("bottlestk")),
                                    ("TP", line.get("testpcs"))):
                if float(weight or 0):
                    adjust_stock(special, stktype, control, weight=weight, sign=+1)
        db.execute("UPDATE refinerym SET status = 2 WHERE slno = ?", (issue_slno,))
    return slno


def pending_issues() -> list:
    """Issues that have not been fully taken back yet."""
    try:
        return db.fetch_all(
            "SELECT slno, docno, tdate, refcode, issuedwgt FROM refinerym "
            "WHERE COALESCE(status,0) < 2 AND COALESCE(issuedwgt,0) > 0 "
            "ORDER BY slno DESC")
    except Exception:
        return []
