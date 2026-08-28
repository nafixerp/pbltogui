"""Item Adjustment — w_itemadjrepo.

Generated from the PowerBuilder window ``w_itemadjrepo.srw`` by
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
    name='w_itemadjrepo',
    title='Item Adjustment',
    width=3639,
    height=2308,
    controls=[],
    tables=['itemadj', 'stktype', 'code', 'items', 'barcode', 'item', 'qty', 'wgt', 'stn'],
    source_path='w_itemadjrepo.srw',
    report={'dataobject': 'd_itemadj', 'sql': 'SELECT itemadj.fromcode AS itemadj_fromcode, itemadj.fromqty AS itemadj_fromqty, itemadj.fromwgt AS itemadj_fromwgt, itemadj.tocode AS itemadj_tocode, itemadj.toqty AS itemadj_toqty, itemadj.towgt AS itemadj_towgt, itemadj.particular AS itemadj_particular, itemadj.tdate AS itemadj_tdate, itemadj.ttime AS itemadj_ttime, itemadj.smcode AS itemadj_smcode, itemadj.slno AS itemadj_slno, itemadj.al AS itemadj_al, itemadj.fromstktype AS itemadj_fromstktype, itemadj.tostktype AS itemadj_tostktype, itemadj.fromstwgt AS itemadj_fromstwgt, itemadj.tostwgt AS itemadj_tostwgt, itemadj.ichange AS itemadj_ichange, itemadj.bcode AS itemadj_bcode, (select name from items where items.code = fromcode) as fromname, (select name from items where items.code = tocode) as toname, 0 as prn FROM itemadj WHERE itemadj.control <= :rlevel AND itemadj.tdate between :date1 and :date2 ORDER BY itemadj.tdate ASC', 'args': ['rlevel', 'date1', 'date2'], 'arg_types': {'rlevel': 'number', 'date1': 'date', 'date2': 'date'}, 'tables': ['itemadj'], 'columns': [{'name': 'fromcode', 'label': 'fromcode', 'type': 'char'}, {'name': 'fromqty', 'label': 'fromqty', 'type': 'long'}, {'name': 'fromwgt', 'label': 'fromwgt', 'type': 'decimal'}, {'name': 'tocode', 'label': 'tocode', 'type': 'char'}, {'name': 'toqty', 'label': 'toqty', 'type': 'long'}, {'name': 'towgt', 'label': 'towgt', 'type': 'decimal'}, {'name': 'particular', 'label': 'particular', 'type': 'char'}, {'name': 'tdate', 'label': 'tdate', 'type': 'date'}, {'name': 'fromname', 'label': 'fromname', 'type': 'char'}, {'name': 'toname', 'label': 'toname', 'type': 'char'}, {'name': 'ttime', 'label': 'ttime', 'type': 'time'}, {'name': 'smcode', 'label': 'smcode', 'type': 'char'}, {'name': 'prn', 'label': 'prn', 'type': 'long'}, {'name': 'slno', 'label': 'slno', 'type': 'decimal'}, {'name': 'al', 'label': 'al', 'type': 'char'}, {'name': 'fromstktype', 'label': 'fromstktype', 'type': 'char'}, {'name': 'tostktype', 'label': 'tostktype', 'type': 'char'}, {'name': 'fromstwgt', 'label': 'fromstwgt', 'type': 'decimal'}, {'name': 'tostwgt', 'label': 'tostwgt', 'type': 'decimal'}, {'name': 'ichange', 'label': 'ichange', 'type': 'long'}, {'name': 'bcode', 'label': 'bcode', 'type': 'decimal'}]},
)


class ItemAdjustmentForm(GeneratedForm):
    """Item Adjustment"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date2', 1275, 0, 411, 100, taborder=20)
        self.add('datawindow', 'dw_fromstktype', 2130, 0, 539, 88, dataobject='d_stktypecode', taborder=100)
        self.add('commandbutton', 'cb_show', 2683, 0, 261, 100, text='&Show', taborder=40)
        self.add('commandbutton', 'cb_1', 2985, 0, 247, 92, text='&Print', taborder=140)
        self.add('commandbutton', 'cb_2', 3360, 0, 247, 92, text='E&xit', taborder=130)
        self.add('editmask', 'em_date1', 384, 4, 411, 100, taborder=10)
        self.add('statictext', 'st_1', 27, 8, 347, 76, text='Date From :')
        self.add('statictext', 'st_5', 1691, 12, 434, 76, text='From Stktype :')
        self.add('statictext', 'st_2', 1138, 16, 128, 76, text='To :')
        self.add('commandbutton', 'cb_remove', 2985, 96, 311, 104, text='Rem.Others', taborder=50)
        self.add('commandbutton', 'cb_sel', 3301, 96, 306, 104, text='Select All', taborder=60)
        self.add('datawindow', 'dw_tostktype', 2130, 100, 539, 88, dataobject='d_stktypecode', taborder=30)
        self.add('datawindow', 'dw_from', 384, 104, 402, 88, dataobject='d_itemcode', taborder=110)
        self.add('datawindow', 'dw_to', 1275, 108, 402, 88, dataobject='d_itemcode', taborder=90)
        self.add('statictext', 'st_3', 5, 116, 370, 76, text='From Code :')
        self.add('statictext', 'st_6', 1755, 116, 370, 76, text='To Stktype :')
        self.add('statictext', 'st_4', 969, 120, 297, 76, text='To Code :')
        self.add('dropdownlistbox', 'ddlb_trantype', 384, 196, 663, 652, text='All', items=['All', 'Stock Transfer Only', 'Item Change Only', 'Add  Less Only', 'Barcode Daywise Comparison'], taborder=70)
        self.add('datawindow', 'dw_smcode', 2130, 196, 677, 88, dataobject='d_smancode', taborder=90)
        self.add('datawindow', 'dw_anycode', 1275, 200, 402, 88, dataobject='d_itemcode', taborder=80)
        self.add('statictext', 'st_9', 1897, 204, 229, 76, text='SMan :')
        self.add('commandbutton', 'cb_delall', 3342, 204, 201, 88, text='Del All', taborder=70)
        self.add('checkbox', 'cbx_speed', 2985, 208, 352, 80, text='Speed Print')
        self.add('statictext', 'st_7', 14, 212, 361, 76, text='Tran. Type :')
        self.add('statictext', 'st_8', 1074, 212, 187, 80, text='Item :')
        self.add('datawindow', 'dw_itemlist', 0, 292, 3611, 1916, dataobject='d_itemadj', taborder=120)
        self.add('dropdownlistbox', 'ddlb_reason', 2130, 300, 448, 560, text='All', items=['All', 'Add/Less', 'Correction', 'Missing'], taborder=111)
        self.add('checkbox', 'cbx_noal', 2985, 316, 425, 68, text='No Add Less')
