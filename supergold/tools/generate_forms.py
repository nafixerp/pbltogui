"""
Generate one Python form module per window of the original application.

The catalog (``data/windows.json``) already holds every window: its size, its
controls at their original positions, the table it edits and the query it
displays. This writes that out as ordinary PySide6 code — ``app/forms/w_x.py``
per screen, plus a registry — so the application is real, readable Python
rather than a renderer driven by data at run time.

The generated classes inherit :class:`app.ui.form_base.GeneratedForm`, which
supplies the record editing, data view, search and export behaviour.

    python tools/generate_forms.py            # writes app/forms/
    python tools/generate_forms.py --check    # report only, write nothing
"""

from __future__ import annotations

import argparse
import json
import keyword
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)

from app import catalog, menu_loader  # noqa: E402

HEADER = '''"""{title} — {window}.

Generated from the PowerBuilder window ``{source}`` by
``tools/generate_forms.py``. It is ordinary PySide6 code: the controls below
are the original ones, at their original positions. Behaviour (record editing,
the data view over this window's own query, search and export) comes from
:class:`app.ui.form_base.GeneratedForm`.

Re-running the generator overwrites this file. Put hand-written business logic
in ``app/modules/`` instead — a module registered there takes precedence.
"""

from app.pb_parser import Window
from app.ui.form_base import GeneratedForm

WINDOW = Window(
    name={window!r},
    title={title!r},
    width={width},
    height={height},
    controls=[],
    tables={tables!r},
    source_path={source!r},{extra}
)


class {cls}(GeneratedForm):
    """{title}"""

    WINDOW = WINDOW

    def build_controls(self):
{body}
'''


def class_name(window: str, title: str) -> str:
    base = re.sub(r"[^A-Za-z0-9]+", " ", title or window).title().replace(" ", "")
    base = re.sub(r"^\d+", "", base) or re.sub(r"[^A-Za-z0-9]+", "", window).title()
    if not base or keyword.iskeyword(base):
        base = re.sub(r"[^A-Za-z0-9]+", "", window).title()
    return f"{base}Form"


def control_line(ctrl: dict) -> str:
    args = [repr(ctrl.get("kind", "statictext")), repr(ctrl.get("name", "")),
            str(ctrl.get("x", 0)), str(ctrl.get("y", 0)),
            str(ctrl.get("width", 0)), str(ctrl.get("height", 0))]
    for key in ("text", "limit", "items", "dataobject", "taborder"):
        value = ctrl.get(key)
        if value:
            args.append(f"{key}={value!r}")
    return "        self.add(" + ", ".join(args) + ")"


def module_source(window: str, doc: dict, title: str) -> str:
    extra = ""
    if doc.get("grid"):
        extra += f"\n    grid={doc['grid']!r},"
    if doc.get("report"):
        extra += f"\n    report={doc['report']!r},"
    body = "\n".join(control_line(c) for c in doc.get("controls", []))
    if not body:
        body = "        pass"
    return HEADER.format(
        title=title or doc.get("title") or window,
        window=window,
        source=doc.get("source_path", f"{window}.srw"),
        width=doc.get("width", 2400), height=doc.get("height", 1500),
        tables=doc.get("tables", []), extra=extra,
        cls=class_name(window, title or doc.get("title", "")),
        body=body)


REGISTRY = '''"""
Every screen of the application, as a generated Python form module.

One module per window (see ``tools/generate_forms.py``). The registry is lazy:
a form module is imported the first time its screen is opened.

Hand-written implementations in :mod:`app.modules` always win — the main window
asks there first.
"""

from __future__ import annotations

import importlib

# window name -> (module, class)
FORMS = {{
{entries}
}}


def get_form(window: str):
    """Return the generated form class for ``window``, or ``None``."""
    entry = FORMS.get((window or "").lower())
    if entry is None:
        return None
    module = importlib.import_module(f"app.forms.{{entry[0]}}")
    return getattr(module, entry[1])


def window_names() -> set:
    return set(FORMS)
'''


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", default=os.path.join(ROOT, "app", "forms"))
    ap.add_argument("--check", action="store_true", help="report only")
    args = ap.parse_args()

    with open(os.path.join(ROOT, "data", "windows.json"), encoding="utf-8") as fh:
        windows = json.load(fh)
    titles = {}
    for leaf in menu_loader.iter_leaves(catalog.load_menu(ROOT)):
        titles.setdefault(leaf.window, leaf.label)

    if args.check:
        print(f"{len(windows)} windows would be generated into {args.out}")
        return 0

    os.makedirs(args.out, exist_ok=True)
    for stale in os.listdir(args.out):
        if stale.endswith(".py"):
            os.remove(os.path.join(args.out, stale))

    entries = []
    for window in sorted(windows):
        doc = windows[window]
        cls = class_name(window, titles.get(window, doc.get("title", "")))
        with open(os.path.join(args.out, f"{window}.py"), "w", encoding="utf-8") as fh:
            fh.write(module_source(window, doc, titles.get(window, "")))
        entries.append(f'    "{window}": ("{window}", "{cls}"),')

    with open(os.path.join(args.out, "__init__.py"), "w", encoding="utf-8") as fh:
        fh.write(REGISTRY.format(entries="\n".join(entries)))

    print(f"generated {len(windows)} form modules in {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
