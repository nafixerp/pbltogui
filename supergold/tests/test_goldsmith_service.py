"""Unit tests for goldsmith fine-weight calculations."""

from decimal import Decimal
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.services.goldsmith_service import (  # noqa: E402
    SmithLine, compute_totals, fine_balance)


def test_fine_weight():
    # net = 10 - 0.5 = 9.5; touch 91.6% -> fine 8.702
    ln = SmithLine(weight="10", stone_wgt="0.5", touch="91.6").compute()
    assert ln.net_wgt == Decimal("9.500")
    assert ln.touch_wgt == Decimal("8.702")


def test_totals():
    lines = [SmithLine(weight="10", stone_wgt="0", touch="100").compute(),
             SmithLine(weight="20", stone_wgt="0", touch="75").compute()]
    t = compute_totals(lines)
    assert t.gross_wgt == Decimal("30.000")
    assert t.fine_wgt == Decimal("25.000")  # 10 + 15


def test_fine_balance():
    assert fine_balance("100.000", "40.000") == Decimal("60.000")
