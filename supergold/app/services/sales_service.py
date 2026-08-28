"""
Sales billing calculations — faithful port of the GMINE ``w_sales`` math.

The arithmetic mirrors the PowerBuilder source (``gminet1/w_sales.srw``):

  net weight   = round(weight - stone weight, 3)
  value add    = round(wastage_grams * rate + making_charge, 2)
  line amount  = round(net_weight * rate + value_add + stone_price, 2)

Bill tax (GST) follows the same branch logic:

  * tax-inclusive prices are grossed-down by ``100 / (100 + tax% + addl%)``
  * inter-state  -> full IGST
  * intra-state  -> CGST = SGST = tax / 2

All money/weight math uses :class:`~decimal.Decimal` with round-half-up to match
the PowerBuilder ``round()`` behaviour and avoid float drift.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal, ROUND_HALF_UP


def D(value) -> Decimal:
    if isinstance(value, Decimal):
        return value
    if value in (None, ""):
        return Decimal("0")
    return Decimal(str(value))


def rnd(value, places: int) -> Decimal:
    q = Decimal(1).scaleb(-places)  # 10**-places
    return D(value).quantize(q, rounding=ROUND_HALF_UP)


@dataclass
class SalesLine:
    code: str = ""
    name: str = ""
    qty: Decimal = field(default_factory=lambda: Decimal("1"))
    weight: Decimal = field(default_factory=lambda: Decimal("0"))
    stone_wgt: Decimal = field(default_factory=lambda: Decimal("0"))
    stone_price: Decimal = field(default_factory=lambda: Decimal("0"))
    wastage: Decimal = field(default_factory=lambda: Decimal("0"))  # grams
    making: Decimal = field(default_factory=lambda: Decimal("0"))
    rate: Decimal = field(default_factory=lambda: Decimal("0"))

    # computed
    net_wgt: Decimal = field(default_factory=lambda: Decimal("0"))
    value_add: Decimal = field(default_factory=lambda: Decimal("0"))
    amount: Decimal = field(default_factory=lambda: Decimal("0"))

    def compute(self) -> "SalesLine":
        weight = rnd(self.weight, 3)
        stone_wgt = rnd(self.stone_wgt, 3)
        rate = rnd(self.rate, 2)
        self.net_wgt = rnd(weight - stone_wgt, 3)
        self.value_add = rnd(rnd(self.wastage, 3) * rate + rnd(self.making, 2), 2)
        self.amount = rnd(self.net_wgt * rate + self.value_add + rnd(self.stone_price, 2), 2)
        return self


@dataclass
class BillTotals:
    gross: Decimal
    taxable: Decimal
    tax_amount: Decimal
    cgst: Decimal
    sgst: Decimal
    igst: Decimal
    round_off: Decimal
    grand_total: Decimal


def compute_bill(lines: list[SalesLine], tax_perc=0, interstate: bool = False,
                 tax_inclusive: bool = False, addl_perc=0) -> BillTotals:
    """Aggregate computed lines into bill totals with the GST split."""
    tax_perc = D(tax_perc)
    addl_perc = D(addl_perc)
    gross = sum((ln.compute().amount for ln in lines), Decimal("0"))
    gross = rnd(gross, 2)

    if tax_inclusive and (tax_perc + addl_perc) > 0:
        taxable = rnd(gross * Decimal(100) / (Decimal(100) + tax_perc + addl_perc), 2)
    else:
        taxable = gross

    tax_amount = rnd(taxable * tax_perc / Decimal(100), 2)

    if interstate:
        igst, cgst, sgst = tax_amount, Decimal("0"), Decimal("0")
    else:
        half = rnd(tax_amount / Decimal(2), 2)
        cgst = sgst = half
        igst = Decimal("0")
        # keep cgst+sgst == tax_amount even when the half is odd
        tax_amount = rnd(cgst + sgst, 2)

    pre_total = taxable + tax_amount if not tax_inclusive else gross
    grand = rnd(pre_total, 0)
    round_off = rnd(grand - pre_total, 2)

    return BillTotals(
        gross=gross, taxable=taxable, tax_amount=tax_amount,
        cgst=cgst, sgst=sgst, igst=igst,
        round_off=round_off, grand_total=grand,
    )
