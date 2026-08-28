"""The generic screen really writes to the database (New / Save / Delete)."""

import os
import sys

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

import db  # noqa: E402
from app.pb_parser import Control, Window  # noqa: E402

PySide6 = pytest.importorskip("PySide6.QtWidgets", reason="PySide6 not installed")
from PySide6.QtWidgets import QApplication  # noqa: E402

from app.ui.pb_form import PBWindowForm  # noqa: E402


@pytest.fixture(scope="session")
def qapp():
    return QApplication.instance() or QApplication([])


@pytest.fixture()
def form(tmp_path, monkeypatch, qapp):
    monkeypatch.setattr(db, "ENGINE", "sqlite")
    monkeypatch.setattr(db, "SQLITE_PATH", str(tmp_path / "form.db"))
    db.execute("""CREATE TABLE itemgrp (
        grp_id INTEGER PRIMARY KEY AUTOINCREMENT,
        code TEXT, name TEXT, wastage REAL)""")
    window = Window(
        name="w_itemgrp", title="Item Groups", width=2000, height=1200,
        controls=[
            Control(name="st_1", kind="statictext", text="Code", x=40, y=40,
                    width=200, height=60),
            Control(name="sle_code", kind="singlelineedit", x=260, y=40,
                    width=300, height=60, limit=10),
            Control(name="sle_name", kind="singlelineedit", x=260, y=120,
                    width=600, height=60),
            Control(name="em_wastage", kind="editmask", x=260, y=200,
                    width=300, height=60),
            Control(name="cb_save", kind="commandbutton", text="&Save",
                    x=900, y=40, width=300, height=80),
        ],
        tables=["itemgrp"], source_path="w_itemgrp.srw")
    return PBWindowForm(window)


def type_in(form, **values):
    for name, value in values.items():
        form._inputs[name].setText(value)


def test_screen_maps_its_fields(form):
    assert form.mapping.table == "itemgrp"
    assert form.mapping.fields == {"sle_code": "code", "sle_name": "name",
                                   "em_wastage": "wastage"}
    assert form._editable()
    assert "3 of 3 fields mapped" in form.mapping.describe()


def test_new_record_is_inserted(form):
    type_in(form, sle_code="G1", sle_name="Gold 916", em_wastage="2.5")
    form._save()
    rows = db.fetch_all("SELECT * FROM itemgrp")
    assert len(rows) == 1
    assert (rows[0]["code"], rows[0]["name"], rows[0]["wastage"]) == ("G1", "Gold 916", 2.5)


def test_selecting_a_row_loads_it_and_save_updates_it(form):
    db.execute("INSERT INTO itemgrp (code, name, wastage) VALUES ('S1','Silver',1.0)")
    form._refresh()
    form._grid.selectRow(0)

    assert form._inputs["sle_code"].text() == "S1"
    assert form._inputs["sle_name"].text() == "Silver"

    form._inputs["sle_name"].setText("Silver 925")
    form._save()

    rows = db.fetch_all("SELECT * FROM itemgrp")
    assert len(rows) == 1                       # updated, not duplicated
    assert rows[0]["name"] == "Silver 925"


def test_new_clears_the_form_so_save_inserts_again(form):
    db.execute("INSERT INTO itemgrp (code, name, wastage) VALUES ('A','First',1)")
    form._refresh()
    form._grid.selectRow(0)
    form._new()
    assert form._inputs["sle_code"].text() == "" and form._current_row is None

    type_in(form, sle_code="B", sle_name="Second", em_wastage="3")
    form._save()
    assert len(db.fetch_all("SELECT * FROM itemgrp")) == 2


def test_delete_removes_the_selected_row(form, monkeypatch):
    db.execute("INSERT INTO itemgrp (code, name, wastage) VALUES ('D','Doomed',0)")
    form._refresh()
    form._grid.selectRow(0)
    monkeypatch.setattr(PBWindowForm, "_confirm", lambda self, q: True)
    form._delete()
    assert db.fetch_all("SELECT * FROM itemgrp") == []


def test_delete_is_cancellable(form, monkeypatch):
    db.execute("INSERT INTO itemgrp (code, name, wastage) VALUES ('K','Keep',0)")
    form._refresh()
    form._grid.selectRow(0)
    monkeypatch.setattr(PBWindowForm, "_confirm", lambda self, q: False)
    form._delete()
    assert len(db.fetch_all("SELECT * FROM itemgrp")) == 1


def test_bad_number_is_reported_not_written(form, monkeypatch):
    warned = []
    monkeypatch.setattr("app.ui.pb_form.QMessageBox.warning",
                        lambda *a, **k: warned.append(a[-1]))
    type_in(form, sle_code="X", sle_name="Bad", em_wastage="abc")
    form._save()
    assert db.fetch_all("SELECT * FROM itemgrp") == []
    assert warned and "not a number" in warned[0]


def test_search_box_filters_the_grid(form):
    db.execute("INSERT INTO itemgrp (code, name) VALUES ('P','Platinum')")
    db.execute("INSERT INTO itemgrp (code, name) VALUES ('D','Diamond')")
    form._search.setText("plat")
    form._refresh()
    assert [r["name"] for r in form._rows] == ["Platinum"]


def test_screen_without_a_table_stays_read_only(qapp, monkeypatch, tmp_path):
    monkeypatch.setattr(db, "ENGINE", "sqlite")
    monkeypatch.setattr(db, "SQLITE_PATH", str(tmp_path / "empty.db"))
    window = Window(name="w_about", title="About", width=800, height=600,
                    controls=[Control(name="st_1", kind="statictext", text="Hi")],
                    tables=[], source_path="w_about.srw")
    form = PBWindowForm(window)
    assert form.mapping is None and not form._editable()


# --- DataWindow (grid) screens --------------------------------------------

@pytest.fixture()
def grid_form(tmp_path, monkeypatch, qapp):
    """A screen that edits its table through its DataWindow, like the original."""
    monkeypatch.setattr(db, "ENGINE", "sqlite")
    monkeypatch.setattr(db, "SQLITE_PATH", str(tmp_path / "grid.db"))
    db.execute("CREATE TABLE itemsubgrp (code TEXT, name TEXT)")
    window = Window(
        name="w_itemsubgrp", title="Sub Groups", width=1600, height=1000,
        controls=[Control(name="dw_1", kind="datawindow", x=40, y=40,
                          width=1200, height=600, dataobject="d_itemsubgrpmaster")],
        tables=["barcode"],          # the window's SQL mentions another table…
        source_path="w_itemsubgrp.srw",
        grid={"control": "dw_1", "dataobject": "d_itemsubgrpmaster",
              "table": "itemsubgrp", "keys": ["code"],
              "columns": [{"name": "code", "label": "Code", "type": "char"},
                          {"name": "name", "label": "Name", "type": "char"}]})
    return PBWindowForm(window)


def set_cell(form, row, col, text):
    from PySide6.QtWidgets import QTableWidgetItem
    form._grid.setItem(row, col, QTableWidgetItem(text))


def test_datawindow_defines_table_and_key(grid_form):
    assert grid_form.grid_mode                       # …the DataWindow wins
    assert grid_form.mapping.table == "itemsubgrp"
    assert grid_form.mapping.pk == ["code"]
    assert grid_form._grid_headers() == ["Code", "Name"]


def test_add_row_and_save_inserts(grid_form):
    grid_form._add_row()
    set_cell(grid_form, 0, 0, "SG1")
    set_cell(grid_form, 0, 1, "Rings")
    grid_form._save_grid()
    rows = db.fetch_all("SELECT * FROM itemsubgrp")
    assert [(r["code"], r["name"]) for r in rows] == [("SG1", "Rings")]


def test_editing_a_cell_updates_that_record(grid_form):
    db.execute("INSERT INTO itemsubgrp VALUES ('SG2','Chain')")
    grid_form._refresh()
    set_cell(grid_form, 0, 1, "Chains")
    grid_form._save_grid()
    rows = db.fetch_all("SELECT * FROM itemsubgrp")
    assert len(rows) == 1 and rows[0]["name"] == "Chains"


def test_unchanged_rows_are_not_rewritten(grid_form):
    db.execute("INSERT INTO itemsubgrp VALUES ('SG3','Bangle')")
    grid_form._refresh()
    grid_form._save_grid()
    assert grid_form._status.text().startswith("Nothing changed")


def test_empty_new_row_is_ignored(grid_form):
    grid_form._add_row()
    grid_form._save_grid()
    assert db.fetch_all("SELECT * FROM itemsubgrp") == []


def test_delete_row_removes_the_record(grid_form, monkeypatch):
    db.execute("INSERT INTO itemsubgrp VALUES ('SG4','Studs')")
    grid_form._refresh()
    grid_form._grid.setCurrentCell(0, 0)
    monkeypatch.setattr(PBWindowForm, "_confirm", lambda self, q: True)
    grid_form._delete_grid_row()
    assert db.fetch_all("SELECT * FROM itemsubgrp") == []


def test_unsaved_row_is_just_dropped(grid_form):
    grid_form._add_row()
    set_cell(grid_form, 0, 0, "TMP")
    grid_form._delete_grid_row()
    assert grid_form._grid.rowCount() == 0
    assert db.fetch_all("SELECT * FROM itemsubgrp") == []


# --- access control --------------------------------------------------------

def test_denied_menu_items_are_blocked(qapp, tmp_path, monkeypatch):
    """Master > Users > Provide Access blocks items for a user (userd)."""
    monkeypatch.setattr(db, "ENGINE", "sqlite")
    monkeypatch.setattr(db, "SQLITE_PATH", str(tmp_path / "acl.db"))
    db.execute("CREATE TABLE userd (code TEXT, menuitem TEXT)")
    db.execute("INSERT INTO userd VALUES ('U1','m_trans_sales')")
    assert db.get_denied_menuitems("U1") == {"m_trans_sales"}
    assert db.get_denied_menuitems("U2") == set()
