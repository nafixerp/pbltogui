"""Supplier Billwise Payment — w_suppbillwisealoc.

Generated from the PowerBuilder window ``w_suppbillwisealoc.srw`` by
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
    name='w_suppbillwisealoc',
    title='Supplier Billwise Payment',
    width=3657,
    height=1928,
    controls=[],
    tables=['daybook', 'accountm', 'collection', 'purchasem', 'clients', 'generali', 'daybookpart'],
    source_path='w_suppbillwisealoc.srw',
    grid={'control': 'dw_aloc', 'dataobject': 'd_purhaloc', 'table': 'purchasem', 'keys': ['slno'], 'columns': [{'name': 'tdate', 'label': 'Date', 'type': 'date'}, {'name': 'duedate', 'label': 'Due Date', 'type': 'date'}, {'name': 'docno', 'label': 'docno', 'type': 'char'}, {'name': 'billamt', 'label': 'billamt', 'type': 'decimal'}, {'name': 'pamt', 'label': 'pamt', 'type': 'decimal'}, {'name': 'addamt', 'label': 'addamt', 'type': 'decimal'}, {'name': 'eamt', 'label': 'eamt', 'type': 'decimal'}, {'name': 'pamtafter', 'label': 'pamtafter', 'type': 'decimal'}, {'name': 'aloc', 'label': 'aloc', 'type': 'long'}, {'name': 'slno', 'label': 'slno', 'type': 'decimal'}, {'name': 'collectedamt', 'label': 'collectedamt', 'type': 'decimal'}, {'name': 'alocamt', 'label': 'alocamt', 'type': 'decimal'}, {'name': 'tdiscamt', 'label': 'tdiscamt', 'type': 'decimal'}, {'name': 'discamt', 'label': 'discamt', 'type': 'decimal'}, {'name': 'netamt', 'label': 'netamt', 'type': 'decimal'}, {'name': 'name', 'label': 'name', 'type': 'char'}]},
    report={'dataobject': 'd_purhaloc', 'sql': 'SELECT purchasem.tdate AS purchasem_tdate, purchasem.duedate AS purchasem_duedate, purchasem.docno AS purchasem_docno, purchasem.billamt AS purchasem_billamt, purchasem.pamt AS purchasem_pamt, purchasem.addamt AS purchasem_addamt, purchasem.eamt AS purchasem_eamt, purchasem.pamtafter AS purchasem_pamtafter, purchasem.slno AS purchasem_slno, purchasem.alocamt AS purchasem_alocamt, purchasem.discamt AS purchasem_discamt, purchasem.netamt AS purchasem_netamt, purchasem.name AS purchasem_name, 0 as aloc, (select sum(collection.tranamt) from collection where collection.islno = purchasem.slno and collection.control <= :rlevel) as collectedamt, (select sum(collection.discount) from collection where collection.islno = purchasem.slno and collection.control <= :rlevel) as tdiscamt FROM purchasem WHERE purchasem.suppcode = :rcode AND purchasem.control <= :rlevel ORDER BY purchasem.tdate ASC, purchasem.slno ASC', 'args': ['rcode', 'rlevel'], 'arg_types': {'rcode': 'string', 'rlevel': 'number'}, 'tables': ['purchasem'], 'columns': [{'name': 'tdate', 'label': 'Date', 'type': 'date'}, {'name': 'duedate', 'label': 'Due Date', 'type': 'date'}, {'name': 'docno', 'label': 'docno', 'type': 'char'}, {'name': 'billamt', 'label': 'billamt', 'type': 'decimal'}, {'name': 'pamt', 'label': 'pamt', 'type': 'decimal'}, {'name': 'addamt', 'label': 'addamt', 'type': 'decimal'}, {'name': 'eamt', 'label': 'eamt', 'type': 'decimal'}, {'name': 'pamtafter', 'label': 'pamtafter', 'type': 'decimal'}, {'name': 'aloc', 'label': 'aloc', 'type': 'long'}, {'name': 'slno', 'label': 'slno', 'type': 'decimal'}, {'name': 'collectedamt', 'label': 'collectedamt', 'type': 'decimal'}, {'name': 'alocamt', 'label': 'alocamt', 'type': 'decimal'}, {'name': 'tdiscamt', 'label': 'tdiscamt', 'type': 'decimal'}, {'name': 'discamt', 'label': 'discamt', 'type': 'decimal'}, {'name': 'netamt', 'label': 'netamt', 'type': 'decimal'}, {'name': 'name', 'label': 'name', 'type': 'char'}]},
)


class SupplierBillwisePaymentForm(GeneratedForm):
    """Supplier Billwise Payment"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('statictext', 'st_doc', 32, 0, 293, 84, text='Doc. No. :')
        self.add('statictext', 'st_docno', 366, 0, 402, 84)
        self.add('statictext', 'st_3', 1070, 0, 247, 84, text='Date :')
        self.add('editmask', 'em_date', 1335, 0, 398, 84, taborder=10)
        self.add('datawindow', 'dw_cashbank', 2185, 0, 878, 88, dataobject='d_cashbankcode', taborder=20)
        self.add('statictext', 'st_8', 1806, 8, 357, 76, text='Cash/Bank :')
        self.add('datawindow', 'dw_staff', 2930, 104, 677, 88, dataobject='d_smancode', taborder=20)
        self.add('datawindow', 'dw_code', 366, 112, 425, 84, dataobject='d_supp', taborder=30)
        self.add('statictext', 'st_name', 795, 112, 937, 84)
        self.add('statictext', 'st_balance', 2185, 112, 398, 84)
        self.add('statictext', 'st_7', 2624, 112, 297, 80, text='SMan :')
        self.add('statictext', 'st_4', 0, 120, 325, 76, text='Supplier :')
        self.add('statictext', 'st_5', 1874, 120, 288, 76, text='Balance :')
        self.add('datawindow', 'dw_aloc', 5, 204, 3621, 1316, dataobject='d_purhaloc', taborder=40)
        self.add('commandbutton', 'cb_2', 3314, 1536, 215, 92, text='Filter', taborder=90)
        self.add('editmask', 'em_alocamt', 759, 1544, 384, 84, taborder=50)
        self.add('editmask', 'em_nonalocamt', 2176, 1544, 347, 84)
        self.add('singlelineedit', 'sle_filter', 2656, 1544, 654, 84, taborder=100)
        self.add('statictext', 'st_1', 5, 1548, 722, 76, text='Total Amount to Allocate :')
        self.add('statictext', 'st_2', 1541, 1548, 617, 76, text='Non-Allocated Amt. :')
        self.add('oval', 'oval_1', 1056, 1624, 686, 184)
        self.add('singlelineedit', 'sle_part', 2176, 1640, 1134, 92, limit=40, taborder=60)
        self.add('checkbox', 'cbx_1', 105, 1648, 649, 76, text='Only Pending Bills')
        self.add('statictext', 'st_6', 1778, 1664, 361, 76, text='Particulars :')
        self.add('commandbutton', 'cb_ok', 1143, 1668, 242, 96, text='&Save', taborder=70)
        self.add('commandbutton', 'cb_exit', 1408, 1668, 242, 96, text='E&xit', taborder=80)
        self.add('checkbox', 'cbx_acupdt', 233, 1724, 521, 76, text="Don't update A/c")
        self.add('checkbox', 'cbx_print', 2176, 1744, 247, 76, text='Print')
