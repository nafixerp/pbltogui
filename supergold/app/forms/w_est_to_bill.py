"""Bill Confirmation — w_est_to_bill.

Generated from the PowerBuilder window ``w_est_to_bill.srw`` by
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
    name='w_est_to_bill',
    title='Bill Confirmation',
    width=1550,
    height=1556,
    controls=[],
    tables=['salesm', 'daybook', 'orderm', 'items', 'itemsstk', 'advafter', 'purchasem', 'counter', 'salesd', 'salesrm', 'salesrd', 'purchased', 'salestype', 'spdmddet', 'generali', 'generals', 'daybookpart', 'userm'],
    source_path='w_est_to_bill.srw',
)


class BillConfirmationForm(GeneratedForm):
    """Bill Confirmation"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('singlelineedit', 'sle_billno', 567, 52, 421, 92, limit=13, taborder=10)
        self.add('commandbutton', 'cb_help', 997, 52, 229, 92, text='&Help')
        self.add('statictext', 'st_1', 133, 60, 425, 64, text='Enter Est no :')
        self.add('datawindow', 'dw_counter', 567, 152, 654, 88, dataobject='d_countercode', taborder=20)
        self.add('statictext', 'st_7', 279, 160, 279, 76, text='Counter :')
        self.add('singlelineedit', 'sle_billno2', 567, 252, 421, 92, limit=13, taborder=30)
        self.add('singlelineedit', 'sle_billno3', 1065, 252, 352, 92, limit=13)
        self.add('commandbutton', 'cb_bhlp', 1426, 252, 69, 92, text='^')
        self.add('statictext', 'st_8', 215, 264, 343, 80, text='Bill No. :')
        self.add('editmask', 'em_date', 567, 352, 421, 92, taborder=40)
        self.add('statictext', 'st_2', 311, 360, 247, 76, text='Date :')
        self.add('editmask', 'em_billamt', 567, 452, 421, 96, taborder=50)
        self.add('statictext', 'st_11', 215, 460, 343, 80, text='Bill Amt :')
        self.add('editmask', 'em_taxperc', 567, 556, 123, 96, taborder=60)
        self.add('editmask', 'em_taxamt', 695, 556, 293, 96)
        self.add('statictext', 'st_9', 215, 564, 343, 80, text='Tax Amt :')
        self.add('editmask', 'em_netamt', 567, 656, 421, 96)
        self.add('statictext', 'st_3', 279, 664, 279, 76, text='Net Amt :')
        self.add('editmask', 'em_rcvd', 567, 760, 421, 100, taborder=50)
        self.add('statictext', 'st_6', 215, 768, 343, 76, text='Rcvd Amt. :')
        self.add('editmask', 'em_discount', 567, 864, 421, 100, taborder=60)
        self.add('statictext', 'st_4', 261, 872, 297, 76, text='Discount :')
        self.add('editmask', 'em_taxdisc', 567, 968, 421, 100, taborder=70)
        self.add('statictext', 'st_10', 215, 984, 343, 80, text='Tax Disc :')
        self.add('editmask', 'em_grandamt', 567, 1072, 421, 96)
        self.add('statictext', 'st_5', 197, 1084, 361, 76, text='Grand Amt :')
        self.add('checkbox', 'cbx_updtfr', 229, 1176, 169, 84, text='&Fr')
        self.add('checkbox', 'cbx_laserprint', 567, 1180, 421, 80, text='Laser Print')
        self.add('oval', 'oval_1', 407, 1268, 713, 208)
        self.add('commandbutton', 'cb_ok', 521, 1324, 233, 96, text='&Ok', taborder=80)
        self.add('commandbutton', 'cb_exit', 777, 1324, 233, 96, text='E&xit', taborder=90)
