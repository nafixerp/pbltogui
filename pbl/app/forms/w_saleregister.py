"""Sales Register — w_saleregister.

Generated from the PowerBuilder window ``w_saleregister.srw`` by
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
    name='w_saleregister',
    title='Sales Register',
    width=4215,
    height=2496,
    controls=[],
    tables=['clients'],
    source_path='w_saleregister.srw',
    report={'dataobject': 'd_saleregister', 'sql': 'SELECT salesm.billno AS salesm_billno, salesm.tdate AS salesm_tdate, salesm.billamt AS salesm_billamt, salesm.eamt AS salesm_eamt, salesm.sretamt AS salesm_sretamt, salesm.staxamt AS salesm_staxamt, salesm.discount AS salesm_discount, salesm.ramt AS salesm_ramt, salesm.ramtafter AS salesm_ramtafter, salesm.slno AS salesm_slno, salesd.slno AS salesd_slno, items.name AS items_name, salesd.qty AS salesd_qty, salesd.weight AS salesd_weight, items.itype AS items_itype, salesd.jcode AS salesd_jcode, items.ornament AS items_ornament, salesd.amount AS salesd_amount, salesm.smcode AS salesm_smcode, salesd.name AS salesd_name, items.code AS items_code, salesd.stonewgt AS salesd_stonewgt, salesd.stktype AS salesd_stktype, salesm.round AS salesm_round, salesm.counter AS salesm_counter, salesd.mcharge AS salesd_mcharge, salesd.wastage AS salesd_wastage, salesd.rate AS salesd_rate, salesm.astamt AS salesm_astamt, salesm.ic AS salesm_ic, salesm.custcode AS salesm_custcode, salesd.bcode AS salesd_bcode, salesm.orderno AS salesm_orderno, salesm.custname AS salesm_custname, salesm.mobno AS salesm_mobno, salesm.netamt AS salesm_netamt, items.dmdplt AS items_dmdplt, salesd.stoneprice AS salesd_stoneprice, salesd.model AS salesd_model, salesd.dmdwgt AS salesd_dmdwgt, items.subgrpcode AS items_subgrpcode, salesm.addr AS salesm_addr, items.grpcode AS items_grpcode, salesm.ttime AS salesm_ttime, (select barcode.weight from barcode where barcode.bcode = salesd.bcode) as bcwgt, (select daybookpart.uid from daybookpart where daybookpart.slno = salesm.slno) as suid, (salesm.billtype) as billtype, (select barcode.counter from barcode where barcode.bcode = salesd.bcode) as stkcounter, (select sum(spdmddet.dmdamt) from spdmddet where spdmddet.slno = salesd.slno and spdmddet.sno = salesd.sno) as dmdamt, (select barcode.subgrp from barcode where barcode.bcode = salesd.bcode) as subgrp FROM salesd, salesm, items WHERE salesd.slno = salesm.slno AND salesd.code = items.code AND salesm.tdate between :rdate1 and :rdate2 AND salesm.control <= :rlevel ORDER BY salesm.tdate ASC, salesm.slno ASC', 'computes': [{'name': 'itemname', 'expression': "if(   salesd_name = '' or isnull(   salesd_name ) , items_name,   salesd_name ) ", 'format': '[general]', 'label': 'itemname', 'band': 'detail'}, {'name': 'netwgt', 'expression': ' salesd_weight  -  salesd_stonewgt ', 'format': '#########0.000', 'label': 'netwgt', 'band': 'detail'}, {'name': 'netwgtamt', 'expression': 'netwgt * salesd_rate', 'format': '#########0.00', 'label': 'netwgtamt', 'band': 'detail'}, {'name': 'stamt', 'expression': 'salesd_stoneprice  + if(isnull(dmdamt), 0, dmdamt) ', 'format': '##########0', 'label': 'stamt', 'band': 'detail'}, {'name': 'va', 'expression': ' salesd_mcharge  +  salesd_wastage  *  salesd_rate ', 'format': '####0', 'label': 'va', 'band': 'detail'}, {'name': 'vaperc', 'expression': 'if( (salesd_amount - va ) > 0, ( va * 100 / (salesd_amount - va ) ) ,0)', 'format': '######0.00', 'label': 'vaperc', 'band': 'detail'}, {'name': 'netgamt', 'expression': 'sum(  netwgtamt for all)', 'format': '[General]', 'label': 'netgamt', 'band': 'summary'}, {'name': 'totva', 'expression': 'sum( va  for all)', 'format': '#########0', 'label': 'totva', 'band': 'summary'}, {'name': 'compute_4', 'expression': 'count(salesm_billno for all distinct)', 'format': '[general]', 'label': 'compute_4', 'band': 'summary'}, {'name': 'compute_5', 'expression': 'count(salesm_billno for all )', 'format': '[general]', 'label': 'compute_5', 'band': 'summary'}, {'name': 'compute_16', 'expression': 'sum(salesd_qty for all)', 'format': '###0', 'label': 'compute_16', 'band': 'summary'}, {'name': 'gstwgt', 'expression': 'sum(salesd_stonewgt for all)', 'format': '#########0.000', 'label': 'gstwgt', 'band': 'summary'}, {'name': 'salesamt', 'expression': 'sum( salesd_amount for all )', 'format': '[General]', 'label': 'salesamt', 'band': 'summary'}, {'name': 'compute_11', 'expression': 'sum(  salesm_sretamt  for all distinct  salesm_slno )', 'format': '######0.00', 'label': 'compute_11', 'band': 'summary'}, {'name': 'compute_20', 'expression': 'sum(  salesm_staxamt  for all distinct  salesm_slno )', 'format': '######0.00', 'label': 'compute_20', 'band': 'summary'}, {'name': 'tround', 'expression': 'sum(  salesm_round for all distinct  salesm_slno )', 'format': '###0.00', 'label': 'tround', 'band': 'summary'}, {'name': 'netgwgt', 'expression': 'sum(  netwgt for all)', 'format': '[General]', 'label': 'netgwgt', 'band': 'summary'}, {'name': 'gswgt', 'expression': ' sum(salesd_weight for all ) ', 'format': '[General]', 'label': 'gswgt', 'band': 'summary'}, {'name': 'compute_15', 'expression': 'sum( stamt for all)', 'format': '#########0.00', 'label': 'compute_15', 'band': 'summary'}, {'name': 'compute_12', 'expression': 'sum(  salesm_eamt  for all distinct  salesm_slno )', 'format': '######0.00', 'label': 'compute_12', 'band': 'summary'}, {'name': 'tdisc', 'expression': 'sum(  salesm_discount for all distinct  salesm_slno )', 'format': '###0.00', 'label': 'tdisc', 'band': 'summary'}, {'name': 'compute_9', 'expression': 'sum(  salesm_ramt  for all distinct  salesm_slno )', 'format': '######0.00', 'label': 'compute_9', 'band': 'summary'}, {'name': 'compute_25', 'expression': "sum( if(   items_itype = 'G',  salesd_qty , 0 ) for all )", 'format': '#####0', 'label': 'compute_25', 'band': 'summary'}, {'name': 'compute_21', 'expression': "sum( if(   items_itype = 'G',  salesd_weight , 0 ) for all )", 'format': '######.000', 'label': 'compute_21', 'band': 'summary'}], 'args': ['rdate1', 'rdate2', 'rlevel'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date', 'rlevel': 'number'}, 'tables': ['salesd', 'salesm', 'items'], 'columns': [{'name': 'salesm_billno', 'label': 'salesm_billno', 'type': 'char'}, {'name': 'salesm_tdate', 'label': 'salesm_tdate', 'type': 'date'}, {'name': 'salesm_billamt', 'label': 'salesm_billamt', 'type': 'decimal'}, {'name': 'salesm_eamt', 'label': 'salesm_eamt', 'type': 'decimal'}, {'name': 'salesm_sretamt', 'label': 'salesm_sretamt', 'type': 'decimal'}, {'name': 'salesm_staxamt', 'label': 'salesm_staxamt', 'type': 'decimal'}, {'name': 'salesm_discount', 'label': 'salesm_discount', 'type': 'decimal'}, {'name': 'salesm_ramt', 'label': 'salesm_ramt', 'type': 'decimal'}, {'name': 'salesm_ramtafter', 'label': 'salesm_ramtafter', 'type': 'decimal'}, {'name': 'salesm_slno', 'label': 'salesm_slno', 'type': 'decimal'}, {'name': 'salesd_slno', 'label': 'salesd_slno', 'type': 'decimal'}, {'name': 'items_name', 'label': 'items_name', 'type': 'char'}, {'name': 'salesd_qty', 'label': 'salesd_qty', 'type': 'long'}, {'name': 'salesd_weight', 'label': 'salesd_weight', 'type': 'decimal'}, {'name': 'items_itype', 'label': 'items_itype', 'type': 'char'}, {'name': 'salesd_jcode', 'label': 'salesd_jcode', 'type': 'char'}, {'name': 'items_ornament', 'label': 'items_ornament', 'type': 'char'}, {'name': 'salesd_amount', 'label': 'salesd_amount', 'type': 'decimal'}, {'name': 'salesm_smcode', 'label': 'salesm_smcode', 'type': 'char'}, {'name': 'salesd_name', 'label': 'salesd_name', 'type': 'char'}, {'name': 'items_code', 'label': 'items_code', 'type': 'char'}, {'name': 'salesd_stonewgt', 'label': 'salesd_stonewgt', 'type': 'decimal'}, {'name': 'salesd_stktype', 'label': 'salesd_stktype', 'type': 'char'}, {'name': 'salesm_round', 'label': 'salesm_round', 'type': 'decimal'}, {'name': 'salesm_counter', 'label': 'salesm_counter', 'type': 'char'}, {'name': 'salesd_mcharge', 'label': 'salesd_mcharge', 'type': 'decimal'}, {'name': 'salesd_wastage', 'label': 'salesd_wastage', 'type': 'decimal'}, {'name': 'salesd_rate', 'label': 'salesd_rate', 'type': 'decimal'}, {'name': 'salesm_astamt', 'label': 'salesm_astamt', 'type': 'decimal'}, {'name': 'salesm_ic', 'label': 'salesm_ic', 'type': 'char'}, {'name': 'salesm_custcode', 'label': 'salesm_custcode', 'type': 'char'}, {'name': 'salesd_bcode', 'label': 'salesd_bcode', 'type': 'decimal'}, {'name': 'salesm_orderno', 'label': 'salesm_orderno', 'type': 'char'}, {'name': 'salesm_custname', 'label': 'salesm_custname', 'type': 'char'}, {'name': 'salesm_mobno', 'label': 'salesm_mobno', 'type': 'char'}, {'name': 'salesm_netamt', 'label': 'salesm_netamt', 'type': 'decimal'}, {'name': 'items_dmdplt', 'label': 'items_dmdplt', 'type': 'char'}, {'name': 'salesd_stoneprice', 'label': 'salesd_stoneprice', 'type': 'decimal'}, {'name': 'bcwgt', 'label': 'bcwgt', 'type': 'decimal'}, {'name': 'suid', 'label': 'suid', 'type': 'char'}, {'name': 'salesd_model', 'label': 'salesd_model', 'type': 'char'}, {'name': 'billtype', 'label': 'billtype', 'type': 'char'}, {'name': 'stkcounter', 'label': 'stkcounter', 'type': 'char'}, {'name': 'salesd_dmdwgt', 'label': 'salesd_dmdwgt', 'type': 'decimal'}, {'name': 'dmdamt', 'label': 'dmdamt', 'type': 'decimal'}, {'name': 'subgrp', 'label': 'subgrp', 'type': 'char'}, {'name': 'items_subgrpcode', 'label': 'items_subgrpcode', 'type': 'char'}, {'name': 'salesm_addr', 'label': 'salesm_addr', 'type': 'char'}, {'name': 'items_grpcode', 'label': 'items_grpcode', 'type': 'char'}, {'name': 'salesm_ttime', 'label': 'salesm_ttime', 'type': 'time'}]},
    opens=['w_clientshelp', 'w_itemhelp'],
)


class SalesRegisterForm(GeneratedForm):
    """Sales Register"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 270, 0, 448, 92, taborder=10)
        self.add('editmask', 'em_date2', 832, 0, 448, 92, taborder=20)
        self.add('statictext', 'st_14', 1289, 0, 206, 76, text='Time :')
        self.add('editmask', 'em_time1', 1504, 0, 283, 88, text='none', taborder=110)
        self.add('editmask', 'em_time2', 1792, 0, 283, 88, text='none', taborder=30)
        self.add('commandbutton', 'cb_show', 2423, 0, 229, 92, text='&Show', taborder=30)
        self.add('commandbutton', 'cb_print', 2656, 0, 229, 92, text='&Print', taborder=130)
        self.add('commandbutton', 'cb_sort', 3291, 0, 229, 92, text='So&rt', taborder=100)
        self.add('commandbutton', 'cb_1', 3529, 0, 229, 92, text='Save &As', taborder=120)
        self.add('commandbutton', 'cb_exit', 3767, 0, 229, 92, text='E&xit', taborder=140)
        self.add('statictext', 'st_10', 0, 8, 270, 64, text='From :')
        self.add('statictext', 'st_11', 727, 8, 110, 72, text='To :')
        self.add('checkbox', 'cbx_speed', 2907, 16, 393, 60, text='Speed Print')
        self.add('datawindow', 'dw_smcode', 270, 92, 677, 88, dataobject='d_smancode', taborder=80)
        self.add('dropdownlistbox', 'ddlb_type1', 1504, 92, 549, 988, text='All', items=['All', 'Gold', 'Silver', 'Others', 'Platinum'], taborder=50)
        self.add('datawindow', 'dw_group', 3195, 92, 800, 88, dataobject='d_itemgrpcode', taborder=110)
        self.add('dropdownlistbox', 'ddlb_reptype', 2423, 96, 539, 988, text='Billwise', items=['Billwise', 'Itemwise Details', 'Itemwise Summary', 'Pres.StoneWise', 'SManWise', 'Order Sales Only', 'With Zero Disc', 'Smithwise Report'], taborder=100)
        self.add('statictext', 'st_1', 0, 100, 270, 76, text='SMan :')
        self.add('statictext', 'st_2', 1271, 100, 224, 76, text='Type1 :')
        self.add('statictext', 'st_7', 2098, 100, 325, 76, text='Rep Type :')
        self.add('statictext', 'st_13', 2971, 108, 224, 80, text='Group:')
        self.add('datawindow', 'dw_ic', 270, 184, 695, 88, dataobject='d_incharge_code', taborder=90)
        self.add('dropdownlistbox', 'ddlb_type2', 1504, 184, 549, 796, text='All', items=['Diamond', 'Platinum', 'Gold', 'Silver', 'Others', 'Color Stone', 'Watch', 'All'], taborder=100)
        self.add('datawindow', 'dw_subgrp', 3195, 184, 800, 88, dataobject='d_itemsubgrpcode', taborder=110)
        self.add('checkbox', 'cbx_ic', 969, 188, 78, 76)
        self.add('statictext', 'st_5', 1271, 188, 224, 76, text='Type2 :')
        self.add('datawindow', 'dw_stktype', 2423, 188, 539, 88, dataobject='d_stktypecode', taborder=70)
        self.add('statictext', 'st_20', 0, 192, 270, 80, text='Incharge :')
        self.add('statictext', 'st_17', 2107, 196, 315, 76, text='Stk Type :')
        self.add('statictext', 'st_12', 2971, 196, 224, 80, text='SubGrp:')
        self.add('datawindow', 'dw_counter', 270, 276, 654, 88, dataobject='d_countercode', taborder=110)
        self.add('dropdownlistbox', 'ddlb_type3', 1504, 276, 549, 988, text='All', items=['All', 'Ornaments Only', 'Not Ornaments'], taborder=90)
        self.add('datawindow', 'dw_stoneitem', 2423, 276, 402, 88, dataobject='d_itemstcode', taborder=100)
        self.add('datawindow', 'dw_custcode', 3200, 276, 402, 88, dataobject='d_cust', taborder=40)
        self.add('singlelineedit', 'sle_itemcode', 3744, 276, 251, 88, limit=10, taborder=60)
        self.add('commandbutton', 'cb_4', 4005, 276, 133, 88, text='&Help')
        self.add('statictext', 'st_9', 0, 280, 270, 76, text='Counter :')
        self.add('checkbox', 'cbx_stkcounter', 1015, 280, 274, 80, text='Stk Cntr')
        self.add('statictext', 'st_6', 1294, 280, 201, 76, text='Type3 :')
        self.add('checkbox', 'cbx_counter', 928, 284, 87, 76)
        self.add('statictext', 'st_4', 3026, 284, 165, 80, text='Party :')
        self.add('statictext', 'st_3', 3584, 288, 183, 72, text='Item :')
        self.add('statictext', 'st_8', 2066, 296, 357, 64, text='Stone Type :')
        self.add('datawindow', 'dw_saleregister', 5, 368, 4192, 1944, dataobject='d_saleregister', taborder=110)
