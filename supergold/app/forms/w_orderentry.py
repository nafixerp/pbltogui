"""Order Entries — w_orderentry.

Generated from the PowerBuilder window ``w_orderentry.srw`` by
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
    name='w_orderentry',
    title='Order Entries',
    width=3689,
    height=2300,
    controls=[],
    tables=[],
    source_path='w_orderentry.srw',
    grid={'control': 'dw_1', 'dataobject': 'd_orderentry', 'table': 'orderm', 'keys': ['slno'], 'columns': [{'name': 'ordno', 'label': 'orderm_ordno', 'type': 'char'}, {'name': 'tdate', 'label': 'orderm_tdate', 'type': 'date'}, {'name': 'duedate', 'label': 'orderm_duedate', 'type': 'date'}, {'name': 'rate', 'label': 'orderm_rate', 'type': 'decimal'}, {'name': 'custname', 'label': 'orderm_custname', 'type': 'char'}, {'name': 'billamt', 'label': 'orderm_billamt', 'type': 'decimal'}, {'name': 'eamt', 'label': 'orderm_eamt', 'type': 'decimal'}, {'name': 'advance', 'label': 'orderm_advance', 'type': 'decimal'}, {'name': 'status', 'label': 'status', 'type': 'long'}, {'name': 'slno', 'label': 'orderm_slno', 'type': 'decimal'}, {'name': 'custcode', 'label': 'custcode', 'type': 'char'}, {'name': 'smname', 'label': 'smname', 'type': 'char'}, {'name': 'gadvance', 'label': 'gadvance', 'type': 'decimal'}, {'name': 'sretamt', 'label': 'sretamt', 'type': 'decimal'}, {'name': 'smcode', 'label': 'smcode', 'type': 'char'}, {'name': 'addr', 'label': 'addr', 'type': 'char'}, {'name': 'refund', 'label': 'refund', 'type': 'decimal'}, {'name': 'duedate_org', 'label': 'duedate_org', 'type': 'date'}]},
    report={'dataobject': 'd_orderentry', 'sql': 'SELECT orderm.ordno AS orderm_ordno, orderm.tdate AS orderm_tdate, orderm.duedate AS orderm_duedate, orderm.rate AS orderm_rate, orderm.custname AS orderm_custname, orderm.billamt AS orderm_billamt, orderm.eamt AS orderm_eamt, orderm.advance AS orderm_advance, orderm.status AS orderm_status, orderm.slno AS orderm_slno, orderm.custcode AS orderm_custcode, orderm.gadvance AS orderm_gadvance, orderm.sretamt AS orderm_sretamt, orderm.smcode AS orderm_smcode, orderm.addr AS orderm_addr, orderm.refund AS orderm_refund, orderm.duedate_org AS orderm_duedate_org, (select name from sman where code = orderm.smcode) as smname FROM orderm WHERE orderm.control <= :rlevel AND orderm.tdate between :rdate1 and :rdate2 ORDER BY orderm.tdate ASC, orderm.slno ASC', 'args': ['rlevel', 'rdate1', 'rdate2'], 'arg_types': {'rlevel': 'number', 'rdate1': 'date', 'rdate2': 'date'}, 'tables': ['orderm'], 'columns': [{'name': 'orderm_ordno', 'label': 'orderm_ordno', 'type': 'char'}, {'name': 'orderm_tdate', 'label': 'orderm_tdate', 'type': 'date'}, {'name': 'orderm_duedate', 'label': 'orderm_duedate', 'type': 'date'}, {'name': 'orderm_rate', 'label': 'orderm_rate', 'type': 'decimal'}, {'name': 'orderm_custname', 'label': 'orderm_custname', 'type': 'char'}, {'name': 'orderm_billamt', 'label': 'orderm_billamt', 'type': 'decimal'}, {'name': 'orderm_eamt', 'label': 'orderm_eamt', 'type': 'decimal'}, {'name': 'orderm_advance', 'label': 'orderm_advance', 'type': 'decimal'}, {'name': 'status', 'label': 'status', 'type': 'long'}, {'name': 'orderm_slno', 'label': 'orderm_slno', 'type': 'decimal'}, {'name': 'custcode', 'label': 'custcode', 'type': 'char'}, {'name': 'smname', 'label': 'smname', 'type': 'char'}, {'name': 'gadvance', 'label': 'gadvance', 'type': 'decimal'}, {'name': 'sretamt', 'label': 'sretamt', 'type': 'decimal'}, {'name': 'smcode', 'label': 'smcode', 'type': 'char'}, {'name': 'addr', 'label': 'addr', 'type': 'char'}, {'name': 'refund', 'label': 'refund', 'type': 'decimal'}, {'name': 'duedate_org', 'label': 'duedate_org', 'type': 'date'}]},
)


class OrderEntriesForm(GeneratedForm):
    """Order Entries"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 361, 0, 434, 92, taborder=10)
        self.add('editmask', 'em_date2', 1175, 0, 434, 92, taborder=20)
        self.add('singlelineedit', 'sle_ordno', 1920, 0, 407, 84, taborder=51)
        self.add('commandbutton', 'cb_show', 2427, 0, 261, 96, text='&Show', taborder=30)
        self.add('commandbutton', 'cb_3', 2830, 0, 261, 92, text='Save &As', taborder=80)
        self.add('commandbutton', 'cb_1', 3095, 0, 265, 92, text='&Print', taborder=90)
        self.add('commandbutton', 'cb_2', 3360, 0, 265, 92, text='E&xit', taborder=70)
        self.add('statictext', 'st_1', 0, 8, 352, 76, text='Date From :')
        self.add('statictext', 'st_6', 1678, 8, 233, 76, text='Ord No :')
        self.add('statictext', 'st_2', 891, 12, 274, 76, text='Date To :')
        self.add('dropdownlistbox', 'ddlb_type', 361, 96, 594, 380, text='All', items=['All', 'Pending Only', 'Returned Only'], taborder=60)
        self.add('datawindow', 'dw_smcode', 1175, 96, 677, 88, dataobject='d_smancode', taborder=40)
        self.add('checkbox', 'cbx_sm', 1861, 96, 73, 76)
        self.add('statictext', 'st_10', 960, 104, 210, 76, text='SMan :')
        self.add('datawindow', 'dw_1', 5, 188, 3621, 2028, dataobject='d_orderentry', taborder=50)
