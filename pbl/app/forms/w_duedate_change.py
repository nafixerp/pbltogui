"""Change Duedate — w_duedate_change.

Generated from the PowerBuilder window ``w_duedate_change.srw`` by
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
    name='w_duedate_change',
    title='Change Duedate',
    width=1742,
    height=752,
    controls=[],
    tables=['clients'],
    source_path='w_duedate_change.srw',
)


class ChangeDuedateForm(GeneratedForm):
    """Change Duedate"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('datawindow', 'dw_accode', 466, 8, 398, 88, dataobject='d_cust', taborder=10)
        self.add('statictext', 'st_3', 105, 16, 338, 72, text='Party  :')
        self.add('singlelineedit', 'sle_name', 466, 112, 1253, 100)
        self.add('statictext', 'st_1', 101, 120, 343, 80, text='Name :')
        self.add('editmask', 'em_oldduedate', 466, 228, 434, 100)
        self.add('statictext', 'st_2', 14, 236, 430, 80, text='Old Duedate :')
        self.add('editmask', 'em_newduedate', 466, 348, 434, 100, taborder=20)
        self.add('statictext', 'st_4', 0, 356, 443, 80, text='Next Duedate :')
        self.add('commandbutton', 'cb_ok', 727, 508, 270, 120, text='&OK', taborder=30)
