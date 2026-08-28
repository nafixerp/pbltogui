"""New — w_diamond_preturn.

Generated from the PowerBuilder window ``w_diamond_preturn.srw`` by
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
    name='w_diamond_preturn',
    title='New',
    width=4928,
    height=3004,
    controls=[],
    tables=['daybook', 'items', 'smithd', 'purchaserd', 'itemsstk', 'purchaserm', 'barcode', 'barcode_dmddet', 'clients', 'smithm', 'purchased_dmddet', 'purchased', 'advafter', 'barcodedmd', 'generali', 'generals', 'generald', 'daybookpart', 'delpart', 'userd'],
    source_path='w_diamond_preturn.srw',
)


class NewForm(GeneratedForm):
    """New"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('statictext', 'st_grno', 352, 0, 439, 84)
        self.add('singlelineedit', 'sle_billno', 1339, 0, 389, 84, taborder=10)
        self.add('editmask', 'em_date', 2025, 0, 425, 88, taborder=20)
        self.add('statictext', 'st_1', 1070, 4, 261, 72, text='Bill No  :')
        self.add('statictext', 'st_bill', 32, 8, 311, 64, text='Doc. No.  :')
        self.add('statictext', 'st_date', 1833, 12, 187, 64, text='Date :')
        self.add('datawindow', 'dw_1', 352, 92, 425, 92, dataobject='d_sucu', taborder=30)
        self.add('commandbutton', 'cb_custhelp', 795, 96, 64, 92, text='^')
        self.add('singlelineedit', 'st_suppname', 864, 96, 864, 92, limit=30, taborder=40)
        self.add('datawindow', 'dw_smcode', 2885, 96, 677, 88, dataobject='d_smancode', taborder=50)
        self.add('editmask', 'em_ob', 2025, 100, 425, 88)
        self.add('statictext', 'st_smcode', 2583, 104, 293, 64, text='SMan :')
        self.add('statictext', 'st_custcode', 0, 108, 343, 72, text='Supplier :')
        self.add('statictext', 'st_12', 1883, 112, 137, 76, text='OB :')
        self.add('datawindow', 'dw_purchase', 0, 192, 4910, 760, dataobject='d_diamond_purchase', taborder=60)
        self.add('statictext', 'st_10', 283, 192, 5, 668)
        self.add('statictext', 'st_3', 649, 192, 5, 760)
        self.add('statictext', 'st_4', 887, 192, 5, 760)
        self.add('statictext', 'st_18', 1102, 192, 5, 760)
        self.add('statictext', 'st_5', 1234, 192, 5, 760)
        self.add('statictext', 'st_29', 1344, 192, 5, 760)
        self.add('statictext', 'st_13', 1563, 192, 5, 760)
        self.add('statictext', 'st_6', 1733, 192, 5, 760)
        self.add('statictext', 'st_7', 1938, 192, 5, 760)
        self.add('statictext', 'st_8', 2139, 192, 5, 760)
        self.add('statictext', 'st_35', 2290, 192, 5, 760)
        self.add('statictext', 'st_9', 2523, 192, 5, 760)
        self.add('statictext', 'st_19', 2747, 192, 5, 760)
        self.add('statictext', 'st_11', 2894, 192, 5, 760)
        self.add('statictext', 'st_15', 3150, 192, 5, 760)
        self.add('statictext', 'st_27', 3287, 192, 5, 760)
        self.add('statictext', 'st_32', 3401, 192, 5, 760)
        self.add('statictext', 'st_36', 3557, 192, 5, 760)
        self.add('statictext', 'st_17', 3781, 192, 5, 760)
        self.add('statictext', 'st_30', 3991, 192, 5, 760)
        self.add('statictext', 'st_31', 4265, 192, 5, 760)
        self.add('statictext', 'st_33', 4521, 192, 5, 760)
        self.add('commandbutton', 'cb_add', 0, 860, 206, 72, text='&Add', taborder=130)
        self.add('commandbutton', 'cb_delete', 201, 860, 197, 72, text='&Delete', taborder=140)
        self.add('statictext', 'st_stktype', 645, 864, 87, 76)
        self.add('statictext', 'st_kdm', 754, 864, 169, 76)
        self.add('datawindow', 'dw_dmd', 0, 964, 2971, 588, dataobject='d_diamond_purchase_dmds', taborder=90)
        self.add('statictext', 'st_22', 928, 968, 5, 584)
        self.add('statictext', 'st_23', 1157, 968, 5, 584)
        self.add('statictext', 'st_24', 1312, 968, 5, 584)
        self.add('statictext', 'st_25', 1559, 968, 5, 584)
        self.add('statictext', 'st_26', 1819, 968, 5, 584)
        self.add('statictext', 'st_28', 2144, 968, 5, 584)
        self.add('statictext', 'st_37', 2537, 968, 5, 584)
        self.add('statictext', 'st_20', 690, 1032, 5, 516)
        self.add('statictext', 'st_21', 343, 1036, 5, 440)
        self.add('commandbutton', 'cb_dmdadd', 0, 1472, 197, 72, text='Add', taborder=150)
        self.add('commandbutton', 'cb_dmddel', 197, 1472, 210, 72, text='Delete', taborder=170)
        self.add('commandbutton', 'cb_ok', 421, 1472, 210, 72, text='OK', taborder=160)
        self.add('editmask', 'em_billtotal', 357, 1560, 407, 96)
        self.add('editmask', 'em_taxperc', 1371, 1564, 119, 96, taborder=70)
        self.add('editmask', 'em_tax', 1490, 1564, 288, 96, taborder=80)
        self.add('editmask', 'em_exchange', 2542, 1564, 407, 96)
        self.add('checkbox', 'cbx_taxexternal', 1787, 1568, 256, 80, text='External')
        self.add('statictext', 'st_billtotal', 9, 1572, 329, 76, text='Bill Total :')
        self.add('statictext', 'st_14', 1102, 1572, 247, 76, text='Tax :')
        self.add('statictext', 'st_exchange', 2066, 1576, 453, 76, text='P.Return Amt. :')
        self.add('roundrectangle', 'rr_1', 4014, 1576, 558, 308)
        self.add('commandbutton', 'cb_save', 4078, 1624, 434, 96, text='&Save', taborder=180)
        self.add('checkbox', 'cbx_nodmdamt', 3118, 1628, 699, 72, text='Dont Add Dmd Amt')
        self.add('editmask', 'em_nettot', 357, 1660, 407, 96)
        self.add('editmask', 'em_others', 1371, 1664, 407, 96, taborder=100)
        self.add('editmask', 'em_pamt', 2542, 1664, 407, 96, taborder=110)
        self.add('statictext', 'st_nettot', 0, 1668, 338, 76, text='Net Total :')
        self.add('statictext', 'st_discount', 1015, 1672, 334, 76, text='Others :')
        self.add('statictext', 'st_rcvd', 2153, 1676, 366, 76, text='Rcvd amt :')
        self.add('checkbox', 'cbx_nodmdwgt', 3118, 1712, 699, 72, text='Dont Add Dmd Wgt in gm')
        self.add('commandbutton', 'cb_exit', 4078, 1740, 434, 96, text='E&xit', taborder=190)
        self.add('editmask', 'em_balance', 357, 1764, 407, 96)
        self.add('editmask', 'em_cb', 1371, 1764, 407, 96)
        self.add('editmask', 'em_duedate', 2542, 1764, 407, 96, taborder=120)
        self.add('statictext', 'st_balance', 9, 1772, 325, 76, text='Balance :')
        self.add('statictext', 'st_16', 1102, 1776, 247, 76, text='CB :')
        self.add('statictext', 'st_2', 2185, 1780, 334, 76, text='Duedate :')
        self.add('checkbox', 'cbx_keepacinwgt', 3118, 1796, 795, 72, text='Keep A/c in Weight')
        self.add('checkbox', 'cbx_cst', 1371, 1880, 384, 84, text='Interstate')
