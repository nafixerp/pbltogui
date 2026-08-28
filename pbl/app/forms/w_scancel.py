"""Cancel — w_scancel.

Generated from the PowerBuilder window ``w_scancel.srw`` by
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
    name='w_scancel',
    title='Cancel',
    width=1573,
    height=652,
    controls=[],
    tables=['items', 'salesm', 'itemsstk', 'orderm', 'salesd', 'salesrd', 'purchased', 'daybook', 'barcode', 'salesrm', 'purchasem', 'stkandprofit', 'oglist', 'delpart', 'userd', 'daybookpart'],
    source_path='w_scancel.srw',
    opens=['w_salehelp', 'w_passverify_modify', 'w_tran_view'],
)


class CancelForm(GeneratedForm):
    """Cancel"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('singlelineedit', 'sle_bno', 558, 56, 462, 100, limit=13, taborder=10)
        self.add('commandbutton', 'cb_help', 1056, 60, 229, 92, text='&Help', taborder=20)
        self.add('statictext', 'st_1', 82, 88, 439, 72, text='Enter Bill No.  :')
        self.add('editmask', 'em_date', 562, 176, 457, 96, taborder=12)
        self.add('statictext', 'st_2', 274, 200, 247, 76, text='Date :')
        self.add('oval', 'oval_1', 411, 296, 759, 220)
        self.add('commandbutton', 'cb_ok', 558, 356, 233, 100, text='&OK', taborder=30)
        self.add('commandbutton', 'cb_exit', 800, 356, 233, 100, text='E&xit', taborder=40)
