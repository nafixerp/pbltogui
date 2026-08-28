"""ReOrder Level Table — w_reorder_master.

Generated from the PowerBuilder window ``w_reorder_master.srw`` by
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
    name='w_reorder_master',
    title='ReOrder Level Table',
    width=2245,
    height=1764,
    controls=[],
    tables=['models', 'rotable', 'items'],
    source_path='w_reorder_master.srw',
    grid={'control': 'dw_wstgset', 'dataobject': 'd_rotable', 'table': 'rotable', 'keys': ['code', 'model', 'size', 'weight1', 'weight2'], 'columns': [{'name': 'code', 'label': 'code', 'type': 'char'}, {'name': 'model', 'label': 'Model', 'type': 'char'}, {'name': 'size', 'label': 'Size', 'type': 'char'}, {'name': 'weight1', 'label': 'Min Wgt', 'type': 'decimal'}, {'name': 'weight2', 'label': 'Max Wgt', 'type': 'decimal'}, {'name': 'minqty', 'label': 'Min Qty', 'type': 'long'}, {'name': 'maxqty', 'label': 'Max Qty', 'type': 'long'}]},
    report={'dataobject': 'd_rotable', 'sql': 'SELECT rotable.code AS rotable_code, rotable.model AS rotable_model, rotable.size AS rotable_size, rotable.weight1 AS rotable_weight1, rotable.weight2 AS rotable_weight2, rotable.minqty AS rotable_minqty, rotable.maxqty AS rotable_maxqty FROM rotable ORDER BY rotable.model ASC, rotable.size ASC, rotable.weight1 ASC, rotable.weight2 ASC', 'args': ['rcode'], 'arg_types': {'rcode': 'string'}, 'tables': ['rotable'], 'columns': [{'name': 'code', 'label': 'code', 'type': 'char'}, {'name': 'model', 'label': 'Model', 'type': 'char'}, {'name': 'size', 'label': 'Size', 'type': 'char'}, {'name': 'weight1', 'label': 'Min Wgt', 'type': 'decimal'}, {'name': 'weight2', 'label': 'Max Wgt', 'type': 'decimal'}, {'name': 'minqty', 'label': 'Min Qty', 'type': 'long'}, {'name': 'maxqty', 'label': 'Max Qty', 'type': 'long'}]},
    opens=['w_itemhelp'],
)


class ReorderLevelTableForm(GeneratedForm):
    """ReOrder Level Table"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('singlelineedit', 'sle_itemcode', 215, 8, 421, 96, limit=10, taborder=10)
        self.add('commandbutton', 'cb_help', 645, 8, 169, 96, text='&Help')
        self.add('statictext', 'st_name', 818, 8, 1147, 96)
        self.add('commandbutton', 'cb_show', 1984, 8, 229, 96, text='Show', taborder=20)
        self.add('statictext', 'st_1', 37, 16, 197, 76, text='Item :')
        self.add('datawindow', 'dw_wstgset', 18, 116, 2199, 1356, dataobject='d_rotable', taborder=40)
        self.add('roundrectangle', 'rr_1', 489, 1488, 1125, 184)
        self.add('commandbutton', 'cb_delall', 14, 1516, 439, 116, text='Del All of this item', taborder=31)
        self.add('commandbutton', 'cb_add', 517, 1524, 251, 108, text='&Add', taborder=60)
        self.add('commandbutton', 'cb_delete', 777, 1524, 251, 108, text='&Delete', taborder=70)
        self.add('commandbutton', 'cb_ok', 1051, 1524, 251, 108, text='&Save', taborder=50)
        self.add('commandbutton', 'cb_1', 1317, 1524, 251, 108, text='E&xit', taborder=80)
