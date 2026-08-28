"""New — w_diamond_purchase.

Generated from the PowerBuilder window ``w_diamond_purchase.srw`` by
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
    name='w_diamond_purchase',
    title='New',
    width=4946,
    height=2076,
    controls=[],
    tables=['items', 'daybook', 'itemsstk', 'smithd', 'barcode', 'purchaserd', 'purchasem', 'purchased', 'barcode_dmddet', 'clients', 'smithm', 'advafter', 'purchased_dmddet', 'purchaserm', 'barcodedmd', 'orderm', 'clientsgs', 'generali', 'generals', 'generald', 'daybookpart', 'delpart', 'userd'],
    source_path='w_diamond_purchase.srw',
    opens=['w_stktypehlp', 'w_camera', 'w_clientshelp', 'w_osalehelp', 'w_sucu', 'w_exchange', 'w_gsmithprint_view', 'w_purchase_view', 'w_barcodelist', 'w_itemhelp', 'w_itemtmphelp', 'w_stktypeqtype', 'w_rmno'],
)


class NewForm(GeneratedForm):
    """New"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('statictext', 'st_grno', 352, 0, 439, 84)
        self.add('checkbox', 'cbx_nobc', 850, 0, 215, 80, text='No BC')
        self.add('singlelineedit', 'sle_billno', 1339, 0, 389, 84, taborder=10)
        self.add('editmask', 'em_date', 2025, 0, 425, 88, taborder=20)
        self.add('singlelineedit', 'sle_ordno', 2885, 0, 375, 88, limit=10, taborder=30)
        self.add('commandbutton', 'cb_1', 3269, 0, 146, 88, text='&Help')
        self.add('statictext', 'st_1', 1070, 4, 261, 72, text='Bill No  :')
        self.add('editmask', 'em_mcperc', 4407, 4, 178, 88, taborder=90)
        self.add('statictext', 'st_bill', 9, 8, 311, 64, text='Doc. No.')
        self.add('statictext', 'st_11', 2519, 8, 384, 76, text='To Order No')
        self.add('checkbox', 'cbx_setsalesamt', 3593, 8, 466, 80, text='Set Sales Amt')
        self.add('statictext', 'st_date', 1833, 12, 187, 64, text='Date')
        self.add('statictext', 'st_34', 4142, 16, 270, 64, text='MC % < :')
        self.add('datawindow', 'dw_1', 352, 92, 425, 92, dataobject='d_sucu', taborder=50)
        self.add('commandbutton', 'cb_allocstamt', 3593, 92, 402, 92, text='Aloc St.Amt', taborder=40)
        self.add('commandbutton', 'cb_custhelp', 795, 96, 64, 92, text='^')
        self.add('singlelineedit', 'st_suppname', 864, 96, 864, 92, limit=30, taborder=70)
        self.add('datawindow', 'dw_smcode', 2885, 96, 677, 88, dataobject='d_smancode', taborder=80)
        self.add('editmask', 'em_stoneperc', 4407, 96, 178, 88, taborder=60)
        self.add('editmask', 'em_ob', 2025, 100, 425, 88)
        self.add('statictext', 'st_smcode', 2519, 104, 261, 64, text='SMan')
        self.add('statictext', 'st_custcode', 9, 108, 343, 72, text='Supplier')
        self.add('statictext', 'st_33', 4142, 108, 265, 64, text='Stone % :')
        self.add('statictext', 'st_12', 1833, 112, 137, 76, text='OB')
        self.add('datawindow', 'dw_purchase', 0, 192, 4919, 760, dataobject='d_diamond_purchase', taborder=100)
        self.add('statictext', 'st_10', 283, 192, 5, 668)
        self.add('statictext', 'st_3', 649, 192, 5, 760)
        self.add('statictext', 'st_4', 887, 192, 5, 760)
        self.add('statictext', 'st_18', 1102, 192, 5, 760)
        self.add('statictext', 'st_5', 1239, 192, 5, 760)
        self.add('statictext', 'st_29', 1344, 192, 5, 760)
        self.add('statictext', 'st_13', 1563, 192, 5, 760)
        self.add('statictext', 'st_6', 1733, 192, 5, 760)
        self.add('statictext', 'st_7', 1938, 192, 5, 760)
        self.add('statictext', 'st_8', 2139, 192, 5, 760)
        self.add('statictext', 'st_35', 2290, 192, 5, 760)
        self.add('statictext', 'st_9', 2523, 192, 5, 760)
        self.add('statictext', 'st_19', 2743, 192, 5, 760)
        self.add('statictext', 'st_38', 2894, 192, 5, 760)
        self.add('statictext', 'st_15', 3150, 192, 5, 760)
        self.add('statictext', 'st_27', 3287, 192, 5, 760)
        self.add('statictext', 'st_32', 3401, 192, 5, 760)
        self.add('statictext', 'st_36', 3557, 192, 5, 760)
        self.add('statictext', 'st_17', 3781, 192, 5, 760)
        self.add('statictext', 'st_30', 3991, 192, 5, 760)
        self.add('statictext', 'st_31', 4265, 192, 5, 760)
        self.add('statictext', 'st_39', 4521, 192, 5, 760)
        self.add('commandbutton', 'cb_add', 0, 860, 206, 72, text='&Add', taborder=180)
        self.add('commandbutton', 'cb_delete', 201, 860, 197, 72, text='&Delete', taborder=190)
        self.add('statictext', 'st_stktype', 645, 864, 87, 76)
        self.add('statictext', 'st_kdm', 754, 864, 169, 76)
        self.add('picture', 'p_photo', 3918, 964, 686, 544)
        self.add('datawindow', 'dw_dmd', 0, 968, 2971, 588, dataobject='d_diamond_purchase_dmds', taborder=130)
        self.add('multilineedit', 'mle_note', 2990, 968, 859, 588, limit=50, taborder=140)
        self.add('statictext', 'st_22', 928, 972, 5, 584)
        self.add('statictext', 'st_23', 1157, 972, 5, 584)
        self.add('statictext', 'st_24', 1312, 972, 5, 584)
        self.add('statictext', 'st_25', 1559, 972, 5, 584)
        self.add('statictext', 'st_26', 1819, 972, 5, 584)
        self.add('statictext', 'st_28', 2144, 972, 5, 584)
        self.add('statictext', 'st_37', 2537, 972, 5, 584)
        self.add('statictext', 'st_20', 690, 1036, 5, 516)
        self.add('statictext', 'st_21', 343, 1040, 5, 440)
        self.add('commandbutton', 'cb_dmdadd', 0, 1476, 197, 72, text='Add', taborder=200)
        self.add('commandbutton', 'cb_dmddel', 197, 1476, 210, 72, text='Delete', taborder=230)
        self.add('commandbutton', 'cb_ok', 421, 1476, 210, 72, text='OK', taborder=220)
        self.add('commandbutton', 'cb_photo', 4101, 1496, 411, 80, text='Select Photo', taborder=250)
        self.add('checkbox', 'cbx_showcamera', 3918, 1512, 178, 52, text='Cam')
        self.add('commandbutton', 'cb_noteok', 3296, 1552, 215, 64, text='ok')
        self.add('editmask', 'em_billtotal', 357, 1560, 407, 96)
        self.add('editmask', 'em_taxperc', 1253, 1564, 119, 96, taborder=110)
        self.add('editmask', 'em_tax', 1371, 1564, 407, 96, taborder=120)
        self.add('editmask', 'em_exchange', 2542, 1564, 407, 96)
        self.add('checkbox', 'cbx_taxexternal', 1787, 1568, 256, 80, text='External')
        self.add('statictext', 'st_billtotal', 27, 1572, 329, 76, text='Bill Total')
        self.add('statictext', 'st_14', 1083, 1572, 155, 76, text='Tax')
        self.add('statictext', 'st_exchange', 2126, 1576, 416, 76, text='P.Return Amt.')
        self.add('roundrectangle', 'rr_1', 4014, 1580, 558, 344)
        self.add('commandbutton', 'cb_exchange', 4078, 1604, 434, 96, text='&Return', taborder=210)
        self.add('checkbox', 'cbx_nodmdamt', 3118, 1628, 699, 72, text='Dont Add Dmd Amt')
        self.add('editmask', 'em_nettot', 357, 1660, 407, 96)
        self.add('editmask', 'em_others', 1371, 1664, 407, 96, taborder=150)
        self.add('editmask', 'em_pamt', 2542, 1664, 407, 96, taborder=160)
        self.add('statictext', 'st_nettot', 27, 1668, 338, 76, text='Net Total')
        self.add('statictext', 'st_discount', 1083, 1672, 242, 76, text='Others')
        self.add('statictext', 'st_rcvd', 2126, 1676, 329, 76, text='Paid amt')
        self.add('commandbutton', 'cb_save', 4078, 1700, 434, 96, text='&Save', taborder=240)
        self.add('checkbox', 'cbx_nodmdwgt', 3118, 1712, 699, 72, text='Dont Add Dmd Wgt in gm')
        self.add('editmask', 'em_balance', 357, 1764, 407, 96)
        self.add('editmask', 'em_cb', 1371, 1764, 407, 96)
        self.add('editmask', 'em_duedate', 2542, 1764, 407, 96, taborder=170)
        self.add('statictext', 'st_balance', 27, 1772, 325, 76, text='Balance')
        self.add('statictext', 'st_16', 1083, 1776, 155, 76, text='CB')
        self.add('statictext', 'st_2', 2126, 1780, 297, 76, text='Duedate')
        self.add('checkbox', 'cbx_keepacinwgt', 3118, 1796, 795, 72, text='Keep A/c in Weight')
        self.add('commandbutton', 'cb_exit', 4078, 1796, 434, 96, text='E&xit', taborder=260)
        self.add('checkbox', 'cbx_updtfr', 2542, 1880, 215, 76, text='&Fr')
        self.add('checkbox', 'cbx_roundoffitemwiseamt', 3118, 1880, 805, 80, text='Round off Itemwise Amount')
        self.add('checkbox', 'cbx_cst', 1371, 1888, 384, 84, text='Interstate')
