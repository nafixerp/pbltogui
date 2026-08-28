"""Edit Loan — w_loanedit.

Generated from the PowerBuilder window ``w_loanedit.srw`` by
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
    name='w_loanedit',
    title='Edit Loan',
    width=1362,
    height=628,
    controls=[],
    tables=['loan'],
    source_path='w_loanedit.srw',
)


class EditLoanForm(GeneratedForm):
    """Edit Loan"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('singlelineedit', 'sle_bno', 471, 116, 425, 100, taborder=10)
        self.add('commandbutton', 'cb_help', 905, 120, 215, 96, text='&Help', taborder=20)
        self.add('statictext', 'st_1', 46, 132, 411, 72, text='Doc No  :')
        self.add('oval', 'oval_1', 347, 244, 654, 224)
        self.add('commandbutton', 'cb_ok', 443, 312, 229, 92, text='OK', taborder=30)
        self.add('commandbutton', 'cb_exit', 681, 312, 229, 92, text='E&xit', taborder=21)
