"""Daily Statement Entry — w_dailystatement_entry.

Generated from the PowerBuilder window ``w_dailystatement_entry.srw`` by
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
    name='w_dailystatement_entry',
    title='Daily Statement Entry',
    width=3346,
    height=1928,
    controls=[],
    tables=['daybook', 'accountm', 'generali', 'daybookpart'],
    source_path='w_dailystatement_entry.srw',
)


class DailyStatementEntryForm(GeneratedForm):
    """Daily Statement Entry"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('datawindow', 'dw_cashbank', 1467, 16, 882, 88, dataobject='d_cashbankcode', taborder=20)
        self.add('datawindow', 'dw_staff', 2642, 16, 677, 88, dataobject='d_smancode', taborder=30)
        self.add('editmask', 'em_date', 192, 20, 439, 96, taborder=10)
        self.add('commandbutton', 'cb_show', 645, 20, 251, 84, text='&Edit')
        self.add('statictext', 'st_2', 923, 24, 530, 72, text='Cash/Bank Code :')
        self.add('statictext', 'st_4', 2373, 24, 247, 76, text='SMan :')
        self.add('statictext', 'st_10', 0, 32, 183, 76, text='Date :')
        self.add('datawindow', 'dw_dim', 0, 152, 3323, 1492, dataobject='d_dailystatement_entry', taborder=40)
        self.add('statictext', 'st_5', 453, 156, 5, 1484)
        self.add('statictext', 'st_1', 1198, 156, 5, 1484, text='1')
        self.add('statictext', 'st_6', 2130, 156, 5, 1484)
        self.add('statictext', 'st_3', 2533, 156, 5, 1484)
        self.add('statictext', 'st_7', 2880, 156, 5, 1484)
        self.add('statictext', 'st_woodqbic', 2395, 1084, 82, 76)
        self.add('statictext', 'st_others', 2249, 1088, 119, 76)
        self.add('statictext', 'st_new', 535, 1552, 110, 68)
        self.add('commandbutton', 'cb_ad', 9, 1556, 206, 76, text='&Add', taborder=70)
        self.add('commandbutton', 'cb_del', 219, 1556, 215, 76, text='&Delete', taborder=80)
        self.add('roundrectangle', 'rr_1', 1312, 1660, 699, 160)
        self.add('commandbutton', 'cb_save', 1381, 1692, 279, 92, text='&Save', taborder=50)
        self.add('commandbutton', 'cb_exit', 1669, 1692, 279, 92, text='E&xit', taborder=60)
