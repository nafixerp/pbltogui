"""Barcode Stock List — w_barcode_stocklist.

Generated from the PowerBuilder window ``w_barcode_stocklist.srw`` by
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
    name='w_barcode_stocklist',
    title='Barcode Stock List',
    width=3680,
    height=2220,
    controls=[],
    tables=['barcode', 'itemgrp', 'itemsubgrp'],
    source_path='w_barcode_stocklist.srw',
    report={'dataobject': 'd_barcode_stocklist', 'sql': 'SELECT items.name AS items_name, barcode.bcode AS barcode_bcode, barcode.icode AS barcode_icode, barcode.qty AS barcode_qty, barcode.weight AS barcode_weight, barcode.stweight AS barcode_stweight, barcode.stprice AS barcode_stprice, barcode.wastage AS barcode_wastage, barcode.mc AS barcode_mc, barcode.tdate AS barcode_tdate, barcode.smcode AS barcode_smcode, barcode.part AS barcode_part, barcode.mcrate AS barcode_mcrate, barcode.stk AS barcode_stk, barcode.qtype AS barcode_qtype, barcode.qunit AS barcode_qunit, barcode.vap AS barcode_vap, barcode.sdate AS barcode_sdate, barcode.weight2 AS barcode_weight2, barcode.counter AS barcode_counter, barcode.serialno AS barcode_serialno, items.grpcode AS items_grpcode, items.itype AS items_itype, items.dmdplt AS items_dmdplt, barcode.subgrp AS barcode_subgrp, barcode.stktouch AS barcode_stktouch, barcode.sizemodel AS barcode_sizemodel, barcode.model AS barcode_model, barcode.status AS barcode_status, barcode.huid AS barcode_huid, 0 as prn, (select barcodedmd.dmdwgt from barcodedmd where barcodedmd.bcode = barcode.bcode) as dmdwgt, (select barcodedmd.dmdamt from barcodedmd where barcodedmd.bcode = barcode.bcode) as dmdamt, (select barcodedmd.dmdnos from barcodedmd where barcodedmd.bcode = barcode.bcode) as dmdnos, (select barcodedmd.dmdunit from barcodedmd where barcodedmd.bcode = barcode.bcode) as dmdunit, (select max(salesd.weight) from salesd where salesd.bcode = barcode.bcode) as soldwgt FROM items, barcode WHERE items.code = barcode.icode AND barcode.control <= :rlevel ORDER BY barcode.bcode ASC', 'computes': [{'name': 'netwgt', 'expression': ' barcode_weight  -  barcode_stweight ', 'format': '######0.000', 'label': 'netwgt', 'band': 'detail'}, {'name': 'stickerwgt', 'expression': 'if(barcode_weight2   > 0, barcode_weight2  - barcode_weight ,0)', 'format': '##0.000', 'label': 'stickerwgt', 'band': 'detail'}, {'name': 'wgtdiff', 'expression': 'if( soldwgt > 0 , soldwgt -  barcode_weight , 0)', 'format': '######0.000', 'label': 'wgtdiff', 'band': 'detail'}, {'name': 'compute_2', 'expression': 'count(barcode_bcode for all)', 'format': '[general]', 'label': 'compute_2', 'band': 'summary'}, {'name': 'compute_3', 'expression': 'sum(barcode_qty for all)', 'format': '######', 'label': 'compute_3', 'band': 'summary'}, {'name': 'compute_6', 'expression': 'sum(barcode_stweight for all)', 'format': '#####0.000', 'label': 'compute_6', 'band': 'summary'}, {'name': 'compute_5', 'expression': 'sum(barcode_stprice for all)', 'format': '#####0.00', 'label': 'compute_5', 'band': 'summary'}, {'name': 'compute_8', 'expression': ' sum(  cdmdamt for all) ', 'format': '[general]', 'label': 'compute_8', 'band': 'summary'}, {'name': 'totsticker', 'expression': 'sum( stickerwgt for all)', 'format': '##0.000', 'label': 'totsticker', 'band': 'summary'}, {'name': 'compute_11', 'expression': 'sum(barcode_weight2 for all)', 'format': '#######0.000', 'label': 'compute_11', 'band': 'summary'}, {'name': 'compute_12', 'expression': 'sum( soldwgt for all)', 'format': '#######0.000', 'label': 'compute_12', 'band': 'summary'}, {'name': 'compute_13', 'expression': 'sum( wgtdiff for all)', 'format': '####0.000', 'label': 'compute_13', 'band': 'summary'}, {'name': 'compute_9', 'expression': 'sum(netwgt for all)', 'format': '#######0.000', 'label': 'compute_9', 'band': 'summary'}, {'name': 'totwgt', 'expression': 'sum(barcode_weight for all)', 'format': '#######0.000', 'label': 'totwgt', 'band': 'summary'}, {'name': 'compute_4', 'expression': ' sum(  cdmdwgt for all) ', 'format': '[general]', 'label': 'compute_4', 'band': 'summary'}, {'name': 'compute_7', 'expression': 'totwgt + totsticker', 'format': '########0.000', 'label': 'compute_7', 'band': 'summary'}, {'name': 'compute_10', 'expression': 'avg( stickerwgt for all )', 'format': '##0.000', 'label': 'compute_10', 'band': 'summary'}], 'args': ['rlevel'], 'arg_types': {'rlevel': 'number'}, 'tables': ['items', 'barcode'], 'columns': [{'name': 'items_name', 'label': 'items_name', 'type': 'char'}, {'name': 'barcode_bcode', 'label': 'barcode_bcode', 'type': 'decimal'}, {'name': 'barcode_icode', 'label': 'barcode_icode', 'type': 'char'}, {'name': 'barcode_qty', 'label': 'barcode_qty', 'type': 'long'}, {'name': 'barcode_weight', 'label': 'barcode_weight', 'type': 'decimal'}, {'name': 'barcode_stweight', 'label': 'barcode_stweight', 'type': 'decimal'}, {'name': 'barcode_stprice', 'label': 'barcode_stprice', 'type': 'decimal'}, {'name': 'barcode_wastage', 'label': 'barcode_wastage', 'type': 'decimal'}, {'name': 'barcode_mc', 'label': 'barcode_mc', 'type': 'decimal'}, {'name': 'barcode_tdate', 'label': 'barcode_tdate', 'type': 'date'}, {'name': 'barcode_smcode', 'label': 'barcode_smcode', 'type': 'char'}, {'name': 'barcode_part', 'label': 'barcode_part', 'type': 'char'}, {'name': 'barcode_mcrate', 'label': 'barcode_mcrate', 'type': 'decimal'}, {'name': 'barcode_stk', 'label': 'barcode_stk', 'type': 'char'}, {'name': 'items_prn', 'label': 'items_prn', 'type': 'long'}, {'name': 'cdmdwgt', 'label': 'cdmdwgt', 'type': 'decimal'}, {'name': 'cdmdamt', 'label': 'cdmdamt', 'type': 'decimal'}, {'name': 'cdmdnos', 'label': 'cdmdnos', 'type': 'long'}, {'name': 'cdmdunit', 'label': 'cdmdunit', 'type': 'char'}, {'name': 'barcode_qtype', 'label': 'barcode_qtype', 'type': 'char'}, {'name': 'barcode_qunit', 'label': 'barcode_qunit', 'type': 'char'}, {'name': 'barcode_vap', 'label': 'barcode_vap', 'type': 'decimal'}, {'name': 'barcode_sdate', 'label': 'barcode_sdate', 'type': 'date'}, {'name': 'barcode_weight2', 'label': 'barcode_weight2', 'type': 'decimal'}, {'name': 'barcode_counter', 'label': 'barcode_counter', 'type': 'char'}, {'name': 'barcode_serialno', 'label': 'barcode_serialno', 'type': 'char'}, {'name': 'items_grpcode', 'label': 'items_grpcode', 'type': 'char'}, {'name': 'items_itype', 'label': 'items_itype', 'type': 'char'}, {'name': 'items_dmdplt', 'label': 'items_dmdplt', 'type': 'char'}, {'name': 'barcode_subgrp', 'label': 'barcode_subgrp', 'type': 'char'}, {'name': 'barcode_stktouch', 'label': 'barcode_stktouch', 'type': 'decimal'}, {'name': 'barcode_sizemodel', 'label': 'barcode_sizemodel', 'type': 'char'}, {'name': 'barcode_model', 'label': 'barcode_model', 'type': 'char'}, {'name': 'soldwgt', 'label': 'soldwgt', 'type': 'decimal'}, {'name': 'barcode_status', 'label': 'barcode_status', 'type': 'char'}, {'name': 'barcode_huid', 'label': 'barcode_huid', 'type': 'char'}]},
    opens=['w_costrate_change', 'w_itemhelp', 'w_barcode_history'],
)


class BarcodeStockListForm(GeneratedForm):
    """Barcode Stock List"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('commandbutton', 'cb_4', 814, 0, 187, 92, text='&Help')
        self.add('commandbutton', 'cb_show', 2290, 0, 261, 88, text='&Show', taborder=80)
        self.add('commandbutton', 'cb_sort', 2574, 0, 261, 88, text='So&rt', taborder=170)
        self.add('commandbutton', 'cb_1', 2843, 0, 261, 88, text='Save &As', taborder=220)
        self.add('commandbutton', 'cb_bcodeprint', 3113, 0, 261, 88, text='&Print', taborder=210)
        self.add('commandbutton', 'cb_exit', 3383, 0, 261, 88, text='E&xit', taborder=200)
        self.add('singlelineedit', 'sle_itemcode', 375, 4, 425, 92, limit=10, taborder=120)
        self.add('editmask', 'em_date', 1253, 4, 425, 92, taborder=40)
        self.add('statictext', 'st_9', 1029, 8, 210, 72, text='As on :')
        self.add('statictext', 'st_1', 114, 12, 247, 76, text='Item :')
        self.add('editmask', 'em_wgt2', 3104, 92, 315, 96, taborder=90)
        self.add('editmask', 'em_wgt1', 2569, 96, 315, 96, taborder=50)
        self.add('editmask', 'em_date1', 375, 100, 425, 92, taborder=20)
        self.add('editmask', 'em_date2', 1253, 100, 425, 92, taborder=30)
        self.add('commandbutton', 'cb_2', 1682, 104, 165, 88, text='Today', taborder=60)
        self.add('statictext', 'st_3', 2976, 104, 119, 80, text='To :')
        self.add('statictext', 'st_10', 0, 108, 361, 64, text='Sold From :')
        self.add('statictext', 'st_11', 1079, 108, 169, 72, text='To :')
        self.add('statictext', 'st_2', 2007, 112, 553, 80, text='Weight Range From :')
        self.add('datawindow', 'dw_grp', 375, 196, 800, 88, dataobject='d_itemgrpcode', taborder=160)
        self.add('dropdownlistbox', 'ddlb_reptype', 1253, 196, 841, 996, text='Detailed Report', items=['Detailed Report', 'Item Summary', 'Item Summary with Subgroup', 'Summary with Stktouch', 'Stktouch Summary', 'With 3 Column', 'Subgroup Summary', 'Group Summary', 'Stock Ledger Comparison', 'Stock Value Summary', 'Stock Value Details'], taborder=10)
        self.add('datawindow', 'dw_counter', 2569, 196, 654, 88, dataobject='d_countercode', taborder=70)
        self.add('commandbutton', 'cb_filter', 3383, 196, 261, 88, text='Filter', taborder=100)
        self.add('checkbox', 'cbx_counter', 3232, 200, 82, 80)
        self.add('statictext', 'st_5', 5, 204, 357, 68, text='Item Group :')
        self.add('statictext', 'st_4', 2290, 204, 270, 72, text='Counter :')
        self.add('datawindow', 'dw_subgrp', 375, 288, 800, 88, dataobject='d_itemsubgrpcode', taborder=110)
        self.add('dropdownlistbox', 'ddlb_itemtype', 1696, 288, 398, 528, text='All', items=['Diamond', 'Platinum', 'Gold', 'Silver', 'Others', 'Color Stone', 'Watch', 'All'], taborder=150)
        self.add('singlelineedit', 'sle_size', 2574, 288, 315, 92, taborder=140)
        self.add('singlelineedit', 'sle_model', 3104, 288, 315, 92, taborder=130)
        self.add('statictext', 'st_6', 5, 292, 357, 72, text='BSubGrp :')
        self.add('dropdownlistbox', 'ddlb_type', 1253, 292, 439, 568, text='Stock Only', items=['Stock Only', 'Not in Stock', 'Transfer Pending', 'All'], taborder=190)
        self.add('statictext', 'st_7', 2290, 296, 270, 72, text='Size :')
        self.add('checkbox', 'cbx_subgrp', 1175, 300, 69, 72)
        self.add('statictext', 'st_8', 2885, 304, 210, 64, text='Model :')
        self.add('datawindow', 'dw_saleregister', 0, 384, 3643, 1740, dataobject='d_barcode_stocklist', taborder=180)
        self.add('commandbutton', 'cb_costupdt', 2514, 396, 951, 80, text='Update Cost for all items w/o cost')
