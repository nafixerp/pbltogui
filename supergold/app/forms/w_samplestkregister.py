"""Sample Stock Register — w_samplestkregister.

Generated from the PowerBuilder window ``w_samplestkregister.srw`` by
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
    name='w_samplestkregister',
    title='Sample Stock Register',
    width=3643,
    height=2256,
    controls=[],
    tables=[],
    source_path='w_samplestkregister.srw',
    report={'dataobject': 'd_samplestkregister', 'sql': 'SELECT items.name AS items_name, items.itype AS items_itype, items.ornament AS items_ornament, items.code AS items_code, orderm.ordno AS orderm_ordno, orderm.tdate AS orderm_tdate, orderm.custname AS orderm_custname, orderdmodel.qty AS orderdmodel_qty, orderdmodel.weight AS orderdmodel_weight, orderdmodel.part AS orderdmodel_part, orderm.status AS orderm_status, (select salesm.tdate from salesm where salesm.billno = orderm.salebill) as refdate FROM items, orderdmodel, orderm WHERE items.code = orderdmodel.code AND orderdmodel.slno = orderm.slno ORDER BY orderm.tdate ASC, orderm.ordno ASC', 'args': ['rdate1', 'rdate2', 'rlevel'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date', 'rlevel': 'number'}, 'tables': ['items', 'orderdmodel', 'orderm'], 'columns': [{'name': 'items_name', 'label': 'items_name', 'type': 'char'}, {'name': 'items_itype', 'label': 'items_itype', 'type': 'char'}, {'name': 'items_ornament', 'label': 'items_ornament', 'type': 'char'}, {'name': 'items_code', 'label': 'items_code', 'type': 'char'}, {'name': 'orderm_ordno', 'label': 'orderm_ordno', 'type': 'char'}, {'name': 'orderm_tdate', 'label': 'orderm_tdate', 'type': 'date'}, {'name': 'orderm_custname', 'label': 'orderm_custname', 'type': 'char'}, {'name': 'orderdmodel_qty', 'label': 'orderdmodel_qty', 'type': 'long'}, {'name': 'orderdmodel_weight', 'label': 'orderdmodel_weight', 'type': 'decimal'}, {'name': 'orderdmodel_part', 'label': 'orderdmodel_part', 'type': 'char'}, {'name': 'orderm_status', 'label': 'orderm_status', 'type': 'long'}, {'name': 'crefdate', 'label': 'crefdate', 'type': 'date'}]},
    opens=['w_itemhelp'],
)


class SampleStockRegisterForm(GeneratedForm):
    """Sample Stock Register"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 384, 0, 384, 92, taborder=10)
        self.add('editmask', 'em_date2', 1463, 0, 384, 92, taborder=20)
        self.add('commandbutton', 'cb_show', 2153, 0, 274, 96, text='&Show', taborder=30)
        self.add('commandbutton', 'cb_sort', 2455, 0, 247, 92, text='So&rt', taborder=60)
        self.add('commandbutton', 'cb_print', 2725, 0, 233, 92, text='&Print', taborder=90)
        self.add('commandbutton', 'cb_1', 2962, 0, 261, 92, text='Save &As', taborder=80)
        self.add('commandbutton', 'cb_exit', 3227, 0, 233, 92, text='E&xit', taborder=100)
        self.add('statictext', 'st_11', 1152, 12, 302, 72, text='Date To :')
        self.add('statictext', 'st_10', 14, 20, 361, 64, text='Date From :')
        self.add('dropdownlistbox', 'ddlb_type', 1463, 100, 608, 532, text='Pending Only', items=['All', 'Pending Only', 'Refunded Only'], taborder=40)
        self.add('singlelineedit', 'sle_itemcode', 384, 104, 393, 96, limit=10, taborder=50)
        self.add('commandbutton', 'cb_4', 791, 108, 187, 88, text='&Help')
        self.add('statictext', 'st_3', 0, 112, 366, 72, text='Item Code :')
        self.add('statictext', 'st_2', 1207, 112, 247, 76, text='Type :')
        self.add('checkbox', 'cbx_speed', 3072, 112, 297, 76, text='Speed')
        self.add('datawindow', 'dw_saleregister', 5, 200, 3593, 1948, dataobject='d_samplestkregister', taborder=70)
