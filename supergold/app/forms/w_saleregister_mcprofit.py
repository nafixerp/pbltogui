"""MC Profit Report — w_saleregister_mcprofit.

Generated from the PowerBuilder window ``w_saleregister_mcprofit.srw`` by
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
    name='w_saleregister_mcprofit',
    title='MC Profit Report',
    width=3662,
    height=2416,
    controls=[],
    tables=['clients', 'salesrm', 'items'],
    source_path='w_saleregister_mcprofit.srw',
    report={'dataobject': 'd_saleregister_mcprofrep', 'sql': 'SELECT salesm.billno AS salesm_billno, salesm.tdate AS salesm_tdate, salesm.billamt AS salesm_billamt, salesm.eamt AS salesm_eamt, salesm.sretamt AS salesm_sretamt, salesm.staxamt AS salesm_staxamt, salesm.discount AS salesm_discount, salesm.ramt AS salesm_ramt, salesm.ramtafter AS salesm_ramtafter, salesm.slno AS salesm_slno, salesd.slno AS salesd_slno, items.name AS items_name, salesd.qty AS salesd_qty, salesd.weight AS salesd_weight, items.itype AS items_itype, salesd.jcode AS salesd_jcode, items.ornament AS items_ornament, salesd.amount AS salesd_amount, salesm.smcode AS salesm_smcode, salesd.name AS salesd_name, items.code AS items_code, salesd.stonewgt AS salesd_stonewgt, salesd.stktype AS salesd_stktype, salesm.round AS salesm_round, salesm.counter AS salesm_counter, salesd.mcharge AS salesd_mcharge, salesd.wastage AS salesd_wastage, salesd.rate AS salesd_rate, salesm.astamt AS salesm_astamt, salesm.ic AS salesm_ic, salesm.custcode AS salesm_custcode, salesd.bcode AS salesd_bcode, salesm.orderno AS salesm_orderno, items.smithmc AS items_smithmc, salesm.custname AS salesm_custname, salesm.netamt AS salesm_netamt, items.dmdplt AS items_dmdplt, salesm.status AS salesm_status, items.grpcode AS items_grpcode, (select barcode.counter from barcode where barcode.bcode = salesd.bcode) as stkcounter, 1 as igrp FROM salesd, salesm, items WHERE salesd.slno = salesm.slno AND salesd.code = items.code AND salesm.tdate between :rdate1 and :rdate2 AND salesm.control <= :rlevel ORDER BY salesm.tdate ASC, salesm.slno ASC', 'computes': [{'name': 'itemname', 'expression': "if(   salesd_name = '' or isnull(   salesd_name ) , items_name,   salesd_name ) ", 'format': '[general]', 'label': 'itemname', 'band': 'detail'}, {'name': 'va', 'expression': ' salesd_mcharge  +  salesd_wastage  *  salesd_rate ', 'format': '####0', 'label': 'va', 'band': 'detail'}, {'name': 'vapergm', 'expression': 'if(( salesd_weight -  salesd_stonewgt )> 0,  va / ( salesd_weight -  salesd_stonewgt ), 0)', 'format': '#####0.00', 'label': 'vapergm', 'band': 'detail'}, {'name': 'disc', 'expression': 'if(salesm_billamt > 0,  salesm_discount * salesd_amount  /  salesm_billamt , 0)', 'format': '########0.00', 'label': 'disc', 'band': 'detail'}, {'name': 'mcprof', 'expression': 'if(salesd_mcharge <> 0, salesd_mcharge - disc - ( salesd_weight  -  salesd_stonewgt ) *  items_smithmc ,0)', 'format': '########0.00', 'label': 'mcprof', 'band': 'detail'}, {'name': 'salesamt', 'expression': "sum( if(   items_itype = 'G',  salesd_amount , 0 ) for all )", 'format': '######0.00', 'label': 'salesamt', 'band': 'summary'}, {'name': 'totmcprof', 'expression': 'sum( mcprof for all )', 'format': '######0.00', 'label': 'totmcprof', 'band': 'summary'}, {'name': 'compute_4', 'expression': 'count(salesm_billno for all distinct)', 'format': '[general]', 'label': 'compute_4', 'band': 'summary'}, {'name': 'compute_5', 'expression': 'count(salesm_billno for all )', 'format': '[general]', 'label': 'compute_5', 'band': 'summary'}, {'name': 'gswgt', 'expression': " sum( if( items_itype  = 'G' , salesd_weight ,0) for all ) ", 'format': '#####0.000', 'label': 'gswgt', 'band': 'summary'}, {'name': 'gstwgt', 'expression': 'sum(salesd_stonewgt for all)', 'format': '[General]', 'label': 'gstwgt', 'band': 'summary'}, {'name': 'compute_8', 'expression': 'sum( salesd_mcharge  +  salesd_wastage  *  salesd_rate  for all)', 'format': '####0', 'label': 'compute_8', 'band': 'summary'}, {'name': 'tsilverwgt', 'expression': "sum( if(   items_itype = 'S',  salesd_weight , 0 ) for all )", 'format': '######.000', 'label': 'tsilverwgt', 'band': 'summary'}, {'name': 'compute_13', 'expression': "sum( if(   items_itype = 'S',  salesd_amount , 0 ) for all )", 'format': '######0.00', 'label': 'compute_13', 'band': 'summary'}, {'name': 'salesamt2', 'expression': "sum( if(   items_itype = 'G' and salesd_weight <> 0,  salesd_amount , 0 ) for all )", 'format': '######0.00', 'label': 'salesamt2', 'band': 'summary'}, {'name': 'compute_6', 'expression': '(salesamt2 - totdisc)/ (gswgt - gstwgt2)', 'format': '######0.00', 'label': 'compute_6', 'band': 'summary'}, {'name': 'netsales', 'expression': ' sum( salesm_billamt  for all distinct salesm_slno ) ', 'format': '#######0.00', 'label': 'netsales', 'band': 'summary'}, {'name': 'gstwgt2', 'expression': "sum( if(   items_itype = 'G' and salesd_stonewgt <> 0,  salesd_stonewgt , 0 ) for all )", 'format': '######0.00', 'label': 'gstwgt2', 'band': 'summary'}, {'name': 'tottax', 'expression': 'sum(  salesm_staxamt + salesm_astamt for all distinct  salesm_slno )', 'format': '###0.00', 'label': 'tottax', 'band': 'summary'}, {'name': 'compute_7', 'expression': "avg( if(items_itype = 'G' ,  (  salesd_amount / (   salesd_weight -   salesd_stonewgt )) ,0)   for all )", 'format': '######0.00', 'label': 'compute_7', 'band': 'summary'}, {'name': 'totdisc', 'expression': 'sum(  salesm_discount for all distinct  salesm_slno )', 'format': '###0.00', 'label': 'totdisc', 'band': 'summary'}], 'args': ['rdate1', 'rdate2', 'rlevel'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date', 'rlevel': 'number'}, 'tables': ['salesd', 'salesm', 'items'], 'columns': [{'name': 'salesm_billno', 'label': 'salesm_billno', 'type': 'char'}, {'name': 'salesm_tdate', 'label': 'salesm_tdate', 'type': 'date'}, {'name': 'salesm_billamt', 'label': 'salesm_billamt', 'type': 'decimal'}, {'name': 'salesm_eamt', 'label': 'salesm_eamt', 'type': 'decimal'}, {'name': 'salesm_sretamt', 'label': 'salesm_sretamt', 'type': 'decimal'}, {'name': 'salesm_staxamt', 'label': 'salesm_staxamt', 'type': 'decimal'}, {'name': 'salesm_discount', 'label': 'salesm_discount', 'type': 'decimal'}, {'name': 'salesm_ramt', 'label': 'salesm_ramt', 'type': 'decimal'}, {'name': 'salesm_ramtafter', 'label': 'salesm_ramtafter', 'type': 'decimal'}, {'name': 'salesm_slno', 'label': 'salesm_slno', 'type': 'decimal'}, {'name': 'salesd_slno', 'label': 'salesd_slno', 'type': 'decimal'}, {'name': 'items_name', 'label': 'items_name', 'type': 'char'}, {'name': 'salesd_qty', 'label': 'salesd_qty', 'type': 'long'}, {'name': 'salesd_weight', 'label': 'salesd_weight', 'type': 'decimal'}, {'name': 'items_itype', 'label': 'items_itype', 'type': 'char'}, {'name': 'salesd_jcode', 'label': 'salesd_jcode', 'type': 'char'}, {'name': 'items_ornament', 'label': 'items_ornament', 'type': 'char'}, {'name': 'salesd_amount', 'label': 'salesd_amount', 'type': 'decimal'}, {'name': 'salesm_smcode', 'label': 'salesm_smcode', 'type': 'char'}, {'name': 'salesd_name', 'label': 'salesd_name', 'type': 'char'}, {'name': 'items_code', 'label': 'items_code', 'type': 'char'}, {'name': 'salesd_stonewgt', 'label': 'salesd_stonewgt', 'type': 'decimal'}, {'name': 'salesd_stktype', 'label': 'salesd_stktype', 'type': 'char'}, {'name': 'salesm_round', 'label': 'salesm_round', 'type': 'decimal'}, {'name': 'salesm_counter', 'label': 'salesm_counter', 'type': 'char'}, {'name': 'salesd_mcharge', 'label': 'salesd_mcharge', 'type': 'decimal'}, {'name': 'salesd_wastage', 'label': 'salesd_wastage', 'type': 'decimal'}, {'name': 'salesd_rate', 'label': 'salesd_rate', 'type': 'decimal'}, {'name': 'salesm_astamt', 'label': 'salesm_astamt', 'type': 'decimal'}, {'name': 'salesm_ic', 'label': 'salesm_ic', 'type': 'char'}, {'name': 'salesm_custcode', 'label': 'salesm_custcode', 'type': 'char'}, {'name': 'salesd_bcode', 'label': 'salesd_bcode', 'type': 'decimal'}, {'name': 'salesm_orderno', 'label': 'salesm_orderno', 'type': 'char'}, {'name': 'items_smithmc', 'label': 'items_smithmc', 'type': 'decimal'}, {'name': 'salesm_custname', 'label': 'salesm_custname', 'type': 'char'}, {'name': 'salesm_netamt', 'label': 'salesm_netamt', 'type': 'decimal'}, {'name': 'items_dmdplt', 'label': 'items_dmdplt', 'type': 'char'}, {'name': 'salesm_status', 'label': 'salesm_status', 'type': 'long'}, {'name': 'stkcounter', 'label': 'stkcounter', 'type': 'char'}, {'name': 'igrp', 'label': 'igrp', 'type': 'long'}, {'name': 'items_grpcode', 'label': 'items_grpcode', 'type': 'char'}]},
    opens=['w_clientshelp', 'w_itemhelp'],
)


class McProfitReportForm(GeneratedForm):
    """MC Profit Report"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 370, 0, 384, 92, taborder=10)
        self.add('editmask', 'em_date2', 1353, 0, 384, 92, taborder=20)
        self.add('commandbutton', 'cb_show', 2327, 0, 229, 92, text='&Show', taborder=30)
        self.add('commandbutton', 'cb_print', 2633, 0, 229, 92, text='&Print', taborder=130)
        self.add('commandbutton', 'cb_sort', 2898, 0, 229, 92, text='So&rt', taborder=100)
        self.add('commandbutton', 'cb_1', 3136, 0, 229, 92, text='Save &As', taborder=120)
        self.add('commandbutton', 'cb_exit', 3374, 0, 229, 92, text='E&xit', taborder=140)
        self.add('checkbox', 'cbx_withzerodisc', 1815, 4, 475, 68, text='With Zero Disc')
        self.add('statictext', 'st_11', 1042, 12, 302, 72, text='Date To :')
        self.add('statictext', 'st_10', 0, 20, 361, 64, text='Date From :')
        self.add('dropdownlistbox', 'ddlb_type', 1353, 100, 608, 532, text='All', items=['All', 'Ornaments Only', 'Not Ornaments', 'Gold', 'Silver', 'Others'], taborder=50)
        self.add('dropdownlistbox', 'ddlb_mctype', 2327, 100, 539, 824, text='All', items=['< 200', '200-250', '250-300', '300-350', '> 350', 'All'], taborder=90)
        self.add('datawindow', 'dw_smcode', 370, 104, 677, 88, dataobject='d_smancode', taborder=80)
        self.add('checkbox', 'cbx_cashonly', 2885, 108, 347, 80, text='Cash only')
        self.add('statictext', 'st_1', 151, 112, 210, 76, text='SMan :')
        self.add('statictext', 'st_2', 1152, 112, 192, 76, text='Type :')
        self.add('statictext', 'st_5', 2011, 112, 302, 76, text='MC Type :')
        self.add('checkbox', 'cbx_speed', 3241, 112, 393, 76, text='Speed Print')
        self.add('datawindow', 'dw_ic', 370, 204, 695, 88, dataobject='d_incharge_code', taborder=90)
        self.add('singlelineedit', 'sle_itemcode', 1358, 204, 393, 88, limit=10, taborder=60)
        self.add('datawindow', 'dw_custcode', 3168, 204, 402, 88, dataobject='d_cust', taborder=40)
        self.add('commandbutton', 'cb_4', 1755, 208, 160, 84, text='&Help')
        self.add('datawindow', 'dw_stktype', 2327, 208, 539, 88, dataobject='d_stktypecode', taborder=70)
        self.add('statictext', 'st_20', 50, 212, 311, 80, text='Incharge :')
        self.add('checkbox', 'cbx_ic', 1065, 212, 87, 76)
        self.add('statictext', 'st_4', 2912, 212, 251, 80, text='Party :')
        self.add('statictext', 'st_3', 1157, 216, 183, 72, text='Item :')
        self.add('statictext', 'st_17', 2011, 216, 293, 76, text='Stk Type :')
        self.add('datawindow', 'dw_saleregister', 5, 308, 3593, 1832, dataobject='d_saleregister_mcprofrep', taborder=110)
