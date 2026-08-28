"""Chart of Accounts — w_accountlist.

Generated from the PowerBuilder window ``w_accountlist.srw`` by
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
    name='w_accountlist',
    title='Chart of Accounts',
    width=3657,
    height=2284,
    controls=[],
    tables=['accountm', 'daybook', 'clients'],
    source_path='w_accountlist.srw',
    report={'dataobject': 'd_accountlist', 'sql': 'SELECT accountm.accode AS accountm_accode, accountm.name AS accountm_name, accountg.name AS accountg_name, accountm.grcode AS accountm_grcode, accountm.actype1 AS accountm_actype1, accountm.actype2 AS accountm_actype2, accountm.opbal AS accountm_opbal, accountm.opbalb AS accountm_opbalb, accountg.position AS accountg_position, accountg.grp AS accountg_grp, accountm.bshead AS accountm_bshead, accountm.removed AS accountm_removed, accountm.amount AS accountm_amount FROM accountm, accountg WHERE accountm.grcode = accountg.grcode ORDER BY accountg.grp ASC, accountg.name ASC, accountm.name ASC', 'args': ['rmcs', 'rdate', 'rlevel'], 'arg_types': {'rmcs': 'string', 'rdate': 'date', 'rlevel': 'number'}, 'tables': ['accountm', 'accountg'], 'columns': [{'name': 'accountm_accode', 'label': 'accountm_accode', 'type': 'char'}, {'name': 'accountm_name', 'label': 'accountm_name', 'type': 'char'}, {'name': 'accountg_name', 'label': 'accountg_name', 'type': 'char'}, {'name': 'accountm_grcode', 'label': 'accountm_grcode', 'type': 'char'}, {'name': 'accountm_actype1', 'label': 'accountm_actype1', 'type': 'char'}, {'name': 'accountm_actype2', 'label': 'accountm_actype2', 'type': 'char'}, {'name': 'accountm_opbal', 'label': 'accountm_opbal', 'type': 'decimal'}, {'name': 'accountm_opbalb', 'label': 'accountm_opbalb', 'type': 'decimal'}, {'name': 'accountg_position', 'label': 'accountg_position', 'type': 'long'}, {'name': 'accountg_grp', 'label': 'accountg_grp', 'type': 'char'}, {'name': 'accountm_bshead', 'label': 'accountm_bshead', 'type': 'char'}, {'name': 'accountm_removed', 'label': 'accountm_removed', 'type': 'long'}, {'name': 'accountm_amount', 'label': 'accountm_amount', 'type': 'decimal'}]},
    opens=['w_achd', 'w_achdbsgrp', 'w_achdgrp', 'w_repsetup', 'w_sucu', 'w_smith', 'w_acledgerpopup'],
)


class ChartOfAccountsForm(GeneratedForm):
    """Chart of Accounts"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('statictext', 'st_1', 14, 0, 443, 76, text='Account Type :')
        self.add('dropdownlistbox', 'ddlb_type', 485, 0, 718, 424, text='All', items=['All', 'Assets Only', 'Liabilities Only', 'Expenses Only', 'Incomes Only'], taborder=30)
        self.add('commandbutton', 'cb_2', 1595, 0, 402, 84, text='Refresh', taborder=40)
        self.add('commandbutton', 'cb_setup', 2085, 0, 247, 84, text='Setup', taborder=90)
        self.add('commandbutton', 'cb_saveas', 2341, 0, 247, 84, text='Save As', taborder=80)
        self.add('commandbutton', 'cb_sort', 2601, 0, 229, 84, text='So&rt', taborder=70)
        self.add('commandbutton', 'cb_filter', 2843, 0, 229, 84, text='&Filter', taborder=20)
        self.add('commandbutton', 'cb_print', 3077, 0, 270, 84, text='&Print', taborder=130)
        self.add('commandbutton', 'cb_exit', 3351, 0, 270, 84, text='E&xit', taborder=10)
        self.add('datawindow', 'dw_1', 0, 96, 3621, 1888, dataobject='d_accountlist', taborder=120)
        self.add('checkbox', 'cbx_withbalance', 2085, 108, 622, 76, text='With Balance Only')
        self.add('checkbox', 'cbx_removedonly', 2843, 108, 645, 80, text='Show Removed Only')
        self.add('datawindow', 'dw_grp', 1326, 1984, 1138, 96, dataobject='d_grcode', taborder=110)
        self.add('commandbutton', 'cb_account', 5, 1992, 306, 96, text='&Account', taborder=40)
        self.add('commandbutton', 'cb_grup', 320, 1992, 306, 96, text='&Group', taborder=60)
        self.add('commandbutton', 'cb_bshead', 635, 1992, 306, 96, text='&BS Head', taborder=50)
        self.add('checkbox', 'cbx_grp', 2478, 1992, 73, 76)
        self.add('statictext', 'st_3', 1065, 2000, 247, 76, text='Group :')
        self.add('commandbutton', 'cb_1', 2569, 2024, 247, 108, text='Filter', taborder=51)
        self.add('datawindow', 'dw_bsgrp', 1326, 2088, 1138, 96, dataobject='d_bsheadcode', taborder=100)
        self.add('checkbox', 'cbx_bshead', 2478, 2092, 73, 76)
        self.add('statictext', 'st_10', 1010, 2104, 302, 76, text='BS Head :')
