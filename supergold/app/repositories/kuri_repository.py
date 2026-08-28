"""
Persistence for Kuri / Scheme collection.

Collections are recorded in ``kuricolln`` (original GMINE columns) and posted to
the accounting day book (Dr Cash, Cr Kuri liability) keyed by receipt number, so
each collection is a real cash receipt that flows into the Cash Book and Trial
Balance. Member list comes from ``clients_kuridet`` (falling back to the customer
master). Portable SQL; SQLite test engine creates the tables on demand.
"""

from __future__ import annotations

import datetime

import db

_SQLITE_DDL = [
    """CREATE TABLE IF NOT EXISTS kuricolln (
        slno INTEGER, tdate TEXT, code TEXT, amount REAL, control TEXT,
        sno INTEGER, grate REAL, agent TEXT, rcptno TEXT, closed TEXT,
        wgt REAL, docno TEXT, note TEXT)""",
    """CREATE TABLE IF NOT EXISTS clients_kuridet (
        code TEXT PRIMARY KEY, name TEXT, opwgt REAL DEFAULT 0,
        showwgtdet TEXT DEFAULT 'Y')""",
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


def list_members() -> list[dict]:
    for sql in ("SELECT code, name FROM clients_kuridet ORDER BY code",
                "SELECT code, name FROM customer_master ORDER BY name"):
        try:
            rows = db.fetch_all(sql)
            if rows:
                return rows
        except Exception:
            continue
    return []


def is_gold_scheme(code: str) -> bool:
    try:
        row = db.fetch_one("SELECT showwgtdet FROM clients_kuridet WHERE code = ?",
                           (code,))
        if row:
            return str(row.get("showwgtdet") or "Y").upper() == "Y"
    except Exception:
        pass
    return True


def next_installment(code: str) -> int:
    try:
        row = db.fetch_one("SELECT COALESCE(MAX(sno),0) AS m FROM kuricolln "
                           "WHERE code = ?", (code,))
        return int(row["m"]) + 1 if row else 1
    except Exception:
        return 1


def next_rcptno() -> str:
    ensure_schema()
    key = "KURIRCPT"
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
    return f"KC{nxt:06d}"


def save_collection(code: str, name: str, tdate: str, amount, grate, wgt,
                    note: str = "") -> str:
    ensure_schema()
    rcptno = next_rcptno()
    sno = next_installment(code)
    slno = _post_gl(rcptno, tdate, amount, code, name)
    db.execute(
        """INSERT INTO kuricolln (slno, tdate, code, amount, control, sno, grate,
           agent, rcptno, closed, wgt, docno, note)
           VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)""",
        (slno, tdate or str(datetime.date.today()), code, float(amount), "KC",
         sno, float(grate or 0), "", rcptno, "N", float(wgt or 0), rcptno, note))
    return rcptno


def _post_gl(rcptno: str, tdate: str, amount, code: str, name: str) -> int:
    """Dr Cash, Cr Kuri liability for the collection (best-effort)."""
    try:
        from app.repositories import accounting_repository as acc
        legs = [("CASH", float(amount)), ("KURI", -float(amount))]
        return acc.post_legs(tdate, legs, control="KC", refno=f"K:{rcptno}",
                             narration=f"Kuri collection {rcptno} - {name or code}")
    except Exception:
        return 0


def member_ledger(code: str) -> list[dict]:
    try:
        return db.fetch_all(
            "SELECT rcptno, tdate, sno, amount, grate, wgt, note FROM kuricolln "
            "WHERE code = ? ORDER BY sno", (code,))
    except Exception:
        return []
