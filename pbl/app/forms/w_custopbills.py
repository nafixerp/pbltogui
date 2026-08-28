"""Customers — w_custopbills.

Generated from the PowerBuilder window ``w_custopbills.srw`` by
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
    name='w_custopbills',
    title='Customers',
    width=4178,
    height=1664,
    controls=[],
    tables=['salesm', 'clients', 'accountm', 'generali'],
    source_path='w_custopbills.srw',
    grid={'control': 'dw_aloc', 'dataobject': 'd_custopbills', 'table': 'salesm', 'keys': ['slno'], 'computes': [{'name': 'balance', 'expression': '  if(isnull(billamt),0,billamt) -   if(isnull(ramt),0,ramt)  -  if(isnull(ramtafter),0,ramtafter) ', 'format': '[general]', 'label': 'balance', 'band': 'detail'}], 'columns': [{'name': 'billno', 'label': 'Bill No.', 'type': 'char'}, {'name': 'tdate', 'label': 'Date', 'type': 'date'}, {'name': 'grate', 'label': 'grate', 'type': 'decimal'}, {'name': 'billamt', 'label': 'billamt', 'type': 'decimal'}, {'name': 'ramt', 'label': 'ramt', 'type': 'decimal'}, {'name': 'ramtafter', 'label': 'ramtafter', 'type': 'decimal'}, {'name': 'dstatus', 'label': 'dstatus', 'type': 'char'}, {'name': 'secwgt', 'label': 'secwgt', 'type': 'decimal'}, {'name': 'secnote', 'label': 'secnote', 'type': 'char'}, {'name': 'custname', 'label': 'custname', 'type': 'char'}, {'name': 'eamt', 'label': 'eamt', 'type': 'decimal'}, {'name': 'staxamt', 'label': 'staxamt', 'type': 'decimal'}, {'name': 'discount', 'label': 'discount', 'type': 'decimal'}, {'name': 'duedate', 'label': 'duedate', 'type': 'date'}, {'name': 'sretamt', 'label': 'sretamt', 'type': 'decimal'}, {'name': 'slno', 'label': 'slno', 'type': 'decimal'}, {'name': 'alocamt', 'label': 'alocamt', 'type': 'decimal'}]},
    report={'dataobject': 'd_custopbills', 'sql': 'SELECT salesm.billno AS salesm_billno, salesm.tdate AS salesm_tdate, salesm.grate AS salesm_grate, salesm.billamt AS salesm_billamt, salesm.ramt AS salesm_ramt, salesm.ramtafter AS salesm_ramtafter, salesm.dstatus AS salesm_dstatus, salesm.secwgt AS salesm_secwgt, salesm.secnote AS salesm_secnote, salesm.custname AS salesm_custname, salesm.eamt AS salesm_eamt, salesm.staxamt AS salesm_staxamt, salesm.discount AS salesm_discount, salesm.duedate AS salesm_duedate, salesm.sretamt AS salesm_sretamt, salesm.slno AS salesm_slno, salesm.alocamt AS salesm_alocamt FROM salesm WHERE salesm.custcode = :rcode AND salesm.control <= :rlevel ORDER BY salesm.tdate ASC, salesm.slno ASC', 'computes': [{'name': 'balance', 'expression': '  if(isnull(billamt),0,billamt) -   if(isnull(ramt),0,ramt)  -  if(isnull(ramtafter),0,ramtafter) ', 'format': '[general]', 'label': 'balance', 'band': 'detail'}], 'args': ['rcode', 'rlevel'], 'arg_types': {'rcode': 'string', 'rlevel': 'number'}, 'tables': ['salesm'], 'columns': [{'name': 'billno', 'label': 'Bill No.', 'type': 'char'}, {'name': 'tdate', 'label': 'Date', 'type': 'date'}, {'name': 'grate', 'label': 'grate', 'type': 'decimal'}, {'name': 'billamt', 'label': 'billamt', 'type': 'decimal'}, {'name': 'ramt', 'label': 'ramt', 'type': 'decimal'}, {'name': 'ramtafter', 'label': 'ramtafter', 'type': 'decimal'}, {'name': 'dstatus', 'label': 'dstatus', 'type': 'char'}, {'name': 'secwgt', 'label': 'secwgt', 'type': 'decimal'}, {'name': 'secnote', 'label': 'secnote', 'type': 'char'}, {'name': 'custname', 'label': 'custname', 'type': 'char'}, {'name': 'eamt', 'label': 'eamt', 'type': 'decimal'}, {'name': 'staxamt', 'label': 'staxamt', 'type': 'decimal'}, {'name': 'discount', 'label': 'discount', 'type': 'decimal'}, {'name': 'duedate', 'label': 'duedate', 'type': 'date'}, {'name': 'sretamt', 'label': 'sretamt', 'type': 'decimal'}, {'name': 'slno', 'label': 'slno', 'type': 'decimal'}, {'name': 'alocamt', 'label': 'alocamt', 'type': 'decimal'}]},
    opens=['w_clientshelp'],
)


class CustomersForm(GeneratedForm):
    """Customers"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('datawindow', 'dw_code', 366, 28, 402, 88, dataobject='d_cust', taborder=10)
        self.add('statictext', 'st_name', 782, 36, 937, 84)
        self.add('statictext', 'st_4', 0, 44, 325, 76, text='Customer :')
        self.add('datawindow', 'dw_aloc', 0, 124, 4160, 1092, dataobject='d_custopbills', taborder=20)
        self.add('commandbutton', 'cb_add', 14, 1116, 247, 84, text='&Add', taborder=30)
        self.add('commandbutton', 'cb_delete', 265, 1116, 247, 84, text='&Delete', taborder=21)
        self.add('oval', 'oval_1', 1646, 1272, 686, 184)
        self.add('commandbutton', 'cb_save', 1746, 1316, 242, 96, text='&Save', taborder=40)
        self.add('commandbutton', 'cb_exit', 2002, 1316, 242, 96, text='E&xit', taborder=50)
