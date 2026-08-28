"""
Generic CRUD engine for the auto-rendered PowerBuilder screens.

Hand-written modules (:mod:`app.modules`) carry the real business rules for the
transactions that need them. Every *other* window is rendered by
:mod:`app.ui.pb_form`, and this service gives those screens working
Insert / Update / Delete against the window's own table.

Safety rules, because a wrong column guess would corrupt real data:

* the column list always comes from the database itself
  (:func:`db.table_columns`), never from the screen;
* a field is written only when its control name maps **exactly** onto a real
  column after the PowerBuilder prefix is stripped (``sle_partycode`` ->
  ``partycode``); anything unmatched is left alone and reported to the user;
* every statement is parameterised, and identifiers are taken from the
  introspected schema, so nothing from the screen reaches SQL as text;
* updates and deletes are keyed on the primary key. A table without one is
  keyed on the whole loaded row (like a PowerBuilder DataWindow), and the
  caller is told how many rows the key matches before anything is written.
"""

from __future__ import annotations

import json
import os
import re
from dataclasses import dataclass, field
from functools import lru_cache

import db

# Optional per-window corrections, so a screen can be fixed without touching
# code:  data/field_map.json
#   {"w_item": {"table": "items",
#               "fields": {"sle_itemcode": "code", "sle_desc": "descr"}}}
OVERRIDE_FILE = "field_map.json"
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


@lru_cache(maxsize=4)
def _overrides(base_dir: str) -> dict:
    path = os.path.join(base_dir, "data", OVERRIDE_FILE)
    if not os.path.exists(path):
        return {}
    try:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    except Exception:
        return {}


def override_for(window: str, base_dir: str | None = None) -> dict:
    """Manual table/field mapping for ``window``, if one is configured."""
    return _overrides(base_dir or BASE_DIR).get(window or "", {})

# PowerBuilder naming conventions: control prefixes that are not part of the
# column name.
_PREFIXES = ("sle_", "em_", "mle_", "cbx_", "cb_", "ddlb_", "dddw_", "ddplb_",
             "lb_", "rb_", "st_", "dw_", "uo_", "tab_", "sle", "em")
# Common column spellings that differ from the control name.
_ALIASES = {
    "partycode": ("accode", "party", "code"),
    "partyname": ("acname", "name"),
    "billno": ("bno", "billno"),
    "billdate": ("bdate", "tdate", "date"),
    "date": ("tdate", "bdate"),
    "amount": ("amt",),
    "amt": ("amount",),
    "weight": ("wgt",),
    "wgt": ("weight",),
    "quantity": ("qty",),
    "qty": ("quantity",),
    "remarks": ("remark", "narration"),
    "narration": ("remarks", "remark"),
    "address": ("add1", "address1"),
    "phone": ("phone1", "mobile"),
}

_NUMERIC_HINTS = ("INT", "DEC", "NUM", "FLOAT", "REAL", "DOUB", "MONEY", "SMALLMONEY")
_DATE_HINTS = ("DATE", "TIME")


def _norm(name: str) -> str:
    """Normalise a control or column name for comparison."""
    name = name.strip().lower()
    for p in _PREFIXES:
        if name.startswith(p) and len(name) > len(p):
            name = name[len(p):]
            break
    return re.sub(r"[^a-z0-9]", "", name)


@dataclass
class Mapping:
    """Which screen fields correspond to which table columns."""
    table: str
    columns: list = field(default_factory=list)       # schema rows from db
    fields: dict = field(default_factory=dict)        # control name -> column
    unmapped: list = field(default_factory=list)      # control names
    keys: list = field(default_factory=list)          # key columns declared by
                                                      # the original DataWindow

    @property
    def column_names(self) -> list:
        return [c["name"] for c in self.columns]

    @property
    def pk(self) -> list:
        """Key columns: the ones the original screen used, else the table's."""
        names = set(self.column_names)
        declared = [k for k in self.keys if k in names]
        return declared or [c["name"] for c in self.columns if c["pk"]]

    @property
    def autoinc(self) -> set:
        return {c["name"] for c in self.columns if c.get("autoinc")}

    @property
    def writable(self) -> bool:
        return bool(self.columns and self.fields)

    def column(self, name: str) -> dict | None:
        for c in self.columns:
            if c["name"] == name:
                return c
        return None

    def describe(self) -> str:
        if not self.columns:
            return f"Table '{self.table}' is not in the current database."
        if not self.fields:
            return (f"{self.table}: no screen field matches a column of this "
                    f"table, so records cannot be edited here.")
        return (f"{self.table}: {len(self.fields)} of "
                f"{len(self.fields) + len(self.unmapped)} fields mapped"
                + (f", key = {', '.join(self.pk)}" if self.pk
                   else ", no primary key (rows are matched on all values)"))


def build_mapping(table: str, control_names, window: str = "") -> Mapping:
    """Map screen controls onto the real columns of ``table``.

    ``window`` enables the per-window corrections in ``data/field_map.json``:
    they can point the screen at a different table and pin individual fields
    that the automatic matching cannot work out.
    """
    manual = override_for(window)
    table = manual.get("table", table)
    columns = db.table_columns(table) if table else []
    mapping = Mapping(table=table, columns=columns)
    if not columns:
        mapping.unmapped = list(control_names)
        return mapping

    by_norm = {}
    for col in columns:
        by_norm.setdefault(_norm(col["name"]), col["name"])

    manual_fields = {k: v for k, v in manual.get("fields", {}).items()
                     if v in by_norm.values() or v in [c["name"] for c in columns]}
    taken: set = set(manual_fields.values())
    for ctrl in control_names:
        if ctrl in manual_fields:
            mapping.fields[ctrl] = manual_fields[ctrl]
            continue
        key = _norm(ctrl)
        target = by_norm.get(key)
        if target is None:
            for alias in _ALIASES.get(key, ()):
                target = by_norm.get(_norm(alias))
                if target:
                    break
        if target and target not in taken:
            mapping.fields[ctrl] = target
            taken.add(target)
        else:
            mapping.unmapped.append(ctrl)
    return mapping


def build_grid_mapping(spec: dict) -> Mapping:
    """Mapping for a screen that edits its table through a DataWindow grid.

    ``spec`` comes from the catalog and mirrors the original ``.srd``: the table
    it updates, its key columns and the columns it shows. Only columns the
    database actually has are kept.
    """
    table = (spec or {}).get("table", "")
    columns = db.table_columns(table) if table else []
    mapping = Mapping(table=table, columns=columns,
                      keys=[k.lower() for k in (spec or {}).get("keys", [])])
    present = {c["name"].lower(): c["name"] for c in columns}
    for col in (spec or {}).get("columns", []):
        name = present.get(str(col.get("name", "")).lower())
        if name and name not in mapping.fields.values():
            mapping.fields[name] = name
        elif col.get("name"):
            mapping.unmapped.append(col["name"])
    return mapping


def coerce(value, column: dict | None):
    """Convert a widget value to something the column accepts."""
    if isinstance(value, bool):
        return 1 if value else 0
    if value is None:
        return None
    text = str(value).strip()
    if text == "":
        return None
    ctype = (column or {}).get("type", "")
    if any(h in ctype for h in _NUMERIC_HINTS):
        cleaned = text.replace(",", "")
        try:
            return int(cleaned) if re.fullmatch(r"-?\d+", cleaned) else float(cleaned)
        except ValueError as exc:
            raise ValueError(f"'{text}' is not a number "
                             f"({column['name']} is {ctype})") from exc
    return text


def prepare_values(mapping: Mapping, raw: dict, *, for_insert: bool) -> dict:
    """Screen values -> column values, dropping identity columns on insert."""
    out: dict = {}
    for ctrl, column in mapping.fields.items():
        if ctrl not in raw:
            continue
        if for_insert and column in mapping.autoinc:
            continue
        out[column] = coerce(raw[ctrl], mapping.column(column))
    return out


def _check_identifier(mapping: Mapping, name: str) -> str:
    if name not in mapping.column_names:
        raise ValueError(f"unknown column {name!r} for table {mapping.table}")
    return name


def _where(mapping: Mapping, key: dict) -> tuple:
    parts, params = [], []
    for col, val in key.items():
        _check_identifier(mapping, col)
        if val is None:
            parts.append(f"{col} IS NULL")
        else:
            parts.append(f"{col} = ?")
            params.append(val)
    return " AND ".join(parts), params


def key_for_row(mapping: Mapping, row: dict) -> dict:
    """The identity used to update/delete ``row``: the PK, else the whole row."""
    if mapping.pk and all(k in row for k in mapping.pk):
        return {k: row[k] for k in mapping.pk}
    return {c: row[c] for c in mapping.column_names if c in row}


def count_matching(mapping: Mapping, key: dict) -> int:
    clause, params = _where(mapping, key)
    if not clause:
        return 0
    row = db.fetch_one(f"SELECT COUNT(*) AS n FROM {mapping.table} WHERE {clause}",
                       params)
    return int(list(row.values())[0]) if row else 0


def insert(mapping: Mapping, values: dict):
    if not values:
        raise ValueError("nothing to save: no field is filled in")
    cols = [_check_identifier(mapping, c) for c in values]
    sql = (f"INSERT INTO {mapping.table} ({', '.join(cols)}) "
           f"VALUES ({', '.join('?' for _ in cols)})")
    return db.execute(sql, [values[c] for c in cols])


def update(mapping: Mapping, values: dict, key: dict):
    if not values:
        raise ValueError("nothing to save: no field is filled in")
    if not key:
        raise ValueError("this record has no key, so it cannot be updated")
    cols = [_check_identifier(mapping, c) for c in values]
    clause, wparams = _where(mapping, key)
    sql = (f"UPDATE {mapping.table} SET "
           + ", ".join(f"{c} = ?" for c in cols)
           + f" WHERE {clause}")
    return db.execute(sql, [values[c] for c in cols] + wparams)


def delete(mapping: Mapping, key: dict):
    if not key:
        raise ValueError("this record has no key, so it cannot be deleted")
    clause, params = _where(mapping, key)
    return db.execute(f"DELETE FROM {mapping.table} WHERE {clause}", params)


def select_rows(mapping: Mapping, limit: int = 500, search: str = "") -> list:
    """Rows for the screen's grid, optionally filtered by a free-text search."""
    sql = f"SELECT * FROM {mapping.table}"
    params: list = []
    text = (search or "").strip()
    if text:
        texty = [c["name"] for c in mapping.columns
                 if not any(h in c["type"] for h in _NUMERIC_HINTS + _DATE_HINTS)]
        if texty:
            sql += " WHERE " + " OR ".join(
                f"UPPER(CAST({c} AS VARCHAR(255))) LIKE ?" for c in texty)
            params = [f"%{text.upper()}%"] * len(texty)
    rows = db.fetch_all(sql, params)
    return rows[:limit]
