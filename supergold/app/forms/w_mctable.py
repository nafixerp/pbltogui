"""MC Table — w_mctable.

Generated from the PowerBuilder window ``w_mctable.srw`` by
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
    name='w_mctable',
    title='MC Table',
    width=2245,
    height=1764,
    controls=[],
    tables=['mctable', 'items'],
    source_path='w_mctable.srw',
    report={'dataobject': 'd_mcmast', 'sql': 'SELECT mctable.weight1 AS mctable_weight1, mctable.weight2 AS mctable_weight2, mctable.mc AS mctable_mc, mctable.mcpergm AS mctable_mcpergm, mctable.mcperqty AS mctable_mcperqty, mctable.vaperc AS mctable_vaperc FROM mctable', 'computes': [], 'args': ['rcode', 'rtype'], 'arg_types': {'rcode': 'string', 'rtype': 'string'}, 'tables': ['mctable'], 'columns': [{'name': 'weight1', 'label': 'From Wgt', 'type': 'decimal'}, {'name': 'weight2', 'label': 'To Wgt', 'type': 'decimal'}, {'name': 'mc', 'label': 'mc', 'type': 'decimal'}, {'name': 'mcpergm', 'label': 'mcpergm', 'type': 'decimal'}, {'name': 'mcperqty', 'label': 'mcperqty', 'type': 'decimal'}, {'name': 'vaperc', 'label': 'vaperc', 'type': 'decimal'}]},
    opens=['w_itemhelp'],
)


class McTableForm(GeneratedForm):
    """MC Table"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('datawindow', 'dw_type', 1262, 4, 443, 88, dataobject='d_itemqtypecode', taborder=30)
        self.add('singlelineedit', 'sle_itemcode', 311, 8, 421, 96, limit=10, taborder=10)
        self.add('commandbutton', 'cb_show', 1737, 8, 229, 84, text='Show', taborder=20)
        self.add('statictext', 'st_1', 46, 12, 247, 76, text='Item :')
        self.add('commandbutton', 'cb_help', 741, 12, 169, 84, text='&Help')
        self.add('statictext', 'st_2', 1001, 12, 247, 76, text='Type :')
        self.add('datawindow', 'dw_wstgset', 18, 116, 2199, 1356, dataobject='d_mcmast', taborder=40)
        self.add('roundrectangle', 'rr_1', 489, 1488, 1125, 184)
        self.add('commandbutton', 'cb_delall', 14, 1516, 439, 116, text='Del All of this item', taborder=31)
        self.add('commandbutton', 'cb_add', 517, 1524, 251, 108, text='&Add', taborder=60)
        self.add('commandbutton', 'cb_delete', 777, 1524, 251, 108, text='&Delete', taborder=70)
        self.add('commandbutton', 'cb_ok', 1051, 1524, 251, 108, text='&Save', taborder=50)
        self.add('commandbutton', 'cb_1', 1317, 1524, 251, 108, text='E&xit', taborder=80)
