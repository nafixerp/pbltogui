"""Suspense Entry — w_susprcptpmnt.

Generated from the PowerBuilder window ``w_susprcptpmnt.srw`` by
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
    name='w_susprcptpmnt',
    title='Suspense Entry',
    width=3497,
    height=1944,
    controls=[],
    tables=['suspentry', 'accountm', 'daybook', 'kuricolln', 'daybookratewgt', 'stkandprof', 'clients', 'generali', 'daybookpart', 'delpart', 'userd'],
    source_path='w_susprcptpmnt.srw',
    opens=['w_suspmaster', 'w_acsusphelp', 'w_cbachdhelp'],
)


class SuspenseEntryForm(GeneratedForm):
    """Suspense Entry"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('statictext', 'st_vchno', 681, 92, 411, 88)
        self.add('statictext', 'st_vchnot', 247, 104, 425, 72, text='Voucher No. :')
        self.add('editmask', 'em_date', 681, 192, 407, 88, taborder=10)
        self.add('statictext', 'st_8', 398, 196, 274, 72, text='Date :')
        self.add('datawindow', 'dw_cashbank', 681, 292, 882, 88, dataobject='d_cashbankcode', taborder=20)
        self.add('statictext', 'st_1', 137, 304, 535, 72, text='Cash/Bank Code :')
        self.add('datawindow', 'dw_staff', 681, 392, 677, 88, dataobject='d_smancode', taborder=30)
        self.add('statictext', 'st_2', 425, 400, 247, 76, text='SMan :')
        self.add('dropdownlistbox', 'ddlb_rp', 681, 492, 480, 400, text='Payment', items=['Payment', 'Receipt'], taborder=40)
        self.add('statictext', 'st_7', 325, 508, 347, 76, text='Rcpt/Pmnt :')
        self.add('datawindow', 'dw_accode', 681, 604, 430, 88, dataobject='d_accode', taborder=50)
        self.add('editmask', 'em_balance', 2400, 604, 393, 96)
        self.add('commandbutton', 'cb_achelp', 1111, 608, 64, 84, text='^')
        self.add('statictext', 'st_desc', 1179, 608, 1056, 88)
        self.add('statictext', 'st_5', 2235, 608, 155, 80, text='OB :')
        self.add('statictext', 'st_4', 247, 612, 425, 72, text='A/C Code :')
        self.add('statictext', 'st_dbcr', 2811, 640, 178, 76)
        self.add('datawindow', 'dw_scode', 681, 708, 1138, 88, dataobject='d_suspcode', taborder=60)
        self.add('commandbutton', 'cb_new', 1838, 708, 215, 92, text='New', taborder=70)
        self.add('editmask', 'em_cb', 2400, 708, 393, 88)
        self.add('statictext', 'st_9', 233, 712, 439, 72, text='Suspense A/c :')
        self.add('statictext', 'st_11', 2267, 712, 123, 80, text='CB :')
        self.add('editmask', 'em_amount', 681, 808, 407, 96, taborder=70)
        self.add('singlelineedit', 'sle_vchno2', 1765, 808, 407, 96, limit=10, taborder=80)
        self.add('commandbutton', 'cb_sushelp', 2171, 808, 64, 92, text='^')
        self.add('statictext', 'st_susvchno', 1184, 812, 562, 80, text='Against Sus.Entry :')
        self.add('statictext', 'st_6', 247, 816, 425, 72, text='Amount :')
        self.add('singlelineedit', 'sle_part', 681, 916, 1554, 88, limit=70, taborder=90)
        self.add('statictext', 'st_3', 224, 924, 448, 72, text='Description :')
        self.add('oval', 'oval_1', 905, 1128, 1015, 260)
        self.add('checkbox', 'cbx_printslip', 2309, 1144, 416, 84, text='Pri&nt Slip')
        self.add('commandbutton', 'cb_ok', 1065, 1204, 238, 100, text='&Save', taborder=100)
        self.add('commandbutton', 'cb_cancel', 1312, 1204, 238, 100, text='&Cancel', taborder=110)
        self.add('commandbutton', 'cb_exit', 1559, 1204, 238, 100, text='&Exit', taborder=120)
        self.add('checkbox', 'cbx_printobcb', 2309, 1236, 466, 84, text='Print OB/CB')
        self.add('checkbox', 'cbx_sendsms', 2309, 1328, 402, 80, text='Send Sms')
