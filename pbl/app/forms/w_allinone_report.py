"""All Report Print — w_allinone_report.

Generated from the PowerBuilder window ``w_allinone_report.srw`` by
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
    name='w_allinone_report',
    title='All Report Print',
    width=2382,
    height=1872,
    controls=[],
    tables=['salesrm', 'salesd', 'salesrd', 'purchased', 'purchaserd', 'salesm', 'purchasem', 'purchaserm', 'smithm', 'smithd'],
    source_path='w_allinone_report.srw',
    opens=['w_allreportsummary'],
)


class AllReportPrintForm(GeneratedForm):
    """All Report Print"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 361, 8, 384, 88, taborder=10)
        self.add('editmask', 'em_date2', 1038, 8, 384, 88, taborder=20)
        self.add('datawindow', 'dw_print', 1513, 8, 571, 120, dataobject='d_daysummaryprint', taborder=50)
        self.add('statictext', 'st_1', 14, 12, 329, 76, text='Date From :')
        self.add('statictext', 'st_2', 795, 12, 256, 76, text='Date To :')
        self.add('checkbox', 'cbx_cashbook', 462, 128, 389, 76, text='Cash Book')
        self.add('checkbox', 'cbx_salepurhwgt', 1509, 132, 663, 76, text='Sales/Purchase Wgt')
        self.add('checkbox', 'cbx_creditsales', 1509, 208, 434, 76, text='Credit Sales')
        self.add('checkbox', 'cbx_stockledger', 462, 220, 466, 76, text='Stock Ledger')
        self.add('checkbox', 'cbx_creditpurch', 1509, 284, 544, 76, text='Credit Purchase')
        self.add('checkbox', 'cbx_salesbook', 462, 308, 407, 76, text='Sales Book')
        self.add('checkbox', 'cbx_custrcpt', 1509, 360, 690, 76, text='Customer Rcpt/Pmnt')
        self.add('checkbox', 'cbx_itemwisesales', 462, 396, 521, 76, text='Itemwise Sales')
        self.add('checkbox', 'cbx_refinery', 1509, 440, 681, 76, text='Refinery Transaction')
        self.add('checkbox', 'cbx_salesreturnbook', 462, 484, 617, 76, text='Sales Return Book')
        self.add('checkbox', 'cbx_refineryanal', 1509, 524, 681, 76, text='Refinery Analysis')
        self.add('checkbox', 'cbx_itemwisesalesreturn', 462, 564, 731, 76, text='Itemwise Sales Return')
        self.add('checkbox', 'cbx_smwisesales', 1509, 612, 782, 80, text='SMan wise Sales')
        self.add('checkbox', 'cbx_purchasebook', 462, 648, 571, 76, text='Purchase Book')
        self.add('checkbox', 'cbx_smwisepurch', 1509, 700, 782, 80, text='SMan wise Purchase')
        self.add('checkbox', 'cbx_itemwisepurchase', 462, 736, 631, 76, text='Itemwise Purchase')
        self.add('checkbox', 'cbx_sundryac', 1509, 796, 782, 80, text='Sundry A/cs')
        self.add('checkbox', 'cbx_purchasereturnbook', 462, 832, 727, 76, text='Purchase Return Book')
        self.add('checkbox', 'cbx_partywgtrcvble', 1509, 892, 782, 80, text='Party Wgt Receivables')
        self.add('checkbox', 'cbx_itemwisepurchasereturn', 462, 912, 901, 76, text='Itemwise Purchase Return')
        self.add('checkbox', 'cbx_partywgtpayble', 1509, 984, 782, 80, text='Party Wgt Payables')
        self.add('checkbox', 'cbx_goldsmithtransactions', 462, 1000, 759, 76, text='Goldsmith Transactions')
        self.add('checkbox', 'cbx_smithsummary', 462, 1088, 672, 76, text='Goldsmith Summary')
        self.add('checkbox', 'cbx_itemadjustments', 462, 1172, 581, 76, text='Item Adjustments')
        self.add('commandbutton', 'cb_showrep', 1509, 1224, 443, 108, text='Show Report', taborder=51)
        self.add('checkbox', 'cbx_acpayable', 462, 1272, 727, 76, text='A/c Payable Summary')
        self.add('datawindow', 'dw_grp', 457, 1372, 800, 88, dataobject='d_itemgrpcode', taborder=30)
        self.add('checkbox', 'cbx_grphistory', 1280, 1376, 87, 76)
        self.add('statictext', 'st_3', 0, 1380, 443, 76, text='Group History :')
        self.add('statictext', 'st_status', 585, 1492, 1339, 76)
        self.add('commandbutton', 'cb_selectall', 521, 1572, 334, 108, text='Select All', taborder=70)
        self.add('commandbutton', 'cb_print', 997, 1580, 334, 100, text='&Print', taborder=60)
        self.add('commandbutton', 'cb_exit', 1463, 1580, 334, 100, text='E&xit', taborder=40)
        self.add('checkbox', 'cbx_skip', 521, 1692, 690, 76, text='Skip After Each Report')
        self.add('checkbox', 'cbx_view', 1463, 1700, 530, 80, text='View before Print')
