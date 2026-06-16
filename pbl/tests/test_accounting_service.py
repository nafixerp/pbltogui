"""Unit tests for double-entry voucher posting."""

from decimal import Decimal
import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.services import accounting_service as acc  # noqa: E402


def test_balanced_rows():
    rows = acc.make_rows(1, "2026-06-15", "CASH", "SUNDRD", "1000", acc.RECEIPT)
    assert len(rows) == 2
    assert acc.is_balanced(rows)
    assert acc.debit_balance(rows, "CASH") == Decimal("1000.00")
    assert acc.debit_balance(rows, "SUNDRD") == Decimal("-1000.00")
    assert all(r.control == acc.RECEIPT for r in rows)


def test_contra_accounts_set():
    rows = acc.make_rows(2, "2026-06-15", "SUNDRC", "CASH", "500", acc.PAYMENT)
    dr = next(r for r in rows if r.accode == "SUNDRC")
    assert dr.opaccode == "CASH" and dr.amount == Decimal("500.00")


def test_rejects_same_account():
    with pytest.raises(ValueError):
        acc.make_rows(3, "2026-06-15", "CASH", "CASH", "100", acc.JOURNAL)


def test_rejects_non_positive():
    with pytest.raises(ValueError):
        acc.make_rows(4, "2026-06-15", "CASH", "BANK", "0", acc.JOURNAL)
