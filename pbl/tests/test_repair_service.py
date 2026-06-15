"""Unit tests for repair/remake memo calculations."""

from decimal import Decimal
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.services.repair_service import RepairLine, compute_totals  # noqa: E402


def test_net_weight():
    ln = RepairLine(weight="12.345", stone_wgt="2.345").compute()
    assert ln.net_wgt == Decimal("10.000")


def test_totals():
    lines = [
        RepairLine(qty="1", weight="10", stone_wgt="1", cost="500").compute(),
        RepairLine(qty="2", weight="5.5", stone_wgt="0.5", cost="250").compute(),
    ]
    t = compute_totals(lines)
    assert t.qty == Decimal("3")
    assert t.gross_wgt == Decimal("15.500")
    assert t.net_wgt == Decimal("14.000")  # 9 + 5
    assert t.cost == Decimal("750.00")
