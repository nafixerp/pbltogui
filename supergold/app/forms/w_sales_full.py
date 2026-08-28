"""Estimate — w_sales_full.

Generated from the PowerBuilder window ``w_sales_full.srw`` by
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
    name='w_sales_full',
    title='Estimate',
    width=3739,
    height=2328,
    controls=[],
    tables=['items', 'itemsstk', 'daybook', 'salesm', 'barcode', 'clients', 'salesd', 'purchased', 'spdmddet', 'stkandprofit', 'salesrd', 'mctable', 'salesrm', 'orderm', 'purchasem', 'itemadj', 'itemstmp', 'wstg', 'barcodedmd', 'accountm', 'generals', 'generali', 'userd', 'generald', 'daybookpart', 'delpart', 'userm'],
    source_path='w_sales_full.srw',
)


class EstimateForm(GeneratedForm):
    """Estimate"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('singlelineedit', 'st_billno', 306, 0, 402, 84)
        self.add('checkbox', 'cbx_manual', 722, 0, 256, 80, text='Ma&nual')
        self.add('editmask', 'em_date', 1463, 0, 416, 84, taborder=10)
        self.add('editmask', 'em_rate', 2153, 0, 416, 84)
        self.add('singlelineedit', 'sle_ordno', 2939, 0, 398, 84, limit=10, taborder=20)
        self.add('commandbutton', 'cb_ordhelp', 3346, 0, 142, 80, text='&Help')
        self.add('editmask', 'em_rate8gm', 3529, 0, 87, 84)
        self.add('statictext', 'st_1', 1883, 4, 256, 60, text='Rate/gm :')
        self.add('statictext', 'st_bill', 55, 8, 233, 56, text='Bill No :')
        self.add('statictext', 'st_date', 1271, 8, 178, 56, text='Date :')
        self.add('statictext', 'st_2', 2638, 8, 288, 60, text='Order No. :')
        self.add('datawindow', 'dw_1', 306, 84, 402, 84, dataobject='d_cust', taborder=30)
        self.add('datawindow', 'dw_smcode', 2939, 84, 677, 84, dataobject='d_smancode', taborder=50)
        self.add('singlelineedit', 'st_custname', 777, 88, 1102, 84, limit=30, taborder=40)
        self.add('editmask', 'em_ob', 2153, 88, 416, 84)
        self.add('commandbutton', 'cb_custhelp', 713, 92, 55, 76, text='^')
        self.add('statictext', 'st_custcode', 0, 96, 288, 68, text='Customer :')
        self.add('statictext', 'st_15', 2002, 96, 137, 64, text='OB :')
        self.add('statictext', 'st_10', 2638, 104, 288, 60, text='SM Name :')
        self.add('datawindow', 'dw_sale', 18, 176, 3602, 564, dataobject='d_sale_full', taborder=60)
        self.add('statictext', 'st_14', 398, 176, 5, 496)
        self.add('statictext', 'st_4', 1047, 176, 5, 556)
        self.add('statictext', 'st_5', 1234, 176, 5, 556)
        self.add('statictext', 'st_6', 1527, 176, 5, 556)
        self.add('statictext', 'st_7', 1801, 176, 5, 556)
        self.add('statictext', 'st_8', 2075, 176, 5, 560)
        self.add('statictext', 'st_9', 2386, 176, 5, 560)
        self.add('statictext', 'st_11', 2711, 176, 5, 560)
        self.add('statictext', 'st_13', 3296, 176, 5, 556)
        self.add('statictext', 'st_12', 3058, 180, 5, 556)
        self.add('commandbutton', 'cb_add', 27, 672, 151, 64, text='&Add')
        self.add('commandbutton', 'cb_delete', 178, 672, 155, 64, text='&Delete')
        self.add('statictext', 'st_stock', 603, 676, 247, 60)
        self.add('editmask', 'em_billtotal', 3205, 740, 416, 80)
        self.add('statictext', 'st_billtotal', 2770, 748, 421, 60, text='Sales Bill Total :')
        self.add('statictext', 'st_19', 23, 760, 411, 60, text='SALES RETURN')
        self.add('datawindow', 'dw_sreturn', 18, 820, 3602, 332, dataobject='d_sreturn_full', taborder=70)
        self.add('statictext', 'st_21', 398, 820, 5, 268)
        self.add('statictext', 'st_30', 1047, 820, 5, 328)
        self.add('statictext', 'st_29', 1234, 820, 5, 328)
        self.add('statictext', 'st_28', 1527, 820, 5, 328)
        self.add('statictext', 'st_27', 1801, 820, 5, 328)
        self.add('statictext', 'st_26', 2075, 820, 5, 332)
        self.add('statictext', 'st_25', 2386, 820, 5, 332)
        self.add('statictext', 'st_24', 2711, 820, 5, 332)
        self.add('statictext', 'st_22', 3296, 820, 5, 328)
        self.add('statictext', 'st_23', 3058, 824, 5, 328)
        self.add('commandbutton', 'cb_sradd', 27, 1084, 151, 60, text='Add')
        self.add('commandbutton', 'cb_srdel', 178, 1084, 169, 60, text='Delete')
        self.add('editmask', 'em_sreturn', 3205, 1152, 416, 80)
        self.add('statictext', 'st_sreturn', 2674, 1164, 517, 60, text='Sales Return Total :')
        self.add('statictext', 'st_20', 23, 1172, 411, 60, text='EXCHANGE')
        self.add('datawindow', 'dw_exchange', 18, 1232, 3602, 344, dataobject='d_exchange_full', taborder=80)
        self.add('statictext', 'st_34', 2304, 1232, 5, 340)
        self.add('statictext', 'st_33', 2523, 1232, 5, 340)
        self.add('statictext', 'st_32', 2706, 1232, 5, 340)
        self.add('statictext', 'st_31', 2930, 1232, 5, 340)
        self.add('statictext', 'st_50', 3214, 1232, 5, 340)
        self.add('statictext', 'st_35', 320, 1236, 5, 268)
        self.add('statictext', 'st_41', 905, 1236, 5, 340)
        self.add('statictext', 'st_40', 1152, 1236, 5, 340)
        self.add('statictext', 'st_39', 1326, 1236, 5, 340)
        self.add('statictext', 'st_38', 1609, 1236, 5, 340)
        self.add('statictext', 'st_37', 1819, 1236, 5, 340)
        self.add('statictext', 'st_36', 2057, 1236, 5, 340)
        self.add('commandbutton', 'cb_exadd', 27, 1508, 151, 60, text='Add')
        self.add('commandbutton', 'cb_exdel', 178, 1508, 183, 60, text='Delete')
        self.add('editmask', 'em_tva', 306, 1580, 416, 84, taborder=90)
        self.add('editmask', 'em_staxamt', 1152, 1580, 416, 84, taborder=100)
        self.add('editmask', 'em_ast', 2066, 1580, 416, 84, taborder=110)
        self.add('editmask', 'em_exchange', 3205, 1580, 416, 88)
        self.add('statictext', 'st_18', 1783, 1584, 265, 76, text='Cess :')
        self.add('statictext', 'st_exchange', 2752, 1584, 439, 60, text='Exchange Total :')
        self.add('statictext', 'st_42', 41, 1588, 256, 64, text='Total VA :')
        self.add('statictext', 'st_staxamt', 878, 1588, 256, 64, text='Tax Amt :')
        self.add('editmask', 'em_advance', 306, 1668, 416, 84, taborder=120)
        self.add('editmask', 'em_nettot', 1152, 1668, 416, 88)
        self.add('editmask', 'em_discount', 2066, 1668, 416, 84, taborder=130)
        self.add('editmask', 'em_rcvd', 3205, 1668, 416, 88, taborder=140)
        self.add('statictext', 'st_discount', 1751, 1672, 297, 52, text='Discount :')
        self.add('statictext', 'st_43', 27, 1676, 270, 64, text='Adv.Retn :')
        self.add('statictext', 'st_nettot', 823, 1676, 311, 60, text='Net Total :')
        self.add('statictext', 'st_rcvd', 2903, 1676, 283, 60, text='Received :')
        self.add('checkbox', 'cbx_updtfr', 2638, 1748, 270, 76, text='&Fr')
        self.add('editmask', 'em_balance', 306, 1756, 416, 88)
        self.add('editmask', 'em_netbalance', 1152, 1756, 416, 84)
        self.add('statictext', 'st_3', 1719, 1756, 329, 64, text='Due Date :')
        self.add('editmask', 'em_duedate', 2066, 1756, 416, 84, taborder=150)
        self.add('commandbutton', 'cb_dthlp', 2487, 1756, 59, 84, text='^')
        self.add('datawindow', 'dw_co', 3205, 1756, 402, 88, dataobject='d_cust', taborder=160)
        self.add('statictext', 'st_balance', 18, 1764, 279, 52, text='Balance :')
        self.add('statictext', 'st_16', 3026, 1764, 165, 76, text='C/o :')
        self.add('commandbutton', 'cb_cohelp', 3616, 1764, 64, 80, text='^')
        self.add('statictext', 'st_17', 960, 1768, 174, 76, text='CB :')
        self.add('commandbutton', 'cb_short', 2071, 1848, 306, 84, text='Short &Print', taborder=170)
        self.add('commandbutton', 'cb_qtnprint', 2405, 1848, 306, 84, text='&Qtn Print', taborder=180)
        self.add('commandbutton', 'cb_save', 3008, 1848, 306, 84, text='&Save', taborder=190)
        self.add('commandbutton', 'cb_exit', 3323, 1848, 306, 84, text='E&xit', taborder=200)
