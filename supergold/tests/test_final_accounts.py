"""Trading / P&L, Balance Sheet and cash balance, converted from the originals."""

import os
import sys

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

import db  # noqa: E402
from app.reports import final_accounts as fa  # noqa: E402


@pytest.fixture()
def books(tmp_path, monkeypatch):
    monkeypatch.setattr(db, "ENGINE", "sqlite")
    monkeypatch.setattr(db, "SQLITE_PATH", str(tmp_path / "books.db"))
    db.execute("""CREATE TABLE accountm (accode TEXT, name TEXT, actype1 TEXT,
                  tplpos INT, bshead TEXT, opbal REAL, opbalb REAL)""")
    db.execute("CREATE TABLE daybook (slno INT, accode TEXT, tdate DATE, amount REAL)")
    # Trading: purchases (debit) and sales (credit)
    db.execute("INSERT INTO accountm VALUES ('PURCH','Purchases','E',1,'',0,0)")
    db.execute("INSERT INTO accountm VALUES ('SALES','Sales','R',1,'',0,0)")
    # Profit & Loss: an expense
    db.execute("INSERT INTO accountm VALUES ('RENT','Rent','E',2,'',0,0)")
    # Balance sheet
    db.execute("INSERT INTO accountm VALUES ('CASH','Cash','A',0,'CA',1000,1000)")
    db.execute("INSERT INTO accountm VALUES ('CAP','Capital','L',0,'CAP',-5000,0)")
    for accode, amount, date in (("PURCH", 4000, "2026-06-01"),
                                 ("SALES", -7000, "2026-06-02"),
                                 ("RENT", 500, "2026-06-03"),
                                 ("CASH", 2500, "2026-06-02")):
        db.execute("INSERT INTO daybook VALUES (1,?,?,?)", (accode, date, amount))
    return tmp_path


# --- balances --------------------------------------------------------------

def test_account_balance_is_opening_plus_movement(books):
    assert fa.account_balance("CASH", "2026-06-30") == 3500.0
    assert fa.account_balance("CASH", "2026-06-01") == 1000.0


# --- trading and P&L -------------------------------------------------------

def test_gross_and_net_profit(books):
    columns, rows = fa.trading_and_pl("2026-06-30")
    assert columns[0] == "section"
    gross = next(r for r in rows if r["name"] == "GROSS PROFIT")
    net = next(r for r in rows if r["name"] == "NET PROFIT")
    # In the T-format Trading account the gross profit balances the debit side.
    assert gross["debit"] == "3000.00"           # 7000 sales - 4000 purchases
    assert net["debit"] == "2500.00"             # less 500 rent
    assert fa.net_profit("2026-06-30") == 2500.0


def test_accounts_are_split_into_trading_and_profit_and_loss(books):
    _cols, rows = fa.trading_and_pl("2026-06-30")
    sections = {r["name"]: r["section"] for r in rows}
    assert sections["Purchases"] == "Trading"
    assert sections["Sales"] == "Trading"
    assert sections["Rent"] == "Profit & Loss"


def test_period_limits_the_movement(books):
    _cols, rows = fa.trading_and_pl("2026-06-01", start="2026-06-01")
    names = {r["name"] for r in rows if r["accode"]}
    assert names == {"Purchases"}                # only that day's posting


def test_zero_balance_accounts_are_left_out(books):
    db.execute("INSERT INTO accountm VALUES ('MISC','Misc','E',2,'',0,0)")
    _cols, rows = fa.trading_and_pl("2026-06-30")
    assert "Misc" not in {r["name"] for r in rows}


# --- balance sheet ---------------------------------------------------------

def test_balance_sheet_sides_and_totals(books):
    _cols, rows = fa.balance_sheet("2026-06-30")
    by_name = {r["name"]: r for r in rows}
    assert by_name["Cash"]["side"] == "Assets" and by_name["Cash"]["amount"] == "3500.00"
    assert by_name["Capital"]["side"] == "Liabilities"
    assert by_name["NET PROFIT"]["side"] == "Liabilities"
    totals = [r for r in rows if r["name"] == "TOTAL"]
    assert {t["side"]: t["amount"] for t in totals} == {
        "Liabilities": "7500.00", "Assets": "3500.00"}


def test_balance_sheet_keeps_the_account_head(books):
    _cols, rows = fa.balance_sheet("2026-06-30")
    assert next(r for r in rows if r["name"] == "Cash")["head"] == "CA"


# --- cash ------------------------------------------------------------------

def test_cash_balance_shows_the_day(books):
    _cols, rows = fa.cash_balance("2026-06-02")
    assert rows[0]["amount"] == "3500.00"
    assert rows[1]["amount"] == "2500.00"        # received that day
    assert rows[2]["amount"] == "0.00"


def test_yearly_cash_balance_has_twelve_months(books):
    columns, rows = fa.yearly_cash_balance(2026)
    assert columns == ["month", "receipts", "payments", "closing"]
    assert len(rows) == 12
    june = next(r for r in rows if r["month"].startswith("Jun"))
    assert june["receipts"] == "2500.00" and june["closing"] == "3500.00"


def test_reports_are_registered_for_their_windows():
    from app import modules
    for window in fa.SPECS:
        assert modules.get_factory(window) is not None
