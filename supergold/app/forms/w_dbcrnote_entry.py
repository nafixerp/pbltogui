"""Debit/Credit Note — w_dbcrnote_entry.

Generated from the PowerBuilder window ``w_dbcrnote_entry.srw`` by
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
    name='w_dbcrnote_entry',
    title='Debit/Credit Note',
    width=3150,
    height=1564,
    controls=[],
    tables=['daybook', 'accountm', 'clients', 'generali', 'daybookpart', 'delpart', 'userd'],
    source_path='w_dbcrnote_entry.srw',
    opens=['w_cbachdhelp'],
)


class DebitCreditNoteForm(GeneratedForm):
    """Debit/Credit Note"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('dropdownlistbox', 'ddlb_rp', 681, 44, 430, 400, text='Credit Note', items=['Credit Note', 'Debit Note'], taborder=10)
        self.add('statictext', 'st_7', 315, 60, 347, 76, text='Type :')
        self.add('statictext', 'st_vchno', 681, 156, 430, 88)
        self.add('statictext', 'st_vchnot', 238, 168, 425, 72, text='Doc No. :')
        self.add('editmask', 'em_date', 681, 256, 430, 88, taborder=20)
        self.add('statictext', 'st_8', 389, 260, 274, 72, text='Date :')
        self.add('datawindow', 'dw_adjac', 681, 352, 430, 88, dataobject='d_accode', taborder=30)
        self.add('commandbutton', 'cb_adjachelp', 1111, 356, 64, 84, text='^')
        self.add('statictext', 'st_adjdesc', 1179, 356, 1056, 88)
        self.add('statictext', 'st_1', 110, 364, 553, 80, text='Adjusted Account :')
        self.add('datawindow', 'dw_staff', 681, 448, 677, 88, dataobject='d_smancode', taborder=40)
        self.add('statictext', 'st_2', 416, 456, 247, 76, text='SMan :')
        self.add('datawindow', 'dw_accode', 681, 548, 430, 88, dataobject='d_accode', taborder=50)
        self.add('commandbutton', 'cb_achelp', 1111, 552, 64, 84, text='^')
        self.add('statictext', 'st_desc', 1179, 552, 1056, 88)
        self.add('editmask', 'em_balance', 2400, 552, 393, 88)
        self.add('statictext', 'st_accode', 96, 556, 567, 72, text='Credited Account :')
        self.add('statictext', 'st_5', 2235, 556, 155, 80, text='OB :')
        self.add('statictext', 'st_dbcr', 2811, 556, 178, 76)
        self.add('editmask', 'em_amount', 681, 648, 430, 96, taborder=60)
        self.add('statictext', 'st_6', 238, 656, 425, 72, text='Amount :')
        self.add('editmask', 'em_taxperc', 681, 756, 133, 96, taborder=70)
        self.add('editmask', 'em_taxamt', 814, 756, 297, 96, taborder=80)
        self.add('statictext', 'st_4', 238, 764, 425, 72, text='Tax :')
        self.add('editmask', 'em_totalamt', 681, 864, 430, 96)
        self.add('statictext', 'st_9', 466, 868, 197, 80, text='Total :')
        self.add('singlelineedit', 'sle_part', 681, 976, 1554, 88, limit=70, taborder=90)
        self.add('statictext', 'st_3', 215, 984, 448, 72, text='Description :')
        self.add('checkbox', 'cbx_printslip', 1801, 1080, 416, 84, text='Pri&nt Slip')
        self.add('checkbox', 'cbx_printobcb', 1801, 1172, 466, 84, text='Print OB/CB')
        self.add('commandbutton', 'cb_ok', 686, 1192, 293, 132, text='&Save')
        self.add('commandbutton', 'cb_cancel', 992, 1192, 293, 132, text='&Cancel')
        self.add('commandbutton', 'cb_exit', 1298, 1192, 293, 132, text='&Exit')
        self.add('checkbox', 'cbx_sendsms', 1801, 1264, 402, 80, text='Send Sms')
