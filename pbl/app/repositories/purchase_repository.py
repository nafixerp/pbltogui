"""
Persistence for the Purchase billing module.

Header -> ``purchasem`` and lines -> ``purchased`` (the original GMINE tables;
``purchased`` columns follow ``w_purchase.srw``). Portable SQL across SQL
Anywhere / SQL Server / SQLite; the SQLite test engine creates the tables on
demand so the module runs without the production database.

As with sales, the deep general-ledger posting is a later increment; this
repository persists the bill header, lines and totals.
"""

from __future__ import annotations

import datetime

import db
from app.services.purchase_service import PurchaseLine

_SQLITE_DDL = [
    """CREATE TABLE IF NOT EXISTS purchasem (
        docno TEXT PRIMARY KEY, billno TEXT, tdate TEXT, suppcode TEXT,
        name TEXT, taxperc REAL DEFAULT 0, interstate TEXT DEFAULT 'N',
        billamt REAL DEFAULT 0, netamt REAL DEFAULT 0, taxamt REAL DEFAULT 0,
        cgst REAL DEFAULT 0, sgst REAL DEFAULT 0, igst REAL DEFAULT 0,
        round REAL DEFAULT 0, total REAL DEFAULT 0)""",
    """CREATE TABLE IF NOT EXISTS purchased (
        docno TEXT, sno INTEGER, code TEXT, name TEXT, qty REAL, weight REAL,
        stwgt REAL, stprice REAL, mud REAL, lessperc REAL, lesswgt REAL,
        mcharge REAL, rate REAL, amount REAL)""",
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


def next_docno(prefix: str = "P") -> str:
    ensure_schema()
    key = f"PBLEN_{prefix}"
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


def list_suppliers() -> list[dict]:
    for sql in ("SELECT code, name FROM supplier_master ORDER BY name",
                "SELECT code, name FROM clients ORDER BY name"):
        try:
            rows = db.fetch_all(sql)
            if rows:
                return rows
        except Exception:
            continue
    return []


def list_items() -> list[dict]:
    try:
        return db.fetch_all("SELECT code, name, rate FROM item_master ORDER BY name")
    except Exception:
        return []


def save_bill(header: dict, lines: list[PurchaseLine]) -> str:
    ensure_schema()
    docno = header["docno"]
    db.execute("DELETE FROM purchased WHERE docno = ?", (docno,))
    db.execute("DELETE FROM purchasem WHERE docno = ?", (docno,))
    db.execute(
        """INSERT INTO purchasem
           (docno, billno, tdate, suppcode, name, taxperc, interstate,
            billamt, netamt, taxamt, cgst, sgst, igst, round, total)
           VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
        (docno, header.get("billno", ""), header.get("tdate", str(datetime.date.today())),
         header.get("suppcode", ""), header.get("name", ""),
         float(header.get("taxperc", 0)), "Y" if header.get("interstate") else "N",
         float(header["billamt"]), float(header["netamt"]), float(header["taxamt"]),
         float(header["cgst"]), float(header["sgst"]), float(header["igst"]),
         float(header["round"]), float(header["total"])))
    for i, ln in enumerate(lines, start=1):
        ln.compute()
        db.execute(
            """INSERT INTO purchased
               (docno, sno, code, name, qty, weight, stwgt, stprice, mud,
                lessperc, lesswgt, mcharge, rate, amount)
               VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (docno, i, ln.code, ln.name, float(ln.qty), float(ln.weight),
             float(ln.stone_wgt), float(ln.stone_price), float(ln.mud),
             float(ln.less_perc), float(ln.less_wgt), float(ln.making),
             float(ln.rate), float(ln.amount)))
    _post_gl(docno, header)
    _post_stock(docno, header, lines)
    return docno


def _post_stock(docno: str, header: dict, lines):
    """Increase item stock for the purchase (best-effort)."""
    try:
        from app.repositories import stock_repository
        from app.services.stock_service import INWARD
        stock_repository.post_document(docno, "P", INWARD,
                                       header.get("tdate"), lines)
    except Exception:
        pass


def _post_gl(docno: str, header: dict):
    """Post the purchase to the accounting day book (best-effort)."""
    try:
        from types import SimpleNamespace
        from app.services import gl_service
        totals = SimpleNamespace(
            grand_total=header["total"], taxable=header["netamt"],
            cgst=header["cgst"], sgst=header["sgst"], igst=header["igst"],
            round_off=header["round"])
        gl_service.post_purchase(docno, header.get("tdate"), totals)
    except Exception:
        pass  # never block the bill save on GL posting


def load_bill(docno: str):
    head = db.fetch_one("SELECT * FROM purchasem WHERE docno = ?", (docno,))
    if not head:
        return None, []
    rows = db.fetch_all("SELECT * FROM purchased WHERE docno = ? ORDER BY sno", (docno,))
    lines = [PurchaseLine(
        code=r["code"], name=r["name"], qty=r["qty"], weight=r["weight"],
        stone_wgt=r["stwgt"], stone_price=r["stprice"], mud=r.get("mud") or 0,
        less_perc=r["lessperc"], making=r["mcharge"], rate=r["rate"]).compute()
        for r in rows]
    return head, lines
