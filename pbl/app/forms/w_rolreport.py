"""ReOrderLevel — w_rolreport.

Generated from the PowerBuilder window ``w_rolreport.srw`` by
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
    name='w_rolreport',
    title='ReOrderLevel',
    width=3465,
    height=2268,
    controls=[],
    tables=['items'],
    source_path='w_rolreport.srw',
    grid={'control': 'dw_itemlist', 'dataobject': 'd_rolreport', 'table': 'items', 'keys': ['code'], 'columns': [{'name': 'code', 'label': 'Code', 'type': 'char'}, {'name': 'name', 'label': 'name', 'type': 'char'}, {'name': 'qty', 'label': 'Qty', 'type': 'long'}, {'name': 'weight', 'label': 'Weight', 'type': 'decimal'}, {'name': 'qtyb', 'label': 'qtyb', 'type': 'long'}, {'name': 'weightb', 'label': 'weightb', 'type': 'decimal'}, {'name': 'rollower', 'label': 'rollower', 'type': 'decimal'}, {'name': 'rolupper', 'label': 'rolupper', 'type': 'decimal'}]},
    report={'dataobject': 'd_rolreport', 'sql': 'SELECT items.code AS items_code, items.name AS items_name, items.qty AS items_qty, items.weight AS items_weight, items.qtyb AS items_qtyb, items.weightb AS items_weightb, items.rollower AS items_rollower, items.rolupper AS items_rolupper FROM items ORDER BY items.name ASC', 'args': ['rlevel'], 'arg_types': {'rlevel': 'number'}, 'tables': ['items'], 'columns': [{'name': 'code', 'label': 'Code', 'type': 'char'}, {'name': 'name', 'label': 'name', 'type': 'char'}, {'name': 'qty', 'label': 'Qty', 'type': 'long'}, {'name': 'weight', 'label': 'Weight', 'type': 'decimal'}, {'name': 'qtyb', 'label': 'qtyb', 'type': 'long'}, {'name': 'weightb', 'label': 'weightb', 'type': 'decimal'}, {'name': 'rollower', 'label': 'rollower', 'type': 'decimal'}, {'name': 'rolupper', 'label': 'rolupper', 'type': 'decimal'}]},
)


class ReorderlevelForm(GeneratedForm):
    """ReOrderLevel"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('singlelineedit', 'sle_itemcode', 178, 0, 421, 96, limit=10, taborder=40)
        self.add('commandbutton', 'cb_help', 608, 0, 169, 96, text='&Help', taborder=50)
        self.add('dropdownlistbox', 'ddlb_type', 910, 0, 549, 400, text='All', items=['All', 'Short Only', 'Excess Only'], taborder=60)
        self.add('commandbutton', 'cb_show', 2569, 0, 247, 92, text='Show', taborder=30)
        self.add('commandbutton', 'cb_1', 2907, 0, 247, 92, text='&Print', taborder=30)
        self.add('commandbutton', 'cb_2', 3182, 0, 247, 92, text='E&xit', taborder=20)
        self.add('statictext', 'st_1', 0, 8, 197, 76, text='Item :')
        self.add('checkbox', 'cbx_modelsizebased', 1678, 8, 827, 80, text='Model,Size Based Report')
        self.add('datawindow', 'dw_itemlist', 0, 104, 3438, 1960, dataobject='d_rolreport', taborder=10)
