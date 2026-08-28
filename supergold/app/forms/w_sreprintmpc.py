"""Reprint — w_sreprintmpc.

Generated from the PowerBuilder window ``w_sreprintmpc.srw`` by
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
    name='w_sreprintmpc',
    title='Reprint',
    width=1403,
    height=668,
    controls=[],
    tables=['salesm', 'spdmddet'],
    source_path='w_sreprintmpc.srw',
)


class ReprintForm(GeneratedForm):
    """Reprint"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('singlelineedit', 'sle_billno', 549, 48, 443, 100, limit=13, taborder=10)
        self.add('commandbutton', 'cb_help', 1024, 52, 229, 100, text='&Help', taborder=20)
        self.add('statictext', 'st_1', 123, 56, 425, 64, text='Enter Bill no :')
        self.add('editmask', 'em_date', 549, 180, 443, 100, taborder=21)
        self.add('statictext', 'st_2', 315, 192, 201, 76, text='Date :')
        self.add('oval', 'oval_1', 430, 300, 713, 208)
        self.add('commandbutton', 'cb_ok', 544, 356, 233, 96, text='&Ok', taborder=30)
        self.add('commandbutton', 'cb_exit', 800, 356, 233, 96, text='E&xit', taborder=40)
        self.add('checkbox', 'cbx_view', 105, 368, 251, 76, text='&View')
