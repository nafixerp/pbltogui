"""Customer Sales Summary — w_partysummaryrep.

Generated from the PowerBuilder window ``w_partysummaryrep.srw`` by
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
    name='w_partysummaryrep',
    title='Customer Sales Summary',
    width=3657,
    height=2188,
    controls=[],
    tables=['accountm'],
    source_path='w_partysummaryrep.srw',
    grid={'control': 'dw_saleregister', 'dataobject': 'd_partysummaryrep', 'table': 'clients', 'keys': ['code'], 'computes': [{'name': 'netswgt', 'expression': 'if(isnull( tsaleswgt ),0,tsaleswgt) - if(isnull(tsretwgt ), 0, tsretwgt)', 'format': '#######0.000', 'label': 'netswgt', 'band': 'detail'}, {'name': 'netsamt', 'expression': 'if(isnull( tsalesamt ),0,tsalesamt)  - if(isnull(  tsretamt ),0, tsretamt) - if(isnull(   tsalesdisc ),0,  tsalesdisc )', 'format': '#######0.00', 'label': 'netsamt', 'band': 'detail'}, {'name': 'points', 'expression': ' netswgt', 'format': '#######0', 'label': 'points', 'band': 'detail'}, {'name': 'compute_3', 'expression': 'sum(tsaleswgt for all)', 'format': '#######0.000', 'label': 'compute_3', 'band': 'summary'}, {'name': 'compute_4', 'expression': 'sum(tsretwgt for all)', 'format': '#######0.000', 'label': 'compute_4', 'band': 'summary'}, {'name': 'compute_8', 'expression': 'sum( netswgt for all)', 'format': '#######0.000', 'label': 'compute_8', 'band': 'summary'}, {'name': 'compute_7', 'expression': 'sum(tsalesamt for all)', 'format': '#########0.00', 'label': 'compute_7', 'band': 'summary'}, {'name': 'compute_6', 'expression': 'sum(tsretamt for all)', 'format': '#########0.00', 'label': 'compute_6', 'band': 'summary'}, {'name': 'compute_9', 'expression': 'sum( netsamt  for all)', 'format': '#########0.00', 'label': 'compute_9', 'band': 'summary'}], 'columns': [{'name': 'tsalesamt', 'label': 'tsalesamt', 'type': 'decimal'}, {'name': 'tsalesdisc', 'label': 'tsalesdisc', 'type': 'decimal'}, {'name': 'tsretamt', 'label': 'tsretamt', 'type': 'decimal'}, {'name': 'tsaleswgt', 'label': 'tsaleswgt', 'type': 'decimal'}, {'name': 'tsretwgt', 'label': 'tsretwgt', 'type': 'decimal'}, {'name': 'name', 'label': 'name', 'type': 'char'}, {'name': 'grp', 'label': 'grp', 'type': 'char'}, {'name': 'code', 'label': 'code', 'type': 'char'}, {'name': 'pcard', 'label': 'pcard', 'type': 'char'}]},
    report={'dataobject': 'd_partysummaryrep', 'sql': "SELECT clients.name AS clients_name, clients.grp AS clients_grp, clients.code AS clients_code, clients.pcard AS clients_pcard, (select sum(sm.billamt) from salesm sm where sm.custcode = clients.code and sm.tdate >= :rdate1 and sm.tdate <= :rdate2 and sm.control <= :rlevel) as tsalesamt, (select sum(sm.discount) from salesm sm where sm.custcode = clients.code and sm.tdate >= :rdate1 and sm.tdate <= :rdate2 and sm.control <= :rlevel) as tsalesdisc, (select sum(sm.billamt) from salesrm sm where sm.custcode = clients.code and sm.tdate >= :rdate1 and sm.tdate <= :rdate2 and sm.control <= :rlevel) as tsretamt, (select sum(salesd.weight) from salesd,salesm sm,items where salesd.slno = sm.slno and salesd.code = items.code and items.itype = 'G' and sm.custcode = clients.code and sm.tdate >= :rdate1 and sm.tdate <= :rdate2 and sm.control <= :rlevel ) as tsaleswgt, (select sum(salesrd.weight) from salesrd,salesrm sm,items where salesrd.slno = sm.slno and salesrd.code = items.code and items.itype = 'G' and sm.custcode = clients.code and sm.tdate >= :rdate1 and sm.tdate <= :rdate2 and sm.control <= :rlevel ) as tsretwgt FROM clients WHERE tsalesamt > 0 ORDER BY clients.name ASC", 'computes': [{'name': 'netswgt', 'expression': 'if(isnull( tsaleswgt ),0,tsaleswgt) - if(isnull(tsretwgt ), 0, tsretwgt)', 'format': '#######0.000', 'label': 'netswgt', 'band': 'detail'}, {'name': 'netsamt', 'expression': 'if(isnull( tsalesamt ),0,tsalesamt)  - if(isnull(  tsretamt ),0, tsretamt) - if(isnull(   tsalesdisc ),0,  tsalesdisc )', 'format': '#######0.00', 'label': 'netsamt', 'band': 'detail'}, {'name': 'points', 'expression': ' netswgt', 'format': '#######0', 'label': 'points', 'band': 'detail'}, {'name': 'compute_3', 'expression': 'sum(tsaleswgt for all)', 'format': '#######0.000', 'label': 'compute_3', 'band': 'summary'}, {'name': 'compute_4', 'expression': 'sum(tsretwgt for all)', 'format': '#######0.000', 'label': 'compute_4', 'band': 'summary'}, {'name': 'compute_8', 'expression': 'sum( netswgt for all)', 'format': '#######0.000', 'label': 'compute_8', 'band': 'summary'}, {'name': 'compute_7', 'expression': 'sum(tsalesamt for all)', 'format': '#########0.00', 'label': 'compute_7', 'band': 'summary'}, {'name': 'compute_6', 'expression': 'sum(tsretamt for all)', 'format': '#########0.00', 'label': 'compute_6', 'band': 'summary'}, {'name': 'compute_9', 'expression': 'sum( netsamt  for all)', 'format': '#########0.00', 'label': 'compute_9', 'band': 'summary'}], 'args': ['rdate1', 'rdate2', 'rlevel', 'rgrp'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date', 'rlevel': 'number', 'rgrp': 'string'}, 'tables': ['clients'], 'columns': [{'name': 'tsalesamt', 'label': 'tsalesamt', 'type': 'decimal'}, {'name': 'tsalesdisc', 'label': 'tsalesdisc', 'type': 'decimal'}, {'name': 'tsretamt', 'label': 'tsretamt', 'type': 'decimal'}, {'name': 'tsaleswgt', 'label': 'tsaleswgt', 'type': 'decimal'}, {'name': 'tsretwgt', 'label': 'tsretwgt', 'type': 'decimal'}, {'name': 'name', 'label': 'name', 'type': 'char'}, {'name': 'grp', 'label': 'grp', 'type': 'char'}, {'name': 'code', 'label': 'code', 'type': 'char'}, {'name': 'pcard', 'label': 'pcard', 'type': 'char'}]},
    opens=['w_clientshelp'],
)


class CustomerSalesSummaryForm(GeneratedForm):
    """Customer Sales Summary"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 224, 0, 361, 92, taborder=10)
        self.add('editmask', 'em_date2', 763, 0, 361, 92, taborder=20)
        self.add('commandbutton', 'cb_show', 2368, 0, 242, 96, text='&Show', taborder=30)
        self.add('commandbutton', 'cb_sort', 2624, 0, 242, 96, text='So&rt', taborder=40)
        self.add('commandbutton', 'cb_saveas', 2871, 0, 242, 96, text='Save &As', taborder=110)
        self.add('commandbutton', 'cb_print', 3127, 0, 242, 96, text='&Print', taborder=90)
        self.add('commandbutton', 'cb_exit', 3378, 0, 242, 96, text='E&xit', taborder=100)
        self.add('datawindow', 'dw_grp', 1431, 4, 677, 88, dataobject='d_clientsgrp_code', taborder=50)
        self.add('statictext', 'st_10', 0, 8, 215, 64, text='From :')
        self.add('statictext', 'st_11', 617, 8, 137, 72, text='To :')
        self.add('checkbox', 'cbx_grp', 2117, 8, 73, 80)
        self.add('statictext', 'st_1', 1184, 12, 238, 64, text='Group :')
        self.add('statictext', 'st_3', 0, 96, 215, 72, text='Party :')
        self.add('datawindow', 'dw_accode', 224, 96, 402, 88, dataobject='d_cust', taborder=70)
        self.add('datawindow', 'dw_pcard', 1431, 96, 745, 88, dataobject='d_pcard_code', taborder=60)
        self.add('checkbox', 'cbx_pcard', 2181, 96, 73, 80)
        self.add('statictext', 'st_2', 1184, 100, 238, 64, text='PCard :')
        self.add('checkbox', 'cbx_sortonpoints', 2373, 104, 498, 80, text='Sort On Points')
        self.add('datawindow', 'dw_saleregister', 0, 184, 3625, 1832, dataobject='d_partysummaryrep', taborder=80)
