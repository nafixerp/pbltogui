"""Provide Access — w_useraccess.

Generated from the PowerBuilder window ``w_useraccess.srw`` by
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
    name='w_useraccess',
    title='Provide Access',
    width=4215,
    height=2184,
    controls=[],
    tables=['userd', 'userm'],
    source_path='w_useraccess.srw',
)


class ProvideAccessForm(GeneratedForm):
    """Provide Access"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('statictext', 'st_status', 3177, 0, 489, 68)
        self.add('datawindow', 'dw_user', 2235, 4, 782, 88, dataobject='d_usercode', taborder=10)
        self.add('statictext', 'st_1', 9, 12, 1792, 76, text='Select the menu items to block for this user')
        self.add('statictext', 'st_2', 1966, 16, 247, 76, text='User :')
        self.add('checkbox', 'cbx_ratesetup', 3090, 76, 539, 80, text='Allow Rate Setup')
        self.add('singlelineedit', 'sle_name', 2235, 96, 795, 92, limit=30, taborder=20)
        self.add('listbox', 'lb_items', 5, 108, 1810, 1244, taborder=180)
        self.add('statictext', 'st_4', 1847, 112, 366, 76, text='User Name :')
        self.add('checkbox', 'cbx_bcstatusedit', 3090, 160, 777, 72, text='Allow Barcode Status Edit')
        self.add('singlelineedit', 'sle_code', 2235, 192, 485, 92, limit=10, taborder=30)
        self.add('statictext', 'st_5', 1865, 208, 347, 76, text='User Code :')
        self.add('checkbox', 'cbx_bcdetailsedit', 3090, 232, 786, 72, text='Allow Barcode Details Edit')
        self.add('singlelineedit', 'sle_psw', 2235, 288, 485, 92, limit=10, taborder=40)
        self.add('statictext', 'st_3', 1883, 304, 329, 76, text='Password :')
        self.add('checkbox', 'cbx_bcdetailsdelete', 3090, 304, 850, 72, text='Allow Barcode Details Delete')
        self.add('checkbox', 'cbx_alloweditbcdetinsales', 3090, 376, 882, 80, text='Allow Edit BC Details in Sales')
        self.add('checkbox', 'cbx_onlineedit', 1838, 384, 667, 76, text='Dont allow online Edit')
        self.add('checkbox', 'cbx_allowbccreationinjewlentry', 3090, 444, 919, 80, text='Allow BC Creation in Jewl Entry')
        self.add('checkbox', 'cbx_mastedit', 1838, 460, 681, 76, text='Dont allow Master Edit')
        self.add('checkbox', 'cbx_alloworderblock', 3090, 516, 777, 80, text='Allow Order Block Opn')
        self.add('checkbox', 'cbx_opbaledit', 1838, 532, 1029, 76, text='Dont allow Master Op. Balance Edit')
        self.add('checkbox', 'cbx_kuricollnedit', 3090, 592, 896, 72, text='Allow Kuri/Scheme Colln Edit')
        self.add('checkbox', 'cbx_mastdel', 1838, 612, 745, 76, text='Dont allow Master Delete')
        self.add('checkbox', 'cbx_itemadjdifftype', 3090, 664, 878, 80, text='Allow Item Adj. Different types')
        self.add('checkbox', 'cbx_journl_alter', 1838, 692, 704, 76, text='Dont allow Journal Alter')
        self.add('checkbox', 'cbx_itemadjinsale', 3090, 740, 713, 80, text='Allow Item Adj. in Sales')
        self.add('checkbox', 'cbx_prevdateentry', 1838, 768, 882, 76, text='Dont allow Previous date entry')
        self.add('checkbox', 'cbx_allowsalescancel', 3090, 816, 896, 72, text='Allow Sales Cancellation')
        self.add('checkbox', 'cbx_afterdateentry', 1838, 840, 882, 72, text='Dont allow After date entry')
        self.add('checkbox', 'cbx_allowsalesestcancel', 3090, 892, 992, 72, text='Allow Sales Estimate Cancellation')
        self.add('checkbox', 'cbx_nowgt', 1838, 908, 672, 76, text='Dont show item wgt')
        self.add('checkbox', 'cbx_allowprevnextinsales', 3090, 968, 1083, 72, text='Allow Prev / Next buttons in Sales')
        self.add('checkbox', 'cbx_credit', 1838, 984, 549, 76, text='Dont allow Credit')
        self.add('checkbox', 'cbx_allowpurchconfirmation', 3090, 1044, 1097, 76, text='Allow Purchase Confirmation')
        self.add('checkbox', 'cbx_nosuppbalinsemi', 1838, 1068, 1024, 80, text="Don't Show Supplier Balance in Semi")
        self.add('checkbox', 'cbx_allowpmntconfirmation', 3090, 1116, 1097, 76, text='Allow Payment Confirmation')
        self.add('checkbox', 'cbx_nopartybalinsemi', 1838, 1144, 1024, 68, text="Don't Show Party Balance in Semi")
        self.add('checkbox', 'cbx_allowjewlmanualdocno', 3090, 1188, 1097, 76, text='Allow Jewl/Smith Manual Doc No')
        self.add('checkbox', 'cbx_nosmithbalinsemi', 1838, 1212, 1024, 80, text="Don't Show Smith Balance in Semi")
        self.add('checkbox', 'cbx_showdiscinrcpt', 3090, 1284, 686, 76, text='Show Discount in Rcpt')
        self.add('checkbox', 'cbx_nosstaffbal', 1838, 1288, 1024, 80, text="Don't Show Staff Balance")
        self.add('checkbox', 'cbx_showdiscinpmnt', 3090, 1352, 704, 76, text='Show Discount in Pmnt')
        self.add('commandbutton', 'cb_del', 9, 1360, 265, 108, text='&Delete', taborder=90)
        self.add('commandbutton', 'cb_selemast', 279, 1360, 635, 108, text='Select All Masters', taborder=110)
        self.add('commandbutton', 'cb_selerep', 919, 1360, 635, 108, text='Select All Reports', taborder=150)
        self.add('commandbutton', 'cb_refresh', 1563, 1360, 256, 108, text='Refresh', taborder=100)
        self.add('checkbox', 'cbx_nototstock', 1838, 1360, 690, 76, text='Dont Show Total Stock')
        self.add('checkbox', 'cbx_showprinteditinconfirm', 3090, 1420, 951, 76, text='Show Edit, Update in Confirmation')
        self.add('commandbutton', 'cb_seletran', 279, 1476, 635, 108, text='Select All Transactions', taborder=120)
        self.add('commandbutton', 'cb_seleutil', 919, 1476, 635, 108, text='Select All Utilities', taborder=111)
        self.add('checkbox', 'cbx_adminbutton', 3090, 1492, 727, 72, text='Show Admin Button')
        self.add('editmask', 'em_minvaperc', 2455, 1496, 361, 92, taborder=70)
        self.add('statictext', 'st_9', 1774, 1504, 672, 76, text='Minimum VA% Allowed :')
        self.add('checkbox', 'cbx_showpartybal', 3090, 1564, 850, 72, text='Show Party Balance in Trans')
        self.add('commandbutton', 'cb_selecancel', 279, 1592, 635, 108, text='Select All Cancel', taborder=140)
        self.add('commandbutton', 'cb_seleedit', 919, 1592, 635, 108, text='Select All Edit', taborder=130)
        self.add('editmask', 'em_maxcredit', 2455, 1592, 361, 92, taborder=60)
        self.add('statictext', 'st_6', 1865, 1600, 581, 76, text='Max. Credit Allowed :')
        self.add('checkbox', 'cbx_showavgpcostva', 3090, 1636, 974, 72, text='Show Avg PCost/VA% in Sales')
        self.add('editmask', 'em_maxdisc', 2455, 1688, 361, 92, taborder=50)
        self.add('statictext', 'st_7', 1879, 1696, 567, 76, text='Max Discount / Gm :')
        self.add('checkbox', 'cbx_showcostdetinbclist', 3090, 1708, 974, 72, text='Show Cost Details in BC List')
        self.add('commandbutton', 'cb_add', 238, 1768, 325, 108, text='&Add', taborder=170)
        self.add('commandbutton', 'cb_edit', 576, 1768, 325, 108, text='&Edit', taborder=80)
        self.add('commandbutton', 'cb_delete', 919, 1768, 325, 108, text='De&lete', taborder=160)
        self.add('commandbutton', 'cb_save', 1257, 1768, 325, 108, text='&Save', taborder=70)
        self.add('editmask', 'em_maxdiscperc', 2455, 1784, 361, 92, taborder=60)
        self.add('checkbox', 'cbx_readonly', 3689, 1784, 361, 80, text='Read Only')
        self.add('checkbox', 'cbx_bccompulsory', 3090, 1788, 535, 76, text='BC Compulsory')
        self.add('statictext', 'st_10', 1879, 1792, 567, 76, text='Max Discount % :')
        self.add('editmask', 'em_bcadjustablewgt', 2455, 1880, 361, 92, taborder=60)
        self.add('statictext', 'st_8', 1623, 1892, 823, 76, text='Maximum Adjustable wgt in BC :')
