"""New — w_purity_entry.

Generated from the PowerBuilder window ``w_purity_entry.srw`` by
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
    name='w_purity_entry',
    title='New',
    width=2034,
    height=1408,
    controls=[],
    tables=['testdet', 'generali'],
    source_path='w_purity_entry.srw',
)


class NewForm(GeneratedForm):
    """New"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_no', 631, 48, 407, 96, taborder=10)
        self.add('statictext', 'st_1', 320, 56, 293, 80, text='No. :')
        self.add('editmask', 'em_date', 631, 148, 407, 96, taborder=20)
        self.add('statictext', 'st_9', 320, 160, 293, 80, text='Date :')
        self.add('singlelineedit', 'sle_customer', 631, 248, 1353, 100, limit=40, taborder=30)
        self.add('statictext', 'st_2', 270, 252, 343, 80, text='Customer :')
        self.add('editmask', 'em_purityinperc', 631, 352, 407, 96, taborder=40)
        self.add('statictext', 'st_3', 256, 364, 357, 80, text='Purity in % :')
        self.add('editmask', 'em_purityinct', 631, 452, 407, 96, taborder=50)
        self.add('statictext', 'st_4', 224, 476, 389, 80, text='Purity in CT :')
        self.add('singlelineedit', 'sle_otherinfo', 631, 552, 1353, 100, limit=40, taborder=60)
        self.add('statictext', 'st_5', 224, 568, 389, 80, text='Other Info :')
        self.add('editmask', 'em_rcvdon', 631, 656, 407, 96, taborder=70)
        self.add('statictext', 'st_6', 192, 668, 421, 80, text='Received On :')
        self.add('editmask', 'em_testedon', 631, 756, 407, 96, taborder=80)
        self.add('statictext', 'st_7', 192, 768, 421, 80, text='Tested On :')
        self.add('editmask', 'em_rcvdwgt', 631, 856, 407, 96, taborder=90)
        self.add('statictext', 'st_8', 192, 864, 421, 80, text='Rcvd Wgt :')
        self.add('singlelineedit', 'sle_typeofsample', 631, 956, 1353, 100, limit=40, taborder=100)
        self.add('statictext', 'st_10', 96, 968, 517, 80, text='Type Of Sample :')
        self.add('commandbutton', 'cb_save', 635, 1120, 343, 124, text='&Save', taborder=110)
        self.add('commandbutton', 'cb_exit', 1061, 1120, 343, 124, text='E&xit', taborder=120)
