"""Smith Suspense Entry — w_gsmithsuspense.

Generated from the PowerBuilder window ``w_gsmithsuspense.srw`` by
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
    name='w_gsmithsuspense',
    title='Smith Suspense Entry',
    width=3657,
    height=1768,
    controls=[],
    tables=['items', 'clients', 'smithsusp'],
    source_path='w_gsmithsuspense.srw',
    grid={'control': 'dw_ruffwork', 'dataobject': 'd_gsmithsuspense', 'table': 'smithsusp', 'keys': ['sno'], 'columns': [{'name': 'tdate', 'label': 'Date', 'type': 'date'}, {'name': 'smithcode', 'label': 'Smith', 'type': 'char'}, {'name': 'smithname', 'label': 'Name', 'type': 'char'}, {'name': 'icode', 'label': 'Item', 'type': 'char'}, {'name': 'iname', 'label': 'Item Name', 'type': 'char'}, {'name': 'qty', 'label': 'Qty', 'type': 'long'}, {'name': 'weight', 'label': 'Weight', 'type': 'decimal'}, {'name': 'ttype', 'label': 'ttype', 'type': 'char'}, {'name': 'part', 'label': 'Particulars', 'type': 'char'}, {'name': 'sno', 'label': 'sno', 'type': 'long'}]},
    report={'dataobject': 'd_gsmithsuspense', 'sql': 'SELECT smithsusp.tdate AS smithsusp_tdate, smithsusp.smithcode AS smithsusp_smithcode, smithsusp.smithname AS smithsusp_smithname, smithsusp.icode AS smithsusp_icode, smithsusp.iname AS smithsusp_iname, smithsusp.qty AS smithsusp_qty, smithsusp.weight AS smithsusp_weight, smithsusp.ttype AS smithsusp_ttype, smithsusp.part AS smithsusp_part, smithsusp.sno AS smithsusp_sno FROM smithsusp', 'args': [], 'arg_types': {}, 'tables': ['smithsusp'], 'columns': [{'name': 'tdate', 'label': 'Date', 'type': 'date'}, {'name': 'smithcode', 'label': 'Smith', 'type': 'char'}, {'name': 'smithname', 'label': 'Name', 'type': 'char'}, {'name': 'icode', 'label': 'Item', 'type': 'char'}, {'name': 'iname', 'label': 'Item Name', 'type': 'char'}, {'name': 'qty', 'label': 'Qty', 'type': 'long'}, {'name': 'weight', 'label': 'Weight', 'type': 'decimal'}, {'name': 'ttype', 'label': 'ttype', 'type': 'char'}, {'name': 'part', 'label': 'Particulars', 'type': 'char'}, {'name': 'sno', 'label': 'sno', 'type': 'long'}]},
    opens=['w_itemhelp', 'w_clientshelp'],
)


class SmithSuspenseEntryForm(GeneratedForm):
    """Smith Suspense Entry"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('datawindow', 'dw_ruffwork', 0, 4, 3634, 1448, dataobject='d_gsmithsuspense', taborder=30)
        self.add('roundrectangle', 'rr_1', 686, 1468, 2281, 176)
        self.add('commandbutton', 'cb_add', 750, 1504, 242, 100, text='&Add', taborder=70)
        self.add('commandbutton', 'cb_delete', 1001, 1504, 242, 100, text='&Delete', taborder=10)
        self.add('commandbutton', 'cb_print', 1303, 1504, 242, 100, text='&Print', taborder=60)
        self.add('commandbutton', 'cb_cancel', 2149, 1504, 242, 100, text='&Cancel', taborder=20)
        self.add('commandbutton', 'cb_save', 2400, 1504, 242, 100, text='&Save', taborder=40)
        self.add('commandbutton', 'cb_exit', 2693, 1504, 242, 100, text='E&xit', taborder=50)
