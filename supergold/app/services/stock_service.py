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


# ---------------------------------------------------------------------------
# Stock transfer and stock add/less  (w_itemadj, w_itemadj_multi, w_stockaddless)
# ---------------------------------------------------------------------------

import datetime  # noqa: E402

import db  # noqa: E402
from app.services.cancel_service import adjust_stock  # noqa: E402


def _next_slno(table: str) -> int:
    try:
        row = db.fetch_one(f"SELECT COALESCE(MAX(slno),0) + 1 AS n FROM {table}")
        return int(row["n"]) if row else 1
    except Exception:
        return 1


def transfer_stock(from_code: str, to_code: str, *, qty=0, weight=0.0,
                   stonewgt=0.0, from_stktype="", to_stktype="", control=1,
                   tdate=None, note="") -> int:
    """Move stock from one item to another, as ``w_itemadj`` does.

    The giving item loses the quantity/weight, the receiving item gains it, and
    an ``itemadj`` row records the movement so it can be listed and cancelled.
    """
    from_code = (from_code or "").strip()
    to_code = (to_code or "").strip()
    if not from_code or not to_code:
        raise ValueError("Both the from-item and the to-item are needed")
    if from_code == to_code and from_stktype == to_stktype:
        raise ValueError("The from-item and the to-item are the same")
    if not (qty or weight or stonewgt):
        raise ValueError("Enter a quantity, weight or stone weight to transfer")

    tdate = tdate or datetime.date.today().isoformat()
    slno = _next_slno("itemadj")
    with db.transaction():
        adjust_stock(from_code, from_stktype, control, qty=qty, weight=weight,
                     stonewgt=stonewgt, sign=-1)
        adjust_stock(to_code, to_stktype, control, qty=qty, weight=weight,
                     stonewgt=stonewgt, sign=+1)
        columns = {c["name"].lower() for c in db.table_columns("itemadj")}
        values = {"slno": slno, "tdate": tdate, "fromcode": from_code,
                  "tocode": to_code, "fromqty": qty, "toqty": qty,
                  "fromwgt": weight, "towgt": weight, "fromstwgt": stonewgt,
                  "tostwgt": stonewgt, "fromstktype": from_stktype,
                  "tostktype": to_stktype, "control": control, "part": note}
        usable = {k: v for k, v in values.items() if k in columns}
        db.execute(f"INSERT INTO itemadj ({', '.join(usable)}) "
                   f"VALUES ({', '.join('?' for _ in usable)})",
                   list(usable.values()))
    return slno


def add_less_stock(code: str, *, qty=0, weight=0.0, stonewgt=0.0, stktype="",
                   control=1, add=True, tdate=None, note="") -> int:
    """Add stock to an item or take it out (``w_stockaddless``)."""
    code = (code or "").strip()
    if not code:
        raise ValueError("Choose the item")
    if not (qty or weight or stonewgt):
        raise ValueError("Enter a quantity, weight or stone weight")

    tdate = tdate or datetime.date.today().isoformat()
    slno = _next_slno("itemadj")
    sign = 1 if add else -1
    with db.transaction():
        adjust_stock(code, stktype, control, qty=qty, weight=weight,
                     stonewgt=stonewgt, sign=sign)
        columns = {c["name"].lower() for c in db.table_columns("itemadj")}
        side = "to" if add else "from"
        values = {"slno": slno, "tdate": tdate, f"{side}code": code,
                  f"{side}qty": qty, f"{side}wgt": weight,
                  f"{side}stwgt": stonewgt, f"{side}stktype": stktype,
                  "control": control, "part": note or ("Stock add" if add
                                                       else "Stock less")}
        usable = {k: v for k, v in values.items() if k in columns}
        db.execute(f"INSERT INTO itemadj ({', '.join(usable)}) "
                   f"VALUES ({', '.join('?' for _ in usable)})",
                   list(usable.values()))
    return slno
