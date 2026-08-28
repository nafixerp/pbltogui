"""Smith Ledger — w_smithledger.

Generated from the PowerBuilder window ``w_smithledger.srw`` by
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
    name='w_smithledger',
    title='Smith Ledger',
    width=3854,
    height=2320,
    controls=[],
    tables=['daybook', 'smithd', 'clients', 'smithsusp', 'smithm', 'accountm'],
    source_path='w_smithledger.srw',
    grid={'control': 'dw_accode', 'dataobject': 'd_smith', 'table': 'codehelp', 'keys': ['code'], 'columns': [{'name': 'code', 'label': 'code', 'type': 'char'}]},
    report={'dataobject': 'd_smithledger', 'sql': 'SELECT items.name AS items_name, smithd.weight AS smithd_weight, smithd.qty AS smithd_qty, smithd.stonewgt AS smithd_stonewgt, smithd.wastage AS smithd_wastage, smithd.givrec AS smithd_givrec, smithd.mcharge AS smithd_mcharge, smithm.slno AS smithm_slno, smithm.docno AS smithm_docno, smithm.tdate AS smithm_tdate, clients.name AS clients_name, smithm.pamt AS smithm_pamt, smithd.stoneprice AS smithd_stoneprice, smithm.ttime AS smithm_ttime, smithd.touch AS smithd_touch, smithd.touchwgt AS smithd_touchwgt, smithd.name AS smithd_name, clients.ctype AS clients_ctype, smithd.touchnote AS smithd_touchnote, smithd.netwgt AS smithd_netwgt, smithd.code AS smithd_code, smithm.tdsamt AS smithm_tdsamt, smithd.hmc AS smithd_hmc, items.ornament AS items_ornament, items.itype AS items_itype, smithm.acidcharge AS smithm_acidcharge, smithm.discount AS smithm_discount, smithm.lotno AS smithm_lotno, smithm.rate AS smithm_rate FROM clients, items, smithd, smithm WHERE items.code = smithd.code AND smithd.slno = smithm.slno AND clients.code = smithm.smithcode AND smithm.smithcode = :rcode AND smithm.tdate between :rdate1 and :rdate2 AND smithm.control <= :rlevel ORDER BY smithm.tdate ASC, smithm.slno ASC', 'args': ['rdate1', 'rdate2', 'rlevel', 'rcode', 'rname', 'ropbalamt', 'ropbalwgt', 'rpaidamt', 'rBalamt'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date', 'rlevel': 'number', 'rcode': 'string', 'rname': 'string', 'ropbalamt': 'decimal', 'ropbalwgt': 'decimal', 'rpaidamt': 'decimal', 'rBalamt': 'decimal'}, 'tables': ['clients', 'items', 'smithd', 'smithm'], 'columns': [{'name': 'items_name', 'label': 'items_name', 'type': 'char'}, {'name': 'smithd_weight', 'label': 'smithd_weight', 'type': 'decimal'}, {'name': 'smithd_qty', 'label': 'smithd_qty', 'type': 'long'}, {'name': 'smithd_stonewgt', 'label': 'smithd_stonewgt', 'type': 'decimal'}, {'name': 'smithd_wastage', 'label': 'smithd_wastage', 'type': 'decimal'}, {'name': 'smithd_givrec', 'label': 'smithd_givrec', 'type': 'char'}, {'name': 'smithd_mcharge', 'label': 'smithd_mcharge', 'type': 'decimal'}, {'name': 'smithm_slno', 'label': 'smithm_slno', 'type': 'decimal'}, {'name': 'smithm_docno', 'label': 'smithm_docno', 'type': 'char'}, {'name': 'smithm_tdate', 'label': 'smithm_tdate', 'type': 'date'}, {'name': 'clients_name', 'label': 'clients_name', 'type': 'char'}, {'name': 'smithm_pamt', 'label': 'smithm_pamt', 'type': 'decimal'}, {'name': 'smithd_stoneprice', 'label': 'smithd_stoneprice', 'type': 'decimal'}, {'name': 'smithm_ttime', 'label': 'smithm_ttime', 'type': 'time'}, {'name': 'smithd_touch', 'label': 'smithd_touch', 'type': 'decimal'}, {'name': 'smithd_touchwgt', 'label': 'smithd_touchwgt', 'type': 'decimal'}, {'name': 'smithd_name', 'label': 'smithd_name', 'type': 'char'}, {'name': 'clients_ctype', 'label': 'clients_ctype', 'type': 'char'}, {'name': 'smithd_touchnote', 'label': 'smithd_touchnote', 'type': 'char'}, {'name': 'smithd_netwgt', 'label': 'smithd_netwgt', 'type': 'decimal'}, {'name': 'smithd_code', 'label': 'smithd_code', 'type': 'char'}, {'name': 'smithm_tdsamt', 'label': 'smithm_tdsamt', 'type': 'decimal'}, {'name': 'smithd_hmc', 'label': 'smithd_hmc', 'type': 'decimal'}, {'name': 'items_ornament', 'label': 'items_ornament', 'type': 'char'}, {'name': 'items_itype', 'label': 'items_itype', 'type': 'char'}, {'name': 'smithm_acidcharge', 'label': 'smithm_acidcharge', 'type': 'decimal'}, {'name': 'smithm_discount', 'label': 'smithm_discount', 'type': 'decimal'}, {'name': 'smithm_lotno', 'label': 'smithm_lotno', 'type': 'char'}, {'name': 'smithm_rate', 'label': 'smithm_rate', 'type': 'decimal'}]},
)


class SmithLedgerForm(GeneratedForm):
    """Smith Ledger"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('commandbutton', 'cb_show', 2821, 0, 238, 96, text='&Show', taborder=60)
        self.add('commandbutton', 'cb_3', 3067, 0, 238, 96, text='Save &As', taborder=110)
        self.add('commandbutton', 'cb_1', 3310, 0, 238, 96, text='&Print', taborder=100)
        self.add('commandbutton', 'cb_2', 3579, 0, 256, 96, text='E&xit', taborder=90)
        self.add('editmask', 'em_date1', 1051, 4, 462, 100, taborder=20)
        self.add('editmask', 'em_date2', 1650, 4, 457, 100, taborder=30)
        self.add('datawindow', 'dw_accode', 379, 8, 439, 92, dataobject='d_smith', taborder=10)
        self.add('statictext', 'st_type', 0, 16, 375, 72, text='GoldSmith  :')
        self.add('statictext', 'st_1', 837, 16, 197, 64, text='From :')
        self.add('statictext', 'st_2', 1518, 16, 128, 72, text='To :')
        self.add('commandbutton', 'cb_setup', 3579, 100, 256, 80, text='Setup', taborder=80)
        self.add('datawindow', 'dw_item', 379, 108, 402, 88, dataobject='d_itemcode', taborder=40)
        self.add('singlelineedit', 'sle_lotno', 1051, 108, 457, 96, limit=10, taborder=50)
        self.add('checkbox', 'cbx_nomcwstg', 1659, 108, 539, 72, text='No MC,Wastage')
        self.add('checkbox', 'cbx_nosummary', 2309, 108, 434, 72, text='No Summary')
        self.add('checkbox', 'cbx_speed', 2821, 108, 407, 72, text='Speed Print')
        self.add('checkbox', 'cbx_preview', 3269, 108, 274, 72, text='Preview')
        self.add('statictext', 'st_4', 795, 112, 238, 64, text='Lot No :')
        self.add('statictext', 'st_3', 174, 116, 201, 64, text='Item :')
        self.add('commandbutton', 'cb_defzoom', 3310, 180, 238, 76, text='Def zoom', taborder=60)
        self.add('commandbutton', 'cb_sort', 3579, 180, 256, 80, text='Sort')
        self.add('checkbox', 'cbx_netwgtmodel', 1659, 184, 480, 72, text='Net Wgt Model')
        self.add('checkbox', 'cbx_norcvdqty', 2313, 184, 430, 72, text='No Rcvd Qty')
        self.add('checkbox', 'cbx_printline', 2821, 184, 352, 72, text='Print Line')
        self.add('datawindow', 'dw_1', 0, 256, 3840, 1968, dataobject='d_smithledger', taborder=70)
