"""
Pre-converted application catalog.

A delivered build ships ``data/menu.json`` and ``data/windows.json`` — the menu
object and every window of the original application, already converted by
``tools/build_catalog.py``. Loading those makes the app completely independent
of the PowerBuilder export at runtime, while producing exactly the same objects
the live parsers do (:class:`app.menu_loader.MenuNode`,
:class:`app.pb_parser.Window`), so the UI and the hand-written modules are
unchanged.
"""

from __future__ import annotations

import json
import os
from functools import lru_cache

from app.menu_loader import MenuNode
from app.pb_parser import Control, Window

MENU_FILE = "menu.json"
WINDOWS_FILE = "windows.json"


def data_dir(base_dir: str) -> str:
    return os.path.join(base_dir, "data")


def available(base_dir: str) -> bool:
    d = data_dir(base_dir)
    return (os.path.exists(os.path.join(d, MENU_FILE))
            and os.path.exists(os.path.join(d, WINDOWS_FILE)))


def _node(doc: dict) -> MenuNode:
    node = MenuNode(
        label=doc.get("label", ""),
        window=doc.get("window"),
        source_ref=doc.get("source_ref"),
        shortcut=doc.get("shortcut", ""),
        name=doc.get("name", ""),
        alternates=list(doc.get("alternates", [])),
    )
    node.children = [_node(c) for c in doc.get("children", [])]
    return node


@lru_cache(maxsize=8)
def load_menu(base_dir: str) -> list:
    """Menu sections exactly as :func:`app.pb_menu.load_menu` would build them."""
    with open(os.path.join(data_dir(base_dir), MENU_FILE), encoding="utf-8") as fh:
        doc = json.load(fh)
    return [_node(s) for s in doc.get("sections", [])]


@lru_cache(maxsize=8)
def _windows(base_dir: str) -> dict:
    with open(os.path.join(data_dir(base_dir), WINDOWS_FILE), encoding="utf-8") as fh:
        return json.load(fh)


def load_window(base_dir: str, name: str) -> Window | None:
    """Rebuild one parsed :class:`Window` from the catalog, or ``None``."""
    doc = _windows(base_dir).get(name)
    if doc is None:
        return None
    controls = [Control(**{**{"name": "", "kind": "statictext"}, **c})
                for c in doc.get("controls", [])]
    return Window(
        name=doc["name"], title=doc.get("title", name),
        width=doc.get("width", 2400), height=doc.get("height", 1500),
        controls=controls, tables=doc.get("tables", []),
        source_path=doc.get("source_path", f"{name}.srw"),
        grid=doc.get("grid"),
        report=doc.get("report"),
        opens=list(doc.get("opens", [])),
    )


def window_names(base_dir: str) -> set:
    return set(_windows(base_dir))
