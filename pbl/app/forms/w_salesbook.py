"""Sales Book — w_salesbook.

Generated from the PowerBuilder window ``w_salesbook.srw`` by
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
    name='w_salesbook',
    title='Sales Book',
    width=3680,
    height=2256,
    controls=[],
    tables=['salesm', 'salesrm', 'items', 'purchasem', 'itemsstk', 'salesd', 'purchased', 'daybook', 'salesrd', 'sreturnd', 'barcode', 'spdmddet', 'salestype', 'counter', 'generali', 'generals', 'daybookpart'],
    source_path='w_salesbook.srw',
    grid={'control': 'dw_saleregister', 'dataobject': 'd_salesbook', 'table': 'salesm', 'keys': ['slno'], 'computes': [{'name': 'compute_23', 'expression': '( salesm_discount / totva) * 100', 'format': '##0.##', 'label': 'compute_23', 'band': 'detail'}, {'name': 'compute_26', 'expression': 'if( totwgt > 0, (  totva - salesm_discount) / (totwgt - totstwgt), 0)', 'format': '####0.0', 'label': 'compute_26', 'band': 'detail'}, {'name': 'ttax', 'expression': ' salesm_staxamt  +  astamt ', 'format': '######0.00', 'label': 'ttax', 'band': 'detail'}, {'name': 'tnetamt', 'expression': ' netamt ', 'format': '######0.00', 'label': 'tnetamt', 'band': 'detail'}, {'name': 'tramt', 'expression': ' salesm_ramt  ', 'format': '#######0.00', 'label': 'tramt', 'band': 'detail'}, {'name': 'balance', 'expression': 'tnetamt -  salesm_ramt  ', 'format': '######0.00', 'label': 'balance', 'band': 'detail'}, {'name': 'compute_12', 'expression': 'sum(salesm_billamt for all)', 'format': '#######0.00', 'label': 'compute_12', 'band': 'summary'}, {'name': 'compute_18', 'expression': 'sum(salesm_sretamt for all)', 'format': '#######0.00', 'label': 'compute_18', 'band': 'summary'}, {'name': 'compute_25', 'expression': 'sum(advance for all)', 'format': '#########0.00', 'label': 'compute_25', 'band': 'summary'}, {'name': 'compute_22', 'expression': 'sum(hmc for all)', 'format': '######0.00', 'label': 'compute_22', 'band': 'summary'}, {'name': 'compute_14', 'expression': 'sum( tnetamt for all)', 'format': '######0.00', 'label': 'compute_14', 'band': 'summary'}, {'name': 'compute_13', 'expression': 'sum(balance for all)', 'format': '######0.00', 'label': 'compute_13', 'band': 'summary'}, {'name': 'compute_17', 'expression': 'sum(salesm_eamt for all)', 'format': '#######0.00', 'label': 'compute_17', 'band': 'summary'}, {'name': 'compute_16', 'expression': 'sum(salesm_discount for all)', 'format': '#######0.00', 'label': 'compute_16', 'band': 'summary'}, {'name': 'compute_15', 'expression': 'sum(ttax for all)', 'format': '#######0.00', 'label': 'compute_15', 'band': 'summary'}, {'name': 'compute_19', 'expression': 'sum( tramt  for all)', 'format': '#######0.00', 'label': 'compute_19', 'band': 'summary'}], 'columns': [{'name': 'tdate', 'label': 'salesm_tdate', 'type': 'date'}, {'name': 'billno', 'label': 'salesm_billno', 'type': 'char'}, {'name': 'custname', 'label': 'salesm_custname', 'type': 'char'}, {'name': 'billamt', 'label': 'salesm_billamt', 'type': 'decimal'}, {'name': 'status', 'label': 'salesm_status', 'type': 'long'}, {'name': 'discount', 'label': 'salesm_discount', 'type': 'decimal'}, {'name': 'discperc', 'label': 'discperc', 'type': 'decimal'}, {'name': 'ramt', 'label': 'salesm_ramt', 'type': 'decimal'}, {'name': 'eamt', 'label': 'salesm_eamt', 'type': 'decimal'}, {'name': 'staxamt', 'label': 'salesm_staxamt', 'type': 'decimal'}, {'name': 'duedate', 'label': 'salesm_duedate', 'type': 'date'}, {'name': 'sretamt', 'label': 'salesm_sretamt', 'type': 'decimal'}, {'name': 'ramtafter', 'label': 'salesm_ramtafter', 'type': 'decimal'}, {'name': 'round', 'label': 'round', 'type': 'decimal'}, {'name': 'netamt', 'label': 'netamt', 'type': 'decimal'}, {'name': 'astamt', 'label': 'astamt', 'type': 'decimal'}, {'name': 'counter', 'label': 'counter', 'type': 'char'}, {'name': 'ic', 'label': 'salesm_ic', 'type': 'char'}, {'name': 'slno', 'label': 'slno', 'type': 'decimal'}, {'name': 'hmc', 'label': 'hmc', 'type': 'decimal'}, {'name': 'totva', 'label': 'totva', 'type': 'decimal'}, {'name': 'smcode', 'label': 'smcode', 'type': 'char'}, {'name': 'advance', 'label': 'advance', 'type': 'decimal'}, {'name': 'billtype', 'label': 'billtype', 'type': 'char'}, {'name': 'totwgt', 'label': 'totwgt', 'type': 'decimal'}, {'name': 'totstwgt', 'label': 'totstwgt', 'type': 'decimal'}]},
    report={'dataobject': 'd_salesbook', 'sql': 'SELECT salesm.tdate AS salesm_tdate, salesm.billno AS salesm_billno, salesm.custname AS salesm_custname, salesm.billamt AS salesm_billamt, salesm.status AS salesm_status, salesm.discount AS salesm_discount, salesm.discperc AS salesm_discperc, salesm.ramt AS salesm_ramt, salesm.eamt AS salesm_eamt, salesm.staxamt AS salesm_staxamt, salesm.duedate AS salesm_duedate, salesm.sretamt AS salesm_sretamt, salesm.ramtafter AS salesm_ramtafter, salesm.round AS salesm_round, salesm.netamt AS salesm_netamt, salesm.astamt AS salesm_astamt, salesm.counter AS salesm_counter, salesm.ic AS salesm_ic, salesm.slno AS salesm_slno, salesm.hmc AS salesm_hmc, salesm.smcode AS salesm_smcode, salesm.advance AS salesm_advance, salesm.billtype AS salesm_billtype, (select sum(salesd.mcharge) from salesd where salesd.slno = salesm.slno) as totva, (select sum(salesd.weight) from salesd where salesd.slno = salesm.slno) as totwgt, (select sum(salesd.stonewgt) from salesd where salesd.slno = salesm.slno) as totstwgt FROM salesm WHERE salesm.tdate between :rdate1 and :rdate2 AND salesm.control <= :rlevel ORDER BY salesm.status ASC, salesm.tdate ASC, salesm.billno ASC', 'computes': [{'name': 'compute_23', 'expression': '( salesm_discount / totva) * 100', 'format': '##0.##', 'label': 'compute_23', 'band': 'detail'}, {'name': 'compute_26', 'expression': 'if( totwgt > 0, (  totva - salesm_discount) / (totwgt - totstwgt), 0)', 'format': '####0.0', 'label': 'compute_26', 'band': 'detail'}, {'name': 'ttax', 'expression': ' salesm_staxamt  +  astamt ', 'format': '######0.00', 'label': 'ttax', 'band': 'detail'}, {'name': 'tnetamt', 'expression': ' netamt ', 'format': '######0.00', 'label': 'tnetamt', 'band': 'detail'}, {'name': 'tramt', 'expression': ' salesm_ramt  ', 'format': '#######0.00', 'label': 'tramt', 'band': 'detail'}, {'name': 'balance', 'expression': 'tnetamt -  salesm_ramt  ', 'format': '######0.00', 'label': 'balance', 'band': 'detail'}, {'name': 'compute_12', 'expression': 'sum(salesm_billamt for all)', 'format': '#######0.00', 'label': 'compute_12', 'band': 'summary'}, {'name': 'compute_18', 'expression': 'sum(salesm_sretamt for all)', 'format': '#######0.00', 'label': 'compute_18', 'band': 'summary'}, {'name': 'compute_25', 'expression': 'sum(advance for all)', 'format': '#########0.00', 'label': 'compute_25', 'band': 'summary'}, {'name': 'compute_22', 'expression': 'sum(hmc for all)', 'format': '######0.00', 'label': 'compute_22', 'band': 'summary'}, {'name': 'compute_14', 'expression': 'sum( tnetamt for all)', 'format': '######0.00', 'label': 'compute_14', 'band': 'summary'}, {'name': 'compute_13', 'expression': 'sum(balance for all)', 'format': '######0.00', 'label': 'compute_13', 'band': 'summary'}, {'name': 'compute_17', 'expression': 'sum(salesm_eamt for all)', 'format': '#######0.00', 'label': 'compute_17', 'band': 'summary'}, {'name': 'compute_16', 'expression': 'sum(salesm_discount for all)', 'format': '#######0.00', 'label': 'compute_16', 'band': 'summary'}, {'name': 'compute_15', 'expression': 'sum(ttax for all)', 'format': '#######0.00', 'label': 'compute_15', 'band': 'summary'}, {'name': 'compute_19', 'expression': 'sum( tramt  for all)', 'format': '#######0.00', 'label': 'compute_19', 'band': 'summary'}], 'args': ['rdate1', 'rdate2', 'rlevel'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date', 'rlevel': 'number'}, 'tables': ['salesm'], 'columns': [{'name': 'salesm_tdate', 'label': 'salesm_tdate', 'type': 'date'}, {'name': 'salesm_billno', 'label': 'salesm_billno', 'type': 'char'}, {'name': 'salesm_custname', 'label': 'salesm_custname', 'type': 'char'}, {'name': 'salesm_billamt', 'label': 'salesm_billamt', 'type': 'decimal'}, {'name': 'salesm_status', 'label': 'salesm_status', 'type': 'long'}, {'name': 'salesm_discount', 'label': 'salesm_discount', 'type': 'decimal'}, {'name': 'discperc', 'label': 'discperc', 'type': 'decimal'}, {'name': 'salesm_ramt', 'label': 'salesm_ramt', 'type': 'decimal'}, {'name': 'salesm_eamt', 'label': 'salesm_eamt', 'type': 'decimal'}, {'name': 'salesm_staxamt', 'label': 'salesm_staxamt', 'type': 'decimal'}, {'name': 'salesm_duedate', 'label': 'salesm_duedate', 'type': 'date'}, {'name': 'salesm_sretamt', 'label': 'salesm_sretamt', 'type': 'decimal'}, {'name': 'salesm_ramtafter', 'label': 'salesm_ramtafter', 'type': 'decimal'}, {'name': 'round', 'label': 'round', 'type': 'decimal'}, {'name': 'netamt', 'label': 'netamt', 'type': 'decimal'}, {'name': 'astamt', 'label': 'astamt', 'type': 'decimal'}, {'name': 'counter', 'label': 'counter', 'type': 'char'}, {'name': 'salesm_ic', 'label': 'salesm_ic', 'type': 'char'}, {'name': 'slno', 'label': 'slno', 'type': 'decimal'}, {'name': 'hmc', 'label': 'hmc', 'type': 'decimal'}, {'name': 'totva', 'label': 'totva', 'type': 'decimal'}, {'name': 'smcode', 'label': 'smcode', 'type': 'char'}, {'name': 'advance', 'label': 'advance', 'type': 'decimal'}, {'name': 'billtype', 'label': 'billtype', 'type': 'char'}, {'name': 'totwgt', 'label': 'totwgt', 'type': 'decimal'}, {'name': 'totstwgt', 'label': 'totstwgt', 'type': 'decimal'}]},
    opens=['w_diamond_sales_print', 'w_sales_view'],
)


class SalesBookForm(GeneratedForm):
    """Sales Book"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 334, 0, 425, 92, taborder=10)
        self.add('editmask', 'em_date2', 1271, 0, 425, 92, taborder=20)
        self.add('commandbutton', 'cb_show', 1728, 0, 293, 96, text='&Show', taborder=30)
        self.add('commandbutton', 'cb_sort', 2583, 0, 256, 92, text='So&rt', taborder=40)
        self.add('commandbutton', 'cb_1', 2843, 0, 256, 92, text='Save &As', taborder=120)
        self.add('commandbutton', 'cb_print', 3109, 0, 256, 92, text='&Print', taborder=90)
        self.add('commandbutton', 'cb_exit', 3369, 0, 256, 92, text='E&xit', taborder=110)
        self.add('statictext', 'st_11', 965, 4, 302, 72, text='Date To :')
        self.add('statictext', 'st_10', 9, 8, 338, 64, text='Date From')
        self.add('checkbox', 'cbx_register', 2071, 8, 302, 76, text='Register')
        self.add('datawindow', 'dw_ic', 2839, 92, 695, 88, dataobject='d_incharge_code', taborder=50)
        self.add('datawindow', 'dw_counter', 334, 96, 658, 88, dataobject='d_countercode', taborder=60)
        self.add('checkbox', 'cbx_taxrep', 2071, 96, 370, 76, text='Tax Report')
        self.add('statictext', 'st_2', 2565, 100, 274, 80, text='Incharge :')
        self.add('checkbox', 'cbx_ic', 3538, 100, 87, 76)
        self.add('statictext', 'st_1', 9, 104, 279, 76, text='Counter')
        self.add('checkbox', 'cbx_counterwise', 1266, 104, 489, 72, text='Counter wise')
        self.add('checkbox', 'cbx_counter', 1001, 108, 87, 76)
        self.add('commandbutton', 'cb_frupdt', 1728, 184, 293, 100, text='Fr Updt')
        self.add('datawindow', 'dw_smcode', 334, 188, 677, 88, dataobject='d_smancode', taborder=80)
        self.add('datawindow', 'dw_billtype', 1271, 188, 425, 88, dataobject='d_billtypecode', taborder=100)
        self.add('commandbutton', 'cb_selall', 2025, 188, 306, 96, text='Select All')
        self.add('commandbutton', 'cb_tobill', 2331, 188, 256, 96, text='To Bill')
        self.add('commandbutton', 'cb_toest', 2587, 188, 256, 96, text='To Est')
        self.add('commandbutton', 'cb_delete', 2848, 188, 256, 96, text='Delete')
        self.add('commandbutton', 'cb_rearrange', 3095, 188, 283, 96, text='Rearrange')
        self.add('commandbutton', 'cb_reprint', 3369, 188, 256, 96, text='Reprint')
        self.add('statictext', 'st_3', 9, 196, 210, 76, text='SMan')
        self.add('statictext', 'st_4', 1061, 200, 206, 72, text='BType :')
        self.add('datawindow', 'dw_saleregister', 0, 284, 3625, 1848, dataobject='d_salesbook', taborder=70)
        self.add('commandbutton', 'cb_einvoice', 2857, 288, 667, 80, text='Create EInvoice Json', taborder=80)
