"""Customer Billwise Rcpt — w_custbillwisealoc.

Generated from the PowerBuilder window ``w_custbillwisealoc.srw`` by
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
    name='w_custbillwisealoc',
    title='Customer Billwise Rcpt',
    width=3666,
    height=2008,
    controls=[],
    tables=['salesm', 'daybook', 'collection', 'accountm', 'daybookratewgt', 'clients', 'generali', 'daybookpart'],
    source_path='w_custbillwisealoc.srw',
    grid={'control': 'dw_aloc', 'dataobject': 'd_salealoc', 'table': 'salesm', 'keys': ['slno'], 'columns': [{'name': 'tdate', 'label': 'Date', 'type': 'date'}, {'name': 'billno', 'label': 'Bill No.', 'type': 'char'}, {'name': 'billamt', 'label': 'billamt', 'type': 'decimal'}, {'name': 'eamt', 'label': 'eamt', 'type': 'decimal'}, {'name': 'staxamt', 'label': 'staxamt', 'type': 'decimal'}, {'name': 'discount', 'label': 'discount', 'type': 'decimal'}, {'name': 'ramt', 'label': 'ramt', 'type': 'decimal'}, {'name': 'ramtafter', 'label': 'ramtafter', 'type': 'decimal'}, {'name': 'duedate', 'label': 'Due Date', 'type': 'date'}, {'name': 'sretamt', 'label': 'sretamt', 'type': 'decimal'}, {'name': 'slno', 'label': 'slno', 'type': 'decimal'}, {'name': 'alocamt', 'label': 'alocamt', 'type': 'decimal'}, {'name': 'custname', 'label': 'custname', 'type': 'char'}, {'name': 'discamt', 'label': 'discamt', 'type': 'decimal'}, {'name': 'round', 'label': 'round', 'type': 'decimal'}, {'name': 'aloc', 'label': 'aloc', 'type': 'long'}, {'name': 'advance', 'label': 'advance', 'type': 'decimal'}, {'name': 'astamt', 'label': 'astamt', 'type': 'decimal'}, {'name': 'collectedamt', 'label': 'collectedamt', 'type': 'decimal'}, {'name': 'tdiscamt', 'label': 'tdiscamt', 'type': 'decimal'}, {'name': 'netamt', 'label': 'netamt', 'type': 'decimal'}, {'name': 'grate', 'label': 'grate', 'type': 'decimal'}, {'name': 'balwgt', 'label': 'balwgt', 'type': 'decimal'}]},
    report={'dataobject': 'd_salealoc', 'sql': 'SELECT salesm.tdate AS salesm_tdate, salesm.billno AS salesm_billno, salesm.billamt AS salesm_billamt, salesm.eamt AS salesm_eamt, salesm.staxamt AS salesm_staxamt, salesm.discount AS salesm_discount, salesm.ramt AS salesm_ramt, salesm.ramtafter AS salesm_ramtafter, salesm.duedate AS salesm_duedate, salesm.sretamt AS salesm_sretamt, salesm.slno AS salesm_slno, salesm.alocamt AS salesm_alocamt, salesm.custname AS salesm_custname, salesm.discamt AS salesm_discamt, salesm.round AS salesm_round, salesm.advance AS salesm_advance, salesm.astamt AS salesm_astamt, salesm.netamt AS salesm_netamt, salesm.grate AS salesm_grate, salesm.balwgt AS salesm_balwgt, 0 as aloc, (select sum(collection.tranamt) from collection where collection.islno = salesm.slno and collection.control <= :rlevel) as collectedamt, (select sum(collection.discount) from collection where collection.islno = salesm.slno and collection.control <= :rlevel) as tdiscamt FROM salesm WHERE salesm.custcode = :rcode AND salesm.control <= :rlevel ORDER BY salesm.tdate ASC, salesm.slno ASC', 'args': ['rcode', 'rlevel'], 'arg_types': {'rcode': 'string', 'rlevel': 'number'}, 'tables': ['salesm'], 'columns': [{'name': 'tdate', 'label': 'Date', 'type': 'date'}, {'name': 'billno', 'label': 'Bill No.', 'type': 'char'}, {'name': 'billamt', 'label': 'billamt', 'type': 'decimal'}, {'name': 'eamt', 'label': 'eamt', 'type': 'decimal'}, {'name': 'staxamt', 'label': 'staxamt', 'type': 'decimal'}, {'name': 'discount', 'label': 'discount', 'type': 'decimal'}, {'name': 'ramt', 'label': 'ramt', 'type': 'decimal'}, {'name': 'ramtafter', 'label': 'ramtafter', 'type': 'decimal'}, {'name': 'duedate', 'label': 'Due Date', 'type': 'date'}, {'name': 'sretamt', 'label': 'sretamt', 'type': 'decimal'}, {'name': 'slno', 'label': 'slno', 'type': 'decimal'}, {'name': 'alocamt', 'label': 'alocamt', 'type': 'decimal'}, {'name': 'custname', 'label': 'custname', 'type': 'char'}, {'name': 'discamt', 'label': 'discamt', 'type': 'decimal'}, {'name': 'round', 'label': 'round', 'type': 'decimal'}, {'name': 'aloc', 'label': 'aloc', 'type': 'long'}, {'name': 'advance', 'label': 'advance', 'type': 'decimal'}, {'name': 'astamt', 'label': 'astamt', 'type': 'decimal'}, {'name': 'collectedamt', 'label': 'collectedamt', 'type': 'decimal'}, {'name': 'tdiscamt', 'label': 'tdiscamt', 'type': 'decimal'}, {'name': 'netamt', 'label': 'netamt', 'type': 'decimal'}, {'name': 'grate', 'label': 'grate', 'type': 'decimal'}, {'name': 'balwgt', 'label': 'balwgt', 'type': 'decimal'}]},
    opens=['w_clientshelp'],
)


class CustomerBillwiseRcptForm(GeneratedForm):
    """Customer Billwise Rcpt"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('statictext', 'st_doc', 46, 0, 293, 84, text='Doc. No. :')
        self.add('statictext', 'st_docno', 366, 0, 402, 84)
        self.add('statictext', 'st_3', 1897, 0, 247, 84, text='Date :')
        self.add('editmask', 'em_date', 2167, 0, 398, 84, taborder=10)
        self.add('statictext', 'st_8', 2624, 0, 297, 80, text='GoldRate :')
        self.add('editmask', 'em_grate', 2930, 0, 398, 84, taborder=20)
        self.add('datawindow', 'dw_code', 366, 104, 402, 88, dataobject='d_cust', taborder=40)
        self.add('datawindow', 'dw_staff', 2930, 104, 677, 88, dataobject='d_smancode', taborder=30)
        self.add('statictext', 'st_name', 782, 112, 937, 84)
        self.add('statictext', 'st_balance', 2167, 112, 398, 84)
        self.add('statictext', 'st_7', 2624, 112, 297, 80, text='SMan :')
        self.add('statictext', 'st_4', 14, 120, 325, 76, text='Customer :')
        self.add('statictext', 'st_5', 1856, 120, 288, 76, text='Balance :')
        self.add('datawindow', 'dw_aloc', 0, 204, 3634, 1316, dataobject='d_salealoc', taborder=50)
        self.add('commandbutton', 'cb_2', 3314, 1536, 215, 92, text='Filter', taborder=100)
        self.add('singlelineedit', 'sle_filter', 2656, 1540, 654, 84, taborder=110)
        self.add('editmask', 'em_alocamt', 759, 1544, 384, 80, taborder=60)
        self.add('editmask', 'em_nonalocamt', 2176, 1544, 347, 80)
        self.add('statictext', 'st_1', 5, 1548, 722, 76, text='Total Amount to Allocate :')
        self.add('statictext', 'st_2', 1541, 1548, 617, 76, text='Non-Allocated Amt. :')
        self.add('oval', 'oval_1', 1019, 1616, 686, 184)
        self.add('singlelineedit', 'sle_part', 2176, 1640, 1134, 92, limit=40, taborder=70)
        self.add('checkbox', 'cbx_1', 105, 1648, 649, 76, text='Only Pending Bills')
        self.add('commandbutton', 'cb_ok', 1106, 1660, 242, 96, text='&Save', taborder=80)
        self.add('commandbutton', 'cb_exit', 1371, 1660, 242, 96, text='E&xit', taborder=90)
        self.add('statictext', 'st_6', 1778, 1664, 361, 76, text='Particulars :')
        self.add('checkbox', 'cbx_acupdt', 233, 1724, 521, 76, text="Don't update A/c")
        self.add('checkbox', 'cbx_print', 2176, 1744, 247, 76, text='Print')
        self.add('checkbox', 'cbx_showwgt', 2683, 1744, 690, 84, text='Show Wgt in Ledger')
