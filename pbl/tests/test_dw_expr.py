"""The DataWindow expression evaluator — the original's own calculations."""

import datetime
import os
import sys

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from app.reports.dw_expr import ExpressionError, evaluate, tokenize  # noqa: E402

ROWS = [
    {"salesd_weight": 10.5, "salesd_stonewgt": 0.5, "salesd_rate": 5000,
     "salesd_mcharge": 300, "salesd_wastage": 0.8, "salesd_amount": 52000,
     "salesd_name": "", "items_name": "Gold Ring"},
    {"salesd_weight": 5.0, "salesd_stonewgt": 0.0, "salesd_rate": 5000,
     "salesd_mcharge": 100, "salesd_wastage": 0.2, "salesd_amount": 25100,
     "salesd_name": "Chain", "items_name": "Gold Chain"},
]


def ev(expression, row=None, rows=None, context=None):
    return evaluate(expression, row if row is not None else ROWS[0],
                    rows if rows is not None else ROWS, context)


# --- arithmetic ------------------------------------------------------------

def test_columns_and_arithmetic():
    assert ev(" salesd_weight  -  salesd_stonewgt ") == 10.0
    assert ev("(  salesd_wastage  *  salesd_rate  )  +  salesd_mcharge ") == 4300.0
    assert ev("salesd_rate / 2") == 2500.0
    assert ev("2 ^ 3") == 8.0


def test_division_by_zero_is_zero_not_a_crash():
    assert ev("salesd_rate / 0") == 0.0


def test_unary_minus_and_precedence():
    assert ev("-salesd_mcharge") == -300.0
    assert ev("1 + 2 * 3") == 7
    assert ev("(1 + 2) * 3") == 9


def test_missing_column_is_null():
    assert ev("nosuchcolumn") is None
    assert ev("if(isnull(nosuchcolumn), 1, 2)") == 1


def test_column_is_found_by_its_short_name():
    assert evaluate("weight", {"salesd_weight": 3.5}, []) == 3.5


# --- strings and conditions ------------------------------------------------

def test_string_concatenation_and_comparison():
    assert ev("'Bill ' + 'No'") == "Bill No"
    assert ev("if( salesd_name = '' , items_name, salesd_name)") == "Gold Ring"
    assert ev("if( salesd_name = '' , items_name, salesd_name)", ROWS[1]) == "Chain"


def test_boolean_operators():
    assert ev("salesd_weight > 10 and salesd_rate = 5000") is True
    assert ev("salesd_weight > 100 or salesd_rate = 5000") is True
    assert ev("not (salesd_weight > 100)") is True


def test_case_expression():
    row = {"status": 3}
    assert evaluate("case(status when 1 then 'new' when 3 then 'done' "
                    "else 'other')", row, [row]) == "done"
    assert evaluate("case(status when 9 then 'x' else 'other')", row, [row]) \
        == "other"


# --- aggregates ------------------------------------------------------------

def test_aggregates_run_over_all_the_rows():
    assert ev("sum(salesd_amount for all)") == 77100.0
    assert ev("count(salesd_weight for all)") == 2
    assert ev("max(salesd_weight for all)") == 10.5
    assert ev("min(salesd_weight for all)") == 5.0
    assert ev("avg(salesd_rate for all)") == 5000.0


def test_aggregate_of_an_expression():
    assert ev("sum(salesd_weight - salesd_stonewgt for all)") == 15.0


def test_group_aggregates_are_accepted():
    assert ev("sum(salesd_amount for group 1)") == 77100.0


# --- functions -------------------------------------------------------------

def test_number_and_text_functions():
    assert ev("round(salesd_weight * salesd_rate, 2)") == 52500.0
    assert ev("abs(0 - salesd_mcharge)") == 300.0
    assert ev("int(10.9)") == 10
    assert ev("len('Jewellery')") == 9
    assert ev("left('Jewellery', 4)") == "Jewe"
    assert ev("right('Jewellery', 4)") == "lery"
    assert ev("mid('Jewellery', 2, 3)") == "ewe"
    assert ev("upper('gold') + lower('RING')") == "GOLDring"
    assert ev("trim('  x  ')") == "x"
    assert ev("pos('Jewellery','well')") == 3


def test_string_applies_a_format_mask():
    assert ev("string(salesd_weight, '#####0.000')") == "10.500"
    assert ev("'SGST ('+string( 3 ,'#0.#')+ '%)'") == "SGST (3%)"


def test_today_and_page():
    assert ev("today()") == datetime.date.today().isoformat()
    assert ev("'Page ' + page() + ' of ' + pageCount()",
              context={"page": 2, "pagecount": 5}) == "Page 2 of 5"


def test_profilestring_reads_the_settings_given_to_it():
    assert ev("profilestring('gmine.ini','Company','Name','')",
              context={"settings": {"Name": "Super Gold"}}) == "Super Gold"
    assert ev("profilestring('gmine.ini','Company','Name','none')") == "none"


def test_previous_row_reference():
    rows = [{"slno": 1, "amt": 10}, {"slno": 1, "amt": 20}]
    assert evaluate("if(slno[-1] = slno, 0, amt)", rows[1], rows,
                    {"row_index": 1}) == 0
    assert evaluate("if(slno[-1] = slno, 0, amt)", rows[0], rows,
                    {"row_index": 0}) == 10


# --- robustness ------------------------------------------------------------

def test_comments_and_escapes_are_handled():
    assert evaluate("/* a note */ 1 + 1", {}, []) == 2
    assert evaluate("string( 1 ,~\"#0~\")", {}, []) == "1"


def test_nonsense_returns_none_rather_than_raising():
    assert evaluate("if(", {}, []) is None
    assert evaluate("", {}, []) is None
    assert evaluate(") )", {}, []) is None


def test_tokenizer_rejects_stray_characters():
    with pytest.raises(ExpressionError):
        tokenize("1 $ 2")


# --- the expressions actually shipped --------------------------------------

def test_the_shipped_expressions_parse():
    """Almost every calculation in the build must be understood."""
    from app.reports import layouts
    if not layouts.available(ROOT):
        pytest.skip("no printed forms in this tree")
    total = failed = 0
    for name in layouts.names(ROOT)[:120]:
        layout = layouts.load(name, ROOT)
        for obj in layout.objects:
            if obj.kind != "compute" or not obj.expression.strip():
                continue
            total += 1
            try:
                tokenize(obj.expression)
            except ExpressionError:
                failed += 1
    assert total > 200
    assert failed / total < 0.05
