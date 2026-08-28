"""Discount Allocation — w_discafter.

Generated from the PowerBuilder window ``w_discafter.srw`` by
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
    name='w_discafter',
    title='Discount Allocation',
    width=1600,
    height=1544,
    controls=[],
    tables=['daybook', 'salesm', 'orderm', 'advafter'],
    source_path='w_discafter.srw',
)


class DiscountAllocationForm(GeneratedForm):
    """Discount Allocation"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('singlelineedit', 'sle_billno', 567, 52, 421, 92, limit=13, taborder=10)
        self.add('commandbutton', 'cb_help', 1024, 52, 229, 100, text='&Help')
        self.add('statictext', 'st_1', 219, 64, 343, 64, text='Bill No')
        self.add('editmask', 'em_date', 567, 148, 421, 92, taborder=20)
        self.add('statictext', 'st_2', 219, 156, 343, 76, text='Date')
        self.add('editmask', 'em_totamt', 567, 244, 421, 96)
        self.add('statictext', 'st_7', 219, 252, 343, 76, text='Total Amt')
        self.add('editmask', 'em_tax', 567, 344, 421, 100, taborder=30)
        self.add('statictext', 'st_8', 219, 352, 343, 76, text='Tax Amt')
        self.add('editmask', 'em_netamt', 567, 448, 421, 96)
        self.add('statictext', 'st_3', 219, 456, 343, 76, text='Net Amt')
        self.add('editmask', 'em_rcvd', 567, 548, 421, 100, taborder=40)
        self.add('statictext', 'st_6', 219, 564, 343, 76, text='Rcvd Amt.')
        self.add('editmask', 'em_discount', 567, 652, 421, 100, taborder=50)
        self.add('statictext', 'st_4', 219, 672, 343, 76, text='Discount')
        self.add('editmask', 'em_grandamt', 567, 756, 421, 96)
        self.add('statictext', 'st_5', 219, 768, 343, 76, text='Grand Amt')
        self.add('datawindow', 'dw_print', 1179, 840, 215, 124, dataobject='d_tendercash_slip')
        self.add('editmask', 'em_tendercash', 567, 856, 421, 100, taborder=60)
        self.add('statictext', 'st_9', 219, 868, 352, 76, text='Tender Amt')
        self.add('editmask', 'em_tenderbal', 567, 960, 421, 96)
        self.add('statictext', 'st_10', 219, 968, 352, 76, text='Tender Bal')
        self.add('checkbox', 'cbx_print', 567, 1084, 402, 84, text='Print Slip')
        self.add('commandbutton', 'cb_ok', 503, 1256, 283, 112, text='&Ok', taborder=70)
        self.add('commandbutton', 'cb_exit', 805, 1256, 283, 112, text='E&xit', taborder=80)
