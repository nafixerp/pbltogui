"""Stock Adjustment — w_stockadj.

Generated from the PowerBuilder window ``w_stockadj.srw`` by
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
    name='w_stockadj',
    title='Stock Adjustment',
    width=3657,
    height=2236,
    controls=[],
    tables=['items', 'itemsstk', 'itemadj', 'generali'],
    source_path='w_stockadj.srw',
    grid={'control': 'dw_1', 'dataobject': 'd_stockadj', 'table': 'items', 'keys': ['code'], 'columns': [{'name': 'name', 'label': 'Item Name', 'type': 'char'}, {'name': 'code', 'label': 'Code', 'type': 'char'}, {'name': 'curqty', 'label': 'curqty', 'type': 'long'}, {'name': 'curwgt', 'label': 'curwgt', 'type': 'decimal'}, {'name': 'qty', 'label': 'qty', 'type': 'long'}, {'name': 'weight', 'label': 'weight', 'type': 'decimal'}, {'name': 'stonewgt', 'label': 'stonewgt', 'type': 'decimal'}, {'name': 'qtyb', 'label': 'qtyb', 'type': 'long'}, {'name': 'weightb', 'label': 'weightb', 'type': 'decimal'}, {'name': 'stonewgtb', 'label': 'stonewgtb', 'type': 'decimal'}, {'name': 'cost', 'label': 'cost', 'type': 'decimal'}, {'name': 'grpcode', 'label': 'grpcode', 'type': 'char'}, {'name': 'itype', 'label': 'itype', 'type': 'char'}, {'name': 'ornament', 'label': 'ornament', 'type': 'char'}, {'name': 'curstwgt', 'label': 'curstwgt', 'type': 'decimal'}, {'name': 'compqtya', 'label': 'compqtya', 'type': 'long'}, {'name': 'compqtyb', 'label': 'compqtyb', 'type': 'long'}, {'name': 'compwgta', 'label': 'compwgta', 'type': 'decimal'}, {'name': 'compwgtb', 'label': 'compwgtb', 'type': 'decimal'}, {'name': 'compstwgta', 'label': 'compstwgta', 'type': 'decimal'}, {'name': 'compstwgtb', 'label': 'compstwgtb', 'type': 'decimal'}]},
    report={'dataobject': 'd_stockadj', 'sql': 'SELECT items.name AS items_name, items.code AS items_code, items.qty AS items_qty, items.weight AS items_weight, items.stonewgt AS items_stonewgt, items.qtyb AS items_qtyb, items.weightb AS items_weightb, items.stonewgtb AS items_stonewgtb, items.cost AS items_cost, items.grpcode AS items_grpcode, items.itype AS items_itype, items.ornament AS items_ornament, (qty) as curqty, (weight) as curwgt, (stonewgt) as curstwgt, (ifnull( :rstktype, qty, (select sum(itemsstk.qty) from itemsstk where itemsstk.code = items.code and itemsstk.stktype = :rstktype))) as compqtya, (ifnull( :rstktype, qtyb, (select sum(itemsstk.qty) from itemsstk where itemsstk.code = items.code and itemsstk.stktype = :rstktype))) as compqtyb, (ifnull( :rstktype, weight, (select sum(itemsstk.weight) from itemsstk where itemsstk.code = items.code and itemsstk.stktype = :rstktype))) as compwgta, (ifnull( :rstktype, weightb, (select sum(itemsstk.weightb) from itemsstk where itemsstk.code = items.code and itemsstk.stktype = :rstktype))) as compwgtb, (ifnull( :rstktype,stonewgt , (select sum(itemsstk.stonewgt) from itemsstk where itemsstk.code = items.code and itemsstk.stktype = :rstktype))) as compstwgta, (ifnull( :rstktype,stonewgtb , (select sum(itemsstk.stonewgtb) from itemsstk where itemsstk.code = items.code and itemsstk.stktype = :rstktype))) as compstwgtb FROM items ORDER BY items.name ASC', 'args': ['rlevel', 'rstktype'], 'arg_types': {'rlevel': 'number', 'rstktype': 'string'}, 'tables': ['items'], 'columns': [{'name': 'name', 'label': 'Item Name', 'type': 'char'}, {'name': 'code', 'label': 'Code', 'type': 'char'}, {'name': 'curqty', 'label': 'curqty', 'type': 'long'}, {'name': 'curwgt', 'label': 'curwgt', 'type': 'decimal'}, {'name': 'qty', 'label': 'qty', 'type': 'long'}, {'name': 'weight', 'label': 'weight', 'type': 'decimal'}, {'name': 'stonewgt', 'label': 'stonewgt', 'type': 'decimal'}, {'name': 'qtyb', 'label': 'qtyb', 'type': 'long'}, {'name': 'weightb', 'label': 'weightb', 'type': 'decimal'}, {'name': 'stonewgtb', 'label': 'stonewgtb', 'type': 'decimal'}, {'name': 'cost', 'label': 'cost', 'type': 'decimal'}, {'name': 'grpcode', 'label': 'grpcode', 'type': 'char'}, {'name': 'itype', 'label': 'itype', 'type': 'char'}, {'name': 'ornament', 'label': 'ornament', 'type': 'char'}, {'name': 'curstwgt', 'label': 'curstwgt', 'type': 'decimal'}, {'name': 'compqtya', 'label': 'compqtya', 'type': 'long'}, {'name': 'compqtyb', 'label': 'compqtyb', 'type': 'long'}, {'name': 'compwgta', 'label': 'compwgta', 'type': 'decimal'}, {'name': 'compwgtb', 'label': 'compwgtb', 'type': 'decimal'}, {'name': 'compstwgta', 'label': 'compstwgta', 'type': 'decimal'}, {'name': 'compstwgtb', 'label': 'compstwgtb', 'type': 'decimal'}]},
    opens=['w_stocklist_popup', 'w_itemhistory'],
)


class StockAdjustmentForm(GeneratedForm):
    """Stock Adjustment"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('datawindow', 'dw_stktype', 352, 0, 539, 88, dataobject='d_stktypecode', taborder=10)
        self.add('datawindow', 'dw_grp', 1289, 0, 800, 88, dataobject='d_itemgrpcode', taborder=20)
        self.add('statictext', 'st_2', 37, 8, 302, 76, text='Stk Type :')
        self.add('statictext', 'st_grp', 1024, 8, 247, 76, text='Group :')
        self.add('commandbutton', 'cb_fillcompstk', 2162, 8, 613, 108, text='&Fill With Comp Stock', taborder=70)
        self.add('commandbutton', 'cb_3', 2798, 12, 279, 100, text='Save &As', taborder=100)
        self.add('commandbutton', 'cb_1', 3081, 12, 265, 100, text='&Print', taborder=110)
        self.add('commandbutton', 'cb_2', 3351, 12, 265, 100, text='E&xit', taborder=90)
        self.add('dropdownlistbox', 'ddlb_type2', 352, 116, 603, 556, text='All', items=['All', 'Gold', 'Silver', 'Others'], taborder=30)
        self.add('datawindow', 'dw_smcode', 1289, 116, 677, 88, dataobject='d_smancode', taborder=40)
        self.add('statictext', 'st_1', 0, 128, 338, 76, text='Item Type :')
        self.add('statictext', 'st_3', 1024, 128, 247, 76, text='SMan :')
        self.add('commandbutton', 'cb_update', 2162, 128, 613, 108, text='&Update Stock', taborder=60)
        self.add('checkbox', 'cbx_speed', 3077, 144, 425, 76, text='Speed Print')
        self.add('datawindow', 'dw_1', 0, 236, 3621, 1884, dataobject='d_stockadj', taborder=80)
        self.add('dropdownlistbox', 'ddlb_type', 2171, 240, 603, 556, text='All', items=['All', 'Ornaments Only', 'Not Ornaments'], taborder=50)
