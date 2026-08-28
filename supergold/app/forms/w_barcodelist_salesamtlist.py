"""Barcode SAmt List — w_barcodelist_salesamtlist.

Generated from the PowerBuilder window ``w_barcodelist_salesamtlist.srw`` by
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
    name='w_barcodelist_salesamtlist',
    title='Barcode SAmt List',
    width=3689,
    height=2336,
    controls=[],
    tables=['barcode', 'barcode_dmddet'],
    source_path='w_barcodelist_salesamtlist.srw',
    grid={'control': 'dw_scode', 'dataobject': 'd_supp', 'table': 'codehelp', 'keys': ['code'], 'computes': [], 'columns': [{'name': 'code', 'label': 'code', 'type': 'char'}]},
    report={'dataobject': 'd_barcodelist_salesamt', 'sql': "SELECT items.name AS items_name, barcode.bcode AS barcode_bcode, barcode.icode AS barcode_icode, barcode.qty AS barcode_qty, barcode.weight AS barcode_weight, barcode.stweight AS barcode_stweight, barcode.stprice AS barcode_stprice, barcode.wastage AS barcode_wastage, barcode.mc AS barcode_mc, barcode.tdate AS barcode_tdate, barcode.smcode AS barcode_smcode, barcode.part AS barcode_part, barcode.mcrate AS barcode_mcrate, barcode.stk AS barcode_stk, barcode.qtype AS barcode_qtype, barcode.qunit AS barcode_qunit, barcode.vap AS barcode_vap, barcode.docno AS barcode_docno, barcode.tamt AS barcode_tamt, items.itype AS items_itype, barcode.costamt AS barcode_costamt, barcode.rate AS barcode_rate, items.stkinnos AS items_stkinnos, items.grpcode AS items_grpcode, items.dmdplt AS items_dmdplt, barcode.subgrp AS barcode_subgrp, barcode.huid AS barcode_huid, 0 as prn, (select barcodedmd.dmdwgt from barcodedmd where barcodedmd.bcode = barcode.bcode) as dmdwgt, (select barcodedmd.dmdamt from barcodedmd where barcodedmd.bcode = barcode.bcode) as dmdamt, (select barcodedmd.dmdnos from barcodedmd where barcodedmd.bcode = barcode.bcode) as dmdnos, (select barcodedmd.dmdunit from barcodedmd where barcodedmd.bcode = barcode.bcode) as dmdunit, (select max(barcodedoc.smith) from barcodedoc where barcodedoc.docno = barcode.docno) as smith, (select max(purchasem.suppcode) from purchasem where purchasem.docno = barcode.docno) as scode, ('') as bcph, (select max(salesd.weight) from salesd where salesd.bcode = barcode.bcode) as soldwgt FROM items, barcode WHERE items.code = barcode.icode AND barcode.tdate >= :rdate1 AND barcode.control <= :rlevel AND barcode.tdate <= :rdate2 ORDER BY barcode.bcode ASC", 'computes': [{'name': 'wgtdiff', 'expression': 'if( soldwgt > 0 ,  soldwgt - barcode_weight , 0)', 'format': '#######0.000', 'label': 'wgtdiff', 'band': 'detail'}, {'name': 'saleamt', 'expression': "if( barcode_tamt> 0 , barcode_tamt, if( items_stkinnos = 'Y',  barcode_rate ,( barcode_weight  -  barcode_stweight ) *  barcode_rate ))", 'format': '########0.00', 'label': 'saleamt', 'band': 'detail'}, {'name': 'diff', 'expression': 'saleamt - barcode_costamt', 'format': '#########0.00', 'label': 'diff', 'band': 'detail'}, {'name': 'compute_9', 'expression': 'count(barcode_bcode for all)', 'format': '[general]', 'label': 'compute_9', 'band': 'summary'}, {'name': 'compute_8', 'expression': 'sum(barcode_weight for all)', 'format': '#######0.000', 'label': 'compute_8', 'band': 'summary'}, {'name': 'compute_13', 'expression': 'sum( wgtdiff for all)', 'format': '#######0.000', 'label': 'compute_13', 'band': 'summary'}, {'name': 'compute_6', 'expression': 'sum(barcode_stprice for all)', 'format': '#####0.00', 'label': 'compute_6', 'band': 'summary'}, {'name': 'compute_5', 'expression': 'sum(barcode_costamt for all)', 'format': '########0.00', 'label': 'compute_5', 'band': 'summary'}, {'name': 'compute_10', 'expression': 'sum(saleamt for all)', 'format': '########0.00', 'label': 'compute_10', 'band': 'summary'}, {'name': 'compute_12', 'expression': 'sum( soldwgt for all)', 'format': '#######0.000', 'label': 'compute_12', 'band': 'summary'}, {'name': 'compute_7', 'expression': 'sum(barcode_stweight for all)', 'format': '#####0.000', 'label': 'compute_7', 'band': 'summary'}, {'name': 'compute_11', 'expression': 'sum(barcode_mc for all)', 'format': '########0.00', 'label': 'compute_11', 'band': 'summary'}, {'name': 'compute_4', 'expression': 'sum(saleamt for all)', 'format': '########0.00', 'label': 'compute_4', 'band': 'summary'}], 'args': ['rdate1', 'rdate2', 'rlevel'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date', 'rlevel': 'number'}, 'tables': ['items', 'barcode'], 'columns': [{'name': 'items_name', 'label': 'items_name', 'type': 'char'}, {'name': 'barcode_bcode', 'label': 'barcode_bcode', 'type': 'decimal'}, {'name': 'barcode_icode', 'label': 'barcode_icode', 'type': 'char'}, {'name': 'barcode_qty', 'label': 'barcode_qty', 'type': 'long'}, {'name': 'barcode_weight', 'label': 'barcode_weight', 'type': 'decimal'}, {'name': 'barcode_stweight', 'label': 'barcode_stweight', 'type': 'decimal'}, {'name': 'barcode_stprice', 'label': 'barcode_stprice', 'type': 'decimal'}, {'name': 'barcode_wastage', 'label': 'barcode_wastage', 'type': 'decimal'}, {'name': 'barcode_mc', 'label': 'barcode_mc', 'type': 'decimal'}, {'name': 'barcode_tdate', 'label': 'barcode_tdate', 'type': 'date'}, {'name': 'barcode_smcode', 'label': 'barcode_smcode', 'type': 'char'}, {'name': 'barcode_part', 'label': 'barcode_part', 'type': 'char'}, {'name': 'barcode_mcrate', 'label': 'barcode_mcrate', 'type': 'decimal'}, {'name': 'barcode_stk', 'label': 'barcode_stk', 'type': 'char'}, {'name': 'items_prn', 'label': 'items_prn', 'type': 'long'}, {'name': 'cdmdwgt', 'label': 'cdmdwgt', 'type': 'decimal'}, {'name': 'cdmdamt', 'label': 'cdmdamt', 'type': 'decimal'}, {'name': 'cdmdnos', 'label': 'cdmdnos', 'type': 'long'}, {'name': 'cdmdunit', 'label': 'cdmdunit', 'type': 'char'}, {'name': 'barcode_qtype', 'label': 'barcode_qtype', 'type': 'char'}, {'name': 'barcode_qunit', 'label': 'barcode_qunit', 'type': 'char'}, {'name': 'barcode_vap', 'label': 'barcode_vap', 'type': 'decimal'}, {'name': 'barcode_docno', 'label': 'barcode_docno', 'type': 'char'}, {'name': 'smith', 'label': 'smith', 'type': 'char'}, {'name': 'barcode_tamt', 'label': 'barcode_tamt', 'type': 'decimal'}, {'name': 'scode', 'label': 'scode', 'type': 'char'}, {'name': 'bcph', 'label': 'bcph', 'type': 'char'}, {'name': 'items_itype', 'label': 'items_itype', 'type': 'char'}, {'name': 'barcode_costamt', 'label': 'barcode_costamt', 'type': 'decimal'}, {'name': 'barcode_rate', 'label': 'barcode_rate', 'type': 'decimal'}, {'name': 'items_stkinnos', 'label': 'items_stkinnos', 'type': 'char'}, {'name': 'items_grpcode', 'label': 'items_grpcode', 'type': 'char'}, {'name': 'items_dmdplt', 'label': 'items_dmdplt', 'type': 'char'}, {'name': 'barcode_subgrp', 'label': 'barcode_subgrp', 'type': 'char'}, {'name': 'soldwgt', 'label': 'soldwgt', 'type': 'decimal'}, {'name': 'barcode_huid', 'label': 'barcode_huid', 'type': 'char'}]},
    opens=['w_clientshelp', 'w_barcode_dochelp', 'w_itemhelp'],
)


class BarcodeSamtListForm(GeneratedForm):
    """Barcode SAmt List"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 219, 0, 434, 92, taborder=10)
        self.add('editmask', 'em_date2', 891, 0, 434, 92, taborder=20)
        self.add('singlelineedit', 'sle_docno', 1687, 0, 379, 92, limit=10, taborder=40)
        self.add('commandbutton', 'cb_dochlp', 2071, 0, 160, 92, text='&Help')
        self.add('commandbutton', 'cb_show', 2258, 0, 315, 92, text='&Show', taborder=60)
        self.add('commandbutton', 'cb_sort', 2606, 0, 247, 92, text='So&rt', taborder=80)
        self.add('commandbutton', 'cb_1', 2885, 0, 270, 92, text='Save &As', taborder=190)
        self.add('commandbutton', 'cb_bcodeprint', 3159, 0, 233, 92, text='&Print', taborder=180)
        self.add('commandbutton', 'cb_exit', 3397, 0, 233, 92, text='E&xit', taborder=170)
        self.add('statictext', 'st_2', 1371, 4, 306, 64, text='Doc.No. :')
        self.add('statictext', 'st_11', 750, 8, 137, 72, text='To :')
        self.add('statictext', 'st_10', 0, 12, 206, 60, text='From :')
        self.add('dropdownlistbox', 'ddlb_type', 891, 96, 571, 392, text='Not in Stock', items=['Stock Only', 'Not in Stock', 'All'], taborder=100)
        self.add('singlelineedit', 'sle_itemcode', 219, 100, 425, 92, limit=10, taborder=70)
        self.add('commandbutton', 'cb_itemhlp', 649, 100, 187, 92, text='&Help')
        self.add('singlelineedit', 'sle_bcno', 1687, 100, 379, 92, limit=10, taborder=30)
        self.add('commandbutton', 'cb_2', 2071, 100, 160, 92, text='Search')
        self.add('commandbutton', 'cb_sel', 2606, 100, 549, 92, text='Select All', taborder=150)
        self.add('commandbutton', 'cb_print', 3159, 100, 471, 92, text='Barcode Print', taborder=160)
        self.add('statictext', 'st_1', 0, 108, 206, 76, text='Item :')
        self.add('statictext', 'st_3', 1467, 120, 210, 64, text='BCNo. :')
        self.add('editmask', 'em_marg', 219, 192, 242, 84, text='none', taborder=140)
        self.add('datawindow', 'dw_scode', 2606, 192, 425, 84, dataobject='d_supp', taborder=50)
        self.add('editmask', 'em_cpfrom', 1687, 196, 265, 84, text='none', taborder=120)
        self.add('editmask', 'em_cpto', 2117, 196, 265, 84, text='none', taborder=130)
        self.add('commandbutton', 'cb_setsamt', 3154, 196, 471, 80, text='Rearange SAmt', taborder=110)
        self.add('statictext', 'st_5', 0, 200, 210, 64, text='Marg % :')
        self.add('checkbox', 'cbx_allstamtzero', 530, 204, 475, 72, text='All St.Amt to Zero')
        self.add('checkbox', 'cbx_allmczero', 1038, 204, 407, 72, text='All Mc to Zero')
        self.add('statictext', 'st_4', 2391, 204, 210, 64, text='Supplier:')
        self.add('statictext', 'st_6', 1454, 212, 224, 56, text='CP From :')
        self.add('statictext', 'st_7', 1952, 212, 165, 56, text='CP To :')
        self.add('datawindow', 'dw_saleregister', 0, 280, 3625, 1840, dataobject='d_barcodelist_salesamt', taborder=90)
        self.add('datawindow', 'dw_grp', 2606, 284, 800, 88, dataobject='d_itemgrpcode', taborder=40)
        self.add('statictext', 'st_8', 2391, 292, 210, 68, text='Group :')
