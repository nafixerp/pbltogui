"""Reprint — w_preprint.

Generated from the PowerBuilder window ``w_preprint.srw`` by
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
    name='w_preprint',
    title='Reprint',
    width=1403,
    height=696,
    controls=[],
    tables=['purchasem', 'purchaserm'],
    source_path='w_preprint.srw',
)


class ReprintForm(GeneratedForm):
    """Reprint"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('commandbutton', 'cb_help', 937, 44, 238, 100, text='&Help', taborder=30)
        self.add('singlelineedit', 'sle_billno', 466, 48, 457, 96, taborder=10)
        self.add('statictext', 'st_1', 18, 60, 430, 64, text='Enter Doc no :')
        self.add('editmask', 'em_date', 466, 160, 457, 92, taborder=20)
        self.add('statictext', 'st_2', 201, 168, 247, 76, text='Date :')
        self.add('oval', 'oval_1', 338, 304, 759, 228)
        self.add('commandbutton', 'cb_ok', 462, 364, 242, 104, text='&OK', taborder=40)
        self.add('commandbutton', 'cb_exit', 731, 364, 247, 104, text='E&xit', taborder=50)
