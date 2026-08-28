"""Expense Voucher Entry — w_purchase_amtentry.

Generated from the PowerBuilder window ``w_purchase_amtentry.srw`` by
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
    name='w_purchase_amtentry',
    title='Expense Voucher Entry',
    width=2363,
    height=1760,
    controls=[],
    tables=['daybook', 'purchasem', 'salestype', 'clients', 'generali', 'daybookpart', 'generals'],
    source_path='w_purchase_amtentry.srw',
    grid={'control': 'dw_accode', 'dataobject': 'd_supp', 'table': 'codehelp', 'keys': ['code'], 'computes': [], 'columns': [{'name': 'code', 'label': 'code', 'type': 'char'}]},
    report={'dataobject': 'd_supp', 'sql': 'SELECT codehelp.code AS codehelp_code FROM codehelp', 'computes': [], 'args': [], 'arg_types': {}, 'tables': ['codehelp'], 'columns': [{'name': 'code', 'label': 'code', 'type': 'char'}]},
    opens=['w_clientshelp', 'w_rcptpmnt_view'],
)


class ExpenseVoucherEntryForm(GeneratedForm):
    """Expense Voucher Entry"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('datawindow', 'dw_billtype', 713, 16, 425, 88, dataobject='d_billtypecode', taborder=10)
        self.add('checkbox', 'cbx_purchentry', 1467, 16, 791, 92, text='Create as purchase bill')
        self.add('commandbutton', 'cb_btypedef', 1152, 20, 210, 88, text='Set Def')
        self.add('statictext', 'st_17', 315, 24, 389, 76, text='Type')
        self.add('statictext', 'st_docno', 713, 124, 421, 92)
        self.add('statictext', 'st_5', 315, 136, 389, 76, text='Doc No')
        self.add('editmask', 'em_date', 713, 224, 421, 92, taborder=20)
        self.add('statictext', 'st_2', 315, 236, 389, 76, text='Date')
        self.add('singlelineedit', 'sle_billno', 713, 324, 425, 92, taborder=30)
        self.add('statictext', 'st_7', 315, 332, 389, 76, text='Bill No')
        self.add('editmask', 'em_billdate', 713, 424, 421, 92, taborder=40)
        self.add('statictext', 'st_6', 315, 436, 389, 76, text='Bill Date')
        self.add('datawindow', 'dw_accode', 713, 520, 425, 84, dataobject='d_supp', taborder=50)
        self.add('statictext', 'st_10', 315, 532, 389, 72, text='Party')
        self.add('singlelineedit', 'sle_name', 713, 612, 1317, 92)
        self.add('statictext', 'st_9', 315, 620, 389, 80, text='Name')
        self.add('editmask', 'em_bamt', 713, 712, 421, 96, taborder=60)
        self.add('datawindow', 'dw_pamtacc', 1152, 716, 878, 88, dataobject='d_accode_sel', taborder=110)
        self.add('commandbutton', 'cb_1', 2075, 720, 210, 88, text='Set Def')
        self.add('statictext', 'st_11', 315, 724, 389, 80, text='Bill Amount')
        self.add('editmask', 'em_discount', 713, 816, 421, 96, taborder=70)
        self.add('datawindow', 'dw_discacc', 1152, 816, 878, 88, dataobject='d_accode_sel', taborder=120)
        self.add('statictext', 'st_1', 315, 828, 389, 80, text='Discount')
        self.add('datawindow', 'dw_taxac', 1152, 916, 878, 88, dataobject='d_accode_sel', taborder=130)
        self.add('editmask', 'em_taxperc', 713, 920, 137, 96, taborder=80)
        self.add('editmask', 'em_taxamt', 855, 920, 279, 96, taborder=90)
        self.add('statictext', 'st_3', 315, 932, 389, 80, text='Tax')
        self.add('editmask', 'em_netamt', 713, 1024, 421, 96)
        self.add('statictext', 'st_4', 315, 1036, 389, 80, text='Net Amount')
        self.add('editmask', 'em_paidamt', 713, 1132, 421, 96, taborder=100)
        self.add('datawindow', 'dw_cbcode', 1152, 1136, 878, 88, dataobject='d_cashbankcode', taborder=140)
        self.add('statictext', 'st_8', 315, 1144, 389, 80, text='Paid Amount')
        self.add('editmask', 'em_balance', 713, 1240, 421, 96)
        self.add('statictext', 'st_12', 315, 1252, 389, 80, text='Balance')
        self.add('commandbutton', 'cb_save', 713, 1472, 347, 108, text='&Save')
        self.add('commandbutton', 'cb_exit', 1079, 1472, 347, 108, text='E&xit')
