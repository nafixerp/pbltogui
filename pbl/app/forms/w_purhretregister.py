"""Purchase Return Register — w_purhretregister.

Generated from the PowerBuilder window ``w_purhretregister.srw`` by
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
    name='w_purhretregister',
    title='Purchase Return Register',
    width=3648,
    height=2192,
    controls=[],
    tables=['purchaserd', 'purchaserm', 'purchased'],
    source_path='w_purhretregister.srw',
    report={'dataobject': 'd_purhretregister', 'sql': 'SELECT items.name AS items_name, items.itype AS items_itype, items.ornament AS items_ornament, purchaserm.tdate AS purchaserm_tdate, purchaserm.docno AS purchaserm_docno, purchaserm.name AS purchaserm_name, purchaserm.billamt AS purchaserm_billamt, purchaserm.ramt AS purchaserm_ramt, purchaserm.addamt AS purchaserm_addamt, purchaserd.rate AS purchaserd_rate, purchaserd.qty AS purchaserd_qty, purchaserd.weight AS purchaserd_weight, purchaserd.lesswgt AS purchaserd_lesswgt, purchaserd.stwgt AS purchaserd_stwgt, purchaserd.stprice AS purchaserd_stprice, purchaserd.amount AS purchaserd_amount, purchaserm.slno AS purchaserm_slno, purchaserm.smcode AS purchaserm_smcode, purchaserd.name AS purchaserd_name, items.code AS items_code, purchaserd.stktype AS purchaserd_stktype, purchaserm.suppcode AS purchaserm_suppcode, items.dmdplt AS items_dmdplt FROM items, purchaserd, purchaserm WHERE items.code = purchaserd.code AND purchaserd.slno = purchaserm.slno AND purchaserm.tdate >= :rdate1 AND purchaserm.control <= :rlevel ORDER BY purchaserm.tdate ASC, purchaserm.docno ASC, purchaserm.slno ASC', 'args': ['rdate1', 'rdate2', 'rlevel'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date', 'rlevel': 'number'}, 'tables': ['items', 'purchaserd', 'purchaserm'], 'columns': [{'name': 'items_name', 'label': 'items_name', 'type': 'char'}, {'name': 'items_itype', 'label': 'items_itype', 'type': 'char'}, {'name': 'items_ornament', 'label': 'items_ornament', 'type': 'char'}, {'name': 'purchaserm_tdate', 'label': 'purchaserm_tdate', 'type': 'date'}, {'name': 'purchaserm_docno', 'label': 'purchaserm_docno', 'type': 'char'}, {'name': 'purchaserm_name', 'label': 'purchaserm_name', 'type': 'char'}, {'name': 'purchaserm_billamt', 'label': 'purchaserm_billamt', 'type': 'decimal'}, {'name': 'purchaserm_ramt', 'label': 'purchaserm_ramt', 'type': 'decimal'}, {'name': 'purchaserm_addamt', 'label': 'purchaserm_addamt', 'type': 'decimal'}, {'name': 'purchaserd_rate', 'label': 'purchaserd_rate', 'type': 'decimal'}, {'name': 'purchaserd_qty', 'label': 'purchaserd_qty', 'type': 'long'}, {'name': 'purchaserd_weight', 'label': 'purchaserd_weight', 'type': 'decimal'}, {'name': 'purchaserd_lesswgt', 'label': 'purchaserd_lesswgt', 'type': 'decimal'}, {'name': 'purchaserd_stwgt', 'label': 'purchaserd_stwgt', 'type': 'decimal'}, {'name': 'purchaserd_stprice', 'label': 'purchaserd_stprice', 'type': 'decimal'}, {'name': 'purchaserd_amount', 'label': 'purchaserd_amount', 'type': 'decimal'}, {'name': 'purchaserm_slno', 'label': 'purchaserm_slno', 'type': 'decimal'}, {'name': 'purchaserm_smcode', 'label': 'purchaserm_smcode', 'type': 'char'}, {'name': 'purchaserd_name', 'label': 'purchaserd_name', 'type': 'char'}, {'name': 'items_code', 'label': 'items_code', 'type': 'char'}, {'name': 'purchaserd_stktype', 'label': 'purchaserd_stktype', 'type': 'char'}, {'name': 'purchaserm_suppcode', 'label': 'purchaserm_suppcode', 'type': 'char'}, {'name': 'items_dmdplt', 'label': 'items_dmdplt', 'type': 'char'}]},
)


class PurchaseReturnRegisterForm(GeneratedForm):
    """Purchase Return Register"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 370, 0, 384, 92, taborder=10)
        self.add('editmask', 'em_date2', 1463, 0, 384, 92, taborder=20)
        self.add('commandbutton', 'cb_show', 2162, 0, 274, 96, text='&Show', taborder=30)
        self.add('commandbutton', 'cb_print', 2798, 4, 247, 88, text='&Print', taborder=90)
        self.add('commandbutton', 'cb_1', 3049, 4, 247, 88, text='Save &As', taborder=100)
        self.add('commandbutton', 'cb_exit', 3301, 4, 247, 88, text='E&xit', taborder=110)
        self.add('statictext', 'st_11', 1143, 12, 302, 72, text='Date To :')
        self.add('statictext', 'st_10', 0, 20, 361, 64, text='Date From :')
        self.add('datawindow', 'dw_smcode', 370, 100, 681, 96, dataobject='d_smancode', taborder=40)
        self.add('dropdownlistbox', 'ddlb_type', 1458, 100, 558, 532, text='All', items=['All', 'Ornaments Only', 'Not Ornaments', 'Gold', 'Silver', 'Others'], taborder=50)
        self.add('statictext', 'st_1', 110, 108, 247, 76, text='SMan :')
        self.add('statictext', 'st_2', 1198, 108, 247, 76, text='Type :')
        self.add('checkbox', 'cbx_itemwise', 2162, 112, 411, 76, text='Item Wise')
        self.add('checkbox', 'cbx_speed', 2807, 116, 370, 76, text='Speed')
        self.add('datawindow', 'dw_purhregister', 0, 200, 3607, 1880, dataobject='d_purhretregister', taborder=60)
        self.add('commandbutton', 'cb_sort', 2469, 204, 247, 92, text='So&rt', taborder=61)
        self.add('singlelineedit', 'sle_itemcode', 1467, 208, 393, 96, limit=10, taborder=80)
        self.add('commandbutton', 'cb_4', 1883, 208, 187, 96, text='&Help', taborder=70)
        self.add('statictext', 'st_3', 1230, 216, 219, 72, text='Item :')
