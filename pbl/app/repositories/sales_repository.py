"""
Persistence for the Sales billing module.

Header is stored in ``salesm`` and lines in ``salesd`` (the original GMINE
tables; ``salesd`` columns match the PowerBuilder ``insert into salesd`` in
``w_sales.srw``). The SQL is portable across SQL Anywhere / SQL Server / SQLite.

On the bundled SQLite test engine the tables are created on demand so the module
is runnable end-to-end without the production database. Against the production
SQL Anywhere database these tables already exist.

Note: the full GMINE sale also posts to the accounting subsystem (daybook,
pdclist, stkandprofit, …). That general-ledger posting is a further increment;
this repository saves the bill header + lines and totals faithfully.
"""

from __future__ import annotations

import datetime

import db
from app.services.sales_service import SalesLine

_SQLITE_DDL = [
    """CREATE TABLE IF NOT EXISTS salesm (
        billno TEXT PRIMARY KEY, tdate TEXT, salestype TEXT,
        custcode TEXT, custname TEXT, taxperc REAL DEFAULT 0,
        interstate TEXT DEFAULT 'N', gross REAL DEFAULT 0, taxable REAL DEFAULT 0,
        cgst REAL DEFAULT 0, sgst REAL DEFAULT 0, igst REAL DEFAULT 0,
        roundoff REAL DEFAULT 0, total REAL DEFAULT 0)""",
    """CREATE TABLE IF NOT EXISTS salesd (
        billno TEXT, sno INTEGER, code TEXT, name TEXT, qty REAL, weight REAL,
        stonewgt REAL, stoneprice REAL, mcharge REAL, wastage REAL, rate REAL,
        amount REAL)""",
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


def next_billno(salestype: str = "S") -> str:
    """Next bill number: ``salestype`` prefix + zero-padded running counter.

    Mirrors the spirit of the PB scheme (prefix + a counter held in ``generali``).
    """
    ensure_schema()
    key = f"SBLEN_{salestype}"
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
    return f"{salestype}{nxt:06d}"


def list_customers() -> list[dict]:
    for sql in ("SELECT code, name FROM customer_master ORDER BY name",
                "SELECT code, name FROM clients ORDER BY name"):
        try:
            rows = db.fetch_all(sql)
            if rows:
                return rows
        except Exception:
            continue
    return []


def list_items() -> list[dict]:
    for sql in ("SELECT code, name, rate FROM item_master ORDER BY name",
                "SELECT code, name, 0 AS rate FROM itemm ORDER BY name"):
        try:
            rows = db.fetch_all(sql)
            if rows:
                return rows
        except Exception:
            continue
    return []


def save_bill(header: dict, lines: list[SalesLine]) -> str:
    ensure_schema()
    billno = header["billno"]
    # Replace any existing rows for an idempotent re-save.
    db.execute("DELETE FROM salesd WHERE billno = ?", (billno,))
    db.execute("DELETE FROM salesm WHERE billno = ?", (billno,))
    db.execute(
        """INSERT INTO salesm
           (billno, tdate, salestype, custcode, custname, taxperc, interstate,
            gross, taxable, cgst, sgst, igst, roundoff, total)
           VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
        (billno, header.get("tdate", str(datetime.date.today())),
         header.get("salestype", "S"), header.get("custcode", ""),
         header.get("custname", ""), float(header.get("taxperc", 0)),
         "Y" if header.get("interstate") else "N",
         float(header["gross"]), float(header["taxable"]), float(header["cgst"]),
         float(header["sgst"]), float(header["igst"]), float(header["roundoff"]),
         float(header["total"])))
    for i, ln in enumerate(lines, start=1):
        ln.compute()
        db.execute(
            """INSERT INTO salesd
               (billno, sno, code, name, qty, weight, stonewgt, stoneprice,
                mcharge, wastage, rate, amount)
               VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""",
            (billno, i, ln.code, ln.name, float(ln.qty), float(ln.weight),
             float(ln.stone_wgt), float(ln.stone_price), float(ln.making),
             float(ln.wastage), float(ln.rate), float(ln.amount)))
    return billno


def load_bill(billno: str):
    head = db.fetch_one("SELECT * FROM salesm WHERE billno = ?", (billno,))
    if not head:
        return None, []
    rows = db.fetch_all("SELECT * FROM salesd WHERE billno = ? ORDER BY sno", (billno,))
    lines = [SalesLine(
        code=r["code"], name=r["name"], qty=r["qty"], weight=r["weight"],
        stone_wgt=r["stonewgt"], stone_price=r["stoneprice"], wastage=r["wastage"],
        making=r["mcharge"], rate=r["rate"]).compute() for r in rows]
    return head, lines
