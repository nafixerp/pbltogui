"""
Parser for the PowerBuilder menu object ``m_mainmenu.srm``.

``project_tree.txt`` is a hand-maintained map of the original menu; the menu
object itself is the authority. This module reads the exported menu source and
rebuilds the real structure:

  * the nesting of every item (``type X from menu within Y``)
  * the display order the menu was created with (the ``this.Item[...]`` list in
    each ``on X.create`` script)
  * the caption, accelerator and visibility of each item
  * the window each leaf opens, recovered from its ``clicked`` script
    (``open``/``openwithparm``/``opensheet``/``setfocus``)

The result is a tree of :class:`app.menu_loader.MenuNode`, so it drops straight
into the existing main window.
"""

from __future__ import annotations

import os
import re
from dataclasses import dataclass, field

from app.menu_loader import MenuNode
from app.pb_parser import decode_pb

# --- PowerBuilder shortcut codes -------------------------------------------
# A shortcut is a Windows virtual-key code plus modifier bits.
_MOD_CTRL, _MOD_ALT, _MOD_SHIFT = 256, 512, 1024
_VK_NAMES = {
    8: "Backspace", 9: "Tab", 13: "Return", 27: "Esc", 32: "Space",
    33: "PgUp", 34: "PgDown", 35: "End", 36: "Home",
    37: "Left", 38: "Up", 39: "Right", 40: "Down", 45: "Ins", 46: "Del",
}
_VK_NAMES.update({112 + i: f"F{i + 1}" for i in range(12)})

_HEADER_RE = re.compile(
    r'(?m)^(?:global\s+)?type\s+(\w+)\s+from\s+(menu|menucascade)\b(?:\s+within\s+(\w+))?')
_TEXT_RE = re.compile(r'this\.text\s*=\s*"((?:[^"]|~")*)"')
_SHORTCUT_RE = re.compile(r'this\.shortcut\s*=\s*(\d+)')
_VISIBLE_RE = re.compile(r'this\.visible\s*=\s*(true|false)', re.I)
_ITEM_RE = re.compile(r'this\.Item\[[^\]]*\]\s*=\s*this\.(\w+)')
_CLICKED_RE = re.compile(r'(?m)^event\s+clicked;([\s\S]*?)^end event')
# open(w_x) / openwithparm(w_x,...) / opensheet(w_x, w_main,...)
_OPEN_RE = re.compile(r'\b(?:open|openwithparm|opensheet|opensheetwithparm)\s*\(\s*([\w"]+)',
                      re.I)
_OPEN_STR_RE = re.compile(r'\bopensheet\w*\s*\(\s*\w+\s*,\s*"(w_\w+)"', re.I)
_SETFOCUS_RE = re.compile(r'\b(w_\w+)\s*\.\s*setfocus\s*\(', re.I)
_LOCAL_DECL_RE = re.compile(r'(?m)^\s*(w_\w+)\s+(\w+)\s*$')
# Frame / transient windows a script may touch that are never a menu target.
_NON_TARGETS = {"w_main", "w_whait", "w_wait"}


def _unescape(text: str) -> str:
    """PowerBuilder string escapes: ``~t`` tab, ``~'`` quote, ``~~`` tilde."""
    return (text.replace("~t", "\t").replace("~n", " ").replace("~r", "")
                .replace('~"', '"').replace("~'", "'").replace("~~", "~"))


def _decode_shortcut(code: int) -> str:
    key = code & 0xFF
    parts = []
    if code & _MOD_CTRL:
        parts.append("Ctrl")
    if code & _MOD_ALT:
        parts.append("Alt")
    if code & _MOD_SHIFT:
        parts.append("Shift")
    name = _VK_NAMES.get(key) or (chr(key) if 32 < key < 127 else "")
    if not name:
        return ""
    parts.append(name)
    return "+".join(parts)


@dataclass
class MenuItem:
    """One raw item of the PowerBuilder menu object."""
    name: str
    parent: str | None = None
    label: str = ""
    shortcut: str = ""
    visible: bool = True
    order: list = field(default_factory=list)   # child names, in creation order
    windows: list = field(default_factory=list)  # windows the clicked script opens

    @property
    def is_separator(self) -> bool:
        return not self.label


def _targets(script: str) -> list:
    """Windows a ``clicked`` script opens, in the order the script names them."""
    # `w_taxreport wtmp` ... `openwithparm(wtmp, "OS")` — map local var -> window.
    locals_ = {var: win for win, var in _LOCAL_DECL_RE.findall(script)}
    found, seen = [], set()

    def add(name: str):
        name = locals_.get(name, name)
        if name.startswith("w_") and name not in seen and name not in _NON_TARGETS:
            seen.add(name)
            found.append(name)

    hits = [(m.start(), m.group(1)) for m in _OPEN_STR_RE.finditer(script)]
    hits += [(m.start(), m.group(1).strip('"')) for m in _OPEN_RE.finditer(script)]
    hits += [(m.start(), m.group(1)) for m in _SETFOCUS_RE.finditer(script)]
    for _pos, name in sorted(hits):
        add(name)
    return found


def parse_menu_source(path: str) -> dict:
    """Parse ``m_mainmenu.srm`` into ``{item name: MenuItem}``."""
    text = decode_pb(path)
    # Everything before `end forward` is declarations only — no captions there.
    body = text[text.find("end forward"):] if "end forward" in text else text

    heads = list(_HEADER_RE.finditer(body))
    items: dict[str, MenuItem] = {}
    for idx, head in enumerate(heads):
        name, _kind, parent = head.group(1), head.group(2), head.group(3)
        chunk = body[head.end(): heads[idx + 1].start() if idx + 1 < len(heads) else len(body)]

        item = items.get(name) or MenuItem(name=name)
        items[name] = item
        if parent:
            item.parent = parent

        if (m := _TEXT_RE.search(chunk)):
            raw = _unescape(m.group(1))
            label, _, accel = raw.partition("\t")
            item.label = label.replace("&", "").strip()
            if accel.strip():
                item.shortcut = accel.strip()
        if not item.shortcut and (m := _SHORTCUT_RE.search(chunk)):
            item.shortcut = _decode_shortcut(int(m.group(1)))
        if (m := _VISIBLE_RE.search(chunk)):
            item.visible = m.group(1).lower() == "true"

        order = _ITEM_RE.findall(chunk)
        if order:
            item.order = order
        for m in _CLICKED_RE.finditer(chunk):
            for win in _targets(m.group(1)):
                if win not in item.windows:
                    item.windows.append(win)

    return items


def build_tree(items: dict, root: str | None = None,
               source_refs: dict | None = None) -> list:
    """Convert parsed items into :class:`MenuNode` sections under ``root``.

    ``root`` defaults to the menu object itself — the one item declared with no
    enclosing menu (``global type m_mainmenu from menu``).
    """
    if root is None:
        root = next((n for n, it in items.items() if it.parent is None), "")
    source_refs = source_refs or {}
    # Children of an item: its creation order first, then anything declared
    # `within` it that the order list missed.
    by_parent: dict[str, list] = {}
    for item in items.values():
        if item.parent:
            by_parent.setdefault(item.parent, []).append(item.name)

    def children_of(name: str) -> list:
        ordered = [c for c in items[name].order if c in items]
        seen = set(ordered)
        return ordered + [c for c in by_parent.get(name, []) if c not in seen]

    def node_for(name: str) -> MenuNode | None:
        item = items[name]
        if not item.visible or item.is_separator:
            return None
        node = MenuNode(label=item.label, shortcut=item.shortcut)
        for child in children_of(name):
            if (sub := node_for(child)) is not None:
                node.children.append(sub)
        if not node.children and item.windows:
            # A script may open one of several windows depending on a runtime
            # setting (e.g. Purchase with/without barcode); keep them all.
            node.alternates = list(item.windows)
            node.window = item.windows[0]
            node.source_ref = source_refs.get(node.window, f"{node.window}.srw")
        return node

    if root not in items:
        return []
    sections = []
    for child in children_of(root):
        node = node_for(child)
        # Drop headings that ended up with neither children nor a window.
        if node is not None and (node.children or node.window):
            sections.append(node)
    return sections


def load_menu(srm_path: str, source_refs: dict | None = None,
              prefer: set | None = None) -> list:
    """Parse ``srm_path`` and return the menu sections it defines.

    ``prefer`` is an optional set of window names (typically the hand-converted
    modules) that wins when an item can open more than one window.
    """
    sections = build_tree(parse_menu_source(srm_path), source_refs=source_refs)
    if prefer:
        _apply_preference(sections, prefer, source_refs or {})
    return sections


def _apply_preference(nodes: list, prefer: set, source_refs: dict) -> None:
    for node in nodes:
        _apply_preference(node.children, prefer, source_refs)
        if len(node.alternates) > 1:
            chosen = next((w for w in node.alternates if w.lower() in prefer), None)
            if chosen and chosen != node.window:
                node.window = chosen
                node.source_ref = source_refs.get(chosen, f"{chosen}.srw")


def find_menu_source(base_dir: str) -> str | None:
    """Locate ``m_mainmenu.srm`` inside the exported PowerBuilder tree."""
    for root, _dirs, files in os.walk(base_dir):
        if "m_mainmenu.srm" in files:
            return os.path.join(root, "m_mainmenu.srm")
    return None
