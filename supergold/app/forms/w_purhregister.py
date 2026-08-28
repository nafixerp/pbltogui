"""Purchase Register — w_purhregister.

Generated from the PowerBuilder window ``w_purhregister.srw`` by
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
    name='w_purhregister',
    title='Purchase Register',
    width=3657,
    height=2296,
    controls=[],
    tables=[],
    source_path='w_purhregister.srw',
    grid={'control': 'dw_1', 'dataobject': 'd_supp', 'table': 'codehelp', 'keys': ['code'], 'columns': [{'name': 'code', 'label': 'code', 'type': 'char'}]},
    report={'dataobject': 'd_purhregister', 'sql': 'SELECT items.name AS items_name, items.itype AS items_itype, purchased.code AS purchased_code, purchased.qty AS purchased_qty, purchased.weight AS purchased_weight, purchased.amount AS purchased_amount, purchasem.tdate AS purchasem_tdate, purchasem.slno AS purchasem_slno, purchasem.docno AS purchasem_docno, purchasem.name AS purchasem_name, purchasem.billamt AS purchasem_billamt, purchasem.pamt AS purchasem_pamt, purchasem.addamt AS purchasem_addamt, purchasem.eamt AS purchasem_eamt, purchasem.duedate AS purchasem_duedate, purchasem.pr AS purchasem_pr, items.ornament AS items_ornament, purchased.lesswgt AS purchased_lesswgt, purchased.slno AS purchased_slno, purchasem.smcode AS purchasem_smcode, purchased.rate AS purchased_rate, items.code AS items_code, purchased.name AS purchased_name, purchased.stwgt AS purchased_stwgt, purchased.mud AS purchased_mud, purchased.stktype AS purchased_stktype, purchasem.suppcode AS purchasem_suppcode, purchasem.ic AS purchasem_ic, items.dmdplt AS items_dmdplt, purchased.stprice AS purchased_stprice, purchased.mcharge AS purchased_mcharge, purchased.dmdamt AS purchased_dmdamt, purchasem.addr AS purchasem_addr, purchasem.rate AS purchasem_rate, (purchasem.counter) as counter, (purchasem.billtype) as billtype FROM items, purchased, purchasem WHERE items.code = purchased.code AND purchased.slno = purchasem.slno AND purchasem.tdate between :rdate1 and :rdate2 AND purchasem.control <= :rlevel ORDER BY purchasem.tdate ASC, purchasem.slno ASC', 'args': ['rdate1', 'rdate2', 'rlevel'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date', 'rlevel': 'number'}, 'tables': ['items', 'purchased', 'purchasem'], 'columns': [{'name': 'items_name', 'label': 'items_name', 'type': 'char'}, {'name': 'items_itype', 'label': 'items_itype', 'type': 'char'}, {'name': 'purchased_code', 'label': 'purchased_code', 'type': 'char'}, {'name': 'purchased_qty', 'label': 'purchased_qty', 'type': 'long'}, {'name': 'purchased_weight', 'label': 'purchased_weight', 'type': 'decimal'}, {'name': 'purchased_amount', 'label': 'purchased_amount', 'type': 'decimal'}, {'name': 'purchasem_tdate', 'label': 'purchasem_tdate', 'type': 'date'}, {'name': 'purchasem_slno', 'label': 'purchasem_slno', 'type': 'decimal'}, {'name': 'purchasem_docno', 'label': 'purchasem_docno', 'type': 'char'}, {'name': 'purchasem_name', 'label': 'purchasem_name', 'type': 'char'}, {'name': 'purchasem_billamt', 'label': 'purchasem_billamt', 'type': 'decimal'}, {'name': 'purchasem_pamt', 'label': 'purchasem_pamt', 'type': 'decimal'}, {'name': 'purchasem_addamt', 'label': 'purchasem_addamt', 'type': 'decimal'}, {'name': 'purchasem_eamt', 'label': 'purchasem_eamt', 'type': 'decimal'}, {'name': 'purchasem_duedate', 'label': 'purchasem_duedate', 'type': 'date'}, {'name': 'purchasem_pr', 'label': 'purchasem_pr', 'type': 'char'}, {'name': 'items_ornament', 'label': 'items_ornament', 'type': 'char'}, {'name': 'purchased_lesswgt', 'label': 'purchased_lesswgt', 'type': 'decimal'}, {'name': 'purchased_slno', 'label': 'purchased_slno', 'type': 'decimal'}, {'name': 'purchasem_smcode', 'label': 'purchasem_smcode', 'type': 'char'}, {'name': 'purchased_rate', 'label': 'purchased_rate', 'type': 'decimal'}, {'name': 'items_code', 'label': 'items_code', 'type': 'char'}, {'name': 'purchased_name', 'label': 'purchased_name', 'type': 'char'}, {'name': 'purchased_stwgt', 'label': 'purchased_stwgt', 'type': 'decimal'}, {'name': 'purchased_mud', 'label': 'purchased_mud', 'type': 'decimal'}, {'name': 'purchased_stktype', 'label': 'purchased_stktype', 'type': 'char'}, {'name': 'purchasem_suppcode', 'label': 'purchasem_suppcode', 'type': 'char'}, {'name': 'purchasem_ic', 'label': 'purchasem_ic', 'type': 'char'}, {'name': 'items_dmdplt', 'label': 'items_dmdplt', 'type': 'char'}, {'name': 'purchased_stprice', 'label': 'purchased_stprice', 'type': 'decimal'}, {'name': 'purchased_mcharge', 'label': 'purchased_mcharge', 'type': 'decimal'}, {'name': 'purchased_dmdamt', 'label': 'purchased_dmdamt', 'type': 'decimal'}, {'name': 'purchasem_addr', 'label': 'purchasem_addr', 'type': 'char'}, {'name': 'purchasem_rate', 'label': 'purchasem_rate', 'type': 'decimal'}, {'name': 'counter', 'label': 'counter', 'type': 'char'}, {'name': 'billtype', 'label': 'billtype', 'type': 'char'}]},
)


class PurchaseRegisterForm(GeneratedForm):
    """Purchase Register"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 261, 0, 443, 92, taborder=10)
        self.add('editmask', 'em_date2', 1321, 0, 443, 92, taborder=20)
        self.add('commandbutton', 'cb_show', 2112, 0, 274, 92, text='&Show', taborder=50)
        self.add('commandbutton', 'cb_print', 2437, 0, 247, 92, text='&Print', taborder=130)
        self.add('commandbutton', 'cb_sort', 2839, 0, 247, 92, text='So&rt', taborder=30)
        self.add('commandbutton', 'cb_1', 3090, 0, 247, 92, text='Save &As', taborder=140)
        self.add('commandbutton', 'cb_exit', 3342, 0, 247, 92, text='E&xit', taborder=150)
        self.add('statictext', 'st_10', 5, 12, 251, 64, text='From')
        self.add('statictext', 'st_11', 1033, 12, 283, 72, text='Date To')
        self.add('statictext', 'st_1', 5, 96, 251, 76, text='SMan')
        self.add('datawindow', 'dw_smcode', 261, 96, 677, 88, dataobject='d_smancode', taborder=70)
        self.add('datawindow', 'dw_ic', 1321, 96, 695, 88, dataobject='d_incharge_code', taborder=61)
        self.add('dropdownlistbox', 'ddlb_reptype', 2441, 96, 539, 988, text='Billwise', items=['Billwise', 'Itemwise', 'Pres.StoneWise', 'SManWise', 'SManWise Summary', 'Touch Profit Report'], taborder=71)
        self.add('dropdownlistbox', 'ddlb_pe', 3095, 96, 494, 532, text='All', items=['All', 'Purchase Only', 'Exchange Only'], taborder=60)
        self.add('checkbox', 'cbx_ic', 2025, 100, 87, 76)
        self.add('statictext', 'st_20', 1033, 104, 283, 80, text='Incharge')
        self.add('statictext', 'st_5', 2121, 104, 311, 76, text='Rep Type')
        self.add('datawindow', 'dw_1', 261, 184, 425, 84, dataobject='d_supp', taborder=40)
        self.add('datawindow', 'dw_stktype', 1321, 184, 539, 88, dataobject='d_stktypecode', taborder=90)
        self.add('datawindow', 'dw_stoneitem', 2441, 184, 402, 88, dataobject='d_itemstcode', taborder=50)
        self.add('dropdownlistbox', 'ddlb_type2', 3095, 188, 494, 796, text='All', items=['Diamond', 'Platinum', 'Gold', 'Silver', 'Others', 'Color Stone', 'Watch', 'All'], taborder=90)
        self.add('statictext', 'st_4', 5, 192, 251, 76, text='Supplier')
        self.add('statictext', 'st_17', 1033, 192, 283, 76, text='Stk Type')
        self.add('statictext', 'st_8', 2121, 192, 320, 68, text='Stone Type')
        self.add('statictext', 'st_6', 2875, 196, 201, 80, text='Type2 :')
        self.add('commandbutton', 'cb_4', 686, 268, 187, 88, text='&Help', taborder=110)
        self.add('statictext', 'st_3', 5, 272, 251, 84, text='Item')
        self.add('singlelineedit', 'sle_itemcode', 261, 272, 421, 84, limit=10, taborder=120)
        self.add('dropdownlistbox', 'ddlb_type', 2441, 272, 402, 532, text='All', items=['All', 'Ornaments Only', 'Not Ornaments', 'Gold', 'Silver', 'Others'], taborder=80)
        self.add('datawindow', 'dw_counter', 1321, 276, 658, 88, dataobject='d_countercode', taborder=90)
        self.add('statictext', 'st_2', 2121, 276, 279, 76, text='Type :')
        self.add('statictext', 'st_7', 1033, 284, 283, 76, text='Counter')
        self.add('checkbox', 'cbx_speed', 3099, 284, 279, 76, text='Speed')
        self.add('checkbox', 'cbx_counter', 1989, 288, 87, 76)
        self.add('datawindow', 'dw_purhregister', 0, 360, 3607, 1772, dataobject='d_purhregister', taborder=100)
