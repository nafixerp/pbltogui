"""Order Advance Report — w_orderadvrep.

Generated from the PowerBuilder window ``w_orderadvrep.srw`` by
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
    name='w_orderadvrep',
    title='Order Advance Report',
    width=3689,
    height=2300,
    controls=[],
    tables=[],
    source_path='w_orderadvrep.srw',
    grid={'control': 'dw_1', 'dataobject': 'd_orderadvrep', 'table': 'orderm', 'keys': ['slno'], 'columns': [{'name': 'ordno', 'label': 'orderm_ordno', 'type': 'char'}, {'name': 'tdate', 'label': 'orderm_tdate', 'type': 'date'}, {'name': 'duedate', 'label': 'orderm_duedate', 'type': 'date'}, {'name': 'rate', 'label': 'orderm_rate', 'type': 'decimal'}, {'name': 'custname', 'label': 'orderm_custname', 'type': 'char'}, {'name': 'billamt', 'label': 'orderm_billamt', 'type': 'decimal'}, {'name': 'eamt', 'label': 'orderm_eamt', 'type': 'decimal'}, {'name': 'advance', 'label': 'orderm_advance', 'type': 'decimal'}, {'name': 'status', 'label': 'status', 'type': 'long'}, {'name': 'slno', 'label': 'orderm_slno', 'type': 'decimal'}, {'name': 'custcode', 'label': 'custcode', 'type': 'char'}, {'name': 'smname', 'label': 'smname', 'type': 'char'}, {'name': 'gadvance', 'label': 'gadvance', 'type': 'decimal'}, {'name': 'sretamt', 'label': 'sretamt', 'type': 'decimal'}, {'name': 'smcode', 'label': 'smcode', 'type': 'char'}, {'name': 'addr', 'label': 'addr', 'type': 'char'}, {'name': 'advafter', 'label': 'advafter', 'type': 'decimal'}, {'name': 'advafterwgt', 'label': 'advafterwgt', 'type': 'decimal'}, {'name': 'salesamt', 'label': 'salesamt', 'type': 'decimal'}, {'name': 'counter', 'label': 'counter', 'type': 'char'}]},
    report={'dataobject': 'd_orderadvrep', 'sql': 'SELECT orderm.ordno AS orderm_ordno, orderm.tdate AS orderm_tdate, orderm.duedate AS orderm_duedate, orderm.rate AS orderm_rate, orderm.custname AS orderm_custname, orderm.billamt AS orderm_billamt, orderm.eamt AS orderm_eamt, orderm.advance AS orderm_advance, orderm.status AS orderm_status, orderm.slno AS orderm_slno, orderm.custcode AS orderm_custcode, orderm.gadvance AS orderm_gadvance, orderm.sretamt AS orderm_sretamt, orderm.smcode AS orderm_smcode, orderm.addr AS orderm_addr, orderm.counter AS orderm_counter, (select name from sman where code = orderm.smcode) as smname, (select sum(advafter.amount) from advafter where advafter.ordno = orderm.ordno) as advafter, (select sum(advafter.wgt) from advafter where advafter.ordno = orderm.ordno) as advafterwgt, (select sum(salesm.billamt) from salesm where salesm.orderno = orderm.ordno) as salesamt FROM orderm WHERE orderm.control <= :rlevel AND orderm.tdate between :rdate1 and :rdate2 ORDER BY orderm.tdate ASC, orderm.slno ASC', 'args': ['rlevel', 'rdate1', 'rdate2'], 'arg_types': {'rlevel': 'number', 'rdate1': 'date', 'rdate2': 'date'}, 'tables': ['orderm'], 'columns': [{'name': 'orderm_ordno', 'label': 'orderm_ordno', 'type': 'char'}, {'name': 'orderm_tdate', 'label': 'orderm_tdate', 'type': 'date'}, {'name': 'orderm_duedate', 'label': 'orderm_duedate', 'type': 'date'}, {'name': 'orderm_rate', 'label': 'orderm_rate', 'type': 'decimal'}, {'name': 'orderm_custname', 'label': 'orderm_custname', 'type': 'char'}, {'name': 'orderm_billamt', 'label': 'orderm_billamt', 'type': 'decimal'}, {'name': 'orderm_eamt', 'label': 'orderm_eamt', 'type': 'decimal'}, {'name': 'orderm_advance', 'label': 'orderm_advance', 'type': 'decimal'}, {'name': 'status', 'label': 'status', 'type': 'long'}, {'name': 'orderm_slno', 'label': 'orderm_slno', 'type': 'decimal'}, {'name': 'custcode', 'label': 'custcode', 'type': 'char'}, {'name': 'smname', 'label': 'smname', 'type': 'char'}, {'name': 'gadvance', 'label': 'gadvance', 'type': 'decimal'}, {'name': 'sretamt', 'label': 'sretamt', 'type': 'decimal'}, {'name': 'smcode', 'label': 'smcode', 'type': 'char'}, {'name': 'addr', 'label': 'addr', 'type': 'char'}, {'name': 'advafter', 'label': 'advafter', 'type': 'decimal'}, {'name': 'advafterwgt', 'label': 'advafterwgt', 'type': 'decimal'}, {'name': 'salesamt', 'label': 'salesamt', 'type': 'decimal'}, {'name': 'counter', 'label': 'counter', 'type': 'char'}]},
)


class OrderAdvanceReportForm(GeneratedForm):
    """Order Advance Report"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 219, 0, 448, 92, taborder=10)
        self.add('editmask', 'em_date2', 896, 0, 448, 92, taborder=20)
        self.add('commandbutton', 'cb_show', 2496, 0, 261, 96, text='&Show', taborder=30)
        self.add('commandbutton', 'cb_3', 2830, 0, 261, 92, text='Save &As', taborder=80)
        self.add('commandbutton', 'cb_1', 3095, 0, 265, 92, text='&Print', taborder=90)
        self.add('commandbutton', 'cb_2', 3360, 0, 265, 92, text='E&xit', taborder=70)
        self.add('statictext', 'st_2', 736, 4, 151, 76, text='To :')
        self.add('datawindow', 'dw_smcode', 1669, 4, 672, 88, dataobject='d_smancode', taborder=40)
        self.add('checkbox', 'cbx_sm', 2345, 8, 73, 76)
        self.add('statictext', 'st_1', 0, 12, 210, 76, text='From :')
        self.add('statictext', 'st_10', 1449, 12, 210, 76, text='SMan :')
        self.add('dropdownlistbox', 'ddlb_type', 219, 96, 562, 384, text='All', items=['All', 'Pending Only', 'Returned Only'], taborder=60)
        self.add('datawindow', 'dw_counter', 1669, 96, 658, 88, dataobject='d_countercode', taborder=70)
        self.add('checkbox', 'cbx_counter', 2345, 96, 73, 76)
        self.add('statictext', 'st_3', 0, 108, 210, 76, text='Type :')
        self.add('statictext', 'st_4', 1381, 108, 279, 76, text='Counter :')
        self.add('datawindow', 'dw_1', 5, 188, 3621, 2084, dataobject='d_orderadvrep', taborder=50)
