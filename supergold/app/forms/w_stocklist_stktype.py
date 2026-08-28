"""Stock Type Wise — w_stocklist_stktype.

Generated from the PowerBuilder window ``w_stocklist_stktype.srw`` by
``tools/generate_forms.py``. It is ordinary PySide6 code: the controls below
are the original ones, at their original positions. Behaviour (record editing,
the data view over this window's own query, search and export) comes from
:class:`app.ui.form_base.GeneratedForm`.

Re-running the generator overwrites this file. Put hand-written business logic
in ``app/modules/`` instead — a module registered there takes precedence.
"""

from app.pb_parser import Window
from app.ui.form_base import GeneratedForm

WINDOW = Window(
    name='w_stocklist_stktype',
    title='Stock Type Wise',
    width=3621,
    height=2252,
    controls=[],
    tables=['userd'],
    source_path='w_stocklist_stktype.srw',
    grid={'control': 'dw_1', 'dataobject': 'd_stocklistreport_stktype', 'table': 'items', 'keys': ['code'], 'columns': [{'name': 'name', 'label': 'Item Name', 'type': 'char'}, {'name': 'code', 'label': 'Code', 'type': 'char'}, {'name': 'regionalname', 'label': 'regionalname', 'type': 'char'}, {'name': 'itype', 'label': 'itype', 'type': 'char'}, {'name': 'ornament', 'label': 'ornament', 'type': 'char'}, {'name': 'cost', 'label': 'cost', 'type': 'decimal'}, {'name': 'grpcode', 'label': 'grpcode', 'type': 'char'}, {'name': 'qty', 'label': 'qty', 'type': 'long'}, {'name': 'weight', 'label': 'weight', 'type': 'decimal'}, {'name': 'stonewgt', 'label': 'St.Wgt.', 'type': 'decimal'}, {'name': 'qtyb', 'label': 'qtyb', 'type': 'long'}, {'name': 'weightb', 'label': 'weightb', 'type': 'decimal'}, {'name': 'stonewgtb', 'label': 'stonewgtb', 'type': 'decimal'}]},
    report={'dataobject': 'd_stocklistreport_stktype', 'sql': 'SELECT items.name AS items_name, items.code AS items_code, items.regionalname AS items_regionalname, items.itype AS items_itype, items.ornament AS items_ornament, items.cost AS items_cost, items.grpcode AS items_grpcode, (select sum(itemsstk.qty) from itemsstk where itemsstk.code = items.code and itemsstk.stktype = ifnull(:rtype,itemsstk.stktype,:rtype)) as qty, (select sum(itemsstk.weight) from itemsstk where itemsstk.code = items.code and itemsstk.stktype = ifnull(:rtype,itemsstk.stktype,:rtype)) as weight, (select sum(itemsstk.stonewgt) from itemsstk where itemsstk.code = items.code and itemsstk.stktype = ifnull(:rtype,itemsstk.stktype,:rtype)) as stonewgt, (select sum(itemsstk.qtyb) from itemsstk where itemsstk.code = items.code and itemsstk.stktype = ifnull(:rtype,itemsstk.stktype,:rtype)) as qtyb, (select sum(itemsstk.weightb) from itemsstk where itemsstk.code = items.code and itemsstk.stktype = ifnull(:rtype,itemsstk.stktype,:rtype)) as weightb, (select sum(itemsstk.stonewgtb) from itemsstk where itemsstk.code = items.code and itemsstk.stktype = ifnull(:rtype,itemsstk.stktype,:rtype)) as stonewgtb FROM items ORDER BY items.name ASC', 'args': ['rlevel', 'rtype'], 'arg_types': {'rlevel': 'number', 'rtype': 'string'}, 'tables': ['items'], 'columns': [{'name': 'name', 'label': 'Item Name', 'type': 'char'}, {'name': 'code', 'label': 'Code', 'type': 'char'}, {'name': 'regionalname', 'label': 'regionalname', 'type': 'char'}, {'name': 'itype', 'label': 'itype', 'type': 'char'}, {'name': 'ornament', 'label': 'ornament', 'type': 'char'}, {'name': 'cost', 'label': 'cost', 'type': 'decimal'}, {'name': 'grpcode', 'label': 'grpcode', 'type': 'char'}, {'name': 'qty', 'label': 'qty', 'type': 'long'}, {'name': 'weight', 'label': 'weight', 'type': 'decimal'}, {'name': 'stonewgt', 'label': 'St.Wgt.', 'type': 'decimal'}, {'name': 'qtyb', 'label': 'qtyb', 'type': 'long'}, {'name': 'weightb', 'label': 'weightb', 'type': 'decimal'}, {'name': 'stonewgtb', 'label': 'stonewgtb', 'type': 'decimal'}]},
)


class StockTypeWiseForm(GeneratedForm):
    """Stock Type Wise"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('checkbox', 'cbx_nowgt', 2080, 0, 329, 76, text='No Wgt')
        self.add('commandbutton', 'cb_3', 2775, 0, 279, 100, text='Save &As', taborder=70)
        self.add('commandbutton', 'cb_1', 3058, 0, 265, 100, text='&Print', taborder=80)
        self.add('commandbutton', 'cb_2', 3328, 0, 265, 100, text='E&xit', taborder=40)
        self.add('dropdownlistbox', 'ddlb_type2', 1440, 4, 603, 556, text='All', items=['All', 'Gold', 'Platinum', 'Silver', 'Others'], taborder=60)
        self.add('checkbox', 'cbx_nototal', 2427, 4, 325, 76, text='No Total')
        self.add('datawindow', 'dw_stktype', 384, 8, 549, 92, dataobject='d_stktypecode', taborder=10)
        self.add('commandbutton', 'cb_show', 978, 8, 224, 92, text='&Show', taborder=11)
        self.add('statictext', 'st_1', 1207, 12, 215, 76, text='Type :')
        self.add('statictext', 'st_grp', 0, 20, 370, 76, text='Stock Type :')
        self.add('dropdownlistbox', 'ddlb_type', 1440, 100, 603, 556, text='All', items=['All', 'Ornaments Only', 'Not Ornaments'], taborder=50)
        self.add('dropdownlistbox', 'ddlb_type3', 384, 104, 814, 556, text='With Not Zero Stock', items=['All', 'With Stock Only', 'With -ve Stock', 'With Zero Stock', 'With Not Zero Stock'], taborder=30)
        self.add('checkbox', 'cbx_stkverify', 2085, 104, 430, 72, text='Stock Verify')
        self.add('checkbox', 'cbx_full', 2770, 112, 247, 76, text='Full')
        self.add('checkbox', 'cbx_speed', 3127, 112, 425, 76, text='Speed Print')
        self.add('datawindow', 'dw_1', 0, 200, 3579, 1952, dataobject='d_stocklistreport_stktype', taborder=20)
