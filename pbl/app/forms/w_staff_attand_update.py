"""Staff Log Update — w_staff_attand_update.

Generated from the PowerBuilder window ``w_staff_attand_update.srw`` by
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
    name='w_staff_attand_update',
    title='Staff Log Update',
    width=3657,
    height=1704,
    controls=[],
    tables=['datepicker', 'staff_log', 'olecustomcontrol', 'clients', 'machine'],
    source_path='w_staff_attand_update.srw',
    opens=['w_staff_userinfo'],
)


class StaffLogUpdateForm(GeneratedForm):
    """Staff Log Update"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('singlelineedit', 'sle_ipaddress', 421, 0, 453, 92, text='192.168.1.201', taborder=50)
        self.add('datepicker', 'dp_date1', 1120, 0, 443, 92, taborder=100)
        self.add('commandbutton', 'cb_connect', 1701, 0, 507, 92, text='Connect', taborder=80)
        self.add('statictext', 'st_status', 2217, 0, 805, 92)
        self.add('commandbutton', 'cb_backup', 3127, 0, 507, 92, text='Backup', taborder=90)
        self.add('statictext', 'st_1', 9, 4, 398, 76, text='IP Address :')
        self.add('statictext', 'st_3', 891, 12, 224, 64, text='From :')
        self.add('singlelineedit', 'sle_ipport', 421, 96, 453, 92, text='4370', taborder=20)
        self.add('datepicker', 'dp_date2', 1120, 96, 443, 92, taborder=90)
        self.add('commandbutton', 'cb_download', 1701, 100, 507, 92, text='Download Logs', taborder=40)
        self.add('commandbutton', 'cb_updatelog', 2217, 100, 507, 92, text='Update Logs', taborder=60)
        self.add('commandbutton', 'cb_clearlogs', 3127, 100, 507, 92, text='Clear Logs')
        self.add('statictext', 'st_4', 891, 104, 224, 64, text='To      :')
        self.add('statictext', 'st_2', 14, 108, 407, 76, text='IP Port        :')
        self.add('olecustomcontrol', 'zkem', 2875, 116, 91, 68, taborder=70)
        self.add('datawindow', 'dw_log', 9, 196, 2199, 1416, dataobject='d_staff_log', taborder=10)
        self.add('datawindow', 'dw_userlist', 2217, 196, 1417, 1416, dataobject='d_staff_machlist', taborder=30)
