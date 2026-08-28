"""Balance Sheet — w_balsheet.

Generated from the PowerBuilder window ``w_balsheet.srw`` by
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
    name='w_balsheet',
    title='Balance Sheet',
    width=3666,
    height=2292,
    controls=[],
    tables=['accountm', 'accountgbs', 'daybook'],
    source_path='w_balsheet.srw',
    opens=['w_balsheet_schedule'],
)


class BalanceSheetForm(GeneratedForm):
    """Balance Sheet"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('dropdownlistbox', 'ddlb_type', 1143, 0, 535, 400, text='Form1', items=['Form1', 'Form2', 'Form3'], taborder=20)
        self.add('commandbutton', 'cb_show', 1714, 0, 270, 84, text='&Show', taborder=20)
        self.add('commandbutton', 'cb_schedule', 2149, 0, 370, 84, text='Sc&hedule', taborder=30)
        self.add('commandbutton', 'cb_saveas', 2711, 0, 293, 84, text='Saveas', taborder=20)
        self.add('commandbutton', 'cb_1', 3090, 0, 233, 84, text='&Print', taborder=60)
        self.add('commandbutton', 'cb_2', 3360, 0, 238, 84, text='E&xit', taborder=50)
        self.add('editmask', 'em_date', 407, 4, 471, 84, taborder=10)
        self.add('statictext', 'st_1', 14, 8, 398, 76, text='Up to date :')
        self.add('statictext', 'st_2', 923, 8, 201, 64, text='Type :')
        self.add('datawindow', 'dw_1', 0, 96, 3598, 2068, dataobject='d_balancesheet', taborder=40)
