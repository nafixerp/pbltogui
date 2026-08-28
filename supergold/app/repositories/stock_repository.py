"""
Stock persistence and movement posting.

Maintains the GMINE-style running stock balance in ``items`` (qty / weight /
stonewgt per item code) and a ``stockledger`` of every inward / outward movement
so the Stock Register can show opening, inward, outward and closing per item.

Posting a document is idempotent: re-posting the same ``docno`` first reverses
its previous ledger rows against the running balance, then applies the new ones,
so a bill re-save never double-counts stock.
"""

from __future__ import annotations

import datetime

import db
from app.services.stock_service import StockMovement, INWARD, OUTWARD

_SQLITE_DDL = [
    """CREATE TABLE IF NOT EXISTS items (
        code TEXT PRIMARY KEY, name TEXT, qty REAL DEFAULT 0,
        weight REAL DEFAULT 0, stonewgt REAL DEFAULT 0, cost REAL DEFAULT 0)""",
    """CREATE TABLE IF NOT EXISTS stockledger (
        id INTEGER PRIMARY KEY AUTOINCREMENT, tdate TEXT, code TEXT, name TEXT,
        ttype TEXT, direction TEXT, qty REAL, weight REAL, stonewgt REAL,
        docno TEXT)""",
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


def _apply(code: str, name: str, sign: int, qty, weight, stonewgt):
    """Add (sign +1) or reverse (sign -1) a quantity to the running balance."""
    row = db.fetch_one("SELECT code FROM items WHERE code = ?", (code,))
    if not row:
        db.execute("INSERT INTO items (code, name, qty, weight, stonewgt) "
                   "VALUES (?,?,0,0,0)", (code, name))
    db.execute(
        "UPDATE items SET qty = qty + ?, weight = weight + ?, "
        "stonewgt = stonewgt + ?, name = COALESCE(NULLIF(name,''), ?) "
        "WHERE code = ?",
        (sign * float(qty), sign * float(weight), sign * float(stonewgt),
         name, code))


def post_document(docno: str, ttype: str, direction: str, tdate: str, lines):
    """Post all stock movements for a document (idempotent by ``docno``)."""
    ensure_schema()
    tdate = tdate or str(datetime.date.today())

    # Reverse and remove any previous ledger rows for this document.
    prev = db.fetch_all(
        "SELECT code, name, direction, qty, weight, stonewgt FROM stockledger "
        "WHERE docno = ?", (docno,))
    for p in prev:
        sign = 1 if p["direction"] == INWARD else -1
        _apply(p["code"], p["name"] or "", -sign, p["qty"], p["weight"],
               p["stonewgt"])
    db.execute("DELETE FROM stockledger WHERE docno = ?", (docno,))

    # Apply the new movements.
    sign = 1 if direction == INWARD else -1
    for ln in lines:
        code = (getattr(ln, "code", "") or "").strip()
        if not code:
            continue
        qty = float(getattr(ln, "qty", 0) or 0)
        weight = float(getattr(ln, "weight", 0) or 0)
        stonewgt = float(getattr(ln, "stone_wgt", 0) or 0)
        name = getattr(ln, "name", "") or ""
        db.execute(
            "INSERT INTO stockledger (tdate, code, name, ttype, direction, qty, "
            "weight, stonewgt, docno) VALUES (?,?,?,?,?,?,?,?,?)",
            (tdate, code, name, ttype, direction, qty, weight, stonewgt, docno))
        _apply(code, name, sign, qty, weight, stonewgt)


def remove_document(docno: str):
    """Reverse and delete all stock movements for a document."""
    ensure_schema()
    prev = db.fetch_all(
        "SELECT code, name, direction, qty, weight, stonewgt FROM stockledger "
        "WHERE docno = ?", (docno,))
    for p in prev:
        sign = 1 if p["direction"] == INWARD else -1
        _apply(p["code"], p["name"] or "", -sign, p["qty"], p["weight"],
               p["stonewgt"])
    db.execute("DELETE FROM stockledger WHERE docno = ?", (docno,))


def current_stock() -> list[dict]:
    try:
        return db.fetch_all(
            "SELECT code, name, qty, weight, stonewgt FROM items ORDER BY code")
    except Exception:
        return []
