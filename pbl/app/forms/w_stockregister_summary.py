"""Stock Register Summary — w_stockregister_summary.

Generated from the PowerBuilder window ``w_stockregister_summary.srw`` by
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
    name='w_stockregister_summary',
    title='Stock Register Summary',
    width=3675,
    height=2444,
    controls=[],
    tables=['refineryd', 'itemadj', 'smithm', 'items', 'smithd', 'repaird', 'purchasem', 'salesrm', 'salesm', 'purchaserm', 'purchased', 'purchaserd', 'salesrd', 'orderdga', 'salesd', 'date', 'clients'],
    source_path='w_stockregister_summary.srw',
)


class StockRegisterSummaryForm(GeneratedForm):
    """Stock Register Summary"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 219, 0, 462, 92, taborder=20)
        self.add('editmask', 'em_date2', 864, 0, 466, 92, taborder=30)
        self.add('commandbutton', 'cb_show', 2510, 0, 288, 96, text='&Show', taborder=40)
        self.add('commandbutton', 'cb_saveas', 2839, 0, 274, 96, text='Save &As', taborder=70)
        self.add('commandbutton', 'cb_print', 3122, 0, 247, 96, text='&Print', taborder=80)
        self.add('commandbutton', 'cb_exit', 3378, 0, 247, 96, text='E&xit', taborder=60)
        self.add('statictext', 'st_1', 5, 8, 206, 76, text='From :')
        self.add('statictext', 'st_2', 736, 8, 119, 76, text='To :')
        self.add('checkbox', 'cbx_withnetwgt', 1417, 8, 407, 76, text='With Netwgt')
        self.add('checkbox', 'cbx_cptostock', 1979, 8, 421, 76, text='CP To Stock')
        self.add('datawindow', 'dw_history', 5, 104, 3630, 2056, dataobject='d_stockregister_summary', taborder=50)
        self.add('statictext', 'st_date', 1929, 116, 421, 84)
        self.add('checkbox', 'cbx_speed', 3081, 116, 393, 76, text='Speed Print')
