"""Cancel — w_itemadjhelp.

Generated from the PowerBuilder window ``w_itemadjhelp.srw`` by
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
    name='w_itemadjhelp',
    title='Cancel',
    width=3557,
    height=1744,
    controls=[],
    tables=[],
    source_path='w_itemadjhelp.srw',
    report={'dataobject': 'd_itemadjhelp', 'sql': 'SELECT itemadj.tdate AS itemadj_tdate, itemadj.fromqty AS itemadj_fromqty, itemadj.fromwgt AS itemadj_fromwgt, itemadj.fromstwgt AS itemadj_fromstwgt, itemadj.toqty AS itemadj_toqty, itemadj.towgt AS itemadj_towgt, itemadj.tostwgt AS itemadj_tostwgt, itemadj.slno AS itemadj_slno, itemadj.tocode AS itemadj_tocode, itemadj.fromcode AS itemadj_fromcode, itemadj.fromstktype AS itemadj_fromstktype, itemadj.tostktype AS itemadj_tostktype, (select items.name from items where items.code = itemadj.fromcode) as fromname, (select items.name from items where items.code = itemadj.tocode) as toname FROM itemadj ORDER BY itemadj.tdate DESC, itemadj.slno DESC', 'computes': [], 'args': [], 'arg_types': {}, 'tables': ['itemadj'], 'columns': [{'name': 'itemadj_tdate', 'label': 'Date', 'type': 'date'}, {'name': 'fromname', 'label': 'fromname', 'type': 'char'}, {'name': 'itemadj_fromqty', 'label': 'itemadj_fromqty', 'type': 'long'}, {'name': 'itemadj_fromwgt', 'label': 'itemadj_fromwgt', 'type': 'decimal'}, {'name': 'itemadj_fromstwgt', 'label': 'itemadj_fromstwgt', 'type': 'decimal'}, {'name': 'toname', 'label': 'toname', 'type': 'char'}, {'name': 'itemadj_toqty', 'label': 'itemadj_toqty', 'type': 'long'}, {'name': 'itemadj_towgt', 'label': 'Weight', 'type': 'decimal'}, {'name': 'itemadj_tostwgt', 'label': 'itemadj_tostwgt', 'type': 'decimal'}, {'name': 'itemadj_slno', 'label': 'itemadj_slno', 'type': 'decimal'}, {'name': 'itemadj_tocode', 'label': 'To Item', 'type': 'char'}, {'name': 'itemadj_fromcode', 'label': 'From Items', 'type': 'char'}, {'name': 'fromstktype', 'label': 'fromstktype', 'type': 'char'}, {'name': 'tostktype', 'label': 'tostktype', 'type': 'char'}]},
)


class CancelForm(GeneratedForm):
    """Cancel"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('datawindow', 'dw_1', 0, 0, 3525, 1440, dataobject='d_itemadjhelp', taborder=10)
        self.add('statictext', 'st_search', 18, 1356, 375, 76)
        self.add('oval', 'oval_1', 1477, 1448, 777, 188)
        self.add('commandbutton', 'cb_ok', 1618, 1496, 247, 92, text='OK', taborder=20)
        self.add('commandbutton', 'cb_cancel', 1883, 1496, 247, 92, text='Cancel', taborder=30)
