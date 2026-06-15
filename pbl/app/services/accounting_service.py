"""
Accounting voucher logic — port of the GMINE Receipt / Payment / Journal
posting (``gminet7/w_rcpt.srw``, ``w_pmnt.srw``, ``w_journal.srw``).

All three write balanced rows to ``daybook(slno, tdate, accode, amount, control,
opaccode)``. GMINE records each leg of a voucher as a row carrying its account
(`accode`), the contra account (`opaccode`) and a signed `amount`, tagged with a
`control` code for the voucher type. A voucher therefore produces two mirrored
rows that net to zero:

    Dr leg:  accode = debit,  amount = +amt, opaccode = credit
    Cr leg:  accode = credit, amount = -amt, opaccode = debit

A debit balance for an account is ``sum(amount)`` over its rows.
"""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal

from app.services.sales_service import D, rnd

# Voucher type -> daybook control code (as used by GMINE).
RECEIPT = "R"
PAYMENT = "P"
JOURNAL = "J"

VOUCHER_LABELS = {RECEIPT: "Receipt", PAYMENT: "Payment", JOURNAL: "Journal"}


@dataclass
class DaybookRow:
    slno: int
    tdate: str
    accode: str
    amount: Decimal
    control: str
    opaccode: str


def make_rows(slno: int, tdate: str, debit: str, credit: str, amount,
              control: str = JOURNAL) -> list[DaybookRow]:
    """Build the two balanced daybook rows for a voucher."""
    amt = rnd(amount, 2)
    if amt <= 0:
        raise ValueError("Voucher amount must be positive.")
    if not debit or not credit:
        raise ValueError("Both debit and credit accounts are required.")
    if debit == credit:
        raise ValueError("Debit and credit accounts must differ.")
    return [
        DaybookRow(slno, tdate, debit, amt, control, credit),
        DaybookRow(slno, tdate, credit, -amt, control, debit),
    ]


def is_balanced(rows: list[DaybookRow]) -> bool:
    return sum((r.amount for r in rows), Decimal("0")) == Decimal("0")


def debit_balance(rows: list[DaybookRow], accode: str) -> Decimal:
    return sum((r.amount for r in rows if r.accode == accode), Decimal("0"))
