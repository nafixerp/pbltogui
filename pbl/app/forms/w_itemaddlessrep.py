"""Item Add Less Report — w_itemaddlessrep.

Generated from the PowerBuilder window ``w_itemaddlessrep.srw`` by
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
    name='w_itemaddlessrep',
    title='Item Add Less Report',
    width=3639,
    height=2224,
    controls=[],
    tables=[],
    source_path='w_itemaddlessrep.srw',
    report={'dataobject': 'd_itemaddlessrep', 'sql': 'SELECT itemadj.fromcode AS itemadj_fromcode, itemadj.fromqty AS itemadj_fromqty, itemadj.fromwgt AS itemadj_fromwgt, itemadj.tocode AS itemadj_tocode, itemadj.toqty AS itemadj_toqty, itemadj.towgt AS itemadj_towgt, itemadj.particular AS itemadj_particular, itemadj.tdate AS itemadj_tdate, itemadj.ttime AS itemadj_ttime, itemadj.smcode AS itemadj_smcode, itemadj.slno AS itemadj_slno, itemadj.al AS itemadj_al, itemadj.fromstwgt AS itemadj_fromstwgt, itemadj.tostwgt AS itemadj_tostwgt, itemadj.fromstktype AS itemadj_fromstktype, itemadj.tostktype AS itemadj_tostktype, (select name from items where items.code = fromcode) as fromname, (select name from items where items.code = tocode) as toname, 0 as prn FROM itemadj WHERE itemadj.control <= :rlevel AND itemadj.tdate between :date1 and :date2 ORDER BY itemadj.tdate ASC', 'computes': [{'name': 'itemname', 'expression': 'if( fromqty >0 or  fromwgt >0 , fromname , toname )', 'format': '[general]', 'label': 'itemname', 'band': 'detail'}, {'name': 'addqty', 'expression': 'if( toqty > 0 or  towgt > 0 , toqty, 0)', 'format': '[general]', 'label': 'addqty', 'band': 'detail'}, {'name': 'addwgt', 'expression': 'if( toqty > 0 or  towgt > 0 , towgt, 0)', 'format': '######0.000', 'label': 'addwgt', 'band': 'detail'}, {'name': 'addstwgt', 'expression': 'if( toqty > 0 or  towgt > 0  or tostwgt > 0, tostwgt, 0)', 'format': '######0.000', 'label': 'addstwgt', 'band': 'detail'}, {'name': 'lessqty', 'expression': 'if( fromqty >0 or  fromwgt >0 ,fromqty, 0 )', 'format': '', 'label': 'lessqty', 'band': 'detail'}, {'name': 'lesswgt', 'expression': 'if( fromqty >0 or fromwgt >0 , fromwgt, 0 )', 'format': '######0.000', 'label': 'lesswgt', 'band': 'detail'}, {'name': 'lessstwgt', 'expression': 'if( fromqty >0 or fromwgt >0 or fromstwgt > 0, fromstwgt, 0 )', 'format': '######0.000', 'label': 'lessstwgt', 'band': 'detail'}, {'name': '', 'expression': 'sum( addqty for all)', 'format': '[general]', 'label': '', 'band': 'summary'}, {'name': '', 'expression': 'sum( addwgt for all)', 'format': '######0.000', 'label': '', 'band': 'summary'}, {'name': '', 'expression': 'sum( addstwgt for all)', 'format': '######0.000', 'label': '', 'band': 'summary'}, {'name': '', 'expression': 'sum( lessqty for all)', 'format': '', 'label': '', 'band': 'summary'}, {'name': '', 'expression': 'sum( lesswgt for all)', 'format': '######0.000', 'label': '', 'band': 'summary'}, {'name': '', 'expression': 'sum( lessstwgt for all)', 'format': '######0.000', 'label': '', 'band': 'summary'}, {'name': '', 'expression': 'count(tdate for all)', 'format': '', 'label': '', 'band': 'summary'}], 'args': ['rlevel', 'date1', 'date2'], 'arg_types': {'rlevel': 'number', 'date1': 'date', 'date2': 'date'}, 'tables': ['itemadj'], 'columns': [{'name': 'fromcode', 'label': 'fromcode', 'type': 'char'}, {'name': 'fromqty', 'label': 'fromqty', 'type': 'long'}, {'name': 'fromwgt', 'label': 'fromwgt', 'type': 'decimal'}, {'name': 'tocode', 'label': 'tocode', 'type': 'char'}, {'name': 'toqty', 'label': 'toqty', 'type': 'long'}, {'name': 'towgt', 'label': 'towgt', 'type': 'decimal'}, {'name': 'particular', 'label': 'particular', 'type': 'char'}, {'name': 'tdate', 'label': 'tdate', 'type': 'date'}, {'name': 'fromname', 'label': 'fromname', 'type': 'char'}, {'name': 'toname', 'label': 'toname', 'type': 'char'}, {'name': 'ttime', 'label': 'ttime', 'type': 'time'}, {'name': 'smcode', 'label': 'smcode', 'type': 'char'}, {'name': 'prn', 'label': 'prn', 'type': 'long'}, {'name': 'slno', 'label': 'slno', 'type': 'decimal'}, {'name': 'al', 'label': 'al', 'type': 'char'}, {'name': 'fromstwgt', 'label': 'fromstwgt', 'type': 'decimal'}, {'name': 'tostwgt', 'label': 'tostwgt', 'type': 'decimal'}, {'name': 'fromstktype', 'label': 'fromstktype', 'type': 'char'}, {'name': 'tostktype', 'label': 'tostktype', 'type': 'char'}]},
)


class ItemAddLessReportForm(GeneratedForm):
    """Item Add Less Report"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date2', 923, 0, 425, 100, taborder=20)
        self.add('commandbutton', 'cb_show', 2437, 0, 261, 100, text='&Show', taborder=30)
        self.add('commandbutton', 'cb_print', 3099, 0, 247, 92, text='&Print', taborder=100)
        self.add('commandbutton', 'cb_exit', 3360, 0, 247, 92, text='E&xit', taborder=90)
        self.add('editmask', 'em_date1', 357, 4, 398, 100, taborder=10)
        self.add('datawindow', 'dw_from', 1646, 4, 402, 88, dataobject='d_itemcode', taborder=40)
        self.add('statictext', 'st_3', 1417, 12, 219, 76, text='Code :')
        self.add('statictext', 'st_1', 0, 16, 347, 76, text='Date From :')
        self.add('statictext', 'st_2', 805, 16, 128, 76, text='To :')
        self.add('dropdownlistbox', 'ddlb_reason', 1646, 96, 448, 560, text='All', items=['All', 'Add/Less', 'Correction', 'Missing'], taborder=60)
        self.add('statictext', 'st_17', 37, 104, 311, 76, text='Stk Type :')
        self.add('datawindow', 'dw_stktype', 357, 104, 539, 88, dataobject='d_stktypecode', taborder=70)
        self.add('statictext', 'st_4', 1294, 104, 343, 80, text='Reason :')
        self.add('datawindow', 'dw_smcode', 2432, 104, 677, 88, dataobject='d_smancode', taborder=80)
        self.add('statictext', 'st_9', 2199, 112, 229, 76, text='SMan :')
        self.add('datawindow', 'dw_itemlist', 0, 192, 3611, 1984, dataobject='d_itemaddlessrep', taborder=50)
