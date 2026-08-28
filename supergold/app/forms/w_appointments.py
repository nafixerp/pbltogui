"""Appointment — w_appointments.

Generated from the PowerBuilder window ``w_appointments.srw`` by
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
    name='w_appointments',
    title='Appointment',
    width=2569,
    height=1284,
    controls=[],
    tables=['appoint', 'generali'],
    source_path='w_appointments.srw',
    report={'dataobject': 'd_appoint', 'sql': 'SELECT appoint.tdatetime AS appoint_tdatetime, appoint.desc AS appoint_desc, appoint.slno AS appoint_slno FROM appoint ORDER BY appoint.tdatetime ASC', 'computes': [], 'args': [], 'arg_types': {}, 'tables': ['appoint'], 'columns': [{'name': 'tdatetime', 'label': 'Date and Time', 'type': 'datetime'}, {'name': 'desc', 'label': 'Description', 'type': 'char'}, {'name': 'slno', 'label': 'slno', 'type': 'decimal'}]},
)


class AppointmentForm(GeneratedForm):
    """Appointment"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_today', 78, 0, 325, 88)
        self.add('statictext', 'st_1', 1015, 24, 581, 100, text='Appointments')
        self.add('commandbutton', 'cb_first', 2107, 48, 306, 108, text='&First', taborder=10)
        self.add('datawindow', 'dw_1', 73, 120, 2002, 1020, dataobject='d_appoint', taborder=20)
        self.add('commandbutton', 'cb_print', 1687, 124, 242, 80, text='Print', taborder=30)
        self.add('commandbutton', 'cb_last', 2107, 164, 306, 108, text='&Last', taborder=50)
        self.add('commandbutton', 'cb_prev', 2107, 288, 306, 108, text='&Previous', taborder=100)
        self.add('editmask', 'em_date', 718, 292, 475, 100, taborder=40)
        self.add('statictext', 'st_2', 69, 308, 622, 76, text='Appointment Date :')
        self.add('commandbutton', 'cb_next', 2107, 404, 306, 108, text='Nex&t', taborder=110)
        self.add('editmask', 'em_time', 718, 424, 475, 100, taborder=60)
        self.add('statictext', 'st_3', 78, 444, 613, 76, text='Appointment Time :')
        self.add('commandbutton', 'cb_1', 2107, 536, 306, 108, text='L&ist', taborder=120)
        self.add('multilineedit', 'mle_desc', 718, 564, 1262, 448, taborder=70)
        self.add('statictext', 'st_4', 315, 572, 375, 76, text='Description :')
        self.add('commandbutton', 'cb_new', 2107, 672, 306, 108, text='&New', taborder=80)
        self.add('commandbutton', 'cb_delete', 2107, 788, 306, 108, text='&Delete', taborder=90)
        self.add('commandbutton', 'cb_save', 2107, 904, 306, 108, text='&Save', taborder=140)
        self.add('commandbutton', 'cb_exit', 2107, 1016, 306, 108, text='E&xit', taborder=130)
