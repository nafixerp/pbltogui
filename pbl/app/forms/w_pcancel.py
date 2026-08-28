"""Cancel — w_pcancel.

Generated from the PowerBuilder window ``w_pcancel.srw`` by
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
    name='w_pcancel',
    title='Cancel',
    width=1586,
    height=640,
    controls=[],
    tables=['purchasem', 'purchaserm', 'items', 'itemsstk', 'barcode', 'purchased', 'purchaserd', 'daybook', 'purchased_dmddet', 'smithm', 'smithd', 'advafter', 'stkandprofit', 'oglist', 'barcode_dmddet', 'delpart', 'daybookpart'],
    source_path='w_pcancel.srw',
    opens=['w_purchhelp', 'w_tran_view'],
)


class CancelForm(GeneratedForm):
    """Cancel"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('singlelineedit', 'sle_bno', 562, 52, 425, 100, limit=13, taborder=10)
        self.add('commandbutton', 'cb_help', 1019, 52, 229, 100, text='&Help', taborder=20)
        self.add('statictext', 'st_1', 64, 64, 480, 72, text='Enter Doc No.  :')
        self.add('editmask', 'em_date', 562, 184, 425, 92, taborder=21)
        self.add('statictext', 'st_2', 297, 192, 247, 76, text='Date :')
        self.add('oval', 'oval_1', 430, 288, 722, 212)
        self.add('commandbutton', 'cb_ok', 539, 340, 247, 100, text='&OK', taborder=40)
        self.add('commandbutton', 'cb_exit', 809, 340, 247, 100, text='E&xit', taborder=30)
