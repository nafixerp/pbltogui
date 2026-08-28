"""Remake Returns — w_repairreturns.

Generated from the PowerBuilder window ``w_repairreturns.srw`` by
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
    name='w_repairreturns',
    title='Remake Returns',
    width=3493,
    height=2184,
    controls=[],
    tables=[],
    source_path='w_repairreturns.srw',
    report={'dataobject': 'd_repairreturns', 'sql': "SELECT repaird.slno AS repaird_slno, repaird.code AS repaird_code, repaird.name AS repaird_name, repaird.weight AS repaird_weight, repaird.qty AS repaird_qty, repaird.stonewgt AS repaird_stonewgt, repaird.complaint AS repaird_complaint, repaird.addwgt AS repaird_addwgt, repaird.amount AS repaird_amount, repairm.status AS repairm_status, repaird.mcharge AS repaird_mcharge, repaird.rate AS repaird_rate, repaird.wastage AS repaird_wastage, repairm.slno AS repairm_slno, repairm.billno AS repairm_billno, repairm.tdate AS repairm_tdate, repairm.duedate AS repairm_duedate, repairm.custname AS repairm_custname, repairm.amount AS repairm_amount, repairm.discount AS repairm_discount, repairm.rcvd AS repairm_rcvd, repairm.rbillno AS repairm_rbillno, repairm.taxamt AS repairm_taxamt FROM repaird, repairm WHERE repaird.slno = repairm.slno AND repairm.givrec = 'G' ORDER BY repairm.slno ASC, repairm.status DESC", 'computes': [{'name': 'compute_4', 'expression': "'Page ' + page() + ' of ' + pageCount()", 'format': '[general]', 'label': 'compute_4', 'band': 'summary'}], 'args': ['rdate1', 'rdate2'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date'}, 'tables': ['repaird', 'repairm'], 'columns': [{'name': 'repaird_slno', 'label': 'repaird_slno', 'type': 'decimal'}, {'name': 'repaird_code', 'label': 'repaird_code', 'type': 'char'}, {'name': 'repaird_name', 'label': 'repaird_name', 'type': 'char'}, {'name': 'repaird_weight', 'label': 'repaird_weight', 'type': 'decimal'}, {'name': 'repaird_qty', 'label': 'repaird_qty', 'type': 'long'}, {'name': 'repaird_stonewgt', 'label': 'repaird_stonewgt', 'type': 'decimal'}, {'name': 'repaird_complaint', 'label': 'repaird_complaint', 'type': 'char'}, {'name': 'repaird_addwgt', 'label': 'repaird_addwgt', 'type': 'decimal'}, {'name': 'repaird_amount', 'label': 'repaird_amount', 'type': 'decimal'}, {'name': 'repairm_status', 'label': 'repairm_status', 'type': 'long'}, {'name': 'repaird_mcharge', 'label': 'repaird_mcharge', 'type': 'decimal'}, {'name': 'repaird_rate', 'label': 'repaird_rate', 'type': 'decimal'}, {'name': 'repaird_wastage', 'label': 'repaird_wastage', 'type': 'decimal'}, {'name': 'repairm_slno', 'label': 'repairm_slno', 'type': 'decimal'}, {'name': 'repairm_billno', 'label': 'repairm_billno', 'type': 'char'}, {'name': 'repairm_tdate', 'label': 'repairm_tdate', 'type': 'date'}, {'name': 'repairm_duedate', 'label': 'repairm_duedate', 'type': 'date'}, {'name': 'repairm_custname', 'label': 'repairm_custname', 'type': 'char'}, {'name': 'repairm_amount', 'label': 'repairm_amount', 'type': 'decimal'}, {'name': 'repairm_discount', 'label': 'repairm_discount', 'type': 'decimal'}, {'name': 'repairm_rcvd', 'label': 'repairm_rcvd', 'type': 'decimal'}, {'name': 'repairm_rbillno', 'label': 'repairm_rbillno', 'type': 'char'}, {'name': 'repairm_taxamt', 'label': 'repairm_taxamt', 'type': 'decimal'}]},
)


class RemakeReturnsForm(GeneratedForm):
    """Remake Returns"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 416, 0, 375, 92, taborder=1)
        self.add('editmask', 'em_date2', 1143, 0, 375, 92, taborder=10)
        self.add('commandbutton', 'cb_show', 1637, 0, 293, 96, text='&Show', taborder=20)
        self.add('commandbutton', 'cb_3', 2469, 0, 265, 96, text='Save &As', taborder=50)
        self.add('commandbutton', 'cb_1', 2734, 0, 274, 96, text='&Print', taborder=60)
        self.add('commandbutton', 'cb_2', 3008, 0, 251, 96, text='E&xit', taborder=40)
        self.add('statictext', 'st_8', 14, 12, 393, 64, text='Date From :')
        self.add('statictext', 'st_2', 823, 12, 302, 72, text='Date To  :')
        self.add('datawindow', 'dw_1', 0, 104, 3497, 1932, dataobject='d_repairreturns', taborder=30)
