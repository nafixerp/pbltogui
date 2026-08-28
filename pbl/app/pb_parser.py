"""
PowerBuilder source parser.

The GMINE application is exported as PowerBuilder source: ``.srw`` window
objects, ``.srd`` DataWindow objects and ``.srf`` function objects, all encoded
as UTF-16. Rather than hand-rewrite 500+ windows, the migration parses these
sources at runtime and reconstructs each window faithfully:

  * window title and geometry
  * every visible control (edits, masks, checkboxes, radios, buttons,
    drop-downs, static labels, group boxes, DataWindow grids) with its
    original position, caption and field length
  * the database tables the window reads / writes, recovered from the embedded
    SQL in its event scripts

The result drives :mod:`app.ui.pb_form`, which renders a real PySide6 form for
any window in the original menu.
"""

from __future__ import annotations

import os
import re
from dataclasses import dataclass, field
from functools import lru_cache

# PowerBuilder Units -> pixels. PB layouts are in PBU; ~1/4 gives a faithful
# on-screen size for these dialogs.
PBU = 0.26

# Control classes we render and how they map conceptually.
INPUT_KINDS = {"singlelineedit", "editmask", "multilineedit"}
DECORATION_KINDS = {"line", "oval", "rectangle", "roundrectangle", "picture"}


@dataclass
class Control:
    name: str
    kind: str
    x: int = 0
    y: int = 0
    width: int = 0
    height: int = 0
    text: str = ""
    taborder: int = 0
    limit: int = 0
    items: list = field(default_factory=list)
    dataobject: str = ""


@dataclass
class Window:
    name: str
    title: str
    width: int
    height: int
    controls: list
    tables: list
    source_path: str
    grid: dict | None = None      # the DataWindow this screen edits, if any


def decode_pb(path: str) -> str:
    """Decode a PowerBuilder source file (UTF-16, BOM optional)."""
    raw = open(path, "rb").read()
    for enc in ("utf-16", "utf-16-le", "utf-8"):
        try:
            return raw.decode(enc)
        except UnicodeDecodeError:
            continue
    return raw.decode("latin-1", errors="replace")


_STR_PROP = lambda body, key: (
    m.group(1) if (m := re.search(rf'string {key}\s*=\s*"((?:[^"\\]|\\.)*)"', body)) else ""
)
_INT_PROP = lambda body, key, d=0: (
    int(m.group(1)) if (m := re.search(rf'\bint {key}\s*=\s*(-?\d+)', body)) else d
)


def _unescape(text: str) -> str:
    return (text.replace('~r', '').replace('~n', ' ')
                .replace('~t', ' ').replace('~"', '"').replace('~~', '~').strip())


def _parse_items(body: str) -> list:
    """Drop-down list items: ``string item[] = {"A","B"}`` or ``item[N] = "X"``."""
    items = []
    arr = re.search(r'item\[\]\s*=\s*\{([^}]*)\}', body)
    if arr:
        items = re.findall(r'"((?:[^"\\]|\\.)*)"', arr.group(1))
    else:
        items = [v for _, v in sorted(
            (int(n), v) for n, v in re.findall(r'item\[(\d+)\]\s*=\s*"([^"]*)"', body))]
    return [_unescape(i) for i in items]


# PowerBuilder control/object classes that follow "from" in type declarations
# (``type cb_x from commandbutton``) — never database tables.
_PB_CLASSES = {
    "commandbutton", "singlelineedit", "multilineedit", "editmask", "checkbox",
    "radiobutton", "groupbox", "statictext", "dropdownlistbox", "listbox",
    "datawindow", "picture", "line", "oval", "rectangle", "roundrectangle",
    "window", "menu", "structure", "userobject", "tab", "tabpage", "graph",
    "picturebutton", "cb", "uo", "scrollbar", "richtextedit", "treeview",
    "listview", "this", "parent", "dual",
}


# Housekeeping tables every script touches (settings, audit log, lookups).
# They are real tables, but never what a screen is *about*, so they must not
# win the "primary table" slot.
_INFRA_TABLES = {
    "generali", "generals", "generald", "generalc", "delpart", "userhist",
    "userm", "userd", "codehelp", "company", "daybookpart", "reminder",
}


def _extract_tables(text: str) -> list:
    """Recover database tables from embedded SQL in event scripts.

    Write targets (INSERT/UPDATE) come first — they are unambiguously real
    tables and make the best "primary table" for a data grid — with
    housekeeping tables pushed to the back so a screen is identified by the
    data it is about.
    """
    write, read = [], []
    for m in re.finditer(r'\bINSERT\s+INTO\s+(\w+)', text, re.I):
        write.append(m.group(1).lower())
    for m in re.finditer(r'\bUPDATE\s+(\w+)\s+SET', text, re.I):
        write.append(m.group(1).lower())
    for m in re.finditer(r'\bFROM\s+(\w+)', text, re.I):
        read.append(m.group(1).lower())

    mentions = {}
    for name in write + read:
        mentions[name] = mentions.get(name, 0) + 1

    ordered, seen = [], set()
    for name in write + read:
        if (name in seen or name in _PB_CLASSES or name.startswith("w_")
                or name.startswith("d_")):
            continue
        seen.add(name)
        ordered.append(name)
    # Stable sort: real subject tables first, most-used first within each group.
    ordered.sort(key=lambda n: (n in _INFRA_TABLES, -mentions.get(n, 0)))
    return ordered


@lru_cache(maxsize=512)
def parse_window(path: str) -> Window:
    text = decode_pb(path)
    win_name = os.path.splitext(os.path.basename(path))[0]

    # Detailed window block (the one carrying geometry/title, not the forward decl).
    title, width, height = win_name, 2400, 1500
    for m in re.finditer(rf'\btype {re.escape(win_name)} from \w+\b([\s\S]*?)\bend type',
                         text):
        body = m.group(1)
        if 'int width' in body:
            title = _unescape(_STR_PROP(body, "title")) or win_name
            width = _INT_PROP(body, "width", width)
            height = _INT_PROP(body, "height", height)
            break

    # Control detail blocks. The forward declarations have empty bodies; we keep
    # the richest (longest) block seen per control name.
    best: dict[str, Control] = {}
    pattern = re.compile(
        r'\btype (\w+) from (\w+) within ' + re.escape(win_name) + r'\b([\s\S]*?)\bend type')
    for m in pattern.finditer(text):
        name, kind, body = m.group(1), m.group(2).lower(), m.group(3)
        if not body.strip():
            continue
        if name in best and len(body) <= getattr(best[name], "_blen", 0):
            continue
        ctrl = Control(
            name=name, kind=kind,
            x=_INT_PROP(body, "x"), y=_INT_PROP(body, "y"),
            width=_INT_PROP(body, "width"), height=_INT_PROP(body, "height"),
            text=_unescape(_STR_PROP(body, "text")),
            taborder=_INT_PROP(body, "taborder"),
            limit=_INT_PROP(body, "limit"),
            items=_parse_items(body) if kind in ("dropdownlistbox", "listbox") else [],
            dataobject=_STR_PROP(body, "dataobject"),
        )
        ctrl._blen = len(body)  # type: ignore[attr-defined]
        best[name] = ctrl

    controls = sorted(best.values(), key=lambda c: (c.y, c.x))
    return Window(
        name=win_name, title=title, width=width, height=height,
        controls=controls, tables=_extract_tables(text), source_path=path,
    )


def find_source(rel_path: str, base_dir: str) -> str | None:
    """Resolve a ``dir\\file.srw`` reference from project_tree.txt to a real path."""
    rel = rel_path.replace("\\", os.sep)
    candidate = os.path.join(base_dir, rel)
    if os.path.exists(candidate):
        return candidate
    # Fall back to a basename search across module folders.
    target = os.path.basename(rel)
    for root, _dirs, files in os.walk(base_dir):
        if target in files:
            return os.path.join(root, target)
    return None


# ---------------------------------------------------------------------------
# DataWindow objects (.srd)
# ---------------------------------------------------------------------------

@dataclass
class DWColumn:
    """One column of a DataWindow, as the original application defined it."""
    name: str
    dbname: str = ""
    type: str = ""
    label: str = ""
    key: bool = False
    update: bool = False

    @property
    def table(self) -> str:
        return self.dbname.split(".")[0].lower() if "." in self.dbname else ""

    @property
    def column(self) -> str:
        return (self.dbname.split(".")[-1] or self.name).lower()


@dataclass
class DataWindow:
    """A parsed ``.srd``: the table the screen edits, its columns and its key."""
    name: str
    update_table: str = ""
    columns: list = field(default_factory=list)
    tables: list = field(default_factory=list)

    def _own(self, c: DWColumn) -> bool:
        return bool(c.dbname) and (not c.table or c.table == self.update_table)

    @property
    def keys(self) -> list:
        return [c.column for c in self.columns if c.key and self._own(c)]

    @property
    def updatable(self) -> list:
        return [c for c in self.columns if self._own(c)]

    @property
    def writable(self) -> bool:
        return bool(self.update_table and self.updatable)


_DW_UPDATE_RE = re.compile(r'\bupdate="(\w+)"')
_DW_TABLE_RE = re.compile(r'TABLE\(NAME=~"(\w+)~"')
_DW_HEADER_RE = re.compile(r'text\(name=(\w+)_t\b[\s\S]*?\btext="([^"]*)"')


@lru_cache(maxsize=1024)
def parse_datawindow(path: str) -> DataWindow:
    text = decode_pb(path)
    name = os.path.splitext(os.path.basename(path))[0]

    start = text.find("table(")
    block = text[start:] if start >= 0 else ""
    end = block.find("\nte")           # the first object after the table block
    block = block[:end] if end > 0 else block

    labels = {k: _unescape(v) for k, v in _DW_HEADER_RE.findall(text)}
    columns = []
    for chunk in block.split("column=(")[1:]:
        body = chunk.split("retrieve=")[0].split("column=(")[0]
        m_name = re.search(r'\bname=(\w+)', body)
        if not m_name:
            continue
        m_type = re.search(r'\btype=([a-z]+)', body)
        m_db = re.search(r'dbname="([^"]*)"', body)
        cname = m_name.group(1)
        columns.append(DWColumn(
            name=cname,
            dbname=(m_db.group(1) if m_db else ""),
            type=(m_type.group(1) if m_type else ""),
            label=labels.get(cname, "") or cname,
            key="key=yes" in body,
            update="update=yes" in body))

    m_upd = _DW_UPDATE_RE.search(block)
    tables = list(dict.fromkeys(t.lower() for t in _DW_TABLE_RE.findall(text)))
    if not tables:
        tables = list(dict.fromkeys(c.table for c in columns if c.table))
    return DataWindow(name=name,
                      update_table=(m_upd.group(1).lower() if m_upd else ""),
                      columns=columns, tables=tables)


def find_datawindow(dataobject: str, base_dir: str) -> str | None:
    """Locate the ``.srd`` file for a DataWindow object name."""
    if not dataobject:
        return None
    return find_source(f"{dataobject}.srd", base_dir)
