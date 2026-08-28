"""Suspense A/c Ledger — w_suspledger.

Generated from the PowerBuilder window ``w_suspledger.srw`` by
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
    name='w_suspledger',
    title='Suspense A/c Ledger',
    width=3666,
    height=2352,
    controls=[],
    tables=['daybook', 'accountm', 'date', 'suspentry', 'suspac', 'clients'],
    source_path='w_suspledger.srw',
    report={'dataobject': 'd_suspledger_entrybal', 'sql': 'SELECT suspentry.amount AS suspentry_amount, suspentry.pend AS suspentry_pend, suspentry.scode AS suspentry_scode, suspentry.tdate AS suspentry_tdate, suspentry.note AS suspentry_note, suspentry.vchno AS suspentry_vchno, (select suspac.name from suspac where suspac.code = suspentry.scode ) as suspacname, (select sum(se.amount) from suspentry se where se.pslno = suspentry.slno ) as totrcpt FROM suspentry ORDER BY suspentry.accode ASC, suspentry.tdate ASC, suspentry.slno ASC', 'args': ['rdate1', 'rdate2', 'rlevel', 'rcode', 'racname', 'ropbal'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date', 'rlevel': 'number', 'rcode': 'string', 'racname': 'string', 'ropbal': 'decimal'}, 'tables': ['suspentry'], 'columns': [{'name': 'suspacname', 'label': 'suspacname', 'type': 'char'}, {'name': 'totrcpt', 'label': 'totrcpt', 'type': 'decimal'}, {'name': 'suspentry_amount', 'label': 'suspentry_amount', 'type': 'decimal'}, {'name': 'suspentry_pend', 'label': 'suspentry_pend', 'type': 'char'}, {'name': 'suspentry_scode', 'label': 'suspentry_scode', 'type': 'char'}, {'name': 'suspentry_tdate', 'label': 'suspentry_tdate', 'type': 'date'}, {'name': 'suspentry_note', 'label': 'suspentry_note', 'type': 'char'}, {'name': 'suspentry_vchno', 'label': 'suspentry_vchno', 'type': 'char'}]},
    opens=['w_susp_totmp', 'w_cbachdhelp'],
)


class SuspenseACLedgerForm(GeneratedForm):
    """Suspense A/c Ledger"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 1070, 0, 398, 92, taborder=20)
        self.add('editmask', 'em_date2', 1760, 0, 393, 92, taborder=30)
        self.add('commandbutton', 'cb_show', 2350, 0, 261, 92, text='&Show', taborder=40)
        self.add('commandbutton', 'cb_sort', 2606, 0, 261, 92, text='So&rt')
        self.add('commandbutton', 'cb_saveas', 2875, 0, 251, 92, text='Save &As', taborder=70)
        self.add('commandbutton', 'cb_print', 3127, 0, 251, 92, text='&Print', taborder=80)
        self.add('commandbutton', 'cb_exit', 3378, 0, 238, 92, text='E&xit', taborder=60)
        self.add('datawindow', 'dw_accode', 334, 4, 430, 88, dataobject='d_accode', taborder=10)
        self.add('statictext', 'st_3', 9, 8, 311, 72, text='A/c Code :')
        self.add('statictext', 'st_1', 823, 8, 242, 64, text='From :')
        self.add('statictext', 'st_2', 1614, 8, 137, 72, text='To :')
        self.add('datawindow', 'dw_scode', 334, 96, 1138, 88, dataobject='d_suspcode', taborder=20)
        self.add('dropdownlistbox', 'ddlb_type', 1760, 96, 553, 400, text='Entry Bal Summary', items=['Detail', 'Entry Bal Summary', 'Susp.Bal Summary'], taborder=30)
        self.add('commandbutton', 'cb_suspalloc', 2350, 96, 517, 88, text='Susp Alloc')
        self.add('statictext', 'st_5', 1554, 100, 192, 72, text='Type :')
        self.add('statictext', 'st_4', 5, 104, 315, 72, text='Susp A/c :')
        self.add('checkbox', 'cbx_scode', 1481, 104, 78, 76)
        self.add('checkbox', 'cbx_noob', 2885, 112, 421, 80, text='No OB Print')
        self.add('checkbox', 'cbx_dosprint', 3342, 112, 288, 76, text='Speed')
        self.add('datawindow', 'dw_1', 0, 188, 3616, 2064, dataobject='d_suspledger_entrybal', taborder=50)
        self.add('checkbox', 'cbx_showpreview', 2885, 192, 421, 80, text='Show Preview')
        self.add('checkbox', 'cbx_susppendonly', 2359, 196, 517, 72, text='Susp.Pending Only')
        self.add('checkbox', 'cbx_condense', 2885, 264, 329, 76, text='Condense')
