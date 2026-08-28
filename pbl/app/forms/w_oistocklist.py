"""Stock List — w_oistocklist.

Generated from the PowerBuilder window ``w_oistocklist.srw`` by
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
    name='w_oistocklist',
    title='Stock List',
    width=3621,
    height=2252,
    controls=[],
    tables=[],
    source_path='w_oistocklist.srw',
    grid={'control': 'dw_1', 'dataobject': 'd_oistocklist', 'table': 'itemsothers', 'keys': ['code'], 'computes': [{'name': 'val', 'expression': ' stock  *  cost ', 'format': '########0.00', 'label': 'val', 'band': 'detail'}, {'name': 'compute_2', 'expression': 'sum(val  for all)', 'format': '########0.00', 'label': 'compute_2', 'band': 'summary'}], 'columns': [{'name': 'code', 'label': 'Code', 'type': 'char'}, {'name': 'name', 'label': 'Item Name', 'type': 'char'}, {'name': 'stock', 'label': 'stock', 'type': 'long'}, {'name': 'grp', 'label': 'grp', 'type': 'char'}, {'name': 'keepstk', 'label': 'keepstk', 'type': 'long'}, {'name': 'cost', 'label': 'cost', 'type': 'decimal'}]},
    report={'dataobject': 'd_oistocklist', 'sql': 'SELECT itemsothers.code AS itemsothers_code, itemsothers.name AS itemsothers_name, itemsothers.stock AS itemsothers_stock, itemsothers.grp AS itemsothers_grp, itemsothers.keepstk AS itemsothers_keepstk, itemsothers.cost AS itemsothers_cost FROM itemsothers ORDER BY itemsothers.name ASC', 'computes': [{'name': 'val', 'expression': ' stock  *  cost ', 'format': '########0.00', 'label': 'val', 'band': 'detail'}, {'name': 'compute_2', 'expression': 'sum(val  for all)', 'format': '########0.00', 'label': 'compute_2', 'band': 'summary'}], 'args': ['rlevel'], 'arg_types': {'rlevel': 'number'}, 'tables': ['itemsothers'], 'columns': [{'name': 'code', 'label': 'Code', 'type': 'char'}, {'name': 'name', 'label': 'Item Name', 'type': 'char'}, {'name': 'stock', 'label': 'stock', 'type': 'long'}, {'name': 'grp', 'label': 'grp', 'type': 'char'}, {'name': 'keepstk', 'label': 'keepstk', 'type': 'long'}, {'name': 'cost', 'label': 'cost', 'type': 'decimal'}]},
)


class StockListForm(GeneratedForm):
    """Stock List"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('commandbutton', 'cb_saveas', 2757, 0, 279, 100, text='Save &As', taborder=50)
        self.add('commandbutton', 'cb_print', 3049, 0, 265, 100, text='&Print', taborder=60)
        self.add('commandbutton', 'cb_exit', 3328, 0, 265, 100, text='E&xit', taborder=30)
        self.add('dropdownlistbox', 'ddlb_type3', 1353, 4, 791, 556, text='With Not Zero Stock', items=['All', 'With Stock Only', 'With -ve Stock', 'With Zero Stock', 'With Not Zero Stock'], taborder=20)
        self.add('datawindow', 'dw_grp', 311, 8, 805, 92, dataobject='d_itemgrpcode', taborder=40)
        self.add('checkbox', 'cbx_grp', 1120, 16, 78, 76)
        self.add('statictext', 'st_grp', 50, 20, 247, 76, text='Group :')
        self.add('datawindow', 'dw_1', 0, 108, 3579, 1952, dataobject='d_oistocklist', taborder=10)
        self.add('checkbox', 'cbx_speed', 3127, 112, 425, 76, text='Speed Print')
