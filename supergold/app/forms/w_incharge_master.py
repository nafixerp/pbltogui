"""Master — w_incharge_master.

Generated from the PowerBuilder window ``w_incharge_master.srw`` by
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
    name='w_incharge_master',
    title='Master',
    width=1371,
    height=1296,
    controls=[],
    tables=['daybookpart'],
    source_path='w_incharge_master.srw',
    grid={'control': 'dw_places', 'dataobject': 'd_incharge_master', 'table': 'incharge', 'keys': ['code'], 'computes': [], 'columns': [{'name': 'code', 'label': 'Code', 'type': 'char'}, {'name': 'name', 'label': 'Name', 'type': 'char'}]},
    report={'dataobject': 'd_incharge_master', 'sql': 'SELECT incharge.code AS incharge_code, incharge.name AS incharge_name FROM incharge', 'computes': [], 'args': [], 'arg_types': {}, 'tables': ['incharge'], 'columns': [{'name': 'code', 'label': 'Code', 'type': 'char'}, {'name': 'name', 'label': 'Name', 'type': 'char'}]},
)


class MasterForm(GeneratedForm):
    """Master"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('datawindow', 'dw_places', 5, 0, 1349, 1016, dataobject='d_incharge_master', taborder=10)
        self.add('roundrectangle', 'rr_1', 0, 1028, 1358, 164)
        self.add('commandbutton', 'cb_add', 37, 1064, 242, 92, text='&Add', taborder=20)
        self.add('commandbutton', 'cb_delete', 288, 1064, 242, 92, text='&Delete', taborder=30)
        self.add('commandbutton', 'cb_cancel', 571, 1064, 242, 92, text='&Cancel', taborder=40)
        self.add('commandbutton', 'cb_save', 823, 1064, 242, 92, text='&Save', taborder=50)
        self.add('commandbutton', 'cb_exit', 1074, 1064, 242, 92, text='E&xit', taborder=60)
