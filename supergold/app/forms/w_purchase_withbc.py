"""Estimate — w_purchase_withbc.

Generated from the PowerBuilder window ``w_purchase_withbc.srw`` by
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
    name='w_purchase_withbc',
    title='Estimate',
    width=3662,
    height=1912,
    controls=[],
    tables=['items', 'daybook', 'itemsstk', 'barcode', 'purchaserd', 'purchasem', 'purchased', 'advafter', 'purchaserm', 'clients', 'orderm', 'accountm', 'generali', 'generald', 'daybookpart', 'generals', 'delpart', 'userd'],
    source_path='w_purchase_withbc.srw',
)


class EstimateForm(GeneratedForm):
    """Estimate"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('singlelineedit', 'st_grno', 352, 0, 439, 84, limit=10, taborder=40)
        self.add('checkbox', 'cbx_manual', 805, 0, 256, 80, text='Manual')
        self.add('singlelineedit', 'sle_billno', 1339, 0, 389, 84, taborder=10)
        self.add('editmask', 'em_date', 2025, 0, 425, 88, taborder=20)
        self.add('singlelineedit', 'sle_ordno', 2885, 0, 375, 88, limit=10, taborder=30)
        self.add('commandbutton', 'cb_1', 3269, 0, 146, 88, text='&Help')
        self.add('statictext', 'st_1', 1070, 4, 261, 72, text='Bill No :')
        self.add('statictext', 'st_bill', 32, 8, 311, 64, text='Doc. No.  :')
        self.add('statictext', 'st_11', 2473, 8, 402, 76, text='To Order No :')
        self.add('statictext', 'st_date', 1833, 12, 187, 64, text='Date :')
        self.add('datawindow', 'dw_1', 352, 88, 425, 96, dataobject='d_sucu', taborder=50)
        self.add('commandbutton', 'cb_custhelp', 795, 92, 64, 92, text='^')
        self.add('singlelineedit', 'st_suppname', 864, 92, 864, 92, limit=30, taborder=60)
        self.add('editmask', 'em_ob', 2025, 96, 425, 88)
        self.add('datawindow', 'dw_smcode', 2885, 96, 677, 88, dataobject='d_smancode', taborder=80)
        self.add('statictext', 'st_custcode', 0, 104, 343, 72, text='Supplier :')
        self.add('statictext', 'st_12', 1883, 108, 137, 76, text='OB :')
        self.add('statictext', 'st_smcode', 2583, 112, 293, 64, text='SMan :')
        self.add('singlelineedit', 'sle_addr', 352, 192, 1376, 92, limit=60, taborder=70)
        self.add('checkbox', 'cbx_speed', 2880, 196, 411, 80, text='Speed Entry')
        self.add('statictext', 'st_20', 0, 200, 343, 72, text='Address :')
        self.add('checkbox', 'cbx_updtfr', 3392, 200, 165, 76, text='&Fr')
        self.add('datawindow', 'dw_purchase', 0, 292, 3639, 1020, dataobject='d_purchase_withbc', taborder=90)
        self.add('statictext', 'st_10', 357, 292, 5, 928)
        self.add('statictext', 'st_3', 832, 292, 5, 1016)
        self.add('statictext', 'st_4', 1083, 292, 5, 1016)
        self.add('statictext', 'st_5', 1248, 292, 5, 1016)
        self.add('statictext', 'st_13', 1536, 292, 5, 1016)
        self.add('statictext', 'st_6', 1746, 292, 5, 1016)
        self.add('statictext', 'st_7', 1998, 292, 5, 1016)
        self.add('statictext', 'st_55', 2254, 292, 5, 1016)
        self.add('statictext', 'st_9', 2496, 292, 5, 1016)
        self.add('statictext', 'st_15', 2816, 292, 5, 1016)
        self.add('statictext', 'st_26', 3063, 292, 5, 1016)
        self.add('statictext', 'st_27', 3337, 292, 5, 1016)
        self.add('commandbutton', 'cb_add', 0, 1224, 206, 72, text='&Add')
        self.add('commandbutton', 'cb_delete', 206, 1224, 197, 72, text='&Delete')
        self.add('statictext', 'st_kdm', 2162, 1224, 169, 76)
        self.add('statictext', 'st_stktype', 663, 1228, 160, 76)
        self.add('roundrectangle', 'rr_1', 3058, 1308, 558, 392)
        self.add('editmask', 'em_billtotal', 361, 1320, 407, 96)
        self.add('editmask', 'em_discperc', 1371, 1320, 128, 96, taborder=110)
        self.add('editmask', 'em_discount', 1499, 1320, 279, 96, taborder=130)
        self.add('editmask', 'em_taxperc', 2592, 1320, 123, 96, taborder=140)
        self.add('editmask', 'em_tax', 2715, 1320, 302, 96, taborder=100)
        self.add('statictext', 'st_billtotal', 23, 1332, 329, 76, text='Bill Total :')
        self.add('statictext', 'st_19', 1065, 1332, 297, 64, text='Discount :')
        self.add('checkbox', 'cbx_taxexternal', 2112, 1332, 288, 80, text='External')
        self.add('statictext', 'st_14', 2336, 1332, 247, 76, text='Tax :')
        self.add('commandbutton', 'cb_exchange', 3122, 1344, 434, 96, text='&Return', taborder=180)
        self.add('editmask', 'em_cess', 361, 1420, 407, 96, taborder=120)
        self.add('editmask', 'em_exchange', 1371, 1420, 407, 96)
        self.add('editmask', 'em_nettot', 2592, 1420, 425, 96)
        self.add('statictext', 'st_exchange', 1029, 1424, 334, 76, text='P.Return :')
        self.add('statictext', 'st_18', 146, 1428, 206, 64, text='Cess :')
        self.add('statictext', 'st_nettot', 2245, 1428, 338, 76, text='Net Total :')
        self.add('commandbutton', 'cb_save', 3122, 1456, 434, 96, text='&Save', taborder=190)
        self.add('editmask', 'em_others', 361, 1520, 407, 96, taborder=150)
        self.add('editmask', 'em_pamt', 1371, 1520, 407, 96, taborder=160)
        self.add('editmask', 'em_balance', 2592, 1520, 425, 96)
        self.add('statictext', 'st_discount', 18, 1528, 334, 76, text='Others :')
        self.add('statictext', 'st_balance', 2258, 1528, 325, 76, text='Balance :')
        self.add('statictext', 'st_rcvd', 997, 1532, 366, 76, text='Paid amt :')
        self.add('commandbutton', 'cb_exit', 3122, 1568, 434, 96, text='E&xit', taborder=200)
        self.add('datawindow', 'dw_billtype', 2592, 1616, 425, 88, dataobject='d_billtypecode', taborder=210)
        self.add('editmask', 'em_cb', 361, 1620, 407, 96)
        self.add('editmask', 'em_duedate', 1371, 1620, 407, 96, taborder=170)
        self.add('statictext', 'st_17', 2336, 1620, 247, 76, text='BType :')
        self.add('statictext', 'st_16', 105, 1632, 247, 76, text='CB :')
        self.add('statictext', 'st_2', 1029, 1636, 334, 76, text='Duedate :')
        self.add('checkbox', 'cbx_printbc', 2592, 1712, 622, 68, text='Print BC After Save')
