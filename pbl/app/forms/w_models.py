"""Models — w_models.

Generated from the PowerBuilder window ``w_models.srw`` by
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
    name='w_models',
    title='Models',
    width=1015,
    height=1520,
    controls=[],
    tables=['models', 'pmctable'],
    source_path='w_models.srw',
    report={'dataobject': 'd_models', 'sql': 'SELECT models.name AS models_name FROM models', 'computes': [], 'args': ['rtype'], 'arg_types': {'rtype': 'string'}, 'tables': ['models'], 'columns': [{'name': 'name', 'label': 'Name', 'type': 'char'}]},
)


class ModelsForm(GeneratedForm):
    """Models"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('datawindow', 'dw_sman', 5, 0, 997, 1304, dataobject='d_models', taborder=10)
        self.add('roundrectangle', 'rr_1', 0, 1312, 987, 108)
        self.add('commandbutton', 'cb_add', 23, 1336, 178, 68, text='&Add', taborder=20)
        self.add('commandbutton', 'cb_delete', 210, 1336, 178, 68, text='&Delete', taborder=30)
        self.add('commandbutton', 'cb_cancel', 407, 1336, 178, 68, text='&Cancel', taborder=40)
        self.add('commandbutton', 'cb_save', 603, 1336, 178, 68, text='&Save', taborder=50)
        self.add('commandbutton', 'cb_exit', 786, 1336, 178, 68, text='E&xit', taborder=60)
