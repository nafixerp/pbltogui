"""Goldsmith — w_smith.

Generated from the PowerBuilder window ``w_smith.srw`` by
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
    name='w_smith',
    title='Goldsmith',
    width=3689,
    height=1956,
    controls=[],
    tables=['accountm', 'clientsgs', 'clients', 'clientspict', 'daybook', 'smithm', 'refinerym', 'userd'],
    source_path='w_smith.srw',
    opens=['w_achdgrp', 'w_clientsgrp', 'w_clientshelp'],
)


class GoldsmithForm(GeneratedForm):
    """Goldsmith"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('statictext', 'st_head', 933, 20, 1330, 76)
        self.add('singlelineedit', 'sle_code', 475, 120, 421, 92, limit=8, taborder=10)
        self.add('singlelineedit', 'sle_name', 2117, 120, 882, 92, limit=30, taborder=20)
        self.add('checkbox', 'cbx_silver', 1001, 124, 402, 76, text='Silver Party')
        self.add('picture', 'p_photo', 3013, 124, 654, 588)
        self.add('statictext', 'st_2', 1664, 132, 448, 80, text='Name')
        self.add('statictext', 'st_1', 0, 136, 334, 72, text='Code')
        self.add('singlelineedit', 'sle_add1', 475, 220, 1129, 92, limit=30, taborder=30)
        self.add('singlelineedit', 'sle_add2', 2117, 220, 882, 92, limit=30, taborder=40)
        self.add('statictext', 'st_3', 0, 236, 325, 72, text='Address')
        self.add('singlelineedit', 'sle_add3', 475, 320, 1129, 92, limit=30, taborder=50)
        self.add('singlelineedit', 'sle_city', 2117, 320, 882, 92, limit=20, taborder=60)
        self.add('statictext', 'st_6', 1664, 332, 448, 72, text='City / Loc')
        self.add('radiobutton', 'rb_debit', 2578, 412, 379, 72, text='To &receive')
        self.add('singlelineedit', 'sle_phone', 475, 420, 539, 92, taborder=70)
        self.add('singlelineedit', 'sle_mobile', 1029, 420, 567, 92, taborder=80)
        self.add('editmask', 'em_balance', 2117, 420, 425, 92, taborder=150)
        self.add('statictext', 'st_4', 0, 424, 471, 72, text='Phone /Mobile')
        self.add('statictext', 'st_5', 1664, 432, 448, 72, text='Op. Amt Bal')
        self.add('radiobutton', 'rb_credit', 2578, 476, 338, 64, text='To &give')
        self.add('singlelineedit', 'sle_pin', 475, 524, 539, 92, taborder=90)
        self.add('datawindow', 'dw_state', 1029, 524, 567, 88, dataobject='d_state_sel', taborder=100)
        self.add('statictext', 'st_pinstate', 0, 528, 471, 72, text='PIN / State')
        self.add('editmask', 'em_weight', 2117, 532, 425, 92, taborder=160)
        self.add('radiobutton', 'rb_tor', 2578, 536, 402, 68, text='To receive')
        self.add('statictext', 'st_8', 1664, 540, 453, 72, text='Op. Weight Bal')
        self.add('radiobutton', 'rb_tog', 2578, 592, 274, 72, text='To give')
        self.add('singlelineedit', 'sle_tin', 475, 624, 1129, 92, limit=30, taborder=110)
        self.add('statictext', 'st_tin', 0, 628, 471, 72, text='GSTIN')
        self.add('editmask', 'em_distance', 2117, 632, 425, 92, taborder=170)
        self.add('statictext', 'st_21', 1664, 640, 453, 72, text='Distance')
        self.add('commandbutton', 'cb_photo', 3127, 716, 425, 92, text='Select Photo')
        self.add('singlelineedit', 'sle_panadhar', 475, 732, 1129, 92, limit=30, taborder=120)
        self.add('statictext', 'st_19', 0, 736, 471, 72, text='PAN/Adhaar')
        self.add('editmask', 'em_wastage', 1317, 836, 288, 92, taborder=140)
        self.add('editmask', 'em_mcrate', 475, 840, 439, 92, taborder=130)
        self.add('editmask', 'em_weightamt', 2117, 840, 425, 92, taborder=180)
        self.add('statictext', 'st_7', 955, 848, 347, 72, text='Wastage %')
        self.add('statictext', 'st_9', 0, 852, 416, 76, text='MC Rate/Gm.')
        self.add('statictext', 'st_10', 1664, 856, 448, 76, text='Weight Amt')
        self.add('datawindow', 'dw_acgrp', 475, 948, 1129, 96, dataobject='d_grcode', taborder=190)
        self.add('datawindow', 'dw_bsgrp', 2117, 948, 1129, 88, dataobject='d_bsheadcode', taborder=200)
        self.add('statictext', 'st_13', 0, 956, 338, 76, text='A/c Group')
        self.add('commandbutton', 'cb_acgrpnew', 1609, 956, 133, 84, text='New')
        self.add('statictext', 'st_20', 1751, 960, 302, 76, text='BS Head')
        self.add('radiobutton', 'rb_debitb', 2569, 1036, 379, 72, text='To &receive')
        self.add('editmask', 'em_balanceb', 2117, 1048, 425, 104, taborder=260)
        self.add('checkbox', 'cbx_24ct', 3109, 1056, 462, 76, text='A/c in 24 Ct')
        self.add('datawindow', 'dw_grp', 475, 1060, 677, 88, dataobject='d_clientsgrp_code', taborder=210)
        self.add('commandbutton', 'cb_newgrp', 1157, 1064, 142, 84, text='New')
        self.add('statictext', 'st_grp', 0, 1068, 311, 76, text='Group')
        self.add('statictext', 'st_opbalb', 1664, 1076, 448, 72, text='Op. Amt Bal B')
        self.add('radiobutton', 'rb_creditb', 2569, 1092, 320, 72, text='To &give')
        self.add('checkbox', 'cbx_remove', 3109, 1144, 384, 76, text='Removed')
        self.add('radiobutton', 'rb_opwbr', 2574, 1156, 402, 68, text='To receive')
        self.add('editmask', 'em_convtouch', 475, 1160, 288, 100, taborder=220)
        self.add('editmask', 'em_deftouch', 1317, 1160, 288, 100, taborder=230)
        self.add('editmask', 'em_weightb', 2117, 1160, 425, 100, taborder=270)
        self.add('statictext', 'st_17', 955, 1176, 320, 80, text='Def.Touch')
        self.add('statictext', 'st_11', 0, 1180, 402, 76, text='Conv. Touch')
        self.add('statictext', 'st_opwb', 1664, 1184, 512, 72, text='Op. Weight Bal B')
        self.add('radiobutton', 'rb_opwbg', 2574, 1212, 274, 72, text='To give')
        self.add('checkbox', 'cbx_blocked', 3109, 1236, 402, 80, text='Blocked')
        self.add('editmask', 'em_stocktouch', 475, 1268, 288, 100, taborder=240)
        self.add('editmask', 'em_weightamtb', 2117, 1272, 425, 96, taborder=280)
        self.add('statictext', 'st_18', 0, 1288, 407, 76, text='Stock Touch')
        self.add('statictext', 'st_wgtamt', 1664, 1288, 448, 76, text='Weight Amt B')
        self.add('statictext', 'st_12', 0, 1376, 247, 76, text='E-mail')
        self.add('singlelineedit', 'sle_email', 475, 1376, 1129, 88, limit=40, taborder=250)
        self.add('editmask', 'em_mcdecround', 2117, 1376, 425, 96, taborder=320)
        self.add('statictext', 'st_16', 1664, 1388, 457, 80, text='MC Dec.Round')
        self.add('editmask', 'em_decround', 475, 1472, 288, 96, taborder=290)
        self.add('editmask', 'em_roundup', 1317, 1472, 288, 96, taborder=300)
        self.add('statictext', 'st_14', 0, 1476, 384, 80, text='Dec. Round')
        self.add('statictext', 'st_15', 955, 1480, 302, 80, text='Round Up')
        self.add('editmask', 'em_intamt', 2117, 1480, 425, 96, taborder=330)
        self.add('editmask', 'em_intwgt', 2743, 1480, 256, 96, taborder=310)
        self.add('statictext', 'st_intamt', 1664, 1488, 457, 80, text='Interest, Amt')
        self.add('statictext', 'st_intwgt', 2555, 1488, 183, 80, text='> Wgt')
        self.add('roundrectangle', 'rr_1', 905, 1620, 1682, 148)
        self.add('singlelineedit', 'sle_chk', 736, 1640, 142, 88, text='A')
        self.add('commandbutton', 'cb_add', 969, 1640, 238, 104, text='&Add', taborder=350)
        self.add('commandbutton', 'cb_edit', 1216, 1640, 238, 104, text='&Edit', taborder=360)
        self.add('commandbutton', 'cb_delete', 1463, 1640, 238, 104, text='&Delete', taborder=370)
        self.add('commandbutton', 'cb_save', 1792, 1640, 238, 104, text='&Save', taborder=340)
        self.add('commandbutton', 'cb_cancel', 2043, 1640, 238, 104, text='&Cancel', taborder=380)
        self.add('commandbutton', 'cb_exit', 2295, 1640, 238, 104, text='E&xit', taborder=390)
