"""A/c Restart Date — w_acstartdate_change.

Generated from the PowerBuilder window ``w_acstartdate_change.srw`` by
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
    name='w_acstartdate_change',
    title='A/c Restart Date',
    width=1742,
    height=752,
    controls=[],
    tables=['accountm'],
    source_path='w_acstartdate_change.srw',
)


class ACRestartDateForm(GeneratedForm):
    """A/c Restart Date"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('datawindow', 'dw_accode', 466, 8, 430, 88, dataobject='d_accode', taborder=10)
        self.add('statictext', 'st_3', 133, 16, 320, 72, text='Account  :')
        self.add('singlelineedit', 'sle_name', 466, 112, 1253, 100)
        self.add('statictext', 'st_1', 128, 120, 325, 80, text='Name :')
        self.add('editmask', 'em_oldduedate', 466, 228, 434, 100)
        self.add('statictext', 'st_2', 41, 236, 411, 80, text='Old Date :')
        self.add('editmask', 'em_newduedate', 466, 348, 434, 100, taborder=20)
        self.add('statictext', 'st_4', 23, 356, 430, 80, text='ReStart Date:')
        self.add('commandbutton', 'cb_ok', 727, 508, 270, 120, text='&OK', taborder=30)
