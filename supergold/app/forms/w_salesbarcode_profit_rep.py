"""Barcode Profit Report — w_salesbarcode_profit_rep.

Generated from the PowerBuilder window ``w_salesbarcode_profit_rep.srw`` by
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
    name='w_salesbarcode_profit_rep',
    title='Barcode Profit Report',
    width=3698,
    height=2416,
    controls=[],
    tables=[],
    source_path='w_salesbarcode_profit_rep.srw',
    report={'dataobject': 'd_salesbarcode_profit_rep', 'sql': 'SELECT salesm.slno AS salesm_slno, salesm.tdate AS salesm_tdate, salesm.billno AS salesm_billno, salesm.custname AS salesm_custname, salesm.billamt AS salesm_billamt, salesm.status AS salesm_status, salesm.discount AS salesm_discount, salesm.ramt AS salesm_ramt, salesm.eamt AS salesm_eamt, salesm.staxamt AS salesm_staxamt, salesm.duedate AS salesm_duedate, salesm.sretamt AS salesm_sretamt, salesm.ramtafter AS salesm_ramtafter, salesm.round AS salesm_round, salesd.code AS salesd_code, salesd.qty AS salesd_qty, salesd.weight AS salesd_weight, salesd.dmdwgt AS salesd_dmdwgt, salesd.dmdunit AS salesd_dmdunit, salesd.dmdamt AS salesd_dmdamt, salesd.bcode AS salesd_bcode, salesd.amount AS salesd_amount, salesd.stonewgt AS salesd_stonewgt, salesd.stoneprice AS salesd_stoneprice, salesd.mcharge AS salesd_mcharge, salesd.wastage AS salesd_wastage, items.name AS items_name, items.grpcode AS items_grpcode, items.subgrpcode AS items_subgrpcode, (select barcode.cost from barcode where barcode.bcode = salesd.bcode) as cost, (select barcode.costperc from barcode where barcode.bcode = salesd.bcode) as costperc, (select barcode.costamt from barcode where barcode.bcode = salesd.bcode) as bccostamt, (select barcode.coststone from barcode where barcode.bcode = salesd.bcode) as stcostamt, (select sum(spdmddet.dmdamt) from spdmddet where spdmddet.slno = salesd.slno and spdmddet.sno = salesd.sno) as dmdamt, (select sum(barcode_dmddet.pamt) from barcode_dmddet where barcode_dmddet.bcode = salesd.bcode) as dmdcostamt FROM salesm, salesd, items WHERE salesm.slno = salesd.slno AND salesd.code = items.code AND salesm.control <= :rlevel ORDER BY salesm.tdate ASC, salesm.slno ASC', 'computes': [{'name': 'costamt', 'expression': 'if(bccostamt > 0, bccostamt, round( if(cost > 0,  (salesd_weight -  salesd_stonewgt ) *  cost ,  salesd_amount * costperc / 100) , 0))', 'format': '######0.00', 'label': 'costamt', 'band': 'detail'}, {'name': 'profit', 'expression': 'if(costamt > 0, salesd_amount - costamt, 0)', 'format': '#######0.00', 'label': 'profit', 'band': 'detail'}, {'name': 'stamt', 'expression': ' salesd_stoneprice  + if(isnull( dmdamt ),0,dmdamt)', 'format': '########0.00', 'label': 'stamt', 'band': 'detail'}, {'name': 'stcost', 'expression': 'if(isnull( stcostamt ),0,stcostamt) + if(isnull(dmdcostamt),0, dmdcostamt)', 'format': '########0.00', 'label': 'stcost', 'band': 'detail'}, {'name': 'stprofit', 'expression': 'stamt - stcost', 'format': '#######0.00', 'label': 'stprofit', 'band': 'detail'}, {'name': 'compute_8', 'expression': 'sum(salesd_qty for all)', 'format': '[general]', 'label': 'compute_8', 'band': 'summary'}, {'name': 'compute_9', 'expression': 'sum(salesd_amount for all)', 'format': '#######0.00', 'label': 'compute_9', 'band': 'summary'}, {'name': 'compute_6', 'expression': 'sum( profit for all)', 'format': '#######0.00', 'label': 'compute_6', 'band': 'summary'}, {'name': 'compute_12', 'expression': 'sum(stcost for all)', 'format': '#######0.00', 'label': 'compute_12', 'band': 'summary'}, {'name': 'compute_4', 'expression': 'count(  salesd_bcode for all)', 'format': '', 'label': 'compute_4', 'band': 'summary'}, {'name': 'compute_5', 'expression': 'sum(salesd_weight for all)', 'format': '######0.000', 'label': 'compute_5', 'band': 'summary'}, {'name': 'compute_7', 'expression': 'sum( costamt  for all)', 'format': '#######0.00', 'label': 'compute_7', 'band': 'summary'}, {'name': 'compute_11', 'expression': 'sum(stamt for all)', 'format': '########0.00', 'label': 'compute_11', 'band': 'summary'}, {'name': 'compute_13', 'expression': 'sum( stprofit for all)', 'format': '#######0.00', 'label': 'compute_13', 'band': 'summary'}], 'args': ['rdate1', 'rdate2', 'rlevel'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date', 'rlevel': 'number'}, 'tables': ['salesm', 'salesd', 'items'], 'columns': [{'name': 'salesm_slno', 'label': 'salesm_slno', 'type': 'decimal'}, {'name': 'salesm_tdate', 'label': 'salesm_tdate', 'type': 'date'}, {'name': 'salesm_billno', 'label': 'salesm_billno', 'type': 'char'}, {'name': 'salesm_custname', 'label': 'salesm_custname', 'type': 'char'}, {'name': 'salesm_billamt', 'label': 'salesm_billamt', 'type': 'decimal'}, {'name': 'salesm_status', 'label': 'salesm_status', 'type': 'long'}, {'name': 'salesm_discount', 'label': 'salesm_discount', 'type': 'decimal'}, {'name': 'salesm_ramt', 'label': 'salesm_ramt', 'type': 'decimal'}, {'name': 'salesm_eamt', 'label': 'salesm_eamt', 'type': 'decimal'}, {'name': 'salesm_staxamt', 'label': 'salesm_staxamt', 'type': 'decimal'}, {'name': 'salesm_duedate', 'label': 'salesm_duedate', 'type': 'date'}, {'name': 'salesm_sretamt', 'label': 'salesm_sretamt', 'type': 'decimal'}, {'name': 'salesm_ramtafter', 'label': 'salesm_ramtafter', 'type': 'decimal'}, {'name': 'round', 'label': 'round', 'type': 'decimal'}, {'name': 'salesd_code', 'label': 'salesd_code', 'type': 'char'}, {'name': 'salesd_qty', 'label': 'salesd_qty', 'type': 'long'}, {'name': 'salesd_weight', 'label': 'salesd_weight', 'type': 'decimal'}, {'name': 'salesd_dmdwgt', 'label': 'salesd_dmdwgt', 'type': 'decimal'}, {'name': 'salesd_dmdunit', 'label': 'salesd_dmdunit', 'type': 'char'}, {'name': 'salesd_dmdamt', 'label': 'salesd_dmdamt', 'type': 'decimal'}, {'name': 'salesd_bcode', 'label': 'salesd_bcode', 'type': 'decimal'}, {'name': 'salesd_amount', 'label': 'salesd_amount', 'type': 'decimal'}, {'name': 'salesd_stonewgt', 'label': 'salesd_stonewgt', 'type': 'decimal'}, {'name': 'salesd_stoneprice', 'label': 'salesd_stoneprice', 'type': 'decimal'}, {'name': 'salesd_mcharge', 'label': 'salesd_mcharge', 'type': 'decimal'}, {'name': 'salesd_wastage', 'label': 'salesd_wastage', 'type': 'decimal'}, {'name': 'items_name', 'label': 'items_name', 'type': 'char'}, {'name': 'cost', 'label': 'cost', 'type': 'decimal'}, {'name': 'costperc', 'label': 'costperc', 'type': 'decimal'}, {'name': 'bccostamt', 'label': 'bccostamt', 'type': 'decimal'}, {'name': 'items_grpcode', 'label': 'items_grpcode', 'type': 'char'}, {'name': 'items_subgrpcode', 'label': 'items_subgrpcode', 'type': 'char'}, {'name': 'stcostamt', 'label': 'stcostamt', 'type': 'decimal'}, {'name': 'dmdamt', 'label': 'dmdamt', 'type': 'decimal'}, {'name': 'dmdcostamt', 'label': 'dmdcostamt', 'type': 'decimal'}]},
)


class BarcodeProfitReportForm(GeneratedForm):
    """Barcode Profit Report"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 261, 0, 425, 92, taborder=10)
        self.add('editmask', 'em_date2', 1509, 0, 425, 92, taborder=20)
        self.add('commandbutton', 'cb_show', 2021, 0, 293, 92, text='&Show', taborder=30)
        self.add('commandbutton', 'cb_sort', 2469, 0, 247, 92, text='So&rt', taborder=31)
        self.add('commandbutton', 'cb_1', 2747, 0, 270, 92, text='Save &As', taborder=70)
        self.add('commandbutton', 'cb_print', 3022, 0, 233, 92, text='&Print', taborder=50)
        self.add('commandbutton', 'cb_exit', 3259, 0, 233, 92, text='E&xit', taborder=60)
        self.add('statictext', 'st_11', 1312, 12, 187, 72, text='To :')
        self.add('statictext', 'st_10', 32, 20, 215, 64, text='From :')
        self.add('datawindow', 'dw_grp', 261, 96, 800, 88, dataobject='d_itemgrpcode', taborder=41)
        self.add('datawindow', 'dw_subgrp', 1509, 96, 800, 88, dataobject='d_itemsubgrpcode', taborder=51)
        self.add('statictext', 'st_grp', 0, 100, 247, 76, text='Group :')
        self.add('checkbox', 'cbx_grp', 1074, 104, 78, 76)
        self.add('checkbox', 'cbx_subgrp', 2318, 104, 78, 76)
        self.add('statictext', 'st_subgrp', 1193, 108, 306, 76, text='Sub Group :')
        self.add('datawindow', 'dw_saleregister', 0, 192, 3625, 1936, dataobject='d_salesbarcode_profit_rep', taborder=40)
