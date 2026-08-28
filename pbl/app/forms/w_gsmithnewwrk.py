"""New Work Note — w_gsmithnewwrk.

Generated from the PowerBuilder window ``w_gsmithnewwrk.srw`` by
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
    name='w_gsmithnewwrk',
    title='New Work Note',
    width=3639,
    height=1780,
    controls=[],
    tables=['smithnewwrk'],
    source_path='w_gsmithnewwrk.srw',
    grid={'control': 'dw_ruffwork', 'dataobject': 'd_gsmithnewwrk', 'table': 'smithnewwrk', 'keys': ['sno'], 'columns': [{'name': 'smithcode', 'label': 'Smith', 'type': 'char'}, {'name': 'tdate', 'label': 'Date', 'type': 'date'}, {'name': 'ordno', 'label': 'Order No', 'type': 'char'}, {'name': 'icode', 'label': 'icode', 'type': 'char'}, {'name': 'qty', 'label': 'qty', 'type': 'long'}, {'name': 'weight', 'label': 'weight', 'type': 'decimal'}, {'name': 'part', 'label': 'Particulars', 'type': 'char'}, {'name': 'status', 'label': 'Status', 'type': 'long'}, {'name': 'sno', 'label': 'sno', 'type': 'long'}]},
    report={'dataobject': 'd_gsmithnewwrk', 'sql': 'SELECT smithnewwrk.smithcode AS smithnewwrk_smithcode, smithnewwrk.tdate AS smithnewwrk_tdate, smithnewwrk.ordno AS smithnewwrk_ordno, smithnewwrk.icode AS smithnewwrk_icode, smithnewwrk.qty AS smithnewwrk_qty, smithnewwrk.weight AS smithnewwrk_weight, smithnewwrk.part AS smithnewwrk_part, smithnewwrk.status AS smithnewwrk_status, smithnewwrk.sno AS smithnewwrk_sno FROM smithnewwrk', 'args': [], 'arg_types': {}, 'tables': ['smithnewwrk'], 'columns': [{'name': 'smithcode', 'label': 'Smith', 'type': 'char'}, {'name': 'tdate', 'label': 'Date', 'type': 'date'}, {'name': 'ordno', 'label': 'Order No', 'type': 'char'}, {'name': 'icode', 'label': 'icode', 'type': 'char'}, {'name': 'qty', 'label': 'qty', 'type': 'long'}, {'name': 'weight', 'label': 'weight', 'type': 'decimal'}, {'name': 'part', 'label': 'Particulars', 'type': 'char'}, {'name': 'status', 'label': 'Status', 'type': 'long'}, {'name': 'sno', 'label': 'sno', 'type': 'long'}]},
)


class NewWorkNoteForm(GeneratedForm):
    """New Work Note"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('datawindow', 'dw_ruffwork', 0, 4, 3584, 1448, dataobject='d_gsmithnewwrk', taborder=40)
        self.add('roundrectangle', 'rr_1', 681, 1484, 2629, 176)
        self.add('datawindow', 'dw_1', 210, 1520, 439, 92, dataobject='d_smith', taborder=50)
        self.add('commandbutton', 'cb_add', 745, 1520, 242, 100, text='&Add', taborder=10)
        self.add('commandbutton', 'cb_delete', 997, 1520, 242, 100, text='&Delete', taborder=20)
        self.add('commandbutton', 'cb_sort', 1271, 1520, 242, 100, text='Sort', taborder=21)
        self.add('commandbutton', 'cb_print', 1545, 1520, 242, 100, text='&Print', taborder=90)
        self.add('commandbutton', 'cb_cancel', 2519, 1520, 242, 100, text='&Cancel', taborder=30)
        self.add('commandbutton', 'cb_save', 2770, 1520, 242, 100, text='&Save', taborder=70)
        self.add('commandbutton', 'cb_exit', 3031, 1520, 242, 100, text='E&xit', taborder=80)
        self.add('dropdownlistbox', 'ddlb_type', 1810, 1524, 704, 472, text='Pending Only', items=['All', 'Pending Only', 'New Work Only', 'Work In Progress Only', 'Work Finished Only'], taborder=60)
        self.add('statictext', 'st_1', 0, 1528, 206, 76, text='Smith :')
