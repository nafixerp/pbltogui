"""Users History — w_userhistory.

Generated from the PowerBuilder window ``w_userhistory.srw`` by
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
    name='w_userhistory',
    title='Users History',
    width=2537,
    height=1948,
    controls=[],
    tables=['delpart', 'userhist'],
    source_path='w_userhistory.srw',
    report={'dataobject': 'd_userhistory', 'sql': 'SELECT userhist.tdate AS userhist_tdate, userhist.time1 AS userhist_time1, userhist.time2 AS userhist_time2, userm.name AS userm_name, userhist.code AS userhist_code FROM userhist, userm WHERE userhist.code = userm.code ORDER BY userhist.tdate ASC, userhist.time1 ASC', 'computes': [], 'args': ['rdate1', 'rdate2'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date'}, 'tables': ['userhist', 'userm'], 'columns': [{'name': 'userhist_tdate', 'label': 'userhist_tdate', 'type': 'date'}, {'name': 'userhist_time1', 'label': 'userhist_time1', 'type': 'time'}, {'name': 'userhist_time2', 'label': 'userhist_time2', 'type': 'time'}, {'name': 'userm_name', 'label': 'userm_name', 'type': 'char'}, {'name': 'userhist_code', 'label': 'userhist_code', 'type': 'char'}]},
)


class UsersHistoryForm(GeneratedForm):
    """Users History"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date2', 1138, 0, 393, 100, taborder=20)
        self.add('commandbutton', 'cb_show', 1641, 0, 270, 96, text='&Show', taborder=30)
        self.add('commandbutton', 'cb_1', 1929, 0, 270, 96, text='&Print', taborder=80)
        self.add('commandbutton', 'cb_2', 2217, 0, 270, 96, text='E&xit', taborder=70)
        self.add('editmask', 'em_date1', 393, 8, 393, 100, taborder=10)
        self.add('statictext', 'st_3', 859, 8, 270, 76, text='Date To :')
        self.add('statictext', 'st_2', 27, 12, 343, 76, text='Date From :')
        self.add('dropdownlistbox', 'ddlb_sort', 398, 120, 754, 540, text='Date', items=['Date, Time', 'User'], taborder=60)
        self.add('commandbutton', 'cb_empty', 2222, 120, 270, 96, text='&Empty', taborder=50)
        self.add('statictext', 'st_1', 119, 124, 247, 76, text='Sort :')
        self.add('datawindow', 'dw_updaterep', 0, 240, 2510, 1576, dataobject='d_userhistory', taborder=40)
