"""Leave Report — w_staff_leaverep.

Generated from the PowerBuilder window ``w_staff_leaverep.srw`` by
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
    name='w_staff_leaverep',
    title='Leave Report',
    width=3045,
    height=2360,
    controls=[],
    tables=[],
    source_path='w_staff_leaverep.srw',
    report={'dataobject': 'd_staff_leaverep', 'sql': 'SELECT clients.name AS clients_name, clients.addr1 AS clients_addr1, clients.addr2 AS clients_addr2, clients.addr3 AS clients_addr3, staffleave.tdate AS staffleave_tdate, staffleave.staff AS staffleave_staff, clients.code AS clients_code, staffleave.ldays AS staffleave_ldays, staffleave.reason AS staffleave_reason, staffleave.note AS staffleave_note, staffleave.plusdays AS staffleave_plusdays FROM clients, staffleave WHERE clients.code = staffleave.staff ORDER BY clients.name ASC, staffleave.tdate ASC', 'args': ['rdate1', 'rdate2'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date'}, 'tables': ['clients', 'staffleave'], 'columns': [{'name': 'clients_name', 'label': 'clients_name', 'type': 'char'}, {'name': 'clients_addr1', 'label': 'clients_addr1', 'type': 'char'}, {'name': 'clients_addr2', 'label': 'clients_addr2', 'type': 'char'}, {'name': 'clients_addr3', 'label': 'clients_addr3', 'type': 'char'}, {'name': 'staffleave_tdate', 'label': 'staffleave_tdate', 'type': 'date'}, {'name': 'staffleave_staff', 'label': 'staffleave_staff', 'type': 'char'}, {'name': 'clients_code', 'label': 'clients_code', 'type': 'char'}, {'name': 'staffleave_ldays', 'label': 'staffleave_ldays', 'type': 'decimal'}, {'name': 'staffleave_reason', 'label': 'staffleave_reason', 'type': 'char'}, {'name': 'staffleave_note', 'label': 'staffleave_note', 'type': 'char'}, {'name': 'staffleave_plusdays', 'label': 'staffleave_plusdays', 'type': 'decimal'}]},
)


class LeaveReportForm(GeneratedForm):
    """Leave Report"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 407, 0, 411, 92, taborder=10)
        self.add('editmask', 'em_date2', 1152, 0, 411, 92, taborder=20)
        self.add('datawindow', 'dw_accode', 1824, 0, 416, 100, dataobject='d_staffcode', taborder=30)
        self.add('commandbutton', 'cb_show', 2258, 0, 261, 92, text='&Show', taborder=40)
        self.add('commandbutton', 'cb_1', 2528, 0, 238, 92, text='&Print', taborder=70)
        self.add('commandbutton', 'cb_2', 2770, 0, 238, 92, text='E&xit', taborder=60)
        self.add('statictext', 'st_dt1', 5, 8, 393, 76, text='Date From :')
        self.add('statictext', 'st_dt2', 841, 12, 293, 76, text='Date To :')
        self.add('statictext', 'st_1', 1591, 12, 219, 76, text='Staff :')
        self.add('datawindow', 'dw_1', 0, 96, 3013, 2120, dataobject='d_staff_leaverep', taborder=50)
        self.add('commandbutton', 'cb_3', 1975, 104, 265, 92, text='Save &As', taborder=40)
        self.add('checkbox', 'cbx_summary', 2263, 116, 343, 80, text='Summary')
