"""Edit — w_itemadj_wgtrcptpmnt.

Generated from the PowerBuilder window ``w_itemadj_wgtrcptpmnt.srw`` by
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
    name='w_itemadj_wgtrcptpmnt',
    title='Edit',
    width=2208,
    height=1812,
    controls=[],
    tables=['items', 'itemadj', 'wgtrcptpmnt', 'itemsstk', 'accountm', 'generali'],
    source_path='w_itemadj_wgtrcptpmnt.srw',
)


class EditForm(GeneratedForm):
    """Edit"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('statictext', 'st_docno', 567, 20, 398, 92)
        self.add('statictext', 'st_12', 297, 32, 256, 80, text='Doc.No :')
        self.add('editmask', 'em_date', 567, 116, 398, 92, taborder=10)
        self.add('statictext', 'st_4', 329, 120, 224, 80, text='Date :')
        self.add('editmask', 'em_goldrate', 567, 212, 398, 92, taborder=20)
        self.add('statictext', 'st_6', 201, 220, 352, 80, text='Gold Rate :')
        self.add('datawindow', 'dw_accode', 567, 308, 402, 92, dataobject='d_sucucode', taborder=30)
        self.add('checkbox', 'cbx_genacc', 1202, 312, 498, 80, text='Gen. Accounts')
        self.add('statictext', 'st_3', 215, 316, 338, 72, text='Party  :')
        self.add('commandbutton', 'cb_new', 978, 316, 174, 80, text='New')
        self.add('singlelineedit', 'sle_name', 567, 404, 1399, 92)
        self.add('statictext', 'st_1', 210, 412, 343, 80, text='Name :')
        self.add('datawindow', 'dw_smcode', 567, 500, 677, 88, dataobject='d_smancode', taborder=40)
        self.add('statictext', 'st_13', 210, 508, 343, 80, text='SMan :')
        self.add('singlelineedit', 'sle_icode', 567, 592, 398, 92, limit=10, taborder=50)
        self.add('statictext', 'st_2', 206, 600, 347, 80, text='Item Code :')
        self.add('singlelineedit', 'sle_iname', 567, 688, 1399, 92)
        self.add('statictext', 'st_7', 187, 696, 366, 80, text='Item Name :')
        self.add('editmask', 'em_qty', 567, 784, 398, 92, taborder=60)
        self.add('statictext', 'st_8', 265, 792, 288, 80, text='Qty :')
        self.add('editmask', 'em_weight', 567, 880, 398, 92, taborder=70)
        self.add('statictext', 'st_5', 229, 892, 325, 80, text='Weight :')
        self.add('editmask', 'em_stwgt', 567, 976, 398, 92, taborder=80)
        self.add('statictext', 'st_9', 192, 980, 361, 80, text='Stone Wgt :')
        self.add('editmask', 'em_touch', 567, 1072, 398, 92, taborder=90)
        self.add('editmask', 'em_ctouch', 1568, 1072, 398, 92, taborder=100)
        self.add('commandbutton', 'cb_det', 1966, 1072, 146, 92, text='Def')
        self.add('statictext', 'st_15', 192, 1080, 361, 80, text='Touch :')
        self.add('statictext', 'st_17', 1147, 1080, 411, 80, text='Conv. Touch :')
        self.add('editmask', 'em_netwgt', 567, 1168, 398, 92)
        self.add('statictext', 'st_16', 192, 1180, 361, 80, text='Net Wgt :')
        self.add('datawindow', 'dw_stktype', 567, 1268, 539, 88, dataobject='d_stktypecode', taborder=110)
        self.add('statictext', 'st_10', 224, 1276, 329, 80, text='Stk Type :')
        self.add('dropdownlistbox', 'ddlb_rcptpmnt', 567, 1360, 398, 316, text='Receipt', items=['Receipt', 'Payment'], taborder=120)
        self.add('statictext', 'st_11', 192, 1364, 361, 80, text='Rcpt/Pmnt :')
        self.add('checkbox', 'cbx_printslip', 1371, 1380, 334, 72, text='Print Slip')
        self.add('singlelineedit', 'sle_note', 567, 1460, 1138, 92, limit=20, taborder=130)
        self.add('statictext', 'st_14', 192, 1472, 361, 80, text='Note :')
        self.add('commandbutton', 'cb_save', 823, 1572, 274, 108, text='&Save', taborder=140)
        self.add('commandbutton', 'cb_exit', 1111, 1572, 274, 108, text='E&xit', taborder=150)
