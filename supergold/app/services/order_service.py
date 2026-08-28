"""
Order calculations — port of GMINE ``w_order`` math (``gminet3/w_order.srw``).

Order line value is the same jewellery formula as a sale:

    amount = (weight - stone_wgt + wastage) * rate + making + stone_price

which is algebraically identical to the sales line (net*rate + wastage*rate +
making + stone), so :class:`app.services.sales_service.SalesLine` is reused for
the lines. An order then tracks advance and exchange against the bill total:

    balance = grand_total - exchange_amount - advance
"""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal

from app.services.sales_service import SalesLine, compute_bill, BillTotals, D, rnd

OrderLine = SalesLine  # identical line math


@dataclass
class OrderTotals:
    bill: BillTotals
    advance: Decimal
    exchange: Decimal
    balance: Decimal


def compute_order(lines, tax_perc=0, interstate: bool = False,
                  tax_inclusive: bool = False, advance=0, exchange=0) -> OrderTotals:
    bill = compute_bill(lines, tax_perc=tax_perc, interstate=interstate,
                        tax_inclusive=tax_inclusive)
    advance = rnd(advance, 2)
    exchange = rnd(exchange, 2)
    balance = rnd(bill.grand_total - exchange - advance, 2)
    return OrderTotals(bill=bill, advance=advance, exchange=exchange, balance=balance)
