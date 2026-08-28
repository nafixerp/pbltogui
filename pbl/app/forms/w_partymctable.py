"""Party MC Table — w_partymctable.

Generated from the PowerBuilder window ``w_partymctable.srw`` by
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
    name='w_partymctable',
    title='Party MC Table',
    width=3342,
    height=1976,
    controls=[],
    tables=['pmctable', 'clients'],
    source_path='w_partymctable.srw',
    grid={'control': 'dw_party', 'dataobject': 'd_smith', 'table': 'codehelp', 'keys': ['code'], 'columns': [{'name': 'code', 'label': 'code', 'type': 'char'}]},
    report={'dataobject': 'd_partymcmast', 'sql': 'SELECT pmctable.icode AS pmctable_icode, pmctable.model AS pmctable_model, pmctable.wastage AS pmctable_wastage, pmctable.mc AS pmctable_mc, pmctable.mcperc AS pmctable_mcperc, pmctable.mcperqty AS pmctable_mcperqty, pmctable.touch AS pmctable_touch, pmctable.formula AS pmctable_formula FROM pmctable', 'args': ['rpcode'], 'arg_types': {'rpcode': 'string'}, 'tables': ['pmctable'], 'columns': [{'name': 'icode', 'label': 'Item', 'type': 'char'}, {'name': 'model', 'label': 'Model', 'type': 'char'}, {'name': 'wastage', 'label': 'Wstg%', 'type': 'decimal'}, {'name': 'mc', 'label': 'MC /gm', 'type': 'decimal'}, {'name': 'mcperc', 'label': 'MC%', 'type': 'decimal'}, {'name': 'mcperqty', 'label': 'MC /Qty', 'type': 'decimal'}, {'name': 'touch', 'label': 'touch', 'type': 'decimal'}, {'name': 'formula', 'label': 'formula', 'type': 'char'}]},
)


class PartyMcTableForm(GeneratedForm):
    """Party MC Table"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('datawindow', 'dw_party', 297, 12, 439, 92, dataobject='d_smith', taborder=30)
        self.add('commandbutton', 'cb_custhelp', 741, 12, 64, 92, text='^', taborder=40)
        self.add('statictext', 'st_name', 814, 12, 983, 92)
        self.add('statictext', 'st_1', 41, 20, 247, 84, text='Party :')
        self.add('datawindow', 'dw_wstgset', 5, 116, 3301, 1580, dataobject='d_partymcmast', taborder=40)
        self.add('roundrectangle', 'rr_1', 1001, 1720, 1111, 144)
        self.add('commandbutton', 'cb_add', 1029, 1736, 251, 108, text='&Add', taborder=60)
        self.add('commandbutton', 'cb_delete', 1289, 1736, 251, 108, text='&Delete', taborder=70)
        self.add('commandbutton', 'cb_ok', 1563, 1736, 251, 108, text='&Save', taborder=50)
        self.add('commandbutton', 'cb_1', 1829, 1736, 251, 108, text='E&xit', taborder=80)
