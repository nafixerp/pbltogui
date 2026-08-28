"""Groups — w_itemgrp.

Generated from the PowerBuilder window ``w_itemgrp.srw`` by
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
    name='w_itemgrp',
    title='Groups',
    width=2103,
    height=1316,
    controls=[],
    tables=['itemgrp', 'items'],
    source_path='w_itemgrp.srw',
    opens=['w_regional', 'w_itemgrphelp'],
)


class GroupsForm(GeneratedForm):
    """Groups"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('statictext', 'st_head', 507, 16, 1079, 76)
        self.add('singlelineedit', 'sle_chk', 1701, 128, 142, 88, text='A', taborder=80)
        self.add('singlelineedit', 'sle_accode', 594, 136, 421, 88, limit=10, taborder=10)
        self.add('checkbox', 'cbx_ornament', 1074, 140, 443, 76, text='Ornament ?')
        self.add('statictext', 'st_1', 133, 144, 453, 72, text='Group Code :')
        self.add('statictext', 'st_2', 133, 252, 453, 80, text='Name :')
        self.add('singlelineedit', 'sle_desc', 594, 252, 919, 88, limit=30, taborder=20)
        self.add('singlelineedit', 'sle_regional', 594, 364, 919, 88, limit=30, taborder=30)
        self.add('statictext', 'st_6', 160, 368, 425, 76, text='Malayalam :')
        self.add('commandbutton', 'cb_langhelp', 1527, 368, 238, 84, text='&Help', taborder=40)
        self.add('editmask', 'em_pos', 594, 476, 421, 96, taborder=24)
        self.add('statictext', 'st_3', 302, 484, 283, 76, text='Position :')
        self.add('checkbox', 'cbx_notinstkrep', 1074, 492, 832, 80, text="Don't show in Stock Reports")
        self.add('commandbutton', 'cb_updtallitems', 1019, 604, 978, 96, text='Update all items with this HSN of this group', taborder=30)
        self.add('singlelineedit', 'sle_hsn', 594, 608, 421, 88, limit=30, taborder=20)
        self.add('statictext', 'st_4', 242, 616, 343, 76, text='HSN Code :')
        self.add('groupbox', 'gb_type', 590, 748, 1303, 196, text='Item type', taborder=50)
        self.add('radiobutton', 'rb_platinum', 882, 828, 306, 80, text='Platinum')
        self.add('radiobutton', 'rb_gold', 631, 832, 242, 72, text='&Gold')
        self.add('radiobutton', 'rb_silver', 1198, 832, 270, 72, text='Sil&ver')
        self.add('radiobutton', 'rb_others', 1490, 832, 288, 72, text='&Others')
        self.add('roundrectangle', 'rr_1', 169, 996, 1737, 204)
        self.add('commandbutton', 'cb_add', 242, 1056, 242, 92, text='&Add', taborder=60)
        self.add('commandbutton', 'cb_edit', 498, 1056, 242, 92, text='&Edit', taborder=70)
        self.add('commandbutton', 'cb_delete', 759, 1056, 242, 92, text='&Delete', taborder=90)
        self.add('commandbutton', 'cb_save', 1083, 1056, 242, 92, text='&Save', taborder=100)
        self.add('commandbutton', 'cb_cancel', 1339, 1056, 242, 92, text='&Cancel', taborder=110)
        self.add('commandbutton', 'cb_exit', 1600, 1056, 242, 92, text='E&xit', taborder=120)
