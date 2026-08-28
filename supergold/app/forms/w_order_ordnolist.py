"""Order Nos List — w_order_ordnolist.

Generated from the PowerBuilder window ``w_order_ordnolist.srw`` by
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
    name='w_order_ordnolist',
    title='Order Nos List',
    width=3680,
    height=2284,
    controls=[],
    tables=[],
    source_path='w_order_ordnolist.srw',
    grid={'control': 'dw_1', 'dataobject': 'd_order_ordnolist', 'table': 'orderm', 'keys': ['slno'], 'columns': [{'name': 'ordno', 'label': 'orderm_ordno', 'type': 'char'}, {'name': 'tdate', 'label': 'orderm_tdate', 'type': 'date'}, {'name': 'duedate', 'label': 'orderm_duedate', 'type': 'date'}, {'name': 'rate', 'label': 'orderm_rate', 'type': 'decimal'}, {'name': 'slno', 'label': 'orderm_slno', 'type': 'decimal'}, {'name': 'custname', 'label': 'orderm_custname', 'type': 'char'}, {'name': 'billamt', 'label': 'orderm_billamt', 'type': 'decimal'}, {'name': 'eamt', 'label': 'orderm_eamt', 'type': 'decimal'}, {'name': 'advance', 'label': 'orderm_advance', 'type': 'decimal'}, {'name': 'smcode', 'label': 'orderm_smcode', 'type': 'char'}, {'name': 'gadvance', 'label': 'orderm_gadvance', 'type': 'decimal'}, {'name': 'sretamt', 'label': 'orderm_sretamt', 'type': 'decimal'}, {'name': 'jewlcode', 'label': 'orderm_jewlcode', 'type': 'char'}, {'name': 'addr', 'label': 'orderm_addr', 'type': 'char'}, {'name': 'duedate_org', 'label': 'orderm_duedate_org', 'type': 'date'}]},
    report={'dataobject': 'd_order_ordnolist', 'sql': 'SELECT orderm.ordno AS orderm_ordno, orderm.tdate AS orderm_tdate, orderm.duedate AS orderm_duedate, orderm.rate AS orderm_rate, orderm.slno AS orderm_slno, orderm.custname AS orderm_custname, orderm.billamt AS orderm_billamt, orderm.eamt AS orderm_eamt, orderm.advance AS orderm_advance, orderm.smcode AS orderm_smcode, orderm.gadvance AS orderm_gadvance, orderm.sretamt AS orderm_sretamt, orderm.jewlcode AS orderm_jewlcode, orderm.addr AS orderm_addr, orderm.duedate_org AS orderm_duedate_org FROM orderm WHERE orderm.control <= :rlevel AND orderm.status = 1 ORDER BY orderm.ordno ASC, orderm.slno ASC', 'args': ['rlevel', 'rdate1', 'rdate2'], 'arg_types': {'rlevel': 'number', 'rdate1': 'date', 'rdate2': 'date'}, 'tables': ['orderm'], 'columns': [{'name': 'orderm_ordno', 'label': 'orderm_ordno', 'type': 'char'}, {'name': 'orderm_tdate', 'label': 'orderm_tdate', 'type': 'date'}, {'name': 'orderm_duedate', 'label': 'orderm_duedate', 'type': 'date'}, {'name': 'orderm_rate', 'label': 'orderm_rate', 'type': 'decimal'}, {'name': 'orderm_slno', 'label': 'orderm_slno', 'type': 'decimal'}, {'name': 'orderm_custname', 'label': 'orderm_custname', 'type': 'char'}, {'name': 'orderm_billamt', 'label': 'orderm_billamt', 'type': 'decimal'}, {'name': 'orderm_eamt', 'label': 'orderm_eamt', 'type': 'decimal'}, {'name': 'orderm_advance', 'label': 'orderm_advance', 'type': 'decimal'}, {'name': 'orderm_smcode', 'label': 'orderm_smcode', 'type': 'char'}, {'name': 'orderm_gadvance', 'label': 'orderm_gadvance', 'type': 'decimal'}, {'name': 'orderm_sretamt', 'label': 'orderm_sretamt', 'type': 'decimal'}, {'name': 'orderm_jewlcode', 'label': 'orderm_jewlcode', 'type': 'char'}, {'name': 'orderm_addr', 'label': 'orderm_addr', 'type': 'char'}, {'name': 'orderm_duedate_org', 'label': 'orderm_duedate_org', 'type': 'date'}]},
    opens=['w_osalehelp'],
)


class OrderNosListForm(GeneratedForm):
    """Order Nos List"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 224, 0, 407, 88, taborder=10)
        self.add('editmask', 'em_date2', 818, 0, 407, 88, taborder=20)
        self.add('dropdownlistbox', 'ddlb_sort', 2263, 0, 553, 520, text='Order No', items=['Due Date', 'Order No', 'Order Date', 'Customer'], taborder=70)
        self.add('commandbutton', 'cb_show', 2834, 0, 261, 92, text='&Show', taborder=30)
        self.add('commandbutton', 'cb_print', 3104, 0, 261, 92, text='&Print', taborder=90)
        self.add('commandbutton', 'cb_exit', 3369, 0, 261, 92, text='E&xit', taborder=80)
        self.add('statictext', 'st_2', 0, 4, 210, 76, text='From :')
        self.add('singlelineedit', 'sle_ordno', 1481, 4, 407, 84, taborder=50)
        self.add('commandbutton', 'cb_help', 1897, 4, 165, 80, text='Help', taborder=40)
        self.add('statictext', 'st_3', 667, 8, 142, 76, text='To :')
        self.add('statictext', 'st_6', 1243, 8, 233, 76, text='Ord No :')
        self.add('statictext', 'st_4', 2080, 8, 165, 76, text='Sort :')
        self.add('datawindow', 'dw_1', 14, 100, 3630, 2060, dataobject='d_order_ordnolist', taborder=60)
