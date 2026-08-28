"""Edit — w_refneditno.

Generated from the PowerBuilder window ``w_refneditno.srw`` by
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
    name='w_refneditno',
    title='Edit',
    width=1403,
    height=668,
    controls=[],
    tables=['refinerym', 'refineryd'],
    source_path='w_refneditno.srw',
    opens=['w_refnallhelp', 'w_refnhelp', 'w_refnenter', 'w_refnreturn1', 'w_refinary'],
)


class EditForm(GeneratedForm):
    """Edit"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('singlelineedit', 'sle_billno', 521, 132, 457, 96, taborder=10)
        self.add('commandbutton', 'cb_hlp', 987, 132, 210, 88, text='&Help', taborder=12)
        self.add('commandbutton', 'cb_1', 987, 132, 206, 92, text='&Help', taborder=20)
        self.add('statictext', 'st_1', 69, 148, 443, 64, text='Enter Doc No :')
        self.add('oval', 'oval_1', 357, 296, 622, 216)
        self.add('commandbutton', 'cb_ok', 425, 356, 229, 96, text='&OK', taborder=30)
        self.add('commandbutton', 'cb_exit', 672, 356, 229, 96, text='Exit', taborder=40)
