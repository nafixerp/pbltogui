"""Stock transfer, stock add/less and the settings screens."""

import os
import sys

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

import db  # noqa: E402
from app.services import stock_service as ss  # noqa: E402

pytest.importorskip("PySide6.QtWidgets")
from PySide6.QtWidgets import QApplication  # noqa: E402


@pytest.fixture(scope="session")
def qapp():
    return QApplication.instance() or QApplication([])


@pytest.fixture()
def stock(tmp_path, monkeypatch):
    monkeypatch.setattr(db, "ENGINE", "sqlite")
    monkeypatch.setattr(db, "SQLITE_PATH", str(tmp_path / "stock.db"))
    db.execute("""CREATE TABLE items (code TEXT, qty INT, weight REAL,
                  stonewgt REAL, qtyb INT, weightb REAL, stonewgtb REAL, cost REAL)""")
    db.execute("""CREATE TABLE itemsstk (code TEXT, stktype TEXT, qty INT,
                  weight REAL, stonewgt REAL, qtyb INT, weightb REAL,
                  stonewgtb REAL)""")
    db.execute("""CREATE TABLE itemadj (slno INT, tdate DATE, fromcode TEXT,
                  tocode TEXT, fromqty INT, toqty INT, fromwgt REAL, towgt REAL,
                  fromstwgt REAL, tostwgt REAL, fromstktype TEXT, tostktype TEXT,
                  control INT, part TEXT)""")
    db.execute("INSERT INTO items VALUES ('G22',10,100.0,0,10,100.0,0,3000)")
    db.execute("INSERT INTO items VALUES ('G18',0,0.0,0,0,0.0,0,2500)")
    db.execute("CREATE TABLE generali (code TEXT, cvalue TEXT)")
    return tmp_path


def wgt(code):
    return db.fetch_one("SELECT weight, qty FROM items WHERE code = ?", (code,))


def test_transfer_moves_weight_between_items(stock):
    ss.transfer_stock("G22", "G18", qty=2, weight=25.0)
    assert wgt("G22")["weight"] == pytest.approx(75.0)
    assert wgt("G18")["weight"] == pytest.approx(25.0)
    assert wgt("G22")["qty"] == 8 and wgt("G18")["qty"] == 2


def test_transfer_records_the_entry(stock):
    slno = ss.transfer_stock("G22", "G18", weight=5.0)
    row = db.fetch_one("SELECT * FROM itemadj WHERE slno = ?", (slno,))
    assert row["fromcode"] == "G22" and row["tocode"] == "G18"
    assert row["fromwgt"] == pytest.approx(5.0)


def test_transfer_needs_two_different_items(stock):
    with pytest.raises(ValueError):
        ss.transfer_stock("G22", "G22", weight=1)
    with pytest.raises(ValueError):
        ss.transfer_stock("G22", "", weight=1)


def test_transfer_needs_something_to_move(stock):
    with pytest.raises(ValueError):
        ss.transfer_stock("G22", "G18")


def test_add_and_less_stock(stock):
    ss.add_less_stock("G22", weight=10.0, add=True)
    assert wgt("G22")["weight"] == pytest.approx(110.0)
    ss.add_less_stock("G22", weight=30.0, add=False)
    assert wgt("G22")["weight"] == pytest.approx(80.0)
    assert len(db.fetch_all("SELECT * FROM itemadj")) == 2


def test_stock_type_rows_follow_the_item(stock):
    db.execute("INSERT INTO itemsstk VALUES ('G22','C1',10,100.0,0,10,100.0,0)")
    db.execute("INSERT INTO itemsstk VALUES ('G18','C2',0,0,0,0,0,0)")
    ss.transfer_stock("G22", "G18", weight=10.0, from_stktype="C1", to_stktype="C2")
    assert db.fetch_one("SELECT weight FROM itemsstk WHERE stktype='C1'")["weight"] \
        == pytest.approx(90.0)
    assert db.fetch_one("SELECT weight FROM itemsstk WHERE stktype='C2'")["weight"] \
        == pytest.approx(10.0)


# --- the screens -----------------------------------------------------------

def test_transfer_screen_saves(qapp, stock):
    from app.modules.extras import StockTransferForm
    form = StockTransferForm()
    form.from_code.setText("G22")
    form.to_code.setText("G18")
    form.weight.setText("12.5")
    form.save()
    assert "Transferred" in form.status.text()
    assert wgt("G18")["weight"] == pytest.approx(12.5)


def test_transfer_screen_reports_a_bad_entry(qapp, stock, monkeypatch):
    from app.modules.extras import StockTransferForm
    warned = []
    monkeypatch.setattr("app.modules.extras.QMessageBox.warning",
                        lambda *a, **k: warned.append(a[-1]))
    form = StockTransferForm()
    form.save()                                   # nothing filled in
    assert warned and "from-item" in warned[0]


def test_settings_screen_writes_key_values(qapp, stock):
    from app.modules.extras import SettingsForm
    form = SettingsForm(["generali"], "Settings")
    form.key.setText("BILLPREFIX")
    form.value.setText("GK")
    form.save()
    assert db.fetch_one("SELECT cvalue FROM generali WHERE code='BILLPREFIX'")["cvalue"] == "GK"
    form.value.setText("SG")
    form.save()                                    # updates, not duplicates
    assert len(db.fetch_all("SELECT * FROM generali")) == 1
    form.delete()
    assert db.fetch_all("SELECT * FROM generali") == []


def test_order_block_screen(qapp, stock):
    from app.modules.extras import OrderBlockForm
    db.execute("CREATE TABLE orderm (slno INT, ordno TEXT, tdate DATE, "
               "custname TEXT, blocked TEXT, status INT)")
    db.execute("INSERT INTO orderm VALUES (1,'O1','2026-06-01','Ravi','N',0)")
    form = OrderBlockForm()
    form.ordno.setText("O1")
    form.set_blocked("Y")
    assert db.fetch_one("SELECT blocked FROM orderm")["blocked"] == "Y"
    form.set_blocked("N")
    assert db.fetch_one("SELECT blocked FROM orderm")["blocked"] == "N"


def test_staff_log_screen(qapp, stock):
    from app.modules.extras import StaffLogForm
    db.execute("CREATE TABLE staff_log (scode TEXT, idno TEXT, tdate DATE, "
               "ttime TEXT, status TEXT)")
    form = StaffLogForm()
    form.scode.setText("S1")
    form.add()
    row = db.fetch_one("SELECT * FROM staff_log")
    assert row["scode"] == "S1" and row["status"] == "IN"


def test_incharge_change_stores_the_setting(qapp, stock):
    from app.modules.extras import InchargeChangeForm
    form = InchargeChangeForm()
    form.person.setEditText("RAJU")
    form.apply()
    assert db.fetch_one("SELECT cvalue FROM generali WHERE code='INCHARGE'")["cvalue"] == "RAJU"
    form.person.setEditText("SUNIL")
    form.apply()
    assert db.fetch_one("SELECT cvalue FROM generali WHERE code='INCHARGE'")["cvalue"] == "SUNIL"
    assert "SUNIL" in form.status.text()


def test_all_reports_screen_runs_one(qapp, stock):
    from app.modules.extras import AllReportsForm
    db.execute("CREATE TABLE accountm (accode TEXT, name TEXT, actype1 TEXT, "
               "tplpos INT, bshead TEXT, opbal REAL, opbalb REAL, grcode TEXT)")
    db.execute("CREATE TABLE daybook (slno INT, accode TEXT, tdate DATE, amount REAL)")
    db.execute("INSERT INTO accountm VALUES ('CASH','Cash','A',0,'',500,0,'')")
    form = AllReportsForm()
    form.report.setCurrentText("Balance Sheet")
    form.run()
    assert form._rows and "Balance Sheet" in form.status.text()


def test_administration_counts_rows(qapp, stock):
    from app.modules.extras import AdministrationForm
    form = AdministrationForm()
    assert form.grid.rowCount() == len(AdministrationForm.WATCH)
