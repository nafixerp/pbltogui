"""Bill Type — w_salestype.

Generated from the PowerBuilder window ``w_salestype.srw`` by
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
    name='w_salestype',
    title='Bill Type',
    width=3703,
    height=1312,
    controls=[],
    tables=['salestype', 'salesm', 'generali'],
    source_path='w_salestype.srw',
    grid={'control': 'dw_1', 'dataobject': 'd_salestype', 'table': 'salestype', 'keys': ['code'], 'computes': [], 'columns': [{'name': 'code', 'label': 'Code', 'type': 'char'}, {'name': 'name', 'label': 'Name', 'type': 'char'}, {'name': 'taxperc', 'label': 'Tax%', 'type': 'decimal'}, {'name': 'formno', 'label': 'Form No', 'type': 'char'}, {'name': 'prefix', 'label': 'SPrefix', 'type': 'char'}, {'name': 'startno', 'label': 'SStartNo', 'type': 'long'}, {'name': 'srprefix', 'label': 'SR Prefix', 'type': 'char'}, {'name': 'srstartno', 'label': 'SR Start No', 'type': 'long'}, {'name': 'pprefix', 'label': 'PPrefix', 'type': 'char'}, {'name': 'pstartno', 'label': 'PStartNo', 'type': 'long'}, {'name': 'prprefix', 'label': 'PR Prefix', 'type': 'char'}, {'name': 'prstartno', 'label': 'PR Start No', 'type': 'long'}]},
    report={'dataobject': 'd_salestype', 'sql': 'SELECT salestype.code AS salestype_code, salestype.name AS salestype_name, salestype.taxperc AS salestype_taxperc, salestype.formno AS salestype_formno, salestype.prefix AS salestype_prefix, salestype.startno AS salestype_startno, salestype.srprefix AS salestype_srprefix, salestype.srstartno AS salestype_srstartno, salestype.pprefix AS salestype_pprefix, salestype.pstartno AS salestype_pstartno, salestype.prprefix AS salestype_prprefix, salestype.prstartno AS salestype_prstartno FROM salestype', 'computes': [], 'args': [], 'arg_types': {}, 'tables': ['salestype'], 'columns': [{'name': 'code', 'label': 'Code', 'type': 'char'}, {'name': 'name', 'label': 'Name', 'type': 'char'}, {'name': 'taxperc', 'label': 'Tax%', 'type': 'decimal'}, {'name': 'formno', 'label': 'Form No', 'type': 'char'}, {'name': 'prefix', 'label': 'SPrefix', 'type': 'char'}, {'name': 'startno', 'label': 'SStartNo', 'type': 'long'}, {'name': 'srprefix', 'label': 'SR Prefix', 'type': 'char'}, {'name': 'srstartno', 'label': 'SR Start No', 'type': 'long'}, {'name': 'pprefix', 'label': 'PPrefix', 'type': 'char'}, {'name': 'pstartno', 'label': 'PStartNo', 'type': 'long'}, {'name': 'prprefix', 'label': 'PR Prefix', 'type': 'char'}, {'name': 'prstartno', 'label': 'PR Start No', 'type': 'long'}]},
)


class BillTypeForm(GeneratedForm):
    """Bill Type"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('datawindow', 'dw_1', 5, 0, 3675, 1016, dataobject='d_salestype', taborder=10)
        self.add('roundrectangle', 'rr_1', 1243, 1036, 1358, 164)
        self.add('commandbutton', 'cb_add', 1280, 1072, 242, 92, text='&Add', taborder=20)
        self.add('commandbutton', 'cb_delete', 1531, 1072, 242, 92, text='&Delete', taborder=30)
        self.add('commandbutton', 'cb_cancel', 1815, 1072, 242, 92, text='&Cancel', taborder=40)
        self.add('commandbutton', 'cb_save', 2066, 1072, 242, 92, text='&Save', taborder=50)
        self.add('commandbutton', 'cb_exit', 2318, 1072, 242, 92, text='E&xit', taborder=60)
