"""Order Sale — w_ordno.

Generated from the PowerBuilder window ``w_ordno.srw`` by
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
    name='w_ordno',
    title='Order Sale',
    width=1403,
    height=668,
    controls=[],
    tables=['orderm', 'salesm'],
    source_path='w_ordno.srw',
)


class OrderSaleForm(GeneratedForm):
    """Order Sale"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('singlelineedit', 'sle_billno', 567, 136, 421, 92, taborder=10)
        self.add('commandbutton', 'cb_help', 1019, 140, 229, 92, text='&Help', taborder=20)
        self.add('statictext', 'st_1', 87, 164, 485, 64, text='Enter Order no :')
        self.add('oval', 'oval_1', 375, 272, 640, 220)
        self.add('commandbutton', 'cb_ok', 434, 340, 242, 92, text='&OK', taborder=30)
        self.add('commandbutton', 'cb_exit', 695, 340, 242, 92, text='Exit', taborder=40)
