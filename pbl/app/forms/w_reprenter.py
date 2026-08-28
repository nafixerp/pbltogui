"""New — w_reprenter.

Generated from the PowerBuilder window ``w_reprenter.srw`` by
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
    name='w_reprenter',
    title='New',
    width=3643,
    height=1644,
    controls=[],
    tables=['repaird', 'items', 'repairm', 'itemsstk', 'stktype', 'sman', 'clients', 'generali'],
    source_path='w_reprenter.srw',
    report={'dataobject': 'd_repairprint_thermal', 'sql': 'SELECT items.name AS items_name, items.itype AS items_itype, items.printvaamt AS items_printvaamt, repairm.billno AS repairm_billno, repairm.tdate AS repairm_tdate, repairm.duedate AS repairm_duedate, repairm.custname AS repairm_custname, repairm.amount AS repairm_amount, repairm.discount AS repairm_discount, repairm.rcvd AS repairm_rcvd, repairm.addr AS repairm_addr, repairm.sman AS repairm_sman, repairm.advance AS repairm_advance, repairm.taxamt AS repairm_taxamt, repairm.taxperc AS repairm_taxperc, repaird.name AS repaird_name, repaird.weight AS repaird_weight, repaird.qty AS repaird_qty, repaird.stonewgt AS repaird_stonewgt, repaird.stoneprice AS repaird_stoneprice, repaird.mcharge AS repaird_mcharge, repaird.addwgt AS repaird_addwgt, repaird.amount AS repaird_amount, repaird.complaint AS repaird_complaint, repaird.givrec AS repaird_givrec, repaird.rate AS repaird_rate, repaird.netwgt AS repaird_netwgt, repairm.givrec AS repairm_givrec FROM items, repaird, repairm WHERE items.code = repaird.code AND repaird.slno = repairm.slno ORDER BY repaird.sno ASC', 'args': ['rslno'], 'arg_types': {'rslno': 'number'}, 'tables': ['items', 'repaird', 'repairm'], 'columns': [{'name': 'items_name', 'label': 'items_name', 'type': 'char'}, {'name': 'items_itype', 'label': 'items_itype', 'type': 'char'}, {'name': 'items_printvaamt', 'label': 'items_printvaamt', 'type': 'char'}, {'name': 'repairm_billno', 'label': 'repairm_billno', 'type': 'char'}, {'name': 'repairm_tdate', 'label': 'repairm_tdate', 'type': 'date'}, {'name': 'repairm_duedate', 'label': 'repairm_duedate', 'type': 'date'}, {'name': 'repairm_custname', 'label': 'repairm_custname', 'type': 'char'}, {'name': 'repairm_amount', 'label': 'repairm_amount', 'type': 'decimal'}, {'name': 'repairm_discount', 'label': 'repairm_discount', 'type': 'decimal'}, {'name': 'repairm_rcvd', 'label': 'repairm_rcvd', 'type': 'decimal'}, {'name': 'repairm_addr', 'label': 'repairm_addr', 'type': 'char'}, {'name': 'repairm_sman', 'label': 'repairm_sman', 'type': 'char'}, {'name': 'repairm_advance', 'label': 'repairm_advance', 'type': 'decimal'}, {'name': 'repairm_taxamt', 'label': 'repairm_taxamt', 'type': 'decimal'}, {'name': 'repairm_taxperc', 'label': 'repairm_taxperc', 'type': 'decimal'}, {'name': 'repaird_name', 'label': 'repaird_name', 'type': 'char'}, {'name': 'repaird_weight', 'label': 'repaird_weight', 'type': 'decimal'}, {'name': 'repaird_qty', 'label': 'repaird_qty', 'type': 'long'}, {'name': 'repaird_stonewgt', 'label': 'repaird_stonewgt', 'type': 'decimal'}, {'name': 'repaird_stoneprice', 'label': 'repaird_stoneprice', 'type': 'decimal'}, {'name': 'repaird_mcharge', 'label': 'repaird_mcharge', 'type': 'decimal'}, {'name': 'repaird_addwgt', 'label': 'repaird_addwgt', 'type': 'decimal'}, {'name': 'repaird_amount', 'label': 'repaird_amount', 'type': 'decimal'}, {'name': 'repaird_complaint', 'label': 'repaird_complaint', 'type': 'char'}, {'name': 'repaird_givrec', 'label': 'repaird_givrec', 'type': 'char'}, {'name': 'repaird_rate', 'label': 'repaird_rate', 'type': 'decimal'}, {'name': 'repaird_netwgt', 'label': 'repaird_netwgt', 'type': 'decimal'}, {'name': 'repairm_givrec', 'label': 'repairm_givrec', 'type': 'char'}]},
    opens=['w_clientshelp', 'w_repairprint_view', 'w_stktypeqtype', 'w_itemhelp', 'w_repcomplhelp'],
)


class NewForm(GeneratedForm):
    """New"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('statictext', 'st_billno', 494, 32, 421, 96)
        self.add('editmask', 'em_date', 1573, 32, 443, 96, taborder=10)
        self.add('datawindow', 'dw_smcode', 2377, 36, 677, 88, dataobject='d_smancode', taborder=20)
        self.add('statictext', 'st_7', 2117, 44, 247, 76, text='SMan :')
        self.add('statictext', 'st_date', 1367, 48, 192, 64, text='Date :')
        self.add('statictext', 'st_bill', 151, 52, 329, 64, text='Doc. No. :')
        self.add('singlelineedit', 'sle_addr', 2377, 152, 1143, 92, limit=50, taborder=50)
        self.add('singlelineedit', 'sle_custname', 1001, 156, 1015, 92, limit=30, taborder=40)
        self.add('datawindow', 'dw_1', 489, 160, 398, 88, dataobject='d_cust', taborder=30)
        self.add('statictext', 'st_5', 2085, 160, 279, 76, text='Address :')
        self.add('commandbutton', 'cb_custhelp', 923, 164, 64, 84, text='^')
        self.add('statictext', 'st_custcode', 119, 180, 361, 72, text='Customer :')
        self.add('datawindow', 'dw_sale', 14, 276, 3598, 948, dataobject='d_repr', taborder=60)
        self.add('statictext', 'st_6', 485, 276, 5, 844)
        self.add('statictext', 'st_1', 1294, 276, 5, 940)
        self.add('statictext', 'st_2', 1504, 276, 5, 940)
        self.add('statictext', 'st_3', 1801, 276, 5, 940)
        self.add('statictext', 'st_4', 2094, 276, 5, 940)
        self.add('statictext', 'st_20', 2368, 276, 5, 940)
        self.add('statictext', 'st_21', 2688, 276, 5, 940)
        self.add('commandbutton', 'cb_add', 27, 1128, 242, 84, text='&Add', taborder=100)
        self.add('commandbutton', 'cb_delete', 274, 1128, 242, 84, text='&Delete', taborder=110)
        self.add('statictext', 'st_stktype', 965, 1132, 297, 76)
        self.add('roundrectangle', 'rr_1', 2821, 1248, 590, 280)
        self.add('commandbutton', 'cb_save', 2885, 1280, 489, 100, text='&Save', taborder=80)
        self.add('editmask', 'em_duedate', 2309, 1304, 480, 96, taborder=70)
        self.add('statictext', 'st_rcvd', 1915, 1320, 384, 72, text='Due date :')
        self.add('datawindow', 'dw_print', 754, 1336, 229, 188, dataobject='d_repairprint_thermal', taborder=80)
        self.add('commandbutton', 'cb_exit', 2880, 1392, 489, 100, text='E&xit', taborder=90)
        self.add('checkbox', 'cbx_laser', 2309, 1420, 398, 80, text='Laser Print')
