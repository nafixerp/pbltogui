"""Barcode Multi Entry — w_barcode_entryall.

Generated from the PowerBuilder window ``w_barcode_entryall.srw`` by
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
    name='w_barcode_entryall',
    title='Barcode Multi Entry',
    width=5143,
    height=1952,
    controls=[],
    tables=['barcode', 'items', 'itemsstk', 'itemadj', 'stk', 'item', 'generali'],
    source_path='w_barcode_entryall.srw',
)


class BarcodeMultiEntryForm(GeneratedForm):
    """Barcode Multi Entry"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('statictext', 'st_billno', 283, 0, 443, 88)
        self.add('singlelineedit', 'sle_itemcode', 1115, 0, 421, 88, limit=10, taborder=10)
        self.add('singlelineedit', 'sle_desc', 1783, 0, 677, 88, limit=30)
        self.add('datawindow', 'dw_stktypefrom', 3049, 0, 539, 88, dataobject='d_stktypecode', taborder=40)
        self.add('statictext', 'st_5', 0, 4, 274, 76, text='Doc No. :')
        self.add('statictext', 'st_2', 2565, 4, 471, 76, text='From Stk Type :')
        self.add('statictext', 'st_1', 750, 8, 352, 76, text='From Item :')
        self.add('commandbutton', 'cb_help', 1563, 8, 169, 84, text='&Help')
        self.add('datawindow', 'dw_smith', 3991, 8, 672, 88, dataobject='d_smithsuppliercode', taborder=50)
        self.add('statictext', 'st_23', 3671, 16, 306, 76, text='Supplier :')
        self.add('editmask', 'em_date', 283, 100, 443, 96, taborder=20)
        self.add('commandbutton', 'cb_setdef', 1115, 104, 421, 88, text='Set as default')
        self.add('datawindow', 'dw_smcode', 1787, 104, 677, 88, dataobject='d_smancode', taborder=30)
        self.add('datawindow', 'dw_stktypeto', 3049, 104, 539, 88, dataobject='d_stktypecode', taborder=50)
        self.add('statictext', 'st_date', 91, 108, 178, 88, text='Date :')
        self.add('statictext', 'st_4', 1600, 112, 174, 76, text='SM :')
        self.add('statictext', 'st_3', 2642, 116, 393, 76, text='To Stk Type :')
        self.add('datawindow', 'dw_sale', 5, 204, 5106, 1496, dataobject='d_barcode_entryall', taborder=60)
        self.add('statictext', 'st_15', 320, 204, 5, 1404)
        self.add('statictext', 'st_10', 704, 204, 5, 1408)
        self.add('statictext', 'st_90', 1088, 204, 5, 1496)
        self.add('statictext', 'st_14', 1440, 204, 5, 1496)
        self.add('statictext', 'st_9', 1627, 204, 5, 1496)
        self.add('statictext', 'st_13', 1888, 204, 5, 1496)
        self.add('statictext', 'st_50', 2066, 204, 5, 1496)
        self.add('statictext', 'st_21', 2345, 204, 5, 1496)
        self.add('statictext', 'st_45', 2574, 204, 5, 1496)
        self.add('statictext', 'st_60', 2862, 204, 5, 1496)
        self.add('statictext', 'st_12', 3461, 204, 5, 1496)
        self.add('statictext', 'st_8', 3653, 204, 5, 1496)
        self.add('statictext', 'st_25', 3899, 204, 5, 1496)
        self.add('statictext', 'st_6', 4215, 204, 5, 1496)
        self.add('statictext', 'st_7', 4434, 204, 5, 1496)
        self.add('statictext', 'st_16', 4832, 204, 5, 1496)
        self.add('statictext', 'st_11', 3127, 208, 5, 1496)
        self.add('statictext', 'st_22', 3301, 208, 5, 1496)
        self.add('statictext', 'st_stktype', 485, 1608, 229, 76)
        self.add('commandbutton', 'cb_add', 14, 1612, 224, 76, text='&Add', taborder=70)
        self.add('commandbutton', 'cb_delete', 242, 1612, 224, 76, text='&Delete', taborder=80)
        self.add('commandbutton', 'cb_save', 1463, 1732, 402, 104, text='&Save ( F9 )', taborder=90)
        self.add('commandbutton', 'cb_exit', 1915, 1732, 402, 104, text='E&xit', taborder=100)
        self.add('commandbutton', 'cb_1', 2880, 1732, 389, 104, text='Barcode List', taborder=101)
        self.add('commandbutton', 'cb_print', 3291, 1732, 393, 104, text='&Print ( F5 )', taborder=110)
        self.add('checkbox', 'cbx_bcsave', 3808, 1740, 535, 80, text='BC Save on Print')
