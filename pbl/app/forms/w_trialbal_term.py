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
    grid={'control': 'dw_1', 'dataobject': 'd_trialbal_grp_term', 'table': 'accountg', 'keys': ['grcode'], 'computes': [{'name': 'compute_2', 'expression': 'if( balance <= 0, string(abs(balance),~"######0.00~"), ~"~")', 'format': '', 'label': 'compute_2', 'band': 'detail'}, {'name': 'compute_3', 'expression': 'if( balance > 0, string(balance,~"######0.00~"), ~"~")', 'format': '', 'label': 'compute_3', 'band': 'detail'}, {'name': 'balance', 'expression': ' if(isnull(  c_total ), 0 ,  c_total )  ', 'format': '[general]', 'label': 'Balances', 'band': 'detail'}, {'name': 'tdebit', 'expression': ' abs(sum( if(balance<0, balance,0)  for all  ))', 'format': '######0.00', 'label': 'tdebit', 'band': 'summary'}, {'name': 'tcredit', 'expression': 'abs(sum( if(balance>0, balance,0)  for all  ))', 'format': '######0.00', 'label': 'tcredit', 'band': 'summary'}, {'name': 'compute_6', 'expression': 'if (round(tdebit,2)<>round(tcredit,2),~"ERROR :~",~"~")', 'format': '[general]', 'label': 'compute_6', 'band': 'summary'}, {'name': 'opbalerror', 'expression': ' rOpBalErr -  opstock ', 'format': '[general]', 'label': 'opbalerror', 'band': 'summary'}, {'name': 'tranerror', 'expression': 'rTranErr', 'format': '#######0.00', 'label': 'tranerror', 'band': 'summary'}, {'name': 'compute_4', 'expression': 'if ( (round(tdebit,2) - round(tcredit,2)) <> 0 , ~"Difference - ~"+string(abs(tcredit-tdebit),~"#######0.00~"), ~"~")', 'format': '[general]', 'label': 'compute_4', 'band': 'summary'}, {'name': 'compute_7', 'expression': 'case (  round(ropbalerr,2) when is >0 then ~"In the opening balance credit is more than debit by ~"+string(abs(ropbalerr),~"########0.00~") when  is <0 then ~"In the opening balance debit is more than credit by  ~"+string(abs(ropbalerr),~"########0.00~") else ~"~") ', 'format': '[general]', 'label': 'compute_7', 'band': 'summary'}, {'name': 'compute_5', 'expression': 'case (  round( tranerror,2) when is >0 then ~"In the transactions credit is more than debit by ~"+string(abs(tranerror),~"########0.00~") when  is <0 then ~"In the transactions debit is more than credit by  ~"+string(abs(tranerror),~"########0.00~") else ~"~")', 'format': '[general]', 'label': 'compute_5', 'band': 'summary'}], 'columns': [{'name': 'name', 'label': 'name', 'type': 'char'}, {'name': 'grcode', 'label': 'grcode', 'type': 'char'}, {'name': 'c_opbalb', 'label': 'c_opbalb', 'type': 'decimal'}, {'name': 'c_opbala', 'label': 'c_opbala', 'type': 'decimal'}, {'name': 'c_total', 'label': 'c_total', 'type': 'decimal'}, {'name': 'pos', 'label': 'pos', 'type': 'long'}, {'name': 'actype1', 'label': 'actype1', 'type': 'char'}]},
    report={'dataobject': 'd_trialbal_grp_term', 'sql': 'SELECT accountg.name AS accountg_name, accountg.grcode AS accountg_grcode, accountg.pos AS accountg_pos, accountg.actype1 AS accountg_actype1, (select sum(opbalb) from accountm where accountm.grcode = accountg.grcode) as c_opbalb, (select sum(opbal) from accountm where accountm.grcode = accountg.grcode) as c_opbala, (select sum(amount) from accountm where accountm.grcode = accountg.grcode ) as c_total FROM accountg ORDER BY accountg.pos ASC, accountg.name ASC', 'computes': [{'name': 'compute_2', 'expression': 'if( balance <= 0, string(abs(balance),~"######0.00~"), ~"~")', 'format': '', 'label': 'compute_2', 'band': 'detail'}, {'name': 'compute_3', 'expression': 'if( balance > 0, string(balance,~"######0.00~"), ~"~")', 'format': '', 'label': 'compute_3', 'band': 'detail'}, {'name': 'balance', 'expression': ' if(isnull(  c_total ), 0 ,  c_total )  ', 'format': '[general]', 'label': 'Balances', 'band': 'detail'}, {'name': 'tdebit', 'expression': ' abs(sum( if(balance<0, balance,0)  for all  ))', 'format': '######0.00', 'label': 'tdebit', 'band': 'summary'}, {'name': 'tcredit', 'expression': 'abs(sum( if(balance>0, balance,0)  for all  ))', 'format': '######0.00', 'label': 'tcredit', 'band': 'summary'}, {'name': 'compute_6', 'expression': 'if (round(tdebit,2)<>round(tcredit,2),~"ERROR :~",~"~")', 'format': '[general]', 'label': 'compute_6', 'band': 'summary'}, {'name': 'opbalerror', 'expression': ' rOpBalErr -  opstock ', 'format': '[general]', 'label': 'opbalerror', 'band': 'summary'}, {'name': 'tranerror', 'expression': 'rTranErr', 'format': '#######0.00', 'label': 'tranerror', 'band': 'summary'}, {'name': 'compute_4', 'expression': 'if ( (round(tdebit,2) - round(tcredit,2)) <> 0 , ~"Difference - ~"+string(abs(tcredit-tdebit),~"#######0.00~"), ~"~")', 'format': '[general]', 'label': 'compute_4', 'band': 'summary'}, {'name': 'compute_7', 'expression': 'case (  round(ropbalerr,2) when is >0 then ~"In the opening balance credit is more than debit by ~"+string(abs(ropbalerr),~"########0.00~") when  is <0 then ~"In the opening balance debit is more than credit by  ~"+string(abs(ropbalerr),~"########0.00~") else ~"~") ', 'format': '[general]', 'label': 'compute_7', 'band': 'summary'}, {'name': 'compute_5', 'expression': 'case (  round( tranerror,2) when is >0 then ~"In the transactions credit is more than debit by ~"+string(abs(tranerror),~"########0.00~") when  is <0 then ~"In the transactions debit is more than credit by  ~"+string(abs(tranerror),~"########0.00~") else ~"~")', 'format': '[general]', 'label': 'compute_5', 'band': 'summary'}], 'args': ['rlevel', 'opstock', 'rDate', 'rDate2', 'rOpBalErr', 'rTranErr'], 'arg_types': {'rlevel': 'number', 'opstock': 'number', 'rDate': 'date', 'rDate2': 'date', 'rOpBalErr': 'number', 'rTranErr': 'number'}, 'tables': ['accountg'], 'columns': [{'name': 'name', 'label': 'name', 'type': 'char'}, {'name': 'grcode', 'label': 'grcode', 'type': 'char'}, {'name': 'c_opbalb', 'label': 'c_opbalb', 'type': 'decimal'}, {'name': 'c_opbala', 'label': 'c_opbala', 'type': 'decimal'}, {'name': 'c_total', 'label': 'c_total', 'type': 'decimal'}, {'name': 'pos', 'label': 'pos', 'type': 'long'}, {'name': 'actype1', 'label': 'actype1', 'type': 'char'}]},
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
