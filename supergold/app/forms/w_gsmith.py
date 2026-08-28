"""Transaction — w_gsmith.

Generated from the PowerBuilder window ``w_gsmith.srw`` by
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
    name='w_gsmith',
    title='Transaction',
    width=4928,
    height=2280,
    controls=[],
    tables=['daybook', 'items', 'smithm', 'barcode', 'smithd', 'itemsstk', 'clients', 'repairm', 'accountm', 'clientsgs', 'smithnewwrk', 'itemadj', 'goldsmith', 'orderm', 'orderd', 'stktype', 'sman', 'repaird', 'pmctable', 'generals', 'generali', 'userd', 'daybookpart', 'delpart', 'generald'],
    source_path='w_gsmith.srw',
    grid={'control': 'dw_1', 'dataobject': 'd_smith', 'table': 'codehelp', 'keys': ['code'], 'columns': [{'name': 'code', 'label': 'code', 'type': 'char'}]},
    report={'dataobject': 'd_smith', 'sql': 'SELECT codehelp.code AS codehelp_code FROM codehelp', 'args': [], 'arg_types': {}, 'tables': ['codehelp'], 'columns': [{'name': 'code', 'label': 'code', 'type': 'char'}]},
    opens=['w_stktypeqtype', 'w_gsmthrefhelp', 'w_gsmithnewwrk', 'w_repairhelp', 'w_clientshelp', 'w_smith', 'w_gsmithprint_view', 'w_barcodelist', 'w_mc_smith', 'w_itemhelp', 'w_mcharge', 'w_wastage', 'w_ageinghelp', 'w_osalehelp', 'w_orderitemhelp'],
)


class TransactionForm(GeneratedForm):
    """Transaction"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('line', 'ln_1', 0, 0, 0, 0)
        self.add('dropdownlistbox', 'ddlb_rmno', 1742, 0, 247, 324, text='1', items=['1', '2', '3'], taborder=10)
        self.add('singlelineedit', 'sle_rmno', 1993, 0, 370, 92, taborder=20)
        self.add('editmask', 'em_date', 2734, 0, 407, 96, taborder=40)
        self.add('datawindow', 'dw_smcode', 3611, 0, 677, 88, dataobject='d_smancode', taborder=50)
        self.add('commandbutton', 'cb_rmhelp', 2368, 4, 146, 80, text='&Help')
        self.add('statictext', 'st_bill', 5, 8, 366, 64, text='Doc.  No')
        self.add('singlelineedit', 'st_billno', 398, 8, 439, 92)
        self.add('statictext', 'st_date', 2523, 8, 210, 64, text='Date')
        self.add('checkbox', 'cbx_manual', 850, 12, 265, 80, text='Manual')
        self.add('commandbutton', 'cb_prev', 1111, 12, 137, 88, text='<', taborder=70)
        self.add('commandbutton', 'cb_next', 1248, 12, 137, 88, text='>', taborder=90)
        self.add('statictext', 'st_rmno', 1390, 12, 338, 76, text='Remake No :')
        self.add('statictext', 'st_50', 3397, 12, 178, 76, text='SMan')
        self.add('editmask', 'em_rate', 4517, 12, 306, 96, taborder=60)
        self.add('statictext', 'st_15', 4302, 16, 197, 76, text='Rate')
        self.add('statictext', 'st_custname', 914, 120, 1445, 96)
        self.add('editmask', 'em_custcode', 2373, 120, 96, 96)
        self.add('statictext', 'st_opbal', 2734, 120, 640, 96)
        self.add('singlelineedit', 'sle_refno', 3611, 120, 370, 96, taborder=80)
        self.add('singlelineedit', 'sle_lotno', 4517, 120, 306, 92, limit=10, taborder=100)
        self.add('datawindow', 'dw_1', 398, 124, 439, 92, dataobject='d_smith', taborder=110)
        self.add('commandbutton', 'cb_custhelp', 841, 128, 64, 84, text='^')
        self.add('commandbutton', 'cb_refnohlp', 3986, 128, 146, 88, text='&Help')
        self.add('statictext', 'st_11', 2523, 132, 210, 76, text='Op.Bal')
        self.add('statictext', 'st_26', 4302, 132, 215, 76, text='Lot No')
        self.add('statictext', 'st_custcode', 5, 136, 384, 72, text='Goldsmith')
        self.add('statictext', 'st_28', 3397, 140, 338, 76, text='Ref. No')
        self.add('datawindow', 'dw_sale', 0, 236, 4905, 1004, dataobject='d_gsmith', taborder=120)
        self.add('statictext', 'st_3', 347, 236, 5, 908)
        self.add('statictext', 'st_2', 777, 236, 5, 1000)
        self.add('statictext', 'st_25', 1042, 236, 5, 1000)
        self.add('statictext', 'st_5', 1673, 236, 5, 1000)
        self.add('statictext', 'st_7', 2213, 236, 5, 1000)
        self.add('statictext', 'st_12', 2478, 236, 5, 1000)
        self.add('statictext', 'st_8', 2693, 236, 5, 1000)
        self.add('statictext', 'st_18', 2985, 236, 5, 1000)
        self.add('statictext', 'st_21', 3214, 236, 5, 1000)
        self.add('statictext', 'st_9', 3456, 236, 5, 1000)
        self.add('statictext', 'st_29', 3611, 236, 5, 1000)
        self.add('statictext', 'st_16', 3909, 236, 5, 1000)
        self.add('statictext', 'st_23', 4114, 236, 5, 1000)
        self.add('statictext', 'st_24', 4242, 236, 5, 1000)
        self.add('statictext', 'st_36', 4480, 236, 5, 1000)
        self.add('statictext', 'st_4', 1184, 240, 5, 1000)
        self.add('statictext', 'st_20', 1477, 240, 5, 1000)
        self.add('statictext', 'st_6', 1833, 240, 5, 1000)
        self.add('statictext', 'st_17', 2011, 240, 5, 1000)
        self.add('commandbutton', 'cb_add', 9, 1148, 247, 84, text='&Add')
        self.add('commandbutton', 'cb_delete', 265, 1148, 247, 84, text='&Delete')
        self.add('statictext', 'st_stktype', 517, 1148, 160, 76)
        self.add('editmask', 'em_twgtissued', 608, 1264, 366, 96)
        self.add('editmask', 'em_acidcharge', 1586, 1264, 338, 96, taborder=130)
        self.add('editmask', 'em_twgtrcvd', 2720, 1264, 366, 96)
        self.add('dropdownlistbox', 'ddlb_doctype', 3433, 1264, 475, 400, text='Normal', items=['Normal', 'Unfixing', 'Fixing'], taborder=140)
        self.add('statictext', 'st_30', 3113, 1272, 320, 64, text='Entry Type')
        self.add('statictext', 'st_twgtissu', 0, 1280, 599, 72, text='Total Issued Weight')
        self.add('statictext', 'st_19', 1266, 1280, 334, 64, text='Acid Charge')
        self.add('statictext', 'st_twgtrcvd', 2181, 1280, 567, 72, text='Total Rcvd Weight')
        self.add('roundrectangle', 'rr_1', 3927, 1280, 558, 268)
        self.add('commandbutton', 'cb_save', 3991, 1312, 430, 92, text='&Save')
        self.add('editmask', 'em_wgtbal', 608, 1368, 366, 96)
        self.add('editmask', 'em_discount', 1586, 1368, 338, 96, taborder=150)
        self.add('editmask', 'em_balance', 2720, 1368, 366, 96)
        self.add('editmask', 'em_duedate', 3433, 1368, 471, 96, taborder=30)
        self.add('statictext', 'st_10', 0, 1376, 421, 76, text='Wgt Balance')
        self.add('statictext', 'st_22', 1266, 1376, 297, 64, text='Discount')
        self.add('statictext', 'st_balance', 2181, 1380, 439, 64, text='Amt  Balance')
        self.add('statictext', 'st_31', 3113, 1380, 320, 64, text='Due Date')
        self.add('commandbutton', 'cb_exit', 3991, 1416, 430, 92, text='E&xit')
        self.add('dropdownlistbox', 'ddlb_pmntrcpt', 2181, 1468, 535, 400, text='PAID', items=['PAID', 'RECEIVED'], taborder=280)
        self.add('editmask', 'em_paid', 2720, 1468, 366, 96, taborder=290)
        self.add('editmask', 'em_tmc', 608, 1472, 366, 96)
        self.add('editmask', 'em_tdsperc', 1586, 1472, 146, 96, taborder=160)
        self.add('editmask', 'em_tds', 1737, 1472, 338, 96, taborder=170)
        self.add('statictext', 'st_tmc', 0, 1484, 672, 64, text='Total Making Charge')
        self.add('statictext', 'st_1', 1266, 1484, 174, 64, text='TDS')
        self.add('commandbutton', 'cb_newwork', 3991, 1556, 430, 100, text='&New Work')
        self.add('editmask', 'em_clbalance', 2720, 1568, 366, 96)
        self.add('editmask', 'em_tcsperc', 608, 1572, 146, 96, taborder=180)
        self.add('editmask', 'em_tcsamt', 759, 1572, 338, 96, taborder=190)
        self.add('editmask', 'em_taxperc', 1586, 1572, 146, 96, taborder=200)
        self.add('editmask', 'em_taxamt', 1737, 1572, 338, 96, taborder=210)
        self.add('statictext', 'st_14', 2181, 1572, 384, 76, text='Cl. Balance')
        self.add('statictext', 'st_37', 0, 1584, 265, 64, text='T.C.S')
        self.add('statictext', 'st_tax', 1266, 1584, 265, 64, text='TAX')
        self.add('statictext', 'st_warn', 3150, 1660, 649, 112)
        self.add('singlelineedit', 'sle_mobile', 608, 1668, 622, 92, limit=20)
        self.add('singlelineedit', 'sle_pos', 2720, 1668, 567, 88, limit=60, taborder=230)
        self.add('datawindow', 'dw_state', 1586, 1672, 567, 88, dataobject='d_state_sel', taborder=220)
        self.add('statictext', 'st_27', 0, 1680, 251, 76, text='Mobile')
        self.add('statictext', 'st_40', 2181, 1680, 402, 76, text='Supply Place')
        self.add('statictext', 'st_state', 1266, 1692, 297, 76, text='State')
        self.add('singlelineedit', 'sle_transportmode', 608, 1764, 622, 88, limit=60, taborder=240)
        self.add('singlelineedit', 'sle_vehno', 1586, 1764, 567, 88, limit=60, taborder=250)
        self.add('singlelineedit', 'sle_purpose', 2720, 1764, 567, 88, limit=60, taborder=260)
        self.add('statictext', 'st_32', 0, 1776, 603, 76, text='Transportation Mode')
        self.add('statictext', 'st_33', 1266, 1776, 334, 80, text='Vehicle No')
        self.add('statictext', 'st_34', 2181, 1780, 334, 80, text='Purpose')
        self.add('multilineedit', 'mle_note', 608, 1856, 1550, 196, taborder=270)
        self.add('singlelineedit', 'sle_person', 2720, 1860, 622, 92, limit=20, taborder=300)
        self.add('statictext', 'st_35', 0, 1880, 585, 76, text='Note')
        self.add('statictext', 'st_13', 2181, 1880, 251, 76, text='Person')
        self.add('checkbox', 'cbx_sendsms', 3374, 1952, 402, 80, text='Send SMS')
        self.add('checkbox', 'cbx_taxreverse', 2720, 1964, 613, 80, text='Tax Reverse Charge')
        self.add('checkbox', 'cbx_createbc', 3374, 1972, 485, 80, text='Create BCode')
        self.add('commandbutton', 'cb_bcstk', 0, 1984, 229, 80, text='BCStk')
        self.add('checkbox', 'cbx_interstate', 2720, 2060, 379, 80, text='Interstate')
