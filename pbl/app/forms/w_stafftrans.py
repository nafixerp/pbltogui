"""Transaction — w_stafftrans.

Generated from the PowerBuilder window ``w_stafftrans.srw`` by
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
    name='w_stafftrans',
    title='Transaction',
    width=3218,
    height=1860,
    controls=[],
    tables=['daybook', 'staff_log', 'staffleave', 'generali', 'daybookpart'],
    source_path='w_stafftrans.srw',
    grid={'control': 'dw_trans', 'dataobject': 'd_stafftrans', 'table': 'clients', 'keys': ['code'], 'columns': [{'name': 'code', 'label': 'code', 'type': 'char'}, {'name': 'name', 'label': 'Name', 'type': 'char'}, {'name': 'salary', 'label': 'salary', 'type': 'decimal'}, {'name': 'amount', 'label': 'Amount', 'type': 'decimal'}, {'name': 'opbalance', 'label': 'opbalance', 'type': 'decimal'}, {'name': 'opbalanceb', 'label': 'opbalanceb', 'type': 'decimal'}, {'name': 'ttran', 'label': 'ttran', 'type': 'decimal'}]},
    report={'dataobject': 'd_stafftrans', 'sql': 'SELECT clients.code AS clients_code, clients.name AS clients_name, clients.salary AS clients_salary, clients.opbalance AS clients_opbalance, clients.opbalanceb AS clients_opbalanceb, 0.00 as amount, (select sum(daybook.amount) from daybook where daybook.accode = clients.code and daybook.control <= :rlevel and daybook.tdate <= :rdate) ttran FROM clients ORDER BY clients.name ASC', 'args': ['rdate', 'rlevel'], 'arg_types': {'rdate': 'date', 'rlevel': 'number'}, 'tables': ['clients'], 'columns': [{'name': 'code', 'label': 'code', 'type': 'char'}, {'name': 'name', 'label': 'Name', 'type': 'char'}, {'name': 'salary', 'label': 'salary', 'type': 'decimal'}, {'name': 'amount', 'label': 'Amount', 'type': 'decimal'}, {'name': 'opbalance', 'label': 'opbalance', 'type': 'decimal'}, {'name': 'opbalanceb', 'label': 'opbalanceb', 'type': 'decimal'}, {'name': 'ttran', 'label': 'ttran', 'type': 'decimal'}]},
    opens=['w_cbachdhelp'],
)


class TransactionForm(GeneratedForm):
    """Transaction"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('groupbox', 'gb_1', 997, 0, 553, 284, text='To Staff A/c')
        self.add('editmask', 'em_allowedleaves', 2249, 0, 315, 100, taborder=10)
        self.add('commandbutton', 'cb_1', 2848, 0, 338, 92, text='Set as Def', taborder=20)
        self.add('statictext', 'st_4', 1801, 16, 457, 72, text='Allowed Leaves')
        self.add('checkbox', 'cbx_salary', 430, 44, 544, 92, text='Salary Allocation')
        self.add('radiobutton', 'rb_debit', 1065, 76, 306, 76, text='Debited')
        self.add('editmask', 'em_endtime', 2862, 96, 320, 100, taborder=20)
        self.add('editmask', 'em_starttime', 2249, 100, 320, 100, taborder=10)
        self.add('statictext', 'st_5', 1801, 112, 457, 72, text='Start Time')
        self.add('statictext', 'st_6', 2601, 112, 283, 72, text='End Time')
        self.add('editmask', 'em_date', 443, 168, 485, 100, taborder=10)
        self.add('radiobutton', 'rb_credit', 1065, 168, 329, 76, text='Credited')
        self.add('statictext', 'st_1', 178, 180, 247, 76, text='Date :')
        self.add('editmask', 'em_reqhours', 2249, 204, 320, 100, taborder=30)
        self.add('statictext', 'st_7', 1787, 212, 457, 64, text='Wrk Hours / Day')
        self.add('datawindow', 'dw_acname', 439, 304, 1102, 88, dataobject='d_anyaccode', taborder=20)
        self.add('commandbutton', 'cb_logbased', 1778, 308, 795, 112, text='Log Based Calculation', taborder=10)
        self.add('statictext', 'st_3', 96, 312, 329, 76, text='A/c Name :')
        self.add('datawindow', 'dw_trans', 41, 432, 3159, 964, dataobject='d_stafftrans', taborder=30)
        self.add('commandbutton', 'cb_delete', 50, 1300, 229, 80, text='&Delete', taborder=60)
        self.add('singlelineedit', 'sle_part', 448, 1412, 1330, 92, limit=40, taborder=40)
        self.add('statictext', 'st_2', 59, 1428, 361, 76, text='Particulars :')
        self.add('commandbutton', 'cb_process', 873, 1552, 338, 108, text='&Save', taborder=50)
        self.add('commandbutton', 'cb_exit', 1221, 1552, 338, 108, text='E&xit', taborder=70)
