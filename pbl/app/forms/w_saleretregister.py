"""Sales Return Register — w_saleretregister.

Generated from the PowerBuilder window ``w_saleretregister.srw`` by
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
    name='w_saleretregister',
    title='Sales Return Register',
    width=3653,
    height=2176,
    controls=[],
    tables=['salesd', 'salesm'],
    source_path='w_saleretregister.srw',
    report={'dataobject': 'd_saleretregister', 'sql': 'SELECT items.name AS items_name, items.itype AS items_itype, salesrm.billno AS salesrm_billno, salesrm.tdate AS salesrm_tdate, salesrm.custname AS salesrm_custname, salesrm.billamt AS salesrm_billamt, salesrm.staxamt AS salesrm_staxamt, salesrm.discount AS salesrm_discount, salesrm.pamt AS salesrm_pamt, salesrd.code AS salesrd_code, salesrd.qty AS salesrd_qty, salesrd.weight AS salesrd_weight, salesrd.rate AS salesrd_rate, salesrd.stonewgt AS salesrd_stonewgt, salesrd.stoneprice AS salesrd_stoneprice, salesrd.mcharge AS salesrd_mcharge, salesrd.wastage AS salesrd_wastage, salesrm.slno AS salesrm_slno, salesrd.amount AS salesrd_amount, salesrm.smcode AS salesrm_smcode, salesrd.name AS salesrd_name, items.code AS items_code, salesrd.stktype AS salesrd_stktype, salesrm.ic AS salesrm_ic, items.ornament AS items_ornament, items.dmdplt AS items_dmdplt, (select barcode.counter from barcode where barcode.bcode = salesrd.bcode) as stkcounter FROM items, salesrd, salesrm WHERE items.code = salesrd.code AND salesrd.slno = salesrm.slno AND salesrm.tdate between :rdate1 and :rdate2 AND salesrm.control <= :rlevel ORDER BY salesrm.tdate ASC, salesrm.slno ASC', 'args': ['rdate1', 'rdate2', 'rlevel'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date', 'rlevel': 'number'}, 'tables': ['items', 'salesrd', 'salesrm'], 'columns': [{'name': 'items_name', 'label': 'items_name', 'type': 'char'}, {'name': 'items_itype', 'label': 'items_itype', 'type': 'char'}, {'name': 'salesrm_billno', 'label': 'salesrm_billno', 'type': 'char'}, {'name': 'salesrm_tdate', 'label': 'salesrm_tdate', 'type': 'date'}, {'name': 'salesrm_custname', 'label': 'salesrm_custname', 'type': 'char'}, {'name': 'salesrm_billamt', 'label': 'salesrm_billamt', 'type': 'decimal'}, {'name': 'salesrm_staxamt', 'label': 'salesrm_staxamt', 'type': 'decimal'}, {'name': 'salesrm_discount', 'label': 'salesrm_discount', 'type': 'decimal'}, {'name': 'salesrm_pamt', 'label': 'salesrm_pamt', 'type': 'decimal'}, {'name': 'salesrd_code', 'label': 'salesrd_code', 'type': 'char'}, {'name': 'salesrd_qty', 'label': 'salesrd_qty', 'type': 'long'}, {'name': 'salesrd_weight', 'label': 'salesrd_weight', 'type': 'decimal'}, {'name': 'salesrd_rate', 'label': 'salesrd_rate', 'type': 'decimal'}, {'name': 'salesrd_stonewgt', 'label': 'salesrd_stonewgt', 'type': 'decimal'}, {'name': 'salesrd_stoneprice', 'label': 'salesrd_stoneprice', 'type': 'decimal'}, {'name': 'salesrd_mcharge', 'label': 'salesrd_mcharge', 'type': 'decimal'}, {'name': 'salesrd_wastage', 'label': 'salesrd_wastage', 'type': 'decimal'}, {'name': 'salesrm_slno', 'label': 'salesrm_slno', 'type': 'decimal'}, {'name': 'salesrd_amount', 'label': 'salesrd_amount', 'type': 'decimal'}, {'name': 'salesrm_smcode', 'label': 'salesrm_smcode', 'type': 'char'}, {'name': 'salesrd_name', 'label': 'salesrd_name', 'type': 'char'}, {'name': 'items_code', 'label': 'items_code', 'type': 'char'}, {'name': 'salesrd_stktype', 'label': 'salesrd_stktype', 'type': 'char'}, {'name': 'salesrm_ic', 'label': 'salesrm_ic', 'type': 'char'}, {'name': 'items_ornament', 'label': 'items_ornament', 'type': 'char'}, {'name': 'items_dmdplt', 'label': 'items_dmdplt', 'type': 'char'}, {'name': 'stkcounter', 'label': 'stkcounter', 'type': 'char'}]},
)


class SalesReturnRegisterForm(GeneratedForm):
    """Sales Return Register"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 347, 0, 443, 88, taborder=10)
        self.add('editmask', 'em_date2', 1463, 0, 443, 88, taborder=20)
        self.add('commandbutton', 'cb_show', 2162, 0, 274, 96, text='&Show', taborder=30)
        self.add('commandbutton', 'cb_print', 2619, 0, 233, 96, text='&Print', taborder=100)
        self.add('commandbutton', 'cb_sort', 2862, 0, 229, 96, text='So&rt', taborder=40)
        self.add('commandbutton', 'cb_1', 3095, 0, 261, 96, text='Save &As', taborder=90)
        self.add('commandbutton', 'cb_exit', 3365, 0, 233, 96, text='E&xit', taborder=110)
        self.add('statictext', 'st_10', 5, 8, 338, 64, text='Date From :')
        self.add('statictext', 'st_11', 1189, 8, 270, 72, text='Date To :')
        self.add('datawindow', 'dw_smcode', 347, 92, 672, 88, dataobject='d_smancode', taborder=40)
        self.add('dropdownlistbox', 'ddlb_type1', 1463, 92, 608, 988, text='All', items=['All', 'Gold', 'Silver', 'Others', 'Platinum'], taborder=71)
        self.add('statictext', 'st_1', 69, 100, 274, 76, text='SMan :')
        self.add('statictext', 'st_4', 1189, 100, 270, 76, text='Type1 :')
        self.add('checkbox', 'cbx_itemwise', 2162, 100, 352, 76, text='Itemwise')
        self.add('checkbox', 'cbx_speed', 2162, 172, 297, 76, text='Speed')
        self.add('singlelineedit', 'sle_itemcode', 347, 184, 443, 88, limit=10, taborder=80)
        self.add('commandbutton', 'cb_4', 795, 184, 160, 88, text='&Help', taborder=70)
        self.add('dropdownlistbox', 'ddlb_type2', 1463, 184, 608, 796, text='All', items=['Diamond', 'Platinum', 'Gold', 'Silver', 'Others', 'Color Stone', 'Watch', 'All'], taborder=60)
        self.add('statictext', 'st_5', 1189, 188, 270, 76, text='Type2 :')
        self.add('statictext', 'st_3', 0, 196, 343, 72, text='Item Code :')
        self.add('datawindow', 'dw_stktype', 347, 272, 539, 88, dataobject='d_stktypecode', taborder=61)
        self.add('dropdownlistbox', 'ddlb_type3', 1463, 272, 608, 988, text='All', items=['All', 'Ornaments Only', 'Not Ornaments'], taborder=70)
        self.add('statictext', 'st_17', 59, 280, 283, 76, text='Stk Type :')
        self.add('statictext', 'st_6', 1189, 280, 270, 76, text='Type3 :')
        self.add('datawindow', 'dw_saleregister', 9, 360, 3625, 1720, dataobject='d_saleretregister', taborder=60)
