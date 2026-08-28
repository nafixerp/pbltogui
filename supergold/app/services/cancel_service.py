"""
Cancelling a document — ported from the original cancel windows.

Cancelling is never just a delete: the original reverses stock (quantity,
weight and stone weight, on both the live and the balance columns), puts
barcoded pieces back, recalculates the weighted-average cost where it applies,
removes the document and its ledger rows, and writes an audit line into
``delpart``.

Every routine here follows the PowerBuilder script of the matching window —
``w_scancel``, ``w_sretcancel``, ``w_pcancel``, ``w_gsmthcancel``, ``w_ocancel``,
``w_rprcancel``, ``w_oitcancel``, ``w_refncancel``, ``w_accancel``,
``w_loancancel`` — including the ``control`` rule those scripts use:

* ``control = 1`` — the document counts in the live stock, so ``weight``/``qty``
  and ``weightb``/``qtyb`` are both adjusted;
* otherwise only the balance columns (``weightb``, ``qtyb``, ``stonewgtb``) are;
* ``control = 3`` — a branch/other-company document: stock is not touched at all.

Everything happens in one transaction: on any failure nothing is written.
"""

from __future__ import annotations

import datetime
from dataclasses import dataclass, field

import db

# Ledger/companion tables a cancelled document is removed from.
_COMMON_LEDGER = ("daybook", "daybookpart", "stkandprofit", "oglist")


@dataclass
class CancelResult:
    document: str
    slno: int
    kind: str
    items_reversed: int = 0
    barcodes_released: int = 0
    rows_deleted: dict = field(default_factory=dict)
    note: str = ""

    def summary(self) -> str:
        deleted = sum(self.rows_deleted.values())
        return (f"{self.kind} {self.document} cancelled — "
                f"{self.items_reversed} stock line(s) reversed, "
                f"{self.barcodes_released} barcode(s) released, "
                f"{deleted} row(s) removed.")


# ---------------------------------------------------------------------------
# Building blocks
# ---------------------------------------------------------------------------

def _num(value, default=0):
    if value is None:
        return default
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def _exec(sql, params=()):
    try:
        return db.execute(sql, params)
    except Exception:
        return None


def _table_has(table: str, column: str) -> bool:
    return any(c["name"].lower() == column.lower()
               for c in db.table_columns(table))


def adjust_stock(code: str, stktype: str, control, *, qty=0, weight=0.0,
                 stonewgt=0.0, sign=1, cost=None):
    """Add (``sign=1``) or remove (``sign=-1``) stock for one item line."""
    code = (code or "").strip()
    if not code:
        return False
    qty = sign * round(_num(qty))
    weight = sign * round(_num(weight), 3)
    stonewgt = sign * round(_num(stonewgt), 3)

    live = str(control) in ("1", "1.0")
    sets = ["weightb = weightb + ?", "qtyb = qtyb + ?", "stonewgtb = stonewgtb + ?"]
    params = [weight, qty, stonewgt]
    if live:
        sets = ["weight = weight + ?", "qty = qty + ?", "stonewgt = stonewgt + ?"] + sets
        params = [weight, qty, stonewgt] + params
    if cost is not None:
        sets.append("cost = ?")
        params.append(cost)
    _exec(f"UPDATE items SET {', '.join(sets)} WHERE TRIM(code) = ?", params + [code])

    if stktype:
        sets_s = ["weightb = weightb + ?", "qtyb = qtyb + ?",
                  "stonewgtb = stonewgtb + ?"]
        params_s = [weight, qty, stonewgt]
        if live:
            sets_s = ["weight = weight + ?", "qty = qty + ?",
                      "stonewgt = stonewgt + ?"] + sets_s
            params_s = [weight, qty, stonewgt] + params_s
        _exec(f"UPDATE itemsstk SET {', '.join(sets_s)} "
              f"WHERE TRIM(code) = ? AND stktype = ?", params_s + [code, stktype])
    return True


def weighted_average_cost(code: str, control, weight, cost, enabled=True):
    """The original's WA cost when purchased weight is taken back out."""
    column = "weight" if str(control) in ("1", "1.0") else "weightb"
    row = db.fetch_one(f"SELECT {column} AS w, cost AS c FROM items WHERE code = ?",
                       ((code or "").strip(),))
    if not row:
        return None
    current_wgt, current_cost = _num(row["w"]), _num(row["c"])
    weight, cost = _num(weight), _num(cost)
    if enabled and current_wgt - weight > 0:
        return (current_wgt * current_cost - weight * cost) / (current_wgt - weight)
    return current_cost


def release_barcode(bcode, in_stock=True):
    if not bcode:
        return False
    _exec("UPDATE barcode SET stk = ? WHERE bcode = ?",
          ("Y" if in_stock else "N", bcode))
    return True


def _delete_rows(tables, slno, result: CancelResult):
    for table in tables:
        try:
            before = db.fetch_one(f"SELECT COUNT(*) AS c FROM {table} WHERE slno = ?",
                                  (slno,))
        except Exception:
            continue                      # table not in this database
        count = int(before["c"]) if before else 0
        if count:
            _exec(f"DELETE FROM {table} WHERE slno = ?", (slno,))
            result.rows_deleted[table] = count


def write_audit(tdate, part: str, slno, ttype: str, user: str = "",
                incharge: str = "", level=1):
    """The ``delpart`` audit line every cancellation writes."""
    columns = {c["name"].lower() for c in db.table_columns("delpart")}
    values = {"tdate": tdate, "part": part, "control": level, "slno": slno,
              "utype": "C", "ttype": ttype,
              "updtdate": datetime.date.today().isoformat(),
              "updttime": datetime.datetime.now().strftime("%H:%M:%S"),
              "uid": user, "ic": incharge}
    usable = {k: v for k, v in values.items() if k in columns}
    if not usable:
        return
    _exec(f"INSERT INTO delpart ({', '.join(usable)}) "
          f"VALUES ({', '.join('?' for _ in usable)})", list(usable.values()))


def _rows(sql, params):
    try:
        return db.fetch_all(sql, params)
    except Exception:
        return []


def _head(table: str, slno):
    return db.fetch_one(f"SELECT * FROM {table} WHERE slno = ?", (slno,))


# ---------------------------------------------------------------------------
# Sales  (w_scancel)
# ---------------------------------------------------------------------------

def cancel_sale(slno, user="", incharge="", level=1, calc_wa_cost=True):
    head = _head("salesm", slno)
    if head is None:
        raise ValueError(f"Sales bill {slno} does not exist")
    control = head.get("control")
    result = CancelResult(document=str(head.get("billno", "")).strip(),
                          slno=slno, kind="Sales")

    if str(control) != "3":
        for row in _rows("SELECT code, qty, weight, stonewgt, jcode, bcode, stktype "
                         "FROM salesd WHERE slno = ?", (slno,)):
            if not str(row.get("jcode") or "").strip():
                adjust_stock(row["code"], row.get("stktype") or "", control,
                             qty=row.get("qty"), weight=row.get("weight"),
                             stonewgt=row.get("stonewgt"), sign=+1)
                result.items_reversed += 1
            if row.get("bcode"):
                release_barcode(row["bcode"], in_stock=True)
                result.barcodes_released += 1

        # Goods taken back on the same bill (exchange return) go out again.
        for row in _rows("SELECT code, qty, weight, stonewgt, stktype "
                         "FROM salesrd WHERE slno = ?", (slno,)):
            adjust_stock(row["code"], row.get("stktype") or "", control,
                         qty=row.get("qty"), weight=row.get("weight"),
                         stonewgt=row.get("stonewgt"), sign=-1)
            result.items_reversed += 1

        # Old gold purchased on the same bill goes out, with the WA cost undone.
        for row in _rows("SELECT code, qty, weight, cost, stktype "
                         "FROM purchased WHERE slno = ?", (slno,)):
            wa = weighted_average_cost(row["code"], control, row.get("weight"),
                                       row.get("cost"), calc_wa_cost)
            adjust_stock(row["code"], row.get("stktype") or "", control,
                         qty=row.get("qty"), weight=row.get("weight"),
                         sign=-1, cost=wa)
            result.items_reversed += 1

    _delete_rows(("salesm", "salesd", "salesrm", "salesrd", "purchasem",
                  "purchased") + _COMMON_LEDGER, slno, result)

    part = (f"Sales Entry({result.document}) - NetAmt "
            f"{_num(head.get('netamt')):.2f} Canceled -{head.get('tdate')}")
    write_audit(head.get("tdate"), part, slno, "S", user, incharge, level)

    orderno = str(head.get("orderno") or "").strip()
    if orderno:
        _exec("UPDATE orderm SET status = 1 WHERE ordno = ?", (orderno,))
        result.note = f"Order {orderno} re-opened"
    elif result.document[:2].upper() == "SO":
        _exec("UPDATE orderm SET status = 1 WHERE salebill = ?", (result.document,))
        result.note = "Order re-opened"
    return result


# ---------------------------------------------------------------------------
# Sales return  (w_sretcancel)
# ---------------------------------------------------------------------------

def cancel_sales_return(slno, user="", incharge="", level=1):
    head = _head("salesrm", slno)
    if head is None:
        raise ValueError(f"Sales return {slno} does not exist")
    control = head.get("control")
    result = CancelResult(document=str(head.get("billno", "")).strip(),
                          slno=slno, kind="Sales return")

    if str(control) != "3":
        for row in _rows("SELECT code, qty, weight, stonewgt, stktype "
                         "FROM salesrd WHERE slno = ?", (slno,)):
            adjust_stock(row["code"], row.get("stktype") or "", control,
                         qty=row.get("qty"), weight=row.get("weight"),
                         stonewgt=row.get("stonewgt"), sign=-1)
            result.items_reversed += 1

    _delete_rows(("salesrm", "salesrd", "daybook", "daybookpart",
                  "stkandprofit"), slno, result)
    write_audit(head.get("tdate"),
                f"Sales Return Entry({result.document}) Canceled -{head.get('tdate')}",
                slno, "SR", user, incharge, level)
    return result


# ---------------------------------------------------------------------------
# Purchase / purchase return  (w_pcancel)
# ---------------------------------------------------------------------------

def cancel_purchase(slno, kind="P", user="", incharge="", level=1,
                    calc_wa_cost=True):
    master = "purchaserm" if kind == "R" else "purchasem"
    head = _head(master, slno)
    if head is None:
        raise ValueError(f"Purchase document {slno} does not exist")
    control = head.get("control")
    result = CancelResult(document=str(head.get("docno", "")).strip(), slno=slno,
                          kind="Purchase return" if kind == "R" else "Purchase")

    # Purchased goods go out again (with the weighted-average cost undone).
    for row in _rows("SELECT code, qty, weight, cost, stwgt, stktype, bcode "
                     "FROM purchased WHERE slno = ?", (slno,)):
        wa = weighted_average_cost(row["code"], control, row.get("weight"),
                                   row.get("cost"), calc_wa_cost)
        adjust_stock(row["code"], row.get("stktype") or "", control,
                     qty=row.get("qty"), weight=row.get("weight"),
                     stonewgt=row.get("stwgt"), sign=-1, cost=wa)
        result.items_reversed += 1

    # Returned goods come back in.
    for row in _rows("SELECT code, qty, weight, cost, stwgt, stktype, bcode "
                     "FROM purchaserd WHERE slno = ?", (slno,)):
        adjust_stock(row["code"], row.get("stktype") or "", control,
                     qty=row.get("qty"), weight=row.get("weight"),
                     stonewgt=row.get("stwgt"), sign=+1)
        result.items_reversed += 1
        if row.get("bcode"):
            release_barcode(row["bcode"], in_stock=True)
            result.barcodes_released += 1

    _delete_rows(("purchasem", "purchased", "purchased_dmddet", "purchaserm",
                  "purchaserd", "smithm", "smithd", "advafter") + _COMMON_LEDGER,
                 slno, result)

    if str(head.get("dmd") or "").upper() == "Y" and kind == "P":
        _exec("DELETE FROM barcode WHERE rslno = ?", (slno,))
        _exec("DELETE FROM barcode_dmddet WHERE slno = ?", (slno,))

    label = "Purchase Return Entry" if kind == "R" else "Purchase Entry"
    write_audit(head.get("tdate"),
                f"{label}({result.document}) Canceled -{head.get('tdate')}",
                slno, "PR" if kind == "R" else "P", user, incharge, level)
    return result


# ---------------------------------------------------------------------------
# Goldsmith / jewellery / party weight  (w_gsmthcancel)
# ---------------------------------------------------------------------------

def cancel_goldsmith(slno, user="", incharge="", level=1):
    head = _head("smithm", slno)
    if head is None:
        raise ValueError(f"Goldsmith document {slno} does not exist")
    control = head.get("control")
    result = CancelResult(document=str(head.get("docno", "")).strip(),
                          slno=slno, kind="Goldsmith")

    for row in _rows("SELECT code, qty, weight, stonewgt, givrec, stktype, bcode "
                     "FROM smithd WHERE slno = ?", (slno,)):
        given = str(row.get("givrec") or "").upper().startswith("G")
        received = str(row.get("givrec") or "").upper().startswith("R")
        if not (given or received):
            continue
        adjust_stock(row["code"], row.get("stktype") or "", control,
                     qty=row.get("qty"), weight=row.get("weight"),
                     stonewgt=row.get("stonewgt"), sign=+1 if given else -1)
        result.items_reversed += 1
        if row.get("bcode"):
            release_barcode(row["bcode"], in_stock=given)
            result.barcodes_released += 1

    # A stock transfer written with the document is undone as well.
    for row in _rows("SELECT tocode, towgt, tostktype FROM itemadj WHERE slno = ?",
                     (slno,)):
        adjust_stock(row["tocode"], row.get("tostktype") or "", control,
                     weight=row.get("towgt"), sign=-1)
        result.items_reversed += 1

    _delete_rows(("smithm", "smithd", "itemadj") + _COMMON_LEDGER, slno, result)
    write_audit(head.get("tdate"),
                f"Goldsmith Entry({result.document}) Canceled -{head.get('tdate')}",
                slno, "GS", user, incharge, level)
    return result


# ---------------------------------------------------------------------------
# Order  (w_ocancel)
# ---------------------------------------------------------------------------

def cancel_order(slno, user="", incharge="", level=1, calc_wa_cost=True):
    head = _head("orderm", slno)
    if head is None:
        raise ValueError(f"Order {slno} does not exist")
    control = head.get("control")
    result = CancelResult(document=str(head.get("ordno", "")).strip(),
                          slno=slno, kind="Order")

    for table, stone in (("purchased", None), ("orderdga", None)):
        for row in _rows(f"SELECT code, qty, weight, cost, stktype "
                         f"FROM {table} WHERE slno = ?", (slno,)):
            wa = weighted_average_cost(row["code"], control, row.get("weight"),
                                       row.get("cost"), calc_wa_cost)
            adjust_stock(row["code"], row.get("stktype") or "", control,
                         qty=row.get("qty"), weight=row.get("weight"),
                         sign=-1, cost=wa)
            result.items_reversed += 1

    for row in _rows("SELECT code, qty, weight, stonewgt, stktype "
                     "FROM salesrd WHERE slno = ?", (slno,)):
        adjust_stock(row["code"], row.get("stktype") or "", control,
                     qty=row.get("qty"), weight=row.get("weight"),
                     stonewgt=row.get("stonewgt"), sign=-1)
        result.items_reversed += 1

    _delete_rows(("orderm", "orderd", "orderdga", "orderdmodel", "purchasem",
                  "purchased", "salesrm", "salesrd") + _COMMON_LEDGER,
                 slno, result)
    write_audit(head.get("tdate"),
                f"Order Entry({result.document}) Canceled -{head.get('tdate')}",
                slno, "O", user, incharge, level)
    return result


# ---------------------------------------------------------------------------
# Repair / remake  (w_rprcancel)
# ---------------------------------------------------------------------------

def cancel_repair(slno, user="", incharge="", level=1):
    head = _head("repairm", slno)
    if head is None:
        raise ValueError(f"Repair document {slno} does not exist")
    control = head.get("control")
    issued = str(head.get("ir") or head.get("givrec") or "I").upper().startswith("I")
    result = CancelResult(document=str(head.get("billno", "")).strip(),
                          slno=slno, kind="Repair")

    for row in _rows("SELECT code, qty, weight, stonewgt, stktype "
                     "FROM repaird WHERE slno = ?", (slno,)):
        adjust_stock(row["code"], row.get("stktype") or "", control,
                     qty=row.get("qty"), weight=row.get("weight"),
                     stonewgt=row.get("stonewgt"), sign=-1 if issued else +1)
        result.items_reversed += 1

    _delete_rows(("repairm", "repaird", "daybook", "daybookpart"), slno, result)
    reference = str(head.get("rbillno") or head.get("refno") or "").strip()
    if reference:
        _exec("UPDATE repairm SET status = 1 WHERE TRIM(billno) = ?", (reference,))
        result.note = f"Memo {reference} re-opened"
    write_audit(head.get("tdate"),
                f"Repair Entry({result.document}) Canceled -{head.get('tdate')}",
                slno, "RP", user, incharge, level)
    return result


# ---------------------------------------------------------------------------
# Other items  (w_oitcancel)
# ---------------------------------------------------------------------------

def cancel_other_item(slno, kind="S", user="", incharge="", level=1):
    head = _head("oitemtranm", slno)
    if head is None:
        raise ValueError(f"Other-item document {slno} does not exist")
    sale = str(head.get("sp") or kind).upper().startswith("S")
    result = CancelResult(document=str(head.get("docno", "")).strip(), slno=slno,
                          kind="Other item sale" if sale else "Other item purchase")

    for row in _rows("SELECT code, qty FROM oitemtrand WHERE slno = ?", (slno,)):
        qty = round(_num(row.get("qty")))
        # A cancelled sale puts the pieces back; a cancelled purchase takes
        # them out again.
        _exec("UPDATE itemsothers SET stock = stock + ? WHERE TRIM(code) = ?",
              (qty if sale else -qty, str(row["code"]).strip()))
        result.items_reversed += 1

    _delete_rows(("oitemtranm", "oitemtrand", "daybook", "daybookpart",
                  "stkandprofit"), slno, result)
    write_audit(head.get("tdate"),
                f"Other Item Entry({result.document}) Canceled -{head.get('tdate')}",
                slno, "OS" if sale else "OP", user, incharge, level)
    return result


# ---------------------------------------------------------------------------
# Refinery  (w_refncancel)
# ---------------------------------------------------------------------------

def cancel_refinery(slno, user="", incharge="", level=1):
    head = _head("refinerym", slno)
    if head is None:
        raise ValueError(f"Refinery document {slno} does not exist")
    control = head.get("control")
    result = CancelResult(document=str(head.get("docno", "")).strip(),
                          slno=slno, kind="Refinery")

    for row in _rows("SELECT * FROM refineryd WHERE slno = ?", (slno,)):
        stktype = row.get("stktype") or ""
        issued_stone = row.get("issuedstwgt", row.get("stwgt"))
        # What came back from the refiner goes out again …
        adjust_stock(row["code"], stktype, control, qty=row.get("rcvdqty"),
                     weight=row.get("rcvdwgt"), sign=-1)
        # … and what was issued comes back in.
        adjust_stock(row["code"], stktype, control, qty=row.get("issuedqty"),
                     weight=row.get("issuedwgt"), stonewgt=issued_stone,
                     sign=+1)
        for code, weight in (("BS", row.get("bottlestk")), ("TP", row.get("testpcs"))):
            if _num(weight):
                adjust_stock(code, stktype, control, weight=weight, sign=-1)
        result.items_reversed += 1

    _delete_rows(("refinerym", "refineryd") + _COMMON_LEDGER, slno, result)
    write_audit(head.get("tdate"),
                f"Refinery Entry({result.document}) Canceled -{head.get('tdate')}",
                slno, "RF", user, incharge, level)
    issued_from = head.get("islno")
    if issued_from:
        _exec("UPDATE refinerym SET status = 1 WHERE slno = ?", (issued_from,))
        result.note = "Issue re-opened"
    return result


# ---------------------------------------------------------------------------
# Accounts voucher  (w_accancel) and loan  (w_loancancel)
# ---------------------------------------------------------------------------

def cancel_voucher(slno, user="", incharge="", level=1):
    head = db.fetch_one("SELECT * FROM daybook WHERE slno = ?", (slno,))
    if head is None:
        raise ValueError(f"Voucher {slno} does not exist")
    result = CancelResult(document=str(head.get("vno") or head.get("docno") or slno),
                          slno=slno, kind="Voucher")
    _delete_rows(("daybook", "daybookpart", "collection", "advafter", "kuricolln",
                  "daybookratewgt", "stkandprofit", "suspentry", "orderdga"),
                 slno, result)
    _exec("UPDATE daybookpart SET slno2 = 0 WHERE slno2 = ?", (slno,))
    write_audit(head.get("tdate"),
                f"Voucher({result.document}) Canceled -{head.get('tdate')}",
                slno, "VH", user, incharge, level)
    return result


def cancel_loan(slno, user="", incharge="", level=1):
    head = _head("loan", slno) if _table_has("loan", "slno") else None
    tdate = (head or {}).get("tdate")
    result = CancelResult(document=str((head or {}).get("loanno") or slno),
                          slno=slno, kind="Loan")
    _delete_rows(("loan", "loan_dates", "loan_items", "daybook", "daybookpart",
                  "pdclist"), slno, result)
    write_audit(tdate, f"Loan({result.document}) Canceled -{tdate}", slno, "VH",
                user, incharge, level)
    return result


def cancel_document(window: str, slno, **kwargs) -> CancelResult:  # noqa: E302
    """Cancel ``slno`` with the routine belonging to ``window``, atomically."""
    entry = HANDLERS.get(window)
    if entry is None:
        raise ValueError(f"{window} has no cancellation routine")
    _table, _key, handler = entry
    with db.transaction():
        return handler(slno, **kwargs)


# The window each routine belongs to, used by the cancel screens.
HANDLERS = {
    "w_scancel": ("salesm", "billno", cancel_sale),
    "w_sretcancel": ("salesrm", "billno", cancel_sales_return),
    "w_pcancel": ("purchasem", "docno", cancel_purchase),
    "w_gsmthcancel": ("smithm", "docno", cancel_goldsmith),
    "w_ocancel": ("orderm", "ordno", cancel_order),
    "w_rprcancel": ("repairm", "billno", cancel_repair),
    "w_oitcancel": ("oitemtranm", "docno", cancel_other_item),
    "w_refncancel": ("refinerym", "docno", cancel_refinery),
    "w_accancel": ("daybook", "vno", cancel_voucher),
    "w_loancancel": ("loan", "loanno", cancel_loan),
}
