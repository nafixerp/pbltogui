"""Leave Entry — w_staffleave.

Generated from the PowerBuilder window ``w_staffleave.srw`` by
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
    name='w_staffleave',
    title='Leave Entry',
    width=2546,
    height=1924,
    controls=[],
    tables=['staffleave'],
    source_path='w_staffleave.srw',
    grid={'control': 'dw_trans', 'dataobject': 'd_staffleave', 'table': 'clients', 'keys': ['code'], 'computes': [], 'columns': [{'name': 'code', 'label': 'code', 'type': 'char'}, {'name': 'name', 'label': 'Name', 'type': 'char'}, {'name': 'salary', 'label': 'salary', 'type': 'decimal'}, {'name': 'ldays', 'label': 'ldays', 'type': 'decimal'}, {'name': 'reason', 'label': 'reason', 'type': 'char'}, {'name': 'note', 'label': 'note', 'type': 'char'}, {'name': 'plusdays', 'label': 'plusdays', 'type': 'decimal'}]},
    report={'dataobject': 'd_staffleave', 'sql': 'SELECT clients.code AS clients_code, clients.name AS clients_name, clients.salary AS clients_salary, (select staffleave.ldays from staffleave where staffleave.staff = clients.code and staffleave.tdate = :rdate) as  ldays, (select staffleave.reason from staffleave where staffleave.staff = clients.code and staffleave.tdate = :rdate) as  reason, (select staffleave.note from staffleave where staffleave.staff = clients.code and staffleave.tdate = :rdate) as  note, (select staffleave.plusdays from staffleave where staffleave.staff = clients.code and staffleave.tdate = :rdate) as  plusdays FROM clients ORDER BY clients.name ASC', 'computes': [], 'args': ['rdate'], 'arg_types': {'rdate': 'date'}, 'tables': ['clients'], 'columns': [{'name': 'code', 'label': 'code', 'type': 'char'}, {'name': 'name', 'label': 'Name', 'type': 'char'}, {'name': 'salary', 'label': 'salary', 'type': 'decimal'}, {'name': 'ldays', 'label': 'ldays', 'type': 'decimal'}, {'name': 'reason', 'label': 'reason', 'type': 'char'}, {'name': 'note', 'label': 'note', 'type': 'char'}, {'name': 'plusdays', 'label': 'plusdays', 'type': 'decimal'}]},
)


class LeaveEntryForm(GeneratedForm):
    """Leave Entry"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date', 297, 4, 553, 100, taborder=10)
        self.add('statictext', 'st_1', 27, 16, 247, 76, text='Date :')
        self.add('datawindow', 'dw_trans', 0, 120, 2528, 1564, dataobject='d_staffleave', taborder=20)
        self.add('commandbutton', 'cb_process', 841, 1692, 338, 108, text='&Save', taborder=30)
        self.add('commandbutton', 'cb_exit', 1189, 1692, 338, 108, text='E&xit', taborder=40)
