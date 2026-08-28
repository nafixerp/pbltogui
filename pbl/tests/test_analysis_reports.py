"""The code-built reports: party/barcode history, integrity, day summary."""

import os
import sys

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

import db  # noqa: E402
from app.reports import analysis as an  # noqa: E402


@pytest.fixture()
def erp(tmp_path, monkeypatch):
    monkeypatch.setattr(db, "ENGINE", "sqlite")
    monkeypatch.setattr(db, "SQLITE_PATH", str(tmp_path / "an.db"))
    for ddl in (
        """CREATE TABLE salesm (slno INT, billno TEXT, tdate DATE, custcode TEXT,
             netamt REAL)""",
        "CREATE TABLE salesd (slno INT, bcode INT, qty INT, weight REAL, stonewgt REAL)",
        "CREATE TABLE salesrm (slno INT, billno TEXT, tdate DATE, custcode TEXT, netamt REAL)",
        "CREATE TABLE salesrd (slno INT, bcode INT, qty INT, weight REAL, stonewgt REAL)",
        "CREATE TABLE purchasem (slno INT, docno TEXT, tdate DATE, suppcode TEXT, netamt REAL)",
        "CREATE TABLE purchased (slno INT, bcode INT, qty INT, weight REAL, stonewgt REAL)",
        "CREATE TABLE purchaserm (slno INT, docno TEXT, tdate DATE, suppcode TEXT, netamt REAL)",
        "CREATE TABLE purchaserd (slno INT, weight REAL)",
        "CREATE TABLE smithm (slno INT, docno TEXT, tdate DATE, smithcode TEXT, netamt REAL)",
        "CREATE TABLE smithd (slno INT, bcode INT, qty INT, weight REAL, stonewgt REAL)",
        "CREATE TABLE orderm (slno INT, ordno TEXT, tdate DATE, custcode TEXT, netamt REAL)",
        "CREATE TABLE orderd (slno INT, weight REAL)",
        "CREATE TABLE itemadj (slno INT, bcode INT, tdate DATE, fromqty INT, fromwgt REAL, fromstwgt REAL)",
        "CREATE TABLE daybook (slno INT, accode TEXT, tdate DATE, amount REAL, sno TEXT)",
        "CREATE TABLE accountm (accode TEXT, name TEXT, grcode TEXT, opbal REAL)",
        "CREATE TABLE items (code TEXT, name TEXT, weight REAL, weightb REAL, qty INT, qtyb INT)",
        "CREATE TABLE loan (slno INT, loanno TEXT, docno TEXT, tdate DATE, amount REAL)",
        "CREATE TABLE loancolln (loanno TEXT, tdate DATE, docno TEXT, ramt REAL, intamt REAL)",
    ):
        db.execute(ddl)
    db.execute("INSERT INTO salesm VALUES (1,'B1','2026-06-01','C1',5000)")
    db.execute("INSERT INTO salesd VALUES (1, 77, 1, 10.5, 0.5)")
    db.execute("INSERT INTO purchasem VALUES (2,'P1','2026-06-02','C1',3000)")
    db.execute("INSERT INTO purchased VALUES (2, 77, 1, 4.0, 0)")
    db.execute("INSERT INTO daybook VALUES (3,'C1','2026-06-03',-2000,'R1')")
    db.execute("INSERT INTO accountm VALUES ('C1','Ravi','DEBTORS',1000)")
    return tmp_path


def test_party_history_gathers_every_document(erp):
    columns, rows = an.party_history("C1", "2026-06-01", "2026-06-30")
    assert columns[:3] == ["tdate", "type", "docno"]
    kinds = [r["type"] for r in rows]
    assert kinds == ["Sales", "Purchase", "Receipt"]
    assert rows[0]["amount"] == "5000.00" and rows[2]["amount"] == "2000.00"


def test_party_history_respects_the_date_range(erp):
    _c, rows = an.party_history("C1", "2026-06-02", "2026-06-02")
    assert [r["docno"] for r in rows] == ["P1"]


def test_party_history_without_an_account_is_empty(erp):
    assert an.party_history("", "2026-06-01", "2026-06-30")[1] == []


def test_barcode_history_follows_the_piece(erp):
    _c, rows = an.barcode_history(77)
    assert [r["type"] for r in rows] == ["Sales", "Purchase"]
    assert rows[0]["weight"] == "10.500"


def test_group_expanded_shows_opening_and_closing(erp):
    _c, rows = an.group_expanded("DEBTORS", "2026-06-02", "2026-06-30")
    row = next(r for r in rows if r["accode"] == "C1")
    assert row["opening"] == "1000.00"        # opbal, nothing posted before
    assert row["movement"] == "-2000.00"
    assert row["closing"] == "-1000.00"


def test_non_transactional_days_lists_only_idle_dates(erp):
    _c, rows = an.non_transactional_days("2026-06-01", "2026-06-05")
    assert [r["tdate"] for r in rows] == ["2026-06-01", "2026-06-02",
                                          "2026-06-04", "2026-06-05"]
    assert rows[0]["day"] == "Monday"


def test_integrity_check_finds_an_unbalanced_voucher(erp):
    _c, rows = an.integrity_check("2026-06-30")
    problems = {r["check"] for r in rows}
    assert "Voucher does not balance" in problems      # the -2000 single leg


def test_integrity_check_reports_a_missing_account(erp):
    db.execute("INSERT INTO daybook VALUES (4,'GHOST','2026-06-04',100,'X')")
    db.execute("INSERT INTO daybook VALUES (4,'C1','2026-06-04',-100,'X')")
    _c, rows = an.integrity_check("2026-06-30")
    assert any(r["reference"] == "GHOST" for r in rows)


def test_integrity_check_is_clean_on_a_clean_book(tmp_path, monkeypatch):
    monkeypatch.setattr(db, "ENGINE", "sqlite")
    monkeypatch.setattr(db, "SQLITE_PATH", str(tmp_path / "clean.db"))
    db.execute("CREATE TABLE daybook (slno INT, accode TEXT, tdate DATE, amount REAL)")
    db.execute("CREATE TABLE accountm (accode TEXT, name TEXT, grcode TEXT, opbal REAL)")
    db.execute("CREATE TABLE items (code TEXT, name TEXT, weight REAL, weightb REAL, qty INT, qtyb INT)")
    db.execute("INSERT INTO accountm VALUES ('CASH','Cash','',0)")
    db.execute("INSERT INTO daybook VALUES (1,'CASH','2026-06-01',100)")
    db.execute("INSERT INTO daybook VALUES (1,'CASH','2026-06-01',-100)")
    _c, rows = an.integrity_check("2026-06-30")
    assert rows == [{"check": "No problems found", "reference": "", "detail": ""}]


def test_loan_ledger_lists_the_loan_and_its_collections(erp):
    db.execute("INSERT INTO loan VALUES (5,'L1','LD1','2026-06-01',10000)")
    db.execute("INSERT INTO loancolln VALUES ('L1','2026-06-10','LC1',2000,150)")
    _c, rows = an.loan_ledger("L1")
    assert [r["particulars"] for r in rows] == ["Loan", "Collection"]
    assert rows[1]["interest"] == "150.00"


def test_day_summary_totals_the_day(erp):
    columns, rows = an.day_summary("2026-06-01", "2026-06-30")
    assert columns == ["particulars", "count", "weight", "amount"]
    by_name = {r["particulars"]: r for r in rows}
    assert by_name["Sales"]["count"] == 1
    assert by_name["Sales"]["weight"] == "10.500"
    assert by_name["Purchase"]["amount"] == "3000.00"
    assert by_name["Cash/Bank paid"]["amount"] == "2000.00"


def test_all_windows_are_registered():
    from app import modules
    for window in an.SPECS:
        assert modules.get_factory(window) is not None


def test_stock_asset_liability_expense(erp):
    db.execute("UPDATE items SET weight = 0 WHERE 1=1")
    db.execute("INSERT INTO items VALUES ('G22','Gold',50.0,50.0,1,1)")
    db.execute("ALTER TABLE items ADD COLUMN cost REAL")
    db.execute("UPDATE items SET cost = 100 WHERE code = 'G22'")
    db.execute("ALTER TABLE accountm ADD COLUMN actype1 TEXT")
    db.execute("UPDATE accountm SET actype1 = 'A' WHERE accode = 'C1'")
    columns, rows = an.stock_asset_liability_expense("2026-06-30")
    assert columns == ["particulars", "amount"]
    values = {r["particulars"]: r["amount"] for r in rows}
    assert values["Stock value"] == "5000.00"
    # C1: opening 1000, posted -2000 -> credit balance, so a liability side entry
    assert values["Assets"] == "0.00"
