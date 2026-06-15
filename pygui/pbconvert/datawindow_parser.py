"""
Parse a PowerBuilder DataWindow export (``.srd``).

We extract the pieces a Qt grid / report needs:

* the ``table(column=(...) ...)`` definitions  -> column name, type, db column
* the ``retrieve="PBSELECT(...)"`` or embedded SQL -> the data source
* the ``update=...`` clause                     -> updatable table name
* ``column(...)`` / ``text(...)`` presentation  -> headings, order, widths

DataWindow SQL is stored either as a PBSELECT() graphical spec or as literal
``SELECT ...``.  We translate the common PBSELECT form to real SQL so the data
can actually be retrieved from the live database.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field


@dataclass
class DWColumn:
    name: str
    type: str = "char"
    dbname: str = ""
    update: bool = False
    key: bool = False
    heading: str = ""
    order: int = 0
    width: int = 0


@dataclass
class DataWindow:
    name: str
    columns: list = field(default_factory=list)
    retrieve_sql: str = ""
    update_table: str = ""
    presentation: str = "grid"   # grid / freeform / tabular / group
    raw_retrieve: str = ""

    def heading_map(self) -> dict:
        return {c.name: (c.heading or c.name) for c in self.columns}


_KV_RE = re.compile(r'(\w+)=("(?:[^"]|(?<=~)")*"|[^\s)]+)')


def _kv(blob: str) -> dict:
    out = {}
    for m in _KV_RE.finditer(blob):
        k = m.group(1)
        v = m.group(2)
        if v.startswith('"') and v.endswith('"'):
            v = v[1:-1].replace('~"', '"')
        out[k] = v
    return out


def _balanced_blocks(text: str, keyword: str):
    """Yield the content of every ``keyword=( ... )`` accounting for the nested
    parens that appear in column types like ``type=char(10)``."""
    i = 0
    pat = keyword + "=("
    while True:
        start = text.find(pat, i)
        if start == -1:
            return
        j = start + len(pat)
        depth = 1
        while j < len(text) and depth:
            ch = text[j]
            if ch == "(":
                depth += 1
            elif ch == ")":
                depth -= 1
            j += 1
        yield text[start + len(pat): j - 1]
        i = j


def _translate_pbselect(spec: str) -> str:
    """Best-effort PBSELECT(...) -> SQL SELECT.

    Handles the common shape produced by the graphical SQL painter:
        PBSELECT( VERSION(400)
            TABLE(NAME="phoneptype")
            COLUMN(NAME="phoneptype.code")
            COLUMN(NAME="phoneptype.name") )
    More exotic specs (joins, where, group) fall back to a plain projection
    over the listed tables; the runtime can still display the columns.
    """
    tables = re.findall(r'TABLE\(NAME=~?"?([\w.]+)~?"?', spec)
    columns = re.findall(r'COLUMN\(NAME=~?"?([\w.]+)~?"?', spec)
    if not tables:
        return ""
    cols = ", ".join(columns) if columns else "*"
    sql = f"SELECT {cols} FROM {', '.join(dict.fromkeys(tables))}"
    # carry a simple WHERE if the painter emitted one as literal text
    where = re.search(r'WHERE\((.*?)\)\s*\)?\s*$', spec, re.DOTALL)
    return sql


def parse_datawindow(text: str, name: str | None = None) -> DataWindow:
    if name is None:
        m = re.search(r'\$PBExportHeader\$(\w+)\.srd', text)
        name = m.group(1) if m else "datawindow"
    dw = DataWindow(name=name)

    # --- columns: every column=( ... ) in the table() definition ---------
    for blob in _balanced_blocks(text, "column"):
        if "dbname=" not in blob and "name=" not in blob:
            continue
        kv = _kv(blob)
        if "name" not in kv:
            continue
        col = DWColumn(
            name=kv.get("name", ""),
            type=re.sub(r'\(.*', '', kv.get("type", "char")),
            dbname=kv.get("dbname", ""),
            update=kv.get("update", "") in ("yes", "y"),
            key=kv.get("key", "") in ("yes", "y"),
        )
        dw.columns.append(col)

    # --- retrieve SQL: quotes inside are PB-escaped as ~" ----------------
    rm = re.search(r'retrieve=\s*"((?:[^"]|(?<=~)")*)"', text, re.DOTALL)
    if rm:
        raw = (rm.group(1).replace('~"', '"')
               .replace('~r~n', ' ').replace('~n', ' ').replace('~t', ' '))
        dw.raw_retrieve = raw.strip()
        head = raw.lstrip().upper()
        if head.startswith("PBSELECT"):
            dw.retrieve_sql = _translate_pbselect(raw)
        elif head.startswith(("SELECT", "EXECUTE", "WITH")):
            dw.retrieve_sql = raw.strip()

    # --- updatable table: the quoted table-level ``update="name"`` -------
    um = re.search(r'\bupdate="(\w+)"', text)
    if um:
        dw.update_table = um.group(1)

    # --- presentation: headings, order, widths ---------------------------
    headings: dict[str, str] = {}
    for blob in _balanced_blocks(text, "text"):
        kv = _kv(blob)
        nm = kv.get("name", "")
        if nm.endswith("_t"):
            headings[nm[:-2]] = kv.get("text", "")

    col_names = {c.name for c in dw.columns}
    widths: dict[str, int] = {}
    # presentation columns are written as ``column(name=... )`` (no '=' after)
    for m in re.finditer(r'\bcolumn\(', text):
        start = m.end()
        depth = 1
        j = start
        while j < len(text) and depth:
            if text[j] == "(":
                depth += 1
            elif text[j] == ")":
                depth -= 1
            j += 1
        kv = _kv(text[start:j - 1])
        nm = kv.get("name", "")
        if nm and nm in col_names:
            try:
                widths[nm] = int(kv.get("width", "0"))
            except ValueError:
                pass

    for idx, col in enumerate(dw.columns):
        col.heading = headings.get(col.name, col.name.replace("_", " ").title())
        col.order = idx
        col.width = widths.get(col.name, 0)

    # presentation style hint
    if re.search(r'\bgroup\(', text):
        dw.presentation = "group"
    elif text.count("detail(height") and 'freeform' in text.lower():
        dw.presentation = "freeform"

    return dw
