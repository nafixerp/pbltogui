"""
Stock movement logic — port of the GMINE ``items`` / ``itemsstk`` stock update
in ``w_sales`` / ``w_purchase``.

The originals keep a running stock balance per item and adjust it on every
transaction: purchases (and returns/exchanges) increase weight and quantity,
sales decrease them:

    update items set qty = qty +/- :iqty, weight = weight +/- :dweight, ...

This module models a single movement and the closing-balance arithmetic used by
the Stock Register (closing = opening + inward − outward).
"""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal

from app.services.sales_service import D, rnd

INWARD = "IN"     # purchase / return / exchange-in
OUTWARD = "OUT"   # sale


@dataclass
class StockMovement:
    code: str
    name: str
    qty: Decimal
    weight: Decimal
    stone_wgt: Decimal
    direction: str
    ttype: str        # source document type, e.g. "S" / "P"
    docno: str

    def sign(self) -> int:
        return 1 if self.direction == INWARD else -1


def closing(opening, inward, outward):
    """Closing balance = opening + inward − outward (3-dp weights)."""
    return rnd(D(opening) + D(inward) - D(outward), 3)
