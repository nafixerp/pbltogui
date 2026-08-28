"""Model Transfer Report — w_modeltransrep.

Generated from the PowerBuilder window ``w_modeltransrep.srw`` by
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
    name='w_modeltransrep',
    title='Model Transfer Report',
    width=3639,
    height=2224,
    controls=[],
    tables=[],
    source_path='w_modeltransrep.srw',
    report={'dataobject': 'd_modeltransrep', 'sql': 'SELECT modelm.tdate AS modelm_tdate, modelm.pcode AS modelm_pcode, modelm.pname AS modelm_pname, modelm.icode AS modelm_icode, modelm.bcode AS modelm_bcode, modelm.qty AS modelm_qty, modelm.weight AS modelm_weight, modelm.stwgt AS modelm_stwgt, modelm.ir AS modelm_ir, modelm.pend AS modelm_pend, modelm.smcode AS modelm_smcode, modelm.stktype AS modelm_stktype, modelm.note AS modelm_note, modelm.slno AS modelm_slno, (select items.name from items where items.code = modelm.icode) as itemname, 0 as prn FROM modelm ORDER BY modelm.tdate ASC, modelm.slno ASC', 'computes': [{'name': 'compute_4', 'expression': "if(  ir = 'R', 'Return','Issued')", 'format': '[GENERAL]', 'label': 'compute_4', 'band': 'detail'}, {'name': 'compute_6', 'expression': "sum(if(  ir = 'R',0, qty ) for all)", 'format': '[general]', 'label': 'compute_6', 'band': 'summary'}, {'name': 'compute_5', 'expression': "sum(if(  ir = 'R',0, weight ) for all)", 'format': '#########0.000', 'label': 'compute_5', 'band': 'summary'}, {'name': 'compute_9', 'expression': "sum(if(  ir = 'R',0, stwgt ) for all)", 'format': '#########0.000', 'label': 'compute_9', 'band': 'summary'}, {'name': 'compute_3', 'expression': 'count(tdate for all)', 'format': '', 'label': 'compute_3', 'band': 'summary'}, {'name': 'compute_8', 'expression': "sum(if(  ir = 'R', qty,0 ) for all)", 'format': '[general]', 'label': 'compute_8', 'band': 'summary'}, {'name': 'compute_7', 'expression': "sum(if(  ir = 'R', weight,0 ) for all)", 'format': '#########0.000', 'label': 'compute_7', 'band': 'summary'}, {'name': 'compute_10', 'expression': "sum(if(  ir = 'R',  stwgt ,0 ) for all)", 'format': '#########0.000', 'label': 'compute_10', 'band': 'summary'}], 'args': ['rlevel', 'date1', 'date2'], 'arg_types': {'rlevel': 'number', 'date1': 'date', 'date2': 'date'}, 'tables': ['modelm'], 'columns': [{'name': 'itemname', 'label': 'itemname', 'type': 'char'}, {'name': 'prn', 'label': 'prn', 'type': 'long'}, {'name': 'tdate', 'label': 'tdate', 'type': 'date'}, {'name': 'pcode', 'label': 'pcode', 'type': 'char'}, {'name': 'pname', 'label': 'pname', 'type': 'char'}, {'name': 'icode', 'label': 'icode', 'type': 'char'}, {'name': 'bcode', 'label': 'bcode', 'type': 'decimal'}, {'name': 'qty', 'label': 'qty', 'type': 'long'}, {'name': 'weight', 'label': 'weight', 'type': 'decimal'}, {'name': 'stwgt', 'label': 'stwgt', 'type': 'decimal'}, {'name': 'ir', 'label': 'ir', 'type': 'char'}, {'name': 'pend', 'label': 'pend', 'type': 'char'}, {'name': 'smcode', 'label': 'smcode', 'type': 'char'}, {'name': 'stktype', 'label': 'stktype', 'type': 'char'}, {'name': 'note', 'label': 'note', 'type': 'char'}, {'name': 'slno', 'label': 'slno', 'type': 'decimal'}]},
)


class ModelTransferReportForm(GeneratedForm):
    """Model Transfer Report"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date2', 923, 0, 425, 100, taborder=20)
        self.add('dropdownlistbox', 'ddlb_type', 2359, 0, 448, 560, text='All', items=['All', 'Return Only', 'Issued Only'], taborder=51)
        self.add('commandbutton', 'cb_show', 2821, 0, 261, 92, text='&Show', taborder=30)
        self.add('commandbutton', 'cb_print', 3099, 0, 247, 92, text='&Print', taborder=80)
        self.add('commandbutton', 'cb_exit', 3360, 0, 247, 92, text='E&xit', taborder=70)
        self.add('editmask', 'em_date1', 357, 4, 398, 100, taborder=10)
        self.add('datawindow', 'dw_from', 1646, 4, 402, 88, dataobject='d_itemcode', taborder=40)
        self.add('statictext', 'st_4', 2144, 8, 201, 80, text='Type :')
        self.add('statictext', 'st_3', 1417, 12, 219, 76, text='Code :')
        self.add('statictext', 'st_1', 0, 16, 347, 76, text='Date From :')
        self.add('statictext', 'st_2', 805, 16, 128, 76, text='To :')
        self.add('datawindow', 'dw_smcode', 1646, 100, 677, 88, dataobject='d_smancode', taborder=50)
        self.add('statictext', 'st_17', 37, 104, 311, 76, text='Stk Type :')
        self.add('datawindow', 'dw_stktype', 357, 104, 539, 88, dataobject='d_stktypecode', taborder=60)
        self.add('statictext', 'st_9', 1413, 108, 229, 76, text='SMan :')
        self.add('checkbox', 'cbx_pendonly', 2821, 112, 475, 72, text='Pending Only')
        self.add('datawindow', 'dw_itemlist', 0, 192, 3611, 1984, dataobject='d_modeltransrep', taborder=50)
