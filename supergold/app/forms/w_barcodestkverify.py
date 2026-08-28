"""Stock Verification — w_barcodestkverify.

Generated from the PowerBuilder window ``w_barcodestkverify.srw`` by
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
    name='w_barcodestkverify',
    title='Stock Verification',
    width=3913,
    height=2236,
    controls=[],
    tables=['barcode', 'items', 'barcodedmd', 'file', 'device'],
    source_path='w_barcodestkverify.srw',
    grid={'control': 'dw_summary', 'dataobject': 'd_barcodestkverify_summary', 'table': 'barcode', 'keys': ['bcode'], 'columns': [{'name': 'bcode', 'label': 'bcode', 'type': 'decimal'}, {'name': 'itemname', 'label': 'itemname', 'type': 'char'}, {'name': 'weight', 'label': 'weight', 'type': 'decimal'}, {'name': 'dmdwgt', 'label': 'dmdwgt', 'type': 'decimal'}, {'name': 'tdate', 'label': 'tdate', 'type': 'date'}, {'name': 'stk', 'label': 'stk', 'type': 'char'}, {'name': 'icode', 'label': 'icode', 'type': 'char'}, {'name': 'qty', 'label': 'qty', 'type': 'long'}, {'name': 'stweight', 'label': 'stweight', 'type': 'decimal'}, {'name': 'stprice', 'label': 'stprice', 'type': 'decimal'}, {'name': 'wastage', 'label': 'wastage', 'type': 'decimal'}, {'name': 'mc', 'label': 'mc', 'type': 'decimal'}, {'name': 'dmdunit', 'label': 'dmdunit', 'type': 'char'}, {'name': 'dmdamt', 'label': 'dmdamt', 'type': 'decimal'}, {'name': 'smcode', 'label': 'smcode', 'type': 'char'}, {'name': 'mcrate', 'label': 'mcrate', 'type': 'decimal'}, {'name': 'rate', 'label': 'rate', 'type': 'decimal'}, {'name': 'tamt', 'label': 'tamt', 'type': 'decimal'}]},
    report={'dataobject': 'd_barcodestkverify_summary', 'sql': 'SELECT barcode.bcode AS barcode_bcode, barcode.weight AS barcode_weight, barcode.dmdwgt AS barcode_dmdwgt, barcode.tdate AS barcode_tdate, barcode.stk AS barcode_stk, barcode.icode AS barcode_icode, barcode.qty AS barcode_qty, barcode.stweight AS barcode_stweight, barcode.stprice AS barcode_stprice, barcode.wastage AS barcode_wastage, barcode.mc AS barcode_mc, barcode.dmdunit AS barcode_dmdunit, barcode.dmdamt AS barcode_dmdamt, barcode.smcode AS barcode_smcode, barcode.mcrate AS barcode_mcrate, barcode.rate AS barcode_rate, barcode.tamt AS barcode_tamt, (select items.name from items where items.code = barcode.icode) as itemname FROM barcode ORDER BY barcode.bcode DESC', 'args': [], 'arg_types': {}, 'tables': ['barcode'], 'columns': [{'name': 'bcode', 'label': 'bcode', 'type': 'decimal'}, {'name': 'itemname', 'label': 'itemname', 'type': 'char'}, {'name': 'weight', 'label': 'weight', 'type': 'decimal'}, {'name': 'dmdwgt', 'label': 'dmdwgt', 'type': 'decimal'}, {'name': 'tdate', 'label': 'tdate', 'type': 'date'}, {'name': 'stk', 'label': 'stk', 'type': 'char'}, {'name': 'icode', 'label': 'icode', 'type': 'char'}, {'name': 'qty', 'label': 'qty', 'type': 'long'}, {'name': 'stweight', 'label': 'stweight', 'type': 'decimal'}, {'name': 'stprice', 'label': 'stprice', 'type': 'decimal'}, {'name': 'wastage', 'label': 'wastage', 'type': 'decimal'}, {'name': 'mc', 'label': 'mc', 'type': 'decimal'}, {'name': 'dmdunit', 'label': 'dmdunit', 'type': 'char'}, {'name': 'dmdamt', 'label': 'dmdamt', 'type': 'decimal'}, {'name': 'smcode', 'label': 'smcode', 'type': 'char'}, {'name': 'mcrate', 'label': 'mcrate', 'type': 'decimal'}, {'name': 'rate', 'label': 'rate', 'type': 'decimal'}, {'name': 'tamt', 'label': 'tamt', 'type': 'decimal'}]},
    opens=['w_itemhelp'],
)


class StockVerificationForm(GeneratedForm):
    """Stock Verification"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('datawindow', 'dw_itemlist', 0, 0, 2377, 1080, dataobject='d_barcodestkverify', taborder=30)
        self.add('datawindow', 'dw_counter', 2670, 0, 654, 88, dataobject='d_countercode', taborder=10)
        self.add('singlelineedit', 'sle_code', 3506, 0, 270, 92, limit=10, taborder=20)
        self.add('commandbutton', 'cb_hlp', 3781, 0, 69, 92, text='^')
        self.add('statictext', 'st_2', 2395, 8, 265, 64, text='Counter :')
        self.add('statictext', 'st_1', 3328, 8, 174, 76, text='Item :')
        self.add('datawindow', 'dw_grp', 2670, 92, 800, 88, dataobject='d_itemgrpcode', taborder=20)
        self.add('statictext', 'st_3', 2395, 96, 265, 64, text='Group :')
        self.add('datawindow', 'dw_subgrp', 2670, 188, 800, 88, dataobject='d_itemsubgrpcode', taborder=30)
        self.add('checkbox', 'cbx_subgrpbcbased', 3483, 192, 366, 80, text='BC Based')
        self.add('statictext', 'st_41', 2382, 196, 279, 80, text='Sub Grp :')
        self.add('datawindow', 'dw_error', 2391, 288, 1454, 792, dataobject='d_barcode_error')
        self.add('commandbutton', 'cb_1', 3054, 984, 247, 88, text='Print')
        self.add('statictext', 'st_search', 5, 996, 361, 80)
        self.add('commandbutton', 'cb_del', 370, 996, 201, 80, text='Del', taborder=80)
        self.add('commandbutton', 'cb_3', 571, 996, 274, 80, text='Fresh Mark', taborder=80)
        self.add('commandbutton', 'cb_filter', 841, 996, 215, 80, text='Filter')
        self.add('commandbutton', 'cb_sort', 1056, 996, 210, 80, text='Sort')
        self.add('commandbutton', 'cb_saveas', 1262, 996, 247, 80, text='&Save As')
        self.add('commandbutton', 'cb_getfromfile', 1509, 996, 329, 80, text='Get from File', taborder=70)
        self.add('commandbutton', 'cb_getfromterminal', 1838, 996, 425, 80, text='Get From Device', taborder=40)
        self.add('datawindow', 'dw_summary', 0, 1088, 3845, 1036, dataobject='d_barcodestkverify_summary', taborder=50)
        self.add('commandbutton', 'cb_summary', 617, 2020, 475, 88, text='Show Summary')
        self.add('commandbutton', 'cb_print', 1422, 2020, 247, 88, text='Print', taborder=60)
        self.add('commandbutton', 'cb_2', 1696, 2020, 567, 88, text='Reset Device', taborder=100)
        self.add('commandbutton', 'cb_finished', 2437, 2020, 320, 88, text='Finished', taborder=110)
        self.add('commandbutton', 'cb_updtcurbcodelist', 2770, 2020, 745, 88, text='Update this list as Correct', taborder=90)
