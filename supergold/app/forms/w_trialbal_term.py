"""Between two dates — w_trialbal_term.

Generated from the PowerBuilder window ``w_trialbal_term.srw`` by
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
    name='w_trialbal_term',
    title='Between two dates',
    width=3506,
    height=2192,
    controls=[],
    tables=['accountm', 'daybook'],
    source_path='w_trialbal_term.srw',
    grid={'control': 'dw_1', 'dataobject': 'd_trialbal_grp_term', 'table': 'accountg', 'keys': ['grcode'], 'columns': [{'name': 'name', 'label': 'name', 'type': 'char'}, {'name': 'grcode', 'label': 'grcode', 'type': 'char'}, {'name': 'c_opbalb', 'label': 'c_opbalb', 'type': 'decimal'}, {'name': 'c_opbala', 'label': 'c_opbala', 'type': 'decimal'}, {'name': 'c_total', 'label': 'c_total', 'type': 'decimal'}, {'name': 'pos', 'label': 'pos', 'type': 'long'}, {'name': 'actype1', 'label': 'actype1', 'type': 'char'}]},
    report={'dataobject': 'd_trialbal_grp_term', 'sql': 'SELECT accountg.name AS accountg_name, accountg.grcode AS accountg_grcode, accountg.pos AS accountg_pos, accountg.actype1 AS accountg_actype1, (select sum(opbalb) from accountm where accountm.grcode = accountg.grcode) as c_opbalb, (select sum(opbal) from accountm where accountm.grcode = accountg.grcode) as c_opbala, (select sum(amount) from accountm where accountm.grcode = accountg.grcode ) as c_total FROM accountg ORDER BY accountg.pos ASC, accountg.name ASC', 'args': ['rlevel', 'opstock', 'rDate', 'rDate2', 'rOpBalErr', 'rTranErr'], 'arg_types': {'rlevel': 'number', 'opstock': 'number', 'rDate': 'date', 'rDate2': 'date', 'rOpBalErr': 'number', 'rTranErr': 'number'}, 'tables': ['accountg'], 'columns': [{'name': 'name', 'label': 'name', 'type': 'char'}, {'name': 'grcode', 'label': 'grcode', 'type': 'char'}, {'name': 'c_opbalb', 'label': 'c_opbalb', 'type': 'decimal'}, {'name': 'c_opbala', 'label': 'c_opbala', 'type': 'decimal'}, {'name': 'c_total', 'label': 'c_total', 'type': 'decimal'}, {'name': 'pos', 'label': 'pos', 'type': 'long'}, {'name': 'actype1', 'label': 'actype1', 'type': 'char'}]},
    opens=['w_calander2', 'w_tranerror', 'w_acgrpdetails', 'w_acledgerpopup'],
)


class BetweenTwoDatesForm(GeneratedForm):
    """Between two dates"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('datawindow', 'dw_1', 18, 20, 2839, 2052, dataobject='d_trialbal_grp_term', taborder=60)
        self.add('checkbox', 'cbx_grp', 2935, 48, 398, 76, text='Group Wise')
        self.add('statictext', 'st_2', 2921, 176, 329, 76, text='Date From')
        self.add('editmask', 'em_date', 2875, 252, 411, 92, taborder=10)
        self.add('commandbutton', 'cb_dthlp1', 3291, 252, 59, 92, text='^', taborder=100)
        self.add('statictext', 'st_3', 2921, 364, 329, 76, text='Date To')
        self.add('editmask', 'em_date2', 2875, 440, 411, 92, taborder=30)
        self.add('commandbutton', 'cb_dthlp2', 3291, 440, 59, 92, text='^', taborder=20)
        self.add('dropdownlistbox', 'ddlb_actype', 2871, 572, 544, 596, text='All', items=['All', 'Revenue', 'Expense', 'Assets', 'Liabilities'], taborder=50)
        self.add('commandbutton', 'cb_show', 2953, 708, 283, 108, text='&Show', taborder=40)
        self.add('commandbutton', 'cb_toexcel', 2953, 904, 283, 92, text='To Excel', taborder=50)
        self.add('commandbutton', 'cb_sort', 2953, 1012, 283, 96, text='&Sort', taborder=41)
        self.add('commandbutton', 'cb_3', 2953, 1108, 283, 96, text='Save &As', taborder=70)
        self.add('commandbutton', 'cb_1', 2953, 1204, 283, 96, text='&Print', taborder=90)
        self.add('commandbutton', 'cb_2', 2953, 1300, 283, 96, text='E&xit', taborder=110)
        self.add('checkbox', 'cbx_speed', 2939, 1448, 425, 80, text='Speed Print')
        self.add('commandbutton', 'cb_tranerr', 2880, 1676, 530, 108, text='Transaction Errors', taborder=80)
