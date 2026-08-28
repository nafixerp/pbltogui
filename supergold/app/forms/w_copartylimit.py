"""C/o Party Limit — w_copartylimit.

Generated from the PowerBuilder window ``w_copartylimit.srw`` by
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
    name='w_copartylimit',
    title='C/o Party Limit',
    width=1842,
    height=1296,
    controls=[],
    tables=[],
    source_path='w_copartylimit.srw',
    grid={'control': 'dw_places', 'dataobject': 'd_copartylimit', 'table': 'copartylimit', 'keys': ['code'], 'columns': [{'name': 'code', 'label': 'C/o Party', 'type': 'char'}, {'name': 'maxamt', 'label': 'Max Crd Amt', 'type': 'decimal'}, {'name': 'maxwgt', 'label': 'maxwgt', 'type': 'decimal'}]},
    report={'dataobject': 'd_copartylimit', 'sql': 'SELECT copartylimit.code AS copartylimit_code, copartylimit.maxamt AS copartylimit_maxamt, copartylimit.maxwgt AS copartylimit_maxwgt FROM copartylimit', 'args': [], 'arg_types': {}, 'tables': ['copartylimit'], 'columns': [{'name': 'code', 'label': 'C/o Party', 'type': 'char'}, {'name': 'maxamt', 'label': 'Max Crd Amt', 'type': 'decimal'}, {'name': 'maxwgt', 'label': 'maxwgt', 'type': 'decimal'}]},
)


class COPartyLimitForm(GeneratedForm):
    """C/o Party Limit"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('datawindow', 'dw_places', 18, 0, 1792, 1016, dataobject='d_copartylimit', taborder=10)
        self.add('roundrectangle', 'rr_1', 215, 1028, 1358, 164)
        self.add('commandbutton', 'cb_add', 251, 1064, 242, 92, text='&Add', taborder=20)
        self.add('commandbutton', 'cb_delete', 503, 1064, 242, 92, text='&Delete', taborder=30)
        self.add('commandbutton', 'cb_cancel', 786, 1064, 242, 92, text='&Cancel', taborder=40)
        self.add('commandbutton', 'cb_save', 1038, 1064, 242, 92, text='&Save', taborder=50)
        self.add('commandbutton', 'cb_exit', 1289, 1064, 242, 92, text='E&xit', taborder=60)
