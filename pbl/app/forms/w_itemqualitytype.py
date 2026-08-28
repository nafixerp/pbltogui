"""Quality Type — w_itemqualitytype.

Generated from the PowerBuilder window ``w_itemqualitytype.srw`` by
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
    name='w_itemqualitytype',
    title='Quality Type',
    width=1083,
    height=1328,
    controls=[],
    tables=['items', 'mctable', 'purchased', 'salesd', 'salesrd', 'barcode', 'orderd', 'orderdga', 'wstgtable'],
    source_path='w_itemqualitytype.srw',
    grid={'control': 'dw_sman', 'dataobject': 'd_itemqtype', 'table': 'itemsqtype', 'keys': ['code'], 'columns': [{'name': 'code', 'label': 'Purity', 'type': 'char'}, {'name': 'touch', 'label': 'Touch', 'type': 'decimal'}, {'name': 'code2', 'label': 'code2', 'type': 'char'}]},
    report={'dataobject': 'd_itemqtype', 'sql': 'SELECT itemsqtype.code AS itemsqtype_code, itemsqtype.touch AS itemsqtype_touch, (code) as code2 FROM itemsqtype', 'args': [], 'arg_types': {}, 'tables': ['itemsqtype'], 'columns': [{'name': 'code', 'label': 'Purity', 'type': 'char'}, {'name': 'touch', 'label': 'Touch', 'type': 'decimal'}, {'name': 'code2', 'label': 'code2', 'type': 'char'}]},
)


class QualityTypeForm(GeneratedForm):
    """Quality Type"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('datawindow', 'dw_sman', 18, 0, 1038, 1140, dataobject='d_itemqtype', taborder=10)
        self.add('commandbutton', 'cb_add', 91, 1148, 206, 88, text='&Add', taborder=20)
        self.add('commandbutton', 'cb_delete', 302, 1148, 206, 88, text='&Delete', taborder=30)
        self.add('commandbutton', 'cb_save', 535, 1148, 206, 88, text='&Save', taborder=40)
        self.add('commandbutton', 'cb_exit', 745, 1148, 206, 88, text='E&xit', taborder=50)
