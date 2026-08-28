"""Group Ledger — w_acledger_group.

Generated from the PowerBuilder window ``w_acledger_group.srw`` by
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
    name='w_acledger_group',
    title='Group Ledger',
    width=3648,
    height=2260,
    controls=[],
    tables=['accountm', 'accountg', 'date', 'daybook'],
    source_path='w_acledger_group.srw',
    report={'dataobject': 'd_acledger_group', 'sql': 'SELECT daybook.tdate AS daybook_tdate, daybook.accode AS daybook_accode, daybook.amount AS daybook_amount, daybookpart.vchno AS daybookpart_vchno, daybook.slno AS daybook_slno, daybookpart.staff AS daybookpart_staff, daybookpart.particular AS daybookpart_particular, accountm.name AS accountm_name FROM daybook, daybookpart, accountm WHERE daybook.slno = daybookpart.slno AND daybook.accode = accountm.accode AND daybook.tdate between :rdate1 and :rdate2 AND daybook.control <= :rlevel ORDER BY daybook.tdate ASC, daybook.slno ASC', 'computes': [{'name': 'part', 'expression': "trim( daybookpart_particular) + if( daybookpart_staff <> '','->Staff->'+ daybookpart_staff,'' ) ", 'format': '[general]', 'label': 'part', 'band': 'detail'}, {'name': 'sdebitamt', 'expression': 'if(daybook_amount < 0,string(abs(daybook_amount),~"#######0.00~"),~"~")', 'format': '', 'label': 'sdebitamt', 'band': 'detail'}, {'name': 'screditamt', 'expression': 'if(daybook_amount > 0,string(daybook_amount,~"#######0.00~"),~"~")', 'format': '', 'label': 'screditamt', 'band': 'detail'}, {'name': 'compute_5', 'expression': 'abs( ropbal + cumulativeSum(   daybook_amount for all ))', 'format': '##########0.00', 'label': 'compute_5', 'band': 'detail'}, {'name': 'tdebitamt', 'expression': 'sum(dec(sdebitamt) for all)', 'format': '########0.00', 'label': 'tdebitamt', 'band': 'summary'}, {'name': 'tcreditamt', 'expression': 'sum(dec(screditamt) for all)', 'format': '########0.00', 'label': 'tcreditamt', 'band': 'summary'}, {'name': 'clbaldb', 'expression': 'if( ( ropbal  - tdebitamt + tcreditamt) < 0,abs(ropbal  - tdebitamt + tcreditamt),0)', 'format': '########0.00', 'label': 'clbaldb', 'band': 'summary'}, {'name': 'clbalcr', 'expression': 'if( ( ropbal  - tdebitamt + tcreditamt) > 0, abs(ropbal  - tdebitamt + tcreditamt),0)', 'format': '########0.00', 'label': 'clbalcr', 'band': 'summary'}], 'args': ['rdate1', 'rdate2', 'rlevel', 'rcode', 'racname', 'ropbal'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date', 'rlevel': 'number', 'rcode': 'string', 'racname': 'string', 'ropbal': 'decimal'}, 'tables': ['daybook', 'daybookpart', 'accountm'], 'columns': [{'name': 'daybook_tdate', 'label': 'daybook_tdate', 'type': 'date'}, {'name': 'daybook_accode', 'label': 'daybook_accode', 'type': 'char'}, {'name': 'daybook_amount', 'label': 'daybook_amount', 'type': 'decimal'}, {'name': 'daybookpart_vchno', 'label': 'daybookpart_vchno', 'type': 'char'}, {'name': 'daybook_slno', 'label': 'daybook_slno', 'type': 'decimal'}, {'name': 'daybookpart_staff', 'label': 'daybookpart_staff', 'type': 'char'}, {'name': 'daybookpart_particular', 'label': 'daybookpart_particular', 'type': 'char'}, {'name': 'accountm_name', 'label': 'accountm_name', 'type': 'char'}]},
    opens=['w_cbachdhelp', 'w_acledgerpopup'],
)


class GroupLedgerForm(GeneratedForm):
    """Group Ledger"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('datawindow', 'dw_grp', 334, 0, 1129, 96, dataobject='d_grcode', taborder=50)
        self.add('commandbutton', 'cb_show', 2080, 0, 261, 96, text='&Show', taborder=40)
        self.add('commandbutton', 'cb_sort', 2583, 0, 251, 96, text='So&rt', taborder=41)
        self.add('commandbutton', 'cb_saveas', 2848, 0, 251, 96, text='Save &As', taborder=70)
        self.add('commandbutton', 'cb_print', 3113, 0, 251, 96, text='&Print', taborder=80)
        self.add('commandbutton', 'cb_exit', 3378, 0, 251, 96, text='E&xit', taborder=60)
        self.add('statictext', 'st_4', 5, 8, 329, 72, text='A/c Group :')
        self.add('checkbox', 'cbx_summary', 1600, 8, 402, 80, text='Summary')
        self.add('editmask', 'em_date1', 334, 100, 398, 92, taborder=20)
        self.add('editmask', 'em_date2', 1070, 100, 393, 92, taborder=30)
        self.add('datawindow', 'dw_accode', 2075, 100, 430, 88, dataobject='d_accode', taborder=10)
        self.add('statictext', 'st_1', 137, 108, 197, 64, text='From :')
        self.add('statictext', 'st_2', 864, 108, 187, 72, text='To :')
        self.add('statictext', 'st_3', 1751, 108, 311, 72, text='A/c Code :')
        self.add('checkbox', 'cbx_noob', 2583, 112, 421, 80, text='No OB Print')
        self.add('checkbox', 'cbx_dosprint', 3118, 112, 288, 76, text='Speed')
        self.add('datawindow', 'dw_1', 0, 192, 3616, 1976, dataobject='d_acledger_group', taborder=50)
        self.add('checkbox', 'cbx_showpreview', 2583, 200, 421, 80, text='Show Preview')
        self.add('checkbox', 'cbx_condense', 3118, 200, 329, 76, text='Condense')
