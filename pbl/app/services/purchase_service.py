"""
Purchase billing calculations — faithful port of GMINE ``w_purchase`` math.

From ``gminet2/w_purchase.srw``:

  less weight = round((weight - stone_wgt - mud) * less% / 100, 3)
  net weight  = round(weight - less_weight - stone_wgt, 3)
  amount      = round((qty*rate if quantity item else net_weight*rate)
                      + stone_price + making, 2)

Bill totals reuse the shared GST split in :mod:`app.services.sales_service`
(inter-state IGST vs intra-state CGST/SGST, tax-inclusive reverse calc and
round-off) since purchase and sales tax handling are identical in GMINE.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from app.services.sales_service import D, rnd, compute_bill, BillTotals  # noqa: F401


@dataclass
class PurchaseLine:
    code: str = ""
    name: str = ""
    qty: Decimal = field(default_factory=lambda: Decimal("1"))
    weight: Decimal = field(default_factory=lambda: Decimal("0"))
    stone_wgt: Decimal = field(default_factory=lambda: Decimal("0"))
    stone_price: Decimal = field(default_factory=lambda: Decimal("0"))
    mud: Decimal = field(default_factory=lambda: Decimal("0"))      # extra deduction wt
    less_perc: Decimal = field(default_factory=lambda: Decimal("0"))
    making: Decimal = field(default_factory=lambda: Decimal("0"))
    rate: Decimal = field(default_factory=lambda: Decimal("0"))
    is_qty: bool = False  # quantity-priced item (qty*rate) vs weight-priced

    # computed
    less_wgt: Decimal = field(default_factory=lambda: Decimal("0"))
    net_wgt: Decimal = field(default_factory=lambda: Decimal("0"))
    amount: Decimal = field(default_factory=lambda: Decimal("0"))

    def compute(self) -> "PurchaseLine":
        weight = rnd(self.weight, 3)
        stone_wgt = rnd(self.stone_wgt, 3)
        mud = rnd(self.mud, 3)
        rate = rnd(self.rate, 2)
        self.less_wgt = rnd((weight - stone_wgt - mud) * D(self.less_perc) / Decimal(100), 3)
        self.net_wgt = rnd(weight - self.less_wgt - stone_wgt, 3)
        base = (D(self.qty) * rate) if self.is_qty else (self.net_wgt * rate)
        self.amount = rnd(base + rnd(self.stone_price, 2) + rnd(self.making, 2), 2)
        return self


def compute_totals(lines, tax_perc=0, interstate=False, tax_inclusive=False,
                   addl_perc=0) -> BillTotals:
    """Purchase bill totals — same GST split as sales."""
    return compute_bill(lines, tax_perc=tax_perc, interstate=interstate,
                        tax_inclusive=tax_inclusive, addl_perc=addl_perc)
