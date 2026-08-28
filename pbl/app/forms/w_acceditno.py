"""Edit Rcpt/Pmnt entry — w_acceditno.

Generated from the PowerBuilder window ``w_acceditno.srw`` by
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
    name='w_acceditno',
    title='Edit Rcpt/Pmnt entry',
    width=1362,
    height=628,
    controls=[],
    tables=['pdclist', 'advafter', 'suspentry', 'daybookpart'],
    source_path='w_acceditno.srw',
    opens=['w_accentyhelp', 'w_susprcptpmnt', 'w_ordadvanceafter', 'w_rcpt', 'w_pmnt', 'w_dbcrnote_entry'],
)


class EditRcptPmntEntryForm(GeneratedForm):
    """Edit Rcpt/Pmnt entry"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('singlelineedit', 'sle_bno', 471, 96, 425, 100, taborder=10)
        self.add('commandbutton', 'cb_help', 951, 100, 215, 96, text='&Help', taborder=20)
        self.add('statictext', 'st_1', 27, 112, 430, 72, text='Voucher No  :')
        self.add('oval', 'oval_1', 347, 244, 654, 224)
        self.add('commandbutton', 'cb_ok', 443, 312, 229, 92, text='OK', taborder=30)
        self.add('commandbutton', 'cb_exit', 681, 312, 229, 92, text='E&xit', taborder=21)
