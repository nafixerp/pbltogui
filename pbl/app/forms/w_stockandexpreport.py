"""Stock,Asset,Liablity,Expense Report — w_stockandexpreport.

Generated from the PowerBuilder window ``w_stockandexpreport.srw`` by
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
    name='w_stockandexpreport',
    title='Stock,Asset,Liablity,Expense Report',
    width=3666,
    height=2684,
    controls=[],
    tables=['items', 'smithd', 'clientsgs', 'barcode'],
    source_path='w_stockandexpreport.srw',
)


class StockAssetLiablityExpenseReportForm(GeneratedForm):
    """Stock,Asset,Liablity,Expense Report"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('commandbutton', 'cb_show', 2551, 0, 261, 100, text='&Show', taborder=30)
        self.add('commandbutton', 'cb_4', 2830, 0, 270, 100, text='Save &As', taborder=60)
        self.add('commandbutton', 'cb_1', 3104, 0, 247, 100, text='&Print', taborder=80)
        self.add('commandbutton', 'cb_2', 3360, 0, 247, 100, text='E&xit', taborder=50)
        self.add('editmask', 'em_date1', 361, 8, 439, 88, taborder=10)
        self.add('editmask', 'em_date2', 1106, 8, 439, 88, taborder=20)
        self.add('statictext', 'st_1', 14, 12, 343, 76, text='Date From :')
        self.add('statictext', 'st_2', 832, 12, 270, 76, text='Date To :')
        self.add('datawindow', 'dw_1', 0, 104, 3611, 2264, dataobject='d_stock_asset_expreport', taborder=40)
