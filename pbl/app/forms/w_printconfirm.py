"""Print Confirm — w_printconfirm.

Generated from the PowerBuilder window ``w_printconfirm.srw`` by
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
    name='w_printconfirm',
    title='Print Confirm',
    width=4608,
    height=1784,
    controls=[],
    tables=['daybook', 'salesm', 'items', 'itemsstk', 'salesrm', 'purchasem', 'salesd', 'orderm', 'purchased', 'salesrd', 'clients', 'salestype', 'barcode', 'pdclist', 'stkandprofit', 'oglist', 'spdmddet', 'generali', 'generals', 'daybookpart', 'userd', 'generald', 'delpart', 'userm'],
    source_path='w_printconfirm.srw',
    grid={'control': 'dw_1', 'dataobject': 'd_printconfirm', 'table': 'salesm', 'keys': ['slno'], 'columns': [{'name': 'tdate', 'label': 'Date', 'type': 'date'}, {'name': 'billno', 'label': 'Doc No', 'type': 'char'}, {'name': 'ramt', 'label': 'Rcvd Amt', 'type': 'decimal'}, {'name': 'discount', 'label': 'Discount', 'type': 'decimal'}, {'name': 'slno', 'label': 'slno', 'type': 'decimal'}, {'name': 'custcode', 'label': 'custcode', 'type': 'char'}, {'name': 'custname', 'label': 'custname', 'type': 'char'}, {'name': 'smcode', 'label': 'smcode', 'type': 'char'}, {'name': 'cocode', 'label': 'cocode', 'type': 'char'}, {'name': 'staxamt', 'label': 'staxamt', 'type': 'decimal'}, {'name': 'duedate', 'label': 'duedate', 'type': 'date'}, {'name': 'control', 'label': 'control', 'type': 'long'}, {'name': 'orderno', 'label': 'orderno', 'type': 'char'}, {'name': 'netamt', 'label': 'Net Amt', 'type': 'decimal'}, {'name': 'disc2', 'label': 'disc2', 'type': 'decimal'}, {'name': 'staxamt2', 'label': 'staxamt2', 'type': 'decimal'}, {'name': 'sr', 'label': 'sr', 'type': 'char'}, {'name': 'balance', 'label': 'balance', 'type': 'decimal'}, {'name': 'netamt', 'label': 'Net Amt', 'type': 'decimal'}, {'name': 'ccamt', 'label': 'ccamt', 'type': 'decimal'}, {'name': 'chqamt', 'label': 'chqamt', 'type': 'decimal'}, {'name': 'cbcode', 'label': 'cbcode', 'type': 'char'}, {'name': 'nodisc', 'label': 'nodisc', 'type': 'long'}]},
    report={'dataobject': 'd_printconfirm', 'sql': 'SELECT "salesm"."tdate",   \r\n         "salesm"."billno",   \r\n         "salesm"."ramt",   \r\n         "salesm"."discount",   \r\n         "salesm"."slno",   \r\n         "salesm"."custcode",   \r\n         "salesm"."custname",   \r\n         "salesm"."smcode",   \r\n\t\t"salesm"."cocode",   \r\n\t\t"salesm"."staxamt",\r\n         "salesm"."duedate",   \r\n         "salesm"."control",   \r\n         "salesm"."orderno",   \r\n         "salesm"."netamt",   \r\n         "salesm"."discount" as disc2,   \r\n\t\t"salesm"."staxamt" as staxamt2,\r\n\t\t"salesm"."sr",   \r\n         (salesm.netamt - salesm.ramt) as balance,   \r\n         (salesm.netamt ) as netamt,\r\n\t\t(salesm.ccamt ) as ccamt,\r\n\t\t(salesm.chqamt ) as chqamt,\r\n\t\t(salesm.cbcode) as cbcode,\r\n\t\t(select count(barcode.bcode) from barcode,salesd where salesd.slno = salesm.slno and barcode.bcode = salesd.bcode and barcode.nodisc = \'N\') as nodisc  \r\n    FROM "salesm"  \r\n   WHERE "salesm"."control" = 3 \r\nORDER BY "salesm"."tdate" ASC,   \r\n         "salesm"."slno" ASC,   \r\n         "salesm"."billno" ASC', 'args': [], 'arg_types': {}, 'tables': ['salesm'], 'columns': [{'name': 'tdate', 'label': 'Date', 'type': 'date'}, {'name': 'billno', 'label': 'Doc No', 'type': 'char'}, {'name': 'ramt', 'label': 'Rcvd Amt', 'type': 'decimal'}, {'name': 'discount', 'label': 'Discount', 'type': 'decimal'}, {'name': 'slno', 'label': 'slno', 'type': 'decimal'}, {'name': 'custcode', 'label': 'custcode', 'type': 'char'}, {'name': 'custname', 'label': 'custname', 'type': 'char'}, {'name': 'smcode', 'label': 'smcode', 'type': 'char'}, {'name': 'cocode', 'label': 'cocode', 'type': 'char'}, {'name': 'staxamt', 'label': 'staxamt', 'type': 'decimal'}, {'name': 'duedate', 'label': 'duedate', 'type': 'date'}, {'name': 'control', 'label': 'control', 'type': 'long'}, {'name': 'orderno', 'label': 'orderno', 'type': 'char'}, {'name': 'netamt', 'label': 'Net Amt', 'type': 'decimal'}, {'name': 'disc2', 'label': 'disc2', 'type': 'decimal'}, {'name': 'staxamt2', 'label': 'staxamt2', 'type': 'decimal'}, {'name': 'sr', 'label': 'sr', 'type': 'char'}, {'name': 'balance', 'label': 'balance', 'type': 'decimal'}, {'name': 'netamt', 'label': 'Net Amt', 'type': 'decimal'}, {'name': 'ccamt', 'label': 'ccamt', 'type': 'decimal'}, {'name': 'chqamt', 'label': 'chqamt', 'type': 'decimal'}, {'name': 'cbcode', 'label': 'cbcode', 'type': 'char'}, {'name': 'nodisc', 'label': 'nodisc', 'type': 'long'}]},
    opens=['w_tran_view', 'w_sales_view_only', 'w_sales_view', 'w_diamond_sales_print', 'w_clientshelp', 'w_sucu'],
)


class PrintConfirmForm(GeneratedForm):
    """Print Confirm"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('datawindow', 'dw_1', 0, 12, 4594, 1432, dataobject='d_printconfirm', taborder=30)
        self.add('commandbutton', 'cb_refresh', 283, 1496, 434, 108, text='&Refresh', taborder=20)
        self.add('commandbutton', 'cb_view', 905, 1496, 434, 108, text='View', taborder=40)
        self.add('commandbutton', 'cb_edit', 1435, 1496, 434, 108, text='&Edit', taborder=10)
        self.add('commandbutton', 'cb_delete', 1947, 1496, 434, 108, text='&Delete', taborder=50)
        self.add('commandbutton', 'cb_fullprint', 2450, 1496, 434, 108, text='&Full Print', taborder=5)
        self.add('commandbutton', 'cb_print', 2967, 1496, 434, 108, text='Update && &Print', taborder=40)
        self.add('checkbox', 'cbx_laser', 3442, 1508, 384, 80, text='Laser Print')
        self.add('checkbox', 'cbx_updtfr', 3845, 1508, 219, 80, text='Fr')
        self.add('checkbox', 'cbx_esttobill', 4087, 1508, 384, 80, text='Est To Bill')
