"""
Database layer for the Jewellery ERP.

Dual engine, selected in db_config.ini:

  * sqlserver  -> connects to Microsoft SQL Server through an ODBC DSN
                  (pyodbc). On first run it can auto-create the DSN, create the
                  database (placing the data files in this project folder) and
                  build the schema + seed data.
  * sqlite     -> a local file (jewellery_erp.db) for quick testing, no setup.

The rest of the app only uses the engine-agnostic helpers:
    fetch_all(sql, params) -> list[dict]
    fetch_one(sql, params) -> dict | None
    execute(sql, params)   -> lastrowid (sqlite) / None
    validate_login(user, pwd), init_db()

Placeholders are '?' for both engines, so module SQL stays portable.
"""

import os
import sys
import hashlib
import configparser

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(BASE_DIR, "db_config.ini")
SQLITE_PATH = os.path.join(BASE_DIR, "jewellery_erp.db")


# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

def _load_config():
    cp = configparser.ConfigParser()
    if os.path.exists(CONFIG_PATH):
        cp.read(CONFIG_PATH)
    return cp


_CFG = _load_config()
ENGINE = _CFG.get("database", "engine", fallback="sqlite").strip().lower()


def _ss(key, fallback=""):
    return _CFG.get("sqlserver", key, fallback=fallback).strip()


def _ss_bool(key, fallback=False):
    return _CFG.get("sqlserver", key, fallback="no").strip().lower() in ("yes", "true", "1")


def _sa(key, fallback=""):
    return _CFG.get("sqlanywhere", key, fallback=fallback).strip()


def _sa_bool(key, fallback=False):
    return _CFG.get("sqlanywhere", key, fallback="no").strip().lower() in ("yes", "true", "1")


# ---------------------------------------------------------------------------
# Passwords
# ---------------------------------------------------------------------------

def hash_password(plain: str) -> str:
    return hashlib.sha256(plain.encode("utf-8")).hexdigest()


# ---------------------------------------------------------------------------
# Connections
# ---------------------------------------------------------------------------

def get_connection():
    """Return a live DB-API connection for the configured engine."""
    if ENGINE == "sqlite":
        import sqlite3
        conn = sqlite3.connect(SQLITE_PATH)
        conn.execute("PRAGMA foreign_keys = ON;")
        return conn

    # ODBC-based engines.
    import pyodbc

    if ENGINE == "sqlanywhere":
        uid = _sa("uid") or _ss("uid")
        pwd = _sa("pwd") or _ss("pwd")
        if _sa_bool("connect_running", False):
            # Mode 2: attach to an already-running server (no file start).
            parts = [f"DRIVER={{{_sa('driver', 'SQL Anywhere 17')}}}"]
            if _sa("server"):
                parts.append(f"ServerName={_sa('server')}")
            if _sa("database"):
                parts.append(f"DatabaseName={_sa('database')}")
            if uid:
                parts.append(f"UID={uid}")
            if pwd:
                parts.append(f"PWD={pwd}")
            return pyodbc.connect(";".join(parts) + ";")
        if _sa("dbf"):
            # Mode 1: open the database FILE with the v17 driver (recommended).
            # Mirrors connectdbf.srf: DBF + Autostop + UID/PWD.
            # 'Start' forces the v17 engine so an older default engine isn't used
            # (that is what caused the -1005 "different version" error).
            parts = [f"DRIVER={{{_sa('driver', 'SQL Anywhere 17')}}}",
                     f"DBF={_sa('dbf')}", "Autostop=yes"]
            if _sa("start"):
                parts.append(f"Start={_sa('start')}")
            if _sa("server"):
                parts.append(f"ServerName={_sa('server')}")
            if uid:
                parts.append(f"UID={uid}")
            if pwd:
                parts.append(f"PWD={pwd}")
            return pyodbc.connect(";".join(parts) + ";")
        # Fallback: connect through the DSN (uses the DSN's bound driver).
        parts = [f"DSN={_ss('dsn', '')}"]
        if uid:
            parts.append(f"UID={uid}")
        if pwd:
            parts.append(f"PWD={pwd}")
        return pyodbc.connect(";".join(parts) + ";")

    # sqlserver / other DSN-based databases.
    parts = [f"DSN={_ss('dsn', '')}"]
    if _ss_bool("trusted_connection", False):
        parts.append("Trusted_Connection=yes")
    else:
        uid, pwd = _ss("uid"), _ss("pwd")
        if uid:
            parts.append(f"UID={uid}")
        if pwd:
            parts.append(f"PWD={pwd}")
    try:
        return pyodbc.connect(";".join(parts) + ";")
    except pyodbc.Error:
        if ENGINE == "sqlserver":
            # DSN missing/unusable -> try a DSN-less SQL Server connection.
            return pyodbc.connect(_connstr_dsnless(_ss("database", "JewelleryERP")))
        raise


def _connstr_dsnless(database):
    """DSN-less connection string used for setup (create DB) operations."""
    driver = _ss("driver", "ODBC Driver 17 for SQL Server")
    server = _ss("server", "localhost")
    parts = [f"DRIVER={{{driver}}}", f"SERVER={server}", f"DATABASE={database}"]
    if _ss_bool("trusted_connection", True):
        parts.append("Trusted_Connection=yes")
    else:
        parts.append(f"UID={_ss('uid')}")
        parts.append(f"PWD={_ss('pwd')}")
    if "18" in driver:
        parts.append(f"Encrypt={'yes' if _ss_bool('encrypt', False) else 'no'}")
        parts.append("TrustServerCertificate=yes")
    return ";".join(parts) + ";"


# ---------------------------------------------------------------------------
# Engine-agnostic data helpers
# ---------------------------------------------------------------------------

def fetch_all(sql, params=()):
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(sql, params)
        cols = [d[0] for d in cur.description]
        return [dict(zip(cols, row)) for row in cur.fetchall()]
    finally:
        conn.close()


def fetch_one(sql, params=()):
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(sql, params)
        cols = [d[0] for d in cur.description]
        row = cur.fetchone()
        return dict(zip(cols, row)) if row else None
    finally:
        conn.close()


def execute(sql, params=()):
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(sql, params)
        conn.commit()
        try:
            return cur.lastrowid           # sqlite
        except Exception:
            return None
    finally:
        conn.close()


# ---------------------------------------------------------------------------
# Schema introspection (used by the generic CRUD screens)
# ---------------------------------------------------------------------------

def table_columns(table):
    """Return ``[{name, type, nullable, pk, autoinc}]`` for ``table``.

    Empty list if the table does not exist or cannot be inspected. Column
    metadata is what lets the generic screens write to a table safely: only
    columns the database really has are ever put into a statement.
    """
    conn = get_connection()
    try:
        cur = conn.cursor()
        if ENGINE == "sqlite":
            cur.execute(f'PRAGMA table_info("{table}")')
            rows = cur.fetchall()
            if not rows:
                return []
            # A single INTEGER PRIMARY KEY column is SQLite's rowid alias.
            pks = [r for r in rows if r[5]]
            autoinc = (len(pks) == 1 and str(pks[0][2]).upper().startswith("INT"))
            return [{"name": r[1], "type": (r[2] or "").upper(),
                     "nullable": not r[3], "pk": bool(r[5]),
                     "autoinc": bool(r[5]) and autoinc}
                    for r in rows]

        # ODBC engines (SQL Anywhere / SQL Server).
        pk_names = set()
        try:
            pk_names = {r.column_name.lower() for r in cur.primaryKeys(table=table)}
        except Exception:
            pass
        cols = []
        try:
            for r in cur.columns(table=table):
                cols.append({"name": r.column_name,
                             "type": str(r.type_name).upper(),
                             "nullable": bool(getattr(r, "nullable", 1)),
                             "pk": r.column_name.lower() in pk_names,
                             "autoinc": False})
        except Exception:
            cols = []
        if not cols:
            # Last resort: describe an empty result set.
            cur.execute(f"SELECT * FROM {table} WHERE 1 = 0")
            cols = [{"name": d[0], "type": "", "nullable": True,
                     "pk": d[0].lower() in pk_names, "autoinc": False}
                    for d in (cur.description or [])]
        return cols
    except Exception:
        return []
    finally:
        try:
            conn.close()
        except Exception:
            pass


def primary_key(table):
    """Primary-key column names of ``table`` (empty when it has none)."""
    return [c["name"] for c in table_columns(table) if c["pk"]]


def validate_login(password: str):
    """
    Port of w_passverify (gmine). The user enters a PASSWORD only; it is
    encrypted with fpencrypt and matched against userm.pcode.

    Returns a dict {code, name} on success, else None.
    If no users exist at all, access is granted (matches the PB behaviour).
    """
    from pb_compat import fpencrypt
    enc = fpencrypt(password, 1)
    try:
        row = fetch_one("SELECT code, name FROM userm WHERE pcode = ?", (enc,))
    except Exception:
        row = None
    if row:
        return row
    try:
        cnt = fetch_one("SELECT COUNT(code) AS c FROM userm")
        if cnt and (cnt.get("c") or 0) == 0:
            return {"code": "", "name": "ADMIN"}
    except Exception:
        pass
    return None


def write_login_history(code: str):
    """Port of the userhist insert in w_passverify (best-effort)."""
    import datetime
    try:
        execute("INSERT INTO userhist (code, tdate, time1) VALUES (?,?,?)",
                (code, datetime.date.today(),
                 datetime.datetime.now().strftime("%H:%M:%S")))
    except Exception:
        pass


def get_denied_menuitems(code: str):
    """Per-user disabled menu items from userd (classname strings)."""
    try:
        rows = fetch_all("SELECT menuitem FROM userd WHERE code = ?", (code,))
        return {r["menuitem"] for r in rows}
    except Exception:
        return set()


# ---------------------------------------------------------------------------
# Schema definitions
# ---------------------------------------------------------------------------

SQLITE_SCHEMA = """
CREATE TABLE IF NOT EXISTS users (
    user_id   INTEGER PRIMARY KEY AUTOINCREMENT,
    username  TEXT NOT NULL UNIQUE, password TEXT NOT NULL,
    full_name TEXT, role TEXT DEFAULT 'USER', active INTEGER DEFAULT 1);
CREATE TABLE IF NOT EXISTS userm (
    code TEXT, name TEXT, pcode TEXT);
CREATE TABLE IF NOT EXISTS userd (
    code TEXT, menuitem TEXT);
CREATE TABLE IF NOT EXISTS userhist (
    code TEXT, tdate DATE, time1 TEXT);
CREATE TABLE IF NOT EXISTS metal_master (
    metal_id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT NOT NULL UNIQUE, name TEXT NOT NULL, active INTEGER DEFAULT 1);
CREATE TABLE IF NOT EXISTS purity_master (
    purity_id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT NOT NULL UNIQUE, name TEXT NOT NULL, metal_id INTEGER,
    purity_value REAL DEFAULT 0, active INTEGER DEFAULT 1);
CREATE TABLE IF NOT EXISTS category_master (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT NOT NULL UNIQUE, name TEXT NOT NULL, active INTEGER DEFAULT 1);
CREATE TABLE IF NOT EXISTS subcategory_master (
    subcategory_id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT NOT NULL UNIQUE, name TEXT NOT NULL, category_id INTEGER,
    active INTEGER DEFAULT 1);
CREATE TABLE IF NOT EXISTS unit_master (
    unit_id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT NOT NULL UNIQUE, name TEXT NOT NULL, active INTEGER DEFAULT 1);
CREATE TABLE IF NOT EXISTS tax_master (
    tax_id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT NOT NULL UNIQUE, name TEXT NOT NULL, rate REAL DEFAULT 0,
    active INTEGER DEFAULT 1);
CREATE TABLE IF NOT EXISTS stone_master (
    stone_id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT NOT NULL UNIQUE, name TEXT NOT NULL, rate REAL DEFAULT 0,
    unit TEXT DEFAULT 'CT', active INTEGER DEFAULT 1);
CREATE TABLE IF NOT EXISTS smith_master (
    smith_id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT NOT NULL UNIQUE, name TEXT NOT NULL, address TEXT, city TEXT,
    phone TEXT, opening_balance REAL DEFAULT 0, active INTEGER DEFAULT 1);
CREATE TABLE IF NOT EXISTS item_master (
    item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT NOT NULL UNIQUE, name TEXT NOT NULL, category_id INTEGER,
    subcategory_id INTEGER, metal_id INTEGER, purity_id INTEGER, hsn TEXT,
    unit TEXT DEFAULT 'GMS', rate REAL DEFAULT 0, active INTEGER DEFAULT 1);
CREATE TABLE IF NOT EXISTS customer_master (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT NOT NULL UNIQUE, name TEXT NOT NULL, address TEXT, city TEXT,
    phone TEXT, email TEXT, gstin TEXT, opening_balance REAL DEFAULT 0,
    active INTEGER DEFAULT 1);
CREATE TABLE IF NOT EXISTS supplier_master (
    supplier_id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT NOT NULL UNIQUE, name TEXT NOT NULL, address TEXT, city TEXT,
    phone TEXT, email TEXT, gstin TEXT, opening_balance REAL DEFAULT 0,
    active INTEGER DEFAULT 1);
"""

# SQL Server: each table guarded so re-runs are safe. IDENTITY for auto PK,
# BIT for flags, NVARCHAR for text, FLOAT for decimals.
SQLSERVER_TABLES = [
    ("users", """CREATE TABLE users (
        user_id INT IDENTITY(1,1) PRIMARY KEY,
        username NVARCHAR(50) NOT NULL UNIQUE, password NVARCHAR(100) NOT NULL,
        full_name NVARCHAR(100), role NVARCHAR(20) DEFAULT 'USER',
        active BIT DEFAULT 1)"""),
    ("userm", """CREATE TABLE userm (
        code NVARCHAR(20), name NVARCHAR(100), pcode NVARCHAR(100))"""),
    ("userd", """CREATE TABLE userd (
        code NVARCHAR(20), menuitem NVARCHAR(100))"""),
    ("userhist", """CREATE TABLE userhist (
        code NVARCHAR(20), tdate DATE, time1 NVARCHAR(20))"""),
    ("metal_master", """CREATE TABLE metal_master (
        metal_id INT IDENTITY(1,1) PRIMARY KEY,
        code NVARCHAR(20) NOT NULL UNIQUE, name NVARCHAR(50) NOT NULL,
        active BIT DEFAULT 1)"""),
    ("purity_master", """CREATE TABLE purity_master (
        purity_id INT IDENTITY(1,1) PRIMARY KEY,
        code NVARCHAR(20) NOT NULL UNIQUE, name NVARCHAR(50) NOT NULL,
        metal_id INT, purity_value FLOAT DEFAULT 0, active BIT DEFAULT 1)"""),
    ("category_master", """CREATE TABLE category_master (
        category_id INT IDENTITY(1,1) PRIMARY KEY,
        code NVARCHAR(20) NOT NULL UNIQUE, name NVARCHAR(50) NOT NULL,
        active BIT DEFAULT 1)"""),
    ("subcategory_master", """CREATE TABLE subcategory_master (
        subcategory_id INT IDENTITY(1,1) PRIMARY KEY,
        code NVARCHAR(20) NOT NULL UNIQUE, name NVARCHAR(50) NOT NULL,
        category_id INT, active BIT DEFAULT 1)"""),
    ("unit_master", """CREATE TABLE unit_master (
        unit_id INT IDENTITY(1,1) PRIMARY KEY,
        code NVARCHAR(20) NOT NULL UNIQUE, name NVARCHAR(50) NOT NULL,
        active BIT DEFAULT 1)"""),
    ("tax_master", """CREATE TABLE tax_master (
        tax_id INT IDENTITY(1,1) PRIMARY KEY,
        code NVARCHAR(20) NOT NULL UNIQUE, name NVARCHAR(50) NOT NULL,
        rate FLOAT DEFAULT 0, active BIT DEFAULT 1)"""),
    ("stone_master", """CREATE TABLE stone_master (
        stone_id INT IDENTITY(1,1) PRIMARY KEY,
        code NVARCHAR(20) NOT NULL UNIQUE, name NVARCHAR(50) NOT NULL,
        rate FLOAT DEFAULT 0, unit NVARCHAR(10) DEFAULT 'CT', active BIT DEFAULT 1)"""),
    ("smith_master", """CREATE TABLE smith_master (
        smith_id INT IDENTITY(1,1) PRIMARY KEY,
        code NVARCHAR(30) NOT NULL UNIQUE, name NVARCHAR(100) NOT NULL,
        address NVARCHAR(200), city NVARCHAR(50), phone NVARCHAR(30),
        opening_balance FLOAT DEFAULT 0, active BIT DEFAULT 1)"""),
    ("item_master", """CREATE TABLE item_master (
        item_id INT IDENTITY(1,1) PRIMARY KEY,
        code NVARCHAR(30) NOT NULL UNIQUE, name NVARCHAR(100) NOT NULL,
        category_id INT, subcategory_id INT, metal_id INT, purity_id INT,
        hsn NVARCHAR(20), unit NVARCHAR(10) DEFAULT 'GMS', rate FLOAT DEFAULT 0,
        active BIT DEFAULT 1)"""),
    ("customer_master", """CREATE TABLE customer_master (
        customer_id INT IDENTITY(1,1) PRIMARY KEY,
        code NVARCHAR(30) NOT NULL UNIQUE, name NVARCHAR(100) NOT NULL,
        address NVARCHAR(200), city NVARCHAR(50), phone NVARCHAR(30),
        email NVARCHAR(100), gstin NVARCHAR(20), opening_balance FLOAT DEFAULT 0,
        active BIT DEFAULT 1)"""),
    ("supplier_master", """CREATE TABLE supplier_master (
        supplier_id INT IDENTITY(1,1) PRIMARY KEY,
        code NVARCHAR(30) NOT NULL UNIQUE, name NVARCHAR(100) NOT NULL,
        address NVARCHAR(200), city NVARCHAR(50), phone NVARCHAR(30),
        email NVARCHAR(100), gstin NVARCHAR(20), opening_balance FLOAT DEFAULT 0,
        active BIT DEFAULT 1)"""),
]


# ---------------------------------------------------------------------------
# SQL Server setup: DSN + database
# ---------------------------------------------------------------------------

def ensure_dsn():
    """Create the User DSN if it does not already exist (Windows only)."""
    if not _ss_bool("create_dsn", False):
        return
    dsn = _ss("dsn", "JewelleryERP")
    try:
        import pyodbc
        existing = {k.lower() for k in pyodbc.dataSources().keys()}
        if dsn.lower() in existing:
            return
    except Exception:
        pass

    if not sys.platform.startswith("win"):
        print("DSN auto-create skipped (not Windows).")
        return

    import ctypes
    from ctypes import wintypes
    ODBC_ADD_DSN = 1
    driver = _ss("driver", "ODBC Driver 17 for SQL Server")
    attrs = [f"DSN={dsn}", f"SERVER={_ss('server', 'localhost')}",
             f"DATABASE={_ss('database', 'JewelleryERP')}"]
    if _ss_bool("trusted_connection", True):
        attrs.append("Trusted_Connection=Yes")
    else:
        attrs += [f"UID={_ss('uid')}", f"PWD={_ss('pwd')}"]

    # Attributes are a null-separated, double-null-terminated list. A Python str
    # cannot hold embedded nulls when handed to a C string parameter, so we pass
    # an explicit byte buffer to the ANSI entry point.
    attr_bytes = ("\0".join(attrs) + "\0\0").encode("mbcs")
    attr_buf = ctypes.create_string_buffer(attr_bytes, len(attr_bytes))

    try:
        func = ctypes.windll.ODBCCP32.SQLConfigDataSource
        func.argtypes = [wintypes.HWND, wintypes.WORD,
                         ctypes.c_char_p, ctypes.c_char_p]
        func.restype = ctypes.c_int
        ok = func(0, ODBC_ADD_DSN, driver.encode("mbcs"), attr_buf)
        if ok:
            print(f"Created ODBC DSN '{dsn}'.")
        else:
            print(f"WARNING: could not create DSN '{dsn}'. "
                  f"The app will connect DSN-less instead.")
    except Exception as e:
        print(f"WARNING: DSN creation skipped ({e}). Connecting DSN-less instead.")


def ensure_database():
    """Create the target database if missing, optionally with files in the folder."""
    if not _ss_bool("create_database", False):
        return
    import pyodbc
    dbname = _ss("database", "JewelleryERP")
    conn = pyodbc.connect(_connstr_dsnless("master"), autocommit=True)
    try:
        cur = conn.cursor()
        cur.execute("SELECT DB_ID(?)", dbname)
        if cur.fetchone()[0] is not None:
            return  # already exists

        if _ss_bool("db_in_folder", False):
            mdf = os.path.join(BASE_DIR, f"{dbname}.mdf")
            ldf = os.path.join(BASE_DIR, f"{dbname}_log.ldf")
            ddl = (f"CREATE DATABASE [{dbname}] ON PRIMARY "
                   f"(NAME=N'{dbname}', FILENAME=N'{mdf}') "
                   f"LOG ON (NAME=N'{dbname}_log', FILENAME=N'{ldf}')")
            try:
                cur.execute(ddl)
                print(f"Created database '{dbname}' with files in project folder.")
                return
            except Exception as e:
                print(f"Could not create DB in folder ({e}); using default location.")
        cur.execute(f"CREATE DATABASE [{dbname}]")
        print(f"Created database '{dbname}'.")
    finally:
        conn.close()


def _table_exists(conn, table):
    cur = conn.cursor()
    if ENGINE == "sqlserver":
        cur.execute("SELECT OBJECT_ID(?)", table)
        return cur.fetchone()[0] is not None
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table,))
    return cur.fetchone() is not None


# ---------------------------------------------------------------------------
# Init + seed
# ---------------------------------------------------------------------------

def init_db():
    if ENGINE == "sqlserver":
        ensure_dsn()
        ensure_database()
        conn = get_connection()
        try:
            for name, ddl in SQLSERVER_TABLES:
                if not _table_exists(conn, name):
                    conn.cursor().execute(ddl)
            conn.commit()
        finally:
            conn.close()
        _seed()
    elif ENGINE == "sqlite":
        conn = get_connection()
        try:
            conn.executescript(SQLITE_SCHEMA)
            # data/schema.sql is the original GMINE schema recovered from the
            # PowerBuilder export (tools/build_schema.py). Creating it locally
            # gives the screens their real tables and columns to work on.
            extra = os.path.join(BASE_DIR, "data", "schema.sql")
            if os.path.exists(extra):
                with open(extra, encoding="utf-8") as fh:
                    conn.executescript(fh.read())
            conn.commit()
        finally:
            conn.close()
        _seed()
    else:
        # Existing external database (e.g. SQL Anywhere): connect only.
        # Do NOT create tables or seed; screens map to your existing tables.
        return


def _seed():
    if fetch_one("SELECT COUNT(*) AS c FROM users")["c"] == 0:
        execute("INSERT INTO users (username, password, full_name, role) VALUES (?,?,?,?)",
                ("admin", hash_password("admin"), "Administrator", "ADMIN"))

    # gmine-style login user (demo password: admin)
    if fetch_one("SELECT COUNT(*) AS c FROM userm")["c"] == 0:
        from pb_compat import fpencrypt
        execute("INSERT INTO userm (code, name, pcode) VALUES (?,?,?)",
                ("01", "Administrator", fpencrypt("admin", 1)))

    if fetch_one("SELECT COUNT(*) AS c FROM metal_master")["c"] == 0:
        for code, name in [("GOLD", "Gold"), ("SILV", "Silver"), ("PLAT", "Platinum")]:
            execute("INSERT INTO metal_master (code, name) VALUES (?,?)", (code, name))

    if fetch_one("SELECT COUNT(*) AS c FROM purity_master")["c"] == 0:
        for code, name, val in [("916", "22 Karat (916)", 91.6),
                                ("750", "18 Karat (750)", 75.0),
                                ("999", "Fine Silver (999)", 99.9)]:
            execute("INSERT INTO purity_master (code, name, purity_value) VALUES (?,?,?)",
                    (code, name, val))

    if fetch_one("SELECT COUNT(*) AS c FROM category_master")["c"] == 0:
        for code, name in [("RING", "Ring"), ("NECK", "Necklace"), ("BANG", "Bangle"),
                           ("CHAIN", "Chain"), ("EARR", "Earring")]:
            execute("INSERT INTO category_master (code, name) VALUES (?,?)", (code, name))

    if fetch_one("SELECT COUNT(*) AS c FROM unit_master")["c"] == 0:
        for code, name in [("GMS", "Grams"), ("PCS", "Pieces"), ("CT", "Carat")]:
            execute("INSERT INTO unit_master (code, name) VALUES (?,?)", (code, name))

    if fetch_one("SELECT COUNT(*) AS c FROM tax_master")["c"] == 0:
        for code, name, rate in [("GST03", "GST 3%", 3.0), ("GST05", "GST 5%", 5.0),
                                 ("GST18", "GST 18%", 18.0)]:
            execute("INSERT INTO tax_master (code, name, rate) VALUES (?,?,?)",
                    (code, name, rate))


if __name__ == "__main__":
    init_db()
    print(f"Engine: {ENGINE}. Database initialised.")
