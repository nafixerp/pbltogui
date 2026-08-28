"""Denomination Master — w_denom_master.

Generated from the PowerBuilder window ``w_denom_master.srw`` by
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
    name='w_denom_master',
    title='Denomination Master',
    width=1509,
    height=2016,
    controls=[],
    tables=['salesm'],
    source_path='w_denom_master.srw',
    grid={'control': 'dw_1', 'dataobject': 'd_denom_master', 'table': 'denom_master', 'keys': ['code'], 'columns': [{'name': 'code', 'label': 'Code', 'type': 'char'}, {'name': 'name', 'label': 'Name', 'type': 'char'}, {'name': 'cvalue', 'label': 'Value', 'type': 'decimal'}]},
    report={'dataobject': 'd_denom_master', 'sql': 'SELECT denom_master.code AS denom_master_code, denom_master.name AS denom_master_name, denom_master.cvalue AS denom_master_cvalue FROM denom_master ORDER BY denom_master.code ASC', 'args': [], 'arg_types': {}, 'tables': ['denom_master'], 'columns': [{'name': 'code', 'label': 'Code', 'type': 'char'}, {'name': 'name', 'label': 'Name', 'type': 'char'}, {'name': 'cvalue', 'label': 'Value', 'type': 'decimal'}]},
)


class DenominationMasterForm(GeneratedForm):
    """Denomination Master"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('datawindow', 'dw_1', 5, 0, 1481, 1788, dataobject='d_denom_master', taborder=10)
        self.add('commandbutton', 'cb_add', 18, 1692, 242, 88, text='&Add', taborder=20)
        self.add('commandbutton', 'cb_delete', 288, 1692, 242, 88, text='&Delete', taborder=30)
        self.add('commandbutton', 'cb_cancel', 297, 1812, 261, 112, text='&Cancel', taborder=40)
        self.add('commandbutton', 'cb_save', 562, 1812, 261, 112, text='&Save', taborder=50)
        self.add('commandbutton', 'cb_exit', 832, 1812, 261, 112, text='E&xit', taborder=60)
