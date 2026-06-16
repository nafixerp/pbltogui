"""
Persistence for the Order module.

Header -> ``orderm`` and lines -> ``orderd`` (original GMINE tables; ``orderd``
columns follow ``w_order.srw``). Customer lookup is shared with the sales
repository. Portable SQL; SQLite test engine creates the tables on demand.
"""

from __future__ import annotations

import datetime

import db
from app.services.order_service import OrderLine
from app.repositories.sales_repository import list_customers, list_items  # noqa: F401

_SQLITE_DDL = [
    """CREATE TABLE IF NOT EXISTS orderm (
        ordno TEXT PRIMARY KEY, tdate TEXT, duedate TEXT, custcode TEXT,
        custname TEXT, rate REAL DEFAULT 0, billamt REAL DEFAULT 0,
        eamt REAL DEFAULT 0, advance REAL DEFAULT 0, balance REAL DEFAULT 0,
        taxperc REAL DEFAULT 0, interstate TEXT DEFAULT 'N',
        status TEXT DEFAULT 'O', closed TEXT DEFAULT 'N')""",
    """CREATE TABLE IF NOT EXISTS orderd (
        ordno TEXT, sno INTEGER, code TEXT, name TEXT, qty REAL, weight REAL,
        stonewgt REAL, stoneprice REAL, mcharge REAL, wastage REAL, rate REAL,
        amount REAL, stage TEXT)""",
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


def next_ordno(prefix: str = "O") -> str:
    ensure_schema()
    key = "ORDLEN"
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


def save_order(header: dict, lines: list[OrderLine]) -> str:
    ensure_schema()
    ordno = header["ordno"]
    db.execute("DELETE FROM orderd WHERE ordno = ?", (ordno,))
    db.execute("DELETE FROM orderm WHERE ordno = ?", (ordno,))
    db.execute(
        """INSERT INTO orderm
           (ordno, tdate, duedate, custcode, custname, billamt, eamt, advance,
            balance, taxperc, interstate, status, closed)
           VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)""",
        (ordno, header.get("tdate", str(datetime.date.today())),
         header.get("duedate", ""), header.get("custcode", ""),
         header.get("custname", ""), float(header["billamt"]),
         float(header.get("exchange", 0)), float(header["advance"]),
         float(header["balance"]), float(header.get("taxperc", 0)),
         "Y" if header.get("interstate") else "N", "O", "N"))
    for i, ln in enumerate(lines, start=1):
        ln.compute()
        db.execute(
            """INSERT INTO orderd
               (ordno, sno, code, name, qty, weight, stonewgt, stoneprice,
                mcharge, wastage, rate, amount, stage)
               VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (ordno, i, ln.code, ln.name, float(ln.qty), float(ln.weight),
             float(ln.stone_wgt), float(ln.stone_price), float(ln.making),
             float(ln.wastage), float(ln.rate), float(ln.amount), "NEW"))
    return ordno


def load_order(ordno: str):
    head = db.fetch_one("SELECT * FROM orderm WHERE ordno = ?", (ordno,))
    if not head:
        return None, []
    rows = db.fetch_all("SELECT * FROM orderd WHERE ordno = ? ORDER BY sno", (ordno,))
    lines = [OrderLine(
        code=r["code"], name=r["name"], qty=r["qty"], weight=r["weight"],
        stone_wgt=r["stonewgt"], stone_price=r["stoneprice"], wastage=r["wastage"],
        making=r["mcharge"], rate=r["rate"]).compute() for r in rows]
    return head, lines
