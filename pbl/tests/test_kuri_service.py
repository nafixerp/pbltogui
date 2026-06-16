"""Unit tests for kuri/scheme collection math."""

from decimal import Decimal
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.services.kuri_service import installment_weight, summarise  # noqa: E402


def test_weight_for_gold_scheme():
    # 6000 paid at 6000/g -> 1.000 g
    assert installment_weight("6000", "6000", True) == Decimal("1.000")
    # 5000 at 6000 -> 0.833 g
    assert installment_weight("5000", "6000", True) == Decimal("0.833")


def test_no_weight_when_not_gold_or_no_rate():
    assert installment_weight("5000", "0", True) == Decimal("0.000")
    assert installment_weight("5000", "6000", False) == Decimal("0.000")


def test_summary():
    rows = [{"amount": 6000, "wgt": 1.0}, {"amount": 6000, "wgt": 1.0},
            {"amount": 3000, "wgt": 0.5}]
    s = summarise(rows)
    assert s.installments == 3
    assert s.total_amount == Decimal("15000.00")
    assert s.total_weight == Decimal("2.500")
