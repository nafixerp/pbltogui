"""Refiner's Summary — w_refnsummary.

Generated from the PowerBuilder window ``w_refnsummary.srw`` by
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
    name='w_refnsummary',
    title="Refiner's Summary",
    width=3675,
    height=2200,
    controls=[],
    tables=['refineryd', 'clients', 'daybook', 'accountm'],
    source_path='w_refnsummary.srw',
    report={'dataobject': 'd_refnsummary', 'sql': 'SELECT refineryd.code AS refineryd_code, items.name AS items_name, refineryd.issuedwgt AS refineryd_issuedwgt, refineryd.issuedqty AS refineryd_issuedqty, refineryd.rcvdwgt AS refineryd_rcvdwgt, refineryd.rcvdqty AS refineryd_rcvdqty, refineryd.bottlestk AS refineryd_bottlestk, refineryd.testpcs AS refineryd_testpcs, refinerym.slno AS refinerym_slno, refinerym.docno AS refinerym_docno, refinerym.tdate AS refinerym_tdate, refinerym.refcode AS refinerym_refcode, refinerym.tbottlestk AS refinerym_tbottlestk, refinerym.ttestpcs AS refinerym_ttestpcs, refinerym.charge AS refinerym_charge, refinerym.paidamt AS refinerym_paidamt, refinerym.testperc AS refinerym_testperc, refinerym.status AS refinerym_status, refinerym.ttime AS refinerym_ttime, refineryd.mudless AS refineryd_mudless, refineryd.issuedstwgt AS refineryd_issuedstwgt FROM items, refineryd, refinerym WHERE items.code = refineryd.code AND refineryd.slno = refinerym.slno AND refinerym.refcode = :rcode AND refinerym.control <= :rlevel AND refinerym.tdate between :rdate1 and :rdate2 ORDER BY refinerym.tdate ASC, refinerym.docno ASC, refinerym.slno ASC', 'args': ['rdate1', 'rdate2', 'rlevel', 'rcode', 'rname', 'rclbalance', 'rclweight', 'rdepwgt'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date', 'rlevel': 'number', 'rcode': 'string', 'rname': 'string', 'rclbalance': 'decimal', 'rclweight': 'decimal', 'rdepwgt': 'decimal'}, 'tables': ['items', 'refineryd', 'refinerym'], 'columns': [{'name': 'refineryd_code', 'label': 'refineryd_code', 'type': 'char'}, {'name': 'items_name', 'label': 'items_name', 'type': 'char'}, {'name': 'refineryd_issuedwgt', 'label': 'refineryd_issuedwgt', 'type': 'decimal'}, {'name': 'refineryd_issuedqty', 'label': 'refineryd_issuedqty', 'type': 'long'}, {'name': 'refineryd_rcvdwgt', 'label': 'refineryd_rcvdwgt', 'type': 'decimal'}, {'name': 'refineryd_rcvdqty', 'label': 'refineryd_rcvdqty', 'type': 'long'}, {'name': 'refineryd_bottlestk', 'label': 'refineryd_bottlestk', 'type': 'decimal'}, {'name': 'refineryd_testpcs', 'label': 'refineryd_testpcs', 'type': 'decimal'}, {'name': 'refinerym_slno', 'label': 'refinerym_slno', 'type': 'decimal'}, {'name': 'refinerym_docno', 'label': 'refinerym_docno', 'type': 'char'}, {'name': 'refinerym_tdate', 'label': 'refinerym_tdate', 'type': 'date'}, {'name': 'refinerym_refcode', 'label': 'refinerym_refcode', 'type': 'char'}, {'name': 'refinerym_tbottlestk', 'label': 'refinerym_tbottlestk', 'type': 'decimal'}, {'name': 'refinerym_ttestpcs', 'label': 'refinerym_ttestpcs', 'type': 'decimal'}, {'name': 'refinerym_charge', 'label': 'refinerym_charge', 'type': 'decimal'}, {'name': 'refinerym_paidamt', 'label': 'refinerym_paidamt', 'type': 'decimal'}, {'name': 'refinerym_testperc', 'label': 'refinerym_testperc', 'type': 'decimal'}, {'name': 'refinerym_status', 'label': 'refinerym_status', 'type': 'long'}, {'name': 'refinerym_ttime', 'label': 'refinerym_ttime', 'type': 'time'}, {'name': 'refineryd_mudless', 'label': 'refineryd_mudless', 'type': 'decimal'}, {'name': 'refineryd_issuedstwgt', 'label': 'refineryd_issuedstwgt', 'type': 'decimal'}]},
)


class RefinerSSummaryForm(GeneratedForm):
    """Refiner's Summary"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('datawindow', 'dw_accode', 325, 0, 425, 96, dataobject='d_refncode', taborder=10)
        self.add('editmask', 'em_date1', 1243, 0, 430, 100, taborder=20)
        self.add('editmask', 'em_date2', 2002, 0, 425, 100, taborder=30)
        self.add('commandbutton', 'cb_show', 2446, 0, 279, 100, text='&Show', taborder=40)
        self.add('commandbutton', 'cb_3', 2807, 0, 256, 96, text='Save &As', taborder=80)
        self.add('commandbutton', 'cb_1', 3077, 0, 265, 96, text='&Print', taborder=70)
        self.add('commandbutton', 'cb_2', 3342, 0, 265, 96, text='E&xit', taborder=60)
        self.add('statictext', 'st_3', 27, 8, 297, 72, text='Refiner  :')
        self.add('statictext', 'st_1', 864, 16, 366, 64, text='Date From :')
        self.add('statictext', 'st_2', 1691, 16, 302, 72, text='Date To :')
        self.add('datawindow', 'dw_1', 0, 100, 3625, 1976, dataobject='d_refnsummary', taborder=50)
