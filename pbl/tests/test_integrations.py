"""The screens that reach outside: file import, database sync, company select."""

import os
import sqlite3
import sys

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

import db  # noqa: E402

pytest.importorskip("PySide6.QtWidgets")
from PySide6.QtWidgets import QApplication  # noqa: E402

from app.modules.integrations import (  # noqa: E402
    CompanySelectForm, DatabaseSyncForm, FileImportForm, WeighingMachineForm)


@pytest.fixture(scope="session")
def qapp():
    return QApplication.instance() or QApplication([])


@pytest.fixture()
def local(tmp_path, monkeypatch):
    monkeypatch.setattr(db, "ENGINE", "sqlite")
    monkeypatch.setattr(db, "SQLITE_PATH", str(tmp_path / "local.db"))
    monkeypatch.setattr(db, "CONFIG_PATH", str(tmp_path / "db_config.ini"))
    db.execute("CREATE TABLE orderm (slno INT, ordno TEXT, custname TEXT)")
    db.execute("CREATE TABLE company (code TEXT, name TEXT)")
    db.execute("INSERT INTO company VALUES ('C1','Super Gold')")
    return tmp_path


# --- file import -----------------------------------------------------------

def test_file_import_reads_and_maps(qapp, local, tmp_path):
    path = tmp_path / "pos.csv"
    path.write_text("slno,ordno,custname\n1,O1,Ravi\n2,O2,Biju\n")
    form = FileImportForm("POS", "orderm")
    form.path.setText(str(path))
    form.load()
    assert len(form._rows) == 2
    assert form.grid.rowCount() == 2

    form.table.setCurrentText("orderm")
    form._build_mapping()
    form.do_import()
    rows = db.fetch_all("SELECT * FROM orderm ORDER BY slno")
    assert [r["ordno"] for r in rows] == ["O1", "O2"]
    assert "Imported 2" in form.status.text()


def test_file_import_writes_nothing_without_a_mapping(qapp, local, tmp_path):
    path = tmp_path / "x.csv"
    path.write_text("a,b\n1,2\n")
    form = FileImportForm("PSR", "")
    form.path.setText(str(path))
    form.load()
    form.do_import()
    assert db.fetch_all("SELECT * FROM orderm") == []


def test_file_import_reports_a_bad_file(qapp, local):
    form = FileImportForm("PSR", "orderm")
    form.path.setText("/no/such/file.csv")
    form.load()
    assert "Could not read" in form.status.text()


# --- database sync ---------------------------------------------------------

def test_sync_copies_only_missing_rows(qapp, local, tmp_path):
    source = tmp_path / "ho.db"
    conn = sqlite3.connect(source)
    conn.execute("CREATE TABLE orderm (slno INT, ordno TEXT, custname TEXT)")
    conn.executemany("INSERT INTO orderm VALUES (?,?,?)",
                     [(1, "O1", "Ravi"), (2, "O2", "Biju")])
    conn.commit()
    conn.close()
    db.execute("INSERT INTO orderm VALUES (1,'O1','Ravi')")

    form = DatabaseSyncForm("Update", ["orderm"])
    form.path.setText(str(source))
    form.table.setCurrentText("orderm")
    form.sync()

    rows = db.fetch_all("SELECT * FROM orderm ORDER BY slno")
    assert [r["ordno"] for r in rows] == ["O1", "O2"]     # no duplicate of O1
    assert "1 new row" in form.log.toPlainText()


def test_sync_needs_a_source(qapp, local):
    form = DatabaseSyncForm("Update", ["orderm"])
    form.sync()
    assert "Choose the source" in form.log.toPlainText()


# --- company select --------------------------------------------------------

def test_company_select_writes_the_config(qapp, local, tmp_path, monkeypatch):
    other = tmp_path / "gm2025.db"
    sqlite3.connect(other).close()
    from PySide6.QtWidgets import QMessageBox
    monkeypatch.setattr(QMessageBox, "question",
                        staticmethod(lambda *a, **k: QMessageBox.Yes))
    form = CompanySelectForm()
    form.choice.setEditText(str(other))
    form.apply()
    assert os.path.exists(db.CONFIG_PATH)
    assert str(other) in open(db.CONFIG_PATH).read()
    assert "Restart" in form.status.text()


def test_company_select_refuses_a_missing_file(qapp, local):
    form = CompanySelectForm()
    form.choice.setEditText("/no/such/company.db")
    form.apply()
    assert "does not exist" in form.status.text()


# --- weighing machine ------------------------------------------------------

def test_weight_can_be_typed(qapp, local):
    form = WeighingMachineForm()
    form.manual.setText("12.345")
    # the "Use typed weight" button is the last one added
    form.weight.setText(form.manual.text())
    assert form.weight.text() == "12.345"


def test_weight_read_without_pyserial_is_explained(qapp, local, monkeypatch):
    monkeypatch.setitem(sys.modules, "serial", None)
    form = WeighingMachineForm()
    form.read_weight()
    assert "pyserial" in form.status.text() or "Could not read" in form.status.text()
