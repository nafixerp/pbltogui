"""
General-ledger posting for billed documents.

Wires the converted Sales and Purchase modules into the accounting ``daybook``
so bills appear in the Day Book, Trial Balance, Account Ledger and Cash Book.
Each bill posts a balanced compound voucher:

  Sale (control ``S``):
    Dr  Debtor/Cash   grand total
    Cr  Sales         taxable
    Cr  GST Output    cgst + sgst + igst
    Cr  Round Off     round-off            (sign as needed)

  Purchase (control ``P``):
    Dr  Purchase      taxable
    Dr  GST Input     cgst + sgst + igst
    Dr  Round Off     round-off
    Cr  Creditor/Cash grand total

Posting is keyed by the bill number (``refno``) so a re-save replaces the prior
voucher rather than duplicating it. Customer/supplier control accounts default
to Sundry Debtors / Creditors (or Cash for a cash bill).
"""

from __future__ import annotations

from decimal import Decimal

from app.services.sales_service import D
from app.repositories import accounting_repository as acc


def post_sale(billno: str, tdate: str, totals, cash: bool = False,
              debtor: str = "SUNDRD") -> int:
    """Post a sale's GL voucher. ``totals`` is a sales BillTotals."""
    debit_acc = "CASH" if cash else debtor
    tax = D(totals.cgst) + D(totals.sgst) + D(totals.igst)
    legs = [
        (debit_acc, D(totals.grand_total)),
        ("SALES", -D(totals.taxable)),
        ("GSTOUT", -tax),
        ("ROUNDOFF", -D(totals.round_off)),
    ]
    return acc.post_legs(tdate, legs, control="S", refno=f"S:{billno}",
                         narration=f"Sales bill {billno}")


def post_purchase(docno: str, tdate: str, totals, cash: bool = False,
                  creditor: str = "SUNDRC") -> int:
    """Post a purchase's GL voucher. ``totals`` is a purchase BillTotals."""
    credit_acc = "CASH" if cash else creditor
    tax = D(totals.cgst) + D(totals.sgst) + D(totals.igst)
    legs = [
        ("PURCH", D(totals.taxable)),
        ("GSTIN", tax),
        ("ROUNDOFF", D(totals.round_off)),
        (credit_acc, -D(totals.grand_total)),
    ]
    return acc.post_legs(tdate, legs, control="P", refno=f"P:{docno}",
                         narration=f"Purchase {docno}")


def unpost_sale(billno: str):
    acc.remove_refno(f"S:{billno}")


def unpost_purchase(docno: str):
    acc.remove_refno(f"P:{docno}")
