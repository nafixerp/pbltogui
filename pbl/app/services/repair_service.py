"""
Repair / Remake memo logic — port of GMINE ``w_reprenter`` / ``w_reprno``
(``gminet5``).

These are service memos (job cards), not billed documents: items are received
from / issued to a party for remake with a complaint note and an estimated cost.
The only line computation is net weight:

    net weight = round(weight - stone weight, 3)

Memo totals are the running quantity, gross weight, net weight and estimated
cost.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from app.services.sales_service import D, rnd

# Memo direction (GMINE ``givrec`` flag).
RECEIPT = "R"   # received from party for remake (w_reprenter)
ISSUE = "G"     # issued back to party (w_reprno)

MEMO_LABELS = {RECEIPT: "Receipt Memo (from party)", ISSUE: "Issue Memo (to party)"}


@dataclass
class RepairLine:
    code: str = ""
    name: str = ""
    qty: Decimal = field(default_factory=lambda: Decimal("1"))
    weight: Decimal = field(default_factory=lambda: Decimal("0"))
    stone_wgt: Decimal = field(default_factory=lambda: Decimal("0"))
    complaint: str = ""
    purity: str = ""
    stktype: str = ""
    cost: Decimal = field(default_factory=lambda: Decimal("0"))

    net_wgt: Decimal = field(default_factory=lambda: Decimal("0"))

    def compute(self) -> "RepairLine":
        self.net_wgt = rnd(rnd(self.weight, 3) - rnd(self.stone_wgt, 3), 3)
        return self


@dataclass
class MemoTotals:
    qty: Decimal
    gross_wgt: Decimal
    net_wgt: Decimal
    cost: Decimal


def compute_totals(lines) -> MemoTotals:
    qty = sum((D(ln.qty) for ln in lines), Decimal("0"))
    gross = rnd(sum((D(ln.weight) for ln in lines), Decimal("0")), 3)
    net = rnd(sum((ln.compute().net_wgt for ln in lines), Decimal("0")), 3)
    cost = rnd(sum((D(ln.cost) for ln in lines), Decimal("0")), 2)
    return MemoTotals(qty=qty, gross_wgt=gross, net_wgt=net, cost=cost)
