"""A/c Summary — w_acsummary.

Generated from the PowerBuilder window ``w_acsummary.srw`` by
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
    name='w_acsummary',
    title='A/c Summary',
    width=3657,
    height=2292,
    controls=[],
    tables=['clients_kuridet', 'accountm', 'daybook', 'date'],
    source_path='w_acsummary.srw',
    report={'dataobject': 'd_acsumm', 'sql': 'SELECT daybook.tdate AS daybook_tdate, daybook.accode AS daybook_accode, daybook.amount AS daybook_amount, daybookpart.vchno AS daybookpart_vchno, daybookpart.particular AS daybookpart_particular, daybook.slno AS daybook_slno, daybookpart.staff AS daybookpart_staff FROM daybook, daybookpart WHERE daybook.slno = daybookpart.slno AND daybook.tdate between :rdate1 and :rdate2 AND daybook.control <= :rlevel ORDER BY daybook.tdate ASC, daybook.slno ASC', 'args': ['rdate1', 'rdate2', 'rlevel', 'rcode', 'racname', 'ropbal'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date', 'rlevel': 'number', 'rcode': 'string', 'racname': 'string', 'ropbal': 'decimal'}, 'tables': ['daybook', 'daybookpart'], 'columns': [{'name': 'daybook_tdate', 'label': 'daybook_tdate', 'type': 'date'}, {'name': 'daybook_accode', 'label': 'daybook_accode', 'type': 'char'}, {'name': 'daybook_amount', 'label': 'daybook_amount', 'type': 'decimal'}, {'name': 'daybookpart_vchno', 'label': 'daybookpart_vchno', 'type': 'char'}, {'name': 'daybookpart_particular', 'label': 'daybookpart_particular', 'type': 'char'}, {'name': 'daybook_slno', 'label': 'daybook_slno', 'type': 'decimal'}, {'name': 'daybookpart_staff', 'label': 'daybookpart_staff', 'type': 'char'}]},
    opens=['w_clientshelp'],
)


class ACSummaryForm(GeneratedForm):
    """A/c Summary"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('commandbutton', 'cb_show', 2345, 0, 261, 100, text='&Show', taborder=40)
        self.add('commandbutton', 'cb_saveas', 2706, 0, 261, 100, text='Save &As', taborder=70)
        self.add('commandbutton', 'cb_print', 3035, 0, 256, 100, text='&Print', taborder=80)
        self.add('commandbutton', 'cb_exit', 3369, 0, 256, 100, text='E&xit', taborder=60)
        self.add('editmask', 'em_date1', 1184, 4, 421, 92, taborder=20)
        self.add('editmask', 'em_date2', 1925, 4, 416, 92, taborder=30)
        self.add('datawindow', 'dw_accode', 347, 8, 425, 88, dataobject='d_accode', taborder=10)
        self.add('statictext', 'st_2', 1618, 12, 283, 72, text='Date To :')
        self.add('statictext', 'st_3', 0, 16, 338, 72, text='A/c Code :')
        self.add('statictext', 'st_1', 805, 16, 366, 64, text='Date From :')
        self.add('datawindow', 'dw_1', 0, 104, 3634, 2068, dataobject='d_acsumm', taborder=50)
        self.add('commandbutton', 'cb_linkac', 1934, 112, 453, 92, text='Show Link Acc', taborder=20)
        self.add('commandbutton', 'cb_sort', 2706, 112, 261, 88, text='So&rt', taborder=71)
        self.add('checkbox', 'cbx_dosprint', 3035, 116, 297, 88, text='Speed')
