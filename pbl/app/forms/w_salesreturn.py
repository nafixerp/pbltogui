"""Estimate — w_salesreturn.

Generated from the PowerBuilder window ``w_salesreturn.srw`` by
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
    name='w_salesreturn',
    title='Estimate',
    width=4983,
    height=1944,
    controls=[],
    tables=['daybook', 'items', 'barcode', 'salesrm', 'salesrd', 'itemsstk', 'clients', 'spdmddet', 'salesm', 'salestype', 'stkandprofit', 'itemsqtype', 'barcodedmd', 'salesd', 'sman', 'accountm', 'itemstmp', 'wstg', 'mctable', 'pcard', 'generali', 'generald', 'userd', 'daybookpart', 'delpart', 'generals'],
    source_path='w_salesreturn.srw',
)


class EstimateForm(GeneratedForm):
    """Estimate"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('singlelineedit', 'st_billno', 389, 4, 411, 84)
        self.add('checkbox', 'cbx_manual', 823, 4, 256, 80, text='Manua&l')
        self.add('singlelineedit', 'sle_sbillno', 1435, 4, 425, 88, limit=15, taborder=10)
        self.add('commandbutton', 'cb_help', 1861, 4, 174, 88, text='&Help')
        self.add('editmask', 'em_date', 2880, 4, 416, 84)
        self.add('statictext', 'st_17', 1207, 12, 219, 76, text='SBill No :')
        self.add('checkbox', 'cbx_updtsys', 2103, 12, 187, 80, text='Sys')
        self.add('checkbox', 'cbx_updtfr', 2318, 12, 197, 80, text='Fr')
        self.add('statictext', 'st_bill', 46, 16, 329, 56, text='Doc No :')
        self.add('statictext', 'st_date', 2565, 16, 293, 56, text='Date :')
        self.add('statictext', 'st_date_m', 2597, 24, 265, 76, text='Znhkw :')
        self.add('editmask', 'em_rate', 389, 96, 411, 84)
        self.add('datawindow', 'dw_billtype', 1435, 96, 425, 88, dataobject='d_billtypecode', taborder=20)
        self.add('editmask', 'em_rate8gm', 2880, 96, 421, 84)
        self.add('statictext', 'st_gratepavan_m', 2469, 104, 389, 76, text=']h~hB3hne :')
        self.add('statictext', 'st_1', 64, 108, 311, 60, text='Rate/gm :')
        self.add('statictext', 'st_21', 1230, 108, 197, 76, text='BType :')
        self.add('statictext', 'st_2', 2542, 108, 315, 60, text='Rate/8 gm :')
        self.add('statictext', 'st_grategm_m', 0, 112, 389, 76, text='kz~hC0~hAEhne :')
        self.add('datawindow', 'dw_1', 389, 188, 402, 88, dataobject='d_cust', taborder=30)
        self.add('datawindow', 'dw_smcode', 2880, 188, 681, 92, dataobject='d_smancode', taborder=50)
        self.add('commandbutton', 'cb_custhelp', 800, 192, 64, 84, text='^')
        self.add('singlelineedit', 'st_custname', 869, 192, 992, 88, limit=30, taborder=40)
        self.add('editmask', 'em_ob', 2098, 192, 398, 88)
        self.add('statictext', 'st_custcode', 59, 200, 315, 72, text='Customer :')
        self.add('statictext', 'st_customer_m', 18, 204, 370, 76, text='Ikv~hC1a~hC0 :')
        self.add('statictext', 'st_ob', 1920, 204, 160, 76, text='OB :')
        self.add('statictext', 'st_smname_m', 2464, 204, 393, 68, text='tkevkvam~hB3 :')
        self.add('statictext', 'st_10', 2569, 204, 288, 76, text='SM Name :')
        self.add('datawindow', 'dw_sale', 23, 296, 4937, 1080, dataobject='d_sale', taborder=60)
        self.add('statictext', 'st_14', 402, 296, 5, 920)
        self.add('statictext', 'st_18', 1257, 296, 5, 1080)
        self.add('statictext', 'st_4', 1445, 296, 5, 1080)
        self.add('statictext', 'st_5', 1737, 296, 5, 992)
        self.add('statictext', 'st_20', 2066, 296, 5, 992)
        self.add('statictext', 'st_6', 2254, 296, 5, 992)
        self.add('statictext', 'st_7', 2546, 296, 5, 992)
        self.add('statictext', 'st_8', 2789, 296, 5, 996)
        self.add('statictext', 'st_16', 3063, 296, 5, 996)
        self.add('statictext', 'st_9', 3337, 296, 5, 996)
        self.add('statictext', 'st_3', 3643, 296, 5, 996)
        self.add('statictext', 'st_11', 3826, 296, 5, 996)
        self.add('statictext', 'st_15', 4142, 296, 5, 996)
        self.add('statictext', 'st_13', 4731, 296, 5, 992)
        self.add('statictext', 'st_12', 4494, 300, 5, 992)
        self.add('statictext', 'st_itemcode_m', 41, 304, 242, 112, text='B`cWw tImUv')
        self.add('statictext', 'st_itemname_m', 416, 304, 471, 112, text='B`cWw t]cv')
        self.add('statictext', 'st_qty_m', 2139, 304, 114, 112, text='F ~hAEw')
        self.add('statictext', 'st_weight_m', 2299, 304, 242, 112, text='Xq~hA1w {Kmw')
        self.add('statictext', 'st_mc_m', 3849, 304, 288, 120, text=']Wn~hA1qen')
        self.add('statictext', 'st_jewl_m', 4741, 304, 137, 112, text='Pz~hC3dn')
        self.add('statictext', 'st_wastage_m', 3360, 308, 279, 112, text=']Wn~hA1pdhv')
        self.add('statictext', 'st_amount_m', 4183, 308, 297, 112, text='XpI')
        self.add('statictext', 'st_stprice_m', 3104, 312, 224, 112, text='I~hC3v hne')
        self.add('statictext', 'st_rate_m', 4530, 312, 192, 112, text='hne')
        self.add('statictext', 'st_stwgt_m', 2560, 316, 219, 112, text='I~hC3v Xq~hA1w')
        self.add('commandbutton', 'cb_add', 32, 1216, 224, 80, text='&Add', taborder=130)
        self.add('commandbutton', 'cb_delete', 261, 1216, 229, 80, text='&Delete', taborder=140)
        self.add('statictext', 'st_kdm', 4160, 1220, 142, 64)
        self.add('statictext', 'st_stktype', 777, 1296, 261, 76)
        self.add('statictext', 'st_stock', 1042, 1304, 384, 60)
        self.add('statictext', 'st_va', 1947, 1304, 311, 60)
        self.add('statictext', 'st_itemadj', 3685, 1304, 306, 60)
        self.add('statictext', 'st_jcode', 4160, 1304, 142, 56)
        self.add('roundrectangle', 'rr_1', 3209, 1404, 576, 276)
        self.add('commandbutton', 'cb_save', 3255, 1424, 485, 108, text='&Save', taborder=120)
        self.add('editmask', 'em_billtotal', 325, 1428, 485, 84)
        self.add('editmask', 'em_taxperc', 1376, 1428, 160, 84, taborder=70)
        self.add('editmask', 'em_staxamt', 1541, 1428, 320, 84, taborder=80)
        self.add('editmask', 'em_astperc', 2427, 1428, 160, 84, taborder=80)
        self.add('editmask', 'em_astamt', 2592, 1428, 320, 84, taborder=90)
        self.add('statictext', 'st_billamt_m', 14, 1436, 306, 76, text='XpI :')
        self.add('statictext', 'st_billtotal', 50, 1440, 261, 60, text='Bill Total :')
        self.add('statictext', 'st_staxamt', 1097, 1440, 261, 64, text='Tax :')
        self.add('statictext', 'st_19', 2149, 1440, 261, 64, text='Cess :')
        self.add('statictext', 'st_taxamt_m', 1074, 1448, 283, 76, text='SmIvkv :')
        self.add('editmask', 'em_discount', 1376, 1524, 485, 84, taborder=90)
        self.add('editmask', 'em_rcvd', 2427, 1524, 485, 84, taborder=100)
        self.add('statictext', 'st_discount', 1047, 1540, 315, 56, text='Discount :')
        self.add('statictext', 'st_discount_m', 1051, 1544, 379, 76, text='Unkv~hA1u~hADv :')
        self.add('statictext', 'st_rcvdamt_m', 2025, 1544, 384, 76, text='sImSp~hAFXv :')
        self.add('statictext', 'st_rcvd', 2039, 1544, 370, 60, text='Paid Amt :')
        self.add('commandbutton', 'cb_exit', 3255, 1544, 485, 108, text='E&xit', taborder=150)
        self.add('editmask', 'em_nettot', 325, 1556, 485, 84)
        self.add('statictext', 'st_nettot', 0, 1572, 325, 60, text='Net Total :')
        self.add('statictext', 'st_netamt_m', 5, 1572, 315, 76, text='sam~hAFw XpI :')
        self.add('editmask', 'em_balance', 1376, 1636, 485, 84)
        self.add('editmask', 'em_cb', 2427, 1636, 485, 84, taborder=110)
        self.add('statictext', 'st_cb', 2171, 1648, 247, 76, text='CB :')
        self.add('statictext', 'st_balance', 1079, 1656, 279, 60, text='Balance :')
        self.add('checkbox', 'cbx_cst', 325, 1660, 361, 84, text='Interstate')
        self.add('statictext', 'st_balance_m', 1061, 1660, 311, 76, text='_m~hA1n :')
        self.add('checkbox', 'cbx_laserprint', 3273, 1696, 402, 76, text='Laser Print')
