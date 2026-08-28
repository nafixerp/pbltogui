"""Monthly Sales — w_mnthsalereport.

Generated from the PowerBuilder window ``w_mnthsalereport.srw`` by
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
    name='w_mnthsalereport',
    title='Monthly Sales',
    width=3639,
    height=2212,
    controls=[],
    tables=[],
    source_path='w_mnthsalereport.srw',
    grid={'control': 'dw_mnthreport', 'dataobject': 'd_mnthsalereport', 'table': 'salesm', 'keys': ['slno'], 'columns': [{'name': 'slno', 'label': 'slno', 'type': 'decimal'}, {'name': 'billno', 'label': 'Bill No.', 'type': 'char'}, {'name': 'tdate', 'label': 'tdate', 'type': 'date'}, {'name': 'custcode', 'label': 'custcode', 'type': 'char'}, {'name': 'custname', 'label': 'Customer Code and Name', 'type': 'char'}, {'name': 'billamt', 'label': 'Bill Amt', 'type': 'decimal'}, {'name': 'eamt', 'label': 'eamt', 'type': 'decimal'}, {'name': 'staxamt', 'label': 'staxamt', 'type': 'decimal'}, {'name': 'discount', 'label': 'Discount', 'type': 'decimal'}, {'name': 'ramt', 'label': 'Received', 'type': 'decimal'}, {'name': 'sretamt', 'label': 'sretamt', 'type': 'decimal'}, {'name': 'ramtafter', 'label': 'ramtafter', 'type': 'decimal'}, {'name': 'round', 'label': 'round', 'type': 'decimal'}, {'name': 'advance', 'label': 'advance', 'type': 'decimal'}, {'name': 'smcode', 'label': 'smcode', 'type': 'char'}]},
    report={'dataobject': 'd_mnthsalereport', 'sql': "SELECT salesm.slno AS salesm_slno, salesm.billno AS salesm_billno, salesm.tdate AS salesm_tdate, salesm.custcode AS salesm_custcode, salesm.custname AS salesm_custname, salesm.billamt AS salesm_billamt, salesm.eamt AS salesm_eamt, salesm.staxamt AS salesm_staxamt, salesm.discount AS salesm_discount, salesm.ramt AS salesm_ramt, salesm.sretamt AS salesm_sretamt, salesm.ramtafter AS salesm_ramtafter, salesm.round AS salesm_round, salesm.advance AS salesm_advance, salesm.smcode AS salesm_smcode FROM salesm WHERE salesm.control <= :rlevel AND salesm.sr = 'S' ORDER BY salesm.tdate ASC, salesm.slno ASC", 'args': ['rdate1', 'rdate2', 'rlevel', 'rsmcode'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date', 'rlevel': 'number', 'rsmcode': 'string'}, 'tables': ['salesm'], 'columns': [{'name': 'slno', 'label': 'slno', 'type': 'decimal'}, {'name': 'billno', 'label': 'Bill No.', 'type': 'char'}, {'name': 'tdate', 'label': 'tdate', 'type': 'date'}, {'name': 'custcode', 'label': 'custcode', 'type': 'char'}, {'name': 'custname', 'label': 'Customer Code and Name', 'type': 'char'}, {'name': 'billamt', 'label': 'Bill Amt', 'type': 'decimal'}, {'name': 'eamt', 'label': 'eamt', 'type': 'decimal'}, {'name': 'staxamt', 'label': 'staxamt', 'type': 'decimal'}, {'name': 'discount', 'label': 'Discount', 'type': 'decimal'}, {'name': 'ramt', 'label': 'Received', 'type': 'decimal'}, {'name': 'sretamt', 'label': 'sretamt', 'type': 'decimal'}, {'name': 'ramtafter', 'label': 'ramtafter', 'type': 'decimal'}, {'name': 'round', 'label': 'round', 'type': 'decimal'}, {'name': 'advance', 'label': 'advance', 'type': 'decimal'}, {'name': 'smcode', 'label': 'smcode', 'type': 'char'}]},
)


class MonthlySalesForm(GeneratedForm):
    """Monthly Sales"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 210, 0, 411, 96, taborder=10)
        self.add('editmask', 'em_date2', 763, 0, 411, 96, taborder=10)
        self.add('commandbutton', 'cb_show', 2505, 0, 270, 96, text='&Show', taborder=20)
        self.add('commandbutton', 'cb_4', 2775, 0, 270, 96, text='Save &As', taborder=70)
        self.add('commandbutton', 'cb_1', 3054, 0, 270, 96, text='&Print', taborder=60)
        self.add('commandbutton', 'cb_2', 3323, 0, 270, 96, text='E&xit', taborder=50)
        self.add('datawindow', 'dw_smcode', 1335, 4, 677, 88, dataobject='d_smancode', taborder=20)
        self.add('checkbox', 'cbx_daysummary', 2098, 8, 398, 76, text='&Day Summary')
        self.add('statictext', 'st_1', 0, 12, 201, 80, text='From :')
        self.add('statictext', 'st_2', 635, 12, 119, 64, text='To :')
        self.add('statictext', 'st_3', 1179, 12, 151, 64, text='SM :')
        self.add('datawindow', 'dw_mnthreport', 5, 104, 3589, 2000, dataobject='d_mnthsalereport', taborder=40)
        self.add('commandbutton', 'cb_3', 2775, 112, 270, 96, text='&Graph', taborder=30)
