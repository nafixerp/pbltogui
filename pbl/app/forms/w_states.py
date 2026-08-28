"""States/Emirates — w_states.

Generated from the PowerBuilder window ``w_states.srw`` by
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
    name='w_states',
    title='States/Emirates',
    width=1545,
    height=1296,
    controls=[],
    tables=['salesm'],
    source_path='w_states.srw',
    grid={'control': 'dw_group', 'dataobject': 'd_state_master', 'table': 'state', 'keys': ['code'], 'computes': [], 'columns': [{'name': 'code', 'label': 'Code', 'type': 'char'}, {'name': 'name', 'label': 'Name', 'type': 'char'}]},
    report={'dataobject': 'd_state_master', 'sql': 'SELECT state.code AS state_code, state.name AS state_name FROM state', 'computes': [], 'args': [], 'arg_types': {}, 'tables': ['state'], 'columns': [{'name': 'code', 'label': 'Code', 'type': 'char'}, {'name': 'name', 'label': 'Name', 'type': 'char'}]},
)


class StatesEmiratesForm(GeneratedForm):
    """States/Emirates"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('datawindow', 'dw_group', 5, 0, 1513, 1016, dataobject='d_state_master', taborder=10)
        self.add('roundrectangle', 'rr_1', 192, 1048, 1138, 132)
        self.add('commandbutton', 'cb_add', 210, 1064, 197, 92, text='&Add', taborder=20)
        self.add('commandbutton', 'cb_delete', 416, 1064, 197, 92, text='&Delete', taborder=30)
        self.add('commandbutton', 'cb_cancel', 640, 1064, 210, 92, text='&Cancel', taborder=40)
        self.add('commandbutton', 'cb_save', 878, 1064, 210, 92, text='&Save', taborder=50)
        self.add('commandbutton', 'cb_exit', 1097, 1064, 210, 92, text='E&xit', taborder=60)
