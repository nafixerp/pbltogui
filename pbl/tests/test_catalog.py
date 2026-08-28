"""The delivered build runs off data/menu.json + data/windows.json."""

import os
import sys

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from app import catalog, menu_loader, modules  # noqa: E402

pytestmark = pytest.mark.skipif(not catalog.available(ROOT),
                                reason="no pre-converted catalog in this tree")


def test_menu_sections_and_items():
    sections = catalog.load_menu(ROOT)
    assert [s.label for s in sections] == [
        "File", "Master", "Transactions", "Reports", "Utilities", "Help"]
    leaves = list(menu_loader.iter_leaves(sections))
    assert len(leaves) >= 390
    assert all(leaf.window for leaf in leaves)


def test_shortcuts_survive_the_catalog():
    leaves = list(menu_loader.iter_leaves(catalog.load_menu(ROOT)))
    by_label = {(l.label, l.shortcut) for l in leaves}
    assert ("Bill", "F2") in by_label          # Sales > Bill
    assert ("Transaction", "Ctrl+G") in by_label  # Goldsmith > Transaction


def test_every_menu_window_is_in_the_catalog():
    names = catalog.window_names(ROOT)
    missing = [l.window for l in menu_loader.iter_leaves(catalog.load_menu(ROOT))
               if l.window not in names]
    assert missing == []


def test_windows_rebuild_with_controls_and_tables():
    win = catalog.load_window(ROOT, "w_sales")
    assert win is not None
    assert win.name == "w_sales" and win.width > 0
    assert len(win.controls) > 10
    assert all(c.name and c.kind for c in win.controls)
    assert win.tables  # SQL tables recovered from the original scripts


def test_converted_modules_are_registered():
    for window in ("w_sales", "w_purchase", "w_rcpt", "w_order", "w_item"):
        assert modules.get_factory(window) is not None


def test_unknown_window_returns_none():
    assert catalog.load_window(ROOT, "w_does_not_exist") is None
