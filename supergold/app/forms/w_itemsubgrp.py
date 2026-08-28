"""Sub Groups — w_itemsubgrp.

Generated from the PowerBuilder window ``w_itemsubgrp.srw`` by
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
    name='w_itemsubgrp',
    title='Sub Groups',
    width=1760,
    height=1320,
    controls=[],
    tables=['barcode'],
    source_path='w_itemsubgrp.srw',
    grid={'control': 'dw_sman', 'dataobject': 'd_itemsubgrpmaster', 'table': 'itemsubgrp', 'keys': ['code'], 'computes': [], 'columns': [{'name': 'code', 'label': 'Code', 'type': 'char'}, {'name': 'name', 'label': 'Name', 'type': 'char'}]},
    report={'dataobject': 'd_itemsubgrpmaster', 'sql': 'SELECT itemsubgrp.code AS itemsubgrp_code, itemsubgrp.name AS itemsubgrp_name FROM itemsubgrp', 'computes': [], 'args': [], 'arg_types': {}, 'tables': ['itemsubgrp'], 'columns': [{'name': 'code', 'label': 'Code', 'type': 'char'}, {'name': 'name', 'label': 'Name', 'type': 'char'}]},
)


class SubGroupsForm(GeneratedForm):
    """Sub Groups"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('datawindow', 'dw_sman', 9, 0, 1723, 1084, dataobject='d_itemsubgrpmaster', taborder=10)
        self.add('commandbutton', 'cb_add', 27, 1000, 178, 76, text='&Add', taborder=20)
        self.add('commandbutton', 'cb_delete', 215, 1000, 178, 76, text='&Delete', taborder=30)
        self.add('commandbutton', 'cb_save', 649, 1112, 261, 96, text='&Save', taborder=40)
        self.add('commandbutton', 'cb_exit', 928, 1112, 261, 96, text='E&xit', taborder=50)
