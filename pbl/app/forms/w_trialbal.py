"""Upto a date — w_trialbal.

Generated from the PowerBuilder window ``w_trialbal.srw`` by
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
    name='w_trialbal',
    title='Upto a date',
    width=3643,
    height=2184,
    controls=[],
    tables=['accountm', 'daybook', 'date', 'clients'],
    source_path='w_trialbal.srw',
    grid={'control': 'dw_1', 'dataobject': 'd_trialbal_grp', 'table': 'accountg', 'keys': ['grcode'], 'columns': [{'name': 'name', 'label': 'name', 'type': 'char'}, {'name': 'grcode', 'label': 'grcode', 'type': 'char'}, {'name': 'c_opbalb', 'label': 'c_opbalb', 'type': 'decimal'}, {'name': 'c_opbala', 'label': 'c_opbala', 'type': 'decimal'}, {'name': 'c_total', 'label': 'c_total', 'type': 'decimal'}, {'name': 'pos', 'label': 'pos', 'type': 'long'}]},
    report={'dataobject': 'd_trialbal_grp', 'sql': 'SELECT accountg.name AS accountg_name, accountg.grcode AS accountg_grcode, accountg.pos AS accountg_pos, (select sum(opbalb) from accountm where accountm.grcode = accountg.grcode) as c_opbalb, (select sum(opbal) from accountm where accountm.grcode = accountg.grcode) as c_opbala, (select sum(accountm.amount) from accountm where accountm.grcode = accountg.grcode) as c_total FROM accountg ORDER BY accountg.pos ASC, accountg.name ASC', 'args': ['rlevel', 'opstock', 'rDate', 'rOpBalErr', 'rTranErr'], 'arg_types': {'rlevel': 'number', 'opstock': 'number', 'rDate': 'date', 'rOpBalErr': 'number', 'rTranErr': 'number'}, 'tables': ['accountg'], 'columns': [{'name': 'name', 'label': 'name', 'type': 'char'}, {'name': 'grcode', 'label': 'grcode', 'type': 'char'}, {'name': 'c_opbalb', 'label': 'c_opbalb', 'type': 'decimal'}, {'name': 'c_opbala', 'label': 'c_opbala', 'type': 'decimal'}, {'name': 'c_total', 'label': 'c_total', 'type': 'decimal'}, {'name': 'pos', 'label': 'pos', 'type': 'long'}]},
)


class UptoADateForm(GeneratedForm):
    """Upto a date"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('statictext', 'st_1', 3173, 12, 247, 76, text='Date')
        self.add('datawindow', 'dw_1', 18, 20, 3081, 2048, dataobject='d_trialbal_grp', taborder=10)
        self.add('editmask', 'em_date', 3113, 104, 443, 92, taborder=40)
        self.add('checkbox', 'cbx_grp', 3163, 224, 398, 76, text='Group Wise')
        self.add('checkbox', 'cbx_withbal', 3159, 316, 439, 76, text='With Balance')
        self.add('commandbutton', 'cb_4', 3186, 428, 279, 104, text='&Show', taborder=30)
        self.add('commandbutton', 'cb_toexcel', 3186, 592, 283, 92, text='To Excel', taborder=40)
        self.add('commandbutton', 'cb_sort', 3186, 700, 283, 96, text='&Sort', taborder=80)
        self.add('commandbutton', 'cb_3', 3186, 796, 283, 96, text='&Save As', taborder=20)
        self.add('commandbutton', 'cb_1', 3186, 892, 283, 96, text='&Print', taborder=70)
        self.add('commandbutton', 'cb_2', 3186, 988, 283, 96, text='E&xit', taborder=130)
        self.add('groupbox', 'gb_1', 3141, 1168, 453, 472, text='Ledger Print', taborder=120)
        self.add('commandbutton', 'cb_selectall', 3159, 1272, 416, 108, text='Select All', taborder=100)
        self.add('commandbutton', 'cb_unselectall', 3159, 1380, 416, 108, text='Deselect All', taborder=110)
        self.add('commandbutton', 'cb_ledgerprint', 3159, 1492, 416, 108, text='Print Ledger', taborder=90)
        self.add('commandbutton', 'cb_tranerr', 3131, 1648, 475, 108, text='Transaction Errors', taborder=50)
        self.add('statictext', 'st_2', 3163, 1764, 407, 80, text='Search Name')
        self.add('datawindow', 'dw_search', 3141, 1840, 462, 92, dataobject='d_search', taborder=60)
