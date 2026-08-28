"""Repair Complaints — w_repaircompl.

Generated from the PowerBuilder window ``w_repaircompl.srw`` by
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
    name='w_repaircompl',
    title='Repair Complaints',
    width=1394,
    height=1604,
    controls=[],
    tables=['items'],
    source_path='w_repaircompl.srw',
    grid={'control': 'dw_sman', 'dataobject': 'd_repcomplmast', 'table': 'repcompl', 'keys': ['part'], 'columns': [{'name': 'part', 'label': 'Complaint', 'type': 'char'}]},
    report={'dataobject': 'd_repcomplmast', 'sql': 'SELECT repcompl.part AS repcompl_part FROM repcompl', 'args': [], 'arg_types': {}, 'tables': ['repcompl'], 'columns': [{'name': 'part', 'label': 'Complaint', 'type': 'char'}]},
    opens=['w_regional', 'w_itemhelp'],
)


class RepairComplaintsForm(GeneratedForm):
    """Repair Complaints"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('datawindow', 'dw_sman', 27, 4, 1321, 1304, dataobject='d_repcomplmast', taborder=10)
        self.add('roundrectangle', 'rr_1', 0, 1328, 1358, 164)
        self.add('commandbutton', 'cb_add', 37, 1364, 242, 92, text='&Add', taborder=20)
        self.add('commandbutton', 'cb_delete', 288, 1364, 242, 92, text='&Delete', taborder=30)
        self.add('commandbutton', 'cb_cancel', 571, 1364, 242, 92, text='&Cancel', taborder=40)
        self.add('commandbutton', 'cb_save', 823, 1364, 242, 92, text='&Save', taborder=50)
        self.add('commandbutton', 'cb_exit', 1074, 1364, 242, 92, text='E&xit', taborder=60)
