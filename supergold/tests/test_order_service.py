"""Unit tests for order calculations."""

from decimal import Decimal
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.services.order_service import OrderLine, compute_order  # noqa: E402


def test_order_line_matches_sales_formula():
    # (weight - stone + wastage) * rate + making + stone_price
    ln = OrderLine(weight="10", stone_wgt="0.5", wastage="0.8", making="150",
                   rate="6000", stone_price="1200").compute()
    # (10 - 0.5 + 0.8)*6000 + 150 + 1200 = 10.3*6000 + 1350 = 61800 + 1350 = 63150
    assert ln.amount == Decimal("63150.00")


def test_order_balance():
    lines = [OrderLine(weight="10", rate="6000").compute()]  # 60000
    t = compute_order(lines, tax_perc=3, interstate=False, advance="10000",
                      exchange="5000")
    # grand 61800 - 5000 - 10000 = 46800
    assert t.bill.grand_total == Decimal("61800")
    assert t.advance == Decimal("10000.00")
    assert t.exchange == Decimal("5000.00")
    assert t.balance == Decimal("46800.00")


def test_order_balance_no_tax():
    lines = [OrderLine(weight="2", rate="5000").compute()]  # 10000
    t = compute_order(lines, tax_perc=0, advance="3000")
    assert t.balance == Decimal("7000.00")
