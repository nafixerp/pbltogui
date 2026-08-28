"""Journal — w_journal.

Generated from the PowerBuilder window ``w_journal.srw`` by
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
    name='w_journal',
    title='Journal',
    width=2629,
    height=1392,
    controls=[],
    tables=['daybook', 'kurifinishdet', 'clients_kuridet', 'collection', 'kuricolln', 'daybookratewgt', 'accountm', 'generali', 'daybookpart', 'delpart'],
    source_path='w_journal.srw',
)


class JournalForm(GeneratedForm):
    """Journal"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('singlelineedit', 'sle_no', 507, 32, 411, 92)
        self.add('editmask', 'em_date', 1321, 32, 416, 92, taborder=10)
        self.add('statictext', 'st_2', 1129, 40, 183, 76, text='Date :')
        self.add('checkbox', 'cbx_autoamt', 1810, 40, 498, 76, text='Auto Amt Aloc')
        self.add('checkbox', 'cbx_updtfr', 2368, 40, 165, 80, text='&Fr')
        self.add('statictext', 'st_1', 105, 44, 389, 76, text='Voucher No :')
        self.add('datawindow', 'dw_1', 37, 164, 2546, 744, dataobject='d_journal', taborder=20)
        self.add('commandbutton', 'cb_addrow', 50, 812, 206, 88, text='Add', taborder=100)
        self.add('commandbutton', 'cb_deleterow', 270, 812, 206, 88, text='Delete', taborder=110)
        self.add('singlelineedit', 'sle_narr', 425, 924, 2158, 92, limit=100, taborder=30)
        self.add('statictext', 'st_10', 110, 932, 320, 76, text='Narration :')
        self.add('roundrectangle', 'rr_1', 379, 1064, 1902, 180)
        self.add('commandbutton', 'cb_add', 453, 1108, 283, 100, text='&Add', taborder=40)
        self.add('commandbutton', 'cb_edit', 745, 1108, 279, 100, text='&Edit', taborder=50)
        self.add('commandbutton', 'cb_delete', 1029, 1108, 279, 100, text='&Delete', taborder=60)
        self.add('commandbutton', 'cb_save', 1367, 1108, 279, 100, text='&Save', taborder=70)
        self.add('commandbutton', 'cb_cancel', 1650, 1108, 279, 100, text='&Cancel', taborder=80)
        self.add('commandbutton', 'cb_exit', 1934, 1108, 279, 100, text='E&xit', taborder=90)
        self.add('checkbox', 'cbx_print', 64, 1116, 274, 68, text='&Print')
