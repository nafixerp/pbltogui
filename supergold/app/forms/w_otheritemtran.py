"""New — w_otheritemtran.

Generated from the PowerBuilder window ``w_otheritemtran.srw`` by
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
    name='w_otheritemtran',
    title='New',
    width=2985,
    height=1528,
    controls=[],
    tables=['itemsothers', 'daybook', 'oitemtranm', 'oitemtrand', 'clients', 'accountm', 'generali', 'daybookpart', 'delpart'],
    source_path='w_otheritemtran.srw',
    opens=['w_clientshelp', 'w_sucu', 'w_item_others_help'],
)


class NewForm(GeneratedForm):
    """New"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('statictext', 'st_billno', 402, 0, 402, 88)
        self.add('editmask', 'em_date', 2501, 0, 402, 96)
        self.add('statictext', 'st_bill', 82, 8, 306, 64, text='Doc No :')
        self.add('statictext', 'st_date', 2231, 8, 256, 64, text='Date :')
        self.add('datawindow', 'dw_1', 402, 108, 402, 88, dataobject='d_cust', taborder=10)
        self.add('singlelineedit', 'st_custname', 887, 108, 1234, 88, limit=30, taborder=20)
        self.add('editmask', 'em_ob', 2501, 108, 398, 88)
        self.add('commandbutton', 'cb_custhelp', 823, 112, 64, 84, text='^')
        self.add('statictext', 'st_custcode', 27, 116, 361, 72, text='Customer :')
        self.add('statictext', 'st_13', 2295, 116, 192, 76, text='OB :')
        self.add('editmask', 'em_custcode', 1157, 208, 329, 96, taborder=60)
        self.add('datawindow', 'dw_smcode', 402, 216, 677, 88, dataobject='d_smancode', taborder=30)
        self.add('statictext', 'st_customer', 41, 228, 347, 64, text='SM Name :')
        self.add('datawindow', 'dw_sale', 59, 324, 2848, 860, dataobject='d_oitemtran', taborder=40)
        self.add('statictext', 'st_10', 512, 328, 5, 760)
        self.add('statictext', 'st_9', 1751, 328, 5, 856)
        self.add('statictext', 'st_3', 2039, 328, 5, 856)
        self.add('statictext', 'st_4', 2395, 328, 5, 856)
        self.add('commandbutton', 'cb_add', 73, 1092, 238, 80, text='&Add')
        self.add('commandbutton', 'cb_delete', 315, 1092, 238, 80, text='&Delete')
        self.add('roundrectangle', 'rr_1', 2478, 1180, 434, 232)
        self.add('editmask', 'em_billtotal', 389, 1200, 366, 84)
        self.add('editmask', 'em_addamt', 1253, 1200, 366, 84, taborder=80)
        self.add('statictext', 'st_2', 1774, 1204, 311, 76, text='Less Amt :')
        self.add('editmask', 'em_lessamt', 2094, 1204, 366, 84, taborder=50)
        self.add('statictext', 'st_1', 923, 1208, 315, 76, text='Add Amt. :')
        self.add('commandbutton', 'cb_save', 2510, 1208, 366, 84, text='&Save', taborder=90)
        self.add('statictext', 'st_billtotal', 46, 1212, 329, 76, text='Bill Total :')
        self.add('editmask', 'em_ramt', 1253, 1296, 366, 84, taborder=70)
        self.add('editmask', 'em_balance', 2094, 1296, 366, 84)
        self.add('editmask', 'em_nettot', 389, 1300, 366, 84)
        self.add('statictext', 'st_ramt', 850, 1300, 389, 76, text='Received :')
        self.add('statictext', 'st_balance', 1769, 1304, 315, 76, text='Balance :')
        self.add('commandbutton', 'cb_exit', 2510, 1304, 366, 84, text='E&xit', taborder=100)
        self.add('statictext', 'st_nettot', 64, 1308, 311, 76, text='Net Total :')
