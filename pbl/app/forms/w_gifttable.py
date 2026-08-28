"""Gift Table — w_gifttable.

Generated from the PowerBuilder window ``w_gifttable.srw`` by
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
    name='w_gifttable',
    title='Gift Table',
    width=2167,
    height=1656,
    controls=[],
    tables=[],
    source_path='w_gifttable.srw',
    grid={'control': 'dw_1', 'dataobject': 'd_gifttable', 'table': 'gifttable', 'keys': ['points'], 'columns': [{'name': 'points', 'label': 'Points', 'type': 'long'}, {'name': 'particulars', 'label': 'Particulars', 'type': 'char'}]},
    report={'dataobject': 'd_gifttable', 'sql': 'SELECT gifttable.points AS gifttable_points, gifttable.particulars AS gifttable_particulars FROM gifttable ORDER BY gifttable.points ASC', 'args': [], 'arg_types': {}, 'tables': ['gifttable'], 'columns': [{'name': 'points', 'label': 'Points', 'type': 'long'}, {'name': 'particulars', 'label': 'Particulars', 'type': 'char'}]},
)


class GiftTableForm(GeneratedForm):
    """Gift Table"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('datawindow', 'dw_1', 5, 0, 2139, 1372, dataobject='d_gifttable', taborder=10)
        self.add('roundrectangle', 'rr_1', 357, 1392, 1358, 164)
        self.add('commandbutton', 'cb_add', 393, 1428, 242, 92, text='&Add', taborder=20)
        self.add('commandbutton', 'cb_delete', 645, 1428, 242, 92, text='&Delete', taborder=30)
        self.add('commandbutton', 'cb_cancel', 928, 1428, 242, 92, text='&Cancel', taborder=40)
        self.add('commandbutton', 'cb_save', 1179, 1428, 242, 92, text='&Save', taborder=50)
        self.add('commandbutton', 'cb_exit', 1431, 1428, 242, 92, text='E&xit', taborder=60)
