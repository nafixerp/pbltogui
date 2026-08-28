"""Item Rate Report — w_itemrate_report.

Generated from the PowerBuilder window ``w_itemrate_report.srw`` by
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
    name='w_itemrate_report',
    title='Item Rate Report',
    width=3639,
    height=2412,
    controls=[],
    tables=[],
    source_path='w_itemrate_report.srw',
    grid={'control': 'dw_1', 'dataobject': 'd_itemrate_report', 'table': 'items', 'keys': ['code'], 'columns': [{'name': 'name', 'label': 'Item Name', 'type': 'char'}, {'name': 'code', 'label': 'Code', 'type': 'char'}, {'name': 'regionalname', 'label': 'regionalname', 'type': 'char'}, {'name': 'itype', 'label': 'itype', 'type': 'char'}, {'name': 'ornament', 'label': 'ornament', 'type': 'char'}, {'name': 'grpcode', 'label': 'grpcode', 'type': 'char'}, {'name': 'crate', 'label': 'crate', 'type': 'decimal'}, {'name': 'rate', 'label': 'rate', 'type': 'decimal'}, {'name': 'wsrate', 'label': 'wsrate', 'type': 'decimal'}, {'name': 'qty', 'label': 'qty', 'type': 'long'}, {'name': 'weight', 'label': 'weight', 'type': 'decimal'}, {'name': 'stonewgt', 'label': 'stonewgt', 'type': 'decimal'}, {'name': 'qtyb', 'label': 'qtyb', 'type': 'long'}, {'name': 'weightb', 'label': 'weightb', 'type': 'decimal'}, {'name': 'stonewgtb', 'label': 'stonewgtb', 'type': 'decimal'}, {'name': 'stkinnos', 'label': 'stkinnos', 'type': 'char'}]},
    report={'dataobject': 'd_itemrate_report', 'sql': 'SELECT items.name AS items_name, items.code AS items_code, items.regionalname AS items_regionalname, items.itype AS items_itype, items.ornament AS items_ornament, items.grpcode AS items_grpcode, items.crate AS items_crate, items.rate AS items_rate, items.wsrate AS items_wsrate, items.qty AS items_qty, items.weight AS items_weight, items.stonewgt AS items_stonewgt, items.qtyb AS items_qtyb, items.weightb AS items_weightb, items.stonewgtb AS items_stonewgtb, items.stkinnos AS items_stkinnos FROM items ORDER BY items.name ASC', 'args': ['rlevel', 'rval'], 'arg_types': {'rlevel': 'number', 'rval': 'string'}, 'tables': ['items'], 'columns': [{'name': 'name', 'label': 'Item Name', 'type': 'char'}, {'name': 'code', 'label': 'Code', 'type': 'char'}, {'name': 'regionalname', 'label': 'regionalname', 'type': 'char'}, {'name': 'itype', 'label': 'itype', 'type': 'char'}, {'name': 'ornament', 'label': 'ornament', 'type': 'char'}, {'name': 'grpcode', 'label': 'grpcode', 'type': 'char'}, {'name': 'crate', 'label': 'crate', 'type': 'decimal'}, {'name': 'rate', 'label': 'rate', 'type': 'decimal'}, {'name': 'wsrate', 'label': 'wsrate', 'type': 'decimal'}, {'name': 'qty', 'label': 'qty', 'type': 'long'}, {'name': 'weight', 'label': 'weight', 'type': 'decimal'}, {'name': 'stonewgt', 'label': 'stonewgt', 'type': 'decimal'}, {'name': 'qtyb', 'label': 'qtyb', 'type': 'long'}, {'name': 'weightb', 'label': 'weightb', 'type': 'decimal'}, {'name': 'stonewgtb', 'label': 'stonewgtb', 'type': 'decimal'}, {'name': 'stkinnos', 'label': 'stkinnos', 'type': 'char'}]},
    opens=['w_stocklist_popup', 'w_itemhistory', 'w_item'],
)


class ItemRateReportForm(GeneratedForm):
    """Item Rate Report"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('dropdownlistbox', 'ddlb_type2', 1440, 0, 603, 556, text='All', items=['All', 'Gold', 'Platinum', 'Silver', 'Others'], taborder=40)
        self.add('commandbutton', 'cb_3', 2775, 0, 279, 100, text='Save &As', taborder=60)
        self.add('commandbutton', 'cb_1', 3058, 0, 265, 100, text='&Print', taborder=70)
        self.add('commandbutton', 'cb_2', 3328, 0, 265, 100, text='E&xit', taborder=20)
        self.add('checkbox', 'cbx_sortoncode', 2176, 4, 434, 72, text='Sort On Code')
        self.add('datawindow', 'dw_grp', 261, 8, 800, 88, dataobject='d_itemgrpcode', taborder=50)
        self.add('statictext', 'st_1', 1207, 8, 215, 76, text='Type :')
        self.add('statictext', 'st_grp', 0, 12, 247, 76, text='Group :')
        self.add('checkbox', 'cbx_grp', 1070, 16, 78, 76)
        self.add('dropdownlistbox', 'ddlb_type', 1440, 96, 603, 556, text='All', items=['All', 'Ornaments Only', 'Not Ornaments'], taborder=30)
        self.add('datawindow', 'dw_1', 0, 192, 3579, 1952, dataobject='d_itemrate_report', taborder=10)
