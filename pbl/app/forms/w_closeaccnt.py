"""Year End Account Close — w_closeaccnt.

Generated from the PowerBuilder window ``w_closeaccnt.srw`` by
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
    name='w_closeaccnt',
    title='Year End Account Close',
    width=2066,
    height=2020,
    controls=[],
    tables=['salesm', 'orderm', 'purchasem', 'daybook', 'salesrm', 'accountm', 'purchased', 'clients', 'salesrd', 'repairm', 'refinerym', 'purchaserm', 'orderdga', 'advafter', 'refineryd', 'wgtrcptpmnt', 'clientsgs', 'kuricolln', 'purchaserd', 'smithd', 'salesd', 'collection', 'smithm', 'orderd', 'repaird', 'oitemtrand', 'daybookratewgt', 'clients_kuridet', 'itemsothers', 'oitemtranm', 'itemadj', 'barcode', 'modelm', 'items', 'itemsstk', 'barcodedmd', 'generali', 'daybookpart', 'generals'],
    source_path='w_closeaccnt.srw',
)


class YearEndAccountCloseForm(GeneratedForm):
    """Year End Account Close"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('statictext', 'st_1', 1193, 0, 462, 76, text='Closing Date')
        self.add('checkbox', 'cbx_chsales', 155, 8, 576, 76, text='Delete Cash Sales', taborder=10)
        self.add('checkbox', 'cbx_crsales', 155, 92, 594, 76, text='Delete Credit Sales', taborder=20)
        self.add('editmask', 'em_date', 1166, 96, 512, 92, taborder=170)
        self.add('checkbox', 'cbx_sret', 155, 168, 613, 76, text='Delete Sales Return', taborder=30)
        self.add('commandbutton', 'cb_closeac', 1166, 196, 512, 108, text='Close A/c', taborder=180)
        self.add('checkbox', 'cbx_chpurchase', 155, 244, 677, 76, text='Delete Cash Purchase', taborder=40)
        self.add('commandbutton', 'cb_1', 1166, 316, 512, 108, text='E&xit', taborder=190)
        self.add('checkbox', 'cbx_crpurchase', 155, 328, 695, 76, text='Delete Credit Purchase', taborder=50)
        self.add('checkbox', 'cbx_purchaseret', 155, 408, 713, 76, text='Delete Purchase Return', taborder=60)
        self.add('commandbutton', 'cb_docnoinit', 1166, 436, 512, 108, text='Init. Doc. Nos.', taborder=150)
        self.add('checkbox', 'cbx_otheritemtran', 155, 488, 905, 76, text='Delete Other Item Transactions', taborder=60)
        self.add('commandbutton', 'cb_delallentries', 1166, 552, 512, 108, text='Del All Entries', taborder=151)
        self.add('checkbox', 'cbx_order', 155, 568, 695, 76, text='Delete Order', taborder=70)
        self.add('checkbox', 'cbx_orderpend', 155, 640, 695, 76, text='Delete Pending Order', taborder=80)
        self.add('checkbox', 'cbx_deldaybookentries', 1166, 688, 709, 80, text='Delete Daybook Entries')
        self.add('checkbox', 'cbx_reppend', 155, 720, 695, 76, text='Delete Pending Repair', taborder=90)
        self.add('checkbox', 'cbx_deloutstockbarcode', 1166, 772, 786, 80, text='Delete Outstock Barcodes')
        self.add('checkbox', 'cbx_repr', 155, 792, 695, 76, text='Delete Repair', taborder=100)
        self.add('checkbox', 'cbx_dontsp', 1166, 860, 763, 76, text="Don't Close Sp. Accounts")
        self.add('checkbox', 'cbx_smith', 155, 864, 887, 76, text='Delete Smith/Jewl/Dep Entries', taborder=110)
        self.add('checkbox', 'cbx_refn', 155, 940, 901, 76, text='Delete Refinery Entries(closed)', taborder=120)
        self.add('checkbox', 'cbx_keeppendbills', 1166, 944, 585, 76, text='Keep Pending Bills')
        self.add('checkbox', 'cbx_refnpend', 155, 1020, 933, 76, text='Delete Refinery Entries(pending)', taborder=130)
        self.add('checkbox', 'cbx_keepbills', 1166, 1028, 411, 76, text='Keep Bills')
        self.add('checkbox', 'cbx_adjustment', 155, 1100, 910, 76, text='Delete Item Adjustment Entries', taborder=140)
        self.add('commandbutton', 'cb_selectall', 1166, 1160, 512, 108, text='Select &All', taborder=160)
        self.add('checkbox', 'cbx_kuricolln', 155, 1176, 969, 76, text='Delete Kuri/Scheme Colln Entries', taborder=140)
        self.add('checkbox', 'cbx_partnersdeposit', 155, 1252, 969, 76, text='Delete Partners Deposit Entries', taborder=140)
        self.add('checkbox', 'cbx_initopbalie', 155, 1340, 1312, 76, text='Initialise Op. Balance of Income/Expense A/cs')
        self.add('checkbox', 'cbx_initopbalal', 155, 1420, 1312, 76, text='Initialise Op. Balance of Assets/Liabilities')
        self.add('checkbox', 'cbx_initopstock', 155, 1500, 1312, 76, text='Initialise Op. Stock Details')
        self.add('checkbox', 'cbx_initpartyopwgt', 155, 1580, 1312, 76, text='Initialise Party Op. Wgt Details')
        self.add('checkbox', 'cbx_initsmithjewlopbal', 155, 1664, 1312, 76, text='Initialise Smth/Jewl Op.Bal Details')
        self.add('checkbox', 'cbx_removeaddr', 155, 1744, 1312, 76, text='Remove Addr+phone from clients')
        self.add('statictext', 'st_recstatus', 151, 1812, 425, 72)
        self.add('statictext', 'st_filestatus', 613, 1812, 1221, 72)
