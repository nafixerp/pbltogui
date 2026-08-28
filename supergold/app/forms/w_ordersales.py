"""Order Returns — w_ordersales.

Generated from the PowerBuilder window ``w_ordersales.srw`` by
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
    name='w_ordersales',
    title='Order Returns',
    width=3662,
    height=2248,
    controls=[],
    tables=['date'],
    source_path='w_ordersales.srw',
    report={'dataobject': 'd_ordersales', 'sql': 'SELECT orderm.ordno AS orderm_ordno, orderm.tdate AS orderm_tdate, orderm.duedate AS orderm_duedate, orderm.rate AS orderm_rate, orderm.custname AS orderm_custname, orderm.billamt AS orderm_billamt, orderm.eamt AS orderm_eamt, orderm.advance AS orderm_advance, salesm.slno AS salesm_slno, salesm.billno AS salesm_billno, salesm.tdate AS salesm_tdate, salesm.ttime AS salesm_ttime, salesm.custname AS salesm_custname, salesm.billamt AS salesm_billamt, salesm.eamt AS salesm_eamt, salesm.staxamt AS salesm_staxamt, salesm.discount AS salesm_discount, salesm.ramt AS salesm_ramt, salesm.grate AS salesm_grate, orderm.smcode AS orderm_smcode, orderm.gadvance AS orderm_gadvance, orderm.slno AS orderm_slno, salesm.sretamt AS salesm_sretamt, salesm.round AS salesm_round, salesm.advance AS salesm_advance, salesm.astamt AS salesm_astamt, (select name from sman where code = orderm.smcode) as csmname FROM orderm, salesm WHERE orderm.salebill = salesm.billno AND orderm.control <= :rlevel ORDER BY orderm.tdate ASC', 'args': ['rdate1', 'rdate2', 'rlevel'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date', 'rlevel': 'number'}, 'tables': ['orderm', 'salesm'], 'columns': [{'name': 'orderm_ordno', 'label': 'orderm_ordno', 'type': 'char'}, {'name': 'orderm_tdate', 'label': 'orderm_tdate', 'type': 'date'}, {'name': 'orderm_duedate', 'label': 'orderm_duedate', 'type': 'date'}, {'name': 'orderm_rate', 'label': 'orderm_rate', 'type': 'decimal'}, {'name': 'orderm_custname', 'label': 'orderm_custname', 'type': 'char'}, {'name': 'orderm_billamt', 'label': 'orderm_billamt', 'type': 'decimal'}, {'name': 'orderm_eamt', 'label': 'orderm_eamt', 'type': 'decimal'}, {'name': 'orderm_advance', 'label': 'orderm_advance', 'type': 'decimal'}, {'name': 'salesm_slno', 'label': 'salesm_slno', 'type': 'decimal'}, {'name': 'salesm_billno', 'label': 'salesm_billno', 'type': 'char'}, {'name': 'salesm_tdate', 'label': 'salesm_tdate', 'type': 'date'}, {'name': 'salesm_ttime', 'label': 'salesm_ttime', 'type': 'time'}, {'name': 'salesm_custname', 'label': 'salesm_custname', 'type': 'char'}, {'name': 'salesm_billamt', 'label': 'salesm_billamt', 'type': 'decimal'}, {'name': 'salesm_eamt', 'label': 'salesm_eamt', 'type': 'decimal'}, {'name': 'salesm_staxamt', 'label': 'salesm_staxamt', 'type': 'decimal'}, {'name': 'salesm_discount', 'label': 'salesm_discount', 'type': 'decimal'}, {'name': 'salesm_ramt', 'label': 'salesm_ramt', 'type': 'decimal'}, {'name': 'salesm_grate', 'label': 'salesm_grate', 'type': 'decimal'}, {'name': 'orderm_smcode', 'label': 'orderm_smcode', 'type': 'char'}, {'name': 'ccsmname', 'label': 'ccsmname', 'type': 'char'}, {'name': 'orderm_gadvance', 'label': 'orderm_gadvance', 'type': 'decimal'}, {'name': 'orderm_slno', 'label': 'orderm_slno', 'type': 'decimal'}, {'name': 'salesm_sretamt', 'label': 'salesm_sretamt', 'type': 'decimal'}, {'name': 'salesm_round', 'label': 'salesm_round', 'type': 'decimal'}, {'name': 'salesm_advance', 'label': 'salesm_advance', 'type': 'decimal'}, {'name': 'salesm_astamt', 'label': 'salesm_astamt', 'type': 'decimal'}]},
)


class OrderReturnsForm(GeneratedForm):
    """Order Returns"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('commandbutton', 'cb_3', 2647, 0, 265, 100, text='Save &As', taborder=60)
        self.add('commandbutton', 'cb_1', 2917, 0, 247, 100, text='&Print', taborder=70)
        self.add('commandbutton', 'cb_2', 3168, 0, 247, 100, text='E&xit', taborder=50)
        self.add('editmask', 'em_date', 370, 8, 393, 88, taborder=10)
        self.add('editmask', 'em_date2', 1079, 8, 393, 88, taborder=20)
        self.add('commandbutton', 'cb_show', 1504, 8, 270, 96, text='&Show', taborder=30)
        self.add('statictext', 'st_date1', 14, 12, 347, 76, text='From date :')
        self.add('statictext', 'st_date2', 795, 16, 274, 76, text='To Date :')
        self.add('datawindow', 'dw_1', 9, 124, 3607, 2020, dataobject='d_ordersales', taborder=40)
