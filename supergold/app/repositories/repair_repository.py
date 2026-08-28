"""
Persistence for the Repair / Remake memo module.

Header -> ``repairm`` and lines -> ``repaird`` (original GMINE tables; columns
follow ``w_reprenter.srw``). Customer lookup shared with sales. Portable SQL;
SQLite test engine creates tables on demand.
"""

from __future__ import annotations

import datetime

import db
from app.services.repair_service import RepairLine
from app.repositories.sales_repository import list_customers  # noqa: F401

_SQLITE_DDL = [
    """CREATE TABLE IF NOT EXISTS repairm (
        billno TEXT PRIMARY KEY, tdate TEXT, duedate TEXT, custcode TEXT,
        custname TEXT, givrec TEXT, control TEXT, status TEXT DEFAULT 'O',
        sman TEXT, addr TEXT)""",
    """CREATE TABLE IF NOT EXISTS repaird (
        billno TEXT, sno INTEGER, code TEXT, name TEXT, qty REAL, weight REAL,
        stonewgt REAL, netwgt REAL, complaint TEXT, givrec TEXT, purity TEXT,
        stktype TEXT, cost REAL)""",
    """CREATE TABLE IF NOT EXISTS generali (code TEXT PRIMARY KEY, cvalue REAL)""",
]


def ensure_schema():
    if db.ENGINE != "sqlite":
        return
    conn = db.get_connection()
    try:
        for ddl in _SQLITE_DDL:
            conn.execute(ddl)
        conn.commit()
    finally:
        conn.close()


def next_memono(givrec: str) -> str:
    ensure_schema()
    key = f"REPRLEN_{givrec}"
    prefix = "RR" if givrec == "R" else "RI"
    row = None
    try:
        row = db.fetch_one("SELECT cvalue FROM generali WHERE code = ?", (key,))
    except Exception:
        pass
    nxt = int((row or {}).get("cvalue") or 0) + 1
    try:
        if row:
            db.execute("UPDATE generali SET cvalue = ? WHERE code = ?", (nxt, key))
        else:
            db.execute("INSERT INTO generali (code, cvalue) VALUES (?, ?)", (key, nxt))
    except Exception:
        pass
    return f"{prefix}{nxt:06d}"


def save_memo(header: dict, lines: list[RepairLine]) -> str:
    ensure_schema()
    billno = header["billno"]
    givrec = header.get("givrec", "R")
    db.execute("DELETE FROM repaird WHERE billno = ?", (billno,))
    db.execute("DELETE FROM repairm WHERE billno = ?", (billno,))
    db.execute(
        """INSERT INTO repairm
           (billno, tdate, duedate, custcode, custname, givrec, control,
            status, sman, addr)
           VALUES (?,?,?,?,?,?,?,?,?,?)""",
        (billno, header.get("tdate", str(datetime.date.today())),
         header.get("duedate", ""), header.get("custcode", ""),
         header.get("custname", ""), givrec, header.get("control", "RPR"),
         "O", header.get("sman", ""), header.get("addr", "")))
    for i, ln in enumerate(lines, start=1):
        ln.compute()
        db.execute(
            """INSERT INTO repaird
               (billno, sno, code, name, qty, weight, stonewgt, netwgt,
                complaint, givrec, purity, stktype, cost)
               VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (billno, i, ln.code, ln.name, float(ln.qty), float(ln.weight),
             float(ln.stone_wgt), float(ln.net_wgt), ln.complaint, givrec,
             ln.purity, ln.stktype, float(ln.cost)))
    return billno


def load_memo(billno: str):
    head = db.fetch_one("SELECT * FROM repairm WHERE billno = ?", (billno,))
    if not head:
        return None, []
    rows = db.fetch_all("SELECT * FROM repaird WHERE billno = ? ORDER BY sno", (billno,))
    lines = [RepairLine(
        code=r["code"], name=r["name"], qty=r["qty"], weight=r["weight"],
        stone_wgt=r["stonewgt"], complaint=r["complaint"] or "",
        purity=r["purity"] or "", stktype=r["stktype"] or "",
        cost=r["cost"] or 0).compute() for r in rows]
    return head, lines
