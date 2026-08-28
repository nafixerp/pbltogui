"""Item Details — w_item.

Generated from the PowerBuilder window ``w_item.srw`` by
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
    name='w_item',
    title='Item Details',
    width=3415,
    height=2164,
    controls=[],
    tables=['items', 'itemadj', 'clients', 'salesd', 'salesrd', 'purchased', 'purchaserd', 'orderd', 'repaird', 'smithd', 'refineryd', 'generals', 'userd'],
    source_path='w_item.srw',
    grid={'control': 'dw_smith', 'dataobject': 'd_smith', 'table': 'codehelp', 'keys': ['code'], 'columns': [{'name': 'code', 'label': 'code', 'type': 'char'}]},
    report={'dataobject': 'd_smith', 'sql': 'SELECT codehelp.code AS codehelp_code FROM codehelp', 'args': [], 'arg_types': {}, 'tables': ['codehelp'], 'columns': [{'name': 'code', 'label': 'code', 'type': 'char'}]},
)


class ItemDetailsForm(GeneratedForm):
    """Item Details"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('statictext', 'st_head', 978, 0, 1595, 76, text='Add New Item')
        self.add('singlelineedit', 'sle_code', 855, 100, 398, 88, limit=10, taborder=10)
        self.add('singlelineedit', 'sle_desc', 2103, 100, 846, 88, limit=20, taborder=20)
        self.add('statictext', 'st_1', 329, 104, 498, 72, text='Code')
        self.add('statictext', 'st_2', 1669, 104, 411, 72, text='Description :')
        self.add('datawindow', 'dw_grp', 855, 192, 800, 88, dataobject='d_itemgrpcode', taborder=50)
        self.add('singlelineedit', 'sle_regional', 2103, 192, 846, 88, limit=20, taborder=30)
        self.add('commandbutton', 'cb_selfont', 2967, 192, 224, 92, text='Sel Font', taborder=40)
        self.add('commandbutton', 'cb_langhelp', 3195, 196, 174, 84, text='&Help')
        self.add('commandbutton', 'cb_newgrp', 1664, 200, 137, 80, text='New')
        self.add('statictext', 'st_6', 1810, 200, 270, 76, text='Regional :')
        self.add('statictext', 'st_10', 329, 212, 498, 76, text='Group')
        self.add('datawindow', 'dw_subgrp', 855, 288, 800, 88, dataobject='d_itemsubgrpcode', taborder=60)
        self.add('checkbox', 'cbx_stkinnos', 2107, 288, 640, 80, text='Stoc&k in nos only')
        self.add('commandbutton', 'cb_newsubgrp', 1664, 292, 137, 80, text='New')
        self.add('statictext', 'st_26', 329, 304, 498, 76, text='Sub Group')
        self.add('editmask', 'em_opcost', 855, 380, 398, 96, taborder=70)
        self.add('editmask', 'em_cost', 2103, 380, 398, 96, taborder=80)
        self.add('groupbox', 'gb_type', 2574, 380, 370, 436, text='Item type')
        self.add('statictext', 'st_3', 329, 392, 498, 76, text='Op. Cost')
        self.add('statictext', 'st_4', 1623, 392, 475, 76, text='Current Cos')
        self.add('radiobutton', 'rb_gold', 2615, 452, 279, 64, text='&Gold')
        self.add('dropdownlistbox', 'ddlb_dmdplt', 2958, 460, 366, 528, items=['Diamond', 'Platinum', 'Gold', 'Silver', 'Others', 'Color Stone', 'Watch'], taborder=300)
        self.add('groupbox', 'gb_1', 1518, 472, 1029, 252, text='ReOrderLevel (Weight/Qty)')
        self.add('editmask', 'em_wastage', 855, 508, 398, 92, taborder=90)
        self.add('statictext', 'st_8', 329, 516, 535, 84, text='Wastage(gm/8gm)')
        self.add('radiobutton', 'rb_silver', 2615, 524, 293, 60, text='Sil&ver')
        self.add('editmask', 'em_rollower', 2103, 540, 279, 84, taborder=160)
        self.add('editmask', 'em_rollowerqty', 2386, 540, 151, 84, taborder=170)
        self.add('statictext', 'st_9', 1623, 548, 475, 76, text='Minimum Limit')
        self.add('radiobutton', 'rb_platinum', 2615, 588, 311, 80, text='Platinum')
        self.add('editmask', 'em_mcrate', 855, 616, 398, 92, taborder=100)
        self.add('editmask', 'em_rolupper', 2103, 628, 279, 84, taborder=180)
        self.add('editmask', 'em_rolupperqty', 2386, 628, 151, 84, taborder=190)
        self.add('statictext', 'st_7', 329, 632, 498, 76, text='M.C.(Amt/gm)')
        self.add('statictext', 'st_5', 1623, 636, 475, 76, text='Maximum Limit')
        self.add('radiobutton', 'rb_dmd', 2615, 660, 311, 80, text='Diamond')
        self.add('editmask', 'em_vaperc', 855, 724, 398, 92, taborder=110)
        self.add('editmask', 'em_vaperqty', 1257, 724, 256, 92, taborder=120)
        self.add('statictext', 'st_18', 329, 728, 498, 76, text='VA % / VA(Qty)')
        self.add('editmask', 'em_touch', 2103, 732, 398, 84, taborder=200)
        self.add('statictext', 'st_12', 1623, 736, 475, 76, text='Touch')
        self.add('radiobutton', 'rb_others', 2615, 736, 311, 72, text='&Others')
        self.add('editmask', 'em_defqty', 855, 824, 398, 92, taborder=130)
        self.add('statictext', 'st_11', 329, 828, 498, 76, text='Default Qty')
        self.add('singlelineedit', 'sle_frcode', 2103, 828, 398, 88, limit=10, taborder=210)
        self.add('checkbox', 'cbx_ornament', 2624, 832, 411, 60, text='O&rnament')
        self.add('statictext', 'st_frcode', 1623, 840, 475, 76, text='Front Code')
        self.add('checkbox', 'cbx_reserve', 2624, 904, 325, 60, text='Reserved')
        self.add('datawindow', 'dw_smith', 2103, 924, 439, 92, dataobject='d_smith', taborder=220)
        self.add('datawindow', 'dw_qtype', 855, 928, 539, 88, dataobject='d_iqtypecode', taborder=140)
        self.add('commandbutton', 'cb_custhelp', 2542, 928, 59, 84, text='^')
        self.add('statictext', 'st_14', 329, 932, 498, 76, text='Def. Purity')
        self.add('statictext', 'st_60', 1623, 936, 475, 76, text='Def. Smith')
        self.add('checkbox', 'cbx_taxinternal', 2944, 972, 402, 80, text='Tax Internal')
        self.add('checkbox', 'cbx_taxable', 2624, 980, 288, 60, text='Taxable')
        self.add('editmask', 'em_stonemarg', 2103, 1024, 398, 92, taborder=230)
        self.add('datawindow', 'dw_stktype', 855, 1028, 539, 88, dataobject='d_stktypecode', taborder=150)
        self.add('statictext', 'st_17', 1623, 1036, 475, 76, text='Stone Margin %')
        self.add('statictext', 'st_13', 329, 1040, 498, 76, text='Def. Stock Type')
        self.add('checkbox', 'cbx_cessinternal', 2944, 1048, 430, 80, text='Cess Internal')
        self.add('checkbox', 'cbx_disable', 2624, 1056, 279, 60, text='Disable')
        self.add('editmask', 'em_rate', 855, 1124, 398, 92, taborder=240)
        self.add('editmask', 'em_wsrate', 2103, 1124, 398, 92, taborder=250)
        self.add('statictext', 'st_28', 1623, 1132, 475, 76, text='WS Rate')
        self.add('editmask', 'em_smithmc', 2926, 1132, 338, 92, taborder=310)
        self.add('statictext', 'st_20', 329, 1136, 498, 80, text='Sales Rate')
        self.add('statictext', 'st_21', 2592, 1144, 329, 80, text='Smith MC')
        self.add('statictext', 'st_15', 329, 1224, 498, 76, text='Footer English')
        self.add('singlelineedit', 'sle_footer_e', 855, 1224, 1646, 88, limit=40, taborder=280)
        self.add('editmask', 'em_jewlmc', 2926, 1224, 338, 92, taborder=320)
        self.add('statictext', 'st_22', 2592, 1240, 329, 80, text='Jewl MC')
        self.add('singlelineedit', 'sle_footer_m', 855, 1316, 1646, 88, limit=40, taborder=290)
        self.add('singlelineedit', 'sle_shedule', 2926, 1316, 338, 88, limit=10, taborder=330)
        self.add('statictext', 'st_23', 2592, 1320, 329, 80, text='Schedule')
        self.add('statictext', 'st_16', 329, 1324, 498, 76, text='Footer(Regional)')
        self.add('singlelineedit', 'sle_vatcode', 2926, 1404, 338, 88, limit=10, taborder=340)
        self.add('editmask', 'em_prate', 855, 1408, 398, 92, taborder=260)
        self.add('statictext', 'st_32', 1623, 1408, 475, 80, text='BC Sticker Wgt')
        self.add('editmask', 'em_stickerwgt', 2103, 1408, 398, 84, taborder=390)
        self.add('statictext', 'st_24', 2592, 1412, 329, 80, text='HSN Code')
        self.add('statictext', 'st_29', 329, 1420, 498, 80, text='Purchase Rate')
        self.add('datawindow', 'dw_billtype', 2103, 1496, 425, 88, dataobject='d_billtypecode', taborder=270)
        self.add('singlelineedit', 'sle_saccode', 2926, 1496, 338, 88, limit=10, taborder=350)
        self.add('statictext', 'st_30', 2592, 1504, 329, 80, text='SAC Code')
        self.add('statictext', 'st_31', 1623, 1508, 475, 72, text='BType')
        self.add('checkbox', 'cbx_printvaamt', 855, 1520, 709, 52, text='Always Print VA Amt')
        self.add('editmask', 'em_stktouch', 2926, 1588, 338, 84, taborder=360)
        self.add('checkbox', 'cbx_bccompulsory', 855, 1592, 686, 72, text='Barcode Compulsory')
        self.add('statictext', 'st_25', 2592, 1596, 389, 80, text='Stock Touch')
        self.add('checkbox', 'cbx_dontshowinstkrep', 1586, 1660, 832, 68, text='Dont Show In Stock Reports')
        self.add('checkbox', 'cbx_stonemust', 855, 1672, 686, 72, text='Stone Compulsory')
        self.add('editmask', 'em_jewltouch', 2926, 1672, 338, 84, taborder=370)
        self.add('statictext', 'st_27', 2592, 1680, 347, 80, text='Jewl Touch')
        self.add('checkbox', 'cbx_nodisc', 855, 1752, 475, 80, text='No Discount')
        self.add('checkbox', 'cbx_vaoffer', 1586, 1760, 832, 68, text='No VA or MC ( Offer )')
        self.add('editmask', 'em_minvap', 2926, 1760, 338, 84, taborder=380)
        self.add('statictext', 'st_19', 2592, 1764, 347, 80, text='Min VA%')
        self.add('roundrectangle', 'rr_1', 709, 1868, 2258, 172)
        self.add('commandbutton', 'cb_rename', 192, 1896, 430, 96, text='Code Rename')
        self.add('commandbutton', 'cb_add', 745, 1900, 283, 104, text='&Add', taborder=400)
        self.add('commandbutton', 'cb_edit', 1042, 1900, 283, 104, text='&Edit', taborder=410)
        self.add('commandbutton', 'cb_delete', 1339, 1900, 283, 104, text='&Delete', taborder=420)
        self.add('commandbutton', 'cb_1', 1705, 1900, 283, 104, text='VA Set', taborder=430)
        self.add('commandbutton', 'cb_save', 2053, 1900, 283, 104, text='&Save', taborder=440)
        self.add('commandbutton', 'cb_cancel', 2350, 1900, 283, 104, text='&Cancel', taborder=450)
        self.add('commandbutton', 'cb_exit', 2647, 1900, 283, 104, text='E&xit', taborder=460)
