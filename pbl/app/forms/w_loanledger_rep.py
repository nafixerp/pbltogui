"""Loan Ledger — w_loanledger_rep.

Generated from the PowerBuilder window ``w_loanledger_rep.srw`` by
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
    name='w_loanledger_rep',
    title='Loan Ledger',
    width=3675,
    height=2256,
    controls=[],
    tables=['loan', 'loancolln', 'clients'],
    source_path='w_loanledger_rep.srw',
    opens=['w_loanhelp'],
)


class LoanLedgerForm(GeneratedForm):
    """Loan Ledger"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 219, 0, 430, 92, taborder=10)
        self.add('editmask', 'em_date2', 837, 0, 425, 92, taborder=20)
        self.add('singlelineedit', 'sle_loanno', 1618, 0, 425, 92, taborder=30)
        self.add('commandbutton', 'cb_show', 2354, 0, 261, 92, text='&Show')
        self.add('commandbutton', 'cb_sort', 2629, 0, 247, 92, text='So&rt')
        self.add('commandbutton', 'cb_1', 2880, 0, 251, 92, text='Save &As')
        self.add('commandbutton', 'cb_print', 3141, 0, 233, 92, text='&Print')
        self.add('commandbutton', 'cb_exit', 3374, 0, 233, 92, text='E&xit')
        self.add('commandbutton', 'cb_help', 2057, 4, 215, 88, text='&Help')
        self.add('statictext', 'st_1', 0, 8, 219, 64, text='From :')
        self.add('statictext', 'st_3', 1280, 8, 325, 80, text='Loan No. :')
        self.add('statictext', 'st_2', 686, 12, 133, 72, text='To :')
        self.add('datawindow', 'dw_1', 0, 100, 3630, 2036, dataobject='d_loanledger_rep', taborder=40)
        self.add('checkbox', 'cbx_showinterest', 2359, 124, 443, 68, text='Show Interest')
