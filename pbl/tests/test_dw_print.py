"""Printing a document on its original designed form."""

import os
import sys

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from app.pb_parser import DWLayout, LayoutObject  # noqa: E402
from app.reports import layouts as dw_layouts  # noqa: E402
from app.reports.dw_print import (  # noqa: E402
    format_value, page_size, render_pdf, value_for)


def simple_layout() -> DWLayout:
    layout = DWLayout(name="d_test", bands={"header": 200, "detail": 100,
                                            "footer": 120, "summary": 0},
                      paper=9, margins={"left": 100, "right": 100})
    layout.objects = [
        LayoutObject(kind="text", band="header", text="TAX INVOICE",
                     x=0, y=0, width=1000, height=64, bold=True, size=12),
        LayoutObject(kind="column", band="header", name="billno",
                     x=1200, y=0, width=400, height=64),
        LayoutObject(kind="line", band="header", x1=0, y1=180, x2=2000, y2=180),
        LayoutObject(kind="column", band="detail", name="items_name",
                     x=0, y=10, width=900, height=64),
        LayoutObject(kind="column", band="detail", name="weight",
                     x=1000, y=10, width=400, height=64,
                     format="#####0.000", alignment=1),
        LayoutObject(kind="compute", band="footer", name="total",
                     expression="sum(weight for all)", format="#####0.000",
                     x=1000, y=10, width=400, height=64, alignment=1),
    ]
    return layout


# --- formatting ------------------------------------------------------------

def test_number_masks():
    assert format_value(1234.5, "#####0.000") == "1234.500"
    assert format_value(1234.5, "#,##0.00") == "1,234.50"
    assert format_value(None, "#####0.000") == ""
    assert format_value("abc", "#####0.000") == "abc"


def test_date_masks():
    assert format_value("2026-06-01", "dd/mm/yyyy") == "01/06/2026"
    assert format_value("2026-06-01", "dd-mm-yy") == "01-06-26"
    assert format_value("not a date", "dd/mm/yyyy") == "not a date"


def test_general_mask_passes_through():
    assert format_value(7, "[GENERAL]") == "7"
    assert format_value("x", "") == "x"


# --- values ----------------------------------------------------------------

def test_column_value_matches_by_alias_or_short_name():
    column = LayoutObject(kind="column", name="salesd_weight")
    assert value_for(column, {"salesd_weight": 10.5}, []) == 10.5
    assert value_for(column, {"weight": 3.25}, []) == 3.25
    assert value_for(column, {}, []) is None


def test_computed_totals():
    rows = [{"weight": 10.0}, {"weight": 5.5}]
    total = LayoutObject(kind="compute", expression="sum(weight for all)")
    count = LayoutObject(kind="compute", expression="count(weight for all)")
    assert value_for(total, rows[0], rows) == 15.5
    assert value_for(count, rows[0], rows) == 2


def test_today_and_literal_expressions():
    import datetime
    today = LayoutObject(kind="compute", expression="today()")
    assert value_for(today, {}, []) == datetime.date.today().isoformat()
    assert value_for(LayoutObject(kind="compute", expression="''"), {}, []) == ""


# --- the page --------------------------------------------------------------

def test_page_size_follows_the_datawindow():
    portrait = DWLayout(name="p", paper=9, orientation=0)
    landscape = DWLayout(name="l", paper=9, orientation=1)
    assert page_size(portrait) == (595.0, 842.0)
    assert page_size(landscape) == (842.0, 595.0)


def test_pdf_is_produced_with_the_rows(tmp_path):
    pytest.importorskip("reportlab")
    path = tmp_path / "bill.pdf"
    rows = [{"items_name": "Ring", "weight": 10.5},
            {"items_name": "Chain", "weight": 22.25}]
    render_pdf(simple_layout(), rows, str(path), {"billno": "B1"})
    assert path.exists() and path.stat().st_size > 800
    assert path.read_bytes().startswith(b"%PDF")


def test_pdf_without_rows_still_prints_the_form(tmp_path):
    pytest.importorskip("reportlab")
    path = tmp_path / "empty.pdf"
    render_pdf(simple_layout(), [], str(path))
    assert path.exists() and path.stat().st_size > 500


# --- the forms shipped with the build --------------------------------------

@pytest.mark.skipif(not dw_layouts.available(ROOT),
                    reason="no printed forms in this tree")
def test_the_build_ships_the_designed_forms():
    names = dw_layouts.names(ROOT)
    assert len(names) > 200
    assert any("saleprint" in n for n in names)
    assert any("gsmithprint" in n for n in names)
    layout = dw_layouts.load(names[0], ROOT)
    assert layout is not None and layout.objects and layout.bands


@pytest.mark.skipif(not dw_layouts.available(ROOT),
                    reason="no printed forms in this tree")
def test_a_window_offers_its_own_forms():
    from app import catalog
    window = catalog.load_window(ROOT, "w_sales")
    forms = dw_layouts.for_window(window, ROOT)
    assert forms and all("print" in f or "slip" in f for f in forms)


@pytest.mark.skipif(not dw_layouts.available(ROOT),
                    reason="no printed forms in this tree")
def test_every_shipped_form_renders(tmp_path):
    pytest.importorskip("reportlab")
    names = dw_layouts.names(ROOT)
    rows = [{"weight": 1.5, "amount": 100, "name": "Item"}]
    for name in names[:40]:
        layout = dw_layouts.load(name, ROOT)
        render_pdf(layout, rows, str(tmp_path / f"{name}.pdf"))
        assert (tmp_path / f"{name}.pdf").exists()
