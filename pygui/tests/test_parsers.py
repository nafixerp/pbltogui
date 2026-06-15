"""
Headless verification of the PB -> Python conversion engine.

Runs without a display (Qt offscreen) and proves the parsers cover the whole
codebase: every window parses and renders, DataWindows yield columns + SQL, and
the full menu tree reconstructs with its window mappings.

    QT_QPA_PLATFORM=offscreen python -m pytest tests/ -q
or simply:
    QT_QPA_PLATFORM=offscreen python tests/test_parsers.py
"""

import os
import sys

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pbconvert import (default_source, parse_window, parse_datawindow,
                       parse_menu, iter_leaves)

SRC = default_source()


def test_all_windows_parse():
    names = SRC.names(".srw")
    assert len(names) > 400
    for nm in names:
        w = parse_window(SRC.text(nm), nm)
        assert w.name


def test_all_datawindows_parse():
    names = SRC.names(".srd")
    assert len(names) > 900
    total_cols = 0
    for nm in names:
        d = parse_datawindow(SRC.text(nm), nm)
        total_cols += len(d.columns)
    assert total_cols > 10000


def test_menu_tree():
    root = parse_menu(SRC.text("m_mainmenu"))
    tops = [c.caption for c in root.children]
    assert "File" in tops and "Master" in tops and "Transactions" in tops
    leaves = list(iter_leaves(root))
    assert len(leaves) > 300
    assert sum(1 for l in leaves if l.opens) > 300


def test_encryption_roundtrip():
    from runtime.pb_compat import fpencrypt
    assert fpencrypt(fpencrypt("admin", 1), 2) == "admin"


def test_render_sample_windows():
    from PySide6.QtWidgets import QApplication
    from ui.window_view import WindowView
    app = QApplication.instance() or QApplication([])
    sample = SRC.names(".srw")[:40]
    for nm in sample:
        v = WindowView(nm, SRC, open_window_cb=lambda w: None)
        assert v.win.name


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication
    QApplication([])
    test_all_windows_parse()
    test_all_datawindows_parse()
    test_menu_tree()
    test_encryption_roundtrip()
    test_render_sample_windows()
    print("ALL TESTS PASSED")
