"""A/c Ledger — w_acledger.

Generated from the PowerBuilder window ``w_acledger.srw`` by
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
    name='w_acledger',
    title='A/c Ledger',
    width=3648,
    height=2336,
    controls=[],
    tables=['daybook', 'accountm', 'clients_kuridet', 'clients', 'date', 'salesm', 'purchasem', 'salesrm', 'purchaserm', 'smithm', 'refinerym', 'advafter', 'orderdga', 'daybookpart', 'userd'],
    source_path='w_acledger.srw',
    report={'dataobject': 'd_acledger', 'sql': 'SELECT daybook.tdate AS daybook_tdate, daybook.accode AS daybook_accode, daybook.amount AS daybook_amount, daybookpart.vchno AS daybookpart_vchno, daybook.slno AS daybook_slno, daybookpart.staff AS daybookpart_staff, daybookpart.particular AS daybookpart_particular, daybookpart.slno2 AS daybookpart_slno2, (select accountm.name from accountm where accountm.accode = daybook.opaccode) as othacname FROM daybook, daybookpart WHERE daybook.slno = daybookpart.slno AND daybook.tdate between :rdate1 and :rdate2 AND daybook.control <= :rlevel AND daybook.accode = :rcode ORDER BY daybook.tdate ASC, daybook.slno ASC', 'computes': [{'name': 'part', 'expression': "trim( daybookpart_particular) + if( daybookpart_staff <> '','->Staff->'+ daybookpart_staff,'' ) ", 'format': '[general]', 'label': 'part', 'band': 'detail'}, {'name': 'sdebitamt', 'expression': 'if(daybook_amount < 0,string(abs(daybook_amount),~"#######0.00~"),~"~")', 'format': '', 'label': 'sdebitamt', 'band': 'detail'}, {'name': 'screditamt', 'expression': 'if(daybook_amount > 0,string(daybook_amount,~"#######0.00~"),~"~")', 'format': '', 'label': 'screditamt', 'band': 'detail'}, {'name': 'compute_5', 'expression': 'abs( ropbal + cumulativeSum(   daybook_amount for all ))', 'format': '##########0.00', 'label': 'compute_5', 'band': 'detail'}, {'name': 'tdebitamt', 'expression': 'sum(dec(sdebitamt) for all)', 'format': '########0.00', 'label': 'tdebitamt', 'band': 'summary'}, {'name': 'tcreditamt', 'expression': 'sum(dec(screditamt) for all)', 'format': '########0.00', 'label': 'tcreditamt', 'band': 'summary'}, {'name': 'clbaldb', 'expression': 'if( ( ropbal  - tdebitamt + tcreditamt) < 0,abs(ropbal  - tdebitamt + tcreditamt),0)', 'format': '########0.00', 'label': 'clbaldb', 'band': 'summary'}, {'name': 'clbalcr', 'expression': 'if( ( ropbal  - tdebitamt + tcreditamt) > 0, abs(ropbal  - tdebitamt + tcreditamt),0)', 'format': '########0.00', 'label': 'clbalcr', 'band': 'summary'}], 'args': ['rdate1', 'rdate2', 'rlevel', 'rcode', 'racname', 'ropbal'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date', 'rlevel': 'number', 'rcode': 'string', 'racname': 'string', 'ropbal': 'decimal'}, 'tables': ['daybook', 'daybookpart'], 'columns': [{'name': 'daybook_tdate', 'label': 'daybook_tdate', 'type': 'date'}, {'name': 'daybook_accode', 'label': 'daybook_accode', 'type': 'char'}, {'name': 'daybook_amount', 'label': 'daybook_amount', 'type': 'decimal'}, {'name': 'daybookpart_vchno', 'label': 'daybookpart_vchno', 'type': 'char'}, {'name': 'daybook_slno', 'label': 'daybook_slno', 'type': 'decimal'}, {'name': 'daybookpart_staff', 'label': 'daybookpart_staff', 'type': 'char'}, {'name': 'daybookpart_particular', 'label': 'daybookpart_particular', 'type': 'char'}, {'name': 'daybookpart_slno2', 'label': 'daybookpart_slno2', 'type': 'decimal'}, {'name': 'othacname', 'label': 'othacname', 'type': 'char'}]},
    opens=['w_acsusphelp', 'w_cbachdhelp'],
)


class ACLedgerForm(GeneratedForm):
    """A/c Ledger"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 1015, 0, 443, 92, taborder=20)
        self.add('editmask', 'em_date2', 1609, 0, 439, 92, taborder=30)
        self.add('dropdownlistbox', 'ddlb_type', 2066, 0, 343, 400, text='Ordinary', items=['Ordinary', 'With Wgt', 'With Rate'], taborder=20)
        self.add('commandbutton', 'cb_show', 2459, 0, 210, 96, text='&Show', taborder=40)
        self.add('commandbutton', 'cb_sort', 2747, 0, 210, 96, text='So&rt')
        self.add('commandbutton', 'cb_saveas', 2967, 0, 210, 96, text='Save &As', taborder=70)
        self.add('commandbutton', 'cb_print', 3186, 0, 210, 96, text='&Print', taborder=80)
        self.add('commandbutton', 'cb_exit', 3401, 0, 210, 96, text='E&xit', taborder=60)
        self.add('datawindow', 'dw_accode', 329, 4, 430, 88, dataobject='d_accode', taborder=10)
        self.add('statictext', 'st_3', 9, 8, 311, 72, text='A/c Code :')
        self.add('statictext', 'st_1', 777, 8, 224, 64, text='From :')
        self.add('statictext', 'st_2', 1445, 8, 146, 72, text='To :')
        self.add('commandbutton', 'cb_filter', 763, 88, 206, 96, text='Filter', taborder=30)
        self.add('commandbutton', 'cb_linkac', 1006, 92, 453, 92, text='Show Link Acc', taborder=30)
        self.add('singlelineedit', 'sle_search', 329, 96, 430, 88, taborder=20)
        self.add('commandbutton', 'cb_suspalloc', 2066, 100, 343, 76, text='Susp Alloc')
        self.add('checkbox', 'cbx_susppendonly', 1504, 104, 521, 72, text='Susp.Pending Only')
        self.add('commandbutton', 'cb_del', 2459, 104, 210, 72, text='Del')
        self.add('checkbox', 'cbx_noob', 2734, 104, 421, 80, text='No OB Print')
        self.add('checkbox', 'cbx_dosprint', 3191, 104, 288, 76, text='Speed')
        self.add('statictext', 'st_4', 14, 108, 329, 72, text='Filter(Desc) :')
        self.add('datawindow', 'dw_1', 0, 184, 3616, 2056, dataobject='d_acledger', taborder=50)
        self.add('checkbox', 'cbx_showpreview', 2734, 188, 421, 80, text='Show Preview')
        self.add('checkbox', 'cbx_condense', 3191, 188, 329, 76, text='Condense')
        self.add('commandbutton', 'cb_toexcel', 2734, 272, 265, 92, text='To Excel', taborder=40)
