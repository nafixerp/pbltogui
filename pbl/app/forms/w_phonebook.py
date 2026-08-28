"""Phone Book — w_phonebook.

Generated from the PowerBuilder window ``w_phonebook.srw`` by
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
    name='w_phonebook',
    title='Phone Book',
    width=3465,
    height=1732,
    controls=[],
    tables=['phonebook'],
    source_path='w_phonebook.srw',
    report={'dataobject': 'd_phonehlp', 'sql': 'SELECT phonebook.name AS phonebook_name, phonebook.no AS phonebook_no, phonebook.resphone AS phonebook_resphone, phonebook.offphone AS phonebook_offphone, phonebook.ptype AS phonebook_ptype FROM phonebook ORDER BY phonebook.name ASC', 'computes': [], 'args': [], 'arg_types': {}, 'tables': ['phonebook'], 'columns': [{'name': 'name', 'label': 'name', 'type': 'char'}, {'name': 'no', 'label': 'no', 'type': 'char'}, {'name': 'resphone', 'label': 'resphone', 'type': 'char'}, {'name': 'offphone', 'label': 'offphone', 'type': 'char'}, {'name': 'ptype', 'label': 'ptype', 'type': 'char'}]},
    opens=['w_phoneptype', 'w_phonebooklist'],
    prints=['d_phonebook_print'],
)


class PhoneBookForm(GeneratedForm):
    """Phone Book"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('datawindow', 'dw_type1', 9, 0, 1015, 88, dataobject='d_phoneptypecode', taborder=10)
        self.add('singlelineedit', 'sle_name', 2409, 0, 1024, 92, taborder=40)
        self.add('statictext', 'st_2', 2144, 16, 261, 76, text='Name :')
        self.add('multilineedit', 'sle_resaddress', 2409, 96, 1024, 360, taborder=50)
        self.add('statictext', 'st_3', 1989, 104, 416, 76, text='Res. Address :')
        self.add('statictext', 'st_1', 9, 108, 1920, 68, text='Search')
        self.add('datawindow', 'dw_search', 9, 188, 1920, 92, dataobject='d_phonesearch', taborder=20)
        self.add('datawindow', 'dw_list', 9, 292, 1920, 1176, dataobject='d_phonehlp', taborder=30)
        self.add('singlelineedit', 'sle_resphone', 2409, 460, 1024, 92, taborder=60)
        self.add('statictext', 'st_5', 1989, 476, 416, 76, text='Res. Phone :')
        self.add('multilineedit', 'sle_offaddress', 2409, 556, 1024, 360, taborder=70)
        self.add('statictext', 'st_4', 1938, 560, 466, 76, text='Office Address :')
        self.add('statictext', 'st_6', 1979, 916, 425, 76, text='Office Phone :')
        self.add('singlelineedit', 'sle_offphone', 2409, 920, 1024, 92, taborder=80)
        self.add('singlelineedit', 'sle_mobile', 2409, 1016, 1024, 92, taborder=90)
        self.add('statictext', 'st_7', 2039, 1036, 366, 76, text='Mobile No :')
        self.add('singlelineedit', 'sle_email', 2409, 1112, 1024, 92, taborder=100)
        self.add('statictext', 'st_8', 2144, 1124, 261, 76, text='Email :')
        self.add('datawindow', 'dw_type2', 2409, 1216, 1015, 88, dataobject='d_phoneptypecode', taborder=110)
        self.add('statictext', 'st_9', 2158, 1220, 247, 76, text='Type :')
        self.add('datawindow', 'dw_grp', 2409, 1316, 677, 88, dataobject='d_clientsgrp_code', taborder=71)
        self.add('statictext', 'st_10', 2158, 1328, 247, 76, text='Group :')
        self.add('datawindow', 'dw_print', 576, 1504, 270, 132, dataobject='d_phonebook_print', taborder=150)
        self.add('commandbutton', 'cb_newtype', 9, 1516, 288, 100, text='&New Type', taborder=180)
        self.add('commandbutton', 'cb_refresh', 1102, 1516, 229, 100, text='&Refresh', taborder=190)
        self.add('commandbutton', 'cb_print', 1344, 1516, 229, 100, text='&Print', taborder=170)
        self.add('commandbutton', 'cb_list', 1586, 1516, 229, 100, text='&List', taborder=200)
        self.add('commandbutton', 'cb_edit', 1829, 1516, 229, 100, text='&Edit', taborder=130)
        self.add('commandbutton', 'cb_add', 2066, 1516, 229, 100, text='&Add', taborder=120)
        self.add('commandbutton', 'cb_delete', 2309, 1516, 229, 100, text='&Delete', taborder=140)
        self.add('commandbutton', 'cb_2', 2551, 1516, 229, 100, text='E&xit', taborder=160)
