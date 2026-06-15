"""
Helpers to translate PowerBuilder presentation primitives to Qt.

* PowerBuilder Units (PBU) -> pixels
* PB packed ``long`` colours (0x00BBGGRR) -> ``#RRGGBB``
* PB ``&`` accelerator text -> Qt ``&`` (already compatible)
* PB control class names -> a normalised widget kind
"""

from __future__ import annotations

# PowerBuilder stores window/control geometry in "PowerBuilder Units".  The
# exact pixel size depends on the display font, but a uniform factor preserves
# the *relative* layout faithfully, which is what matters for the port.  Tuned
# so typical dialogs and buttons land at sensible pixel sizes.
PB_SCALE = float(__import__("os").environ.get("PB_SCALE", "0.30"))


def px(units) -> int:
    try:
        return int(round(float(units) * PB_SCALE))
    except (TypeError, ValueError):
        return 0


def color(value) -> str | None:
    """Convert a PB ``long`` colour to ``#RRGGBB``.

    PB packs colours little-endian as ``red | green<<8 | blue<<16``.  Some
    very large sentinel values (e.g. 536870912 = "transparent/default") are
    returned as ``None`` so the caller can fall back to the Qt default.
    """
    if value is None:
        return None
    try:
        v = int(value)
    except (TypeError, ValueError):
        return None
    if v < 0:
        return None
    # 536870912 (1<<29) and 553648127 etc. are PB "system colour" sentinels.
    if v >= (1 << 24):
        return None
    r = v & 0xFF
    g = (v >> 8) & 0xFF
    b = (v >> 16) & 0xFF
    return f"#{r:02x}{g:02x}{b:02x}"


# PB control class -> normalised kind used by the UI factory.
CONTROL_KINDS = {
    "commandbutton": "button",
    "picturebutton": "button",
    "cb": "button",
    "singlelineedit": "edit",
    "multilineedit": "textarea",
    "editmask": "edit",
    "statictext": "label",
    "statichyperlink": "label",
    "checkbox": "checkbox",
    "radiobutton": "radio",
    "dropdownlistbox": "combo",
    "dropdownpicturelistbox": "combo",
    "listbox": "listbox",
    "datawindow": "datawindow",
    "dw": "datawindow",
    "tab": "tab",
    "groupbox": "groupbox",
    "picture": "picture",
    "line": "line",
    "rectangle": "rectangle",
    "oval": "rectangle",
    "roundrectangle": "rectangle",
    "userobject": "userobject",
    "graph": "graph",
}


def control_kind(pb_class: str) -> str:
    return CONTROL_KINDS.get((pb_class or "").lower(), "unknown")


def clean_text(value: str | None) -> str:
    """PB stores literal text with ``~t`` (tab), ``~r~n`` and ``~"`` escapes."""
    if value is None:
        return ""
    return (value.replace("~t", "\t")
                 .replace("~r~n", "\n")
                 .replace("~n", "\n")
                 .replace("~r", "")
                 .replace('~"', '"')
                 .replace("~~", "~"))
