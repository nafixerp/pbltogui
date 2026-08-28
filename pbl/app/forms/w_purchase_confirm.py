"""Confirmation — w_purchase_confirm.

Generated from the PowerBuilder window ``w_purchase_confirm.srw`` by
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
    name='w_purchase_confirm',
    title='Confirmation',
    width=3369,
    height=1540,
    controls=[],
    tables=['purchasem', 'items', 'daybook', 'itemsstk', 'purchaserm', 'stkandprofit', 'purchased', 'advafter', 'pdclist', 'purchaserd', 'oglist', 'userd', 'delpart', 'daybookpart'],
    source_path='w_purchase_confirm.srw',
    grid={'control': 'dw_1', 'dataobject': 'd_purchase_confirm', 'table': 'purchasem', 'keys': ['slno'], 'columns': [{'name': 'docno', 'label': 'Doc. No.', 'type': 'char'}, {'name': 'tdate', 'label': 'Date', 'type': 'date'}, {'name': 'billno', 'label': 'billno', 'type': 'char'}, {'name': 'name', 'label': 'Party Name', 'type': 'char'}, {'name': 'billamt', 'label': 'Bill Amt.', 'type': 'decimal'}, {'name': 'netamt', 'label': 'netamt', 'type': 'decimal'}, {'name': 'pamt', 'label': 'pamt', 'type': 'decimal'}, {'name': 'slno', 'label': 'slno', 'type': 'decimal'}, {'name': 'dmd', 'label': 'dmd', 'type': 'char'}]},
    report={'dataobject': 'd_purchase_confirm', 'sql': "SELECT purchasem.docno AS purchasem_docno, purchasem.tdate AS purchasem_tdate, purchasem.billno AS purchasem_billno, purchasem.name AS purchasem_name, purchasem.billamt AS purchasem_billamt, purchasem.netamt AS purchasem_netamt, purchasem.pamt AS purchasem_pamt, purchasem.slno AS purchasem_slno, purchasem.dmd AS purchasem_dmd FROM purchasem WHERE purchasem.control = 4 AND purchasem.pr = 'P' ORDER BY purchasem.tdate ASC, purchasem.slno ASC, purchasem.docno ASC", 'args': [], 'arg_types': {}, 'tables': ['purchasem'], 'columns': [{'name': 'docno', 'label': 'Doc. No.', 'type': 'char'}, {'name': 'tdate', 'label': 'Date', 'type': 'date'}, {'name': 'billno', 'label': 'billno', 'type': 'char'}, {'name': 'name', 'label': 'Party Name', 'type': 'char'}, {'name': 'billamt', 'label': 'Bill Amt.', 'type': 'decimal'}, {'name': 'netamt', 'label': 'netamt', 'type': 'decimal'}, {'name': 'pamt', 'label': 'pamt', 'type': 'decimal'}, {'name': 'slno', 'label': 'slno', 'type': 'decimal'}, {'name': 'dmd', 'label': 'dmd', 'type': 'char'}]},
    opens=['w_tran_view'],
)


class ConfirmationForm(GeneratedForm):
    """Confirmation"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('datawindow', 'dw_1', 0, 0, 3337, 1272, dataobject='d_purchase_confirm', taborder=10)
        self.add('statictext', 'st_search', 27, 1184, 416, 76)
        self.add('commandbutton', 'cb_refresh', 1207, 1304, 366, 120, text='Refresh', taborder=40)
        self.add('commandbutton', 'cb_ok', 1595, 1304, 366, 120, text='Confirm', taborder=20)
        self.add('commandbutton', 'cb_cancel', 2043, 1304, 366, 120, text='Exit', taborder=30)
        self.add('commandbutton', 'cb_delete', 677, 1316, 434, 108, text='&Delete', taborder=50)
