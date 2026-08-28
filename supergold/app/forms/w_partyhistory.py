"""Party History — w_partyhistory.

Generated from the PowerBuilder window ``w_partyhistory.srw`` by
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
    name='w_partyhistory',
    title='Party History',
    width=3657,
    height=2292,
    controls=[],
    tables=['daybook', 'items', 'accountm', 'purchased', 'salesrd', 'date', 'purchaserm', 'purchasem', 'purchaserd', 'salesm', 'salesd', 'salesrm', 'smithm', 'smithd', 'refinerym', 'refineryd', 'orderm', 'orderd', 'repairm', 'repaird', 'oitemtranm', 'oitemtrand'],
    source_path='w_partyhistory.srw',
    opens=['w_clientshelp'],
)


class PartyHistoryForm(GeneratedForm):
    """Party History"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 1184, 0, 439, 92, taborder=20)
        self.add('editmask', 'em_date2', 1925, 0, 434, 92, taborder=30)
        self.add('commandbutton', 'cb_4', 2386, 0, 261, 96, text='&Show', taborder=40)
        self.add('commandbutton', 'cb_3', 2706, 0, 261, 100, text='Save &As', taborder=70)
        self.add('commandbutton', 'cb_1', 2976, 0, 256, 100, text='&Print', taborder=90)
        self.add('commandbutton', 'cb_2', 3232, 0, 256, 100, text='E&xit', taborder=60)
        self.add('datawindow', 'dw_accode', 251, 8, 430, 88, dataobject='d_accode', taborder=10)
        self.add('statictext', 'st_1', 987, 12, 183, 72, text='From')
        self.add('statictext', 'st_2', 1765, 12, 155, 72, text='To')
        self.add('statictext', 'st_3', 0, 16, 251, 72, text='Account')
        self.add('dropdownlistbox', 'ddlb_filter', 251, 100, 699, 1440, text='All', items=['All', 'Sales Only', 'Sales Return Only', 'Purchase Only', 'Purchase Return Only', 'Smith Entry Only', 'Jewl Entry Only', 'Refinery Entry Only', 'Order Entry Only', 'Repair Entry Only', 'Other Item Tran Only', 'With Debit Amt Only', 'With Credit Amt Only', 'With Debit or Credit Amt Only', 'Payment Only', 'Receipt Only', 'Journal Only'], taborder=11)
        self.add('dropdownlistbox', 'ddlb_type', 1184, 100, 535, 1440, text='All', items=['All', 'Sales', 'Sales Return', 'Purchase', 'Exchange', 'Purchase Return', 'Order Entry', 'Other Sales', 'Other Purchase', 'Refinery Issue', 'Refinery Rcpt', 'Repair Rcpt', 'Repair Issue', 'Smith Issue', 'Smith Rcpt', 'Jewl Issue', 'Jewl Rcpt', 'Journal', 'Receipt', 'Payment'], taborder=20)
        self.add('checkbox', 'cbx_acledger', 2382, 104, 398, 80, text='A/c Ledger')
        self.add('commandbutton', 'cb_sort', 3232, 104, 256, 80, text='So&rt', taborder=80)
        self.add('statictext', 'st_4', 0, 108, 251, 72, text='Filter')
        self.add('checkbox', 'cbx_speed', 2967, 108, 265, 80, text='Speed')
        self.add('statictext', 'st_5', 987, 112, 183, 72, text='Type')
        self.add('datawindow', 'dw_1', 0, 196, 3634, 1992, dataobject='d_partyhistory', taborder=50)
