"""Stock Add - Less Edit — w_itemaddlesshelp.

Generated from the PowerBuilder window ``w_itemaddlesshelp.srw`` by
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
    name='w_itemaddlesshelp',
    title='Stock Add - Less Edit',
    width=859,
    height=1356,
    controls=[],
    tables=[],
    source_path='w_itemaddlesshelp.srw',
    report={'dataobject': 'd_itemaddlesshelp', 'sql': 'SELECT itemadj.tdate AS itemadj_tdate FROM itemadj ORDER BY itemadj.tdate DESC', 'args': [], 'arg_types': {}, 'tables': ['itemadj'], 'columns': [{'name': 'itemadj_tdate', 'label': 'Date', 'type': 'date'}]},
)


class StockAddLessEditForm(GeneratedForm):
    """Stock Add - Less Edit"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('datawindow', 'dw_1', 0, 0, 791, 1076, dataobject='d_itemaddlesshelp', taborder=10)
        self.add('statictext', 'st_search', 18, 992, 375, 76)
        self.add('oval', 'oval_1', 14, 1088, 777, 188)
        self.add('commandbutton', 'cb_ok', 155, 1136, 247, 92, text='OK', taborder=20)
        self.add('commandbutton', 'cb_cancel', 421, 1136, 247, 92, text='Cancel', taborder=30)
