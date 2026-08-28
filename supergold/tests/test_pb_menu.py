"""Tests for the PowerBuilder menu-object parser (m_mainmenu.srm)."""

import os
import sys

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from app import menu_loader, pb_menu, pb_parser  # noqa: E402

SRM = os.path.join(ROOT, "gminestr", "m_mainmenu.srm")

SAMPLE = '''forward
global type m_demo from menu
end type
type m_file from menu within m_demo
end type
end forward

global type m_demo from menu
m_file m_file
end type

on m_demo.create
this.m_file=create m_file
this.Item[UpperBound(this.Item)+1]=this.m_file
end on

type m_file from menu within m_demo
m_open m_open
m_sep m_sep
m_hidden m_hidden
m_noop m_noop
end type

on m_file.create
this.text = "&File"
this.Item[UpperBound(this.Item)+1]=this.m_open
this.Item[UpperBound(this.Item)+1]=this.m_sep
this.Item[UpperBound(this.Item)+1]=this.m_hidden
this.Item[UpperBound(this.Item)+1]=this.m_noop
end on

type m_open from menu within m_file
end type

event clicked;
if iuserctrl = 0 then
\topensheet(child,"w_sales",w_main,1,layered!)
else
\tchkmenuaccess(this)
end if
end event

on m_open.create
this.text = "&Bill~tCtrl+G"
this.shortcut = 327
end on

type m_sep from menu within m_file
end type

on m_sep.create
end on

type m_hidden from menu within m_file
end type

on m_hidden.create
this.visible = false
this.text = "Hidden"
end on

type m_noop from menu within m_file
end type

event clicked;printsetup()
end event

on m_noop.create
this.text = "&Printer Setup"
end on
'''


@pytest.fixture()
def sample_srm(tmp_path):
    path = tmp_path / "m_demo.srm"
    path.write_bytes(SAMPLE.encode("utf-16"))
    return str(path)


def test_parses_hierarchy_and_captions(sample_srm):
    items = pb_menu.parse_menu_source(sample_srm)
    assert items["m_file"].label == "File"
    assert items["m_file"].parent == "m_demo"
    assert items["m_file"].order == ["m_open", "m_sep", "m_hidden", "m_noop"]
    assert items["m_open"].label == "Bill"


def test_shortcut_from_caption_and_code(sample_srm):
    items = pb_menu.parse_menu_source(sample_srm)
    assert items["m_open"].shortcut == "Ctrl+G"
    # The numeric form decodes to the same accelerator.
    assert pb_menu._decode_shortcut(327) == "Ctrl+G"
    assert pb_menu._decode_shortcut(113) == "F2"
    assert pb_menu._decode_shortcut(1369) == "Ctrl+Shift+Y"


def test_target_window_from_clicked_script(sample_srm):
    items = pb_menu.parse_menu_source(sample_srm)
    assert items["m_open"].windows == ["w_sales"]
    assert items["m_noop"].windows == []


MENUCASCADE = '''forward
global type m_demo from menu
end type
end forward

global type m_demo from menu
m_trans m_trans
end type

on m_demo.create
this.Item[UpperBound(this.Item)+1]=this.m_trans
end on

type m_trans from menu within m_demo
m_new m_new
end type

on m_trans.create
this.text = "Diamonds/Pres.Stone Bill"
this.Item[UpperBound(this.Item)+1]=this.m_new
end on

type m_new from menucascade within m_trans
end type

event clicked;
open(w_diamond_purchase)
end event

on m_new.create
this.text = "New"
end on
'''


def test_menucascade_items_are_parsed(tmp_path):
    path = tmp_path / "m_casc.srm"
    path.write_bytes(MENUCASCADE.encode("utf-16"))
    sections = pb_menu.load_menu(str(path))
    assert [s.label for s in sections] == ["Diamonds/Pres.Stone Bill"]
    leaf = sections[0].children[0]
    assert (leaf.label, leaf.window) == ("New", "w_diamond_purchase")


def test_frame_windows_are_not_targets():
    assert pb_menu._targets("open(w_whait)\nw_main.setfocus()\n") == []


def test_preference_picks_a_converted_module(tmp_path):
    src = SAMPLE.replace('opensheet(child,"w_sales",w_main,1,layered!)',
                         'open(w_sales_full)\n\topensheet(child,"w_sales",w_main,1,layered!)')
    path = tmp_path / "m_pref.srm"
    path.write_bytes(src.encode("utf-16"))
    default = pb_menu.load_menu(str(path))[0].children[0]
    assert default.window == "w_sales_full"
    assert default.alternates == ["w_sales", "w_sales_full"] or "w_sales" in default.alternates
    preferred = pb_menu.load_menu(str(path), prefer={"w_sales"})[0].children[0]
    assert preferred.window == "w_sales"


def test_local_variable_target():
    script = 'w_taxreport wtmp\n\nopenwithparm(wtmp,"OS")\n'
    assert pb_menu._targets(script) == ["w_taxreport"]


def test_tree_drops_separators_and_hidden_items(sample_srm):
    sections = pb_menu.load_menu(sample_srm, source_refs={"w_sales": "gminet1\\w_sales.srw"})
    assert [s.label for s in sections] == ["File"]
    labels = [c.label for c in sections[0].children]
    assert labels == ["Bill", "Printer Setup"]      # separator and hidden dropped
    bill = sections[0].children[0]
    assert (bill.window, bill.shortcut) == ("w_sales", "Ctrl+G")
    assert bill.source_ref == "gminet1\\w_sales.srw"
    # An item whose script opens nothing stays visible but carries no window.
    assert sections[0].children[1].window is None


# --- the real menu object shipped with the export --------------------------

@pytest.mark.skipif(not os.path.exists(SRM), reason="menu object not in export")
def test_real_menu_object():
    refs = menu_loader.source_ref_index(os.path.join(ROOT, "project_tree.txt"))
    sections = pb_menu.load_menu(SRM, source_refs=refs, prefer={"w_purchase"})
    assert [s.label for s in sections] == [
        "File", "Master", "Transactions", "Reports", "Utilities", "Help"]

    leaves = list(menu_loader.iter_leaves(sections))
    # The menu object covers at least everything the maintained map lists.
    old = list(menu_loader.iter_leaves(
        menu_loader.load_menu(os.path.join(ROOT, "project_tree.txt"))))
    assert len(leaves) >= len(old)

    windows = {leaf.window for leaf in leaves}
    for expected in ("w_sales", "w_purchase", "w_rcpt", "w_item", "w_acledger"):
        assert expected in windows


@pytest.mark.skipif(not os.path.exists(SRM), reason="menu object not in export")
def test_every_leaf_resolves_to_a_source_file():
    sections = pb_menu.load_menu(SRM)
    unresolved = [leaf.label for leaf in menu_loader.iter_leaves(sections)
                  if pb_parser.find_source(leaf.source_ref, ROOT) is None]
    assert unresolved == []
