"""Every list/report window runs its own DataWindow query."""

import os
import sys

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

import db  # noqa: E402
from app import catalog  # noqa: E402
from app.pb_parser import pbselect_to_sql  # noqa: E402

pytest.importorskip("PySide6.QtWidgets", reason="PySide6 not installed")
from PySide6.QtWidgets import QApplication  # noqa: E402

from app.reports.generic import GenericDataView, bind, default_for  # noqa: E402


# --- PBSELECT -> SQL -------------------------------------------------------

PBSELECT = ('PBSELECT( VERSION(400) TABLE(NAME="salesd" )  TABLE(NAME="items" ) '
            'COLUMN(NAME="salesd.slno") COLUMN(NAME="items.name") '
            'JOIN (LEFT="salesd.code"    OP ="="RIGHT="items.code" )'
            'WHERE(    EXP1 ="salesd.slno"   OP ="="    EXP2 =":rslno" ) ) '
            'ORDER(NAME="salesd.slno" ASC=yes ) ARG(NAME = "rslno" TYPE = number) ')


def test_pbselect_becomes_sql():
    sql, args = pbselect_to_sql(PBSELECT)
    assert sql == ("SELECT salesd.slno AS salesd_slno, items.name AS items_name "
                   "FROM salesd, items "
                   "WHERE salesd.code = items.code AND salesd.slno = :rslno "
                   "ORDER BY salesd.slno ASC")
    assert args == ["rslno"]


def test_multiple_conditions_keep_their_connectors():
    src = ('PBSELECT( TABLE(NAME="salesm" ) COLUMN(NAME="salesm.billno")'
           'WHERE(  EXP1 ="salesm.tdate" OP ="between" EXP2 =":rdate1 and :rdate2"'
           ' LOGIC ="and" ) WHERE( EXP1 ="salesm.control" OP ="<=" EXP2 =":rlevel" ) )'
           ' ARG(NAME = "rdate1" TYPE = date) ARG(NAME = "rdate2" TYPE = date)'
           ' ARG(NAME = "rlevel" TYPE = number)')
    sql, args = pbselect_to_sql(src)
    assert "WHERE salesm.tdate between :rdate1 and :rdate2 AND salesm.control <= :rlevel" in sql
    assert args == ["rdate1", "rdate2", "rlevel"]


def test_plain_sql_is_kept():
    sql, args = pbselect_to_sql('SELECT * FROM salesm WHERE tdate = :rdate1 ')
    assert sql.startswith("SELECT * FROM salesm")
    assert args == ["rdate1"]


# --- binding ---------------------------------------------------------------

def test_arguments_become_placeholders_in_order():
    sql, params = bind("SELECT 1 FROM t WHERE d between :a and :b AND c <= :n",
                       {"a": "2026-01-01", "b": "2026-01-31", "n": 9})
    assert sql == "SELECT 1 FROM t WHERE d between ? and ? AND c <= ?"
    assert params == ["2026-01-01", "2026-01-31", 9]


def test_defaults_by_argument_type():
    import datetime
    assert default_for("rdate1", "date") == datetime.date.today()
    assert default_for("rlevel", "number") == 9
    assert default_for("rcode", "string") == ""


# --- the widget ------------------------------------------------------------

@pytest.fixture(scope="session")
def qapp():
    return QApplication.instance() or QApplication([])


@pytest.fixture()
def sales_db(tmp_path, monkeypatch):
    monkeypatch.setattr(db, "ENGINE", "sqlite")
    monkeypatch.setattr(db, "SQLITE_PATH", str(tmp_path / "rep.db"))
    db.execute("CREATE TABLE salesm (billno TEXT, tdate DATE, billamt REAL)")
    db.execute("INSERT INTO salesm VALUES ('B1','2026-06-01',100.5)")
    db.execute("INSERT INTO salesm VALUES ('B2','2026-06-02',200.25)")
    return {
        "dataobject": "d_salesbook",
        "sql": "SELECT salesm.billno AS salesm_billno, salesm.billamt AS salesm_billamt"
               " FROM salesm WHERE salesm.tdate between :rdate1 and :rdate2",
        "args": ["rdate1", "rdate2"],
        "arg_types": {"rdate1": "date", "rdate2": "date"},
        "columns": [{"name": "salesm_billno", "label": "Bill No", "type": "char"},
                    {"name": "salesm_billamt", "label": "Amount", "type": "decimal"}],
    }


def test_view_runs_the_query_with_its_parameters(qapp, sales_db):
    view = GenericDataView(sales_db, "Sales Book")
    view._param_widgets["rdate1"].setDate(view._param_widgets["rdate1"].date().fromString(
        "2026-06-01", "yyyy-MM-dd"))
    view._param_widgets["rdate2"].setDate(view._param_widgets["rdate2"].date().fromString(
        "2026-06-30", "yyyy-MM-dd"))
    view.run()
    assert len(view._rows) == 2
    assert view._status.text() == "2 rows"
    assert view._labels() == ["Bill No", "Amount"]


def test_numeric_columns_are_totalled(qapp, sales_db):
    view = GenericDataView(sales_db, "Sales Book")
    view._param_widgets["rdate1"].setDate(view._param_widgets["rdate1"].date().fromString(
        "2026-01-01", "yyyy-MM-dd"))
    view._param_widgets["rdate2"].setDate(view._param_widgets["rdate2"].date().fromString(
        "2026-12-31", "yyyy-MM-dd"))
    view.run()
    total_row = view._grid.rowCount() - 1
    assert view._grid.item(total_row, 0).text() == "TOTAL"
    assert view._grid.item(total_row, 1).text() == "300.75"


def test_a_broken_query_is_reported_not_raised(qapp, sales_db):
    spec = dict(sales_db, sql="SELECT * FROM no_such_table")
    view = GenericDataView(spec, "Broken")
    assert view._rows == []
    assert "Query failed" in view._grid.item(0, 0).text()


# --- the catalog shipped with the build ------------------------------------

@pytest.mark.skipif(not catalog.available(ROOT), reason="no catalog in this tree")
def test_most_windows_have_a_query_definition():
    import json
    with open(os.path.join(ROOT, "data", "windows.json"), encoding="utf-8") as fh:
        windows = json.load(fh)
    with_report = [w for w in windows.values() if w.get("report", {}).get("sql")]
    assert len(with_report) >= 190
    for spec in with_report[:20]:
        assert spec["report"]["sql"].lower().startswith("select")
