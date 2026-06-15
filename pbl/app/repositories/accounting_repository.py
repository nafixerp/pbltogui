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
        opaccode TEXT)""",
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
    for r in rows:
        db.execute(
            "INSERT INTO daybook (slno, tdate, accode, amount, control, opaccode) "
            "VALUES (?,?,?,?,?,?)",
            (r.slno, r.tdate, r.accode, float(r.amount), r.control, r.opaccode))
    db.execute("INSERT INTO daybookpart (slno, particular, vchno, control) "
               "VALUES (?,?,?,?)", (slno, narration, str(slno), control))
    return slno


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
