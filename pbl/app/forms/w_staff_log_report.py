"""Staff Log Report — w_staff_log_report.

Generated from the PowerBuilder window ``w_staff_log_report.srw`` by
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
    name='w_staff_log_report',
    title='Staff Log Report',
    width=3666,
    height=2480,
    controls=[],
    tables=['staff_log', 'clients', 'userd'],
    source_path='w_staff_log_report.srw',
    grid={'control': 'dw_1', 'dataobject': 'd_staff_log_report', 'table': 'staff_log', 'keys': ['idno', 'tdate', 'ttime'], 'computes': [{'name': 'compute_3', 'expression': ' count(  idno for all) ', 'format': '[general]', 'label': 'compute_3', 'band': 'summary'}, {'name': 'compute_2', 'expression': ' count(  idno for all distinct  idno )', 'format': '[general]', 'label': 'compute_2', 'band': 'summary'}], 'columns': [{'name': 'scode', 'label': 'scode', 'type': 'char'}, {'name': 'idno', 'label': 'idno', 'type': 'char'}, {'name': 'tdate', 'label': 'tdate', 'type': 'date'}, {'name': 'ttime', 'label': 'ttime', 'type': 'time'}, {'name': 'status', 'label': 'status', 'type': 'char'}, {'name': 'name', 'label': 'name', 'type': 'char'}]},
    report={'dataobject': 'd_staff_log_report', 'sql': 'SELECT staff_log.scode AS staff_log_scode, staff_log.idno AS staff_log_idno, staff_log.tdate AS staff_log_tdate, staff_log.ttime AS staff_log_ttime, staff_log.status AS staff_log_status, (select clients.name from clients where clients.code = staff_log.scode) as name FROM staff_log ORDER BY staff_log.tdate ASC, staff_log.ttime ASC, staff_log.idno ASC', 'computes': [{'name': 'compute_3', 'expression': ' count(  idno for all) ', 'format': '[general]', 'label': 'compute_3', 'band': 'summary'}, {'name': 'compute_2', 'expression': ' count(  idno for all distinct  idno )', 'format': '[general]', 'label': 'compute_2', 'band': 'summary'}], 'args': ['rlevel', 'rdate1', 'rdate2'], 'arg_types': {'rlevel': 'number', 'rdate1': 'date', 'rdate2': 'date'}, 'tables': ['staff_log'], 'columns': [{'name': 'scode', 'label': 'scode', 'type': 'char'}, {'name': 'idno', 'label': 'idno', 'type': 'char'}, {'name': 'tdate', 'label': 'tdate', 'type': 'date'}, {'name': 'ttime', 'label': 'ttime', 'type': 'time'}, {'name': 'status', 'label': 'status', 'type': 'char'}, {'name': 'name', 'label': 'name', 'type': 'char'}]},
)


class StaffLogReportForm(GeneratedForm):
    """Staff Log Report"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 219, 0, 407, 92, taborder=10)
        self.add('editmask', 'em_date2', 946, 0, 407, 92, taborder=20)
        self.add('dropdownlistbox', 'ddlb_reptype', 1714, 0, 494, 884, text='Entrywise', items=['Entrywise', 'Daywise', 'Staffwise'], taborder=30)
        self.add('commandbutton', 'cb_show', 2231, 0, 265, 92, text='&Show', taborder=40)
        self.add('commandbutton', 'cb_sort', 2514, 0, 265, 92, text='So&rt', taborder=140)
        self.add('commandbutton', 'cb_filter', 2793, 0, 265, 92, text='&Filter', taborder=130)
        self.add('commandbutton', 'cb_print', 3072, 0, 265, 92, text='&Print', taborder=160)
        self.add('commandbutton', 'cb_exit', 3351, 0, 265, 92, text='E&xit', taborder=150)
        self.add('statictext', 'st_dt2', 832, 4, 110, 76, text='To :')
        self.add('statictext', 'st_dt1', 9, 8, 201, 76, text='From :')
        self.add('statictext', 'st_3', 1490, 8, 215, 76, text='RType :')
        self.add('datawindow', 'dw_staff', 219, 96, 407, 88, dataobject='d_staffcode', taborder=110)
        self.add('commandbutton', 'cb_saveas', 2793, 96, 265, 92, text='Save As', taborder=120)
        self.add('commandbutton', 'cb_del', 3072, 96, 265, 92, text='Delete', taborder=100)
        self.add('statictext', 'st_1', 9, 104, 201, 76, text='Staff :')
        self.add('checkbox', 'cbx_staff', 626, 104, 69, 80)
        self.add('datawindow', 'dw_1', 0, 192, 3621, 2024, dataobject='d_staff_log_report', taborder=50)
