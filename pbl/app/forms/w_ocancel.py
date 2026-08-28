"""Cancel — w_ocancel.

Generated from the PowerBuilder window ``w_ocancel.srw`` by
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
    name='w_ocancel',
    title='Cancel',
    width=1559,
    height=648,
    controls=[],
    tables=['items', 'itemsstk', 'orderm', 'purchased', 'orderdga', 'salesrd', 'salesm', 'orderd', 'purchasem', 'salesrm', 'orderdmodel', 'daybook', 'stkandprofit', 'oglist', 'delpart', 'daybookpart'],
    source_path='w_ocancel.srw',
    opens=['w_orderhelp', 'w_tran_view'],
)


class CancelForm(GeneratedForm):
    """Cancel"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('singlelineedit', 'sle_bno', 562, 132, 425, 100, limit=13, taborder=10)
        self.add('commandbutton', 'cb_help', 1010, 140, 229, 92, text='&Help', taborder=11)
        self.add('statictext', 'st_1', 119, 164, 439, 72, text='Order  No.  :')
        self.add('oval', 'oval_1', 416, 308, 727, 196)
        self.add('commandbutton', 'cb_ok', 535, 360, 247, 100, text='&OK', taborder=20)
        self.add('commandbutton', 'cb_exit', 791, 360, 247, 100, text='E&xit', taborder=30)
