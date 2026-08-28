"""Item History — w_itemhistory.

Generated from the PowerBuilder window ``w_itemhistory.srw`` by
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
    name='w_itemhistory',
    title='Item History',
    width=3657,
    height=2284,
    controls=[],
    tables=['refineryd', 'smithd', 'itemadj', 'repaird', 'purchased', 'refinerym', 'clients', 'items', 'purchaserd', 'salesrd', 'orderdga', 'salesd', 'smithm', 'repairm', 'purchasem', 'purchaserm', 'salesm', 'salesrm', 'orderm', 'date', 'userd'],
    source_path='w_itemhistory.srw',
    grid={'control': 'dw_history', 'dataobject': 'd_itemhistory', 'table': 'items', 'keys': ['code'], 'computes': [{'name': 'compute_6', 'expression': 'rClQty', 'format': '#####0', 'label': 'compute_6', 'band': 'summary'}, {'name': 'opstkqty', 'expression': 'rOpqty', 'format': '###0', 'label': 'opstkqty', 'band': 'detail'}, {'name': 'clweight', 'expression': 'rClWgt', 'format': '######0.000', 'label': 'clweight', 'band': 'summary'}, {'name': 'compute_7', 'expression': ' rClStwgt ', 'format': '######0.000', 'label': 'compute_7', 'band': 'summary'}, {'name': 'compute_10', 'expression': 'rClWgt -  rClStwgt ', 'format': '#####0.000', 'label': 'compute_10', 'band': 'summary'}, {'name': 'clvalue', 'expression': ' clweight *  items_cost ', 'format': '########0.00', 'label': 'clvalue', 'band': 'summary'}, {'name': 'opstkwgt', 'expression': 'rOpWgt', 'format': '####0.000', 'label': 'opstkwgt', 'band': 'detail'}, {'name': 'compute_5', 'expression': ' rOpStwgt ', 'format': '####0.000', 'label': 'compute_5', 'band': 'detail'}, {'name': 'compute_9', 'expression': 'rOpWgt -  rOpStwgt ', 'format': '#####0.000', 'label': 'compute_9', 'band': 'detail'}, {'name': 'opvalue', 'expression': 'rOpwgt * items_opcost', 'format': '######0.00', 'label': 'opvalue', 'band': 'detail'}], 'columns': [{'name': 'code', 'label': 'items_code', 'type': 'char'}, {'name': 'name', 'label': 'items_name', 'type': 'char'}, {'name': 'opqty', 'label': 'items_opqty', 'type': 'long'}, {'name': 'opweight', 'label': 'items_opweight', 'type': 'real'}, {'name': 'opqtyb', 'label': 'items_opqtyb', 'type': 'long'}, {'name': 'opweightb', 'label': 'items_opweightb', 'type': 'real'}, {'name': 'opcost', 'label': 'items_opcost', 'type': 'real'}, {'name': 'cost', 'label': 'items_cost', 'type': 'real'}]},
    report={'dataobject': 'd_itemhistory', 'sql': 'SELECT items.code AS items_code, items.name AS items_name, items.opqty AS items_opqty, items.opweight AS items_opweight, items.opqtyb AS items_opqtyb, items.opweightb AS items_opweightb, items.opcost AS items_opcost, items.cost AS items_cost FROM items WHERE items.code = :rcode', 'computes': [{'name': 'compute_6', 'expression': 'rClQty', 'format': '#####0', 'label': 'compute_6', 'band': 'summary'}, {'name': 'opstkqty', 'expression': 'rOpqty', 'format': '###0', 'label': 'opstkqty', 'band': 'detail'}, {'name': 'clweight', 'expression': 'rClWgt', 'format': '######0.000', 'label': 'clweight', 'band': 'summary'}, {'name': 'compute_7', 'expression': ' rClStwgt ', 'format': '######0.000', 'label': 'compute_7', 'band': 'summary'}, {'name': 'compute_10', 'expression': 'rClWgt -  rClStwgt ', 'format': '#####0.000', 'label': 'compute_10', 'band': 'summary'}, {'name': 'clvalue', 'expression': ' clweight *  items_cost ', 'format': '########0.00', 'label': 'clvalue', 'band': 'summary'}, {'name': 'opstkwgt', 'expression': 'rOpWgt', 'format': '####0.000', 'label': 'opstkwgt', 'band': 'detail'}, {'name': 'compute_5', 'expression': ' rOpStwgt ', 'format': '####0.000', 'label': 'compute_5', 'band': 'detail'}, {'name': 'compute_9', 'expression': 'rOpWgt -  rOpStwgt ', 'format': '#####0.000', 'label': 'compute_9', 'band': 'detail'}, {'name': 'opvalue', 'expression': 'rOpwgt * items_opcost', 'format': '######0.00', 'label': 'opvalue', 'band': 'detail'}], 'args': ['rcode', 'rlevel', 'rdate1', 'rdate2', 'rOpQty', 'rOpWgt', 'rClQty', 'rClWgt', 'rOpStwgt', 'rClStwgt', 'rstktype', 'rstktouch'], 'arg_types': {'rcode': 'string', 'rlevel': 'number', 'rdate1': 'date', 'rdate2': 'date', 'rOpQty': 'number', 'rOpWgt': 'decimal', 'rClQty': 'number', 'rClWgt': 'decimal', 'rOpStwgt': 'decimal', 'rClStwgt': 'decimal', 'rstktype': 'string', 'rstktouch': 'string'}, 'tables': ['items'], 'columns': [{'name': 'items_code', 'label': 'items_code', 'type': 'char'}, {'name': 'items_name', 'label': 'items_name', 'type': 'char'}, {'name': 'items_opqty', 'label': 'items_opqty', 'type': 'long'}, {'name': 'items_opweight', 'label': 'items_opweight', 'type': 'real'}, {'name': 'items_opqtyb', 'label': 'items_opqtyb', 'type': 'long'}, {'name': 'items_opweightb', 'label': 'items_opweightb', 'type': 'real'}, {'name': 'items_opcost', 'label': 'items_opcost', 'type': 'real'}, {'name': 'items_cost', 'label': 'items_cost', 'type': 'real'}]},
    opens=['w_repsetup', 'w_itemhelp'],
)


class ItemHistoryForm(GeneratedForm):
    """Item History"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('statictext', 'st_3', 18, 0, 366, 72, text='Item Code :')
        self.add('singlelineedit', 'sle_itemcode', 393, 0, 539, 96, limit=10, taborder=10)
        self.add('commandbutton', 'cb_4', 946, 0, 187, 96, text='&Help')
        self.add('editmask', 'em_date1', 1417, 0, 347, 92, taborder=30)
        self.add('editmask', 'em_date2', 2075, 0, 352, 92, taborder=40)
        self.add('commandbutton', 'cb_show', 2469, 0, 288, 96, text='&Show', taborder=50)
        self.add('commandbutton', 'cb_3', 2839, 0, 274, 96, text='Save &As', taborder=80)
        self.add('commandbutton', 'cb_1', 3113, 0, 247, 96, text='&Print', taborder=90)
        self.add('commandbutton', 'cb_2', 3360, 0, 247, 96, text='E&xit', taborder=70)
        self.add('statictext', 'st_1', 1211, 8, 197, 76, text='From :')
        self.add('statictext', 'st_2', 1888, 8, 178, 76, text='To :')
        self.add('datawindow', 'dw_stktype', 393, 96, 539, 88, dataobject='d_stktypecode', taborder=20)
        self.add('commandbutton', 'cb_defzoom', 3360, 96, 247, 88, text='Def zoom', taborder=30)
        self.add('statictext', 'st_date', 1042, 100, 357, 76)
        self.add('checkbox', 'cbx_ledger', 1413, 100, 672, 68, text='Show as Stock Ledger')
        self.add('checkbox', 'cbx_summary', 2094, 100, 338, 68, text='Summary')
        self.add('checkbox', 'cbx_withoutqty', 2478, 100, 402, 68, text='Without Qty')
        self.add('checkbox', 'cbx_speed', 2894, 100, 270, 68, text='Speed')
        self.add('statictext', 'st_grp', 14, 108, 370, 76, text='Stock Type :')
        self.add('checkbox', 'cbx_stktype', 965, 108, 82, 76)
        self.add('checkbox', 'cbx_withstktouch', 1413, 176, 686, 80, text='With Stock Touch Calc')
        self.add('checkbox', 'cbx_nostktouchwgt', 2094, 176, 553, 80, text='No Stk Touch Wgt')
        self.add('checkbox', 'cbx_wsmodel', 2894, 176, 480, 80, text='WS Model Print')
        self.add('commandbutton', 'cb_setup', 3360, 180, 247, 80, text='Setup', taborder=30)
        self.add('checkbox', 'cbx_taxrep', 389, 200, 370, 68, text='Tax Report')
        self.add('datawindow', 'dw_history', 0, 284, 3630, 1868, dataobject='d_itemhistory', taborder=60)
        self.add('commandbutton', 'cb_toexcel', 2894, 288, 265, 92, text='To Excel', taborder=40)
