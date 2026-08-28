"""Finance Issue — w_finance_entry.

Generated from the PowerBuilder window ``w_finance_entry.srw`` by
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
    name='w_finance_entry',
    title='Finance Issue',
    width=2318,
    height=1900,
    controls=[],
    tables=['items', 'wgtrcptpmnt', 'daybook', 'itemsstk', 'itemadj', 'accountm', 'generali', 'daybookpart'],
    source_path='w_finance_entry.srw',
)


class FinanceIssueForm(GeneratedForm):
    """Finance Issue"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('statictext', 'st_docno', 613, 20, 398, 92)
        self.add('statictext', 'st_idocno', 1614, 20, 398, 92)
        self.add('commandbutton', 'cb_hlp', 2021, 24, 165, 92, text='Help', taborder=10)
        self.add('statictext', 'st_tidocno', 1248, 28, 352, 80, text='Issued No :')
        self.add('statictext', 'st_12', 343, 32, 256, 80, text='Doc.No :')
        self.add('editmask', 'em_date', 613, 116, 398, 92, taborder=10)
        self.add('statictext', 'st_6', 1248, 116, 352, 80, text='Gold Rate :')
        self.add('editmask', 'em_goldrate', 1614, 116, 398, 92, taborder=20)
        self.add('statictext', 'st_4', 375, 120, 224, 80, text='Date :')
        self.add('datawindow', 'dw_accode', 613, 212, 402, 92, dataobject='d_sucucode', taborder=30)
        self.add('checkbox', 'cbx_genacc', 1248, 216, 498, 80, text='Gen. Accounts')
        self.add('statictext', 'st_3', 261, 220, 338, 72, text='Party  :')
        self.add('commandbutton', 'cb_new', 1024, 220, 174, 80, text='New')
        self.add('singlelineedit', 'sle_name', 613, 308, 1399, 92)
        self.add('statictext', 'st_1', 256, 316, 343, 80, text='Name :')
        self.add('datawindow', 'dw_smcode', 613, 404, 677, 88, dataobject='d_smancode', taborder=40)
        self.add('statictext', 'st_13', 256, 412, 343, 80, text='SMan :')
        self.add('singlelineedit', 'sle_icode', 613, 496, 398, 92, limit=10, taborder=50)
        self.add('statictext', 'st_2', 251, 504, 347, 80, text='Item Code :')
        self.add('singlelineedit', 'sle_iname', 613, 592, 1399, 92)
        self.add('statictext', 'st_7', 233, 600, 366, 80, text='Item Name :')
        self.add('editmask', 'em_qty', 613, 688, 398, 92, taborder=60)
        self.add('editmask', 'em_weight', 1614, 688, 398, 92, taborder=80)
        self.add('statictext', 'st_8', 311, 696, 288, 80, text='Qty :')
        self.add('statictext', 'st_5', 1275, 700, 325, 80, text='Weight :')
        self.add('editmask', 'em_stwgt', 613, 784, 398, 92, taborder=90)
        self.add('editmask', 'em_netwgt', 1614, 784, 398, 92, taborder=70)
        self.add('statictext', 'st_9', 238, 788, 361, 80, text='Stone Wgt :')
        self.add('statictext', 'st_15', 1230, 796, 370, 80, text='Net Weight :')
        self.add('datawindow', 'dw_stktype', 613, 884, 539, 88, dataobject='d_stktypecode', taborder=100)
        self.add('statictext', 'st_10', 270, 892, 329, 80, text='Stk Type :')
        self.add('singlelineedit', 'sle_note', 613, 976, 1399, 92, limit=20, taborder=120)
        self.add('statictext', 'st_14', 238, 988, 361, 80, text='Note :')
        self.add('editmask', 'em_finamt', 613, 1072, 398, 92, taborder=130)
        self.add('editmask', 'em_intperc', 1669, 1072, 338, 92, taborder=140)
        self.add('statictext', 'st_17', 1097, 1080, 558, 80, text='Monthly Interest% :')
        self.add('statictext', 'st_16', 183, 1084, 416, 80, text='Finance Amt :')
        self.add('editmask', 'em_netamt', 613, 1172, 398, 92, taborder=130)
        self.add('editmask', 'em_intamt', 1669, 1172, 338, 92, taborder=140)
        self.add('statictext', 'st_19', 1097, 1176, 558, 80, text='Interest Amt :')
        self.add('statictext', 'st_20', 183, 1180, 416, 80, text='Net Amt :')
        self.add('editmask', 'em_rpamt', 613, 1272, 398, 92, taborder=150)
        self.add('statictext', 'st_rpamt', 128, 1276, 471, 80, text='Paid Amt :')
        self.add('checkbox', 'cbx_printslip', 1669, 1288, 334, 72, text='Print Slip')
        self.add('commandbutton', 'cb_save', 832, 1568, 274, 108, text='&Save', taborder=160)
        self.add('commandbutton', 'cb_exit', 1120, 1568, 274, 108, text='E&xit', taborder=170)
