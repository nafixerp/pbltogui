"""Item Adjustment Details — w_itemadjview.

Generated from the PowerBuilder window ``w_itemadjview.srw`` by
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
    name='w_itemadjview',
    title='Item Adjustment Details',
    width=2171,
    height=1348,
    controls=[],
    tables=[],
    source_path='w_itemadjview.srw',
    report={'dataobject': 'd_itemadjview', 'sql': 'SELECT itemadj.fromcode AS itemadj_fromcode, itemadj.fromqty AS itemadj_fromqty, itemadj.fromwgt AS itemadj_fromwgt, itemadj.tocode AS itemadj_tocode, itemadj.toqty AS itemadj_toqty, itemadj.towgt AS itemadj_towgt, itemadj.particular AS itemadj_particular, itemadj.tdate AS itemadj_tdate, itemadj.ttime AS itemadj_ttime, itemadj.smcode AS itemadj_smcode, itemadj.slno AS itemadj_slno, itemadj.al AS itemadj_al, itemadj.fromstktype AS itemadj_fromstktype, itemadj.tostktype AS itemadj_tostktype, itemadj.fromstwgt AS itemadj_fromstwgt, itemadj.tostwgt AS itemadj_tostwgt, (select name from items where items.code = fromcode) as fromname, (select name from items where items.code = tocode) as toname, 0 as prn FROM itemadj ORDER BY itemadj.tdate ASC', 'args': ['rslno'], 'arg_types': {'rslno': 'number'}, 'tables': ['itemadj'], 'columns': [{'name': 'fromcode', 'label': 'fromcode', 'type': 'char'}, {'name': 'fromqty', 'label': 'fromqty', 'type': 'long'}, {'name': 'fromwgt', 'label': 'fromwgt', 'type': 'decimal'}, {'name': 'tocode', 'label': 'tocode', 'type': 'char'}, {'name': 'toqty', 'label': 'toqty', 'type': 'long'}, {'name': 'towgt', 'label': 'towgt', 'type': 'decimal'}, {'name': 'particular', 'label': 'particular', 'type': 'char'}, {'name': 'tdate', 'label': 'tdate', 'type': 'date'}, {'name': 'fromname', 'label': 'fromname', 'type': 'char'}, {'name': 'toname', 'label': 'toname', 'type': 'char'}, {'name': 'ttime', 'label': 'ttime', 'type': 'time'}, {'name': 'smcode', 'label': 'smcode', 'type': 'char'}, {'name': 'prn', 'label': 'prn', 'type': 'long'}, {'name': 'slno', 'label': 'slno', 'type': 'decimal'}, {'name': 'al', 'label': 'al', 'type': 'char'}, {'name': 'fromstktype', 'label': 'fromstktype', 'type': 'char'}, {'name': 'tostktype', 'label': 'tostktype', 'type': 'char'}, {'name': 'fromstwgt', 'label': 'fromstwgt', 'type': 'decimal'}, {'name': 'tostwgt', 'label': 'tostwgt', 'type': 'decimal'}]},
)


class ItemAdjustmentDetailsForm(GeneratedForm):
    """Item Adjustment Details"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('datawindow', 'dw_salechklist', 0, 0, 2135, 1248, dataobject='d_itemadjview', taborder=10)
        self.add('commandbutton', 'cb_exit', 1719, 0, 265, 92, text='E&xit', taborder=20)
