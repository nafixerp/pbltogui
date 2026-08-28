"""All in one Entry — w_refinary.

Generated from the PowerBuilder window ``w_refinary.srw`` by
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
    name='w_refinary',
    title='All in one Entry',
    width=3653,
    height=1824,
    controls=[],
    tables=['items', 'itemsstk', 'refinerym', 'daybook', 'refineryd', 'clients', 'accountm', 'sman', 'generali', 'daybookpart', 'delpart'],
    source_path='w_refinary.srw',
)


class AllInOneEntryForm(GeneratedForm):
    """All in one Entry"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('statictext', 'st_billno', 357, 4, 421, 88)
        self.add('statictext', 'st_bill', 32, 8, 297, 88, text='Doc No. :')
        self.add('editmask', 'em_date', 1435, 12, 443, 92, taborder=10)
        self.add('datawindow', 'dw_smcode', 2889, 12, 677, 88, dataobject='d_smancode', taborder=20)
        self.add('statictext', 'st_date', 1184, 20, 233, 88, text='Date :')
        self.add('statictext', 'st_4', 2633, 20, 247, 76, text='SM :')
        self.add('statictext', 'st_custcode', 69, 128, 261, 84, text='Refiner :')
        self.add('datawindow', 'dw_1', 352, 128, 416, 88, dataobject='d_refncode', taborder=30)
        self.add('commandbutton', 'cb_custhelp', 768, 128, 59, 88, text='^')
        self.add('statictext', 'st_customer', 1184, 136, 233, 84, text='Name :')
        self.add('statictext', 'st_rname', 1435, 136, 805, 84)
        self.add('statictext', 'st_6', 2418, 140, 462, 92, text='Test Pieces % :')
        self.add('datawindow', 'dw_sale', 14, 264, 3566, 932, dataobject='d_refnreturn', taborder=40)
        self.add('statictext', 'st_15', 430, 264, 5, 840)
        self.add('statictext', 'st_10', 837, 264, 5, 932)
        self.add('statictext', 'st_21', 1015, 264, 5, 932)
        self.add('statictext', 'st_45', 1280, 264, 5, 932)
        self.add('statictext', 'st_12', 2025, 264, 5, 932)
        self.add('statictext', 'st_30', 2222, 264, 5, 932)
        self.add('statictext', 'st_65', 2427, 264, 5, 932)
        self.add('statictext', 'st_13', 2642, 264, 5, 932)
        self.add('statictext', 'st_14', 2816, 264, 5, 932)
        self.add('statictext', 'st_26', 3131, 264, 5, 932)
        self.add('statictext', 'st_11', 1499, 268, 5, 932)
        self.add('statictext', 'st_22', 1797, 268, 5, 932)
        self.add('statictext', 'st_stktype', 485, 1104, 169, 76)
        self.add('commandbutton', 'cb_add', 23, 1108, 224, 76, text='&Add', taborder=80)
        self.add('commandbutton', 'cb_delete', 251, 1108, 224, 76, text='&Delete', taborder=90)
        self.add('roundrectangle', 'rr_1', 2907, 1236, 667, 256)
        self.add('editmask', 'em_tcharge', 622, 1256, 375, 88, taborder=50)
        self.add('editmask', 'em_netbalance', 2418, 1256, 393, 88)
        self.add('commandbutton', 'cb_save', 2985, 1264, 521, 96, text='&Save', taborder=100)
        self.add('statictext', 'st_7', 0, 1268, 608, 76, text='Total Charge amt.  :')
        self.add('statictext', 'st_9', 1993, 1268, 421, 76, text='Net Balance :')
        self.add('commandbutton', 'cb_exit', 2985, 1364, 521, 96, text='E&xit', taborder=110)
        self.add('singlelineedit', 'sle_note', 622, 1384, 1138, 88, limit=30, taborder=60)
        self.add('editmask', 'em_paidamt', 2418, 1384, 393, 88, taborder=70)
        self.add('statictext', 'st_18', 334, 1392, 274, 76, text='Note  :')
        self.add('statictext', 'st_8', 1970, 1396, 443, 76, text='Amount Paid :')
