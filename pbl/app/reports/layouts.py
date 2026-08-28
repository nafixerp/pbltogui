"""
The printed forms shipped with the build (``data/layouts.json``).

Loads a stored DataWindow layout back into :class:`app.pb_parser.DWLayout` so
:mod:`app.reports.dw_print` can draw a document on its original designed form.
"""

from __future__ import annotations

import json
import os
from functools import lru_cache

from app.pb_parser import DWLayout, LayoutObject

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LAYOUT_FILE = "layouts.json"


def path(base_dir: str | None = None) -> str:
    return os.path.join(base_dir or BASE_DIR, "data", LAYOUT_FILE)


def available(base_dir: str | None = None) -> bool:
    return os.path.exists(path(base_dir))


@lru_cache(maxsize=4)
def _all(base_dir: str) -> dict:
    with open(path(base_dir), encoding="utf-8") as fh:
        return json.load(fh)


def names(base_dir: str | None = None) -> list:
    if not available(base_dir):
        return []
    return sorted(_all(base_dir or BASE_DIR))


def load(name: str, base_dir: str | None = None) -> DWLayout | None:
    """Return the printed form called ``name``, or ``None``."""
    if not name or not available(base_dir):
        return None
    doc = _all(base_dir or BASE_DIR).get(name)
    if doc is None:
        return None
    layout = DWLayout(name=doc.get("name", name),
                      bands=doc.get("bands", {}),
                      orientation=doc.get("orientation", 0),
                      paper=doc.get("paper", 9),
                      margins=doc.get("margins", {}))
    layout.objects = [LayoutObject(**obj) for obj in doc.get("objects", [])]
    return layout


# Bill windows often choose their form at run time from a setting, so the
# script never names it. Fall back to the forms named after the window.
_STEMS = {"sales": ("sale",), "salesreturn": ("sret", "salesret"),
          "purchase": ("purch",), "gsmith": ("smith", "gsmith"),
          "rcpt": ("rcpt", "receipt"), "pmnt": ("pmnt", "payment"),
          "order": ("order",), "reprenter": ("repair", "remake"),
          "reprno": ("repair", "remake"), "refnenter": ("refn", "refinery"),
          "journal": ("journal",), "otheritemtran": ("oit", "otheritem"),
          "kuricolln": ("kuri", "scheme"), "diamond": ("diamond",)}


# The table a screen is about also says which form its documents print on.
_DOCUMENT_WORDS = ("bill", "print", "cancel", "edit", "entry", "enter",
                   "sale", "purch", "smith", "order", "repair", "refn",
                   "oit", "kuri", "rcpt", "pmnt", "journal", "reprint",
                   "confirm", "memo", "reprno", "reprenter")

_TABLE_STEMS = {"salesm": ("saleprint", "salesprint"), "salesrm": ("sret",),
                "purchasem": ("purchprint", "purchaseprint"),
                "purchaserm": ("purchretprint", "pretprint"),
                "smithm": ("gsmithprint", "smithprint"),
                "orderm": ("orderprint",), "repairm": ("repairprint",),
                "refinerym": ("refnprint", "refineryprint"),
                "oitemtranm": ("oitprint", "otheritemprint"),
                "daybook": ("rcptpmntprint", "voucher"),
                "kuricolln": ("kuriprint", "schemeprint", "passbook"),
                "loan": ("loanprint",), "barcode": ("label",)}


def for_window(window, base_dir: str | None = None) -> list:
    """The printed forms a window uses, most likely one first."""
    known = names(base_dir)
    known_set = set(known)
    found = [w for w in (getattr(window, "prints", []) or []) if w in known_set]

    stem = (getattr(window, "name", "") or "").removeprefix("w_").lower()
    keys = list(_STEMS.get(stem, (stem,)) if stem else ())
    # A screen's table only suggests a form when the screen is about single
    # documents (entry, edit, cancel, reprint) — not for ledgers and lists.
    if any(word in stem for word in _DOCUMENT_WORDS):
        for table in (getattr(window, "tables", []) or [])[:2]:
            keys.extend(_TABLE_STEMS.get(str(table).lower(), ()))
    for key in keys:
        if len(key) < 3:
            continue
        for candidate in known:
            if key in candidate.lower() and candidate not in found:
                found.append(candidate)
    return found[:12]
