"""Unit tests for the multi-leg GL voucher builder."""

from decimal import Decimal
import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.services import accounting_service as acc  # noqa: E402


def test_multi_rows_balance():
    legs = [("SUNDRD", Decimal("61800")), ("SALES", Decimal("-60000")),
            ("GSTOUT", Decimal("-1800")), ("ROUNDOFF", Decimal("0"))]
    rows = acc.make_multi_rows(1, "2026-06-15", legs, "S", "S:S000001")
    assert acc.is_balanced(rows)
    # zero leg dropped
    assert len(rows) == 3
    assert all(r.refno == "S:S000001" for r in rows)
    # debit leg's contra is the largest credit (SALES)
    dr = next(r for r in rows if r.accode == "SUNDRD")
    assert dr.opaccode == "SALES"


def test_multi_rows_unbalanced_rejected():
    legs = [("A", Decimal("100")), ("B", Decimal("-90"))]
    with pytest.raises(ValueError):
        acc.make_multi_rows(1, "2026-06-15", legs, "J", "")


def test_roundoff_leg_included():
    legs = [("SUNDRD", Decimal("343")), ("SALES", Decimal("-333.33")),
            ("GSTOUT", Decimal("-10")), ("ROUNDOFF", Decimal("0.33"))]
    rows = acc.make_multi_rows(1, "2026-06-15", legs, "S", "r")
    assert acc.is_balanced(rows)
    assert any(r.accode == "ROUNDOFF" for r in rows)
