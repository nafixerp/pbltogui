"""Barcode Entry Comparison — w_barcode_comparison_report.

Generated from the PowerBuilder window ``w_barcode_comparison_report.srw`` by
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
    name='w_barcode_comparison_report',
    title='Barcode Entry Comparison',
    width=3707,
    height=2496,
    controls=[],
    tables=[],
    source_path='w_barcode_comparison_report.srw',
    report={'dataobject': 'd_barcode_comparison_rep', 'sql': 'SELECT barcodedoc.docno AS barcodedoc_docno, barcodedoc.tdate AS barcodedoc_tdate, barcodedoc.smith AS barcodedoc_smith, barcodedoc.totwgt AS barcodedoc_totwgt, barcodedoc.totnos AS barcodedoc_totnos, 0 as prn, (select sum(barcode.weight) from barcode where barcode.docno = barcodedoc.docno) as bctwgt, (select sum(barcode.qty) from barcode where barcode.docno = barcodedoc.docno) as bctqty FROM barcodedoc WHERE barcodedoc.tdate >= :rdate1 AND barcodedoc.tdate <= :rdate2 ORDER BY barcodedoc.tdate ASC, barcodedoc.docno ASC', 'computes': [{'name': 'qtydiff', 'expression': ' totnos  -  if(isnull( bctqty ),0,bctqty)', 'format': '####0', 'label': 'qtydiff', 'band': 'detail'}, {'name': 'wgtdiff', 'expression': ' totwgt  -  if(isnull(  bctwgt ),0, bctwgt )', 'format': '####0.000', 'label': 'wgtdiff', 'band': 'detail'}, {'name': 'compute_4', 'expression': 'sum(totnos for all)', 'format': '#####0', 'label': 'compute_4', 'band': 'summary'}, {'name': 'compute_7', 'expression': 'sum(bctqty for all)', 'format': '#####0', 'label': 'compute_7', 'band': 'summary'}, {'name': 'compute_8', 'expression': 'sum(qtydiff for all)', 'format': '####0', 'label': 'compute_8', 'band': 'summary'}, {'name': 'compute_6', 'expression': 'sum(totwgt for all)', 'format': '######0.000', 'label': 'compute_6', 'band': 'summary'}, {'name': 'compute_5', 'expression': 'sum(bctwgt for all)', 'format': '######0.000', 'label': 'compute_5', 'band': 'summary'}, {'name': 'compute_9', 'expression': 'sum( wgtdiff for all)', 'format': '####0.000', 'label': 'compute_9', 'band': 'summary'}, {'name': 'compute_10', 'expression': 'avg(qtydiff for all)', 'format': '####0', 'label': 'compute_10', 'band': 'summary'}, {'name': 'compute_11', 'expression': 'avg( wgtdiff for all)', 'format': '####0.000', 'label': 'compute_11', 'band': 'summary'}], 'args': ['rdate1', 'rdate2', 'rlevel'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date', 'rlevel': 'number'}, 'tables': ['barcodedoc'], 'columns': [{'name': 'items_prn', 'label': 'items_prn', 'type': 'long'}, {'name': 'docno', 'label': 'docno', 'type': 'char'}, {'name': 'tdate', 'label': 'tdate', 'type': 'date'}, {'name': 'smith', 'label': 'smith', 'type': 'char'}, {'name': 'totwgt', 'label': 'totwgt', 'type': 'decimal'}, {'name': 'totnos', 'label': 'totnos', 'type': 'decimal'}, {'name': 'bctwgt', 'label': 'bctwgt', 'type': 'decimal'}, {'name': 'bctqty', 'label': 'bctqty', 'type': 'long'}]},
)


class BarcodeEntryComparisonForm(GeneratedForm):
    """Barcode Entry Comparison"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 402, 0, 425, 92, taborder=10)
        self.add('editmask', 'em_date2', 1207, 0, 425, 92, taborder=20)
        self.add('commandbutton', 'cb_show', 1883, 0, 315, 92, text='&Show', taborder=30)
        self.add('commandbutton', 'cb_sort', 2469, 0, 247, 92, text='So&rt', taborder=50)
        self.add('commandbutton', 'cb_1', 2747, 0, 270, 92, text='Save &As', taborder=120)
        self.add('commandbutton', 'cb_bcodeprint', 3022, 0, 233, 92, text='&Print', taborder=110)
        self.add('commandbutton', 'cb_exit', 3259, 0, 233, 92, text='E&xit', taborder=100)
        self.add('statictext', 'st_11', 901, 8, 302, 72, text='Date To :')
        self.add('statictext', 'st_10', 27, 12, 361, 64, text='Date From :')
        self.add('datawindow', 'dw_saleregister', 0, 192, 3625, 1932, dataobject='d_barcode_comparison_rep', taborder=60)
