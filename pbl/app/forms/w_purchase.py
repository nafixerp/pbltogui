"""Purchase Details — w_purchase.

Generated from the PowerBuilder window ``w_purchase.srw`` by
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
    name='w_purchase',
    title='Purchase Details',
    width=4283,
    height=2248,
    controls=[],
    tables=['daybook', 'items', 'itemsstk', 'purchaserd', 'purchasem', 'purchased', 'advafter', 'pdclist', 'salestype', 'purchaserm', 'oglist', 'stkandprofit', 'clients', 'bamt', 'orderm', 'sman', 'accountm', 'itemsqtype', 'generali', 'generals', 'generald', 'userd', 'daybookpart', 'delpart'],
    source_path='w_purchase.srw',
    report={'dataobject': 'd_purchprint_thermal', 'sql': 'SELECT items.name AS items_name, items.itype AS items_itype, items.printvaamt AS items_printvaamt, purchasem.tdate AS purchasem_tdate, purchasem.docno AS purchasem_docno, purchasem.name AS purchasem_name, purchasem.billamt AS purchasem_billamt, purchasem.pamt AS purchasem_pamt, purchasem.addamt AS purchasem_addamt, purchasem.eamt AS purchasem_eamt, purchased.code AS purchased_code, purchased.qty AS purchased_qty, purchased.weight AS purchased_weight, purchased.lesswgt AS purchased_lesswgt, purchased.amount AS purchased_amount, purchased.rate AS purchased_rate, purchased.stwgt AS purchased_stwgt, purchasem.rate AS purchasem_rate, purchasem.smcode AS purchasem_smcode, purchasem.netamt AS purchasem_netamt, purchasem.taxamt AS purchasem_taxamt, purchasem.control AS purchasem_control, items.vatcode AS items_vatcode, items.stonewgt AS items_stonewgt, purchased.stprice AS purchased_stprice FROM items, purchased, purchasem WHERE items.code = purchased.code AND purchased.slno = purchasem.slno ORDER BY purchased.sno ASC', 'args': ['rslno'], 'arg_types': {'rslno': 'number'}, 'tables': ['items', 'purchased', 'purchasem'], 'columns': [{'name': 'items_name', 'label': 'items_name', 'type': 'char'}, {'name': 'items_itype', 'label': 'items_itype', 'type': 'char'}, {'name': 'items_printvaamt', 'label': 'items_printvaamt', 'type': 'char'}, {'name': 'purchasem_tdate', 'label': 'purchasem_tdate', 'type': 'date'}, {'name': 'purchasem_docno', 'label': 'purchasem_docno', 'type': 'char'}, {'name': 'purchasem_name', 'label': 'purchasem_name', 'type': 'char'}, {'name': 'purchasem_billamt', 'label': 'purchasem_billamt', 'type': 'decimal'}, {'name': 'purchasem_pamt', 'label': 'purchasem_pamt', 'type': 'decimal'}, {'name': 'purchasem_addamt', 'label': 'purchasem_addamt', 'type': 'decimal'}, {'name': 'purchasem_eamt', 'label': 'purchasem_eamt', 'type': 'decimal'}, {'name': 'purchased_code', 'label': 'purchased_code', 'type': 'char'}, {'name': 'purchased_qty', 'label': 'purchased_qty', 'type': 'long'}, {'name': 'purchased_weight', 'label': 'purchased_weight', 'type': 'decimal'}, {'name': 'purchased_lesswgt', 'label': 'purchased_lesswgt', 'type': 'decimal'}, {'name': 'purchased_amount', 'label': 'purchased_amount', 'type': 'decimal'}, {'name': 'purchased_rate', 'label': 'purchased_rate', 'type': 'decimal'}, {'name': 'purchased_stwgt', 'label': 'purchased_stwgt', 'type': 'decimal'}, {'name': 'purchasem_rate', 'label': 'purchasem_rate', 'type': 'decimal'}, {'name': 'purchasem_smcode', 'label': 'purchasem_smcode', 'type': 'char'}, {'name': 'purchasem_netamt', 'label': 'purchasem_netamt', 'type': 'decimal'}, {'name': 'purchasem_taxamt', 'label': 'purchasem_taxamt', 'type': 'decimal'}, {'name': 'purchasem_control', 'label': 'purchasem_control', 'type': 'long'}, {'name': 'items_vatcode', 'label': 'items_vatcode', 'type': 'char'}, {'name': 'items_stonewgt', 'label': 'items_stonewgt', 'type': 'decimal'}, {'name': 'purchased_stprice', 'label': 'purchased_stprice', 'type': 'decimal'}]},
    opens=['w_stktypehlp', 'w_clientshelp', 'w_osalehelp', 'w_sucu', 'w_exchange', 'w_purchase_view', 'w_purchase_vat_print', 'w_itemtmphelp', 'w_stktypeqtype', 'w_rmno', 'w_itemhelp'],
    prints=['d_purchprint_thermal'],
)


class PurchaseDetailsForm(GeneratedForm):
    """Purchase Details"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('singlelineedit', 'st_grno', 274, 0, 439, 84, limit=10, taborder=40)
        self.add('checkbox', 'cbx_manual', 727, 0, 256, 80, text='Manual')
        self.add('singlelineedit', 'sle_billno', 1234, 0, 521, 84, limit=20, taborder=10)
        self.add('editmask', 'em_date', 2025, 0, 425, 88, taborder=20)
        self.add('singlelineedit', 'sle_ordno', 2953, 0, 375, 88, limit=10, taborder=30)
        self.add('commandbutton', 'cb_1', 3337, 0, 146, 88, text='&Help')
        self.add('statictext', 'st_1', 969, 4, 261, 72, text='Bill No :')
        self.add('statictext', 'st_bill', 5, 8, 279, 64, text='Doc. No.')
        self.add('statictext', 'st_11', 2592, 8, 370, 80, text='To Order No')
        self.add('statictext', 'st_date', 1774, 12, 187, 64, text='Date')
        self.add('datawindow', 'dw_1', 274, 88, 425, 96, dataobject='d_sucu', taborder=50)
        self.add('commandbutton', 'cb_custhelp', 718, 92, 64, 92, text='^')
        self.add('singlelineedit', 'st_suppname', 786, 92, 969, 92, limit=30, taborder=60)
        self.add('editmask', 'em_ob', 2025, 96, 425, 88)
        self.add('datawindow', 'dw_smcode', 2953, 96, 677, 88, dataobject='d_smancode', taborder=100)
        self.add('statictext', 'st_custcode', 5, 104, 279, 72, text='Supplier')
        self.add('statictext', 'st_ob', 1774, 108, 187, 76, text='OB')
        self.add('statictext', 'st_smcode', 2592, 112, 315, 64, text='Sales Man')
        self.add('singlelineedit', 'sle_addr', 274, 192, 1481, 92, limit=60, taborder=70)
        self.add('singlelineedit', 'sle_pan', 2025, 192, 544, 92, limit=60, taborder=80)
        self.add('singlelineedit', 'sle_mobile', 2953, 192, 677, 92, limit=20, taborder=90)
        self.add('statictext', 'st_20', 5, 200, 265, 72, text='Address')
        self.add('statictext', 'st_22', 1774, 204, 238, 76, text='PAN/Adh')
        self.add('statictext', 'st_23', 2592, 204, 343, 76, text='Mobile No')
        self.add('datawindow', 'dw_purchase', 0, 292, 4037, 1020, dataobject='d_exchange1', taborder=110)
        self.add('statictext', 'st_10', 357, 292, 5, 928)
        self.add('statictext', 'st_25', 1042, 292, 5, 1016)
        self.add('statictext', 'st_3', 1239, 292, 5, 1016)
        self.add('statictext', 'st_4', 1495, 292, 5, 1016)
        self.add('statictext', 'st_5', 1659, 292, 5, 1016)
        self.add('statictext', 'st_13', 1947, 292, 5, 1016)
        self.add('statictext', 'st_6', 2158, 292, 5, 1016)
        self.add('statictext', 'st_7', 2409, 292, 5, 1016)
        self.add('statictext', 'st_55', 2578, 292, 5, 1016)
        self.add('statictext', 'st_8', 2747, 292, 5, 1016)
        self.add('statictext', 'st_9', 2921, 292, 5, 1016)
        self.add('statictext', 'st_15', 3122, 292, 5, 1016)
        self.add('statictext', 'st_26', 3383, 292, 5, 1016)
        self.add('statictext', 'st_27', 3625, 292, 5, 1016)
        self.add('commandbutton', 'cb_add', 0, 1224, 206, 72, text='&Add')
        self.add('commandbutton', 'cb_delete', 201, 1224, 197, 72, text='&Delete')
        self.add('statictext', 'st_kdm', 2162, 1224, 169, 76)
        self.add('statictext', 'st_stktype', 663, 1228, 160, 76)
        self.add('roundrectangle', 'rr_1', 3058, 1308, 558, 392)
        self.add('editmask', 'em_billtotal', 293, 1336, 407, 96)
        self.add('editmask', 'em_discperc', 1550, 1336, 128, 96, taborder=130)
        self.add('editmask', 'em_discount', 1678, 1336, 279, 96, taborder=160)
        self.add('editmask', 'em_taxperc', 2450, 1336, 142, 96, taborder=170)
        self.add('editmask', 'em_tax', 2592, 1336, 425, 96, taborder=120)
        self.add('checkbox', 'cbx_cst', 786, 1340, 384, 84, text='Interstate')
        self.add('commandbutton', 'cb_exchange', 3122, 1344, 434, 96, text='&Return')
        self.add('statictext', 'st_billtotal', 0, 1348, 293, 76, text='Bill Total')
        self.add('statictext', 'st_19', 1243, 1348, 306, 64, text='Discount')
        self.add('checkbox', 'cbx_taxexternal', 1989, 1348, 288, 80, text='External')
        self.add('statictext', 'st_14', 2313, 1348, 155, 76, text='Tax')
        self.add('editmask', 'em_cess', 293, 1436, 407, 96, taborder=140)
        self.add('editmask', 'em_hmc', 800, 1436, 370, 96, taborder=150)
        self.add('editmask', 'em_exchange', 1550, 1436, 407, 96)
        self.add('editmask', 'em_nettot', 2592, 1436, 425, 96)
        self.add('statictext', 'st_exchange', 1243, 1440, 306, 68, text='P.Return')
        self.add('statictext', 'st_18', 0, 1444, 293, 64, text='Cess')
        self.add('statictext', 'st_nettot', 2313, 1444, 270, 76, text='Net Total')
        self.add('statictext', 'st_29', 704, 1452, 169, 72, text='HMC')
        self.add('commandbutton', 'cb_save', 3122, 1456, 434, 96, text='&Save')
        self.add('editmask', 'em_others', 293, 1536, 407, 96, taborder=190)
        self.add('editmask', 'em_tcsperc', 800, 1536, 146, 96, taborder=180)
        self.add('editmask', 'em_tcsamt', 946, 1536, 224, 96, taborder=200)
        self.add('editmask', 'em_pamt', 1550, 1536, 407, 96, taborder=210)
        self.add('editmask', 'em_balance', 2592, 1536, 425, 96)
        self.add('statictext', 'st_discount', 0, 1544, 293, 76, text='Others')
        self.add('statictext', 'st_rcvd', 1243, 1544, 306, 76, text='Paid Amt')
        self.add('statictext', 'st_balance', 2313, 1544, 270, 76, text='Balance')
        self.add('statictext', 'st_tcs', 704, 1552, 169, 72, text='TCS')
        self.add('commandbutton', 'cb_exit', 3122, 1568, 434, 96, text='E&xit')
        self.add('datawindow', 'dw_billtype', 2592, 1632, 425, 88, dataobject='d_billtypecode', taborder=310)
        self.add('statictext', 'st_17', 2313, 1636, 270, 76, text='BType')
        self.add('datawindow', 'dw_chqbank', 293, 1640, 882, 88, dataobject='d_cashbankcode', taborder=220)
        self.add('editmask', 'em_chqamt', 1550, 1640, 407, 84, taborder=230)
        self.add('statictext', 'st_12', 0, 1648, 293, 76, text='Chq Bank')
        self.add('statictext', 'st_34', 1243, 1652, 306, 76, text='Chq. Amt')
        self.add('editmask', 'em_chqdate', 1550, 1728, 407, 84, taborder=260)
        self.add('datawindow', 'dw_state', 2592, 1728, 567, 88, dataobject='d_state_sel', taborder=250)
        self.add('checkbox', 'cbx_laserprint', 3209, 1728, 402, 80, text='Laser Print')
        self.add('singlelineedit', 'sle_chqno', 293, 1732, 882, 88, limit=20, taborder=240)
        self.add('statictext', 'st_16', 1243, 1736, 306, 76, text='Chq. Date')
        self.add('checkbox', 'cbx_pdc', 1989, 1740, 224, 72, text='PDC')
        self.add('statictext', 'st_42', 2313, 1744, 270, 76, text='State')
        self.add('statictext', 'st_36', 0, 1748, 293, 76, text='Chq. No')
        self.add('editmask', 'em_duedate', 1550, 1816, 407, 96, taborder=290)
        self.add('singlelineedit', 'sle_note', 293, 1824, 882, 92, limit=60, taborder=270)
        self.add('editmask', 'em_cb', 2592, 1824, 425, 96)
        self.add('checkbox', 'cbx_taxdeduct', 3209, 1824, 677, 80, text='Tax deduct from BAmt')
        self.add('statictext', 'st_2', 1243, 1832, 306, 76, text='Duedate')
        self.add('datawindow', 'dw_print', 2075, 1832, 123, 76, dataobject='d_purchprint_thermal', taborder=280)
        self.add('statictext', 'st_21', 0, 1836, 293, 76, text='Note')
        self.add('statictext', 'st_cb', 2313, 1844, 270, 76, text='CB')
        self.add('datawindow', 'dw_counter', 293, 1920, 658, 88, dataobject='d_countercode', taborder=300)
        self.add('checkbox', 'cbx_taxonmconly', 3209, 1924, 567, 80, text='Tax on MC Only')
        self.add('statictext', 'st_24', 0, 1928, 293, 76, text='Counter')
        self.add('checkbox', 'cbx_updtfr', 2587, 1944, 165, 76, text='&Fr')
        self.add('checkbox', 'cbx_updtsys', 2848, 1944, 206, 76, text='Sys')
