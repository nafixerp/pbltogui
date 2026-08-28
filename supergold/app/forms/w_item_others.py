"""Other Items — w_item_others.

Generated from the PowerBuilder window ``w_item_others.srw`` by
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
    name='w_item_others',
    title='Other Items',
    width=1824,
    height=1368,
    controls=[],
    tables=['itemsothers', 'otheritemtrans'],
    source_path='w_item_others.srw',
    opens=['w_item_others_help'],
)


class OtherItemsForm(GeneratedForm):
    """Other Items"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('statictext', 'st_head', 87, 8, 1595, 76, text='Add New Item')
        self.add('singlelineedit', 'sle_code', 553, 128, 398, 88, limit=10, taborder=20)
        self.add('statictext', 'st_1', 256, 144, 274, 72, text='Code :')
        self.add('singlelineedit', 'sle_desc', 553, 224, 1065, 88, limit=30, taborder=30)
        self.add('statictext', 'st_2', 229, 244, 302, 72, text='Name :')
        self.add('datawindow', 'dw_grp', 553, 320, 805, 92, dataobject='d_itemgrpcode', taborder=40)
        self.add('statictext', 'st_10', 283, 344, 247, 76, text='Group :')
        self.add('editmask', 'em_srate', 553, 420, 398, 96, taborder=50)
        self.add('statictext', 'st_5', 169, 436, 361, 76, text='Sales Rate :')
        self.add('editmask', 'em_prate', 553, 520, 398, 96, taborder=60)
        self.add('statictext', 'st_6', 59, 532, 471, 76, text='Purchase Rate :')
        self.add('editmask', 'em_opstock', 553, 620, 398, 96, taborder=70)
        self.add('statictext', 'st_4', 201, 640, 329, 76, text='Op. Stock :')
        self.add('editmask', 'em_opcost', 553, 716, 398, 96, taborder=10)
        self.add('statictext', 'st_3', 233, 728, 297, 76, text='Op. Cost :')
        self.add('editmask', 'em_stock', 553, 820, 398, 96, taborder=80)
        self.add('statictext', 'st_7', 224, 832, 306, 76, text='Cl. Stock :')
        self.add('checkbox', 'cbx_keepstk', 1179, 912, 393, 76, text='Keep Stock')
        self.add('editmask', 'em_cost', 553, 916, 398, 96, taborder=90)
        self.add('statictext', 'st_8', 261, 940, 270, 76, text='Cl. Cost :')
        self.add('roundrectangle', 'rr_1', 5, 1064, 1778, 172)
        self.add('commandbutton', 'cb_add', 119, 1108, 238, 92, text='&Add', taborder=100)
        self.add('commandbutton', 'cb_edit', 366, 1108, 238, 92, text='&Edit', taborder=110)
        self.add('commandbutton', 'cb_delete', 613, 1108, 238, 92, text='&Delete', taborder=120)
        self.add('commandbutton', 'cb_save', 923, 1108, 238, 92, text='&Save', taborder=130)
        self.add('commandbutton', 'cb_cancel', 1170, 1108, 238, 92, text='&Cancel', taborder=140)
        self.add('commandbutton', 'cb_exit', 1417, 1108, 238, 92, text='E&xit', taborder=150)
