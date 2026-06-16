"""
Persistence for accounting vouchers (Receipt / Payment / Journal).

Posts balanced rows to ``daybook`` and the narration to ``daybookpart`` — the
original GMINE tables. Account list comes from ``accountm``. Portable across SQL
Anywhere / SQL Server / SQLite; the SQLite test engine creates the tables and a
small chart of accounts on demand.
"""

from __future__ import annotations

import datetime

import db
from app.services.accounting_service import DaybookRow, make_rows

_SQLITE_DDL = [
    """CREATE TABLE IF NOT EXISTS accountm (
        accode TEXT PRIMARY KEY, name TEXT, opbal REAL DEFAULT 0,
        actype1 TEXT, actype2 TEXT, grcode TEXT)""",
    """CREATE TABLE IF NOT EXISTS daybook (
        slno INTEGER, tdate TEXT, accode TEXT, amount REAL, control TEXT,
        opaccode TEXT, refno TEXT)""",
    """CREATE TABLE IF NOT EXISTS daybookpart (
        slno INTEGER, particular TEXT, vchno TEXT, control TEXT)""",
    """CREATE TABLE IF NOT EXISTS generali (code TEXT PRIMARY KEY, cvalue REAL)""",
]

_SEED_ACCOUNTS = [
    ("CASH", "Cash in Hand", "A"), ("BANK", "Bank Account", "A"),
    ("SALES", "Sales Account", "I"), ("PURCH", "Purchase Account", "E"),
    ("SUNDRD", "Sundry Debtors", "A"), ("SUNDRC", "Sundry Creditors", "L"),
    ("GSTOUT", "GST Output", "L"), ("GSTIN", "GST Input", "A"),
    ("EXPENS", "General Expenses", "E"), ("CAPITL", "Capital Account", "L"),
    ("ROUNDOFF", "Round Off", "I"),
]


def ensure_schema():
    if db.ENGINE != "sqlite":
        return
    conn = db.get_connection()
    try:
        for ddl in _SQLITE_DDL:
            conn.execute(ddl)
        # Older test DBs may pre-date the refno column; add it if missing.
        cols = {r[1] for r in conn.execute("PRAGMA table_info(daybook)")}
        if "refno" not in cols:
            conn.execute("ALTER TABLE daybook ADD COLUMN refno TEXT")
        conn.commit()
    finally:
        conn.close()
    if not db.fetch_one("SELECT 1 AS x FROM accountm LIMIT 1"):
        for accode, name, actype in _SEED_ACCOUNTS:
            db.execute("INSERT INTO accountm (accode, name, actype1) VALUES (?,?,?)",
                       (accode, name, actype))


def list_accounts() -> list[dict]:
    try:
        rows = db.fetch_all("SELECT accode, name FROM accountm ORDER BY name")
        if rows:
            return rows
    except Exception:
        pass
    return [{"accode": a, "name": n} for a, n, _ in _SEED_ACCOUNTS]


def next_slno() -> int:
    ensure_schema()
    key = "DBSLNO"
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
    return nxt


def post_voucher(tdate: str, debit: str, credit: str, amount, control: str,
                 narration: str = "") -> int:
    """Write a balanced voucher; returns the daybook slno."""
    ensure_schema()
    slno = next_slno()
    rows = make_rows(slno, tdate or str(datetime.date.today()),
                     debit, credit, amount, control)
    _write_rows(rows)
    db.execute("INSERT INTO daybookpart (slno, particular, vchno, control) "
               "VALUES (?,?,?,?)", (slno, narration, str(slno), control))
    return slno


def _write_rows(rows):
    for r in rows:
        db.execute(
            "INSERT INTO daybook (slno, tdate, accode, amount, control, opaccode, "
            "refno) VALUES (?,?,?,?,?,?,?)",
            (r.slno, r.tdate, r.accode, float(r.amount), r.control, r.opaccode,
             getattr(r, "refno", "")))


def post_legs(tdate: str, legs, control: str, refno: str, narration: str = "") -> int:
    """Post a compound (multi-leg) voucher; replaces any prior rows for ``refno``.

    ``legs`` is ``[(accode, signed_amount), ...]`` (debit +, credit −) summing to
    zero. Used by the GL integration for sales/purchase bills so a re-save is
    idempotent. Returns the daybook slno (or 0 if there was nothing to post).
    """
    from app.services.accounting_service import make_multi_rows
    ensure_schema()
    if refno:
        db.execute("DELETE FROM daybook WHERE refno = ?", (refno,))
    rows = make_multi_rows(0, tdate or str(datetime.date.today()),
                           legs, control, refno)
    if not rows:
        return 0
    slno = next_slno()
    for r in rows:
        r.slno = slno
    _write_rows(rows)
    db.execute("INSERT INTO daybookpart (slno, particular, vchno, control) "
               "VALUES (?,?,?,?)", (slno, narration, refno, control))
    return slno


def remove_refno(refno: str):
    """Delete any daybook rows posted for a document reference."""
    try:
        db.execute("DELETE FROM daybook WHERE refno = ?", (refno,))
    except Exception:
        pass


def list_daybook(limit: int = 200) -> list[dict]:
    try:
        return db.fetch_all(
            "SELECT slno, tdate, accode, amount, control, opaccode "
            "FROM daybook ORDER BY slno DESC, amount DESC")[:limit]
    except Exception:
        return []


def account_balance(accode: str):
    try:
        row = db.fetch_one(
            "SELECT COALESCE(SUM(amount),0) AS bal FROM daybook WHERE accode = ?",
            (accode,))
        return row["bal"] if row else 0
    except Exception:
        return 0
