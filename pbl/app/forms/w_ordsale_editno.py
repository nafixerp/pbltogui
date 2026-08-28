"""Edit Order Sale — w_ordsale_editno.

Generated from the PowerBuilder window ``w_ordsale_editno.srw`` by
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
    name='w_ordsale_editno',
    title='Edit Order Sale',
    width=1403,
    height=668,
    controls=[],
    tables=['salesm'],
    source_path='w_ordsale_editno.srw',
    opens=['w_salehelp', 'w_ordersale'],
)


class EditOrderSaleForm(GeneratedForm):
    """Edit Order Sale"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('singlelineedit', 'sle_billno', 539, 96, 421, 92, limit=13, taborder=10)
        self.add('commandbutton', 'cb_help', 997, 96, 229, 100, text='&Help', taborder=20)
        self.add('statictext', 'st_1', 69, 112, 425, 64, text='Enter Bill no :')
        self.add('editmask', 'em_date', 539, 212, 421, 92, taborder=21)
        self.add('statictext', 'st_2', 247, 232, 247, 76, text='Date :')
        self.add('oval', 'oval_1', 375, 352, 713, 208)
        self.add('commandbutton', 'cb_ok', 489, 408, 233, 96, text='&Ok', taborder=30)
        self.add('commandbutton', 'cb_exit', 745, 408, 233, 96, text='E&xit', taborder=40)
