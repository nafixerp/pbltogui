"""Purchase Book — w_purhbook.

Generated from the PowerBuilder window ``w_purhbook.srw`` by
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
    name='w_purhbook',
    title='Purchase Book',
    width=3721,
    height=2256,
    controls=[],
    tables=['items', 'purchasem', 'itemsstk', 'purchased', 'salesd', 'salesrd', 'salesm', 'barcode', 'salesrm', 'daybook', 'salestype', 'generali', 'daybookpart', 'generals'],
    source_path='w_purhbook.srw',
    grid={'control': 'dw_saleregister', 'dataobject': 'd_purhbook', 'table': 'purchasem', 'keys': ['slno'], 'computes': [{'name': 'netamt2', 'expression': 'netamt', 'format': '######0.00', 'label': 'netamt2', 'band': 'detail'}, {'name': 'balance', 'expression': 'netamt  -  pamt ', 'format': '######0.00', 'label': 'balance', 'band': 'detail'}, {'name': 'compute_14', 'expression': 'sum( balance for all)', 'format': '#####0.00', 'label': 'compute_14', 'band': 'summary'}, {'name': 'compute_11', 'expression': 'sum(billamt for all)', 'format': '######0.00', 'label': 'compute_11', 'band': 'summary'}, {'name': 'compute_12', 'expression': 'sum( netamt2  for all)', 'format': '#####0.00', 'label': 'compute_12', 'band': 'summary'}, {'name': 'compute_13', 'expression': 'sum(pamt for all)', 'format': '#####0.00', 'label': 'compute_13', 'band': 'summary'}], 'columns': [{'name': 'tdate', 'label': 'tdate', 'type': 'date'}, {'name': 'docno', 'label': 'docno', 'type': 'char'}, {'name': 'name', 'label': 'name', 'type': 'char'}, {'name': 'billamt', 'label': 'billamt', 'type': 'decimal'}, {'name': 'addamt', 'label': 'addamt', 'type': 'decimal'}, {'name': 'pamt', 'label': 'pamt', 'type': 'decimal'}, {'name': 'eamt', 'label': 'eamt', 'type': 'decimal'}, {'name': 'status', 'label': 'status', 'type': 'long'}, {'name': 'duedate', 'label': 'duedate', 'type': 'date'}, {'name': 'slno', 'label': 'slno', 'type': 'decimal'}, {'name': 'smcode', 'label': 'smcode', 'type': 'char'}, {'name': 'pr', 'label': 'pr', 'type': 'char'}, {'name': 'ic', 'label': 'ic', 'type': 'char'}, {'name': 'counter', 'label': 'counter', 'type': 'char'}, {'name': 'netamt', 'label': 'netamt', 'type': 'decimal'}, {'name': 'billtype', 'label': 'billtype', 'type': 'char'}]},
    report={'dataobject': 'd_purhbook', 'sql': 'SELECT purchasem.tdate AS purchasem_tdate, purchasem.docno AS purchasem_docno, purchasem.name AS purchasem_name, purchasem.billamt AS purchasem_billamt, purchasem.addamt AS purchasem_addamt, purchasem.pamt AS purchasem_pamt, purchasem.eamt AS purchasem_eamt, purchasem.status AS purchasem_status, purchasem.duedate AS purchasem_duedate, purchasem.slno AS purchasem_slno, purchasem.smcode AS purchasem_smcode, purchasem.pr AS purchasem_pr, purchasem.ic AS purchasem_ic, purchasem.counter AS purchasem_counter, purchasem.netamt AS purchasem_netamt, purchasem.billtype AS purchasem_billtype FROM purchasem WHERE purchasem.tdate between :rdate1 and :rdate2 AND purchasem.control <= :rlevel ORDER BY purchasem.status ASC, purchasem.tdate ASC, purchasem.docno ASC', 'computes': [{'name': 'netamt2', 'expression': 'netamt', 'format': '######0.00', 'label': 'netamt2', 'band': 'detail'}, {'name': 'balance', 'expression': 'netamt  -  pamt ', 'format': '######0.00', 'label': 'balance', 'band': 'detail'}, {'name': 'compute_14', 'expression': 'sum( balance for all)', 'format': '#####0.00', 'label': 'compute_14', 'band': 'summary'}, {'name': 'compute_11', 'expression': 'sum(billamt for all)', 'format': '######0.00', 'label': 'compute_11', 'band': 'summary'}, {'name': 'compute_12', 'expression': 'sum( netamt2  for all)', 'format': '#####0.00', 'label': 'compute_12', 'band': 'summary'}, {'name': 'compute_13', 'expression': 'sum(pamt for all)', 'format': '#####0.00', 'label': 'compute_13', 'band': 'summary'}], 'args': ['rdate1', 'rdate2', 'rlevel'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date', 'rlevel': 'number'}, 'tables': ['purchasem'], 'columns': [{'name': 'tdate', 'label': 'tdate', 'type': 'date'}, {'name': 'docno', 'label': 'docno', 'type': 'char'}, {'name': 'name', 'label': 'name', 'type': 'char'}, {'name': 'billamt', 'label': 'billamt', 'type': 'decimal'}, {'name': 'addamt', 'label': 'addamt', 'type': 'decimal'}, {'name': 'pamt', 'label': 'pamt', 'type': 'decimal'}, {'name': 'eamt', 'label': 'eamt', 'type': 'decimal'}, {'name': 'status', 'label': 'status', 'type': 'long'}, {'name': 'duedate', 'label': 'duedate', 'type': 'date'}, {'name': 'slno', 'label': 'slno', 'type': 'decimal'}, {'name': 'smcode', 'label': 'smcode', 'type': 'char'}, {'name': 'pr', 'label': 'pr', 'type': 'char'}, {'name': 'ic', 'label': 'ic', 'type': 'char'}, {'name': 'counter', 'label': 'counter', 'type': 'char'}, {'name': 'netamt', 'label': 'netamt', 'type': 'decimal'}, {'name': 'billtype', 'label': 'billtype', 'type': 'char'}]},
    opens=['w_purchase_vat_print'],
)


class PurchaseBookForm(GeneratedForm):
    """Purchase Book"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 247, 0, 430, 92, taborder=10)
        self.add('editmask', 'em_date2', 1275, 0, 425, 92, taborder=20)
        self.add('dropdownlistbox', 'ddlb_pe', 1723, 0, 494, 532, text='All', items=['All', 'Purchase Only', 'Exchange Only'], taborder=60)
        self.add('commandbutton', 'cb_show', 2226, 0, 297, 96, text='&Show', taborder=30)
        self.add('commandbutton', 'cb_sort', 2519, 0, 297, 92, text='So&rt', taborder=40)
        self.add('commandbutton', 'cb_1', 2811, 0, 297, 92, text='Save &As', taborder=110)
        self.add('commandbutton', 'cb_print', 3104, 0, 297, 92, text='&Print', taborder=100)
        self.add('commandbutton', 'cb_exit', 3401, 0, 297, 92, text='E&xit', taborder=120)
        self.add('statictext', 'st_1', 9, 8, 238, 64, text='From')
        self.add('statictext', 'st_2', 1029, 12, 233, 76, text='Date To')
        self.add('datawindow', 'dw_ic', 247, 96, 695, 88, dataobject='d_incharge_code', taborder=50)
        self.add('datawindow', 'dw_billtype', 1275, 96, 425, 88, dataobject='d_billtypecode', taborder=101)
        self.add('commandbutton', 'cb_frupdt', 2226, 96, 297, 96, text='Fr Updt', taborder=91)
        self.add('commandbutton', 'cb_selall', 2519, 96, 297, 96, text='Select All', taborder=81)
        self.add('commandbutton', 'cb_delete', 2811, 96, 297, 96, text='Delete', taborder=80)
        self.add('commandbutton', 'cb_rearrange', 3104, 96, 297, 96, text='Rearrange', taborder=70)
        self.add('commandbutton', 'cb_reprint', 3401, 96, 297, 96, text='Reprint', taborder=91)
        self.add('checkbox', 'cbx_ic', 946, 100, 87, 76)
        self.add('statictext', 'st_9', 9, 104, 247, 80, text='Incharge')
        self.add('statictext', 'st_4', 1033, 104, 238, 68, text='Bill Type')
        self.add('datawindow', 'dw_counter', 247, 184, 658, 88, dataobject='d_countercode', taborder=101)
        self.add('statictext', 'st_3', 9, 192, 247, 76, text='Counter')
        self.add('checkbox', 'cbx_register', 1275, 192, 320, 76, text='Register')
        self.add('checkbox', 'cbx_taxrep', 1723, 192, 398, 84, text='Tax Report')
        self.add('checkbox', 'cbx_counter', 919, 196, 87, 76)
        self.add('datawindow', 'dw_saleregister', 0, 276, 3698, 1852, dataobject='d_purhbook', taborder=90)
