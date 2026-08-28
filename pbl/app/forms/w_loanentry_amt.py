"""New Loan — w_loanentry_amt.

Generated from the PowerBuilder window ``w_loanentry_amt.srw`` by
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
    name='w_loanentry_amt',
    title='New Loan',
    width=4379,
    height=2280,
    controls=[],
    tables=['daybook', 'loan', 'loan_dates', 'loan_items', 'itemsqtype', 'clients', 'pdclist', 'items', 'generali', 'daybookpart'],
    source_path='w_loanentry_amt.srw',
    report={'dataobject': 'd_loan_items', 'sql': 'SELECT loan_items.item AS loan_items_item, loan_items.purity AS loan_items_purity, loan_items.qty AS loan_items_qty, loan_items.weight AS loan_items_weight, loan_items.stwgt AS loan_items_stwgt, loan_items.rate AS loan_items_rate, loan_items.mcharge AS loan_items_mcharge, loan_items.amount AS loan_items_amount, loan_items.touch AS loan_items_touch FROM loan_items', 'computes': [], 'args': ['rslno'], 'arg_types': {'rslno': 'number'}, 'tables': ['loan_items'], 'columns': [{'name': 'item', 'label': 'item', 'type': 'char'}, {'name': 'purity', 'label': 'purity', 'type': 'char'}, {'name': 'qty', 'label': 'qty', 'type': 'long'}, {'name': 'weight', 'label': 'weight', 'type': 'decimal'}, {'name': 'stwgt', 'label': 'stwgt', 'type': 'decimal'}, {'name': 'rate', 'label': 'rate', 'type': 'decimal'}, {'name': 'mcharge', 'label': 'mcharge', 'type': 'decimal'}, {'name': 'amount', 'label': 'amount', 'type': 'decimal'}, {'name': 'touch', 'label': 'touch', 'type': 'decimal'}]},
    opens=['w_clientshelp', 'w_sucu'],
)


class NewLoanForm(GeneratedForm):
    """New Loan"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('statictext', 'st_docno', 581, 0, 402, 92)
        self.add('datawindow', 'dw_1', 1582, 0, 402, 92, dataobject='d_cust', taborder=10)
        self.add('statictext', 'st_7', 37, 4, 343, 64, text='Doc. No')
        self.add('commandbutton', 'cb_custhelp', 1989, 4, 59, 84, text='^')
        self.add('editmask', 'em_date', 3186, 4, 402, 92, taborder=20)
        self.add('statictext', 'st_2', 2702, 8, 480, 76, text='Date')
        self.add('statictext', 'st_8', 1152, 12, 411, 64, text='Customer')
        self.add('singlelineedit', 'sle_refno', 581, 100, 402, 92, limit=10, taborder=30)
        self.add('singlelineedit', 'st_custname', 1582, 104, 974, 88)
        self.add('editmask', 'em_grate', 3186, 104, 402, 96, taborder=40)
        self.add('statictext', 'st_12', 37, 108, 539, 64, text='Ref. No')
        self.add('statictext', 'st_18', 1152, 108, 411, 80, text='Name')
        self.add('statictext', 'st_9', 2702, 112, 480, 76, text='Gold Rate')
        self.add('editmask', 'em_amount', 581, 200, 402, 96, taborder=50)
        self.add('editmask', 'em_intamt', 1582, 204, 402, 96, taborder=60)
        self.add('editmask', 'em_netamt', 3186, 204, 402, 96)
        self.add('statictext', 'st_13', 32, 208, 539, 76, text='Loan Amount')
        self.add('statictext', 'st_3', 2702, 212, 480, 76, text='Total Amount')
        self.add('statictext', 'st_1', 1152, 216, 411, 76, text='Interest Amt')
        self.add('editmask', 'em_rcvd', 581, 304, 402, 100, taborder=70)
        self.add('statictext', 'st_6', 27, 308, 539, 76, text='Deposit Amount')
        self.add('datawindow', 'dw_cashbank', 1582, 308, 882, 88, dataobject='d_cashbankcode', taborder=80)
        self.add('editmask', 'em_paidamt', 3186, 308, 402, 100, taborder=90)
        self.add('statictext', 'st_14', 2702, 312, 480, 76, text='Paid Now')
        self.add('statictext', 'st_25', 1152, 320, 411, 76, text='Cash/Card')
        self.add('dropdownlistbox', 'ddlb_collntype', 1582, 404, 402, 344, text='Monthly', items=['Monthly', 'Weekly', 'Daily', 'Anytime'], taborder=110)
        self.add('checkbox', 'cbx_closed', 3826, 404, 343, 80, text='Closed')
        self.add('statictext', 'st_10', 1152, 412, 411, 76, text='Colln Type')
        self.add('editmask', 'em_instamt', 3186, 412, 402, 100, taborder=120)
        self.add('editmask', 'em_instnos', 581, 416, 402, 100, taborder=100)
        self.add('statictext', 'st_4', 32, 424, 539, 76, text='No.of installments')
        self.add('statictext', 'st_5', 2702, 424, 480, 76, text='Installment Amt')
        self.add('datawindow', 'dw_smcode', 1582, 516, 677, 88, dataobject='d_smancode', taborder=140)
        self.add('dropdownlistbox', 'ddlb_loantype', 3186, 516, 402, 344, text='Finance', items=['Finance', 'Sales'], taborder=150)
        self.add('editmask', 'em_validity', 3927, 516, 402, 100, taborder=160)
        self.add('editmask', 'em_collndate', 581, 520, 402, 100, taborder=130)
        self.add('statictext', 'st_17', 2702, 520, 480, 76, text='Loan Type')
        self.add('statictext', 'st_15', 3643, 524, 247, 76, text='Validity')
        self.add('statictext', 'st_11', 37, 528, 539, 76, text='Colln Start Date')
        self.add('statictext', 'st_staff', 1152, 528, 411, 64, text='Staff')
        self.add('statictext', 'st_items', 41, 624, 2574, 84, text='Guarantee Items')
        self.add('statictext', 'st_16', 2624, 624, 1710, 84, text='Collection Schedule')
        self.add('datawindow', 'dw_items', 41, 712, 2574, 1204, dataobject='d_loan_items', taborder=170)
        self.add('datawindow', 'dw_dates', 2624, 712, 1710, 1204, dataobject='d_loan_dates', taborder=180)
        self.add('commandbutton', 'cb_2', 55, 1832, 174, 68, text='Add', taborder=220)
        self.add('commandbutton', 'cb_item_add', 64, 1832, 174, 68, text='Add', taborder=210)
        self.add('commandbutton', 'cb_1', 242, 1832, 174, 68, text='Del', taborder=230)
        self.add('commandbutton', 'cb_item_del', 251, 1832, 174, 68, text='Del', taborder=250)
        self.add('commandbutton', 'cb_add', 2638, 1832, 174, 68, text='Add', taborder=190)
        self.add('commandbutton', 'cb_del', 2825, 1832, 174, 68, text='Del', taborder=200)
        self.add('commandbutton', 'cb_ok', 1851, 2004, 379, 136, text='&Save', taborder=240)
        self.add('commandbutton', 'cb_exit', 2235, 2004, 370, 136, text='E&xit', taborder=260)
