"""Day Lock — w_daylock.

Generated from the PowerBuilder window ``w_daylock.srw`` by
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
    name='w_daylock',
    title='Day Lock',
    width=1157,
    height=820,
    controls=[],
    tables=['daylock'],
    source_path='w_daylock.srw',
)


class DayLockForm(GeneratedForm):
    """Day Lock"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('statictext', 'st_status', 393, 4, 398, 76)
        self.add('editmask', 'em_date1', 389, 104, 407, 100, taborder=10)
        self.add('statictext', 'st_1', 14, 120, 352, 76, text='Date From :')
        self.add('editmask', 'em_date2', 389, 228, 407, 100, taborder=20)
        self.add('statictext', 'st_2', 73, 248, 293, 76, text='Date To :')
        self.add('commandbutton', 'cb_lock', 151, 376, 393, 108, text='&Lock', taborder=60)
        self.add('commandbutton', 'cb_unlock', 576, 376, 393, 108, text='&Unlock', taborder=30)
        self.add('commandbutton', 'cb_hide', 151, 504, 393, 108, text='&Hide', taborder=40)
        self.add('commandbutton', 'cb_exit', 576, 504, 393, 108, text='E&xit', taborder=50)
