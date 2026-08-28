"""Bank Book — w_bankbookreport.

Generated from the PowerBuilder window ``w_bankbookreport.srw`` by
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
    name='w_bankbookreport',
    title='Bank Book',
    width=3648,
    height=2284,
    controls=[],
    tables=['accountm', 'daybook'],
    source_path='w_bankbookreport.srw',
    report={'dataobject': 'd_bankbook', 'sql': 'SELECT daybook.slno AS daybook_slno, daybook.tdate AS daybook_tdate, daybook.amount AS daybook_amount, daybookpart.vchno AS daybookpart_vchno, daybookpart.chequeno AS daybookpart_chequeno, daybookpart.particular AS daybookpart_particular, daybookpart.chequedate AS daybookpart_chequedate, (select name from accountm where accountm.accode = :rcode) as bankname, (select max(abs(dbk.amount)) from daybook dbk where dbk.slno = daybook.slno and dbk.accode <> :rcode ) as opacctamt, (select max(dbk.accode) from daybook dbk where dbk.slno = daybook.slno and dbk.accode <> :rcode and abs(dbk.amount) >= opacctamt) as opaccode, (select accountm.name from accountm where accountm.accode = opaccode ) as opacname FROM daybook, daybookpart WHERE daybook.slno = daybookpart.slno AND daybook.control <= :rlevel AND daybook.tdate >= :rdate1 AND daybook.accode = :rcode AND daybook.tdate <= :rdate2 ORDER BY daybook.tdate ASC, daybook.slno ASC', 'args': ['rdate1', 'rdate2', 'rcode', 'rlevel', 'ropbal'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date', 'rcode': 'string', 'rlevel': 'number', 'ropbal': 'decimal'}, 'tables': ['daybook', 'daybookpart'], 'columns': [{'name': 'daybook_slno', 'label': 'daybook_slno', 'type': 'decimal'}, {'name': 'daybook_tdate', 'label': 'daybook_tdate', 'type': 'date'}, {'name': 'daybook_amount', 'label': 'daybook_amount', 'type': 'decimal'}, {'name': 'daybookpart_vchno', 'label': 'daybookpart_vchno', 'type': 'char'}, {'name': 'daybookpart_chequeno', 'label': 'daybookpart_chequeno', 'type': 'char'}, {'name': 'cbankname', 'label': 'cbankname', 'type': 'char'}, {'name': 'daybookpart_particular', 'label': 'daybookpart_particular', 'type': 'char'}, {'name': 'copacctamt', 'label': 'copacctamt', 'type': 'decimal'}, {'name': 'copaccode', 'label': 'copaccode', 'type': 'char'}, {'name': 'copacname', 'label': 'copacname', 'type': 'char'}, {'name': 'daybookpart_chequedate', 'label': 'daybookpart_chequedate', 'type': 'date'}]},
)


class BankBookForm(GeneratedForm):
    """Bank Book"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('datawindow', 'dw_bank', 361, 0, 1010, 88, dataobject='d_bankcode', taborder=60)
        self.add('commandbutton', 'cb_show', 1431, 0, 261, 92, text='&Show')
        self.add('commandbutton', 'cb_print', 1733, 0, 265, 92, text='&Print')
        self.add('commandbutton', 'cb_saveas', 2514, 0, 265, 92, text='Save As')
        self.add('commandbutton', 'cb_sort', 2793, 0, 265, 92, text='So&rt')
        self.add('commandbutton', 'cb_filter', 3072, 0, 265, 92, text='&Filter')
        self.add('commandbutton', 'cb_exit', 3355, 0, 265, 92, text='E&xit')
        self.add('statictext', 'st_1', 41, 12, 315, 76, text='Bank A/c :')
        self.add('editmask', 'em_date1', 361, 96, 430, 92, taborder=20)
        self.add('editmask', 'em_date2', 928, 96, 443, 92, taborder=30)
        self.add('editmask', 'em_chqdate1', 2514, 96, 370, 92, taborder=40)
        self.add('editmask', 'em_chqdate2', 3250, 96, 370, 92, taborder=50)
        self.add('statictext', 'st_2', 5, 104, 352, 76, text='Date From :')
        self.add('statictext', 'st_3', 809, 104, 133, 76, text='To :')
        self.add('checkbox', 'cbx_withoutop', 1431, 108, 544, 76, text='Without Op Bal')
        self.add('statictext', 'st_8', 2021, 108, 485, 76, text='Chq Date From :')
        self.add('statictext', 'st_7', 3113, 108, 133, 76, text='To :')
        self.add('datawindow', 'dw_1', 0, 192, 3625, 1972, dataobject='d_bankbook', taborder=10)
