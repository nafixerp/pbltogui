"""Stock Transfer Multi Entry — w_itemadj_multi.

Generated from the PowerBuilder window ``w_itemadj_multi.srw`` by
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
    name='w_itemadj_multi',
    title='Stock Transfer Multi Entry',
    width=2514,
    height=2200,
    controls=[],
    tables=['items', 'barcode', 'itemsstk', 'itemadj', 'bc', 'stk', 'item', 'generali'],
    source_path='w_itemadj_multi.srw',
)


class StockTransferMultiEntryForm(GeneratedForm):
    """Stock Transfer Multi Entry"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('statictext', 'st_billno', 283, 0, 443, 88)
        self.add('singlelineedit', 'sle_itemcode', 1115, 0, 421, 88, limit=10, taborder=10)
        self.add('singlelineedit', 'sle_desc', 1783, 0, 677, 88, limit=30)
        self.add('statictext', 'st_5', 0, 4, 274, 76, text='Doc No. :')
        self.add('statictext', 'st_1', 750, 8, 352, 76, text='From Item :')
        self.add('commandbutton', 'cb_help', 1563, 8, 169, 84, text='&Help')
        self.add('editmask', 'em_date', 283, 92, 443, 96, taborder=20)
        self.add('commandbutton', 'cb_setdef', 1115, 96, 421, 88, text='Set as default')
        self.add('datawindow', 'dw_smcode', 1783, 96, 677, 88, dataobject='d_smancode', taborder=30)
        self.add('statictext', 'st_date', 91, 100, 178, 88, text='Date :')
        self.add('statictext', 'st_4', 1600, 104, 174, 76, text='SM :')
        self.add('datawindow', 'dw_stktypefrom', 1783, 184, 539, 88, dataobject='d_stktypecode', taborder=40)
        self.add('statictext', 'st_2', 1303, 188, 471, 76, text='From Stk Type :')
        self.add('datawindow', 'dw_grp', 283, 192, 800, 88, dataobject='d_itemgrpcode', taborder=50)
        self.add('statictext', 'st_6', 5, 204, 265, 88, text='Group :')
        self.add('datawindow', 'dw_stktypeto', 1783, 276, 539, 88, dataobject='d_stktypecode', taborder=50)
        self.add('statictext', 'st_3', 1381, 288, 393, 76, text='To Stk Type :')
        self.add('checkbox', 'cbx_pendonly', 283, 292, 407, 68, text='BC Pend Only')
        self.add('commandbutton', 'cb_getfrombclist', 283, 364, 841, 96, text='Take from BC List (Summary)')
        self.add('datawindow', 'dw_sale', 5, 464, 2464, 1496, dataobject='d_itemadj_multi', taborder=60)
        self.add('statictext', 'st_15', 393, 464, 5, 1404)
        self.add('statictext', 'st_9', 1262, 464, 5, 1496)
        self.add('statictext', 'st_13', 1499, 464, 5, 1496)
        self.add('statictext', 'st_50', 1783, 464, 5, 1496)
        self.add('statictext', 'st_21', 2030, 464, 5, 1496)
        self.add('statictext', 'st_stktype', 814, 1868, 229, 76)
        self.add('commandbutton', 'cb_add', 14, 1872, 224, 76, text='&Add', taborder=70)
        self.add('commandbutton', 'cb_delete', 242, 1872, 224, 76, text='&Delete', taborder=80)
        self.add('commandbutton', 'cb_save', 882, 1972, 306, 88, text='&Save', taborder=90)
        self.add('commandbutton', 'cb_exit', 1221, 1972, 306, 88, text='E&xit', taborder=100)
