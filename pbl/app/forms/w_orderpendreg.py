"""Pending Register — w_orderpendreg.

Generated from the PowerBuilder window ``w_orderpendreg.srw`` by
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
    name='w_orderpendreg',
    title='Pending Register',
    width=3680,
    height=2284,
    controls=[],
    tables=['clients'],
    source_path='w_orderpendreg.srw',
    report={'dataobject': 'd_orderpendreg', 'sql': 'SELECT orderm.ordno AS orderm_ordno, orderm.tdate AS orderm_tdate, orderm.duedate AS orderm_duedate, orderm.rate AS orderm_rate, orderm.slno AS orderm_slno, orderm.custname AS orderm_custname, orderm.billamt AS orderm_billamt, orderm.eamt AS orderm_eamt, orderm.advance AS orderm_advance, items.name AS items_name, orderd.qty AS orderd_qty, orderd.weight AS orderd_weight, orderm.smcode AS orderm_smcode, orderd.iqtype AS orderd_iqtype, orderd.stonewgt AS orderd_stonewgt, orderd.stoneprice AS orderd_stoneprice, orderm.gadvance AS orderm_gadvance, orderm.sretamt AS orderm_sretamt, orderd.part AS orderd_part, orderd.code AS orderd_code, orderm.custcode AS orderm_custcode, orderm.addr AS orderm_addr, orderd.amount AS orderd_amount, orderm.phone AS orderm_phone, items.dmdplt AS items_dmdplt, orderm.counter AS orderm_counter, orderd.stage AS orderd_stage, orderd.smith AS orderd_smith, (select name from sman where code = orderm.smcode) as smname, (select max(smithnewwrk.smithcode) from smithnewwrk where smithnewwrk.ordno =  orderm.ordno and smithnewwrk.icode = orderd.code) as smithcode, (select max(smithnewwrk.status) from smithnewwrk where smithnewwrk.ordno = orderm.ordno and smithnewwrk.icode = orderd.code) as wrkstatus FROM orderm, orderd, items WHERE orderm.slno = orderd.slno AND orderd.code = items.code AND orderm.control <= :rlevel AND orderm.status = 1 ORDER BY orderm.slno ASC', 'args': ['rlevel'], 'arg_types': {'rlevel': 'number'}, 'tables': ['orderm', 'orderd', 'items'], 'columns': [{'name': 'orderm_ordno', 'label': 'orderm_ordno', 'type': 'char'}, {'name': 'orderm_tdate', 'label': 'orderm_tdate', 'type': 'date'}, {'name': 'orderm_duedate', 'label': 'orderm_duedate', 'type': 'date'}, {'name': 'orderm_rate', 'label': 'orderm_rate', 'type': 'decimal'}, {'name': 'orderm_slno', 'label': 'orderm_slno', 'type': 'decimal'}, {'name': 'orderm_custname', 'label': 'orderm_custname', 'type': 'char'}, {'name': 'orderm_billamt', 'label': 'orderm_billamt', 'type': 'decimal'}, {'name': 'orderm_eamt', 'label': 'orderm_eamt', 'type': 'decimal'}, {'name': 'orderm_advance', 'label': 'orderm_advance', 'type': 'decimal'}, {'name': 'items_name', 'label': 'items_name', 'type': 'char'}, {'name': 'orderd_qty', 'label': 'orderd_qty', 'type': 'long'}, {'name': 'orderd_weight', 'label': 'orderd_weight', 'type': 'decimal'}, {'name': 'orderm_smcode', 'label': 'orderm_smcode', 'type': 'char'}, {'name': 'csmname', 'label': 'csmname', 'type': 'char'}, {'name': 'csmithcode', 'label': 'csmithcode', 'type': 'char'}, {'name': 'cwrkstatus', 'label': 'cwrkstatus', 'type': 'long'}, {'name': 'orderd_iqtype', 'label': 'orderd_iqtype', 'type': 'char'}, {'name': 'orderd_stonewgt', 'label': 'orderd_stonewgt', 'type': 'decimal'}, {'name': 'orderd_stoneprice', 'label': 'orderd_stoneprice', 'type': 'decimal'}, {'name': 'orderm_gadvance', 'label': 'orderm_gadvance', 'type': 'decimal'}, {'name': 'orderm_sretamt', 'label': 'orderm_sretamt', 'type': 'decimal'}, {'name': 'orderd_part', 'label': 'orderd_part', 'type': 'char'}, {'name': 'orderd_code', 'label': 'orderd_code', 'type': 'char'}, {'name': 'orderm_custcode', 'label': 'orderm_custcode', 'type': 'char'}, {'name': 'orderm_addr', 'label': 'orderm_addr', 'type': 'char'}, {'name': 'orderd_amount', 'label': 'orderd_amount', 'type': 'decimal'}, {'name': 'orderm_phone', 'label': 'orderm_phone', 'type': 'char'}, {'name': 'items_dmdplt', 'label': 'items_dmdplt', 'type': 'char'}, {'name': 'orderm_counter', 'label': 'orderm_counter', 'type': 'char'}, {'name': 'orderd_stage', 'label': 'orderd_stage', 'type': 'long'}, {'name': 'orderd_smith', 'label': 'orderd_smith', 'type': 'char'}]},
)


class PendingRegisterForm(GeneratedForm):
    """Pending Register"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 334, 0, 407, 88, taborder=10)
        self.add('editmask', 'em_date2', 1147, 0, 407, 88, taborder=20)
        self.add('datawindow', 'dw_smcode', 1797, 0, 677, 88, dataobject='d_smancode', taborder=30)
        self.add('commandbutton', 'cb_show', 2578, 0, 261, 84, text='&Show', taborder=40)
        self.add('commandbutton', 'cb_3', 2853, 0, 256, 84, text='Save &As', taborder=100)
        self.add('commandbutton', 'cb_1', 3127, 0, 219, 84, text='&Print', taborder=110)
        self.add('commandbutton', 'cb_2', 3406, 0, 219, 84, text='E&xit', taborder=90)
        self.add('checkbox', 'cbx_sm', 2478, 4, 78, 76)
        self.add('statictext', 'st_2', 0, 8, 334, 76, text='Date From')
        self.add('statictext', 'st_3', 937, 8, 210, 76, text='Date To')
        self.add('statictext', 'st_1', 1577, 12, 210, 76, text='SMan')
        self.add('singlelineedit', 'sle_itemcode', 334, 92, 407, 92, limit=10, taborder=60)
        self.add('dropdownlistbox', 'ddlb_sort', 1147, 92, 407, 796, text='Due Date', items=['Due Date', 'Order No', 'Order Date', 'Customer', 'Amount', 'Weight', 'Advance'], taborder=80)
        self.add('commandbutton', 'cb_4', 741, 96, 169, 88, text='&Help', taborder=70)
        self.add('datawindow', 'dw_counter', 1797, 96, 658, 88, dataobject='d_countercode', taborder=80)
        self.add('statictext', 'st_44', 0, 100, 334, 84, text='Item Code')
        self.add('statictext', 'st_4', 937, 100, 210, 76, text='Sort')
        self.add('checkbox', 'cbx_all', 2578, 100, 402, 76, text='All Pending')
        self.add('checkbox', 'cbx_speed', 3127, 100, 425, 76, text='Speed Print')
        self.add('statictext', 'st_7', 1573, 108, 219, 76, text='Counter')
        self.add('checkbox', 'cbx_counter', 2464, 108, 87, 76)
        self.add('checkbox', 'cbx_duedatebased', 2578, 184, 512, 80, text='Duedate Based')
        self.add('dropdownlistbox', 'ddlb_type2', 334, 188, 407, 796, text='All', items=['Diamond', 'Platinum', 'Gold', 'Silver', 'Others', 'Color Stone', 'Watch', 'All'], taborder=70)
        self.add('datawindow', 'dw_custcode', 1147, 188, 402, 88, dataobject='d_cust', taborder=80)
        self.add('commandbutton', 'cb_addr', 3127, 188, 498, 88, text='Full Address', taborder=60)
        self.add('statictext', 'st_5', 937, 196, 210, 76, text='Party')
        self.add('checkbox', 'cbx_smwise', 1797, 196, 334, 76, text='SM Wise')
        self.add('statictext', 'st_6', 0, 200, 334, 76, text='Item Type')
        self.add('datawindow', 'dw_1', 0, 280, 3630, 1868, dataobject='d_orderpendreg', taborder=50)
