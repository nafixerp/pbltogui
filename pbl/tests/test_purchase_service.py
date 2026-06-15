"""Unit tests for the ported purchase billing math."""

from decimal import Decimal
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.services.purchase_service import PurchaseLine, compute_totals  # noqa: E402


def test_less_and_net_weight():
    # 100g gross, 2g stone, 1g mud, 2% less on (100-2-1)=97 -> 1.94g
    ln = PurchaseLine(weight="100", stone_wgt="2", mud="1", less_perc="2",
                      rate="5000").compute()
    assert ln.less_wgt == Decimal("1.940")
    # net = 100 - 1.94 - 2 = 96.06
    assert ln.net_wgt == Decimal("96.060")
    # amount = 96.06 * 5000 = 480300
    assert ln.amount == Decimal("480300.00")


def test_amount_with_stone_and_making():
    ln = PurchaseLine(weight="10", stone_wgt="0", mud="0", less_perc="0",
                      rate="6000", stone_price="500", making="200").compute()
    # net 10 -> 60000 + 500 + 200 = 60700
    assert ln.amount == Decimal("60700.00")


def test_qty_priced_item():
    ln = PurchaseLine(qty="5", rate="100", is_qty=True).compute()
    assert ln.amount == Decimal("500.00")


def test_totals_intrastate():
    lines = [PurchaseLine(weight="10", rate="6000").compute()]  # 60000
    t = compute_totals(lines, tax_perc=3, interstate=False)
    assert t.cgst == Decimal("900.00")
    assert t.sgst == Decimal("900.00")
    assert t.grand_total == Decimal("61800")
