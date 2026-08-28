"""Stock Transfer — w_itemadj.

Generated from the PowerBuilder window ``w_itemadj.srw`` by
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
    name='w_itemadj',
    title='Stock Transfer',
    width=2606,
    height=1896,
    controls=[],
    tables=['items', 'itemsstk', 'barcode', 'itemadj', 'sman', 'generali', 'delpart'],
    source_path='w_itemadj.srw',
    opens=['w_itemhelp'],
)


class StockTransferForm(GeneratedForm):
    """Stock Transfer"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date', 1582, 48, 398, 92, taborder=30)
        self.add('datawindow', 'dw_smcode', 430, 52, 677, 88, dataobject='d_smancode', taborder=10)
        self.add('statictext', 'st_20', 133, 64, 288, 76, text='SM Name :')
        self.add('statictext', 'st_14', 1312, 64, 247, 76, text='Date :')
        self.add('statictext', 'st_1', 430, 168, 439, 76, text='Item From')
        self.add('statictext', 'st_2', 1582, 168, 439, 76, text='Item To')
        self.add('checkbox', 'cbx_ichange', 969, 172, 494, 76, text='&Item Change')
        self.add('singlelineedit', 'sle_frombcode', 430, 248, 434, 88, limit=15, taborder=20)
        self.add('singlelineedit', 'sle_tobcode', 1582, 248, 434, 88, limit=15, taborder=130)
        self.add('statictext', 'st_frombcode', 55, 252, 366, 76, text='Barcode :')
        self.add('statictext', 'st_frombcwgt', 878, 256, 389, 80)
        self.add('statictext', 'st_tobcode', 1193, 256, 366, 76, text='Barcode :')
        self.add('statictext', 'st_tobcwgt', 2030, 256, 389, 80)
        self.add('singlelineedit', 'sle_fromcode', 430, 340, 320, 100, taborder=40)
        self.add('singlelineedit', 'sle_tocode', 1582, 340, 320, 100, taborder=140)
        self.add('commandbutton', 'cb_help2', 1915, 348, 64, 84, text='^')
        self.add('commandbutton', 'cb_help1', 759, 352, 64, 84, text='^')
        self.add('statictext', 'st_4', 82, 356, 338, 76, text='Item Code :')
        self.add('statictext', 'st_11', 1211, 360, 347, 76, text='Item Code :')
        self.add('singlelineedit', 'sle_fromname', 430, 444, 686, 92, taborder=50)
        self.add('singlelineedit', 'sle_toname', 1582, 444, 686, 92, taborder=150)
        self.add('statictext', 'st_5', 192, 456, 229, 76, text='Name  :')
        self.add('statictext', 'st_10', 1330, 472, 229, 76, text='Name  :')
        self.add('editmask', 'em_fromqty', 430, 544, 320, 100, taborder=60)
        self.add('editmask', 'em_toqty', 1582, 544, 320, 100, taborder=160)
        self.add('statictext', 'st_6', 270, 560, 151, 76, text='Qty :')
        self.add('statictext', 'st_9', 1408, 568, 151, 76, text='Qty :')
        self.add('editmask', 'em_fromwgt', 430, 648, 320, 100, taborder=70)
        self.add('editmask', 'em_towgt', 1582, 648, 320, 100, taborder=170)
        self.add('statictext', 'st_7', 155, 664, 265, 76, text='Weight :')
        self.add('statictext', 'st_8', 1312, 672, 247, 76, text='Weight :')
        self.add('editmask', 'em_fromstwgt', 430, 752, 320, 100, taborder=80)
        self.add('editmask', 'em_tostwgt', 1582, 752, 320, 100, taborder=180)
        self.add('statictext', 'st_15', 174, 760, 247, 76, text='St.Wgt :')
        self.add('statictext', 'st_16', 1312, 772, 247, 76, text='St.Wgt :')
        self.add('editmask', 'em_fromstamt', 430, 856, 320, 100, taborder=90)
        self.add('editmask', 'em_tostamt', 1582, 856, 320, 100, taborder=190)
        self.add('statictext', 'st_19', 1312, 864, 247, 76, text='St.Amt :')
        self.add('statictext', 'st_18', 174, 868, 247, 76, text='St.Amt :')
        self.add('editmask', 'em_fromcost', 430, 960, 320, 100, taborder=100)
        self.add('editmask', 'em_tocost', 1582, 960, 320, 100, taborder=200)
        self.add('statictext', 'st_12', 110, 976, 311, 76, text='Cur. Cost :')
        self.add('statictext', 'st_13', 1376, 976, 183, 76, text='Cost :')
        self.add('datawindow', 'dw_stktypefrom', 430, 1064, 539, 88, dataobject='d_stktypecode', taborder=110)
        self.add('datawindow', 'dw_stktypeto', 1582, 1064, 539, 88, dataobject='d_stktypecode', taborder=210)
        self.add('statictext', 'st_17', 110, 1072, 311, 76, text='Stk Type :')
        self.add('statictext', 'st_25', 1253, 1072, 311, 76, text='Stk Type :')
        self.add('editmask', 'em_fromstktouch', 430, 1156, 320, 100, taborder=120)
        self.add('editmask', 'em_tostktouch', 1582, 1156, 320, 100, taborder=220)
        self.add('statictext', 'st_22', 1157, 1160, 407, 76, text='Stock Touch :')
        self.add('statictext', 'st_21', 14, 1168, 407, 76, text='Stock Touch :')
        self.add('statictext', 'st_3', 814, 1284, 750, 76, text='Reason For Adjustment')
        self.add('singlelineedit', 'sle_reason', 425, 1364, 1833, 92, limit=30, taborder=230)
        self.add('oval', 'oval_1', 891, 1464, 768, 224)
        self.add('checkbox', 'cbx_printslip', 1765, 1508, 352, 80, text='Print Slip')
        self.add('commandbutton', 'cb_save', 1019, 1520, 242, 104, text='&Save', taborder=240)
        self.add('commandbutton', 'cb_exit', 1289, 1520, 242, 104, text='E&xit', taborder=250)
