"""
Collect the printed forms of the application into ``data/layouts.json``.

Bills, memos, vouchers and certificates are printed through their own
DataWindow: the ``.srd`` holds the bands and every label, column, total and
line of the designed form. This stores those layouts so the software can print
a document exactly as the original printed it, without the export.

    python tools/build_layouts.py --source <export folder>
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import asdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)

from app import pb_parser  # noqa: E402

# A DataWindow is a printed form when its name says so — but not the little
# code/help pickers that merely have "bill" in the name.
FORM_WORDS = ("print", "slip", "voucher", "memo", "certificate", "invoice",
              "passbook", "label", "receipt")
NOT_FORM = ("code", "help", "hlp", "list", "lookup", "search")


def is_form(name: str) -> bool:
    lower = name.lower()
    if any(word in lower for word in NOT_FORM):
        return False
    return any(word in lower for word in FORM_WORDS)


def collect(source: str) -> dict:
    layouts = {}
    for root, _dirs, files in os.walk(source):
        for fname in files:
            if not fname.lower().endswith(".srd"):
                continue
            name = os.path.splitext(fname)[0]
            if not is_form(name):
                continue
            try:
                layout = pb_parser.parse_layout(os.path.join(root, fname))
            except Exception:
                continue
            if not layout.objects or not layout.bands:
                continue
            doc = asdict(layout)
            doc["objects"] = [
                {k: v for k, v in obj.items() if v not in ("", 0, False)}
                | {"kind": obj["kind"], "band": obj["band"]}
                for obj in doc["objects"]]
            layouts[name] = doc
    return layouts


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--source", required=True)
    ap.add_argument("--out", default=os.path.join(ROOT, "data", "layouts.json"))
    args = ap.parse_args()

    layouts = collect(os.path.abspath(args.source))
    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as fh:
        json.dump(layouts, fh, separators=(",", ":"), ensure_ascii=False)
    objects = sum(len(l["objects"]) for l in layouts.values())
    print(f"printed forms: {len(layouts)}  objects: {objects}  -> {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
