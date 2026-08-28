"""Counter Issue — w_counter_issue.

Generated from the PowerBuilder window ``w_counter_issue.srw`` by
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
    name='w_counter_issue',
    title='Counter Issue',
    width=3657,
    height=2236,
    controls=[],
    tables=['barcode', 'counter', 'barcodedmd', 'items'],
    source_path='w_counter_issue.srw',
    grid={'control': 'dw_summary', 'dataobject': 'd_barcodestkverify_summary', 'table': 'barcode', 'keys': ['bcode'], 'computes': [{'name': 'netwgt', 'expression': ' weight  -  stweight ', 'format': '######0.000', 'label': 'netwgt', 'band': 'detail'}, {'name': 'compute_1', 'expression': 'count(bcode for all)', 'format': '[general]', 'label': 'compute_1', 'band': 'summary'}, {'name': 'compute_3', 'expression': 'sum(qty for all)', 'format': '#####', 'label': 'compute_3', 'band': 'summary'}, {'name': 'compute_2', 'expression': 'sum(weight for all)', 'format': '#######0.000', 'label': 'compute_2', 'band': 'summary'}, {'name': 'compute_4', 'expression': 'sum(stweight for all)', 'format': '#####0.000', 'label': 'compute_4', 'band': 'summary'}, {'name': 'compute_5', 'expression': 'sum( netwgt  for all)', 'format': '######0.000', 'label': 'compute_5', 'band': 'summary'}, {'name': 'compute_6', 'expression': 'sum(dmdwgt for all)', 'format': '#######0.00', 'label': 'compute_6', 'band': 'summary'}, {'name': 'compute_7', 'expression': 'sum(tamt for all)', 'format': '###########0.00', 'label': 'compute_7', 'band': 'summary'}], 'columns': [{'name': 'bcode', 'label': 'bcode', 'type': 'decimal'}, {'name': 'itemname', 'label': 'itemname', 'type': 'char'}, {'name': 'weight', 'label': 'weight', 'type': 'decimal'}, {'name': 'dmdwgt', 'label': 'dmdwgt', 'type': 'decimal'}, {'name': 'tdate', 'label': 'tdate', 'type': 'date'}, {'name': 'stk', 'label': 'stk', 'type': 'char'}, {'name': 'icode', 'label': 'icode', 'type': 'char'}, {'name': 'qty', 'label': 'qty', 'type': 'long'}, {'name': 'stweight', 'label': 'stweight', 'type': 'decimal'}, {'name': 'stprice', 'label': 'stprice', 'type': 'decimal'}, {'name': 'wastage', 'label': 'wastage', 'type': 'decimal'}, {'name': 'mc', 'label': 'mc', 'type': 'decimal'}, {'name': 'dmdunit', 'label': 'dmdunit', 'type': 'char'}, {'name': 'dmdamt', 'label': 'dmdamt', 'type': 'decimal'}, {'name': 'smcode', 'label': 'smcode', 'type': 'char'}, {'name': 'mcrate', 'label': 'mcrate', 'type': 'decimal'}, {'name': 'rate', 'label': 'rate', 'type': 'decimal'}, {'name': 'tamt', 'label': 'tamt', 'type': 'decimal'}]},
    report={'dataobject': 'd_barcodestkverify_summary', 'sql': 'SELECT barcode.bcode AS barcode_bcode, barcode.weight AS barcode_weight, barcode.dmdwgt AS barcode_dmdwgt, barcode.tdate AS barcode_tdate, barcode.stk AS barcode_stk, barcode.icode AS barcode_icode, barcode.qty AS barcode_qty, barcode.stweight AS barcode_stweight, barcode.stprice AS barcode_stprice, barcode.wastage AS barcode_wastage, barcode.mc AS barcode_mc, barcode.dmdunit AS barcode_dmdunit, barcode.dmdamt AS barcode_dmdamt, barcode.smcode AS barcode_smcode, barcode.mcrate AS barcode_mcrate, barcode.rate AS barcode_rate, barcode.tamt AS barcode_tamt, (select items.name from items where items.code = barcode.icode) as itemname FROM barcode ORDER BY barcode.bcode DESC', 'computes': [{'name': 'netwgt', 'expression': ' weight  -  stweight ', 'format': '######0.000', 'label': 'netwgt', 'band': 'detail'}, {'name': 'compute_1', 'expression': 'count(bcode for all)', 'format': '[general]', 'label': 'compute_1', 'band': 'summary'}, {'name': 'compute_3', 'expression': 'sum(qty for all)', 'format': '#####', 'label': 'compute_3', 'band': 'summary'}, {'name': 'compute_2', 'expression': 'sum(weight for all)', 'format': '#######0.000', 'label': 'compute_2', 'band': 'summary'}, {'name': 'compute_4', 'expression': 'sum(stweight for all)', 'format': '#####0.000', 'label': 'compute_4', 'band': 'summary'}, {'name': 'compute_5', 'expression': 'sum( netwgt  for all)', 'format': '######0.000', 'label': 'compute_5', 'band': 'summary'}, {'name': 'compute_6', 'expression': 'sum(dmdwgt for all)', 'format': '#######0.00', 'label': 'compute_6', 'band': 'summary'}, {'name': 'compute_7', 'expression': 'sum(tamt for all)', 'format': '###########0.00', 'label': 'compute_7', 'band': 'summary'}], 'args': [], 'arg_types': {}, 'tables': ['barcode'], 'columns': [{'name': 'bcode', 'label': 'bcode', 'type': 'decimal'}, {'name': 'itemname', 'label': 'itemname', 'type': 'char'}, {'name': 'weight', 'label': 'weight', 'type': 'decimal'}, {'name': 'dmdwgt', 'label': 'dmdwgt', 'type': 'decimal'}, {'name': 'tdate', 'label': 'tdate', 'type': 'date'}, {'name': 'stk', 'label': 'stk', 'type': 'char'}, {'name': 'icode', 'label': 'icode', 'type': 'char'}, {'name': 'qty', 'label': 'qty', 'type': 'long'}, {'name': 'stweight', 'label': 'stweight', 'type': 'decimal'}, {'name': 'stprice', 'label': 'stprice', 'type': 'decimal'}, {'name': 'wastage', 'label': 'wastage', 'type': 'decimal'}, {'name': 'mc', 'label': 'mc', 'type': 'decimal'}, {'name': 'dmdunit', 'label': 'dmdunit', 'type': 'char'}, {'name': 'dmdamt', 'label': 'dmdamt', 'type': 'decimal'}, {'name': 'smcode', 'label': 'smcode', 'type': 'char'}, {'name': 'mcrate', 'label': 'mcrate', 'type': 'decimal'}, {'name': 'rate', 'label': 'rate', 'type': 'decimal'}, {'name': 'tamt', 'label': 'tamt', 'type': 'decimal'}]},
)


class CounterIssueForm(GeneratedForm):
    """Counter Issue"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('commandbutton', 'cb_removeallitems', 1833, 0, 558, 104, text='Refresh This List', taborder=10)
        self.add('commandbutton', 'cb_ok', 2409, 0, 274, 104, text='Ok', taborder=40)
        self.add('commandbutton', 'cb_update', 2757, 0, 507, 104, text='Update Counter', taborder=30)
        self.add('datawindow', 'dw_counter', 370, 8, 654, 88, dataobject='d_countercode', taborder=20)
        self.add('statictext', 'st_2', 59, 16, 297, 76, text='Counter :')
        self.add('datawindow', 'dw_itemlist', 0, 112, 2386, 968, dataobject='d_barcodestkverify', taborder=50)
        self.add('datawindow', 'dw_error', 2395, 116, 1225, 964, dataobject='d_barcode_error', taborder=60)
        self.add('commandbutton', 'cb_summary', 1787, 972, 475, 96, text='Show Summary')
        self.add('statictext', 'st_search', 50, 976, 585, 84)
        self.add('singlelineedit', 'sle_code', 352, 976, 329, 92, limit=10)
        self.add('commandbutton', 'cb_filter', 722, 976, 247, 92, text='Filter')
        self.add('commandbutton', 'cb_sort', 987, 976, 247, 92, text='Sort')
        self.add('commandbutton', 'cb_saveas', 1266, 976, 247, 92, text='&Save As')
        self.add('commandbutton', 'cb_print2', 1531, 976, 233, 92, text='Print')
        self.add('statictext', 'st_1', 27, 984, 320, 76, text='Item Code :')
        self.add('datawindow', 'dw_summary', 0, 1088, 3607, 1036, dataobject='d_barcodestkverify_summary', taborder=70)
        self.add('commandbutton', 'cb_print', 1733, 2012, 389, 100, text='Print', taborder=80)
