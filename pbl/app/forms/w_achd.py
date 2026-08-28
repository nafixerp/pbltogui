"""Account — w_achd.

Generated from the PowerBuilder window ``w_achd.srw`` by
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
    name='w_achd',
    title='Account',
    width=2409,
    height=1788,
    controls=[],
    tables=['accountm', 'daybook', 'userd', 'generals'],
    source_path='w_achd.srw',
    opens=['w_accode_rename', 'w_achdbsgrp', 'w_achdgrp', 'w_cbachdhelp'],
)


class AccountForm(GeneratedForm):
    """Account"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('statictext', 'st_head', 622, 16, 1079, 76)
        self.add('singlelineedit', 'sle_accode', 507, 112, 421, 88, limit=8, taborder=10)
        self.add('statictext', 'st_1', 87, 120, 338, 72, text='A/c Code')
        self.add('checkbox', 'cbx_display', 978, 120, 338, 76, text='Display ?')
        self.add('checkbox', 'cbx_hlp', 1358, 124, 571, 76, text="Don't show in Help")
        self.add('checkbox', 'cbx_removed', 2007, 124, 334, 76, text='Removed')
        self.add('singlelineedit', 'sle_desc', 507, 224, 1422, 88, limit=60, taborder=20)
        self.add('checkbox', 'cbx_sp', 2007, 224, 311, 76, text='Special?')
        self.add('statictext', 'st_2', 87, 232, 379, 80, text='Description')
        self.add('multilineedit', 'mle_note', 507, 316, 1422, 232, limit=150, taborder=30)
        self.add('statictext', 'st_8', 87, 328, 379, 80, text='Note')
        self.add('checkbox', 'cbx_reserve', 2007, 328, 325, 76, text='Reserved')
        self.add('checkbox', 'cbx_updtfr', 2007, 432, 311, 76, text='Fr')
        self.add('groupbox', 'gb_4', 1838, 516, 549, 724, taborder=70)
        self.add('datawindow', 'dw_grp', 507, 552, 1129, 96, dataobject='d_grcode', taborder=40)
        self.add('commandbutton', 'cb_grpnew', 1650, 560, 133, 84, text='New')
        self.add('statictext', 'st_3', 87, 564, 247, 76, text='Group')
        self.add('statictext', 'st_4', 1888, 564, 462, 132, text='Trading Prof Loss Group Position')
        self.add('datawindow', 'dw_bsgrp', 507, 672, 1129, 88, dataobject='d_bsheadcode', taborder=50)
        self.add('commandbutton', 'cb_bshnew', 1650, 676, 133, 84, text='New')
        self.add('statictext', 'st_10', 119, 680, 302, 76, text='BS Head')
        self.add('editmask', 'em_pos', 2002, 708, 210, 84, taborder=80)
        self.add('groupbox', 'gb_3', 987, 752, 640, 136, taborder=120)
        self.add('editmask', 'em_balance', 507, 788, 439, 104, taborder=60)
        self.add('statictext', 'st_6', 1947, 800, 347, 116, text='BS Schedule Pos')
        self.add('statictext', 'st_5', 87, 804, 421, 72, text='Op. Balance')
        self.add('radiobutton', 'rb_debit', 1010, 804, 274, 52, text='De&bit')
        self.add('radiobutton', 'rb_credit', 1321, 804, 283, 60, text='Credit')
        self.add('groupbox', 'gb_opb', 987, 884, 640, 132, taborder=100)
        self.add('editmask', 'em_balanceb', 507, 916, 439, 104, taborder=130)
        self.add('statictext', 'st_opbalb', 87, 928, 416, 72, text='Op. Balance B')
        self.add('editmask', 'em_shedpos', 2002, 928, 210, 84, taborder=90)
        self.add('radiobutton', 'rb_debitb', 1010, 932, 274, 52, text='De&bit')
        self.add('radiobutton', 'rb_creditb', 1321, 932, 283, 52, text='Credit')
        self.add('statictext', 'st_7', 1897, 1028, 439, 76, text='Schedule Group')
        self.add('groupbox', 'gb_2', 41, 1080, 434, 256, text='Cash/Bank', taborder=150)
        self.add('groupbox', 'gb_1', 512, 1084, 923, 256, text='A/c type', taborder=140)
        self.add('datawindow', 'dw_shedgrp', 1934, 1108, 430, 88, dataobject='d_accode', taborder=110)
        self.add('checkbox', 'cbx_cash', 69, 1152, 265, 64, text='Cas&h')
        self.add('radiobutton', 'rb_revenue', 549, 1156, 379, 72, text='&Revenue')
        self.add('radiobutton', 'rb_asset', 1001, 1156, 315, 72, text='Asse&t')
        self.add('checkbox', 'cbx_bank', 69, 1232, 270, 64, text='Ban&k')
        self.add('radiobutton', 'rb_expense', 549, 1232, 370, 72, text='Ex&pense')
        self.add('radiobutton', 'rb_liability', 1001, 1232, 357, 72, text='&Liability')
        self.add('checkbox', 'cbx_blocked', 1888, 1252, 402, 80, text='Blocked')
        self.add('roundrectangle', 'rr_1', 297, 1344, 1737, 204)
        self.add('commandbutton', 'cb_add', 370, 1404, 242, 92, text='&Add', taborder=160)
        self.add('commandbutton', 'cb_edit', 626, 1404, 242, 92, text='&Edit', taborder=170)
        self.add('commandbutton', 'cb_delete', 887, 1404, 242, 92, text='&Delete', taborder=200)
        self.add('commandbutton', 'cb_save', 1211, 1404, 242, 92, text='&Save', taborder=210)
        self.add('commandbutton', 'cb_cancel', 1467, 1404, 242, 92, text='&Cancel', taborder=220)
        self.add('commandbutton', 'cb_exit', 1728, 1404, 242, 92, text='E&xit', taborder=230)
        self.add('singlelineedit', 'sle_chk', 2039, 1412, 142, 88, text='A', taborder=190)
        self.add('commandbutton', 'cb_coderename', 887, 1560, 567, 92, text='Code Rename', taborder=180)
