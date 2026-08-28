"""Reprint — w_gsmthreprint.

Generated from the PowerBuilder window ``w_gsmthreprint.srw`` by
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
    name='w_gsmthreprint',
    title='Reprint',
    width=1403,
    height=668,
    controls=[],
    tables=['smithm'],
    source_path='w_gsmthreprint.srw',
)


class ReprintForm(GeneratedForm):
    """Reprint"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('commandbutton', 'cb_help', 942, 136, 215, 92, text='&Help', taborder=11)
        self.add('singlelineedit', 'sle_billno', 512, 140, 411, 96, taborder=10)
        self.add('statictext', 'st_1', 32, 164, 439, 64, text='Enter Doc no :')
        self.add('oval', 'oval_1', 398, 312, 731, 216)
        self.add('commandbutton', 'cb_ok', 485, 376, 261, 96, text='&OK', taborder=20)
        self.add('commandbutton', 'cb_exit', 782, 376, 261, 96, text='E&xit', taborder=30)
