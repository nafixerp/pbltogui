"""Loan Termination — w_loan_termination.

Generated from the PowerBuilder window ``w_loan_termination.srw`` by
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
    name='w_loan_termination',
    title='Loan Termination',
    width=2153,
    height=2148,
    controls=[],
    tables=['daybook', 'loancolln', 'loan', 'items', 'clients', 'itemadj', 'loan_items', 'generali', 'daybookpart'],
    source_path='w_loan_termination.srw',
    opens=['w_itemhelp', 'w_loanhelp'],
)


class LoanTerminationForm(GeneratedForm):
    """Loan Termination"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('statictext', 'st_docno', 585, 36, 402, 96)
        self.add('singlelineedit', 'sle_refno', 1627, 36, 402, 96, limit=10, taborder=10)
        self.add('statictext', 'st_7', 91, 40, 494, 64, text='Voucher No')
        self.add('statictext', 'st_18', 1152, 44, 466, 76, text='Ref. No.')
        self.add('editmask', 'em_date', 585, 136, 402, 96, taborder=20)
        self.add('editmask', 'em_prevtotint', 1627, 136, 402, 96)
        self.add('statictext', 'st_2', 91, 144, 494, 76, text='Date')
        self.add('statictext', 'st_20', 1152, 156, 475, 60, text='Total Interest Prev.')
        self.add('editmask', 'em_grate', 585, 236, 402, 96, taborder=30)
        self.add('editmask', 'em_intforamt', 1627, 236, 402, 96, taborder=80)
        self.add('statictext', 'st_9', 91, 248, 494, 76, text='Gold Rate')
        self.add('statictext', 'st_21', 1152, 248, 466, 76, text='For Amt')
        self.add('singlelineedit', 'sle_loandocno', 585, 336, 402, 96, limit=13, taborder=40)
        self.add('editmask', 'em_intdays', 1627, 336, 165, 96, taborder=90)
        self.add('editmask', 'em_intperc', 1856, 336, 174, 96, taborder=100)
        self.add('commandbutton', 'cb_loanhelp', 997, 340, 142, 88, text='&Help')
        self.add('statictext', 'st_22', 1152, 344, 466, 76, text='For Days')
        self.add('statictext', 'st_23', 1797, 344, 64, 76, text='%')
        self.add('statictext', 'st_4', 91, 348, 494, 64, text='Loan No')
        self.add('singlelineedit', 'st_custcode', 585, 436, 402, 96)
        self.add('editmask', 'em_intamt', 1627, 436, 402, 96, taborder=110)
        self.add('statictext', 'st_8', 91, 444, 494, 64, text='Customer')
        self.add('statictext', 'st_24', 1152, 444, 466, 76, text='Interest Amt')
        self.add('singlelineedit', 'st_custname', 585, 536, 1440, 96)
        self.add('singlelineedit', 'st_billno', 585, 636, 402, 96)
        self.add('editmask', 'em_srate', 1627, 636, 402, 96)
        self.add('statictext', 'st_1', 91, 640, 494, 64, text='Bill No')
        self.add('statictext', 'st_13', 1152, 644, 466, 80, text='Sold G.Rate')
        self.add('editmask', 'em_netamt', 585, 736, 402, 96)
        self.add('editmask', 'em_tadv', 1627, 736, 402, 96)
        self.add('statictext', 'st_3', 91, 744, 494, 76, text='Loan Amt')
        self.add('statictext', 'st_11', 1152, 752, 466, 80, text='T.Advance')
        self.add('editmask', 'em_totcollected', 585, 836, 402, 96, taborder=120)
        self.add('editmask', 'em_prevadj', 1627, 836, 402, 96)
        self.add('statictext', 'st_16', 91, 844, 494, 76, text='Total Collected')
        self.add('statictext', 'st_14', 1152, 852, 466, 80, text='Prev.Adjusted')
        self.add('editmask', 'em_advadj', 1627, 936, 402, 96, taborder=120)
        self.add('editmask', 'em_loanbal', 585, 940, 402, 96)
        self.add('statictext', 'st_15', 91, 948, 494, 76, text='Loan Balance')
        self.add('statictext', 'st_10', 1152, 948, 466, 76, text='Advance Adjust')
        self.add('editmask', 'em_advbal', 1627, 1036, 402, 96)
        self.add('editmask', 'em_instamt', 585, 1044, 402, 96)
        self.add('statictext', 'st_12', 1152, 1048, 466, 80, text='Advance Bal')
        self.add('statictext', 'st_5', 91, 1052, 494, 76, text='Installment Amt')
        self.add('editmask', 'em_rcvd', 585, 1144, 402, 96, taborder=50)
        self.add('statictext', 'st_6', 91, 1156, 494, 76, text='Refunded Amt')
        self.add('datawindow', 'dw_cashbank', 585, 1244, 882, 88, dataobject='d_cashbankcode', taborder=60)
        self.add('statictext', 'st_25', 91, 1256, 411, 76, text='Cash/Card')
        self.add('singlelineedit', 'sle_note', 585, 1336, 750, 96, limit=15, taborder=70)
        self.add('statictext', 'st_17', 91, 1348, 494, 76, text='Note')
        self.add('singlelineedit', 'sle_item', 585, 1440, 402, 92, limit=10, taborder=80)
        self.add('singlelineedit', 'sle_iname', 997, 1440, 1038, 92, taborder=90)
        self.add('statictext', 'st_26', 91, 1452, 494, 76, text='Move Items to')
        self.add('checkbox', 'cbx_convertitems', 585, 1552, 1509, 80, text='Convert items related to this loan into this item')
        self.add('oval', 'oval_1', 718, 1664, 713, 208)
        self.add('commandbutton', 'cb_ok', 832, 1720, 247, 100, text='&Save', taborder=130)
        self.add('commandbutton', 'cb_exit', 1097, 1720, 238, 100, text='E&xit', taborder=140)
