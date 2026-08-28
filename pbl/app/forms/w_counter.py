"""Counters — w_counter.

Generated from the PowerBuilder window ``w_counter.srw`` by
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
    name='w_counter',
    title='Counters',
    width=1760,
    height=1188,
    controls=[],
    tables=['salesm', 'barcode', 'generali'],
    source_path='w_counter.srw',
    grid={'control': 'dw_sman', 'dataobject': 'd_counter', 'table': 'counter', 'keys': ['code'], 'computes': [], 'columns': [{'name': 'code', 'label': 'Code', 'type': 'char'}, {'name': 'name', 'label': 'Name', 'type': 'char'}, {'name': 'startbillno', 'label': 'startbillno', 'type': 'decimal'}]},
    report={'dataobject': 'd_counter', 'sql': 'SELECT counter.code AS counter_code, counter.name AS counter_name, counter.startbillno AS counter_startbillno FROM counter', 'computes': [], 'args': [], 'arg_types': {}, 'tables': ['counter'], 'columns': [{'name': 'code', 'label': 'Code', 'type': 'char'}, {'name': 'name', 'label': 'Name', 'type': 'char'}, {'name': 'startbillno', 'label': 'startbillno', 'type': 'decimal'}]},
)


class CountersForm(GeneratedForm):
    """Counters"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('datawindow', 'dw_sman', 9, 0, 1723, 1084, dataobject='d_counter', taborder=10)
        self.add('commandbutton', 'cb_add', 27, 1000, 178, 76, text='&Add', taborder=20)
        self.add('commandbutton', 'cb_delete', 215, 1000, 178, 76, text='&Delete', taborder=30)
        self.add('commandbutton', 'cb_save', 846, 1000, 178, 76, text='&Save', taborder=40)
        self.add('commandbutton', 'cb_exit', 1033, 1000, 178, 76, text='E&xit', taborder=50)
