"""Transactions — w_smithentry.

Generated from the PowerBuilder window ``w_smithentry.srw`` by
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
    name='w_smithentry',
    title='Transactions',
    width=3643,
    height=2248,
    controls=[],
    tables=[],
    source_path='w_smithentry.srw',
    grid={'control': 'dw_accode', 'dataobject': 'd_smith', 'table': 'codehelp', 'keys': ['code'], 'columns': [{'name': 'code', 'label': 'code', 'type': 'char'}]},
    report={'dataobject': 'd_smithentry', 'sql': 'SELECT items.name AS items_name, smithd.weight AS smithd_weight, smithd.qty AS smithd_qty, smithd.stonewgt AS smithd_stonewgt, smithd.wastage AS smithd_wastage, smithd.givrec AS smithd_givrec, smithd.mcharge AS smithd_mcharge, smithm.slno AS smithm_slno, smithm.docno AS smithm_docno, smithm.tdate AS smithm_tdate, clients.name AS clients_name, smithm.pamt AS smithm_pamt, smithm.ttime AS smithm_ttime, smithd.touch AS smithd_touch, smithd.touchwgt AS smithd_touchwgt, smithd.wgtamt AS smithd_wgtamt, items.itype AS items_itype, items.ornament AS items_ornament, smithd.name AS smithd_name, smithm.smithcode AS smithm_smithcode, clients.grp AS clients_grp, clients.ctype AS clients_ctype, smithd.stktype AS smithd_stktype, smithd.code AS smithd_code, smithd.touchnote AS smithd_touchnote, smithm.rmno AS smithm_rmno, smithd.netwgt AS smithd_netwgt, smithm.opwgt AS smithm_opwgt, smithm.opamt AS smithm_opamt, smithm.tmcharge AS smithm_tmcharge, smithd.stktouch AS smithd_stktouch, smithm.acidcharge AS smithm_acidcharge, smithm.discount AS smithm_discount, smithd.hmc AS smithd_hmc, smithd.stoneprice AS smithd_stoneprice, items.dmdplt AS items_dmdplt FROM items, smithd, smithm, clients WHERE items.code = smithd.code AND smithd.slno = smithm.slno AND clients.code = smithm.smithcode AND smithm.tdate between :rdate1 and :rdate2 AND smithm.control <= :rlevel ORDER BY smithm.tdate ASC, smithm.slno ASC', 'args': ['rdate1', 'rdate2', 'rlevel'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date', 'rlevel': 'number'}, 'tables': ['items', 'smithd', 'smithm', 'clients'], 'columns': [{'name': 'items_name', 'label': 'items_name', 'type': 'char'}, {'name': 'smithd_weight', 'label': 'smithd_weight', 'type': 'decimal'}, {'name': 'smithd_qty', 'label': 'smithd_qty', 'type': 'long'}, {'name': 'smithd_stonewgt', 'label': 'smithd_stonewgt', 'type': 'decimal'}, {'name': 'smithd_wastage', 'label': 'smithd_wastage', 'type': 'decimal'}, {'name': 'smithd_givrec', 'label': 'smithd_givrec', 'type': 'char'}, {'name': 'smithd_mcharge', 'label': 'smithd_mcharge', 'type': 'decimal'}, {'name': 'smithm_slno', 'label': 'smithm_slno', 'type': 'decimal'}, {'name': 'smithm_docno', 'label': 'smithm_docno', 'type': 'char'}, {'name': 'smithm_tdate', 'label': 'smithm_tdate', 'type': 'date'}, {'name': 'clients_name', 'label': 'clients_name', 'type': 'char'}, {'name': 'smithm_pamt', 'label': 'smithm_pamt', 'type': 'decimal'}, {'name': 'smithm_ttime', 'label': 'smithm_ttime', 'type': 'time'}, {'name': 'smithd_touch', 'label': 'smithd_touch', 'type': 'decimal'}, {'name': 'smithd_touchwgt', 'label': 'smithd_touchwgt', 'type': 'decimal'}, {'name': 'smithd_wgtamt', 'label': 'smithd_wgtamt', 'type': 'decimal'}, {'name': 'items_itype', 'label': 'items_itype', 'type': 'char'}, {'name': 'items_ornament', 'label': 'items_ornament', 'type': 'char'}, {'name': 'smithd_name', 'label': 'smithd_name', 'type': 'char'}, {'name': 'smithm_smithcode', 'label': 'smithm_smithcode', 'type': 'char'}, {'name': 'clients_grp', 'label': 'clients_grp', 'type': 'char'}, {'name': 'clients_ctype', 'label': 'clients_ctype', 'type': 'char'}, {'name': 'smithd_stktype', 'label': 'smithd_stktype', 'type': 'char'}, {'name': 'smithd_code', 'label': 'smithd_code', 'type': 'char'}, {'name': 'smithd_touchnote', 'label': 'smithd_touchnote', 'type': 'char'}, {'name': 'smithm_rmno', 'label': 'smithm_rmno', 'type': 'char'}, {'name': 'smithd_netwgt', 'label': 'smithd_netwgt', 'type': 'decimal'}, {'name': 'smithm_opwgt', 'label': 'smithm_opwgt', 'type': 'decimal'}, {'name': 'smithm_opamt', 'label': 'smithm_opamt', 'type': 'decimal'}, {'name': 'smithm_tmcharge', 'label': 'smithm_tmcharge', 'type': 'decimal'}, {'name': 'smithd_stktouch', 'label': 'smithd_stktouch', 'type': 'decimal'}, {'name': 'smithm_acidcharge', 'label': 'smithm_acidcharge', 'type': 'decimal'}, {'name': 'smithm_discount', 'label': 'smithm_discount', 'type': 'decimal'}, {'name': 'smithd_hmc', 'label': 'smithd_hmc', 'type': 'decimal'}, {'name': 'smithd_stoneprice', 'label': 'smithd_stoneprice', 'type': 'decimal'}, {'name': 'items_dmdplt', 'label': 'items_dmdplt', 'type': 'char'}]},
)


class TransactionsForm(GeneratedForm):
    """Transactions"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 384, 0, 448, 100, taborder=10)
        self.add('editmask', 'em_date2', 1138, 0, 448, 100, taborder=20)
        self.add('commandbutton', 'cb_show', 2528, 0, 279, 100, text='&Show', taborder=70)
        self.add('commandbutton', 'cb_3', 2816, 0, 256, 100, text='Save &As', taborder=140)
        self.add('commandbutton', 'cb_1', 3077, 0, 265, 100, text='&Print', taborder=130)
        self.add('commandbutton', 'cb_2', 3342, 0, 265, 100, text='E&xit', taborder=120)
        self.add('dropdownlistbox', 'ddlb_type2', 1947, 4, 544, 796, text='All', items=['Diamond', 'Platinum', 'Gold', 'Silver', 'Others', 'Color Stone', 'Watch', 'All'], taborder=80)
        self.add('statictext', 'st_3', 1600, 12, 338, 76, text='Item Type :')
        self.add('statictext', 'st_1', 5, 16, 366, 64, text='Date From :')
        self.add('statictext', 'st_2', 846, 16, 283, 72, text='Date To :')
        self.add('dropdownlistbox', 'ddlb_type', 1943, 104, 544, 556, text='All', items=['All', 'Ornaments Only', 'Not Ornaments'], taborder=80)
        self.add('datawindow', 'dw_accode', 384, 108, 434, 88, dataobject='d_smith', taborder=30)
        self.add('datawindow', 'dw_grp', 1138, 108, 672, 88, dataobject='d_clientsgrp_code', taborder=50)
        self.add('statictext', 'st_grp', 905, 112, 224, 76, text='Group :')
        self.add('checkbox', 'cbx_grp', 1838, 112, 82, 76)
        self.add('checkbox', 'cbx_speed', 2542, 120, 512, 76, text='Speed Print')
        self.add('checkbox', 'cbx_landscape', 3077, 120, 402, 80, text='Landscape')
        self.add('statictext', 'st_type', 23, 124, 347, 72, text='Smith  :')
        self.add('dropdownlistbox', 'ddlb_irtype', 2537, 200, 489, 556, text='All', items=['All', 'Issued Only', 'Rcvd Only'], taborder=60)
        self.add('datawindow', 'dw_stktype', 1943, 204, 539, 88, dataobject='d_stktypecode', taborder=100)
        self.add('singlelineedit', 'sle_itemcode', 384, 208, 448, 96, limit=10, taborder=40)
        self.add('commandbutton', 'cb_4', 846, 208, 187, 96, text='&Help')
        self.add('checkbox', 'cbx_bclist', 1138, 212, 416, 80, text='Barcode List')
        self.add('statictext', 'st_item', 5, 216, 366, 72, text='Item Code :')
        self.add('statictext', 'st_17', 1623, 216, 311, 76, text='Stk Type :')
        self.add('checkbox', 'cbx_remakeonly', 1134, 292, 443, 80, text='Remake Only')
        self.add('checkbox', 'cbx_daybreak', 1943, 304, 361, 76, text='Day Break')
        self.add('commandbutton', 'cb_sort', 3337, 304, 265, 80, text='Sort')
        self.add('checkbox', 'cbx_netwgtmodel', 2542, 308, 512, 76, text='Net Wgt Model')
        self.add('datawindow', 'dw_1', 0, 388, 3611, 1760, dataobject='d_smithentry', taborder=110)
