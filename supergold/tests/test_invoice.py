"""Unit tests for invoice amount-in-words (Indian numbering)."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.reports.invoice import amount_in_words  # noqa: E402


def test_simple():
    assert amount_in_words("0") == "Rupees Zero Only"
    assert amount_in_words("100") == "Rupees One Hundred Only"
    assert amount_in_words("61800") == "Rupees Sixty One Thousand Eight Hundred Only"


def test_lakhs_and_paise():
    assert amount_in_words("123456.50") == (
        "Rupees One Lakh Twenty Three Thousand Four Hundred Fifty Six "
        "and Fifty Paise Only")


def test_crore():
    assert amount_in_words("10000000") == "Rupees One Crore Only"
