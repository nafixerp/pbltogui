"""Attendance Report — w_staff_attendance_rep.

Generated from the PowerBuilder window ``w_staff_attendance_rep.srw`` by
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
    name='w_staff_attendance_rep',
    title='Attendance Report',
    width=3246,
    height=2360,
    controls=[],
    tables=[],
    source_path='w_staff_attendance_rep.srw',
    report={'dataobject': 'd_staff_attendancerep_details', 'sql': 'SELECT clients.name AS clients_name, clients.addr1 AS clients_addr1, clients.addr2 AS clients_addr2, clients.addr3 AS clients_addr3, clients.code AS clients_code, staffcheckin.tdate AS staffcheckin_tdate, staffcheckin.ttime AS staffcheckin_ttime, staffcheckin.stat AS staffcheckin_stat, clients.idno AS clients_idno FROM clients, staffcheckin WHERE clients.code = staffcheckin.code ORDER BY staffcheckin.tdate ASC, staffcheckin.ttime ASC, clients.name ASC', 'args': ['rdate1', 'rdate2'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date'}, 'tables': ['clients', 'staffcheckin'], 'columns': [{'name': 'clients_name', 'label': 'clients_name', 'type': 'char'}, {'name': 'clients_addr1', 'label': 'clients_addr1', 'type': 'char'}, {'name': 'clients_addr2', 'label': 'clients_addr2', 'type': 'char'}, {'name': 'clients_addr3', 'label': 'clients_addr3', 'type': 'char'}, {'name': 'clients_code', 'label': 'clients_code', 'type': 'char'}, {'name': 'staffcheckin_tdate', 'label': 'staffcheckin_tdate', 'type': 'date'}, {'name': 'staffcheckin_ttime', 'label': 'staffcheckin_ttime', 'type': 'time'}, {'name': 'staffcheckin_stat', 'label': 'staffcheckin_stat', 'type': 'long'}, {'name': 'clients_idno', 'label': 'clients_idno', 'type': 'long'}]},
    opens=['w_clientshelp'],
)


class AttendanceReportForm(GeneratedForm):
    """Attendance Report"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 242, 0, 411, 92, taborder=10)
        self.add('editmask', 'em_date2', 1248, 0, 411, 92, taborder=20)
        self.add('commandbutton', 'cb_show', 2144, 0, 261, 92, text='&Show', taborder=40)
        self.add('commandbutton', 'cb_saveas', 2427, 0, 265, 92, text='Save &As', taborder=40)
        self.add('commandbutton', 'cb_1', 2715, 0, 238, 92, text='&Print', taborder=70)
        self.add('commandbutton', 'cb_2', 2958, 0, 238, 92, text='E&xit', taborder=60)
        self.add('statictext', 'st_dt1', 32, 8, 201, 76, text='From :')
        self.add('statictext', 'st_dt2', 1079, 12, 151, 76, text='To :')
        self.add('dropdownlistbox', 'ddlb_type', 1248, 92, 759, 400, text='Details', items=['Details', 'Summary'], taborder=40)
        self.add('datawindow', 'dw_accode', 242, 96, 402, 88, dataobject='d_staffcode', taborder=30)
        self.add('statictext', 'st_2', 1038, 104, 192, 76, text='Type :')
        self.add('statictext', 'st_1', 9, 108, 219, 76, text='Staff :')
        self.add('datawindow', 'dw_1', 0, 188, 3200, 2032, dataobject='d_staff_attendancerep_details', taborder=50)
