"""Enter Customers — w_sucu_kuri.

Generated from the PowerBuilder window ``w_sucu_kuri.srw`` by
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
    name='w_sucu_kuri',
    title='Enter Customers',
    width=3273,
    height=2388,
    controls=[],
    tables=['accountm', 'clients', 'clients_kuridet', 'clientspict', 'kuritype', 'daybook', 'clients_advanced', 'userd'],
    source_path='w_sucu_kuri.srw',
    opens=['w_clientshelp', 'w_camera', 'w_clientsgrp', 'w_clientsroute', 'w_cbachdhelp', 'w_kuritype_master'],
)


class EnterCustomersForm(GeneratedForm):
    """Enter Customers"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('statictext', 'st_head', 699, 0, 1435, 68)
        self.add('singlelineedit', 'sle_chk', 2286, 0, 142, 80, text='A')
        self.add('datawindow', 'dw_kuritype', 530, 84, 677, 88, dataobject='d_kuritype_code', taborder=10)
        self.add('commandbutton', 'cb_newgrp', 1221, 88, 142, 84, text='New')
        self.add('statictext', 'st_grp', 55, 92, 466, 76, text='Kuri Type :')
        self.add('checkbox', 'cbx_autocode', 1902, 96, 402, 80, text='Auto Code')
        self.add('checkbox', 'cbx_fr', 2679, 100, 174, 72, text='Fr')
        self.add('singlelineedit', 'sle_code', 530, 176, 439, 88, limit=8, taborder=20)
        self.add('singlelineedit', 'sle_name', 1902, 176, 965, 88, limit=30, taborder=30)
        self.add('statictext', 'st_1', 270, 184, 251, 72, text='Code :')
        self.add('statictext', 'st_2', 1627, 184, 265, 80, text='Name :')
        self.add('singlelineedit', 'sle_add1', 530, 268, 965, 88, limit=30, taborder=40)
        self.add('singlelineedit', 'sle_add2', 1902, 268, 965, 88, limit=30, taborder=50)
        self.add('statictext', 'st_3', 197, 280, 325, 72, text='Address :')
        self.add('singlelineedit', 'sle_add3', 530, 360, 965, 88, limit=30, taborder=60)
        self.add('singlelineedit', 'sle_city', 1902, 360, 965, 88, limit=20, taborder=70)
        self.add('statictext', 'st_6', 1719, 368, 174, 72, text='City :')
        self.add('singlelineedit', 'sle_phone', 530, 452, 613, 88, limit=25, taborder=80)
        self.add('singlelineedit', 'sle_mobile', 1902, 452, 613, 88, limit=25, taborder=90)
        self.add('statictext', 'st_4', 192, 456, 329, 72, text='Phone :')
        self.add('statictext', 'st_22', 1646, 460, 247, 72, text='Mobile :')
        self.add('statictext', 'st_23', 23, 544, 498, 72, text='Nominee Name :')
        self.add('singlelineedit', 'sle_nomname', 530, 544, 965, 88, limit=30, taborder=100)
        self.add('multilineedit', 'mle_nomaddress', 1902, 544, 965, 184, taborder=110)
        self.add('statictext', 'st_25', 1614, 548, 279, 72, text='Address :')
        self.add('dropdownlistbox', 'ddlb_nomrelation', 530, 636, 617, 728, items=['Father', 'Mother', 'Son', 'Daughter', 'Brother', 'Sister', 'Husband', 'Wife', 'Others'], taborder=120)
        self.add('statictext', 'st_24', 23, 648, 498, 72, text='Relationship :')
        self.add('datawindow', 'dw_acgrp', 530, 732, 1129, 96, dataobject='d_grcode', taborder=130)
        self.add('editmask', 'em_date', 1902, 732, 439, 88, taborder=140)
        self.add('statictext', 'st_9', 183, 740, 338, 76, text='A/c Group :')
        self.add('statictext', 'st_7', 1664, 740, 229, 76, text='Crtd dt :')
        self.add('checkbox', 'cbx_remove', 2501, 740, 370, 52, text='Removed')
        self.add('checkbox', 'cbx_display', 2501, 820, 366, 52, text='Display ?')
        self.add('datawindow', 'dw_co', 1902, 828, 402, 88, dataobject='d_cust', taborder=270)
        self.add('statictext', 'st_16', 183, 832, 338, 76, text='BS Head :')
        self.add('datawindow', 'dw_bshead', 530, 832, 1129, 88, dataobject='d_bsheadcode', taborder=150)
        self.add('statictext', 'st_co', 1728, 840, 165, 76, text='C/o :')
        self.add('editmask', 'em_balance', 530, 924, 439, 88, taborder=160)
        self.add('dropdownlistbox', 'ddlb_amtbaltype', 974, 924, 343, 400, text='To Give', items=['To Receive', 'To Give'], taborder=170)
        self.add('editmask', 'em_balanceb', 1902, 924, 439, 88, taborder=180)
        self.add('dropdownlistbox', 'ddlb_amtbalbtype', 2345, 924, 343, 400, text='To Give', items=['To Receive', 'To Give'], taborder=190)
        self.add('statictext', 'st_5', 14, 932, 507, 72, text='A/c Op. Amt Bal :')
        self.add('statictext', 'st_opbalb', 1326, 940, 567, 76, text='A/c Op. Amt Bal B :')
        self.add('editmask', 'em_wgtbal', 530, 1016, 439, 88, taborder=200)
        self.add('dropdownlistbox', 'ddlb_wgtbaltype', 974, 1016, 343, 400, text='To Give', items=['To Receive', 'To Give'], taborder=210)
        self.add('editmask', 'em_wgtbalb', 1902, 1016, 439, 88, taborder=220)
        self.add('dropdownlistbox', 'ddlb_wgtbalbtype', 2345, 1016, 343, 400, text='To Give', items=['To Receive', 'To Give'], taborder=230)
        self.add('statictext', 'st_26', 78, 1024, 443, 72, text='Op. Wgt Bal :')
        self.add('statictext', 'st_wgtbalb', 1435, 1032, 457, 76, text='Op. Wgt Bal B :')
        self.add('editmask', 'em_collnopbal', 530, 1108, 439, 88, taborder=240)
        self.add('dropdownlistbox', 'ddlb_collnopbal', 974, 1108, 343, 400, text='To Give', items=['To Receive', 'To Give'], taborder=250)
        self.add('datawindow', 'dw_custlinkac', 1902, 1112, 402, 88, dataobject='d_cust', taborder=260)
        self.add('statictext', 'st_collnopbal', 0, 1116, 521, 76, text='Colln OpBal Amt :')
        self.add('statictext', 'st_27', 1317, 1120, 576, 76, text='Customer Link Ac  :')
        self.add('datawindow', 'dw_route', 530, 1200, 791, 88, dataobject='d_clientsroute_code', taborder=280)
        self.add('commandbutton', 'cb_newroute', 1326, 1204, 142, 84, text='New')
        self.add('datawindow', 'dw_grp', 1902, 1204, 677, 88, dataobject='d_clientsgrp_code', taborder=290)
        self.add('statictext', 'st_17', 192, 1208, 329, 76, text='Route :')
        self.add('commandbutton', 'cb_1', 2583, 1208, 133, 80, text='New')
        self.add('statictext', 'st_19', 1664, 1216, 229, 76, text='Group :')
        self.add('datawindow', 'dw_collnagent', 530, 1292, 402, 88, dataobject='d_staffcode', taborder=300)
        self.add('dropdownlistbox', 'ddlb_colntype', 1906, 1292, 439, 368, text='Weekly', items=['Daily', 'Weekly', 'Monthly'], taborder=310)
        self.add('statictext', 'st_18', 133, 1300, 389, 76, text='Colln Agent :')
        self.add('statictext', 'st_15', 1550, 1300, 343, 76, text='Coln Type :')
        self.add('picture', 'p_photo', 2400, 1308, 686, 544)
        self.add('editmask', 'em_startdate', 530, 1384, 439, 88, taborder=320)
        self.add('editmask', 'em_maturitydate', 1906, 1384, 439, 88, taborder=330)
        self.add('statictext', 'st_startdate', 0, 1396, 521, 76, text='Kuri Start Date :')
        self.add('statictext', 'st_13', 1385, 1396, 507, 76, text='Date of Maturity :')
        self.add('editmask', 'em_instnos', 530, 1476, 439, 88, taborder=340)
        self.add('editmask', 'em_instamt', 1906, 1476, 439, 88, taborder=350)
        self.add('statictext', 'st_10', 1458, 1484, 434, 76, text='Inst. Amt :')
        self.add('statictext', 'st_8', 87, 1488, 434, 76, text='No. of Inst :')
        self.add('editmask', 'em_totamt', 530, 1568, 439, 88, taborder=360)
        self.add('checkbox', 'cbx_showwgtdet', 1897, 1572, 485, 80, text='Show Wgt Details')
        self.add('statictext', 'st_11', 87, 1580, 434, 76, text='Total Amt :')
        self.add('editmask', 'em_bonus', 530, 1660, 439, 88, taborder=370)
        self.add('editmask', 'em_intrate', 1902, 1660, 439, 88, taborder=380)
        self.add('statictext', 'st_14', 1362, 1668, 530, 80, text='Yearly Interest % :')
        self.add('statictext', 'st_12', 87, 1672, 434, 76, text='Bonus :')
        self.add('editmask', 'em_wadate', 530, 1752, 439, 88, taborder=390)
        self.add('editmask', 'em_bdate', 1902, 1752, 439, 88, taborder=400)
        self.add('statictext', 'st_20', 87, 1756, 434, 76, text='WA Date :')
        self.add('statictext', 'st_21', 1554, 1764, 338, 80, text='BDate :')
        self.add('editmask', 'em_collnminamt', 530, 1844, 439, 88, taborder=410)
        self.add('editmask', 'em_collnmaxamt', 1902, 1844, 439, 88, taborder=420)
        self.add('statictext', 'st_29', 9, 1856, 512, 76, text='Colln Min Amt :')
        self.add('statictext', 'st_28', 1381, 1856, 512, 76, text='Colln Max Amt :')
        self.add('commandbutton', 'cb_photo', 2542, 1864, 425, 80, text='Select Photo', taborder=520)
        self.add('singlelineedit', 'sle_bankacno', 530, 1936, 965, 88, limit=30, taborder=430)
        self.add('singlelineedit', 'sle_bankifsc', 1902, 1936, 613, 88, limit=30, taborder=440)
        self.add('statictext', 'st_30', 23, 1940, 498, 72, text='Bank A/c No :')
        self.add('statictext', 'st_31', 1550, 1940, 343, 72, text='Bank IFSC :')
        self.add('checkbox', 'cbx_showcamera', 2542, 1944, 494, 80, text='Show Camera')
        self.add('singlelineedit', 'sle_bankname', 530, 2028, 965, 88, limit=30, taborder=450)
        self.add('statictext', 'st_32', 23, 2032, 498, 72, text='Bank Name :')
        self.add('roundrectangle', 'rr_1', 512, 2132, 1897, 164)
        self.add('commandbutton', 'cb_add', 590, 2160, 247, 108, text='&Add', taborder=470)
        self.add('commandbutton', 'cb_edit', 864, 2160, 247, 108, text='&Edit', taborder=480)
        self.add('commandbutton', 'cb_delete', 1138, 2160, 247, 108, text='&Delete', taborder=490)
        self.add('commandbutton', 'cb_save', 1531, 2160, 247, 108, text='&Save', taborder=460)
        self.add('commandbutton', 'cb_cancel', 1810, 2160, 247, 108, text='&Cancel', taborder=500)
        self.add('commandbutton', 'cb_exit', 2085, 2160, 247, 108, text='E&xit', taborder=510)
