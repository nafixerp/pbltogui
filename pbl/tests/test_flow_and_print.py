"""Screen-to-screen flow (bill pickers) and printing."""

import os
import sys

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

import db  # noqa: E402
from app import catalog  # noqa: E402

pytest.importorskip("PySide6.QtWidgets")
from PySide6.QtWidgets import QApplication  # noqa: E402

from app.reports.generic import seed_value  # noqa: E402
from app.ui import navigation  # noqa: E402
from app.ui.printing import render_html  # noqa: E402


@pytest.fixture(scope="session")
def qapp():
    return QApplication.instance() or QApplication([])


# --- carrying a record to the next screen ---------------------------------

def test_seed_value_matches_a_retrieval_argument():
    row = {"slno": 101, "billno": "B101", "salesm_tdate": "2026-06-01"}
    assert seed_value("rslno", row) == 101
    assert seed_value("rbillno", row) == "B101"
    assert seed_value("rtdate", row) == "2026-06-01"   # via salesm_tdate
    assert seed_value("rmissing", row) is None
    assert seed_value("rslno", {}) is None


def test_navigation_registry(qapp):
    opened = []
    navigation.set_opener(lambda w, p, l: opened.append((w, p, l)))
    assert navigation.open_window("w_sales", {"slno": 5}, "Edit")
    assert opened == [("w_sales", {"slno": 5}, "Edit")]
    navigation.set_opener(None)
    assert not navigation.open_window("w_sales")


@pytest.mark.skipif(not catalog.available(ROOT), reason="no catalog in this tree")
def test_picker_screens_know_where_they_lead(qapp):
    from app import forms
    db.init_db()
    form = forms.get_form("w_seditbillno")()
    targets = form._flow_targets()
    assert "w_sales" in targets
    assert all("help" not in t for t in targets[:1])   # entry screen first


@pytest.mark.skipif(not catalog.available(ROOT), reason="no catalog in this tree")
def test_flow_opens_the_target_with_the_selected_record(qapp):
    from app import forms
    db.init_db()
    db.execute("DELETE FROM refinerym")
    db.execute("INSERT INTO refinerym (slno, docno, tdate) VALUES (7,'R7','2026-06-02')")
    opened = {}
    navigation.set_opener(lambda w, p, l: opened.update({"window": w, "params": p}))
    form = forms.get_form("w_refneditno")()
    if form._rows:
        form._grid.selectRow(0)
    elif form._view and form._view._rows:
        form._view._grid.setCurrentCell(0, 0)
    form._open_next()
    navigation.set_opener(None)
    assert opened["window"] == "w_refnenter"
    assert opened["params"].get("docno") == "R7"


# --- printing --------------------------------------------------------------

def test_printed_document_contains_the_rows():
    html = render_html("Sales Book", ["billno", "amount"],
                       [{"billno": "B1", "amount": 100},
                        {"billno": "B2", "amount": None}])
    assert "<h3" in html and "Sales Book" in html
    assert "B1" in html and "100" in html
    assert "2 rows" in html
    assert html.count("<tr") == 3           # header + two rows


def test_printed_document_escapes_content():
    html = render_html("T", ["c"], [{"c": "<script>x</script>"}])
    assert "<script>" not in html and "&lt;script&gt;" in html
