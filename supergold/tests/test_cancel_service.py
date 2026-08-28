"""Cancelling a document reverses exactly what the original reversed."""

import os
import sys

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

import db  # noqa: E402
from app.services import cancel_service as cx  # noqa: E402


@pytest.fixture()
def erp(tmp_path, monkeypatch):
    """A miniature GMINE database: items, a sales bill and its ledger rows."""
    monkeypatch.setattr(db, "ENGINE", "sqlite")
    monkeypatch.setattr(db, "SQLITE_PATH", str(tmp_path / "cancel.db"))
    ddl = [
        """CREATE TABLE items (code TEXT, qty INT, weight REAL, stonewgt REAL,
             qtyb INT, weightb REAL, stonewgtb REAL, cost REAL)""",
        """CREATE TABLE itemsstk (code TEXT, stktype TEXT, qty INT, weight REAL,
             stonewgt REAL, qtyb INT, weightb REAL, stonewgtb REAL)""",
        "CREATE TABLE barcode (bcode INT, stk TEXT, rslno INT)",
        """CREATE TABLE salesm (slno INT, billno TEXT, tdate DATE, netamt REAL,
             control INT, orderno TEXT)""",
        """CREATE TABLE salesd (slno INT, code TEXT, qty INT, weight REAL,
             stonewgt REAL, jcode TEXT, bcode INT, stktype TEXT)""",
        "CREATE TABLE salesrm (slno INT, billno TEXT, tdate DATE, control INT)",
        """CREATE TABLE salesrd (slno INT, code TEXT, qty INT, weight REAL,
             stonewgt REAL, stktype TEXT)""",
        "CREATE TABLE purchasem (slno INT, docno TEXT, tdate DATE, control INT, dmd TEXT)",
        """CREATE TABLE purchased (slno INT, code TEXT, qty INT, weight REAL,
             cost REAL, stwgt REAL, stktype TEXT, bcode INT)""",
        """CREATE TABLE purchaserm (slno INT, docno TEXT, tdate DATE, control INT)""",
        """CREATE TABLE purchaserd (slno INT, code TEXT, qty INT, weight REAL,
             cost REAL, stwgt REAL, stktype TEXT, bcode INT)""",
        "CREATE TABLE smithm (slno INT, docno TEXT, tdate DATE, control INT)",
        """CREATE TABLE smithd (slno INT, code TEXT, qty INT, weight REAL,
             stonewgt REAL, givrec TEXT, stktype TEXT, bcode INT)""",
        """CREATE TABLE itemadj (slno INT, tocode TEXT, towgt REAL, tostktype TEXT)""",
        "CREATE TABLE orderm (slno INT, ordno TEXT, tdate DATE, control INT, status INT, salebill TEXT)",
        "CREATE TABLE orderd (slno INT)",
        "CREATE TABLE orderdga (slno INT, code TEXT, qty INT, weight REAL, cost REAL, stktype TEXT)",
        "CREATE TABLE orderdmodel (slno INT)",
        "CREATE TABLE daybook (slno INT, tdate DATE, vno TEXT)",
        "CREATE TABLE daybookpart (slno INT, slno2 INT)",
        "CREATE TABLE stkandprofit (slno INT)",
        "CREATE TABLE oglist (slno INT)",
        "CREATE TABLE advafter (slno INT)",
        """CREATE TABLE delpart (tdate DATE, part TEXT, control INT, slno INT,
             utype TEXT, ttype TEXT, updtdate DATE, updttime TEXT, uid TEXT, ic TEXT)""",
        "CREATE TABLE itemsothers (code TEXT, stock INT, cost REAL)",
        "CREATE TABLE oitemtranm (slno INT, docno TEXT, tdate DATE, sp TEXT)",
        "CREATE TABLE oitemtrand (slno INT, code TEXT, qty INT, cost REAL)",
    ]
    for statement in ddl:
        db.execute(statement)
    db.execute("INSERT INTO items VALUES ('G22', 10, 100.0, 5.0, 10, 100.0, 5.0, 3000)")
    db.execute("INSERT INTO itemsstk VALUES ('G22','COUNTER1', 10, 100.0, 5.0, 10, 100.0, 5.0)")
    return tmp_path


def item(code="G22"):
    return db.fetch_one("SELECT * FROM items WHERE code = ?", (code,))


def make_sale(control=1, qty=2, weight=20.0, stonewgt=1.0, bcode=None, jcode=None):
    db.execute("INSERT INTO salesm VALUES (1,'B1','2026-06-01',50000,?,NULL)", (control,))
    db.execute("INSERT INTO salesd VALUES (1,'G22',?,?,?,?,?,'COUNTER1')",
               (qty, weight, stonewgt, jcode, bcode))
    db.execute("INSERT INTO daybook VALUES (1,'2026-06-01','V1')")
    db.execute("INSERT INTO stkandprofit VALUES (1)")


# --- sales -----------------------------------------------------------------

def test_cancelling_a_sale_puts_the_stock_back(erp):
    make_sale()
    result = cx.cancel_document("w_scancel", 1)
    row = item()
    assert (row["qty"], row["weight"], row["stonewgt"]) == (12, 120.0, 6.0)
    assert (row["qtyb"], row["weightb"], row["stonewgtb"]) == (12, 120.0, 6.0)
    assert result.items_reversed == 1
    stk = db.fetch_one("SELECT * FROM itemsstk WHERE code='G22'")
    assert (stk["qty"], stk["weight"]) == (12, 120.0)


def test_cancelling_a_sale_removes_the_document_and_its_ledger(erp):
    make_sale()
    cx.cancel_document("w_scancel", 1)
    for table in ("salesm", "salesd", "daybook", "stkandprofit"):
        assert db.fetch_all(f"SELECT * FROM {table}") == []


def test_cancelling_writes_the_audit_line(erp):
    make_sale()
    cx.cancel_document("w_scancel", 1, user="U1", incharge="IC", level=2)
    audit = db.fetch_one("SELECT * FROM delpart")
    assert audit["ttype"] == "S" and audit["utype"] == "C"
    assert audit["slno"] == 1 and audit["uid"] == "U1"
    assert "Sales Entry(B1)" in audit["part"] and "50000.00" in audit["part"]


def test_control_2_touches_only_the_balance_columns(erp):
    make_sale(control=2)
    cx.cancel_document("w_scancel", 1)
    row = item()
    assert (row["qty"], row["weight"]) == (10, 100.0)          # live untouched
    assert (row["qtyb"], row["weightb"]) == (12, 120.0)


def test_control_3_does_not_touch_stock_at_all(erp):
    make_sale(control=3)
    cx.cancel_document("w_scancel", 1)
    row = item()
    assert (row["qty"], row["weight"], row["qtyb"], row["weightb"]) == \
        (10, 100.0, 10, 100.0)
    assert db.fetch_all("SELECT * FROM salesm") == []          # still removed


def test_a_barcoded_piece_goes_back_into_stock(erp):
    db.execute("INSERT INTO barcode VALUES (55,'N',NULL)")
    make_sale(bcode=55)
    result = cx.cancel_document("w_scancel", 1)
    assert db.fetch_one("SELECT stk FROM barcode WHERE bcode=55")["stk"] == "Y"
    assert result.barcodes_released == 1


def test_job_work_lines_do_not_move_stock(erp):
    make_sale(jcode="J1")
    cx.cancel_document("w_scancel", 1)
    row = item()
    assert (row["qty"], row["weight"]) == (10, 100.0)


def test_old_gold_taken_in_on_the_bill_goes_out_again(erp):
    make_sale()
    db.execute("INSERT INTO purchased VALUES (1,'G22',1,10.0,2500,0,'COUNTER1',NULL)")
    cx.cancel_document("w_scancel", 1)
    row = item()
    # +2/+20 from the sale, then -1/-10 for the exchange purchase
    assert (row["qty"], row["weight"]) == (11, 110.0)


def test_cancelling_a_sale_reopens_its_order(erp):
    make_sale()
    db.execute("UPDATE salesm SET orderno = 'ORD9' WHERE slno = 1")
    db.execute("INSERT INTO orderm VALUES (9,'ORD9','2026-05-01',1,2,'B1')")
    cx.cancel_document("w_scancel", 1)
    assert db.fetch_one("SELECT status FROM orderm WHERE ordno='ORD9'")["status"] == 1


def test_unknown_document_is_refused(erp):
    with pytest.raises(ValueError):
        cx.cancel_document("w_scancel", 999)


def test_nothing_is_written_when_the_reversal_fails(erp, monkeypatch):
    make_sale()
    monkeypatch.setattr(cx, "write_audit",
                        lambda *a, **k: (_ for _ in ()).throw(RuntimeError("boom")))
    with pytest.raises(RuntimeError):
        cx.cancel_document("w_scancel", 1)
    assert len(db.fetch_all("SELECT * FROM salesm")) == 1       # rolled back
    row = item()
    assert (row["qty"], row["weight"]) == (10, 100.0)


# --- other documents -------------------------------------------------------

def test_cancelling_a_purchase_takes_the_goods_out(erp):
    db.execute("INSERT INTO purchasem VALUES (2,'P1','2026-06-02',1,'N')")
    db.execute("INSERT INTO purchased VALUES (2,'G22',3,30.0,2800,1.0,'COUNTER1',NULL)")
    cx.cancel_document("w_pcancel", 2)
    row = item()
    assert (row["qty"], row["weight"], row["stonewgt"]) == (7, 70.0, 4.0)
    assert db.fetch_one("SELECT ttype FROM delpart")["ttype"] == "P"


def test_purchase_cancel_recalculates_the_average_cost(erp):
    db.execute("INSERT INTO purchasem VALUES (2,'P1','2026-06-02',1,'N')")
    db.execute("INSERT INTO purchased VALUES (2,'G22',0,20.0,4000,0,'',NULL)")
    cx.cancel_document("w_pcancel", 2)
    # (100*3000 - 20*4000) / (100-20) = 2750
    assert item()["cost"] == pytest.approx(2750.0)


def test_cancelling_a_goldsmith_issue_brings_the_metal_back(erp):
    db.execute("INSERT INTO smithm VALUES (3,'GS1','2026-06-03',1)")
    db.execute("INSERT INTO smithd VALUES (3,'G22',1,15.0,0,'G','COUNTER1',NULL)")
    cx.cancel_document("w_gsmthcancel", 3)
    assert item()["weight"] == pytest.approx(115.0)
    assert db.fetch_one("SELECT ttype FROM delpart")["ttype"] == "GS"


def test_cancelling_a_goldsmith_receipt_takes_the_metal_out(erp):
    db.execute("INSERT INTO smithm VALUES (4,'GS2','2026-06-03',1)")
    db.execute("INSERT INTO smithd VALUES (4,'G22',1,15.0,0,'R','COUNTER1',NULL)")
    cx.cancel_document("w_gsmthcancel", 4)
    assert item()["weight"] == pytest.approx(85.0)


def test_cancelling_an_other_item_sale_puts_the_pieces_back(erp):
    db.execute("INSERT INTO itemsothers VALUES ('BOX', 5, 20)")
    db.execute("INSERT INTO oitemtranm VALUES (6,'OI1','2026-06-04','S')")
    db.execute("INSERT INTO oitemtrand VALUES (6,'BOX',2,20)")
    cx.cancel_document("w_oitcancel", 6)
    assert db.fetch_one("SELECT stock FROM itemsothers")["stock"] == 7


def test_cancelling_a_voucher_clears_its_ledger_rows(erp):
    db.execute("INSERT INTO daybook VALUES (8,'2026-06-05','V8')")
    db.execute("INSERT INTO daybookpart VALUES (8, 0)")
    db.execute("INSERT INTO daybookpart VALUES (9, 8)")
    cx.cancel_document("w_accancel", 8)
    assert db.fetch_all("SELECT * FROM daybook WHERE slno = 8") == []
    assert db.fetch_one("SELECT slno2 FROM daybookpart WHERE slno = 9")["slno2"] == 0
    assert db.fetch_one("SELECT ttype FROM delpart")["ttype"] == "VH"


def test_every_cancel_window_has_a_routine():
    from app import modules
    for window in cx.HANDLERS:
        assert modules.get_factory(window) is not None
