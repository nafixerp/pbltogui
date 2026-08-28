"""Net Sales Report — w_netsalesrep.

Generated from the PowerBuilder window ``w_netsalesrep.srw`` by
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
    name='w_netsalesrep',
    title='Net Sales Report',
    width=3689,
    height=2336,
    controls=[],
    tables=['salesm', 'purchasem', 'salesrm', 'daybook', 'accountm', 'counter', 'generals', 'daybookpart', 'generali'],
    source_path='w_netsalesrep.srw',
    grid={'control': 'dw_saleregister', 'dataobject': 'd_netsalesrep', 'table': 'salesm', 'keys': ['slno'], 'columns': [{'name': 'slno', 'label': 'salesm_slno', 'type': 'decimal'}, {'name': 'tdate', 'label': 'salesm_tdate', 'type': 'date'}, {'name': 'billno', 'label': 'salesm_billno', 'type': 'char'}, {'name': 'custname', 'label': 'salesm_custname', 'type': 'char'}, {'name': 'billamt', 'label': 'salesm_billamt', 'type': 'decimal'}, {'name': 'status', 'label': 'salesm_status', 'type': 'long'}, {'name': 'discount', 'label': 'salesm_discount', 'type': 'decimal'}, {'name': 'ramt', 'label': 'salesm_ramt', 'type': 'decimal'}, {'name': 'eamt', 'label': 'salesm_eamt', 'type': 'decimal'}, {'name': 'staxamt', 'label': 'salesm_staxamt', 'type': 'decimal'}, {'name': 'duedate', 'label': 'salesm_duedate', 'type': 'date'}, {'name': 'sretamt', 'label': 'salesm_sretamt', 'type': 'decimal'}, {'name': 'ramtafter', 'label': 'salesm_ramtafter', 'type': 'decimal'}, {'name': 'round', 'label': 'round', 'type': 'decimal'}, {'name': 'netamt', 'label': 'netamt', 'type': 'decimal'}, {'name': 'astamt', 'label': 'astamt', 'type': 'decimal'}, {'name': 'counter', 'label': 'counter', 'type': 'char'}, {'name': 'ic', 'label': 'salesm_ic', 'type': 'char'}, {'name': 'tsaleswgt', 'label': 'tsaleswgt', 'type': 'decimal'}, {'name': 'tsretwgt', 'label': 'tsretwgt', 'type': 'decimal'}, {'name': 'smcode', 'label': 'smcode', 'type': 'char'}, {'name': 'cocode', 'label': 'cocode', 'type': 'char'}, {'name': 'tsalesstwgt', 'label': 'tsalesstwgt', 'type': 'decimal'}, {'name': 'tva', 'label': 'tva', 'type': 'decimal'}, {'name': 'tstamt', 'label': 'tstamt', 'type': 'decimal'}, {'name': 'agcode', 'label': 'agcode', 'type': 'char'}]},
    report={'dataobject': 'd_netsalesrep', 'sql': 'SELECT salesm.slno AS salesm_slno, salesm.tdate AS salesm_tdate, salesm.billno AS salesm_billno, salesm.custname AS salesm_custname, salesm.billamt AS salesm_billamt, salesm.status AS salesm_status, salesm.discount AS salesm_discount, salesm.ramt AS salesm_ramt, salesm.eamt AS salesm_eamt, salesm.staxamt AS salesm_staxamt, salesm.duedate AS salesm_duedate, salesm.sretamt AS salesm_sretamt, salesm.ramtafter AS salesm_ramtafter, salesm.round AS salesm_round, salesm.netamt AS salesm_netamt, salesm.astamt AS salesm_astamt, salesm.counter AS salesm_counter, salesm.ic AS salesm_ic, salesm.smcode AS salesm_smcode, salesm.cocode AS salesm_cocode, salesm.agcode AS salesm_agcode, (select sum(salesd.weight) from salesd where salesd.slno = salesm.slno) as tsaleswgt, (select sum(salesrd.weight) from salesrd where salesrd.slno = salesm.slno) as tsretwgt, (select sum(salesd.stonewgt) from salesd where salesd.slno = salesm.slno) as tsalesstwgt, (select sum(salesd.mcharge) from salesd where salesd.slno = salesm.slno) as tva, (select sum(salesd.stoneprice) from salesd where salesd.slno = salesm.slno) as tstamt FROM salesm WHERE salesm.tdate between :rdate1 and :rdate2 AND salesm.control <= :rlevel ORDER BY salesm.status ASC, salesm.tdate ASC, salesm.billno ASC, salesm.slno ASC', 'args': ['rdate1', 'rdate2', 'rlevel'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date', 'rlevel': 'number'}, 'tables': ['salesm'], 'columns': [{'name': 'salesm_slno', 'label': 'salesm_slno', 'type': 'decimal'}, {'name': 'salesm_tdate', 'label': 'salesm_tdate', 'type': 'date'}, {'name': 'salesm_billno', 'label': 'salesm_billno', 'type': 'char'}, {'name': 'salesm_custname', 'label': 'salesm_custname', 'type': 'char'}, {'name': 'salesm_billamt', 'label': 'salesm_billamt', 'type': 'decimal'}, {'name': 'salesm_status', 'label': 'salesm_status', 'type': 'long'}, {'name': 'salesm_discount', 'label': 'salesm_discount', 'type': 'decimal'}, {'name': 'salesm_ramt', 'label': 'salesm_ramt', 'type': 'decimal'}, {'name': 'salesm_eamt', 'label': 'salesm_eamt', 'type': 'decimal'}, {'name': 'salesm_staxamt', 'label': 'salesm_staxamt', 'type': 'decimal'}, {'name': 'salesm_duedate', 'label': 'salesm_duedate', 'type': 'date'}, {'name': 'salesm_sretamt', 'label': 'salesm_sretamt', 'type': 'decimal'}, {'name': 'salesm_ramtafter', 'label': 'salesm_ramtafter', 'type': 'decimal'}, {'name': 'round', 'label': 'round', 'type': 'decimal'}, {'name': 'netamt', 'label': 'netamt', 'type': 'decimal'}, {'name': 'astamt', 'label': 'astamt', 'type': 'decimal'}, {'name': 'counter', 'label': 'counter', 'type': 'char'}, {'name': 'salesm_ic', 'label': 'salesm_ic', 'type': 'char'}, {'name': 'tsaleswgt', 'label': 'tsaleswgt', 'type': 'decimal'}, {'name': 'tsretwgt', 'label': 'tsretwgt', 'type': 'decimal'}, {'name': 'smcode', 'label': 'smcode', 'type': 'char'}, {'name': 'cocode', 'label': 'cocode', 'type': 'char'}, {'name': 'tsalesstwgt', 'label': 'tsalesstwgt', 'type': 'decimal'}, {'name': 'tva', 'label': 'tva', 'type': 'decimal'}, {'name': 'tstamt', 'label': 'tstamt', 'type': 'decimal'}, {'name': 'agcode', 'label': 'agcode', 'type': 'char'}]},
)


class NetSalesReportForm(GeneratedForm):
    """Net Sales Report"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 224, 0, 443, 92, taborder=10)
        self.add('editmask', 'em_date2', 878, 0, 443, 92, taborder=20)
        self.add('dropdownlistbox', 'ddlb_reptype', 1582, 0, 503, 380, text='Net Sales', items=['Net Sales', 'C/o Summary', 'Agent Summary'], taborder=50)
        self.add('commandbutton', 'cb_show', 2144, 0, 293, 96, text='&Show', taborder=30)
        self.add('commandbutton', 'cb_sort', 2464, 0, 265, 96, text='So&rt', taborder=40)
        self.add('commandbutton', 'cb_saveas', 2770, 0, 265, 96, text='Save &As', taborder=110)
        self.add('commandbutton', 'cb_print', 3072, 0, 265, 96, text='&Print', taborder=90)
        self.add('commandbutton', 'cb_exit', 3355, 0, 265, 96, text='E&xit', taborder=100)
        self.add('statictext', 'st_11', 731, 8, 137, 72, text='To :')
        self.add('statictext', 'st_5', 1344, 8, 238, 80, text='RepType')
        self.add('statictext', 'st_10', 0, 12, 229, 64, text='From')
        self.add('datawindow', 'dw_counter', 224, 100, 654, 88, dataobject='d_countercode', taborder=60)
        self.add('datawindow', 'dw_ic', 1582, 100, 695, 88, dataobject='d_incharge_code', taborder=50)
        self.add('commandbutton', 'cb_selall', 2464, 100, 265, 88, text='Select All')
        self.add('commandbutton', 'cb_tobill', 2770, 100, 265, 88, text='To Bill')
        self.add('commandbutton', 'cb_toest', 3072, 100, 265, 88, text='To Est')
        self.add('statictext', 'st_1', 0, 104, 229, 76, text='Counter')
        self.add('statictext', 'st_2', 1344, 104, 238, 80, text='Incharge')
        self.add('checkbox', 'cbx_ic', 2281, 104, 87, 76)
        self.add('checkbox', 'cbx_counter', 882, 108, 87, 76)
        self.add('datawindow', 'dw_smcode', 224, 192, 677, 88, dataobject='d_smancode', taborder=72)
        self.add('datawindow', 'dw_agent', 2464, 192, 882, 88, dataobject='d_agent_sel', taborder=72)
        self.add('checkbox', 'cbx_agent', 3346, 192, 87, 76)
        self.add('datawindow', 'dw_co', 1582, 196, 402, 88, dataobject='d_cust', taborder=70)
        self.add('statictext', 'st_3', 0, 200, 229, 76, text='SMan')
        self.add('commandbutton', 'cb_cohelp', 1989, 200, 91, 84, text='^', taborder=62)
        self.add('statictext', 'st_16', 1344, 204, 238, 76, text='C/o')
        self.add('statictext', 'st_4', 2277, 204, 178, 76, text='Agent')
        self.add('datawindow', 'dw_saleregister', 0, 284, 3625, 1852, dataobject='d_netsalesrep', taborder=80)
