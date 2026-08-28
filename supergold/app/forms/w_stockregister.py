"""Stock Register — w_stockregister.

Generated from the PowerBuilder window ``w_stockregister.srw`` by
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
    name='w_stockregister',
    title='Stock Register',
    width=3666,
    height=2364,
    controls=[],
    tables=['itemadj', 'refineryd', 'items', 'smithm', 'smithd', 'repaird', 'purchasem', 'purchaserm', 'salesm', 'salesrm', 'itemgrp', 'purchased', 'purchaserd', 'salesrd', 'orderdga', 'salesd', 'date'],
    source_path='w_stockregister.srw',
)


class StockRegisterForm(GeneratedForm):
    """Stock Register"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('datawindow', 'dw_grp', 238, 0, 800, 88, dataobject='d_itemgrpcode', taborder=50)
        self.add('commandbutton', 'cb_show', 2510, 0, 288, 96, text='&Show', taborder=40)
        self.add('commandbutton', 'cb_saveas', 2839, 0, 274, 96, text='Save &As', taborder=70)
        self.add('commandbutton', 'cb_print', 3122, 0, 247, 96, text='&Print', taborder=80)
        self.add('commandbutton', 'cb_exit', 3378, 0, 247, 96, text='E&xit', taborder=60)
        self.add('statictext', 'st_grp', 0, 4, 229, 76, text='Group :')
        self.add('checkbox', 'cbx_grp', 1047, 8, 78, 76)
        self.add('checkbox', 'cbx_qtybased', 1559, 8, 402, 80, text='Qty Based')
        self.add('checkbox', 'cbx_summary', 2043, 8, 402, 80, text='Summary')
        self.add('singlelineedit', 'sle_itemcode', 238, 96, 416, 96, limit=10, taborder=10)
        self.add('commandbutton', 'cb_help', 663, 96, 133, 96, text='&Help')
        self.add('editmask', 'em_date1', 1024, 96, 393, 92, taborder=20)
        self.add('editmask', 'em_date2', 1559, 96, 398, 92, taborder=30)
        self.add('statictext', 'st_date', 2112, 100, 384, 84)
        self.add('statictext', 'st_3', 59, 104, 169, 72, text='Item :')
        self.add('statictext', 'st_1', 809, 104, 206, 76, text='From :')
        self.add('statictext', 'st_2', 1435, 104, 119, 76, text='To :')
        self.add('checkbox', 'cbx_withnetwgt', 2519, 116, 407, 76, text='With Netwgt')
        self.add('checkbox', 'cbx_speed', 3081, 116, 393, 76, text='Speed Print')
        self.add('datawindow', 'dw_history', 5, 200, 3630, 1960, dataobject='d_stockregister', taborder=50)
