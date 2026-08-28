"""Estimate — w_purchase_ret.

Generated from the PowerBuilder window ``w_purchase_ret.srw`` by
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
    name='w_purchase_ret',
    title='Estimate',
    width=4064,
    height=1824,
    controls=[],
    tables=['daybook', 'items', 'purchaserd', 'purchaserm', 'itemsstk', 'barcode', 'stkandprofit', 'salestype', 'clients', 'barcodedmd', 'sman', 'accountm', 'itemsqtype', 'generali', 'generals', 'userd', 'daybookpart', 'delpart'],
    source_path='w_purchase_ret.srw',
)


class EstimateForm(GeneratedForm):
    """Estimate"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('statictext', 'st_grno', 334, 8, 439, 92)
        self.add('statictext', 'st_1', 1006, 8, 247, 76, text='Date :')
        self.add('editmask', 'em_date', 1271, 8, 439, 92, taborder=10)
        self.add('singlelineedit', 'sle_billno', 2021, 8, 421, 92, taborder=20)
        self.add('statictext', 'st_12', 2519, 8, 297, 76, text='Bill Date :')
        self.add('editmask', 'em_billdate', 2825, 8, 439, 92, taborder=30)
        self.add('statictext', 'st_bill', 9, 16, 306, 64, text='Doc. No. :')
        self.add('statictext', 'st_11', 1755, 16, 251, 76, text='Bill No :')
        self.add('datawindow', 'dw_1', 334, 112, 430, 96, dataobject='d_sucu', taborder=40)
        self.add('singlelineedit', 'st_suppname', 841, 116, 869, 92, limit=30, taborder=50)
        self.add('editmask', 'em_ob', 2025, 116, 421, 92)
        self.add('datawindow', 'dw_smcode', 2825, 120, 677, 88, dataobject='d_smancode', taborder=60)
        self.add('statictext', 'st_custcode', 14, 124, 302, 72, text='Supplier :')
        self.add('commandbutton', 'cb_custhelp', 773, 124, 64, 84, text='^')
        self.add('statictext', 'st_ob', 1833, 128, 174, 80, text='OB :')
        self.add('statictext', 'st_smcode', 2523, 136, 293, 64, text='SMan :')
        self.add('datawindow', 'dw_purchase', 0, 228, 4037, 1072, dataobject='d_exchange1', taborder=70)
        self.add('statictext', 'st_10', 357, 228, 5, 980)
        self.add('statictext', 'st_14', 1042, 228, 5, 1068)
        self.add('statictext', 'st_3', 1243, 228, 5, 1068)
        self.add('statictext', 'st_4', 1495, 228, 5, 1068)
        self.add('statictext', 'st_5', 1659, 228, 5, 1068)
        self.add('statictext', 'st_13', 1943, 228, 5, 1068)
        self.add('statictext', 'st_6', 2158, 228, 5, 1068)
        self.add('statictext', 'st_7', 2409, 228, 5, 1068)
        self.add('statictext', 'st_8', 2578, 228, 5, 1068)
        self.add('statictext', 'st_9', 2747, 228, 5, 1068)
        self.add('statictext', 'st_50', 2921, 228, 5, 1068)
        self.add('statictext', 'st_15', 3122, 228, 5, 1068)
        self.add('statictext', 'st_25', 3383, 228, 5, 1068)
        self.add('statictext', 'st_26', 3625, 228, 5, 1068)
        self.add('commandbutton', 'cb_add', 5, 1208, 238, 80, text='&Add')
        self.add('commandbutton', 'cb_delete', 247, 1208, 238, 80, text='&Delete')
        self.add('statictext', 'st_stktype', 677, 1212, 155, 76)
        self.add('roundrectangle', 'rr_1', 3099, 1316, 507, 264)
        self.add('editmask', 'em_billtotal', 443, 1320, 407, 92)
        self.add('editmask', 'em_taxperc', 1641, 1320, 137, 88, taborder=80)
        self.add('editmask', 'em_tax', 1778, 1320, 288, 88, taborder=90)
        self.add('editmask', 'em_others', 2629, 1320, 407, 88, taborder=100)
        self.add('statictext', 'st_2', 1371, 1324, 206, 72, text='Tax')
        self.add('statictext', 'st_billtotal', 101, 1332, 329, 72, text='Bill Total :')
        self.add('statictext', 'st_discount', 2281, 1332, 334, 64, text='Others :')
        self.add('commandbutton', 'cb_save', 3136, 1332, 434, 96, text='&Save', taborder=140)
        self.add('editmask', 'em_pamt', 443, 1420, 407, 88, taborder=110)
        self.add('datawindow', 'dw_billtype', 1641, 1420, 425, 88, dataobject='d_billtypecode', taborder=120)
        self.add('editmask', 'em_balance', 2629, 1420, 407, 88)
        self.add('statictext', 'st_rcvd', 64, 1428, 366, 72, text='Rcvd amt :')
        self.add('statictext', 'st_17', 1371, 1432, 288, 76, text='Bill Type')
        self.add('statictext', 'st_balance', 2290, 1432, 325, 64, text='Balance :')
        self.add('commandbutton', 'cb_exit', 3136, 1440, 434, 96, text='E&xit', taborder=150)
        self.add('editmask', 'em_cb', 2629, 1520, 407, 88, taborder=130)
        self.add('statictext', 'st_cb', 2272, 1532, 343, 80, text='CB :')
        self.add('checkbox', 'cbx_cst', 1637, 1552, 384, 84, text='Interstate')
