"""
Opening one screen from another.

The original application chains screens: a bill-number window looks a document
up and opens the entry screen for it, a cancel window opens the viewer, and so
on. The window scripts name those targets, `tools/build_catalog.py` records
them, and this tiny registry lets a form ask the main window to open one —
without a form needing to know about the main window at all.
"""

from __future__ import annotations

_opener = None


def set_opener(fn):
    """Called once by the main window."""
    global _opener
    _opener = fn


def open_window(window: str, params: dict | None = None, label: str = "") -> bool:
    """Open ``window`` as a new tab, seeded with ``params``. False if not wired."""
    if _opener is None or not window:
        return False
    _opener(window, params or {}, label)
    return True


def available() -> bool:
    return _opener is not None
