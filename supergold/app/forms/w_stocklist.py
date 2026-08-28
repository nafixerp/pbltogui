"""Items — w_stocklist.

Generated from the PowerBuilder window ``w_stocklist.srw`` by
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
    name='w_stocklist',
    title='Items',
    width=3621,
    height=2252,
    controls=[],
    tables=['items', 'userd'],
    source_path='w_stocklist.srw',
    grid={'control': 'dw_1', 'dataobject': 'd_stocklistreport1', 'table': 'items', 'keys': ['code'], 'computes': [{'name': 'cqty', 'expression': 'if(rlevel=1,qty,qtyB)', 'format': '#####0', 'label': 'cqty', 'band': 'detail'}, {'name': 'cwgt', 'expression': 'if(rlevel=1,weight,weightb)', 'format': '######0.000', 'label': 'cwgt', 'band': 'detail'}, {'name': 'cstwgt', 'expression': 'if(rlevel=1,stonewgt,stonewgtb)', 'format': '####0.000', 'label': 'cstwgt', 'band': 'detail'}, {'name': 'netwgt', 'expression': ' cwgt  -  cstwgt ', 'format': '######0.000', 'label': 'netwgt', 'band': 'detail'}, {'name': 'ccost', 'expression': "if(rval = 'C', cost ,crate )", 'format': '[General]', 'label': 'ccost', 'band': 'detail'}, {'name': 'cvalue', 'expression': 'netwgt * ccost', 'format': '#######0.00', 'label': 'cvalue', 'band': 'detail'}, {'name': 'compute_4', 'expression': 'count(code for all)', 'format': '#####0', 'label': 'compute_4', 'band': 'summary'}, {'name': 'tqty1', 'expression': "sum( if(itype='G',cqty,0) for all)", 'format': '#####0', 'label': 'tqty1', 'band': 'summary'}, {'name': 'twgt1', 'expression': "sum( if(itype='G',cwgt,0) for all)", 'format': '######0.000', 'label': 'twgt1', 'band': 'summary'}, {'name': 'tstwgt1', 'expression': 'sum(if(rlevel=1,stonewgt,stonewgtb) for all)', 'format': '####0.000', 'label': 'tstwgt1', 'band': 'summary'}, {'name': 'tnetwgt1', 'expression': "sum( if(itype='G', netwgt,0) for all)", 'format': '######0.000', 'label': 'tnetwgt1', 'band': 'summary'}, {'name': 'tval1', 'expression': "sum( if(itype = 'G', cvalue,0) for all)", 'format': '#######0.00', 'label': 'tval1', 'band': 'summary'}, {'name': 'tqty2', 'expression': "sum( if(itype='S',cqty,0) for all)", 'format': '#####0', 'label': 'tqty2', 'band': 'summary'}, {'name': 'twgt2', 'expression': "sum( if(itype='S',cwgt,0) for all)", 'format': '######0.000', 'label': 'twgt2', 'band': 'summary'}, {'name': 'tval2', 'expression': "sum( if(itype = 'S', cvalue,0) for all)", 'format': '#######0.00', 'label': 'tval2', 'band': 'summary'}, {'name': 'tqty3', 'expression': "sum( if(itype='O',cqty,0) for all)", 'format': '#####0', 'label': 'tqty3', 'band': 'summary'}, {'name': 'twgt3', 'expression': "sum( if(itype='O',cwgt,0) for all)", 'format': '######0.000', 'label': 'twgt3', 'band': 'summary'}, {'name': 'tval3', 'expression': "sum( if(itype = 'O', cvalue,0) for all)", 'format': '#######0.00', 'label': 'tval3', 'band': 'summary'}], 'columns': [{'name': 'name', 'label': 'Item Name', 'type': 'char'}, {'name': 'code', 'label': 'Code', 'type': 'char'}, {'name': 'regionalname', 'label': 'regionalname', 'type': 'char'}, {'name': 'itype', 'label': 'itype', 'type': 'char'}, {'name': 'ornament', 'label': 'ornament', 'type': 'char'}, {'name': 'qty', 'label': 'qty', 'type': 'long'}, {'name': 'weight', 'label': 'weight', 'type': 'decimal'}, {'name': 'stonewgt', 'label': 'St.Wgt.', 'type': 'decimal'}, {'name': 'qtyb', 'label': 'qtyb', 'type': 'long'}, {'name': 'weightb', 'label': 'weightb', 'type': 'decimal'}, {'name': 'stonewgtb', 'label': 'stonewgtb', 'type': 'decimal'}, {'name': 'cost', 'label': 'Rate', 'type': 'decimal'}, {'name': 'grpcode', 'label': 'grpcode', 'type': 'char'}, {'name': 'crate', 'label': 'crate', 'type': 'decimal'}]},
    report={'dataobject': 'd_stocklistreport1', 'sql': 'SELECT items.name AS items_name, items.code AS items_code, items.regionalname AS items_regionalname, items.itype AS items_itype, items.ornament AS items_ornament, items.qty AS items_qty, items.weight AS items_weight, items.stonewgt AS items_stonewgt, items.qtyb AS items_qtyb, items.weightb AS items_weightb, items.stonewgtb AS items_stonewgtb, items.cost AS items_cost, items.grpcode AS items_grpcode, items.crate AS items_crate FROM items ORDER BY items.name ASC', 'computes': [{'name': 'cqty', 'expression': 'if(rlevel=1,qty,qtyB)', 'format': '#####0', 'label': 'cqty', 'band': 'detail'}, {'name': 'cwgt', 'expression': 'if(rlevel=1,weight,weightb)', 'format': '######0.000', 'label': 'cwgt', 'band': 'detail'}, {'name': 'cstwgt', 'expression': 'if(rlevel=1,stonewgt,stonewgtb)', 'format': '####0.000', 'label': 'cstwgt', 'band': 'detail'}, {'name': 'netwgt', 'expression': ' cwgt  -  cstwgt ', 'format': '######0.000', 'label': 'netwgt', 'band': 'detail'}, {'name': 'ccost', 'expression': "if(rval = 'C', cost ,crate )", 'format': '[General]', 'label': 'ccost', 'band': 'detail'}, {'name': 'cvalue', 'expression': 'netwgt * ccost', 'format': '#######0.00', 'label': 'cvalue', 'band': 'detail'}, {'name': 'compute_4', 'expression': 'count(code for all)', 'format': '#####0', 'label': 'compute_4', 'band': 'summary'}, {'name': 'tqty1', 'expression': "sum( if(itype='G',cqty,0) for all)", 'format': '#####0', 'label': 'tqty1', 'band': 'summary'}, {'name': 'twgt1', 'expression': "sum( if(itype='G',cwgt,0) for all)", 'format': '######0.000', 'label': 'twgt1', 'band': 'summary'}, {'name': 'tstwgt1', 'expression': 'sum(if(rlevel=1,stonewgt,stonewgtb) for all)', 'format': '####0.000', 'label': 'tstwgt1', 'band': 'summary'}, {'name': 'tnetwgt1', 'expression': "sum( if(itype='G', netwgt,0) for all)", 'format': '######0.000', 'label': 'tnetwgt1', 'band': 'summary'}, {'name': 'tval1', 'expression': "sum( if(itype = 'G', cvalue,0) for all)", 'format': '#######0.00', 'label': 'tval1', 'band': 'summary'}, {'name': 'tqty2', 'expression': "sum( if(itype='S',cqty,0) for all)", 'format': '#####0', 'label': 'tqty2', 'band': 'summary'}, {'name': 'twgt2', 'expression': "sum( if(itype='S',cwgt,0) for all)", 'format': '######0.000', 'label': 'twgt2', 'band': 'summary'}, {'name': 'tval2', 'expression': "sum( if(itype = 'S', cvalue,0) for all)", 'format': '#######0.00', 'label': 'tval2', 'band': 'summary'}, {'name': 'tqty3', 'expression': "sum( if(itype='O',cqty,0) for all)", 'format': '#####0', 'label': 'tqty3', 'band': 'summary'}, {'name': 'twgt3', 'expression': "sum( if(itype='O',cwgt,0) for all)", 'format': '######0.000', 'label': 'twgt3', 'band': 'summary'}, {'name': 'tval3', 'expression': "sum( if(itype = 'O', cvalue,0) for all)", 'format': '#######0.00', 'label': 'tval3', 'band': 'summary'}], 'args': ['rlevel', 'rval'], 'arg_types': {'rlevel': 'number', 'rval': 'string'}, 'tables': ['items'], 'columns': [{'name': 'name', 'label': 'Item Name', 'type': 'char'}, {'name': 'code', 'label': 'Code', 'type': 'char'}, {'name': 'regionalname', 'label': 'regionalname', 'type': 'char'}, {'name': 'itype', 'label': 'itype', 'type': 'char'}, {'name': 'ornament', 'label': 'ornament', 'type': 'char'}, {'name': 'qty', 'label': 'qty', 'type': 'long'}, {'name': 'weight', 'label': 'weight', 'type': 'decimal'}, {'name': 'stonewgt', 'label': 'St.Wgt.', 'type': 'decimal'}, {'name': 'qtyb', 'label': 'qtyb', 'type': 'long'}, {'name': 'weightb', 'label': 'weightb', 'type': 'decimal'}, {'name': 'stonewgtb', 'label': 'stonewgtb', 'type': 'decimal'}, {'name': 'cost', 'label': 'Rate', 'type': 'decimal'}, {'name': 'grpcode', 'label': 'grpcode', 'type': 'char'}, {'name': 'crate', 'label': 'crate', 'type': 'decimal'}]},
    opens=['w_stocklist_popup', 'w_itemhistory', 'w_item'],
)


class ItemsForm(GeneratedForm):
    """Items"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('checkbox', 'cbx_nowgt', 2080, 0, 329, 76, text='No Wgt')
        self.add('commandbutton', 'cb_3', 2775, 0, 279, 100, text='Save &As', taborder=60)
        self.add('commandbutton', 'cb_1', 3058, 0, 265, 100, text='&Print', taborder=70)
        self.add('commandbutton', 'cb_2', 3328, 0, 265, 100, text='E&xit', taborder=20)
        self.add('dropdownlistbox', 'ddlb_type2', 1440, 4, 603, 556, text='All', items=['All', 'Gold', 'Platinum', 'Silver', 'Others'], taborder=40)
        self.add('checkbox', 'cbx_nototal', 2427, 4, 325, 76, text='No Total')
        self.add('datawindow', 'dw_grp', 311, 8, 800, 88, dataobject='d_itemgrpcode', taborder=50)
        self.add('statictext', 'st_grp', 50, 12, 247, 76, text='Group :')
        self.add('statictext', 'st_1', 1207, 12, 215, 76, text='Type :')
        self.add('checkbox', 'cbx_grp', 1120, 16, 78, 76)
        self.add('dropdownlistbox', 'ddlb_type3', 311, 100, 800, 556, text='With Not Zero Stock', items=['All', 'With Stock Only', 'With -ve Stock', 'With Zero Stock', 'With Not Zero Stock'], taborder=11)
        self.add('dropdownlistbox', 'ddlb_type', 1440, 100, 603, 556, text='All', items=['All', 'Ornaments Only', 'Not Ornaments'], taborder=30)
        self.add('checkbox', 'cbx_1', 2080, 112, 466, 76, text='To Std Touch')
        self.add('checkbox', 'cbx_speed', 3127, 112, 425, 76, text='Speed Print')
        self.add('checkbox', 'cbx_stkverify', 2638, 116, 430, 72, text='Stock Verify')
        self.add('datawindow', 'dw_1', 0, 200, 3579, 1952, dataobject='d_stocklistreport1', taborder=10)
        self.add('checkbox', 'cbx_costval', 2638, 216, 402, 64, text='Cost Value')
        self.add('checkbox', 'cbx_sortoncode', 2080, 220, 434, 72, text='Sort On Code')
