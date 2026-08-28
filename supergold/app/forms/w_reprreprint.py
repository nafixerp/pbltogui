"""Reprint — w_reprreprint.

Generated from the PowerBuilder window ``w_reprreprint.srw`` by
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
    name='w_reprreprint',
    title='Reprint',
    width=1403,
    height=728,
    controls=[],
    tables=['repairm'],
    source_path='w_reprreprint.srw',
    report={'dataobject': 'd_repairprint_thermal', 'sql': 'SELECT items.name AS items_name, items.itype AS items_itype, items.printvaamt AS items_printvaamt, repairm.billno AS repairm_billno, repairm.tdate AS repairm_tdate, repairm.duedate AS repairm_duedate, repairm.custname AS repairm_custname, repairm.amount AS repairm_amount, repairm.discount AS repairm_discount, repairm.rcvd AS repairm_rcvd, repairm.addr AS repairm_addr, repairm.sman AS repairm_sman, repairm.advance AS repairm_advance, repairm.taxamt AS repairm_taxamt, repairm.taxperc AS repairm_taxperc, repaird.name AS repaird_name, repaird.weight AS repaird_weight, repaird.qty AS repaird_qty, repaird.stonewgt AS repaird_stonewgt, repaird.stoneprice AS repaird_stoneprice, repaird.mcharge AS repaird_mcharge, repaird.addwgt AS repaird_addwgt, repaird.amount AS repaird_amount, repaird.complaint AS repaird_complaint, repaird.givrec AS repaird_givrec, repaird.rate AS repaird_rate, repaird.netwgt AS repaird_netwgt, repairm.givrec AS repairm_givrec FROM items, repaird, repairm WHERE items.code = repaird.code AND repaird.slno = repairm.slno ORDER BY repaird.sno ASC', 'computes': [{'name': 'itemname', 'expression': ' items_name ', 'format': '[General]', 'label': 'itemname', 'band': 'detail'}, {'name': 'compute_16', 'expression': ' repaird_qty ', 'format': '######', 'label': 'compute_16', 'band': 'detail'}, {'name': 'compute_17', 'expression': ' repaird_weight ', 'format': '####0.000', 'label': 'compute_17', 'band': 'detail'}, {'name': 'tstwgt', 'expression': ' repaird_stonewgt ', 'format': '######0.000', 'label': 'tstwgt', 'band': 'detail'}, {'name': 'tstamt', 'expression': ' repaird_stoneprice ', 'format': '#####0.00', 'label': 'tstamt', 'band': 'detail'}, {'name': 'compute_5', 'expression': '  sum(  repaird_amount for all) ', 'format': '#########0.00', 'label': 'compute_5', 'band': 'summary'}], 'args': ['rslno'], 'arg_types': {'rslno': 'number'}, 'tables': ['items', 'repaird', 'repairm'], 'columns': [{'name': 'items_name', 'label': 'items_name', 'type': 'char'}, {'name': 'items_itype', 'label': 'items_itype', 'type': 'char'}, {'name': 'items_printvaamt', 'label': 'items_printvaamt', 'type': 'char'}, {'name': 'repairm_billno', 'label': 'repairm_billno', 'type': 'char'}, {'name': 'repairm_tdate', 'label': 'repairm_tdate', 'type': 'date'}, {'name': 'repairm_duedate', 'label': 'repairm_duedate', 'type': 'date'}, {'name': 'repairm_custname', 'label': 'repairm_custname', 'type': 'char'}, {'name': 'repairm_amount', 'label': 'repairm_amount', 'type': 'decimal'}, {'name': 'repairm_discount', 'label': 'repairm_discount', 'type': 'decimal'}, {'name': 'repairm_rcvd', 'label': 'repairm_rcvd', 'type': 'decimal'}, {'name': 'repairm_addr', 'label': 'repairm_addr', 'type': 'char'}, {'name': 'repairm_sman', 'label': 'repairm_sman', 'type': 'char'}, {'name': 'repairm_advance', 'label': 'repairm_advance', 'type': 'decimal'}, {'name': 'repairm_taxamt', 'label': 'repairm_taxamt', 'type': 'decimal'}, {'name': 'repairm_taxperc', 'label': 'repairm_taxperc', 'type': 'decimal'}, {'name': 'repaird_name', 'label': 'repaird_name', 'type': 'char'}, {'name': 'repaird_weight', 'label': 'repaird_weight', 'type': 'decimal'}, {'name': 'repaird_qty', 'label': 'repaird_qty', 'type': 'long'}, {'name': 'repaird_stonewgt', 'label': 'repaird_stonewgt', 'type': 'decimal'}, {'name': 'repaird_stoneprice', 'label': 'repaird_stoneprice', 'type': 'decimal'}, {'name': 'repaird_mcharge', 'label': 'repaird_mcharge', 'type': 'decimal'}, {'name': 'repaird_addwgt', 'label': 'repaird_addwgt', 'type': 'decimal'}, {'name': 'repaird_amount', 'label': 'repaird_amount', 'type': 'decimal'}, {'name': 'repaird_complaint', 'label': 'repaird_complaint', 'type': 'char'}, {'name': 'repaird_givrec', 'label': 'repaird_givrec', 'type': 'char'}, {'name': 'repaird_rate', 'label': 'repaird_rate', 'type': 'decimal'}, {'name': 'repaird_netwgt', 'label': 'repaird_netwgt', 'type': 'decimal'}, {'name': 'repairm_givrec', 'label': 'repairm_givrec', 'type': 'char'}]},
    opens=['w_repairhelp', 'w_repairprint_view'],
    prints=['d_repairprint_thermal'],
)


class ReprintForm(GeneratedForm):
    """Reprint"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('singlelineedit', 'sle_billno', 544, 140, 421, 92, limit=13, taborder=10)
        self.add('commandbutton', 'cb_help', 1001, 140, 229, 100, text='&Help', taborder=20)
        self.add('statictext', 'st_1', 114, 152, 485, 64, text='Enter Doc No :')
        self.add('checkbox', 'cbx_laser', 549, 260, 398, 80, text='Laser Print')
        self.add('datawindow', 'dw_print', 27, 280, 229, 188, dataobject='d_repairprint_thermal', taborder=50)
        self.add('commandbutton', 'cb_ok', 439, 408, 256, 100, text='&OK', taborder=30)
        self.add('commandbutton', 'cb_exit', 704, 408, 256, 100, text='E&xit', taborder=40)
