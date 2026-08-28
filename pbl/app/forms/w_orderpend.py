"""Pending Details — w_orderpend.

Generated from the PowerBuilder window ``w_orderpend.srw`` by
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
    name='w_orderpend',
    title='Pending Details',
    width=3643,
    height=2232,
    controls=[],
    tables=[],
    source_path='w_orderpend.srw',
    grid={'control': 'dw_1', 'dataobject': 'd_orderpend', 'table': 'orderm', 'keys': ['slno'], 'columns': [{'name': 'ordno', 'label': 'orderm_ordno', 'type': 'char'}, {'name': 'tdate', 'label': 'orderm_tdate', 'type': 'date'}, {'name': 'duedate', 'label': 'orderm_duedate', 'type': 'date'}, {'name': 'rate', 'label': 'orderm_rate', 'type': 'decimal'}, {'name': 'slno', 'label': 'orderm_slno', 'type': 'decimal'}, {'name': 'custname', 'label': 'orderm_custname', 'type': 'char'}, {'name': 'billamt', 'label': 'orderm_billamt', 'type': 'decimal'}, {'name': 'eamt', 'label': 'orderm_eamt', 'type': 'decimal'}, {'name': 'advance', 'label': 'orderm_advance', 'type': 'decimal'}, {'name': 'smname', 'label': 'smname', 'type': 'char'}, {'name': 'gadvance', 'label': 'gadvance', 'type': 'decimal'}, {'name': 'smcode', 'label': 'smcode', 'type': 'char'}, {'name': 'sretamt', 'label': 'sretamt', 'type': 'decimal'}, {'name': 'refund', 'label': 'refund', 'type': 'decimal'}, {'name': 'advaft', 'label': 'advaft', 'type': 'decimal'}, {'name': 'addr', 'label': 'addr', 'type': 'char'}, {'name': 'orderm_counter', 'label': 'orderm_counter', 'type': 'char'}]},
    report={'dataobject': 'd_orderpend', 'sql': 'SELECT orderm.ordno AS orderm_ordno, orderm.tdate AS orderm_tdate, orderm.duedate AS orderm_duedate, orderm.rate AS orderm_rate, orderm.slno AS orderm_slno, orderm.custname AS orderm_custname, orderm.billamt AS orderm_billamt, orderm.eamt AS orderm_eamt, orderm.advance AS orderm_advance, orderm.gadvance AS orderm_gadvance, orderm.smcode AS orderm_smcode, orderm.sretamt AS orderm_sretamt, orderm.refund AS orderm_refund, orderm.addr AS orderm_addr, (select name from sman where code = orderm.smcode) as smname, (select sum(amount) from advafter where advafter.ordno = orderm.ordno) as advaft, (orderm.counter) as orderm_counter FROM orderm WHERE orderm.control <= :rlevel ORDER BY orderm.duedate ASC, orderm.slno ASC', 'args': ['rlevel', 'rdate1', 'rdate2'], 'arg_types': {'rlevel': 'number', 'rdate1': 'date', 'rdate2': 'date'}, 'tables': ['orderm'], 'columns': [{'name': 'orderm_ordno', 'label': 'orderm_ordno', 'type': 'char'}, {'name': 'orderm_tdate', 'label': 'orderm_tdate', 'type': 'date'}, {'name': 'orderm_duedate', 'label': 'orderm_duedate', 'type': 'date'}, {'name': 'orderm_rate', 'label': 'orderm_rate', 'type': 'decimal'}, {'name': 'orderm_slno', 'label': 'orderm_slno', 'type': 'decimal'}, {'name': 'orderm_custname', 'label': 'orderm_custname', 'type': 'char'}, {'name': 'orderm_billamt', 'label': 'orderm_billamt', 'type': 'decimal'}, {'name': 'orderm_eamt', 'label': 'orderm_eamt', 'type': 'decimal'}, {'name': 'orderm_advance', 'label': 'orderm_advance', 'type': 'decimal'}, {'name': 'smname', 'label': 'smname', 'type': 'char'}, {'name': 'gadvance', 'label': 'gadvance', 'type': 'decimal'}, {'name': 'smcode', 'label': 'smcode', 'type': 'char'}, {'name': 'sretamt', 'label': 'sretamt', 'type': 'decimal'}, {'name': 'refund', 'label': 'refund', 'type': 'decimal'}, {'name': 'advaft', 'label': 'advaft', 'type': 'decimal'}, {'name': 'addr', 'label': 'addr', 'type': 'char'}, {'name': 'orderm_counter', 'label': 'orderm_counter', 'type': 'char'}]},
)


class PendingDetailsForm(GeneratedForm):
    """Pending Details"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 411, 0, 443, 92, taborder=10)
        self.add('editmask', 'em_date2', 1157, 0, 411, 92, taborder=20)
        self.add('datawindow', 'dw_smcode', 1925, 0, 677, 88, dataobject='d_smancode', taborder=50)
        self.add('commandbutton', 'cb_show', 2610, 0, 261, 100, text='&Show', taborder=40)
        self.add('commandbutton', 'cb_3', 2871, 0, 274, 100, text='Save &As', taborder=80)
        self.add('commandbutton', 'cb_1', 3141, 0, 251, 100, text='&Print', taborder=90)
        self.add('commandbutton', 'cb_2', 3383, 0, 251, 100, text='E&xit', taborder=70)
        self.add('statictext', 'st_2', 969, 4, 160, 72, text='To')
        self.add('statictext', 'st_8', 14, 12, 393, 64, text='Entry From')
        self.add('statictext', 'st_1', 1710, 12, 210, 76, text='SMan :')
        self.add('statictext', 'st_3', 1609, 88, 311, 76, text='Order No :')
        self.add('singlelineedit', 'sle_billno', 1925, 92, 379, 84, taborder=30)
        self.add('commandbutton', 'cb_hlp', 2313, 92, 183, 80, text='&Help')
        self.add('editmask', 'em_ddate1', 411, 96, 443, 92, taborder=10)
        self.add('editmask', 'em_ddate2', 1157, 96, 411, 92, taborder=20)
        self.add('statictext', 'st_4', 14, 108, 411, 64, text='Due Dt From')
        self.add('statictext', 'st_5', 969, 108, 160, 72, text='To')
        self.add('checkbox', 'cbx_all', 2619, 108, 247, 76, text='All')
        self.add('datawindow', 'dw_1', 0, 192, 3630, 1928, dataobject='d_orderpend', taborder=60)
