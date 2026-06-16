"""Unit tests for the ported sales billing math (run: python -m pytest -q)."""

from decimal import Decimal

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.services.sales_service import SalesLine, compute_bill  # noqa: E402


def test_line_amount():
    # 10g gross, 0.5g stone, 8% wastage(g)=0.8, making 150, rate 6000, stone 1200
    ln = SalesLine(weight="10", stone_wgt="0.5", wastage="0.8", making="150",
                   rate="6000", stone_price="1200").compute()
    assert ln.net_wgt == Decimal("9.500")
    # value add = 0.8*6000 + 150 = 4950
    assert ln.value_add == Decimal("4950.00")
    # amount = 9.5*6000 + 4950 + 1200 = 57000 + 6150 = 63150
    assert ln.amount == Decimal("63150.00")


def test_bill_intrastate_split():
    lines = [SalesLine(weight="10", rate="6000").compute()]  # amount 60000
    t = compute_bill(lines, tax_perc=3, interstate=False)
    assert t.gross == Decimal("60000.00")
    assert t.tax_amount == Decimal("1800.00")
    assert t.cgst == Decimal("900.00")
    assert t.sgst == Decimal("900.00")
    assert t.igst == Decimal("0")
    assert t.grand_total == Decimal("61800")


def test_bill_interstate_igst():
    lines = [SalesLine(weight="10", rate="6000").compute()]
    t = compute_bill(lines, tax_perc=3, interstate=True)
    assert t.igst == Decimal("1800.00")
    assert t.cgst == Decimal("0")
    assert t.grand_total == Decimal("61800")


def test_tax_inclusive_reverse():
    # gross 61800 inclusive of 3% -> taxable ~60000
    lines = [SalesLine(weight="10", rate="6180").compute()]  # amount 61800
    t = compute_bill(lines, tax_perc=3, interstate=False, tax_inclusive=True)
    assert t.taxable == Decimal("60000.00")
    assert t.tax_amount == Decimal("1800.00")
    assert t.grand_total == Decimal("61800")


def test_round_off():
    lines = [SalesLine(weight="1", rate="333.33").compute()]  # 333.33
    t = compute_bill(lines, tax_perc=3, interstate=False)
    # taxable 333.33, tax 10.00 -> 343.33 -> rounds to 343, round_off -0.33
    assert t.grand_total == Decimal("343")
    assert t.round_off == Decimal("-0.33")
