"""Rate Diff Adjustment — w_ratediffadjust.

Generated from the PowerBuilder window ``w_ratediffadjust.srw`` by
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
    name='w_ratediffadjust',
    title='Rate Diff Adjustment',
    width=2002,
    height=1636,
    controls=[],
    tables=['salesm', 'daybook', 'collection', 'clients', 'daybookratewgt', 'salesd', 'generali', 'daybookpart'],
    source_path='w_ratediffadjust.srw',
    opens=['w_clientshelp', 'w_salehelp'],
)


class RateDiffAdjustmentForm(GeneratedForm):
    """Rate Diff Adjustment"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date', 713, 0, 402, 92, taborder=10)
        self.add('statictext', 'st_2', 443, 12, 247, 76, text='Date :')
        self.add('datawindow', 'dw_accode', 713, 96, 402, 88, dataobject='d_cust', taborder=20)
        self.add('statictext', 'st_10', 357, 108, 338, 72, text='Party  :')
        self.add('singlelineedit', 'sle_name', 713, 188, 1253, 92)
        self.add('statictext', 'st_9', 352, 196, 343, 80, text='Name :')
        self.add('editmask', 'em_balance', 713, 284, 421, 96)
        self.add('editmask', 'em_pwgtbal', 1545, 284, 421, 96, taborder=30)
        self.add('statictext', 'st_11', 297, 296, 398, 80, text='A/c Balance :')
        self.add('statictext', 'st_14', 1157, 296, 370, 80, text='Wgt Bal :')
        self.add('singlelineedit', 'sle_billno', 713, 384, 421, 92, limit=13, taborder=30)
        self.add('commandbutton', 'cb_help', 1143, 388, 187, 84, text='&Help')
        self.add('statictext', 'st_1', 270, 396, 425, 64, text='Enter Bill no :')
        self.add('editmask', 'em_netamt', 713, 480, 421, 96)
        self.add('statictext', 'st_3', 416, 488, 279, 76, text='Net Amt :')
        self.add('editmask', 'em_weight', 713, 580, 421, 100, taborder=40)
        self.add('statictext', 'st_7', 384, 592, 311, 76, text='Weight :')
        self.add('editmask', 'em_wgtbal', 713, 684, 421, 96)
        self.add('statictext', 'st_12', 146, 688, 549, 76, text='Weight (Balance) :')
        self.add('editmask', 'em_oldrate', 713, 784, 421, 100, taborder=50)
        self.add('statictext', 'st_6', 384, 796, 311, 76, text='Old Rate :')
        self.add('editmask', 'em_newrate', 713, 888, 421, 100, taborder=60)
        self.add('statictext', 'st_4', 366, 900, 329, 76, text='New Rate :')
        self.add('editmask', 'em_diffamt', 713, 992, 421, 100, taborder=70)
        self.add('statictext', 'st_5', 302, 1000, 389, 76, text='Diff Amount :')
        self.add('editmask', 'em_clbalance', 713, 1096, 421, 96)
        self.add('statictext', 'st_8', 215, 1104, 475, 76, text='A/c Cl.Balance :')
        self.add('editmask', 'em_clwgtbal', 713, 1200, 421, 96, taborder=80)
        self.add('statictext', 'st_13', 192, 1204, 498, 76, text='Wgt Cl.Balance :')
        self.add('oval', 'oval_1', 635, 1316, 713, 208)
        self.add('commandbutton', 'cb_ok', 750, 1372, 233, 96, text='&Ok', taborder=80)
        self.add('commandbutton', 'cb_exit', 1006, 1372, 233, 96, text='E&xit', taborder=90)
