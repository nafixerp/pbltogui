"""Groupwise Expanded List — w_account_grpwise_expand_rep.

Generated from the PowerBuilder window ``w_account_grpwise_expand_rep.srw`` by
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
    name='w_account_grpwise_expand_rep',
    title='Groupwise Expanded List',
    width=3657,
    height=2284,
    controls=[],
    tables=['daybook', 'accountm', 'accountg', 'date', 'clients'],
    source_path='w_account_grpwise_expand_rep.srw',
)


class GroupwiseExpandedListForm(GeneratedForm):
    """Groupwise Expanded List"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 270, 0, 416, 96, taborder=50)
        self.add('editmask', 'em_date2', 983, 0, 416, 96, taborder=10)
        self.add('commandbutton', 'cb_show', 1701, 0, 242, 96, text='&Show', taborder=40)
        self.add('commandbutton', 'cb_print', 2057, 4, 270, 88, text='&Print', taborder=150)
        self.add('commandbutton', 'cb_setup', 2336, 4, 247, 88, text='Setup', taborder=120)
        self.add('commandbutton', 'cb_saveas', 2592, 4, 247, 88, text='Save As', taborder=110)
        self.add('commandbutton', 'cb_sort', 2853, 4, 229, 88, text='So&rt', taborder=100)
        self.add('commandbutton', 'cb_filter', 3095, 4, 229, 88, text='&Filter', taborder=30)
        self.add('commandbutton', 'cb_exit', 3333, 4, 270, 88, text='E&xit', taborder=20)
        self.add('statictext', 'st_date1', 32, 8, 229, 80, text='Upto :')
        self.add('statictext', 'st_date2', 754, 8, 219, 80, text='To :')
        self.add('datawindow', 'dw_grp', 270, 96, 1129, 96, dataobject='d_grcode', taborder=130)
        self.add('commandbutton', 'cb_ledgerprint', 2853, 96, 471, 88, text='Print All Ledger')
        self.add('checkbox', 'cbx_grp', 1403, 104, 73, 76)
        self.add('checkbox', 'cbx_term', 1696, 104, 288, 80, text='Term')
        self.add('checkbox', 'cbx_withbalance', 2053, 108, 622, 76, text='With Balance Only')
        self.add('statictext', 'st_3', 14, 112, 247, 76, text='Group :')
        self.add('datawindow', 'dw_1', 0, 192, 3621, 1776, dataobject='d_account_grpwise_expand_rep', taborder=140)
        self.add('commandbutton', 'cb_1', 2624, 1972, 247, 108, text='Filter', taborder=80)
        self.add('commandbutton', 'cb_account', 5, 1992, 306, 96, text='&Account', taborder=60)
        self.add('commandbutton', 'cb_grup', 320, 1992, 306, 96, text='&Group', taborder=90)
        self.add('commandbutton', 'cb_bshead', 635, 1992, 306, 96, text='&BS Head', taborder=70)
