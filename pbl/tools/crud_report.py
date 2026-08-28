"""
Report how much of the application can edit records on the current database.

Runs the same mapping the screens use, for every window in the menu, against
the database configured in ``db_config.ini``, and prints one line per screen:
its table, how many fields matched real columns, and its key. Use it after
pointing the software at the live jewellery database to see exactly which
screens are ready and which need a correction in ``data/field_map.json``.

    python tools/crud_report.py                # summary
    python tools/crud_report.py --details      # every screen
    python tools/crud_report.py --unmapped     # only screens needing attention
"""

from __future__ import annotations

import argparse
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)

from app import catalog, menu_loader, modules  # noqa: E402
from app.pb_parser import INPUT_KINDS  # noqa: E402
from app.services import crud_service  # noqa: E402

EDITABLE_KINDS = INPUT_KINDS | {"checkbox", "radiobutton", "dropdownlistbox", "listbox"}


def rows():
    sections = catalog.load_menu(ROOT)
    seen = set()
    for leaf in menu_loader.iter_leaves(sections):
        window = leaf.window
        if not window or window in seen:
            continue
        seen.add(window)
        if modules.get_factory(window):
            yield leaf.label, window, "module", None
            continue
        win = catalog.load_window(ROOT, window)
        if win is None:
            yield leaf.label, window, "no definition", None
            continue
        if win.grid:
            mapping = crud_service.build_grid_mapping(win.grid)
            if mapping.writable:
                yield leaf.label, window, "grid", mapping
                continue
        controls = [c.name for c in win.controls if c.kind in EDITABLE_KINDS]
        table = win.tables[0] if win.tables else ""
        mapping = crud_service.build_mapping(table, controls, window=window)
        yield leaf.label, window, "fields", mapping


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--details", action="store_true", help="list every screen")
    ap.add_argument("--unmapped", action="store_true",
                    help="list only screens that cannot edit yet")
    args = ap.parse_args()

    hand, grids, editable, readonly, no_table = [], [], [], [], []
    for label, window, kind, mapping in rows():
        if kind == "module":
            hand.append((label, window))
        elif kind == "grid":
            grids.append((label, window, mapping))
        elif mapping is None or not mapping.table:
            no_table.append((label, window))
        elif mapping.writable:
            editable.append((label, window, mapping))
        else:
            readonly.append((label, window, mapping))

    if args.details or args.unmapped:
        for label, window, mapping in (readonly if args.unmapped
                                       else grids + editable + readonly):
            print(f"{window:32s} {label[:34]:34s} {mapping.describe()}")
        print()

    total = len(hand) + len(grids) + len(editable) + len(readonly) + len(no_table)
    print(f"windows                       : {total}")
    print(f"  hand-written modules        : {len(hand)}")
    print(f"  editable DataWindow grid    : {len(grids)}")
    print(f"  fields mapped, full CRUD    : {len(editable)}")
    print(f"  generic, cannot edit yet    : {len(readonly)}")
    print(f"  no table on the screen      : {len(no_table)}")
    if readonly:
        print("\nAdd corrections for the 'cannot edit' screens to "
              "data/field_map.json, then re-run this report.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
