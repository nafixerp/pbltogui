"""Non Transactional Days Report — w_nontransactionaldays_report.

Generated from the PowerBuilder window ``w_nontransactionaldays_report.srw`` by
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
    name='w_nontransactionaldays_report',
    title='Non Transactional Days Report',
    width=1829,
    height=2004,
    controls=[],
    tables=['daybook', 'accountm', 'smithm', 'clients'],
    source_path='w_nontransactionaldays_report.srw',
)


class NonTransactionalDaysReportForm(GeneratedForm):
    """Non Transactional Days Report"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 201, 0, 457, 96, taborder=40)
        self.add('editmask', 'em_date2', 795, 0, 457, 96, taborder=1)
        self.add('commandbutton', 'cb_show', 1257, 0, 265, 96, text='&Show', taborder=30)
        self.add('commandbutton', 'cb_print', 1541, 0, 265, 96, text='&Print', taborder=140)
        self.add('statictext', 'st_date1', 0, 8, 197, 80, text='From :')
        self.add('statictext', 'st_date2', 658, 8, 133, 80, text='To :')
        self.add('commandbutton', 'cb_setup', 197, 100, 265, 88, text='Setup', taborder=110)
        self.add('commandbutton', 'cb_saveas', 457, 100, 265, 88, text='Save As', taborder=100)
        self.add('commandbutton', 'cb_sort', 718, 100, 265, 88, text='So&rt', taborder=90)
        self.add('commandbutton', 'cb_filter', 978, 100, 265, 88, text='&Filter', taborder=20)
        self.add('commandbutton', 'cb_exit', 1541, 100, 265, 88, text='E&xit', taborder=10)
        self.add('datawindow', 'dw_1', 9, 196, 1806, 1700, dataobject='d_nontransactionaldays_rep', taborder=130)
