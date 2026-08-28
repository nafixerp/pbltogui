"""
Kuri / Scheme collection logic — port of GMINE ``w_kuricolln`` (``gminet7``).

A member pays a periodic installment. For a gold scheme the paid amount is
converted to a gold weight at the day's rate, exactly as the PowerBuilder source:

    weight = amount / gold rate          (0 if not a gold scheme / no rate)

A member's standing is the running total of installments, amount and (for gold
schemes) accumulated weight.
"""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal

from app.services.sales_service import D, rnd


def installment_weight(amount, gold_rate, gold_scheme: bool = True) -> Decimal:
    """Gold weight credited for a paid amount."""
    rate = D(gold_rate)
    if not gold_scheme or rate <= 0:
        return Decimal("0.000")
    return rnd(D(amount) / rate, 3)


@dataclass
class MemberSummary:
    installments: int
    total_amount: Decimal
    total_weight: Decimal


def summarise(rows) -> MemberSummary:
    amt = rnd(sum((D(r.get("amount")) for r in rows), Decimal("0")), 2)
    wgt = rnd(sum((D(r.get("wgt")) for r in rows), Decimal("0")), 3)
    return MemberSummary(installments=len(rows), total_amount=amt, total_weight=wgt)
