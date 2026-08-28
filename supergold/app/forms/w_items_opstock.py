"""Op.Stock Entry — w_items_opstock.

Generated from the PowerBuilder window ``w_items_opstock.srw`` by
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
    name='w_items_opstock',
    title='Op.Stock Entry',
    width=3657,
    height=2072,
    controls=[],
    tables=['itemsstk', 'items'],
    source_path='w_items_opstock.srw',
    grid={'control': 'dw_itemlist', 'dataobject': 'd_items_opstockentry', 'table': 'items', 'keys': ['code'], 'computes': [{'name': 'grosswgt', 'expression': ' cweight  -  cstwgt ', 'format': '#######0.000', 'label': 'grosswgt', 'band': 'detail'}], 'columns': [{'name': 'code', 'label': 'Code', 'type': 'char'}, {'name': 'name', 'label': 'Name', 'type': 'char'}, {'name': 'itype', 'label': 'itype', 'type': 'char'}, {'name': 'cqty', 'label': 'cqty', 'type': 'long'}, {'name': 'cweight', 'label': 'cweight', 'type': 'decimal'}, {'name': 'cstwgt', 'label': 'cstwgt', 'type': 'decimal'}, {'name': 'stonemarg', 'label': 'stonemarg', 'type': 'decimal'}, {'name': 'cstoneamt', 'label': 'cstoneamt', 'type': 'decimal'}, {'name': 'code2', 'label': 'code2', 'type': 'char'}, {'name': 'touch', 'label': 'touch', 'type': 'decimal'}, {'name': 'grpcode', 'label': 'grpcode', 'type': 'char'}, {'name': 'cdmdwgt', 'label': 'cdmdwgt', 'type': 'decimal'}]},
    report={'dataobject': 'd_items_opstockentry', 'sql': 'SELECT items.code AS items_code, items.name AS items_name, items.itype AS items_itype, items.stonemarg AS items_stonemarg, items.touch AS items_touch, items.grpcode AS items_grpcode, (ifnull( :ropstk, ifnull( :rlevel , ifnull(:rtype, qty, (select sum(itemsstk.qty) from itemsstk where itemsstk.code = items.code and itemsstk.stktype = :rtype)) , ifnull(:rtype, qtyb,(select sum(itemsstk.qtyb) from itemsstk where itemsstk.code = items.code and itemsstk.stktype = :rtype)) ),ifnull(:rlevel , ifnull( :rtype, opqty , (select sum(opqty) from itemsstk where itemsstk.code = items.code and itemsstk.stktype = :rtype)) , ifnull( :rtype, opqtyb , (select sum(opqtyb) from itemsstk where itemsstk.code = items.code and itemsstk.stktype = :rtype)) ))) as cqty, (ifnull( :ropstk, ifnull( :rlevel , ifnull(:rtype, weight, (select sum(itemsstk.weight) from itemsstk where itemsstk.code = items.code and itemsstk.stktype = :rtype)) , ifnull(:rtype, weightb,(select sum(itemsstk.weightb) from itemsstk where itemsstk.code = items.code and itemsstk.stktype = :rtype)) ),ifnull(:rlevel , ifnull( :rtype, opweight , (select sum(opweight) from itemsstk where itemsstk.code = items.code and itemsstk.stktype = :rtype)) , ifnull( :rtype, opweightb , (select sum(opweightb) from itemsstk where itemsstk.code = items.code and itemsstk.stktype = :rtype)) ))) as cweight, (ifnull( :ropstk, ifnull( :rlevel , ifnull(:rtype, stonewgt, (select sum(itemsstk.stonewgt) from itemsstk where itemsstk.code = items.code and itemsstk.stktype = :rtype)) , ifnull(:rtype, stonewgtb,(select sum(itemsstk.stonewgtb) from itemsstk where itemsstk.code = items.code and itemsstk.stktype = :rtype)) ),ifnull(:rlevel , ifnull( :rtype, opstonewgt , (select sum(opstonewgt) from itemsstk where itemsstk.code = items.code and itemsstk.stktype = :rtype)) , ifnull( :rtype, opstonewgtb , (select sum(opstonewgtb) from itemsstk where itemsstk.code = items.code and itemsstk.stktype = :rtype)) ))) as cstwgt, (ifnull( :ropstk, ifnull( :rlevel , ifnull(:rtype, opstoneamt, (select sum(itemsstk.opstoneamt) from itemsstk where itemsstk.code = items.code and itemsstk.stktype = :rtype)) , ifnull(:rtype, opstoneamtb,(select sum(itemsstk.opstoneamtb) from itemsstk where itemsstk.code = items.code and itemsstk.stktype = :rtype)) ),ifnull(:rlevel , ifnull( :rtype, opstoneamt , (select sum(opstoneamt) from itemsstk where itemsstk.code = items.code and itemsstk.stktype = :rtype)) , ifnull( :rtype, opstoneamtb , (select sum(opstoneamtb) from itemsstk where itemsstk.code = items.code and itemsstk.stktype = :rtype)) ))) as cstoneamt, (items.code) as code2, (ifnull( :ropstk, ifnull( :rlevel , ifnull(:rtype, opdmdwgt, (select sum(itemsstk.opdmdwgt) from itemsstk where itemsstk.code = items.code and itemsstk.stktype = :rtype)) , ifnull(:rtype, opdmdwgt,(select sum(itemsstk.opdmdwgt) from itemsstk where itemsstk.code = items.code and itemsstk.stktype = :rtype)) ),ifnull(:rlevel , ifnull( :rtype, opdmdwgt , (select sum(opdmdwgt) from itemsstk where itemsstk.code = items.code and itemsstk.stktype = :rtype)) , ifnull( :rtype, opdmdwgt , (select sum(opdmdwgt) from itemsstk where itemsstk.code = items.code and itemsstk.stktype = :rtype)) ))) as cdmdwgt FROM items ORDER BY items.name ASC, items.code ASC', 'computes': [{'name': 'grosswgt', 'expression': ' cweight  -  cstwgt ', 'format': '#######0.000', 'label': 'grosswgt', 'band': 'detail'}], 'args': ['rlevel', 'ropstk', 'rtype'], 'arg_types': {'rlevel': 'number', 'ropstk': 'string', 'rtype': 'string'}, 'tables': ['items'], 'columns': [{'name': 'code', 'label': 'Code', 'type': 'char'}, {'name': 'name', 'label': 'Name', 'type': 'char'}, {'name': 'itype', 'label': 'itype', 'type': 'char'}, {'name': 'cqty', 'label': 'cqty', 'type': 'long'}, {'name': 'cweight', 'label': 'cweight', 'type': 'decimal'}, {'name': 'cstwgt', 'label': 'cstwgt', 'type': 'decimal'}, {'name': 'stonemarg', 'label': 'stonemarg', 'type': 'decimal'}, {'name': 'cstoneamt', 'label': 'cstoneamt', 'type': 'decimal'}, {'name': 'code2', 'label': 'code2', 'type': 'char'}, {'name': 'touch', 'label': 'touch', 'type': 'decimal'}, {'name': 'grpcode', 'label': 'grpcode', 'type': 'char'}, {'name': 'cdmdwgt', 'label': 'cdmdwgt', 'type': 'decimal'}]},
)


class OpStockEntryForm(GeneratedForm):
    """Op.Stock Entry"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('dropdownlistbox', 'ddlb_stktype', 2368, 0, 599, 340, text='Op.Stock', items=['Op.Stock', 'Cl.Stock'], taborder=80)
        self.add('dropdownlistbox', 'ddlb_itype', 3017, 0, 567, 412, text='All', items=['All', 'Gold Only', 'Silver Only', 'Other Only'], taborder=70)
        self.add('datawindow', 'dw_stktype', 379, 12, 539, 88, dataobject='d_stktypecode', taborder=10)
        self.add('commandbutton', 'cb_show', 942, 12, 224, 92, text='&Show', taborder=20)
        self.add('datawindow', 'dw_grp', 1472, 12, 800, 88, dataobject='d_itemgrpcode', taborder=61)
        self.add('statictext', 'st_1', 0, 16, 366, 76, text='Stock Type :')
        self.add('checkbox', 'cbx_grp', 2281, 16, 78, 76)
        self.add('statictext', 'st_grp', 1211, 20, 247, 76, text='Group :')
        self.add('datawindow', 'dw_itemlist', 5, 124, 3621, 1708, dataobject='d_items_opstockentry', taborder=30)
        self.add('commandbutton', 'cb_updtothers', 1138, 1848, 594, 108, text='&Update Other Det', taborder=60)
        self.add('commandbutton', 'cb_3', 1765, 1848, 306, 108, text='&Update', taborder=50)
        self.add('commandbutton', 'cb_1', 2107, 1848, 311, 108, text='&Print', taborder=40)
        self.add('commandbutton', 'cb_2', 2455, 1848, 311, 108, text='E&xit', taborder=90)
        self.add('checkbox', 'cbx_clstkalso', 443, 1852, 699, 76, text='Update Cl.Stock also')
        self.add('checkbox', 'cbx_samestock', 3003, 1860, 430, 76, text='Same Stock')
