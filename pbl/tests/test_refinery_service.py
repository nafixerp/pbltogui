"""Refinery issue and return move stock the way the original did."""

import os
import sys

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

import db  # noqa: E402
from app.services import cancel_service as cx  # noqa: E402
from app.services import refinery_service as rs  # noqa: E402


@pytest.fixture()
def refinery(tmp_path, monkeypatch):
    monkeypatch.setattr(db, "ENGINE", "sqlite")
    monkeypatch.setattr(db, "SQLITE_PATH", str(tmp_path / "refn.db"))
    db.execute("""CREATE TABLE items (code TEXT, qty INT, weight REAL,
                  stonewgt REAL, qtyb INT, weightb REAL, stonewgtb REAL, cost REAL)""")
    db.execute("""CREATE TABLE itemsstk (code TEXT, stktype TEXT, qty INT,
                  weight REAL, stonewgt REAL, qtyb INT, weightb REAL, stonewgtb REAL)""")
    db.execute("""CREATE TABLE refinerym (slno REAL, docno TEXT, tdate DATE,
                  refcode TEXT, control TEXT, status INT, islno REAL,
                  issuedwgt REAL, rcvdwgt REAL, note TEXT)""")
    db.execute("""CREATE TABLE refineryd (slno TEXT, sno TEXT, code TEXT,
                  issuedqty INT, issuedwgt REAL, issuedstwgt REAL, rcvdqty INT,
                  rcvdwgt REAL, bottlestk REAL, testpcs REAL, stktype TEXT,
                  status TEXT)""")
    db.execute("""CREATE TABLE delpart (tdate DATE, part TEXT, control INT,
                  slno INT, utype TEXT, ttype TEXT, updtdate DATE,
                  updttime TEXT, uid TEXT, ic TEXT)""")
    db.execute("CREATE TABLE daybook (slno INT)")
    db.execute("CREATE TABLE daybookpart (slno INT)")
    db.execute("CREATE TABLE stkandprofit (slno INT)")
    db.execute("CREATE TABLE oglist (slno INT)")
    for code in ("OLDG", "BS", "TP"):
        db.execute("INSERT INTO items VALUES (?,0,100.0,0,0,100.0,0,0)", (code,))
    return tmp_path


def weight(code="OLDG"):
    return db.fetch_one("SELECT weight FROM items WHERE code = ?", (code,))["weight"]


def test_issue_takes_the_metal_out_of_stock(refinery):
    slno = rs.issue("REF1", [{"code": "OLDG", "qty": 1, "weight": 30.0}])
    assert weight() == pytest.approx(70.0)
    head = db.fetch_one("SELECT * FROM refinerym WHERE slno = ?", (slno,))
    assert head["refcode"] == "REF1" and head["issuedwgt"] == pytest.approx(30.0)
    assert len(db.fetch_all("SELECT * FROM refineryd")) == 1


def test_issue_needs_a_refiner_and_a_line(refinery):
    with pytest.raises(ValueError):
        rs.issue("", [{"code": "OLDG", "weight": 1}])
    with pytest.raises(ValueError):
        rs.issue("REF1", [])


def test_return_brings_the_metal_back(refinery):
    issue = rs.issue("REF1", [{"code": "OLDG", "weight": 30.0}])
    rs.receive(issue, [{"code": "OLDG", "weight": 28.5,
                        "bottlestk": 0.5, "testpcs": 0.2}])
    assert weight() == pytest.approx(98.5)          # 100 - 30 + 28.5
    assert weight("BS") == pytest.approx(100.5)
    assert weight("TP") == pytest.approx(100.2)


def test_return_closes_the_issue(refinery):
    issue = rs.issue("REF1", [{"code": "OLDG", "weight": 10.0}])
    assert [r["slno"] for r in rs.pending_issues()] == [issue]
    rs.receive(issue, [{"code": "OLDG", "weight": 9.8}])
    assert rs.pending_issues() == []


def test_return_needs_an_existing_issue(refinery):
    with pytest.raises(ValueError):
        rs.receive(999, [{"code": "OLDG", "weight": 1}])


def test_cancelling_an_issue_puts_the_metal_back(refinery):
    issue = rs.issue("REF1", [{"code": "OLDG", "qty": 1, "weight": 30.0}])
    cx.cancel_document("w_refncancel", issue)
    assert weight() == pytest.approx(100.0)
    assert db.fetch_all("SELECT * FROM refinerym WHERE slno = ?", (issue,)) == []


def test_screens_use_the_service(refinery):
    pytest.importorskip("PySide6.QtWidgets")
    from PySide6.QtWidgets import QApplication, QTableWidgetItem
    app = QApplication.instance() or QApplication([])
    from app.modules.refinery import RefineryIssueForm
    form = RefineryIssueForm()
    form.refiner.setText("REF9")
    form.grid.setItem(0, 0, QTableWidgetItem("OLDG"))
    form.grid.setItem(0, 2, QTableWidgetItem("12"))
    form.save()
    assert "Issued" in form.status.text()
    assert weight() == pytest.approx(88.0)
