"""
Persistence for the Goldsmith / Jewellery weight transaction.

Header -> ``smithm`` and lines -> ``smithd`` (original GMINE tables; ``smithd``
columns follow ``w_gsmith.srw``). Goldsmith list comes from the smith master.
The fine-weight balance for a smith is derived from ``smithd`` (given − received
touch weight). Portable SQL; SQLite test engine creates the tables on demand.
"""

from __future__ import annotations

import datetime

import db
from app.services.goldsmith_service import SmithLine, GIVEN, RECEIVED

_SQLITE_DDL = [
    """CREATE TABLE IF NOT EXISTS smithm (
        billno TEXT PRIMARY KEY, tdate TEXT, smithcode TEXT, smithname TEXT,
        givrec TEXT, control TEXT, status TEXT DEFAULT 'O')""",
    """CREATE TABLE IF NOT EXISTS smithd (
        billno TEXT, sno INTEGER, code TEXT, name TEXT, qty REAL, weight REAL,
        stonewgt REAL, netwgt REAL, touch REAL, touchwgt REAL, mcharge REAL,
        givrec TEXT)""",
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
    key = f"SMITHLEN_{givrec}"
    prefix = "GS" if givrec == GIVEN else "RS"
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


def list_smiths() -> list[dict]:
    for sql in ("SELECT code, name FROM smith_master ORDER BY name",
                "SELECT code, name FROM clientsgs ORDER BY code"):
        try:
            rows = db.fetch_all(sql)
            if rows:
                return rows
        except Exception:
            continue
    return []


def fine_balance(smithcode: str):
    """Outstanding fine weight with a smith = given − received touch weight."""
    try:
        row = db.fetch_one(
            "SELECT "
            "COALESCE(SUM(CASE WHEN d.givrec='G' THEN d.touchwgt ELSE 0 END),0) AS given, "
            "COALESCE(SUM(CASE WHEN d.givrec='R' THEN d.touchwgt ELSE 0 END),0) AS recd "
            "FROM smithd d JOIN smithm m ON m.billno = d.billno "
            "WHERE m.smithcode = ?", (smithcode,))
        if row:
            return round(float(row["given"]) - float(row["recd"]), 3)
    except Exception:
        pass
    return 0.0


def save_memo(header: dict, lines: list[SmithLine]) -> str:
    ensure_schema()
    billno = header["billno"]
    givrec = header.get("givrec", GIVEN)
    db.execute("DELETE FROM smithd WHERE billno = ?", (billno,))
    db.execute("DELETE FROM smithm WHERE billno = ?", (billno,))
    db.execute(
        """INSERT INTO smithm (billno, tdate, smithcode, smithname, givrec,
           control, status) VALUES (?,?,?,?,?,?,?)""",
        (billno, header.get("tdate", str(datetime.date.today())),
         header.get("smithcode", ""), header.get("smithname", ""), givrec,
         header.get("control", "GS"), "O"))
    for i, ln in enumerate(lines, start=1):
        ln.compute()
        db.execute(
            """INSERT INTO smithd (billno, sno, code, name, qty, weight,
               stonewgt, netwgt, touch, touchwgt, mcharge, givrec)
               VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""",
            (billno, i, ln.code, ln.name, float(ln.qty), float(ln.weight),
             float(ln.stone_wgt), float(ln.net_wgt), float(ln.touch),
             float(ln.touch_wgt), float(ln.making), givrec))
    return billno


def load_memo(billno: str):
    head = db.fetch_one("SELECT * FROM smithm WHERE billno = ?", (billno,))
    if not head:
        return None, []
    rows = db.fetch_all("SELECT * FROM smithd WHERE billno = ? ORDER BY sno", (billno,))
    lines = [SmithLine(
        code=r["code"], name=r["name"], qty=r["qty"], weight=r["weight"],
        stone_wgt=r["stonewgt"], touch=r["touch"], making=r["mcharge"]).compute()
        for r in rows]
    return head, lines
