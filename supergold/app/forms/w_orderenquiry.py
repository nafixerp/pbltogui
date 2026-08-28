"""Order Enquiry — w_orderenquiry.

Generated from the PowerBuilder window ``w_orderenquiry.srw`` by
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
    name='w_orderenquiry',
    title='Order Enquiry',
    width=3465,
    height=2140,
    controls=[],
    tables=[],
    source_path='w_orderenquiry.srw',
    grid={'control': 'dw_1', 'dataobject': 'd_orderenquiry', 'table': 'orderm', 'keys': ['slno'], 'computes': [], 'columns': [{'name': 'ordno', 'label': 'orderm_ordno', 'type': 'char'}, {'name': 'tdate', 'label': 'orderm_tdate', 'type': 'date'}, {'name': 'duedate', 'label': 'orderm_duedate', 'type': 'date'}, {'name': 'rate', 'label': 'orderm_rate', 'type': 'decimal'}, {'name': 'custname', 'label': 'orderm_custname', 'type': 'char'}, {'name': 'billamt', 'label': 'orderm_billamt', 'type': 'decimal'}, {'name': 'eamt', 'label': 'orderm_eamt', 'type': 'decimal'}, {'name': 'advance', 'label': 'orderm_advance', 'type': 'decimal'}, {'name': 'status', 'label': 'status', 'type': 'long'}, {'name': 'slno', 'label': 'orderm_slno', 'type': 'decimal'}, {'name': 'custcode', 'label': 'custcode', 'type': 'char'}, {'name': 'smname', 'label': 'smname', 'type': 'char'}, {'name': 'gadvance', 'label': 'gadvance', 'type': 'decimal'}, {'name': 'sretamt', 'label': 'sretamt', 'type': 'decimal'}, {'name': 'smcode', 'label': 'smcode', 'type': 'char'}, {'name': 'addr', 'label': 'addr', 'type': 'char'}, {'name': 'refund', 'label': 'refund', 'type': 'decimal'}, {'name': 'duedate_org', 'label': 'duedate_org', 'type': 'date'}, {'name': 'phone', 'label': 'phone', 'type': 'char'}, {'name': 'advafter', 'label': 'advafter', 'type': 'decimal'}, {'name': 'advafterwgt', 'label': 'advafterwgt', 'type': 'decimal'}]},
    report={'dataobject': 'd_orderenquiry', 'sql': 'SELECT orderm.ordno AS orderm_ordno, orderm.tdate AS orderm_tdate, orderm.duedate AS orderm_duedate, orderm.rate AS orderm_rate, orderm.custname AS orderm_custname, orderm.billamt AS orderm_billamt, orderm.eamt AS orderm_eamt, orderm.advance AS orderm_advance, orderm.status AS orderm_status, orderm.slno AS orderm_slno, orderm.custcode AS orderm_custcode, orderm.gadvance AS orderm_gadvance, orderm.sretamt AS orderm_sretamt, orderm.smcode AS orderm_smcode, orderm.addr AS orderm_addr, orderm.refund AS orderm_refund, orderm.duedate_org AS orderm_duedate_org, orderm.phone AS orderm_phone, (select name from sman where code = orderm.smcode) as smname, (select sum(advafter.amount) from advafter where advafter.ordno = orderm.ordno) as advafter, (select sum(advafter.wgt) from advafter where advafter.ordno = orderm.ordno) as advafterwgt FROM orderm WHERE orderm.control <= :rlevel ORDER BY orderm.tdate ASC, orderm.slno ASC', 'computes': [], 'args': ['rordno', 'rlevel'], 'arg_types': {'rordno': 'string', 'rlevel': 'number'}, 'tables': ['orderm'], 'columns': [{'name': 'orderm_ordno', 'label': 'orderm_ordno', 'type': 'char'}, {'name': 'orderm_tdate', 'label': 'orderm_tdate', 'type': 'date'}, {'name': 'orderm_duedate', 'label': 'orderm_duedate', 'type': 'date'}, {'name': 'orderm_rate', 'label': 'orderm_rate', 'type': 'decimal'}, {'name': 'orderm_custname', 'label': 'orderm_custname', 'type': 'char'}, {'name': 'orderm_billamt', 'label': 'orderm_billamt', 'type': 'decimal'}, {'name': 'orderm_eamt', 'label': 'orderm_eamt', 'type': 'decimal'}, {'name': 'orderm_advance', 'label': 'orderm_advance', 'type': 'decimal'}, {'name': 'status', 'label': 'status', 'type': 'long'}, {'name': 'orderm_slno', 'label': 'orderm_slno', 'type': 'decimal'}, {'name': 'custcode', 'label': 'custcode', 'type': 'char'}, {'name': 'smname', 'label': 'smname', 'type': 'char'}, {'name': 'gadvance', 'label': 'gadvance', 'type': 'decimal'}, {'name': 'sretamt', 'label': 'sretamt', 'type': 'decimal'}, {'name': 'smcode', 'label': 'smcode', 'type': 'char'}, {'name': 'addr', 'label': 'addr', 'type': 'char'}, {'name': 'refund', 'label': 'refund', 'type': 'decimal'}, {'name': 'duedate_org', 'label': 'duedate_org', 'type': 'date'}, {'name': 'phone', 'label': 'phone', 'type': 'char'}, {'name': 'advafter', 'label': 'advafter', 'type': 'decimal'}, {'name': 'advafterwgt', 'label': 'advafterwgt', 'type': 'decimal'}]},
    opens=['w_orderhelp'],
)


class OrderEnquiryForm(GeneratedForm):
    """Order Enquiry"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('commandbutton', 'cb_3', 2459, 0, 261, 92, text='Save &As')
        self.add('commandbutton', 'cb_1', 2725, 0, 265, 92, text='&Print')
        self.add('commandbutton', 'cb_2', 2990, 0, 265, 92, text='E&xit')
        self.add('singlelineedit', 'sle_ordno', 288, 4, 654, 92, taborder=10)
        self.add('commandbutton', 'cb_show', 1257, 4, 261, 96, text='&Show', taborder=20)
        self.add('statictext', 'st_6', 46, 8, 233, 76, text='Ord No :')
        self.add('commandbutton', 'cb_help', 955, 12, 201, 80, text='&Help')
        self.add('datawindow', 'dw_1', 5, 104, 3442, 1928, dataobject='d_orderenquiry', taborder=30)
