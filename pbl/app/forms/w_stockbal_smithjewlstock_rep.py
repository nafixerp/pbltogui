"""Item Stock,Party Wgt Report — w_stockbal_smithjewlstock_rep.

Generated from the PowerBuilder window ``w_stockbal_smithjewlstock_rep.srw`` by
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
    name='w_stockbal_smithjewlstock_rep',
    title='Item Stock,Party Wgt Report',
    width=3630,
    height=2228,
    controls=[],
    tables=['clients', 'items', 'clientsgrp', 'oglist', 'itemgrp', 'clientsgs', 'smithd', 'refineryd', 'kuricolln', 'orderdga'],
    source_path='w_stockbal_smithjewlstock_rep.srw',
)


class ItemStockPartyWgtReportForm(GeneratedForm):
    """Item Stock,Party Wgt Report"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date', 192, 0, 347, 96, taborder=10)
        self.add('dropdownlistbox', 'ddlb_wgtstatus', 549, 0, 507, 588, text='All', items=['All', 'Only To Get', 'Only To Give'], taborder=20)
        self.add('datawindow', 'dw_grp', 1344, 0, 681, 88, dataobject='d_clientsgrp_code', taborder=60)
        self.add('commandbutton', 'cb_show', 2487, 0, 247, 96, text='Show', taborder=30)
        self.add('commandbutton', 'cb_3', 2738, 0, 270, 96, text='Save &As', taborder=80)
        self.add('commandbutton', 'cb_1', 3026, 0, 279, 92, text='&Print', taborder=40)
        self.add('commandbutton', 'cb_2', 3310, 0, 279, 92, text='E&xit', taborder=70)
        self.add('statictext', 'st_grp', 1115, 4, 224, 76, text='Group :')
        self.add('statictext', 'st_1', 5, 8, 178, 76, text='Up to :')
        self.add('checkbox', 'cbx_grp', 2034, 8, 82, 76)
        self.add('statictext', 'st_4', 9, 100, 178, 76, text='Rate :')
        self.add('editmask', 'em_rate', 192, 100, 347, 92, taborder=61)
        self.add('dropdownlistbox', 'ddlb_reptype', 544, 100, 512, 532, text='Detailed', items=['Detailed', 'Groupwise', 'Split Grp Details'], taborder=61)
        self.add('editmask', 'em_touch', 1349, 100, 247, 88, taborder=51)
        self.add('editmask', 'em_schmtouch', 1961, 100, 206, 88, taborder=70)
        self.add('commandbutton', 'cb_sort', 3310, 100, 279, 80, text='Sort', taborder=70)
        self.add('statictext', 'st_2', 1079, 112, 261, 76, text='To Touch :')
        self.add('statictext', 'st_5', 1600, 112, 357, 76, text='Schm Touch :')
        self.add('checkbox', 'cbx_withbalonly', 2487, 112, 590, 80, text='With balance only')
        self.add('datawindow', 'dw_1', 0, 200, 3598, 1912, dataobject='d_stockbal_smithjewlstock_grp_rep', taborder=50)
