"""Stock Verification Report — w_bcstkverifyrep.

Generated from the PowerBuilder window ``w_bcstkverifyrep.srw`` by
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
    name='w_bcstkverifyrep',
    title='Stock Verification Report',
    width=3680,
    height=2256,
    controls=[],
    tables=[],
    source_path='w_bcstkverifyrep.srw',
    grid={'control': 'dw_1', 'dataobject': 'd_bcstkverifyrep', 'table': 'items', 'keys': ['code'], 'columns': [{'name': 'code', 'label': 'code', 'type': 'char'}, {'name': 'itype', 'label': 'itype', 'type': 'char'}, {'name': 'ornament', 'label': 'ornament', 'type': 'char'}, {'name': 'grpcode', 'label': 'grpcode', 'type': 'char'}, {'name': 'counteriqty', 'label': 'counteriqty', 'type': 'long'}, {'name': 'counteriwgt', 'label': 'counteriwgt', 'type': 'decimal'}, {'name': 'name', 'label': 'name', 'type': 'char'}, {'name': 'counterswgt', 'label': 'counterswgt', 'type': 'decimal'}, {'name': 'countersqty', 'label': 'countersqty', 'type': 'long'}, {'name': 'verifyqty', 'label': 'verifyqty', 'type': 'long'}, {'name': 'verifywgt', 'label': 'verifywgt', 'type': 'decimal'}, {'name': 'dmdplt', 'label': 'dmdplt', 'type': 'char'}]},
    report={'dataobject': 'd_bcstkverifyrep', 'sql': "SELECT items.code AS items_code, items.itype AS items_itype, items.ornament AS items_ornament, items.grpcode AS items_grpcode, items.name AS items_name, items.dmdplt AS items_dmdplt, (select sum(barcode.qty) from barcode where barcode.icode = items.code and barcode.counter = ifnull(:rcounter,barcode.counter,:rcounter) and barcode.counter <> '') as counteriqty, (select sum(barcode.weight) from barcode where barcode.icode = items.code and barcode.counter = ifnull(:rcounter,barcode.counter,:rcounter) and barcode.counter <> '') as counteriwgt, (select sum(salesd.weight) from salesd,barcode,salesm where salesd.slno = salesm.slno and salesm.tdate = :rdate and salesm.control <= :rlevel and salesd.bcode = barcode.bcode and barcode.icode = items.code and barcode.counter = ifnull(:rcounter,barcode.counter,:rcounter) and barcode.counter <> '') as counterswgt, (select sum(salesd.qty) from salesd,barcode,salesm where salesd.slno = salesm.slno and salesm.tdate = :rdate and salesm.control <= :rlevel and salesd.bcode = barcode.bcode and barcode.icode = items.code and barcode.counter = ifnull(:rcounter,barcode.counter,:rcounter) and barcode.counter <> '') as countersqty, (select sum(barcode.qty) from barcode where barcode.icode = items.code and barcode.counter = ifnull(:rcounter,barcode.counter,:rcounter) and barcode.counter <> '' and taken = 1) as verifyqty, (select sum(barcode.weight) from barcode where barcode.icode = items.code and barcode.counter = ifnull(:rcounter,barcode.counter,:rcounter) and barcode.counter <> '' and taken = 1) as verifywgt FROM items", 'args': ['rdate', 'rlevel', 'rcounter'], 'arg_types': {'rdate': 'date', 'rlevel': 'number', 'rcounter': 'string'}, 'tables': ['items'], 'columns': [{'name': 'code', 'label': 'code', 'type': 'char'}, {'name': 'itype', 'label': 'itype', 'type': 'char'}, {'name': 'ornament', 'label': 'ornament', 'type': 'char'}, {'name': 'grpcode', 'label': 'grpcode', 'type': 'char'}, {'name': 'counteriqty', 'label': 'counteriqty', 'type': 'long'}, {'name': 'counteriwgt', 'label': 'counteriwgt', 'type': 'decimal'}, {'name': 'name', 'label': 'name', 'type': 'char'}, {'name': 'counterswgt', 'label': 'counterswgt', 'type': 'decimal'}, {'name': 'countersqty', 'label': 'countersqty', 'type': 'long'}, {'name': 'verifyqty', 'label': 'verifyqty', 'type': 'long'}, {'name': 'verifywgt', 'label': 'verifywgt', 'type': 'decimal'}, {'name': 'dmdplt', 'label': 'dmdplt', 'type': 'char'}]},
)


class StockVerificationReportForm(GeneratedForm):
    """Stock Verification Report"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date', 279, 0, 425, 92, taborder=10)
        self.add('datawindow', 'dw_counter', 1152, 0, 667, 88, dataobject='d_countercode', taborder=70)
        self.add('commandbutton', 'cb_show', 2158, 0, 293, 92, text='&Show', taborder=20)
        self.add('commandbutton', 'cb_sort', 2491, 0, 247, 92, text='So&rt', taborder=30)
        self.add('commandbutton', 'cb_1', 2761, 0, 270, 92, text='Save &As', taborder=80)
        self.add('commandbutton', 'cb_bcodeprint', 3054, 0, 233, 92, text='&Print', taborder=60)
        self.add('commandbutton', 'cb_exit', 3314, 0, 233, 92, text='E&xit', taborder=50)
        self.add('checkbox', 'cbx_counter', 1829, 4, 82, 76)
        self.add('statictext', 'st_1', 864, 8, 279, 76, text='Counter :')
        self.add('statictext', 'st_10', 32, 12, 233, 64, text='Date :')
        self.add('datawindow', 'dw_1', 0, 116, 3625, 1932, dataobject='d_bcstkverifyrep', taborder=40)
