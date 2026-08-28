"""PDC Report — w_pdclist_report.

Generated from the PowerBuilder window ``w_pdclist_report.srw`` by
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
    name='w_pdclist_report',
    title='PDC Report',
    width=3634,
    height=2360,
    controls=[],
    tables=['pdclist', 'clients'],
    source_path='w_pdclist_report.srw',
    grid={'control': 'dw_1', 'dataobject': 'd_pdclist_report', 'table': 'pdclist', 'keys': ['chqno'], 'computes': [{'name': 'rcvdamt', 'expression': "if( rp ='R', amount, 0)", 'format': '#######0.00', 'label': 'rcvdamt', 'band': 'detail'}, {'name': 'paidamt', 'expression': "if( rp ='P', amount, 0)", 'format': '#######0.00', 'label': 'paidamt', 'band': 'detail'}, {'name': 'compute_5', 'expression': 'count(chqno for all)', 'format': '[general]', 'label': 'compute_5', 'band': 'summary'}, {'name': 'compute_3', 'expression': 'sum(rcvdamt for all)', 'format': '#######0.00', 'label': 'compute_3', 'band': 'summary'}, {'name': 'compute_4', 'expression': 'sum( paidamt for all)', 'format': '#######0.00', 'label': 'compute_4', 'band': 'summary'}], 'columns': [{'name': 'tdate', 'label': 'tdate', 'type': 'date'}, {'name': 'docno', 'label': 'docno', 'type': 'char'}, {'name': 'chqdate', 'label': 'chqdate', 'type': 'date'}, {'name': 'bank', 'label': 'bank', 'type': 'char'}, {'name': 'code', 'label': 'code', 'type': 'char'}, {'name': 'chqno', 'label': 'chqno', 'type': 'char'}, {'name': 'amount', 'label': 'amount', 'type': 'decimal'}, {'name': 'particulars', 'label': 'particulars', 'type': 'char'}, {'name': 'rp', 'label': 'rp', 'type': 'char'}, {'name': 'pend', 'label': 'pend', 'type': 'char'}, {'name': 'slno', 'label': 'slno', 'type': 'decimal'}, {'name': 'bankname', 'label': 'bankname', 'type': 'char'}, {'name': 'partyname', 'label': 'partyname', 'type': 'char'}]},
    report={'dataobject': 'd_pdclist_report', 'sql': 'SELECT pdclist.tdate AS pdclist_tdate, pdclist.docno AS pdclist_docno, pdclist.chqdate AS pdclist_chqdate, pdclist.bank AS pdclist_bank, pdclist.code AS pdclist_code, pdclist.chqno AS pdclist_chqno, pdclist.amount AS pdclist_amount, pdclist.particulars AS pdclist_particulars, pdclist.rp AS pdclist_rp, pdclist.pend AS pdclist_pend, pdclist.slno AS pdclist_slno, (select accountm.name from accountm where accountm.accode = pdclist.bank) as bankname, (select accountm.name from accountm where accountm.accode = pdclist.code) as partyname FROM pdclist ORDER BY pdclist.tdate ASC, pdclist.docno ASC', 'computes': [{'name': 'rcvdamt', 'expression': "if( rp ='R', amount, 0)", 'format': '#######0.00', 'label': 'rcvdamt', 'band': 'detail'}, {'name': 'paidamt', 'expression': "if( rp ='P', amount, 0)", 'format': '#######0.00', 'label': 'paidamt', 'band': 'detail'}, {'name': 'compute_5', 'expression': 'count(chqno for all)', 'format': '[general]', 'label': 'compute_5', 'band': 'summary'}, {'name': 'compute_3', 'expression': 'sum(rcvdamt for all)', 'format': '#######0.00', 'label': 'compute_3', 'band': 'summary'}, {'name': 'compute_4', 'expression': 'sum( paidamt for all)', 'format': '#######0.00', 'label': 'compute_4', 'band': 'summary'}], 'args': ['rdate1', 'rdate2', 'rlevel'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date', 'rlevel': 'number'}, 'tables': ['pdclist'], 'columns': [{'name': 'tdate', 'label': 'tdate', 'type': 'date'}, {'name': 'docno', 'label': 'docno', 'type': 'char'}, {'name': 'chqdate', 'label': 'chqdate', 'type': 'date'}, {'name': 'bank', 'label': 'bank', 'type': 'char'}, {'name': 'code', 'label': 'code', 'type': 'char'}, {'name': 'chqno', 'label': 'chqno', 'type': 'char'}, {'name': 'amount', 'label': 'amount', 'type': 'decimal'}, {'name': 'particulars', 'label': 'particulars', 'type': 'char'}, {'name': 'rp', 'label': 'rp', 'type': 'char'}, {'name': 'pend', 'label': 'pend', 'type': 'char'}, {'name': 'slno', 'label': 'slno', 'type': 'decimal'}, {'name': 'bankname', 'label': 'bankname', 'type': 'char'}, {'name': 'partyname', 'label': 'partyname', 'type': 'char'}]},
    opens=['w_pdc_colln', 'w_clientshelp', 'w_repsetup'],
)


class PdcReportForm(GeneratedForm):
    """PDC Report"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 379, 0, 402, 100, taborder=10)
        self.add('editmask', 'em_date2', 1147, 0, 402, 100, taborder=20)
        self.add('commandbutton', 'cb_show', 1874, 0, 270, 96, text='&Show', taborder=30)
        self.add('commandbutton', 'cb_setup', 2153, 0, 238, 96, text='Setup', taborder=120)
        self.add('commandbutton', 'cb_saveas', 2400, 0, 238, 96, text='Save As', taborder=110)
        self.add('commandbutton', 'cb_sort', 2647, 0, 219, 96, text='So&rt', taborder=100)
        self.add('commandbutton', 'cb_filter', 2875, 0, 219, 96, text='&Filter', taborder=90)
        self.add('commandbutton', 'cb_1', 3104, 0, 247, 96, text='&Print', taborder=150)
        self.add('commandbutton', 'cb_2', 3355, 0, 247, 96, text='E&xit', taborder=140)
        self.add('checkbox', 'cbx_chqdate', 1586, 4, 256, 76, text='Chq Dt')
        self.add('statictext', 'st_2', 837, 8, 302, 72, text='Date To :')
        self.add('statictext', 'st_1', 9, 12, 366, 64, text='Date From :')
        self.add('dropdownlistbox', 'ddlb_rptype', 384, 108, 425, 468, text='All', items=['All', 'Paid', 'Received'], taborder=50)
        self.add('dropdownlistbox', 'ddlb_pend', 1147, 108, 608, 468, text='Pending Only', items=['All', 'Pending Only', 'Not Pending Only'], taborder=60)
        self.add('singlelineedit', 'sle_chqno', 3104, 108, 503, 92, taborder=40)
        self.add('datawindow', 'dw_party', 2144, 112, 425, 88, dataobject='d_sucu', taborder=80)
        self.add('statictext', 'st_3', 64, 116, 311, 76, text='R/P Type :')
        self.add('statictext', 'st_4', 1888, 116, 247, 76, text='Party :')
        self.add('statictext', 'st_5', 837, 120, 302, 76, text='Pending :')
        self.add('statictext', 'st_7', 2834, 120, 256, 76, text='Chq No :')
        self.add('datawindow', 'dw_1', 0, 216, 3616, 2052, dataobject='d_pdclist_report', taborder=130)
        self.add('commandbutton', 'cb_del', 2405, 220, 334, 72, text='Del', taborder=70)
        self.add('commandbutton', 'cb_clearance', 2752, 220, 334, 72, text='Clearance', taborder=121)
