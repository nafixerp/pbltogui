"""Customer — w_sucu.

Generated from the PowerBuilder window ``w_sucu.srw`` by
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
    name='w_sucu',
    title='Customer',
    width=3877,
    height=2276,
    controls=[],
    tables=['clients', 'accountm', 'clients_advanced', 'clientspict', 'phonebook', 'daybook', 'generali', 'userd', 'generals'],
    source_path='w_sucu.srw',
    report={'dataobject': 'd_pcard_print', 'sql': 'SELECT clients.code AS clients_code, clients.name AS clients_name, clients.addr1 AS clients_addr1 FROM clients WHERE clients.code = :rcode', 'args': ['rcode'], 'arg_types': {'rcode': 'string'}, 'tables': ['clients'], 'columns': [{'name': 'code', 'label': 'code', 'type': 'char'}, {'name': 'name', 'label': 'name', 'type': 'char'}, {'name': 'addr1', 'label': 'addr1', 'type': 'char'}]},
    opens=['w_camera', 'w_pcard', 'w_clientsarea', 'w_achdgrp', 'w_clientsroute', 'w_sucu_advanced', 'w_clientsgrp', 'w_clientshelp', 'w_cbachdhelp', 'w_custopbills'],
)


class CustomerForm(GeneratedForm):
    """Customer"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('picture', 'p_photo', 3003, 0, 686, 544)
        self.add('statictext', 'st_head', 1065, 28, 1486, 84)
        self.add('singlelineedit', 'sle_chk', 2318, 36, 142, 88, text='A')
        self.add('singlelineedit', 'sle_code', 475, 148, 439, 96, limit=8, taborder=10)
        self.add('editmask', 'em_idno', 1083, 148, 274, 96, taborder=20)
        self.add('singlelineedit', 'sle_name', 1902, 148, 1070, 96, limit=30, taborder=30)
        self.add('statictext', 'st_2', 1477, 156, 398, 80, text='Name')
        self.add('statictext', 'st_idno', 923, 160, 133, 72, text='ID')
        self.add('statictext', 'st_1', 69, 164, 251, 72, text='Code')
        self.add('singlelineedit', 'sle_add1', 475, 256, 882, 96, limit=30, taborder=40)
        self.add('singlelineedit', 'sle_add2', 1902, 256, 1070, 96, limit=30, taborder=50)
        self.add('statictext', 'st_3', 69, 268, 325, 72, text='Address')
        self.add('singlelineedit', 'sle_add3', 475, 360, 882, 96, limit=30, taborder=60)
        self.add('singlelineedit', 'sle_city', 1902, 360, 1070, 96, limit=20, taborder=70)
        self.add('statictext', 'st_6', 1477, 368, 398, 72, text='City / Loc')
        self.add('singlelineedit', 'sle_phone', 475, 464, 882, 96, limit=25, taborder=80)
        self.add('singlelineedit', 'sle_mobile', 1902, 464, 745, 96, limit=30, taborder=90)
        self.add('statictext', 'st_11', 1477, 468, 398, 72, text='Mobile')
        self.add('statictext', 'st_4', 69, 476, 329, 72, text='Phone')
        self.add('commandbutton', 'cb_photo', 3145, 556, 425, 80, text='Select Photo')
        self.add('singlelineedit', 'sle_email', 475, 564, 882, 96, limit=40, taborder=100)
        self.add('singlelineedit', 'sle_pin', 1902, 564, 745, 96, limit=10, taborder=110)
        self.add('statictext', 'st_17', 69, 568, 329, 72, text='Email')
        self.add('statictext', 'st_20', 1477, 568, 398, 72, text='PIN Code')
        self.add('commandbutton', 'cb_advanced', 3040, 644, 645, 112, text='Advanced &Properties')
        self.add('singlelineedit', 'sle_panadhar', 1902, 664, 745, 96, limit=20, taborder=130)
        self.add('singlelineedit', 'sle_tin', 475, 668, 882, 96, limit=40, taborder=120)
        self.add('statictext', 'st_tin', 69, 676, 329, 72, text='GSTIN')
        self.add('statictext', 'st_pan', 1477, 680, 402, 72, text='PAN/Aadhar')
        self.add('dropdownlistbox', 'ddlb_religion', 475, 768, 882, 400, items=['Hindu', 'Muslim', 'Christian', 'Others'], taborder=140)
        self.add('datawindow', 'dw_smcode', 1902, 768, 677, 88, dataobject='d_smancode', taborder=150)
        self.add('editmask', 'em_distance', 3337, 768, 334, 92, taborder=220)
        self.add('statictext', 'st_13', 69, 776, 329, 72, text='Religion')
        self.add('statictext', 'st_18', 1477, 776, 398, 72, text='SMan')
        self.add('statictext', 'st_23', 2990, 788, 334, 64, text='Distance :')
        self.add('datawindow', 'dw_state', 1902, 860, 567, 88, dataobject='d_state_sel', taborder=170)
        self.add('datawindow', 'dw_acgrp', 475, 864, 882, 96, dataobject='d_grcode', taborder=160)
        self.add('editmask', 'em_colncomn', 3337, 864, 334, 92, taborder=210)
        self.add('commandbutton', 'cb_acgrpnew', 1349, 868, 128, 84, text='New')
        self.add('statictext', 'st_21', 1477, 868, 398, 72, text='State')
        self.add('statictext', 'st_9', 69, 884, 338, 76, text='A/c Group')
        self.add('statictext', 'st_colncomn', 2990, 884, 334, 64, text='Coln Com% :')
        self.add('radiobutton', 'rb_debit', 2359, 948, 379, 48, text='To &receive')
        self.add('editmask', 'em_balance', 1902, 952, 439, 96, taborder=190)
        self.add('editmask', 'em_cutrate', 3337, 956, 334, 96)
        self.add('datawindow', 'dw_bshead', 475, 964, 882, 88, dataobject='d_bsheadcode', taborder=200)
        self.add('statictext', 'st_5', 1477, 964, 398, 72, text='Op. Balance')
        self.add('statictext', 'st_cutrate', 3013, 964, 311, 80, text='Cut Rate :')
        self.add('statictext', 'st_19', 69, 980, 338, 76, text='BS Head')
        self.add('radiobutton', 'rb_credit', 2359, 1000, 338, 48, text='To &give')
        self.add('editmask', 'em_salary', 1902, 1048, 439, 96)
        self.add('datawindow', 'dw_grp', 475, 1052, 677, 88, dataobject='d_clientsgrp_code', taborder=220)
        self.add('singlelineedit', 'sle_pospwd', 3337, 1052, 334, 96, limit=10, taborder=180)
        self.add('commandbutton', 'cb_newgrp', 1157, 1056, 137, 80, text='New')
        self.add('statictext', 'st_pospwd', 2999, 1056, 325, 80, text='POS Pwd :')
        self.add('statictext', 'st_salary', 1477, 1060, 398, 76, text='Salary')
        self.add('statictext', 'st_grp', 69, 1064, 311, 76, text='Group')
        self.add('checkbox', 'cbx_coparty', 3003, 1144, 402, 80, text='C/o Party')
        self.add('datawindow', 'dw_route', 475, 1148, 791, 88, dataobject='d_clientsroute_code', taborder=230)
        self.add('datawindow', 'dw_area', 1902, 1148, 745, 88, dataobject='d_clientsarea_code', taborder=240)
        self.add('commandbutton', 'cb_areanew', 2647, 1152, 142, 84, text='New')
        self.add('commandbutton', 'cb_newroute', 1266, 1156, 128, 80, text='New')
        self.add('statictext', 'st_15', 1477, 1156, 398, 76, text='Area')
        self.add('statictext', 'st_10', 69, 1160, 311, 76, text='Route')
        self.add('checkbox', 'cbx_agent', 3003, 1216, 402, 80, text='Agent')
        self.add('datawindow', 'dw_co', 475, 1244, 402, 88, dataobject='d_cust', taborder=250)
        self.add('editmask', 'em_balanceb', 1902, 1244, 439, 96, taborder=260)
        self.add('radiobutton', 'rb_debitb', 2359, 1248, 407, 48, text='To receive')
        self.add('statictext', 'st_co', 69, 1260, 311, 76, text='C/o Code')
        self.add('statictext', 'st_opbalb', 1477, 1260, 398, 76, text='Op. BalanceB')
        self.add('radiobutton', 'rb_creditb', 2359, 1300, 297, 48, text='To give')
        self.add('checkbox', 'cbx_linktophbook', 3003, 1304, 603, 52, text='Link to Phone Book')
        self.add('editmask', 'em_date', 475, 1344, 439, 96, taborder=270)
        self.add('editmask', 'em_duedate', 1902, 1348, 439, 96, taborder=280)
        self.add('statictext', 'st_7', 69, 1352, 215, 76, text='Date')
        self.add('statictext', 'st_8', 1477, 1356, 398, 76, text='Due Date')
        self.add('checkbox', 'cbx_opbillentry', 3003, 1372, 869, 52, text='Show Op.Bill Creation Screen')
        self.add('radiobutton', 'rb_wgtbaltr', 923, 1436, 325, 56, text='To Receive')
        self.add('editmask', 'em_opwgtbal', 475, 1444, 439, 96, taborder=290)
        self.add('checkbox', 'cbx_remove', 3003, 1444, 384, 52, text='Removed')
        self.add('statictext', 'st_12', 69, 1456, 402, 76, text='Op.Weight Bal')
        self.add('singlelineedit', 'sle_pcardno', 1902, 1456, 443, 96, limit=20, taborder=340)
        self.add('statictext', 'st_22', 1477, 1472, 398, 64, text='Prev. Card No')
        self.add('radiobutton', 'rb_wgtbaltg', 923, 1492, 256, 64, text='To Give')
        self.add('checkbox', 'cbx_display', 3003, 1520, 366, 52, text='Display ?')
        self.add('radiobutton', 'rb_depwgtbaltr', 923, 1552, 325, 56, text='To Receive')
        self.add('editmask', 'em_opdepwgtbal', 475, 1556, 439, 96, taborder=300)
        self.add('datawindow', 'dw_pcard', 1902, 1556, 745, 88, dataobject='d_pcard_code', taborder=310)
        self.add('commandbutton', 'cb_pcardnew', 2647, 1560, 142, 84, text='New')
        self.add('statictext', 'st_pcard', 1477, 1568, 421, 64, text='Prev. Card Type')
        self.add('statictext', 'st_16', 69, 1572, 407, 76, text='Op.Dep.Wgt Bal')
        self.add('checkbox', 'cbx_showcamera', 3003, 1584, 494, 80, text='Show Camera')
        self.add('radiobutton', 'rb_depwgtbaltg', 923, 1608, 256, 56, text='To Give')
        self.add('editmask', 'em_oppcardpoints', 1902, 1652, 439, 92, taborder=330)
        self.add('singlelineedit', 'sle_cst', 475, 1660, 882, 96, limit=40, taborder=320)
        self.add('statictext', 'st_oppcardpoints', 1477, 1664, 439, 64, text='Op.PCard Points')
        self.add('checkbox', 'cbx_blocked', 3003, 1668, 494, 80, text='Blocked')
        self.add('statictext', 'st_cst', 69, 1672, 398, 72, text='CST')
        self.add('checkbox', 'cbx_approval', 3003, 1748, 622, 80, text='Approval Authority')
        self.add('multilineedit', 'mle_note', 475, 1764, 1874, 180, limit=100, taborder=350)
        self.add('statictext', 'st_14', 69, 1780, 347, 76, text='Note')
        self.add('checkbox', 'cbx_printpcard', 3003, 1840, 558, 80, text='Print Prev.Card')
        self.add('checkbox', 'cbx_updtfr', 3003, 1928, 206, 80, text='&Fr')
        self.add('roundrectangle', 'rr_1', 928, 1984, 1897, 156)
        self.add('datawindow', 'dw_pcardprint', 3529, 1996, 192, 116, dataobject='d_pcard_print')
        self.add('commandbutton', 'cb_add', 1006, 2008, 247, 108, text='&Add', taborder=370)
        self.add('commandbutton', 'cb_edit', 1280, 2008, 247, 108, text='&Edit', taborder=380)
        self.add('commandbutton', 'cb_delete', 1554, 2008, 247, 108, text='&Delete', taborder=390)
        self.add('commandbutton', 'cb_save', 1947, 2008, 247, 108, text='&Save', taborder=360)
        self.add('commandbutton', 'cb_cancel', 2226, 2008, 247, 108, text='&Cancel', taborder=400)
        self.add('commandbutton', 'cb_exit', 2501, 2008, 247, 108, text='E&xit', taborder=410)
