"""Journal — w_journrpt.

Generated from the PowerBuilder window ``w_journrpt.srw`` by
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
    name='w_journrpt',
    title='Journal',
    width=3685,
    height=2240,
    controls=[],
    tables=[],
    source_path='w_journrpt.srw',
    report={'dataobject': 'd_journrpt', 'sql': 'SELECT daybook.slno AS daybook_slno, daybook.tdate AS daybook_tdate, daybook.accode AS daybook_accode, daybook.amount AS daybook_amount, daybookpart.vchno AS daybookpart_vchno, accountm.name AS accountm_name, daybookpart.particular AS daybookpart_particular FROM accountm, daybook, daybookpart WHERE accountm.accode = daybook.accode AND daybook.slno = daybookpart.slno AND daybook.control <= :rlevel AND daybook.tdate >= :rDate1 ORDER BY daybook.tdate ASC, daybookpart.vchno ASC', 'args': ['rlevel', 'rDate1', 'rDate2'], 'arg_types': {'rlevel': 'number', 'rDate1': 'date', 'rDate2': 'date'}, 'tables': ['accountm', 'daybook', 'daybookpart'], 'columns': [{'name': 'daybook_slno', 'label': 'daybook_slno', 'type': 'decimal'}, {'name': 'daybook_tdate', 'label': 'daybook_tdate', 'type': 'date'}, {'name': 'daybook_accode', 'label': 'daybook_accode', 'type': 'char'}, {'name': 'daybook_amount', 'label': 'daybook_amount', 'type': 'decimal'}, {'name': 'daybookpart_vchno', 'label': 'daybookpart_vchno', 'type': 'char'}, {'name': 'accountm_name', 'label': 'accountm_name', 'type': 'char'}, {'name': 'daybookpart_particular', 'label': 'daybookpart_particular', 'type': 'char'}]},
)


class JournalForm(GeneratedForm):
    """Journal"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 439, 0, 430, 100, taborder=10)
        self.add('editmask', 'em_date2', 1326, 0, 425, 100, taborder=20)
        self.add('commandbutton', 'cb_show', 1929, 0, 261, 92, text='&Show', taborder=30)
        self.add('commandbutton', 'cb_reprint', 2254, 0, 265, 92, text='Reprint', taborder=40)
        self.add('commandbutton', 'cb_1', 2866, 0, 233, 92, text='&Print', taborder=60)
        self.add('commandbutton', 'cb_2', 3369, 0, 238, 92, text='E&xit', taborder=50)
        self.add('statictext', 'st_1', 9, 12, 411, 76, text='Date  From :')
        self.add('statictext', 'st_2', 933, 12, 366, 72, text='Date To :')
        self.add('datawindow', 'dw_1', 0, 116, 3616, 1972, dataobject='d_journrpt', taborder=40)
