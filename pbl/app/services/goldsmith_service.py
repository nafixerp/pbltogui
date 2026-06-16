"""
Goldsmith / Jewellery weight transaction — port of GMINE ``w_gsmith``
(``gminet4``).

Gold is issued to (Given) and received from (Received) a goldsmith for making.
Each line carries a metal weight, a stone weight and a *touch* (purity %); the
business value is the **fine (pure) weight**, exactly as the PowerBuilder source
computes it:

    net weight   = weight - stone weight
    touch weight = net weight * touch / 100      (fine / pure gold)

A goldsmith's outstanding balance is the fine weight given minus the fine weight
received. The same screen serves Goldsmith, Jewellery and Party-Weight-Deposit
in the original menu.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from app.services.sales_service import D, rnd

GIVEN = "G"
RECEIVED = "R"
DIR_LABELS = {GIVEN: "Given to smith", RECEIVED: "Received from smith"}


@dataclass
class SmithLine:
    code: str = ""
    name: str = ""
    qty: Decimal = field(default_factory=lambda: Decimal("1"))
    weight: Decimal = field(default_factory=lambda: Decimal("0"))
    stone_wgt: Decimal = field(default_factory=lambda: Decimal("0"))
    touch: Decimal = field(default_factory=lambda: Decimal("0"))
    making: Decimal = field(default_factory=lambda: Decimal("0"))

    net_wgt: Decimal = field(default_factory=lambda: Decimal("0"))
    touch_wgt: Decimal = field(default_factory=lambda: Decimal("0"))

    def compute(self) -> "SmithLine":
        self.net_wgt = rnd(rnd(self.weight, 3) - rnd(self.stone_wgt, 3), 3)
        self.touch_wgt = rnd(self.net_wgt * D(self.touch) / Decimal(100), 3)
        return self


@dataclass
class SmithTotals:
    qty: Decimal
    gross_wgt: Decimal
    net_wgt: Decimal
    fine_wgt: Decimal
    making: Decimal


def compute_totals(lines) -> SmithTotals:
    qty = sum((D(ln.qty) for ln in lines), Decimal("0"))
    gross = rnd(sum((D(ln.weight) for ln in lines), Decimal("0")), 3)
    net = rnd(sum((ln.compute().net_wgt for ln in lines), Decimal("0")), 3)
    fine = rnd(sum((ln.touch_wgt for ln in lines), Decimal("0")), 3)
    making = rnd(sum((D(ln.making) for ln in lines), Decimal("0")), 2)
    return SmithTotals(qty=qty, gross_wgt=gross, net_wgt=net, fine_wgt=fine,
                       making=making)


def fine_balance(given_fine, received_fine) -> Decimal:
    """Outstanding fine weight with a smith = given − received."""
    return rnd(D(given_fine) - D(received_fine), 3)
