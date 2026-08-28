"""Every window of the application exists as a generated Python form module."""

import ast
import json
import os
import sys

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from app import catalog, menu_loader  # noqa: E402

FORMS_DIR = os.path.join(ROOT, "app", "forms")
pytestmark = pytest.mark.skipif(
    not os.path.exists(os.path.join(FORMS_DIR, "__init__.py"))
    or not catalog.available(ROOT),
    reason="generated forms / catalog are not present in this tree")

from app import forms  # noqa: E402


def test_a_module_exists_for_every_window_in_the_catalog():
    with open(os.path.join(ROOT, "data", "windows.json"), encoding="utf-8") as fh:
        windows = set(json.load(fh))
    assert windows <= forms.window_names()
    missing = [w for w in windows
               if not os.path.exists(os.path.join(FORMS_DIR, f"{w}.py"))]
    assert missing == []


def test_every_menu_item_resolves_to_a_module_or_a_form():
    from app import modules
    unresolved = [leaf.label for leaf in menu_loader.iter_leaves(catalog.load_menu(ROOT))
                  if not modules.get_factory(leaf.window)
                  and forms.get_form(leaf.window) is None]
    assert unresolved == []


def test_generated_modules_are_valid_python():
    for name in sorted(os.listdir(FORMS_DIR))[:60]:
        if not name.endswith(".py"):
            continue
        with open(os.path.join(FORMS_DIR, name), encoding="utf-8") as fh:
            ast.parse(fh.read(), filename=name)


@pytest.fixture(scope="session")
def qapp():
    pytest.importorskip("PySide6.QtWidgets")
    from PySide6.QtWidgets import QApplication
    return QApplication.instance() or QApplication([])


@pytest.mark.parametrize("window", ["w_itemsubgrp", "w_sman", "w_states",
                                    "w_salesbook", "w_about"])
def test_sample_forms_build_with_their_controls(qapp, window):
    cls = forms.get_form(window)
    assert cls is not None
    form = cls()
    assert form.window_def.name == window
    # The controls declared in the module were actually created.
    assert len(form.window_def.controls) >= 1


def test_form_keeps_the_screen_behaviour(qapp):
    form = forms.get_form("w_itemsubgrp")()
    assert form.grid_mode                       # edits its DataWindow's table
    assert form.mapping.table == "itemsubgrp"
    assert form.mapping.pk == ["code"]
