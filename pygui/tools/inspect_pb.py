"""
Command-line inspector for the converted PowerBuilder source.

Useful when porting a specific screen's business logic: it prints a window's
controls and the verbatim PowerScript of each event, a DataWindow's columns
and translated SQL, or the menu tree.

    python tools/inspect_pb.py menu
    python tools/inspect_pb.py window w_sales
    python tools/inspect_pb.py datawindow d_sales
    python tools/inspect_pb.py stats
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pbconvert import (default_source, parse_window, parse_datawindow,
                       parse_menu)


def show_menu(src):
    root = parse_menu(src.text("m_mainmenu"))

    def walk(node, depth=0):
        for ch in node.children:
            tgt = f"  -> {ch.opens}" if ch.opens else ""
            print("  " * depth + f"{ch.caption}{tgt}")
            walk(ch, depth + 1)
    walk(root)


def show_window(src, name):
    w = parse_window(src.text(name), name)
    print(f"# Window {w.name}  title={w.title!r}  "
          f"size={w.width}x{w.height}  type={w.windowtype}")
    print(f"# {len(w.controls)} controls\n")
    for c in w.controls:
        print(f"- {c.name} ({c.pb_class}) "
              f"x={c.props.get('x')} y={c.props.get('y')} "
              f"w={c.props.get('width')} h={c.props.get('height')} "
              f"text={c.props.get('text')!r}")
        for ev, script in c.events.items():
            print(f"    event {ev}:")
            for line in script.strip().splitlines():
                print(f"      {line}")
    if w.events:
        print("\n# window events")
        for ev, script in w.events.items():
            print(f"  event {ev}:")
            for line in script.strip().splitlines():
                print(f"    {line}")


def show_datawindow(src, name):
    d = parse_datawindow(src.text(name), name)
    print(f"# DataWindow {d.name}  update_table={d.update_table!r}")
    print(f"# retrieve SQL: {d.retrieve_sql or '(none translated)'}\n")
    for c in sorted(d.columns, key=lambda c: c.order):
        flags = "".join(["K" if c.key else "", "U" if c.update else ""])
        print(f"- {c.name:20} {c.type:8} db={c.dbname:30} "
              f"head={c.heading!r} {flags}")


def show_stats(src):
    c = src.counts()
    print("Object counts:")
    for ext in (".srw", ".srd", ".srm", ".sru", ".srs", ".srf"):
        print(f"  {ext}: {c.get(ext, 0)}")


def main(argv):
    src = default_source()
    if not argv:
        print(__doc__)
        return 1
    cmd = argv[0]
    if cmd == "menu":
        show_menu(src)
    elif cmd == "window" and len(argv) > 1:
        show_window(src, argv[1])
    elif cmd == "datawindow" and len(argv) > 1:
        show_datawindow(src, argv[1])
    elif cmd == "stats":
        show_stats(src)
    else:
        print(__doc__)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
