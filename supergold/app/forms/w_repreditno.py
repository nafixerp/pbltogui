"""Edit — w_repreditno.

Generated from the PowerBuilder window ``w_repreditno.srw`` by
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
    name='w_repreditno',
    title='Edit',
    width=1403,
    height=668,
    controls=[],
    tables=['repairm'],
    source_path='w_repreditno.srw',
)


class EditForm(GeneratedForm):
    """Edit"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('singlelineedit', 'sle_billno', 544, 140, 421, 92, limit=13, taborder=10)
        self.add('commandbutton', 'cb_help', 1001, 140, 229, 100, text='&Help', taborder=20)
        self.add('statictext', 'st_1', 114, 152, 485, 64, text='Enter Doc No :')
        self.add('oval', 'oval_1', 343, 292, 713, 208)
        self.add('commandbutton', 'cb_ok', 439, 344, 233, 100, text='&OK', taborder=30)
        self.add('commandbutton', 'cb_exit', 704, 344, 233, 100, text='E&xit', taborder=40)
