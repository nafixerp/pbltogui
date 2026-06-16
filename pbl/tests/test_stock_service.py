"""Unit tests for stock closing-balance math."""

from decimal import Decimal
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.services.stock_service import closing, StockMovement, INWARD, OUTWARD  # noqa: E402


def test_closing_balance():
    assert closing("10", "20", "6") == Decimal("24.000")


def test_movement_sign():
    inw = StockMovement("X", "Item", 1, 10, 0, INWARD, "P", "P1")
    outw = StockMovement("X", "Item", 1, 4, 0, OUTWARD, "S", "S1")
    assert inw.sign() == 1
    assert outw.sign() == -1
