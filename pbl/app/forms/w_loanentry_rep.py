"""Entry Report — w_loanentry_rep.

Generated from the PowerBuilder window ``w_loanentry_rep.srw`` by
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
    name='w_loanentry_rep',
    title='Entry Report',
    width=3653,
    height=2256,
    controls=[],
    tables=['loan', 'loan_dates'],
    source_path='w_loanentry_rep.srw',
    grid={'control': 'dw_1', 'dataobject': 'd_loanentry_rep', 'table': 'loan', 'keys': ['slno'], 'columns': [{'name': 'tdate', 'label': 'tdate', 'type': 'date'}, {'name': 'docno', 'label': 'docno', 'type': 'char'}, {'name': 'billno', 'label': 'billno', 'type': 'char'}, {'name': 'ccode', 'label': 'ccode', 'type': 'char'}, {'name': 'grate', 'label': 'grate', 'type': 'decimal'}, {'name': 'loanamt', 'label': 'loanamt', 'type': 'decimal'}, {'name': 'advance', 'label': 'advance', 'type': 'decimal'}, {'name': 'instnos', 'label': 'instnos', 'type': 'long'}, {'name': 'instamt', 'label': 'instamt', 'type': 'decimal'}, {'name': 'collntype', 'label': 'collntype', 'type': 'char'}, {'name': 'collnstart', 'label': 'collnstart', 'type': 'date'}, {'name': 'closed', 'label': 'closed', 'type': 'char'}, {'name': 'slno', 'label': 'slno', 'type': 'decimal'}, {'name': 'cname', 'label': 'cname', 'type': 'char'}, {'name': 'tcolln', 'label': 'tcolln', 'type': 'decimal'}, {'name': 'tadvadj', 'label': 'tadvadj', 'type': 'decimal'}, {'name': 'disc', 'label': 'disc', 'type': 'decimal'}, {'name': 'tintamt2', 'label': 'tintamt2', 'type': 'decimal'}, {'name': 'loantype', 'label': 'loantype', 'type': 'char'}, {'name': 'interestamt', 'label': 'interestamt', 'type': 'decimal'}, {'name': 'totalamt', 'label': 'totalamt', 'type': 'decimal'}, {'name': 'paidnow', 'label': 'paidnow', 'type': 'decimal'}, {'name': 'tintamt', 'label': 'tintamt', 'type': 'decimal'}]},
    report={'dataobject': 'd_loanentry_rep', 'sql': 'SELECT loan.tdate AS loan_tdate, loan.docno AS loan_docno, loan.billno AS loan_billno, loan.ccode AS loan_ccode, loan.grate AS loan_grate, loan.loanamt AS loan_loanamt, loan.advance AS loan_advance, loan.instnos AS loan_instnos, loan.instamt AS loan_instamt, loan.collntype AS loan_collntype, loan.collnstart AS loan_collnstart, loan.closed AS loan_closed, loan.slno AS loan_slno, loan.disc AS loan_disc, loan.loantype AS loan_loantype, loan.interestamt AS loan_interestamt, loan.totalamt AS loan_totalamt, loan.paidnow AS loan_paidnow, (select clients.name from clients where clients.code = loan.ccode) as cname, (select sum(loancolln.ramt) from loancolln where loancolln.loanno = loan.docno) as tcolln, (select sum(loancolln.advadj) from loancolln where loancolln.loanno = loan.docno) as tadvadj, (select sum(loancolln.intamt) from loancolln where loancolln.loanno = loan.docno) as tintamt2, (interestamt + ifnull(tintamt2,0,tintamt2)) as tintamt FROM loan ORDER BY loan.tdate ASC, loan.docno ASC', 'args': ['rdate1', 'rdate2', 'rlevel'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date', 'rlevel': 'number'}, 'tables': ['loan'], 'columns': [{'name': 'tdate', 'label': 'tdate', 'type': 'date'}, {'name': 'docno', 'label': 'docno', 'type': 'char'}, {'name': 'billno', 'label': 'billno', 'type': 'char'}, {'name': 'ccode', 'label': 'ccode', 'type': 'char'}, {'name': 'grate', 'label': 'grate', 'type': 'decimal'}, {'name': 'loanamt', 'label': 'loanamt', 'type': 'decimal'}, {'name': 'advance', 'label': 'advance', 'type': 'decimal'}, {'name': 'instnos', 'label': 'instnos', 'type': 'long'}, {'name': 'instamt', 'label': 'instamt', 'type': 'decimal'}, {'name': 'collntype', 'label': 'collntype', 'type': 'char'}, {'name': 'collnstart', 'label': 'collnstart', 'type': 'date'}, {'name': 'closed', 'label': 'closed', 'type': 'char'}, {'name': 'slno', 'label': 'slno', 'type': 'decimal'}, {'name': 'cname', 'label': 'cname', 'type': 'char'}, {'name': 'tcolln', 'label': 'tcolln', 'type': 'decimal'}, {'name': 'tadvadj', 'label': 'tadvadj', 'type': 'decimal'}, {'name': 'disc', 'label': 'disc', 'type': 'decimal'}, {'name': 'tintamt2', 'label': 'tintamt2', 'type': 'decimal'}, {'name': 'loantype', 'label': 'loantype', 'type': 'char'}, {'name': 'interestamt', 'label': 'interestamt', 'type': 'decimal'}, {'name': 'totalamt', 'label': 'totalamt', 'type': 'decimal'}, {'name': 'paidnow', 'label': 'paidnow', 'type': 'decimal'}, {'name': 'tintamt', 'label': 'tintamt', 'type': 'decimal'}]},
)


class EntryReportForm(GeneratedForm):
    """Entry Report"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 206, 0, 379, 92, taborder=10)
        self.add('editmask', 'em_date2', 745, 0, 379, 92, taborder=20)
        self.add('dropdownlistbox', 'ddlb_type', 1152, 0, 608, 676, text='Entry', items=['Entry', 'Collection', 'Pending Register'], taborder=60)
        self.add('commandbutton', 'cb_show', 2386, 0, 261, 92, text='&Show', taborder=30)
        self.add('commandbutton', 'cb_sort', 2656, 0, 247, 92, text='So&rt', taborder=40)
        self.add('commandbutton', 'cb_1', 2907, 0, 251, 92, text='Save &As', taborder=90)
        self.add('commandbutton', 'cb_print', 3163, 0, 233, 92, text='&Print', taborder=80)
        self.add('commandbutton', 'cb_exit', 3397, 0, 233, 92, text='E&xit', taborder=100)
        self.add('statictext', 'st_1', 0, 8, 197, 64, text='From :')
        self.add('statictext', 'st_2', 613, 12, 123, 72, text='To :')
        self.add('checkbox', 'cbx_allpending', 1801, 16, 480, 80, text='All Pending')
        self.add('datawindow', 'dw_1', 0, 100, 3630, 2036, dataobject='d_loanentry_rep', taborder=70)
        self.add('commandbutton', 'cb_ledger', 2386, 104, 261, 92, text='Ledger', taborder=51)
        self.add('commandbutton', 'cb_updtdisc', 2656, 104, 741, 92, text='Updt Disc for Not Closed', taborder=50)
