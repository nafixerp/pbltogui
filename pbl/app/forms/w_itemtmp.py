"""Item Temp — w_itemtmp.

Generated from the PowerBuilder window ``w_itemtmp.srw`` by
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
    name='w_itemtmp',
    title='Item Temp',
    width=2519,
    height=1604,
    controls=[],
    tables=['orderm', 'items'],
    source_path='w_itemtmp.srw',
    grid={'control': 'dw_sman', 'dataobject': 'd_itemtmp', 'table': 'itemstmp', 'keys': ['code', 'name'], 'columns': [{'name': 'code', 'label': 'Code', 'type': 'char'}, {'name': 'name', 'label': 'Name', 'type': 'char'}, {'name': 'mname', 'label': 'Malayalam Name', 'type': 'char'}, {'name': 'iqtype', 'label': 'iqtype', 'type': 'char'}]},
    report={'dataobject': 'd_itemtmp', 'sql': 'SELECT itemstmp.code AS itemstmp_code, itemstmp.name AS itemstmp_name, itemstmp.mname AS itemstmp_mname, itemstmp.iqtype AS itemstmp_iqtype FROM itemstmp ORDER BY itemstmp.code ASC, itemstmp.name ASC', 'args': [], 'arg_types': {}, 'tables': ['itemstmp'], 'columns': [{'name': 'code', 'label': 'Code', 'type': 'char'}, {'name': 'name', 'label': 'Name', 'type': 'char'}, {'name': 'mname', 'label': 'Malayalam Name', 'type': 'char'}, {'name': 'iqtype', 'label': 'iqtype', 'type': 'char'}]},
)


class ItemTempForm(GeneratedForm):
    """Item Temp"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('datawindow', 'dw_sman', 5, 0, 2473, 1304, dataobject='d_itemtmp', taborder=10)
        self.add('roundrectangle', 'rr_1', 526, 1324, 1358, 164)
        self.add('commandbutton', 'cb_add', 562, 1360, 242, 92, text='&Add', taborder=20)
        self.add('commandbutton', 'cb_delete', 814, 1360, 242, 92, text='&Delete', taborder=30)
        self.add('commandbutton', 'cb_cancel', 1097, 1360, 242, 92, text='&Cancel', taborder=40)
        self.add('commandbutton', 'cb_save', 1349, 1360, 242, 92, text='&Save', taborder=50)
        self.add('commandbutton', 'cb_exit', 1600, 1360, 242, 92, text='E&xit', taborder=60)
