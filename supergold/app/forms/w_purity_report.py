"""Purity Test Report — w_purity_report.

Generated from the PowerBuilder window ``w_purity_report.srw`` by
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
    name='w_purity_report',
    title='Purity Test Report',
    width=3611,
    height=2040,
    controls=[],
    tables=['testdet'],
    source_path='w_purity_report.srw',
    grid={'control': 'dw_1', 'dataobject': 'd_purity_report', 'table': 'testdet', 'keys': ['slno'], 'columns': [{'name': 'tdate', 'label': 'Date', 'type': 'date'}, {'name': 'docno', 'label': 'Doc No', 'type': 'char'}, {'name': 'customer', 'label': 'Customer', 'type': 'char'}, {'name': 'purityinperc', 'label': 'Purity%', 'type': 'decimal'}, {'name': 'purityinct', 'label': 'Purity CT', 'type': 'decimal'}, {'name': 'otherinfo', 'label': 'Other Info', 'type': 'char'}, {'name': 'rcvdon', 'label': 'Rcvd On', 'type': 'date'}, {'name': 'testedon', 'label': 'Tested On', 'type': 'date'}, {'name': 'rcvdwgt', 'label': 'Rcvd Wgt', 'type': 'decimal'}, {'name': 'slno', 'label': 'slno', 'type': 'decimal'}]},
    report={'dataobject': 'd_purity_report', 'sql': 'SELECT testdet.tdate AS testdet_tdate, testdet.docno AS testdet_docno, testdet.customer AS testdet_customer, testdet.purityinperc AS testdet_purityinperc, testdet.purityinct AS testdet_purityinct, testdet.otherinfo AS testdet_otherinfo, testdet.rcvdon AS testdet_rcvdon, testdet.testedon AS testdet_testedon, testdet.rcvdwgt AS testdet_rcvdwgt, testdet.slno AS testdet_slno FROM testdet ORDER BY testdet.tdate ASC, testdet.docno ASC', 'args': ['rdate1', 'rdate2', 'rlevel'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date', 'rlevel': 'number'}, 'tables': ['testdet'], 'columns': [{'name': 'tdate', 'label': 'Date', 'type': 'date'}, {'name': 'docno', 'label': 'Doc No', 'type': 'char'}, {'name': 'customer', 'label': 'Customer', 'type': 'char'}, {'name': 'purityinperc', 'label': 'Purity%', 'type': 'decimal'}, {'name': 'purityinct', 'label': 'Purity CT', 'type': 'decimal'}, {'name': 'otherinfo', 'label': 'Other Info', 'type': 'char'}, {'name': 'rcvdon', 'label': 'Rcvd On', 'type': 'date'}, {'name': 'testedon', 'label': 'Tested On', 'type': 'date'}, {'name': 'rcvdwgt', 'label': 'Rcvd Wgt', 'type': 'decimal'}, {'name': 'slno', 'label': 'slno', 'type': 'decimal'}]},
    opens=['w_purity_entry'],
)


class PurityTestReportForm(GeneratedForm):
    """Purity Test Report"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 242, 8, 411, 100, taborder=10)
        self.add('editmask', 'em_date2', 969, 8, 411, 100, taborder=20)
        self.add('commandbutton', 'cb_show', 1435, 8, 343, 100, text='&Show')
        self.add('commandbutton', 'cb_print', 1879, 8, 343, 100, text='Print')
        self.add('commandbutton', 'cb_del', 2322, 8, 343, 100, text='Delete')
        self.add('commandbutton', 'cb_slip', 2784, 8, 343, 100, text='Slip Print')
        self.add('commandbutton', 'cb_exit', 3218, 8, 343, 100, text='E&xit')
        self.add('statictext', 'st_2', 827, 16, 123, 80, text='To :')
        self.add('statictext', 'st_1', 9, 20, 219, 80, text='From :')
        self.add('datawindow', 'dw_1', 0, 116, 3566, 1784, dataobject='d_purity_report', taborder=30)
