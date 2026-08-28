"""Order Process — w_order_process.

Generated from the PowerBuilder window ``w_order_process.srw`` by
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
    name='w_order_process',
    title='Order Process',
    width=3794,
    height=2284,
    controls=[],
    tables=['orderm', 'clients', 'orderd', 'daybook', 'daybookpart'],
    source_path='w_order_process.srw',
    grid={'control': 'dw_smith', 'dataobject': 'd_smith', 'table': 'codehelp', 'keys': ['code'], 'computes': [], 'columns': [{'name': 'code', 'label': 'code', 'type': 'char'}]},
    report={'dataobject': 'd_order_process', 'sql': 'SELECT orderm.ordno AS orderm_ordno, orderm.tdate AS orderm_tdate, orderm.duedate AS orderm_duedate, orderm.rate AS orderm_rate, orderm.slno AS orderm_slno, orderm.custname AS orderm_custname, orderm.billamt AS orderm_billamt, orderm.eamt AS orderm_eamt, orderm.advance AS orderm_advance, items.name AS items_name, orderd.qty AS orderd_qty, orderd.weight AS orderd_weight, orderm.smcode AS orderm_smcode, orderd.iqtype AS orderd_iqtype, orderd.stonewgt AS orderd_stonewgt, orderd.stoneprice AS orderd_stoneprice, orderm.gadvance AS orderm_gadvance, orderm.sretamt AS orderm_sretamt, orderd.code AS orderd_code, orderd.smith AS orderd_smith, orderd.stage AS orderd_stage, orderd.sno AS orderd_sno, orderm.jewlcode AS orderm_jewlcode, orderd.part AS orderd_part, orderd.smithddate AS orderd_smithddate, orderm.custcode AS orderm_custcode, items.dmdplt AS items_dmdplt, orderm.addr AS orderm_addr, orderm.phone AS orderm_phone, (select clients.mobile from clients where clients.code = orderm.custcode) as cmobile FROM orderm, orderd, items WHERE orderm.slno = orderd.slno AND orderd.code = items.code AND orderm.control <= :rlevel AND orderm.status = 1 ORDER BY orderm.slno ASC', 'computes': [{'name': 'tadv', 'expression': '  orderm_advance  +  orderm_eamt  +  orderm_sretamt ', 'format': '#########0.00', 'label': 'tadv', 'band': 'detail'}, {'name': 'compute_2', 'expression': 'sum(orderd_weight for all)', 'format': '######0.000', 'label': 'compute_2', 'band': 'summary'}], 'args': ['rlevel'], 'arg_types': {'rlevel': 'number'}, 'tables': ['orderm', 'orderd', 'items'], 'columns': [{'name': 'orderm_ordno', 'label': 'orderm_ordno', 'type': 'char'}, {'name': 'orderm_tdate', 'label': 'orderm_tdate', 'type': 'date'}, {'name': 'orderm_duedate', 'label': 'orderm_duedate', 'type': 'date'}, {'name': 'orderm_rate', 'label': 'orderm_rate', 'type': 'decimal'}, {'name': 'orderm_slno', 'label': 'orderm_slno', 'type': 'decimal'}, {'name': 'orderm_custname', 'label': 'orderm_custname', 'type': 'char'}, {'name': 'orderm_billamt', 'label': 'orderm_billamt', 'type': 'decimal'}, {'name': 'orderm_eamt', 'label': 'orderm_eamt', 'type': 'decimal'}, {'name': 'orderm_advance', 'label': 'orderm_advance', 'type': 'decimal'}, {'name': 'items_name', 'label': 'items_name', 'type': 'char'}, {'name': 'orderd_qty', 'label': 'orderd_qty', 'type': 'long'}, {'name': 'orderd_weight', 'label': 'orderd_weight', 'type': 'decimal'}, {'name': 'orderm_smcode', 'label': 'orderm_smcode', 'type': 'char'}, {'name': 'orderd_iqtype', 'label': 'orderd_iqtype', 'type': 'char'}, {'name': 'orderd_stonewgt', 'label': 'orderd_stonewgt', 'type': 'decimal'}, {'name': 'orderd_stoneprice', 'label': 'orderd_stoneprice', 'type': 'decimal'}, {'name': 'orderm_gadvance', 'label': 'orderm_gadvance', 'type': 'decimal'}, {'name': 'orderm_sretamt', 'label': 'orderm_sretamt', 'type': 'decimal'}, {'name': 'orderd_code', 'label': 'orderd_code', 'type': 'char'}, {'name': 'orderd_smith', 'label': 'orderd_smith', 'type': 'char'}, {'name': 'orderd_stage', 'label': 'orderd_stage', 'type': 'long'}, {'name': 'orderd_sno', 'label': 'orderd_sno', 'type': 'long'}, {'name': 'orderm_jewlcode', 'label': 'orderm_jewlcode', 'type': 'char'}, {'name': 'orderd_part', 'label': 'orderd_part', 'type': 'char'}, {'name': 'orderd_smithddate', 'label': 'orderd_smithddate', 'type': 'date'}, {'name': 'orderm_custcode', 'label': 'orderm_custcode', 'type': 'char'}, {'name': 'items_dmdplt', 'label': 'items_dmdplt', 'type': 'char'}, {'name': 'orderm_addr', 'label': 'orderm_addr', 'type': 'char'}, {'name': 'orderm_phone', 'label': 'orderm_phone', 'type': 'char'}, {'name': 'cmobile', 'label': 'cmobile', 'type': 'char'}]},
    opens=['w_itemhelp', 'w_clientshelp', 'w_osalehelp'],
)


class OrderProcessForm(GeneratedForm):
    """Order Process"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 233, 0, 439, 88, taborder=10)
        self.add('editmask', 'em_date2', 1042, 0, 407, 88, taborder=20)
        self.add('dropdownlistbox', 'ddlb_sort', 1769, 0, 494, 520, text='Due Date', items=['Due Date', 'Order No', 'Order Date', 'Customer', 'Smith Duedate'], taborder=130)
        self.add('commandbutton', 'cb_show', 2309, 0, 261, 92, text='&Show', taborder=30)
        self.add('commandbutton', 'cb_update', 2578, 0, 261, 92, text='&Update', taborder=40)
        self.add('commandbutton', 'cb_delete', 2848, 0, 247, 92, text='Delete', taborder=100)
        self.add('commandbutton', 'cb_1', 3104, 0, 261, 92, text='&Print', taborder=150)
        self.add('commandbutton', 'cb_2', 3369, 0, 261, 92, text='E&xit', taborder=140)
        self.add('statictext', 'st_2', 23, 4, 206, 76, text='From :')
        self.add('statictext', 'st_3', 891, 8, 142, 76, text='To :')
        self.add('statictext', 'st_4', 1586, 8, 178, 76, text='Sort :')
        self.add('dropdownlistbox', 'ddlb_stage', 1769, 92, 494, 440, text='All', items=['All', 'New Work', 'Work In Progress', 'Finished'], taborder=60)
        self.add('datawindow', 'dw_jewl', 1042, 96, 439, 92, dataobject='d_jewl', taborder=110)
        self.add('datawindow', 'dw_smith', 233, 100, 439, 92, dataobject='d_smith', taborder=90)
        self.add('dropdownlistbox', 'ddlb_stagepref', 1513, 100, 242, 88, text='Only', items=['Only', 'Not'], taborder=50)
        self.add('singlelineedit', 'sle_itemcode', 2853, 104, 393, 88, limit=10, taborder=70)
        self.add('statictext', 'st_1', 14, 108, 215, 76, text='Smith :')
        self.add('checkbox', 'cbx_all', 2309, 108, 338, 76, text='All Pending')
        self.add('commandbutton', 'cb_4', 3255, 108, 160, 84, text='&Help', taborder=80)
        self.add('statictext', 'st_5', 850, 112, 183, 76, text='Jewl :')
        self.add('statictext', 'st_10', 2661, 116, 183, 72, text='Item :')
        self.add('dropdownlistbox', 'ddlb_reptype', 1769, 184, 494, 540, text='Details', items=['Details', 'Summary', 'Without Customers'], taborder=63)
        self.add('datawindow', 'dw_custcode', 1042, 196, 402, 88, dataobject='d_cust', taborder=80)
        self.add('datawindow', 'dw_smcode', 2853, 196, 672, 88, dataobject='d_smancode', taborder=80)
        self.add('singlelineedit', 'sle_ordno', 233, 200, 439, 88, taborder=80)
        self.add('statictext', 'st_6', 0, 204, 229, 76, text='Ord No :')
        self.add('statictext', 'st_9', 837, 204, 201, 80, text='Party :')
        self.add('checkbox', 'cbx_sm', 3529, 204, 73, 72)
        self.add('commandbutton', 'cb_help', 677, 208, 119, 80, text='Help', taborder=70)
        self.add('statictext', 'st_7', 1495, 212, 270, 64, text='Rep Type :')
        self.add('statictext', 'st_8', 2610, 212, 233, 72, text='SMan :')
        self.add('dropdownlistbox', 'ddlb_type2', 1769, 276, 494, 796, text='All', items=['Diamond', 'Platinum', 'Gold', 'Silver', 'Others', 'Color Stone', 'Watch', 'All'], taborder=80)
        self.add('commandbutton', 'cb_sendsms', 2309, 276, 503, 92, text='Send SMS', taborder=90)
        self.add('statictext', 'st_11', 1477, 292, 288, 64, text='Item Type :')
        self.add('checkbox', 'cbx_speed', 2853, 292, 425, 68, text='Speed Print')
        self.add('datawindow', 'dw_1', 5, 372, 3767, 1800, dataobject='d_order_process', taborder=120)
