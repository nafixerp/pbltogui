"""Diamond/Pres.Stone Stock list — w_stocklist_dmdplt.

Generated from the PowerBuilder window ``w_stocklist_dmdplt.srw`` by
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
    name='w_stocklist_dmdplt',
    title='Diamond/Pres.Stone Stock list',
    width=3648,
    height=2268,
    controls=[],
    tables=[],
    source_path='w_stocklist_dmdplt.srw',
    grid={'control': 'dw_1', 'dataobject': 'd_stocklist_dmdplt', 'table': 'items', 'keys': ['code'], 'columns': [{'name': 'name', 'label': 'Item Name', 'type': 'char'}, {'name': 'code', 'label': 'Code', 'type': 'char'}, {'name': 'regionalname', 'label': 'regionalname', 'type': 'char'}, {'name': 'itype', 'label': 'itype', 'type': 'char'}, {'name': 'ornament', 'label': 'ornament', 'type': 'char'}, {'name': 'qty', 'label': 'qty', 'type': 'long'}, {'name': 'weight', 'label': 'weight', 'type': 'decimal'}, {'name': 'stonewgt', 'label': 'stonewgt', 'type': 'decimal'}, {'name': 'qtyb', 'label': 'qtyb', 'type': 'long'}, {'name': 'weightb', 'label': 'weightb', 'type': 'decimal'}, {'name': 'stonewgtb', 'label': 'stonewgtb', 'type': 'decimal'}, {'name': 'cost', 'label': 'cost', 'type': 'decimal'}, {'name': 'grpcode', 'label': 'grpcode', 'type': 'char'}, {'name': 'dmdwgt', 'label': 'dmdwgt', 'type': 'decimal'}, {'name': 'dmdplt', 'label': 'dmdplt', 'type': 'char'}, {'name': 'gwgt', 'label': 'gwgt', 'type': 'long'}, {'name': 'nos', 'label': 'nos', 'type': 'long'}, {'name': 'stwgt', 'label': 'stwgt', 'type': 'decimal'}, {'name': 'tmrp', 'label': 'tmrp', 'type': 'decimal'}, {'name': 'dmdcostamt', 'label': 'dmdcostamt', 'type': 'decimal'}]},
    report={'dataobject': 'd_stocklist_dmdplt', 'sql': "SELECT items.name AS items_name, items.code AS items_code, items.regionalname AS items_regionalname, items.itype AS items_itype, items.ornament AS items_ornament, items.qty AS items_qty, items.weight AS items_weight, items.stonewgt AS items_stonewgt, items.qtyb AS items_qtyb, items.weightb AS items_weightb, items.stonewgtb AS items_stonewgtb, items.cost AS items_cost, items.grpcode AS items_grpcode, items.dmdplt AS items_dmdplt, (select sum(barcode_dmddet.carats) from barcode,barcode_dmddet,items itm where barcode.icode = itm.code and itm.grpcode = ifnull(:rgrp, itm.grpcode, :rgrp) and barcode_dmddet.bcode = barcode.bcode and barcode_dmddet.stcode = items.code and barcode.stk = 'Y' and barcode_dmddet.stcode = ifnull(:ritem, barcode_dmddet.stcode,:ritem) and barcode.tdate >= ifnull(:rdate1, barcode.tdate, :rdate1) and barcode.tdate <= ifnull(:rdate2, barcode.tdate, :rdate2)) as dmdwgt, (0) as gwgt, (select sum(barcode_dmddet.pcs) from barcode,barcode_dmddet,items itm where barcode.icode = itm.code and itm.grpcode = ifnull(:rgrp, itm.grpcode, :rgrp) and  barcode_dmddet.bcode = barcode.bcode and barcode_dmddet.stcode = items.code and barcode.stk = 'Y' and barcode_dmddet.stcode = ifnull(:ritem, barcode_dmddet.stcode,:ritem) and barcode.tdate >= ifnull(:rdate1, barcode.tdate, :rdate1) and barcode.tdate <= ifnull(:rdate2, barcode.tdate, :rdate2) ) as nos, (select sum(barcode.stweight) from barcode where barcode.icode = items.code and items.grpcode = ifnull(:rgrp, items.grpcode, :rgrp) and barcode.stk = 'Y' and barcode.tdate >= ifnull(:rdate1, barcode.tdate, :rdate1) and barcode.tdate <= ifnull(:rdate2, barcode.tdate, :rdate2)) as stwgt, (select sum(barcode_dmddet.carats * barcode_dmddet.rate ) from barcode,barcode_dmddet ,items itm where barcode.icode = itm.code and itm.grpcode = ifnull(:rgrp, itm.grpcode, :rgrp) and barcode_dmddet.bcode = barcode.bcode and barcode_dmddet.stcode = items.code and barcode.stk = 'Y' and barcode_dmddet.stcode = ifnull(:ritem, barcode_dmddet.stcode,:ritem) and barcode.tdate >= ifnull(:rdate1, barcode.tdate, :rdate1) and barcode.tdate <= ifnull(:rdate2, barcode.tdate, :rdate2)) as tmrp, (select sum(barcode_dmddet.pamt) from barcode,barcode_dmddet,items itm where barcode.icode = itm.code and itm.grpcode = ifnull(:rgrp, itm.grpcode, :rgrp) and barcode_dmddet.bcode = barcode.bcode and barcode_dmddet.stcode = items.code and barcode.stk = 'Y' and barcode_dmddet.stcode = ifnull(:ritem, barcode_dmddet.stcode,:ritem) and barcode.tdate >= ifnull(:rdate1, barcode.tdate, :rdate1) and barcode.tdate <= ifnull(:rdate2, barcode.tdate, :rdate2)) as dmdcostamt FROM items ORDER BY items.name ASC", 'args': ['rlevel', 'ritem', 'rdate1', 'rdate2', 'rgrp'], 'arg_types': {'rlevel': 'number', 'ritem': 'string', 'rdate1': 'date', 'rdate2': 'date', 'rgrp': 'string'}, 'tables': ['items'], 'columns': [{'name': 'name', 'label': 'Item Name', 'type': 'char'}, {'name': 'code', 'label': 'Code', 'type': 'char'}, {'name': 'regionalname', 'label': 'regionalname', 'type': 'char'}, {'name': 'itype', 'label': 'itype', 'type': 'char'}, {'name': 'ornament', 'label': 'ornament', 'type': 'char'}, {'name': 'qty', 'label': 'qty', 'type': 'long'}, {'name': 'weight', 'label': 'weight', 'type': 'decimal'}, {'name': 'stonewgt', 'label': 'stonewgt', 'type': 'decimal'}, {'name': 'qtyb', 'label': 'qtyb', 'type': 'long'}, {'name': 'weightb', 'label': 'weightb', 'type': 'decimal'}, {'name': 'stonewgtb', 'label': 'stonewgtb', 'type': 'decimal'}, {'name': 'cost', 'label': 'cost', 'type': 'decimal'}, {'name': 'grpcode', 'label': 'grpcode', 'type': 'char'}, {'name': 'dmdwgt', 'label': 'dmdwgt', 'type': 'decimal'}, {'name': 'dmdplt', 'label': 'dmdplt', 'type': 'char'}, {'name': 'gwgt', 'label': 'gwgt', 'type': 'long'}, {'name': 'nos', 'label': 'nos', 'type': 'long'}, {'name': 'stwgt', 'label': 'stwgt', 'type': 'decimal'}, {'name': 'tmrp', 'label': 'tmrp', 'type': 'decimal'}, {'name': 'dmdcostamt', 'label': 'dmdcostamt', 'type': 'decimal'}]},
)


class DiamondPresStoneStockListForm(GeneratedForm):
    """Diamond/Pres.Stone Stock list"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('commandbutton', 'cb_show', 2542, 0, 251, 100, text='Show', taborder=21)
        self.add('commandbutton', 'cb_saveas', 2802, 0, 251, 100, text='Save &As', taborder=60)
        self.add('commandbutton', 'cb_print', 3063, 0, 251, 100, text='&Print', taborder=70)
        self.add('commandbutton', 'cb_exit', 3323, 0, 251, 100, text='E&xit', taborder=20)
        self.add('dropdownlistbox', 'ddlb_type', 219, 8, 439, 556, text='All', items=['Diamond', 'Platinum', 'Color Stone', 'All'], taborder=40)
        self.add('datawindow', 'dw_stoneitem', 933, 8, 402, 88, dataobject='d_itemstcode', taborder=21)
        self.add('datawindow', 'dw_item', 1605, 8, 402, 88, dataobject='d_itemcode', taborder=50)
        self.add('dropdownlistbox', 'ddlb_reptype', 2016, 8, 398, 496, text='Summary', items=['Summary', 'Details', 'Stone Info'], taborder=60)
        self.add('statictext', 'st_grp', 14, 12, 192, 76, text='Type :')
        self.add('statictext', 'st_1', 672, 16, 256, 64, text='St.Type :')
        self.add('statictext', 'st_2', 1403, 16, 197, 64, text='Item :')
        self.add('editmask', 'em_date1', 219, 104, 439, 92, taborder=60)
        self.add('editmask', 'em_date2', 933, 104, 430, 92, taborder=70)
        self.add('datawindow', 'dw_grp', 1605, 104, 800, 88, dataobject='d_itemgrpcode', taborder=80)
        self.add('statictext', 'st_3', 1376, 108, 224, 76, text='Group :')
        self.add('checkbox', 'cbx_grp', 2409, 112, 78, 76)
        self.add('checkbox', 'cbx_withpresstwgt', 2926, 112, 663, 76, text='With Pres.Stone Wgt Only')
        self.add('statictext', 'st_10', 0, 116, 206, 60, text='From :')
        self.add('statictext', 'st_11', 791, 116, 137, 72, text='To :')
        self.add('checkbox', 'cbx_stockonly', 2542, 116, 343, 72, text='Stock Only')
        self.add('datawindow', 'dw_1', 0, 200, 3579, 1876, dataobject='d_stocklist_dmdplt', taborder=10)
