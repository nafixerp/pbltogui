"""Edit — w_purcheditno.

Generated from the PowerBuilder window ``w_purcheditno.srw`` by
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
    name='w_purcheditno',
    title='Edit',
    width=1403,
    height=668,
    controls=[],
    tables=['purchasem', 'purchaserm', 'purchaserd', 'purchased'],
    source_path='w_purcheditno.srw',
    opens=['w_purchhelp', 'w_purchase_amtentry', 'w_diamond_preturn', 'w_purchase_ret', 'w_diamond_purchase', 'w_purchase_withbc', 'w_purchase'],
)


class EditForm(GeneratedForm):
    """Edit"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('commandbutton', 'cb_help', 951, 68, 238, 100, text='&Help')
        self.add('singlelineedit', 'sle_billno', 466, 72, 457, 96, taborder=10)
        self.add('statictext', 'st_1', 27, 84, 430, 64, text='Enter Doc no :')
        self.add('editmask', 'em_date', 466, 184, 457, 92, taborder=20)
        self.add('statictext', 'st_2', 210, 192, 247, 76, text='Date :')
        self.add('oval', 'oval_1', 338, 292, 759, 228)
        self.add('commandbutton', 'cb_ok', 462, 352, 242, 104, text='&OK', taborder=30)
        self.add('commandbutton', 'cb_exit', 731, 352, 247, 104, text='E&xit', taborder=40)
