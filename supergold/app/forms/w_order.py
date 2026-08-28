"""New Order — w_order.

Generated from the PowerBuilder window ``w_order.srw`` by
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
    name='w_order',
    title='New Order',
    width=4507,
    height=2264,
    controls=[],
    tables=['items', 'orderm', 'daybook', 'itemsstk', 'purchased', 'orderdga', 'salesrd', 'salesrm', 'clients', 'pdclist', 'purchasem', 'stkandprofit', 'orderd', 'orderdmodel', 'smithnewwrk', 'oglist', 'accountm', 'sman', 'wstg', 'generali', 'generals', 'userd', 'daybookpart', 'generald', 'delpart'],
    source_path='w_order.srw',
    report={'dataobject': 'd_orderprint_thermal', 'sql': 'SELECT items.name AS items_name, items.itype AS items_itype, items.printvaamt AS items_printvaamt, orderm.ordno AS orderm_ordno, orderm.tdate AS orderm_tdate, orderm.custname AS orderm_custname, orderm.duedate AS orderm_duedate, orderm.rate AS orderm_rate, orderm.billamt AS orderm_billamt, orderm.eamt AS orderm_eamt, orderm.advance AS orderm_advance, orderm.smcode AS orderm_smcode, orderm.gadvance AS orderm_gadvance, orderm.sretamt AS orderm_sretamt, orderm.addr AS orderm_addr, orderm.refund AS orderm_refund, orderm.phone AS orderm_phone, orderm.tax AS orderm_tax, orderm.note AS orderm_note, orderm.cbcode AS orderm_cbcode, orderm.bcharge AS orderm_bcharge, orderm.addbcharge AS orderm_addbcharge, orderm.ccamt AS orderm_ccamt, orderm.chqno AS orderm_chqno, orderm.chqdate AS orderm_chqdate, orderm.chqamt AS orderm_chqamt, orderm.chqbank AS orderm_chqbank, orderm.cocode AS orderm_cocode, orderd.rate AS orderd_rate, orderd.qty AS orderd_qty, orderd.weight AS orderd_weight, orderd.mcharge AS orderd_mcharge, orderd.stonewgt AS orderd_stonewgt, orderd.stoneprice AS orderd_stoneprice, orderd.amount AS orderd_amount, orderd.part AS orderd_part, (orderm.eamt + orderm.sretamt ) as ordadv, (select sum(purchased.weight ) from purchased where purchased.slno = orderm.slno) as exchwgt, (select sum(purchased.stwgt) from purchased where purchased.slno = orderm.slno) as exchstwgt, (select sum(salesrd.weight ) from salesrd where salesrd.slno = orderm.slno) as sretwgt, (select sum(salesrd.stonewgt ) from salesrd where salesrd.slno = orderm.slno) as sretstwgt FROM items, orderd, orderm WHERE items.code = orderd.code AND orderd.slno = orderm.slno ORDER BY orderd.sno ASC', 'args': ['rslno'], 'arg_types': {'rslno': 'number'}, 'tables': ['items', 'orderd', 'orderm'], 'columns': [{'name': 'items_name', 'label': 'items_name', 'type': 'char'}, {'name': 'items_itype', 'label': 'items_itype', 'type': 'char'}, {'name': 'items_printvaamt', 'label': 'items_printvaamt', 'type': 'char'}, {'name': 'ordadv', 'label': 'ordadv', 'type': 'decimal'}, {'name': 'exchwgt', 'label': 'exchwgt', 'type': 'decimal'}, {'name': 'exchstwgt', 'label': 'exchstwgt', 'type': 'decimal'}, {'name': 'sretwgt', 'label': 'sretwgt', 'type': 'decimal'}, {'name': 'sretstwgt', 'label': 'sretstwgt', 'type': 'decimal'}, {'name': 'orderm_ordno', 'label': 'orderm_ordno', 'type': 'char'}, {'name': 'orderm_tdate', 'label': 'orderm_tdate', 'type': 'date'}, {'name': 'orderm_custname', 'label': 'orderm_custname', 'type': 'char'}, {'name': 'orderm_duedate', 'label': 'orderm_duedate', 'type': 'date'}, {'name': 'orderm_rate', 'label': 'orderm_rate', 'type': 'decimal'}, {'name': 'orderm_billamt', 'label': 'orderm_billamt', 'type': 'decimal'}, {'name': 'orderm_eamt', 'label': 'orderm_eamt', 'type': 'decimal'}, {'name': 'orderm_advance', 'label': 'orderm_advance', 'type': 'decimal'}, {'name': 'orderm_smcode', 'label': 'orderm_smcode', 'type': 'char'}, {'name': 'orderm_gadvance', 'label': 'orderm_gadvance', 'type': 'decimal'}, {'name': 'orderm_sretamt', 'label': 'orderm_sretamt', 'type': 'decimal'}, {'name': 'orderm_addr', 'label': 'orderm_addr', 'type': 'char'}, {'name': 'orderm_refund', 'label': 'orderm_refund', 'type': 'decimal'}, {'name': 'orderm_phone', 'label': 'orderm_phone', 'type': 'char'}, {'name': 'orderm_tax', 'label': 'orderm_tax', 'type': 'decimal'}, {'name': 'orderm_note', 'label': 'orderm_note', 'type': 'char'}, {'name': 'orderm_cbcode', 'label': 'orderm_cbcode', 'type': 'char'}, {'name': 'orderm_bcharge', 'label': 'orderm_bcharge', 'type': 'decimal'}, {'name': 'orderm_addbcharge', 'label': 'orderm_addbcharge', 'type': 'char'}, {'name': 'orderm_ccamt', 'label': 'orderm_ccamt', 'type': 'decimal'}, {'name': 'orderm_chqno', 'label': 'orderm_chqno', 'type': 'char'}, {'name': 'orderm_chqdate', 'label': 'orderm_chqdate', 'type': 'date'}, {'name': 'orderm_chqamt', 'label': 'orderm_chqamt', 'type': 'decimal'}, {'name': 'orderm_chqbank', 'label': 'orderm_chqbank', 'type': 'char'}, {'name': 'orderm_cocode', 'label': 'orderm_cocode', 'type': 'char'}, {'name': 'orderd_rate', 'label': 'orderd_rate', 'type': 'decimal'}, {'name': 'orderd_qty', 'label': 'orderd_qty', 'type': 'long'}, {'name': 'orderd_weight', 'label': 'orderd_weight', 'type': 'decimal'}, {'name': 'orderd_mcharge', 'label': 'orderd_mcharge', 'type': 'decimal'}, {'name': 'orderd_stonewgt', 'label': 'orderd_stonewgt', 'type': 'decimal'}, {'name': 'orderd_stoneprice', 'label': 'orderd_stoneprice', 'type': 'decimal'}, {'name': 'orderd_amount', 'label': 'orderd_amount', 'type': 'decimal'}, {'name': 'orderd_part', 'label': 'orderd_part', 'type': 'char'}]},
    opens=['w_clientshelp', 'w_cbachdhelp', 'w_ordermodels', 'w_sreturn', 'w_gadvance', 'w_sucu', 'w_exchange', 'w_orderprint_view', 'w_sel_smith', 'w_itemhelp', 'w_itemtmphelp', 'w_wastage', 'w_mcharge', 'w_stktypeqtype', 'w_mcharge_perc'],
    prints=['d_orderprint_thermal'],
)


class NewOrderForm(GeneratedForm):
    """New Order"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date', 2866, 0, 402, 96)
        self.add('singlelineedit', 'st_billno', 311, 4, 411, 92, limit=10)
        self.add('commandbutton', 'cb_prev', 1134, 4, 197, 92, text='<')
        self.add('commandbutton', 'cb_next', 1330, 4, 197, 92, text='>')
        self.add('singlelineedit', 'sle_mobile', 3813, 4, 539, 84, limit=60)
        self.add('editmask', 'em_custcode', 1563, 8, 219, 96)
        self.add('checkbox', 'cbx_manual', 750, 12, 288, 76, text='Manual')
        self.add('statictext', 'st_39', 3561, 12, 233, 76, text='Mobile')
        self.add('statictext', 'st_bill', 9, 16, 302, 64, text='Order No')
        self.add('checkbox', 'cbx_updtfr', 1975, 16, 178, 68, text='Fr')
        self.add('statictext', 'st_date', 2560, 20, 320, 64, text='Date')
        self.add('editmask', 'em_rate', 311, 104, 411, 96)
        self.add('editmask', 'em_rate8gm', 2866, 104, 402, 96)
        self.add('singlelineedit', 'sle_pan', 3813, 104, 539, 84, limit=60)
        self.add('datawindow', 'dw_co', 1975, 116, 402, 88, dataobject='d_cust', taborder=20)
        self.add('commandbutton', 'cb_cohelp', 2382, 116, 142, 88, text='^')
        self.add('statictext', 'st_37', 3561, 116, 233, 76, text='PAN/Adhr')
        self.add('datawindow', 'dw_counter', 1134, 120, 658, 88, dataobject='d_countercode', taborder=10)
        self.add('statictext', 'st_2', 2560, 120, 320, 72, text='Rate/8 gm')
        self.add('statictext', 'st_1', 9, 124, 302, 72, text='Rate/gm')
        self.add('statictext', 'st_31', 814, 124, 306, 76, text='Counter :')
        self.add('statictext', 'st_21', 1838, 128, 114, 76, text='C/o')
        self.add('datawindow', 'dw_1', 311, 212, 402, 88, dataobject='d_cust', taborder=30)
        self.add('singlelineedit', 'st_custname', 795, 212, 997, 92, limit=30, taborder=40)
        self.add('editmask', 'em_ob', 1975, 212, 544, 88)
        self.add('datawindow', 'dw_smcode', 2866, 212, 677, 88, dataobject='d_smancode', taborder=60)
        self.add('singlelineedit', 'sle_tin', 3813, 212, 539, 84, limit=60)
        self.add('statictext', 'st_custcode', 9, 220, 302, 72, text='Customer')
        self.add('commandbutton', 'cb_custhelp', 722, 220, 59, 80, text='^')
        self.add('statictext', 'st_41', 3561, 220, 233, 76, text='GSTIN')
        self.add('statictext', 'st_ob', 1838, 228, 133, 76, text='OB')
        self.add('statictext', 'st_customer', 2560, 232, 320, 64, text='SM Name')
        self.add('singlelineedit', 'st_custaddr', 311, 308, 1481, 92, limit=60, taborder=50)
        self.add('singlelineedit', 'sle_phone', 1975, 308, 544, 92, limit=20, taborder=70)
        self.add('datawindow', 'dw_jewl', 2866, 308, 439, 92, dataobject='d_jewl', taborder=80)
        self.add('statictext', 'st_14', 9, 316, 302, 76, text='Address')
        self.add('statictext', 'st_16', 2560, 320, 302, 80, text='Jewellery')
        self.add('statictext', 'st_17', 1838, 328, 133, 76, text='Ph')
        self.add('datawindow', 'dw_sale', 0, 412, 4361, 856, dataobject='d_order', taborder=90)
        self.add('statictext', 'st_10', 361, 412, 5, 760)
        self.add('statictext', 'st_9', 1070, 412, 5, 856)
        self.add('statictext', 'st_3', 1234, 412, 5, 856)
        self.add('statictext', 'st_4', 1509, 412, 5, 856)
        self.add('statictext', 'st_50', 1751, 412, 5, 856)
        self.add('statictext', 'st_51', 1993, 412, 5, 856)
        self.add('statictext', 'st_5', 3054, 412, 5, 856)
        self.add('statictext', 'st_7', 3611, 412, 5, 856)
        self.add('statictext', 'st_6', 3319, 416, 5, 856)
        self.add('statictext', 'st_8', 3854, 416, 5, 856)
        self.add('statictext', 'st_qtype', 2985, 1180, 215, 76)
        self.add('commandbutton', 'cb_add', 14, 1184, 238, 80, text='&Add')
        self.add('commandbutton', 'cb_delete', 256, 1184, 238, 80, text='&Delete')
        self.add('statictext', 'st_smith', 1993, 1184, 288, 72)
        self.add('roundrectangle', 'rr_1', 3630, 1276, 521, 460)
        self.add('commandbutton', 'cb_exchange', 3653, 1288, 480, 84, text='&Exchange', taborder=250)
        self.add('editmask', 'em_gadvance', 347, 1304, 366, 84)
        self.add('editmask', 'em_billtotal', 1824, 1304, 375, 84)
        self.add('editmask', 'em_exchange', 3241, 1304, 366, 84)
        self.add('statictext', 'st_11', 0, 1308, 338, 76, text='Gold Adv')
        self.add('statictext', 'st_exchange', 2939, 1316, 297, 76, text='Exchange')
        self.add('statictext', 'st_billtotal', 1527, 1320, 270, 76, text='Bill Total')
        self.add('commandbutton', 'cb_sreturn', 3653, 1376, 480, 84, text='Sales &Return', taborder=240)
        self.add('editmask', 'em_retamt', 347, 1400, 366, 84)
        self.add('editmask', 'em_tax', 1824, 1400, 375, 84, taborder=220)
        self.add('checkbox', 'cbx_showtax', 2213, 1400, 343, 80, text='Show Tax')
        self.add('editmask', 'em_nettot', 3241, 1400, 366, 84)
        self.add('statictext', 'st_12', 0, 1408, 338, 76, text='Return Amt')
        self.add('statictext', 'st_nettot', 2939, 1408, 293, 76, text='Net Total')
        self.add('statictext', 'st_18', 1527, 1412, 270, 76, text='Tax')
        self.add('commandbutton', 'cb_gorder', 3653, 1460, 480, 84, text='&Gold Advance', taborder=230)
        self.add('editmask', 'em_advance', 347, 1496, 366, 84, taborder=100)
        self.add('editmask', 'em_refund', 1824, 1496, 375, 84, taborder=110)
        self.add('checkbox', 'cbx_taxable', 2213, 1496, 343, 80, text='Taxable')
        self.add('editmask', 'em_balance', 3241, 1496, 366, 84)
        self.add('statictext', 'st_discount', 0, 1504, 375, 76, text='T.Advance')
        self.add('statictext', 'st_balance', 2939, 1504, 293, 76, text='Balance')
        self.add('statictext', 'st_15', 1527, 1508, 270, 76, text='Refund')
        self.add('commandbutton', 'cb_save', 3653, 1552, 480, 84, text='&Save', taborder=260)
        self.add('editmask', 'em_cb', 3241, 1588, 366, 84)
        self.add('datawindow', 'dw_cashbank', 347, 1592, 882, 88, dataobject='d_cashbankcode', taborder=120)
        self.add('editmask', 'em_ccamt', 1824, 1592, 375, 84, taborder=130)
        self.add('editmask', 'em_bcharge', 2341, 1592, 265, 84, taborder=140)
        self.add('statictext', 'st_13', 2939, 1600, 293, 76, text='CB')
        self.add('statictext', 'st_25', 0, 1604, 338, 76, text='Cash/Bank')
        self.add('statictext', 'st_26', 2213, 1604, 114, 76, text='BC :')
        self.add('statictext', 'st_27', 1527, 1612, 270, 76, text='CCardAmt')
        self.add('commandbutton', 'cb_exit', 3653, 1636, 480, 84, text='E&xit', taborder=280)
        self.add('editmask', 'em_netbal', 3241, 1680, 366, 84, taborder=270)
        self.add('datawindow', 'dw_chqbank', 347, 1684, 882, 88, dataobject='d_cashbankcode', taborder=150)
        self.add('editmask', 'em_chqamt', 1824, 1684, 375, 84, taborder=160)
        self.add('editmask', 'em_chqdate', 2226, 1684, 389, 84, taborder=170)
        self.add('statictext', 'st_20', 0, 1692, 315, 76, text='Chq Bank')
        self.add('statictext', 'st_22', 2939, 1692, 366, 76, text='Net Bal')
        self.add('statictext', 'st_34', 1527, 1700, 306, 76, text='Chq.Amt/ Dt')
        self.add('commandbutton', 'cb_samples', 3241, 1768, 366, 88, text='Sam&ples')
        self.add('singlelineedit', 'sle_chqno', 1824, 1772, 786, 88, limit=20, taborder=180)
        self.add('editmask', 'em_duedate', 347, 1776, 393, 88, taborder=190)
        self.add('statictext', 'st_duedate_org', 859, 1780, 357, 76)
        self.add('statictext', 'st_rcvd', 0, 1784, 311, 76, text='Del. date')
        self.add('checkbox', 'cbx_pdc', 2939, 1784, 261, 72, text='PDC')
        self.add('statictext', 'st_36', 1527, 1788, 297, 76, text='Chq. No')
        self.add('datawindow', 'dw_print', 3799, 1788, 434, 248, dataobject='d_orderprint_thermal', taborder=200)
        self.add('checkbox', 'cbx_addbc', 2939, 1864, 261, 72, text='Add BC')
        self.add('singlelineedit', 'sle_note', 1824, 1868, 786, 88, limit=40, taborder=210)
        self.add('checkbox', 'cbx_laser', 3241, 1868, 274, 80, text='Laser')
        self.add('checkbox', 'cbx_amttowgt', 343, 1880, 667, 72, text='Advance Amt To Wgt')
        self.add('statictext', 'st_19', 1527, 1892, 270, 76, text='Note')
        self.add('checkbox', 'cbx_sendsms', 3241, 1952, 411, 72, text='Send Sms')
        self.add('checkbox', 'cbx_block', 1824, 1964, 352, 72, text='Block')
        self.add('checkbox', 'cbx_pending', 2240, 1964, 402, 72, text='Pending')
