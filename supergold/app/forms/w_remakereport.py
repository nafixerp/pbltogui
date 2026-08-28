"""Remake Reports — w_remakereport.

Generated from the PowerBuilder window ``w_remakereport.srw`` by
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
    name='w_remakereport',
    title='Remake Reports',
    width=3657,
    height=2280,
    controls=[],
    tables=[],
    source_path='w_remakereport.srw',
    report={'dataobject': 'd_remakereport_1', 'sql': "SELECT repaird.slno AS repaird_slno, repaird.name AS repaird_name, repaird.weight AS repaird_weight, repaird.qty AS repaird_qty, repaird.stonewgt AS repaird_stonewgt, repaird.complaint AS repaird_complaint, repairm.status AS repairm_status, repairm.slno AS repairm_slno, repairm.billno AS repairm_billno, repairm.tdate AS repairm_tdate, repairm.duedate AS repairm_duedate, repairm.custname AS repairm_custname FROM repaird, repairm WHERE repaird.slno = repairm.slno AND repairm.givrec = 'R' ORDER BY repairm.slno ASC, repairm.status ASC", 'args': ['rdate1', 'rdate2', 'rlevel'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date', 'rlevel': 'number'}, 'tables': ['repaird', 'repairm'], 'columns': [{'name': 'repaird_slno', 'label': 'repaird_slno', 'type': 'decimal'}, {'name': 'repaird_name', 'label': 'repaird_name', 'type': 'char'}, {'name': 'repaird_weight', 'label': 'repaird_weight', 'type': 'decimal'}, {'name': 'repaird_qty', 'label': 'repaird_qty', 'type': 'long'}, {'name': 'repaird_stonewgt', 'label': 'repaird_stonewgt', 'type': 'decimal'}, {'name': 'repaird_complaint', 'label': 'repaird_complaint', 'type': 'char'}, {'name': 'repairm_status', 'label': 'repairm_status', 'type': 'long'}, {'name': 'repairm_slno', 'label': 'repairm_slno', 'type': 'decimal'}, {'name': 'repairm_billno', 'label': 'repairm_billno', 'type': 'char'}, {'name': 'repairm_tdate', 'label': 'repairm_tdate', 'type': 'date'}, {'name': 'repairm_duedate', 'label': 'repairm_duedate', 'type': 'date'}, {'name': 'repairm_custname', 'label': 'repairm_custname', 'type': 'char'}]},
)


class RemakeReportsForm(GeneratedForm):
    """Remake Reports"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 416, 0, 375, 92, taborder=10)
        self.add('editmask', 'em_date2', 1143, 0, 375, 92, taborder=20)
        self.add('dropdownlistbox', 'ddlb_reptype', 1550, 0, 827, 476, text='Remake Entry Details', items=['Remake Entry Details', 'Goldsmith Issue Details', 'Goldsmith Rcpt Details', 'Remake Return to Party Detials'], taborder=31)
        self.add('commandbutton', 'cb_show', 2432, 0, 270, 96, text='&Show', taborder=30)
        self.add('commandbutton', 'cb_3', 2811, 0, 270, 96, text='Save &As', taborder=60)
        self.add('commandbutton', 'cb_1', 3081, 0, 274, 96, text='&Print', taborder=70)
        self.add('commandbutton', 'cb_2', 3360, 0, 251, 96, text='E&xit', taborder=50)
        self.add('statictext', 'st_8', 14, 12, 393, 64, text='Date From :')
        self.add('statictext', 'st_2', 823, 12, 302, 72, text='Date To  :')
        self.add('datawindow', 'dw_1', 0, 100, 3621, 2080, dataobject='d_remakereport_1', taborder=40)
