"""Credit Bill Details — w_partycreditbills.

Generated from the PowerBuilder window ``w_partycreditbills.srw`` by
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
    name='w_partycreditbills',
    title='Credit Bill Details',
    width=3680,
    height=2256,
    controls=[],
    tables=['accountm'],
    source_path='w_partycreditbills.srw',
    grid={'control': 'dw_saleregister', 'dataobject': 'd_salesbook_creditonly', 'table': 'salesm', 'keys': ['slno'], 'columns': [{'name': 'slno', 'label': 'salesm_slno', 'type': 'decimal'}, {'name': 'tdate', 'label': 'salesm_tdate', 'type': 'date'}, {'name': 'billno', 'label': 'salesm_billno', 'type': 'char'}, {'name': 'custname', 'label': 'salesm_custname', 'type': 'char'}, {'name': 'billamt', 'label': 'salesm_billamt', 'type': 'decimal'}, {'name': 'status', 'label': 'salesm_status', 'type': 'long'}, {'name': 'control', 'label': 'salesm_control', 'type': 'long'}, {'name': 'discount', 'label': 'salesm_discount', 'type': 'decimal'}, {'name': 'ramt', 'label': 'salesm_ramt', 'type': 'decimal'}, {'name': 'eamt', 'label': 'salesm_eamt', 'type': 'decimal'}, {'name': 'staxamt', 'label': 'salesm_staxamt', 'type': 'decimal'}, {'name': 'duedate', 'label': 'salesm_duedate', 'type': 'date'}, {'name': 'sretamt', 'label': 'salesm_sretamt', 'type': 'decimal'}, {'name': 'ramtafter', 'label': 'salesm_ramtafter', 'type': 'decimal'}, {'name': 'custadd1', 'label': 'custadd1', 'type': 'char'}, {'name': 'custadd2', 'label': 'custadd2', 'type': 'char'}, {'name': 'smcode', 'label': 'smcode', 'type': 'char'}, {'name': 'custadd3', 'label': 'custadd3', 'type': 'char'}, {'name': 'custcode', 'label': 'custcode', 'type': 'char'}, {'name': 'rcvdafter', 'label': 'rcvdafter', 'type': 'decimal'}, {'name': 'cocode', 'label': 'cocode', 'type': 'char'}, {'name': 'round', 'label': 'round', 'type': 'decimal'}, {'name': 'netamt', 'label': 'netamt', 'type': 'decimal'}, {'name': 'advance', 'label': 'advance', 'type': 'decimal'}, {'name': 'custphone', 'label': 'custphone', 'type': 'char'}, {'name': 'astamt', 'label': 'astamt', 'type': 'decimal'}, {'name': 'ctype', 'label': 'ctype', 'type': 'char'}]},
    report={'dataobject': 'd_salesbook_creditonly', 'sql': 'SELECT salesm.slno AS salesm_slno, salesm.tdate AS salesm_tdate, salesm.billno AS salesm_billno, salesm.custname AS salesm_custname, salesm.billamt AS salesm_billamt, salesm.status AS salesm_status, salesm.control AS salesm_control, salesm.discount AS salesm_discount, salesm.ramt AS salesm_ramt, salesm.eamt AS salesm_eamt, salesm.staxamt AS salesm_staxamt, salesm.duedate AS salesm_duedate, salesm.sretamt AS salesm_sretamt, salesm.ramtafter AS salesm_ramtafter, salesm.smcode AS salesm_smcode, salesm.custcode AS salesm_custcode, salesm.cocode AS salesm_cocode, salesm.round AS salesm_round, salesm.netamt AS salesm_netamt, salesm.advance AS salesm_advance, salesm.astamt AS salesm_astamt, (select clients.addr1 from clients where clients.code = salesm.custcode) as custadd1, (select clients.addr2 from clients where clients.code = salesm.custcode) as custadd2, (select clients.addr3 from clients where clients.code = salesm.custcode) as custadd3, (select sum(collection.tranamt + collection.discount) from collection where collection.billno = salesm.billno and collection.code = salesm.custcode ) as rcvdafter, (select clients.telephone from clients where clients.code = salesm.custcode) as custphone, (select clients.ctype from clients where clients.code = salesm.custcode) as ctype FROM salesm WHERE salesm.tdate between :rdate1 and :rdate2 AND salesm.control <= :rlevel ORDER BY salesm.status ASC, salesm.tdate ASC, salesm.slno ASC', 'args': ['rdate1', 'rdate2', 'rlevel', 'rtype'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date', 'rlevel': 'number', 'rtype': 'number'}, 'tables': ['salesm'], 'columns': [{'name': 'salesm_slno', 'label': 'salesm_slno', 'type': 'decimal'}, {'name': 'salesm_tdate', 'label': 'salesm_tdate', 'type': 'date'}, {'name': 'salesm_billno', 'label': 'salesm_billno', 'type': 'char'}, {'name': 'salesm_custname', 'label': 'salesm_custname', 'type': 'char'}, {'name': 'salesm_billamt', 'label': 'salesm_billamt', 'type': 'decimal'}, {'name': 'salesm_status', 'label': 'salesm_status', 'type': 'long'}, {'name': 'salesm_control', 'label': 'salesm_control', 'type': 'long'}, {'name': 'salesm_discount', 'label': 'salesm_discount', 'type': 'decimal'}, {'name': 'salesm_ramt', 'label': 'salesm_ramt', 'type': 'decimal'}, {'name': 'salesm_eamt', 'label': 'salesm_eamt', 'type': 'decimal'}, {'name': 'salesm_staxamt', 'label': 'salesm_staxamt', 'type': 'decimal'}, {'name': 'salesm_duedate', 'label': 'salesm_duedate', 'type': 'date'}, {'name': 'salesm_sretamt', 'label': 'salesm_sretamt', 'type': 'decimal'}, {'name': 'salesm_ramtafter', 'label': 'salesm_ramtafter', 'type': 'decimal'}, {'name': 'custadd1', 'label': 'custadd1', 'type': 'char'}, {'name': 'custadd2', 'label': 'custadd2', 'type': 'char'}, {'name': 'smcode', 'label': 'smcode', 'type': 'char'}, {'name': 'custadd3', 'label': 'custadd3', 'type': 'char'}, {'name': 'custcode', 'label': 'custcode', 'type': 'char'}, {'name': 'rcvdafter', 'label': 'rcvdafter', 'type': 'decimal'}, {'name': 'cocode', 'label': 'cocode', 'type': 'char'}, {'name': 'round', 'label': 'round', 'type': 'decimal'}, {'name': 'netamt', 'label': 'netamt', 'type': 'decimal'}, {'name': 'advance', 'label': 'advance', 'type': 'decimal'}, {'name': 'custphone', 'label': 'custphone', 'type': 'char'}, {'name': 'astamt', 'label': 'astamt', 'type': 'decimal'}, {'name': 'ctype', 'label': 'ctype', 'type': 'char'}]},
)


class CreditBillDetailsForm(GeneratedForm):
    """Credit Bill Details"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 370, 0, 384, 92, taborder=10)
        self.add('editmask', 'em_date2', 1115, 0, 384, 92, taborder=20)
        self.add('dropdownlistbox', 'ddlb_ptype', 1522, 0, 352, 400, text='Customers', items=['Customers', 'Suppliers', 'All'], taborder=50)
        self.add('commandbutton', 'cb_show', 2011, 0, 293, 92, text='&Show', taborder=40)
        self.add('checkbox', 'cbx_netbal', 2469, 0, 352, 76, text='Net Balance')
        self.add('commandbutton', 'cb_1', 2862, 0, 270, 92, text='Save &As', taborder=90)
        self.add('commandbutton', 'cb_print', 3136, 0, 233, 92, text='&Print', taborder=70)
        self.add('commandbutton', 'cb_exit', 3374, 0, 233, 92, text='E&xit', taborder=80)
        self.add('statictext', 'st_11', 809, 12, 302, 72, text='Date To :')
        self.add('statictext', 'st_10', 0, 20, 361, 64, text='Date From :')
        self.add('dropdownlistbox', 'ddlb_sort', 1115, 100, 731, 576, text='Date', items=['Customer', 'Date', 'Bill No', 'Balance', 'Due Date'], taborder=50)
        self.add('commandbutton', 'cb_fulladdr', 2862, 100, 507, 92, text='Full Address', taborder=51)
        self.add('datawindow', 'dw_accode', 370, 104, 402, 88, dataobject='d_cust', taborder=30)
        self.add('datawindow', 'dw_co', 2016, 104, 402, 88, dataobject='d_cust', taborder=41)
        self.add('checkbox', 'cbx_purchase', 2469, 108, 343, 80, text='Purchase')
        self.add('statictext', 'st_4', 832, 112, 256, 76, text='Sort On :')
        self.add('statictext', 'st_3', 41, 116, 325, 76, text='Customer :')
        self.add('statictext', 'st_16', 1870, 120, 137, 76, text='C/o :')
        self.add('datawindow', 'dw_saleregister', 0, 196, 3625, 2032, dataobject='d_salesbook_creditonly', taborder=60)
