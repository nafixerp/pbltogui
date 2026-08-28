"""Sales Man — w_sman.

Generated from the PowerBuilder window ``w_sman.srw`` by
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
    name='w_sman',
    title='Sales Man',
    width=2089,
    height=1296,
    controls=[],
    tables=['sman', 'orderm'],
    source_path='w_sman.srw',
    grid={'control': 'dw_sman', 'dataobject': 'd_sman', 'table': 'sman', 'keys': ['code'], 'columns': [{'name': 'code', 'label': 'Code', 'type': 'char'}, {'name': 'name', 'label': 'Name', 'type': 'char'}, {'name': 'accode', 'label': 'accode', 'type': 'char'}, {'name': 'active', 'label': 'active', 'type': 'char'}]},
    report={'dataobject': 'd_sman', 'sql': 'SELECT sman.code AS sman_code, sman.name AS sman_name, sman.accode AS sman_accode, sman.active AS sman_active FROM sman', 'args': [], 'arg_types': {}, 'tables': ['sman'], 'columns': [{'name': 'code', 'label': 'Code', 'type': 'char'}, {'name': 'name', 'label': 'Name', 'type': 'char'}, {'name': 'accode', 'label': 'accode', 'type': 'char'}, {'name': 'active', 'label': 'active', 'type': 'char'}]},
)


class SalesManForm(GeneratedForm):
    """Sales Man"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('datawindow', 'dw_sman', 5, 0, 2057, 1016, dataobject='d_sman', taborder=10)
        self.add('roundrectangle', 'rr_1', 210, 1024, 1358, 164)
        self.add('commandbutton', 'cb_add', 247, 1060, 242, 92, text='&Add', taborder=20)
        self.add('commandbutton', 'cb_delete', 498, 1060, 242, 92, text='&Delete', taborder=30)
        self.add('commandbutton', 'cb_cancel', 782, 1060, 242, 92, text='&Cancel', taborder=40)
        self.add('commandbutton', 'cb_save', 1033, 1060, 242, 92, text='&Save', taborder=50)
        self.add('commandbutton', 'cb_exit', 1285, 1060, 242, 92, text='E&xit', taborder=60)
