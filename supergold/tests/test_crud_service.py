"""CRUD engine behind the generic screens: mapping, statements, round trips."""

import os
import sys

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

import db  # noqa: E402
from app.services import crud_service as cs  # noqa: E402


@pytest.fixture()
def party_table(tmp_path, monkeypatch):
    """A throwaway SQLite database with a keyed and an unkeyed table."""
    monkeypatch.setattr(db, "ENGINE", "sqlite")
    monkeypatch.setattr(db, "SQLITE_PATH", str(tmp_path / "crud.db"))
    db.execute("""CREATE TABLE party (
        party_id INTEGER PRIMARY KEY AUTOINCREMENT,
        code TEXT, name TEXT, balance REAL, active INTEGER)""")
    db.execute("""CREATE TABLE flat (code TEXT, name TEXT)""")
    return "party"


def mapping_for(table, controls):
    return cs.build_mapping(table, controls)


# --- mapping ---------------------------------------------------------------

def test_maps_controls_onto_real_columns(party_table):
    m = mapping_for("party", ["sle_code", "sle_name", "em_balance",
                              "cbx_active", "sle_unknown"])
    assert m.fields == {"sle_code": "code", "sle_name": "name",
                        "em_balance": "balance", "cbx_active": "active"}
    assert m.unmapped == ["sle_unknown"]
    assert m.pk == ["party_id"] and m.autoinc == {"party_id"}
    assert m.writable


def test_unknown_table_is_not_writable():
    m = mapping_for("no_such_table", ["sle_code"])
    assert not m.writable and "not in the current database" in m.describe()


def test_alias_matching(party_table):
    m = mapping_for("party", ["sle_partycode"])
    assert m.fields == {"sle_partycode": "code"}


def test_one_column_is_claimed_once(party_table):
    m = mapping_for("party", ["sle_code", "sle_partycode"])
    assert list(m.fields.values()) == ["code"]
    assert m.unmapped == ["sle_partycode"]


# --- value handling --------------------------------------------------------

def test_numeric_and_blank_coercion(party_table):
    m = mapping_for("party", ["sle_balance"])
    assert cs.coerce("1,250.50", m.column("balance")) == 1250.5
    assert cs.coerce("  ", m.column("balance")) is None
    assert cs.coerce(True, m.column("active")) == 1
    with pytest.raises(ValueError):
        cs.coerce("abc", m.column("balance"))


def test_identity_column_dropped_on_insert(party_table):
    m = mapping_for("party", ["sle_party_id", "sle_code"])
    values = cs.prepare_values(m, {"sle_party_id": "9", "sle_code": "A1"},
                               for_insert=True)
    assert values == {"code": "A1"}
    values = cs.prepare_values(m, {"sle_party_id": "9", "sle_code": "A1"},
                               for_insert=False)
    assert values == {"party_id": 9, "code": "A1"}


# --- statements ------------------------------------------------------------

def test_insert_update_delete_round_trip(party_table):
    m = mapping_for("party", ["sle_code", "sle_name", "em_balance"])
    cs.insert(m, cs.prepare_values(
        m, {"sle_code": "C1", "sle_name": "Ravi", "em_balance": "500"},
        for_insert=True))
    rows = cs.select_rows(m)
    assert len(rows) == 1 and rows[0]["name"] == "Ravi" and rows[0]["balance"] == 500

    key = cs.key_for_row(m, rows[0])
    assert key == {"party_id": rows[0]["party_id"]}
    assert cs.count_matching(m, key) == 1

    cs.update(m, {"name": "Ravi Kumar", "balance": 750}, key)
    assert cs.select_rows(m)[0]["name"] == "Ravi Kumar"

    cs.delete(m, key)
    assert cs.select_rows(m) == []


def test_table_without_primary_key_is_matched_on_all_values(party_table):
    m = mapping_for("flat", ["sle_code", "sle_name"])
    assert m.pk == []
    for _ in range(2):
        cs.insert(m, {"code": "X", "name": "Same"})
    rows = cs.select_rows(m)
    key = cs.key_for_row(m, rows[0])
    assert key == {"code": "X", "name": "Same"}
    # The caller is told both rows match before it writes anything.
    assert cs.count_matching(m, key) == 2
    cs.delete(m, key)
    assert cs.select_rows(m) == []


def test_search_filters_text_columns(party_table):
    m = mapping_for("party", ["sle_code", "sle_name"])
    cs.insert(m, {"code": "A", "name": "Anil"})
    cs.insert(m, {"code": "B", "name": "Biju"})
    assert [r["name"] for r in cs.select_rows(m, search="anil")] == ["Anil"]
    assert len(cs.select_rows(m, search="")) == 2


def test_null_values_use_is_null_in_the_key(party_table):
    m = mapping_for("flat", ["sle_code", "sle_name"])
    cs.insert(m, {"code": "K", "name": None})
    row = cs.select_rows(m)[0]
    assert cs.count_matching(m, cs.key_for_row(m, row)) == 1


# --- safety ----------------------------------------------------------------

def test_columns_not_in_the_table_are_rejected(party_table):
    m = mapping_for("party", ["sle_code"])
    with pytest.raises(ValueError):
        cs.insert(m, {"code": "A", "dropped); DROP TABLE party;--": 1})
    with pytest.raises(ValueError):
        cs.update(m, {"nope": 1}, {"party_id": 1})


def test_empty_statements_are_refused(party_table):
    m = mapping_for("party", ["sle_code"])
    with pytest.raises(ValueError):
        cs.insert(m, {})
    with pytest.raises(ValueError):
        cs.update(m, {"code": "A"}, {})
    with pytest.raises(ValueError):
        cs.delete(m, {})


# --- manual corrections ----------------------------------------------------

def test_field_map_override(party_table, tmp_path, monkeypatch):
    import json
    data = tmp_path / "data"
    data.mkdir()
    (data / "field_map.json").write_text(json.dumps({
        "w_demo": {"table": "party", "fields": {"sle_xyz": "name"}}}))
    monkeypatch.setattr(cs, "BASE_DIR", str(tmp_path))
    cs._overrides.cache_clear()

    m = cs.build_mapping("wrong_table", ["sle_xyz", "sle_code"], window="w_demo")
    assert m.table == "party"                       # table redirected
    assert m.fields["sle_xyz"] == "name"            # field pinned by hand
    assert m.fields["sle_code"] == "code"           # automatic matching still runs
    cs._overrides.cache_clear()


def test_missing_field_map_is_fine(party_table, tmp_path, monkeypatch):
    monkeypatch.setattr(cs, "BASE_DIR", str(tmp_path))
    cs._overrides.cache_clear()
    m = cs.build_mapping("party", ["sle_code"], window="w_demo")
    assert m.fields == {"sle_code": "code"}
    cs._overrides.cache_clear()
