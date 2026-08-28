"""Purchase Check List — w_purhchklist.

Generated from the PowerBuilder window ``w_purhchklist.srw`` by
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
    name='w_purhchklist',
    title='Purchase Check List',
    width=3616,
    height=2288,
    controls=[],
    tables=[],
    source_path='w_purhchklist.srw',
    grid={'control': 'dw_purhchklist', 'dataobject': 'd_pchecklist', 'table': 'purchasem', 'keys': ['slno'], 'computes': [], 'columns': [{'name': 'slno', 'label': 'slno', 'type': 'decimal'}, {'name': 'tdate', 'label': 'tdate', 'type': 'date'}, {'name': 'ttime', 'label': 'ttime', 'type': 'time'}, {'name': 'billno', 'label': 'billno', 'type': 'char'}, {'name': 'docno', 'label': 'docno', 'type': 'char'}, {'name': 'suppcode', 'label': 'suppcode', 'type': 'char'}, {'name': 'name', 'label': 'name', 'type': 'char'}, {'name': 'billamt', 'label': 'billamt', 'type': 'decimal'}, {'name': 'pamt', 'label': 'pamt', 'type': 'decimal'}, {'name': 'addamt', 'label': 'addamt', 'type': 'decimal'}, {'name': 'eamt', 'label': 'eamt', 'type': 'decimal'}, {'name': 'duedate', 'label': 'duedate', 'type': 'date'}, {'name': 'smname', 'label': 'smname', 'type': 'char'}, {'name': 'pan', 'label': 'pan', 'type': 'char'}, {'name': 'addr', 'label': 'addr', 'type': 'char'}]},
    report={'dataobject': 'd_pchecklist', 'sql': "SELECT purchasem.slno AS purchasem_slno, purchasem.tdate AS purchasem_tdate, purchasem.ttime AS purchasem_ttime, purchasem.billno AS purchasem_billno, purchasem.docno AS purchasem_docno, purchasem.suppcode AS purchasem_suppcode, purchasem.name AS purchasem_name, purchasem.billamt AS purchasem_billamt, purchasem.pamt AS purchasem_pamt, purchasem.addamt AS purchasem_addamt, purchasem.eamt AS purchasem_eamt, purchasem.duedate AS purchasem_duedate, purchasem.pan AS purchasem_pan, purchasem.addr AS purchasem_addr, (select name from sman where sman.code = purchasem.smcode) as smname FROM purchasem WHERE purchasem.tdate between :rdate1 and :rdate2 AND purchasem.control <= :rlevel AND purchasem.pr = 'P' ORDER BY purchasem.tdate ASC, purchasem.slno ASC", 'computes': [], 'args': ['rdate1', 'rdate2', 'rlevel'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date', 'rlevel': 'number'}, 'tables': ['purchasem'], 'columns': [{'name': 'slno', 'label': 'slno', 'type': 'decimal'}, {'name': 'tdate', 'label': 'tdate', 'type': 'date'}, {'name': 'ttime', 'label': 'ttime', 'type': 'time'}, {'name': 'billno', 'label': 'billno', 'type': 'char'}, {'name': 'docno', 'label': 'docno', 'type': 'char'}, {'name': 'suppcode', 'label': 'suppcode', 'type': 'char'}, {'name': 'name', 'label': 'name', 'type': 'char'}, {'name': 'billamt', 'label': 'billamt', 'type': 'decimal'}, {'name': 'pamt', 'label': 'pamt', 'type': 'decimal'}, {'name': 'addamt', 'label': 'addamt', 'type': 'decimal'}, {'name': 'eamt', 'label': 'eamt', 'type': 'decimal'}, {'name': 'duedate', 'label': 'duedate', 'type': 'date'}, {'name': 'smname', 'label': 'smname', 'type': 'char'}, {'name': 'pan', 'label': 'pan', 'type': 'char'}, {'name': 'addr', 'label': 'addr', 'type': 'char'}]},
    opens=['w_clientshelp'],
)


class PurchaseCheckListForm(GeneratedForm):
    """Purchase Check List"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 375, 0, 384, 92, taborder=10)
        self.add('editmask', 'em_date2', 1143, 0, 384, 92, taborder=20)
        self.add('commandbutton', 'cb_show', 2427, 0, 261, 96, text='&Show', taborder=40)
        self.add('commandbutton', 'cb_print', 2976, 0, 283, 96, text='&Print', taborder=70)
        self.add('commandbutton', 'cb_exit', 3269, 0, 283, 96, text='E&xit', taborder=60)
        self.add('datawindow', 'dw_1', 1934, 8, 421, 88, dataobject='d_supp', taborder=30)
        self.add('statictext', 'st_2', 823, 12, 302, 72, text='Date To :')
        self.add('statictext', 'st_4', 1623, 12, 297, 76, text='Supplier :')
        self.add('statictext', 'st_1', 0, 20, 361, 64, text='Date From :')
        self.add('datawindow', 'dw_purhchklist', 0, 104, 3584, 2044, dataobject='d_pchecklist', taborder=50)
