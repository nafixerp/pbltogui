"""Cheque Clearance — w_pdc_colln.

Generated from the PowerBuilder window ``w_pdc_colln.srw`` by
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
    name='w_pdc_colln',
    title='Cheque Clearance',
    width=2149,
    height=1584,
    controls=[],
    tables=['daybook', 'pdclist', 'clients', 'accountm', 'collection', 'generali', 'daybookpart'],
    source_path='w_pdc_colln.srw',
    opens=['w_pdc_chqhelp'],
)


class ChequeClearanceForm(GeneratedForm):
    """Cheque Clearance"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('statictext', 'st_vchno', 855, 36, 425, 96)
        self.add('statictext', 'st_4', 457, 48, 389, 76, text='Doc.No. :')
        self.add('statictext', 'st_type', 1303, 52, 709, 76)
        self.add('editmask', 'em_date', 855, 136, 425, 96, taborder=10)
        self.add('statictext', 'st_5', 658, 148, 187, 76, text='Date :')
        self.add('singlelineedit', 'sle_chequeno', 855, 236, 425, 96, limit=20, taborder=20)
        self.add('commandbutton', 'cb_help', 1289, 240, 224, 88, text='Help')
        self.add('statictext', 'st_1', 457, 248, 389, 76, text='Cheque No. :')
        self.add('editmask', 'em_chqdate', 855, 336, 425, 96, taborder=30)
        self.add('statictext', 'st_2', 457, 348, 389, 76, text='Cheque Dt :')
        self.add('statictext', 'st_partycode', 1472, 356, 393, 80)
        self.add('statictext', 'st_partyname', 855, 440, 1010, 80)
        self.add('statictext', 'st_10', 457, 444, 389, 76, text='Party Name :')
        self.add('datawindow', 'dw_bank', 855, 524, 878, 88, dataobject='d_cashbankcode', taborder=40)
        self.add('statictext', 'st_3', 457, 532, 389, 76, text='Bank :')
        self.add('editmask', 'em_amount', 855, 620, 425, 96)
        self.add('statictext', 'st_6', 571, 628, 274, 76, text='Amount :')
        self.add('editmask', 'em_expense', 855, 724, 425, 96, taborder=50)
        self.add('statictext', 'st_7', 521, 728, 325, 76, text='Bank Exp :')
        self.add('editmask', 'em_scharge', 855, 828, 425, 96, taborder=60)
        self.add('statictext', 'st_9', 210, 832, 635, 76, text='Interest && SCharge :')
        self.add('checkbox', 'cbx_bounce', 1312, 832, 471, 80, text='Chq Bounced')
        self.add('editmask', 'em_netamt', 855, 932, 425, 96)
        self.add('statictext', 'st_8', 521, 944, 325, 76, text='Net Amt :')
        self.add('oval', 'oval_1', 745, 1040, 654, 280)
        self.add('checkbox', 'cbx_fr', 1417, 1076, 210, 80, text='Fr')
        self.add('commandbutton', 'cb_save', 878, 1080, 393, 96, text='&Save', taborder=70)
        self.add('commandbutton', 'cb_exit', 878, 1184, 393, 96, text='E&xit', taborder=80)
