"""Order Rate Fix — w_order_ratefix.

Generated from the PowerBuilder window ``w_order_ratefix.srw`` by
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
    name='w_order_ratefix',
    title='Order Rate Fix',
    width=1403,
    height=716,
    controls=[],
    tables=['orderm'],
    source_path='w_order_ratefix.srw',
)


class OrderRateFixForm(GeneratedForm):
    """Order Rate Fix"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('singlelineedit', 'sle_billno', 544, 148, 416, 104, limit=13, taborder=10)
        self.add('commandbutton', 'cb_help', 983, 152, 229, 100, text='&Help')
        self.add('statictext', 'st_1', 69, 164, 480, 64, text='Enter Order no :')
        self.add('editmask', 'em_rate', 544, 264, 416, 104, taborder=20)
        self.add('statictext', 'st_2', 69, 280, 480, 64, text='Rate Fixed :')
        self.add('commandbutton', 'cb_ok', 462, 456, 233, 96, text='&Ok', taborder=30)
        self.add('commandbutton', 'cb_exit', 718, 456, 233, 96, text='E&xit', taborder=40)
