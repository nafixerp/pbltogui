"""
Pre-convert the PowerBuilder export into a data catalog.

The app can parse ``.srw``/``.srm`` sources at runtime, but a delivered build
should not need the PowerBuilder export at all. This script runs the parsers
once and writes everything the UI needs into JSON:

    data/menu.json      the menu tree (sections, items, shortcuts, windows)
    data/windows.json   every window's title, geometry, controls and tables

Usage (from the folder holding the gmine* source folders)::

    python tools/build_catalog.py --source . --out ../supergold/data
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from dataclasses import asdict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))

from app import menu_loader, pb_menu, pb_parser  # noqa: E402


def node_to_dict(node) -> dict:
    out = {"label": node.label}
    if node.shortcut:
        out["shortcut"] = node.shortcut
    if node.window:
        out["window"] = node.window
    if node.source_ref:
        out["source_ref"] = node.source_ref
    if node.alternates:
        out["alternates"] = node.alternates
    if node.children:
        out["children"] = [node_to_dict(c) for c in node.children]
    return out


def window_to_dict(win) -> dict:
    return {
        "name": win.name,
        "title": win.title,
        "width": win.width,
        "height": win.height,
        "tables": win.tables,
        "source_path": os.path.basename(win.source_path),
        "controls": [
            {k: v for k, v in asdict(c).items() if v not in ("", 0, [], None)}
            | {"name": c.name, "kind": c.kind}
            for c in win.controls
        ],
    }


def build(source_dir: str, out_dir: str) -> tuple:
    srm = pb_menu.find_menu_source(source_dir)
    if not srm:
        raise SystemExit(f"m_mainmenu.srm not found under {source_dir}")

    tree_path = os.path.join(source_dir, "project_tree.txt")
    refs = menu_loader.source_ref_index(tree_path) if os.path.exists(tree_path) else {}

    from app import modules  # imported late: pulls in PySide6-free registry only
    sections = pb_menu.load_menu(srm, source_refs=refs,
                                 prefer=modules.registered_windows())

    windows: dict[str, dict] = {}
    missing: list[str] = []
    for leaf in menu_loader.iter_leaves(sections):
        for name in (leaf.alternates or [leaf.window]):
            if not name or name in windows:
                continue
            path = pb_parser.find_source(f"{name}.srw", source_dir)
            if path is None:
                missing.append(name)
                continue
            windows[name] = window_to_dict(pb_parser.parse_window(path))

    os.makedirs(out_dir, exist_ok=True)
    menu_doc = {"sections": [node_to_dict(s) for s in sections]}
    with open(os.path.join(out_dir, "menu.json"), "w", encoding="utf-8") as fh:
        json.dump(menu_doc, fh, indent=1, ensure_ascii=False)
    with open(os.path.join(out_dir, "windows.json"), "w", encoding="utf-8") as fh:
        json.dump(windows, fh, indent=1, ensure_ascii=False)
    return sections, windows, missing


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--source", default=os.path.dirname(HERE),
                    help="folder containing the gmine* PowerBuilder source folders")
    ap.add_argument("--out", default=os.path.join(os.path.dirname(HERE), "data"),
                    help="output folder for menu.json / windows.json")
    args = ap.parse_args()

    sections, windows, missing = build(os.path.abspath(args.source),
                                       os.path.abspath(args.out))
    leaves = sum(1 for _ in menu_loader.iter_leaves(sections))
    print(f"sections: {len(sections)}  menu items: {leaves}  windows: {len(windows)}")
    if missing:
        print(f"windows with no .srw in the export ({len(missing)}): "
              + ", ".join(sorted(set(missing))))
    print(f"written to {os.path.abspath(args.out)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
