"""Advance After — w_ordadvanceafter.

Generated from the PowerBuilder window ``w_ordadvanceafter.srw`` by
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
    name='w_ordadvanceafter',
    title='Advance After',
    width=2985,
    height=1400,
    controls=[],
    tables=['items', 'orderdga', 'advafter', 'daybook', 'orderm', 'generali', 'daybookpart'],
    source_path='w_ordadvanceafter.srw',
)


class AdvanceAfterForm(GeneratedForm):
    """Advance After"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('singlelineedit', 'sle_billno', 608, 60, 430, 92, limit=13, taborder=10)
        self.add('commandbutton', 'cb_help', 1056, 64, 229, 88, text='&Help', taborder=70)
        self.add('editmask', 'em_prevadv', 1829, 64, 430, 88, taborder=80)
        self.add('statictext', 'st_1', 101, 72, 485, 64, text='Enter Order no :')
        self.add('statictext', 'st_4', 1335, 72, 471, 76, text='Prev. Advance :')
        self.add('editmask', 'em_date', 608, 176, 430, 92, taborder=20)
        self.add('editmask', 'em_rate', 1829, 176, 430, 92, taborder=30)
        self.add('statictext', 'st_3', 338, 180, 247, 76, text='Date :')
        self.add('statictext', 'st_5', 1467, 180, 338, 76, text='Gold Rate :')
        self.add('editmask', 'em_amount', 608, 292, 430, 92, taborder=40)
        self.add('statictext', 'st_2', 206, 296, 379, 76, text='Amount :')
        self.add('checkbox', 'cbx_printobcb', 1829, 296, 425, 60, text='Print OB/CB')
        self.add('checkbox', 'cbx_amttowgt', 1829, 376, 690, 80, text='Advance Amt To Wgt')
        self.add('statictext', 'st_9', 1074, 408, 585, 76, text='Weight Advance')
        self.add('datawindow', 'dw_exchange', 0, 496, 2944, 592, dataobject='d_gadvance', taborder=50)
        self.add('statictext', 'st_7', 407, 500, 5, 496)
        self.add('statictext', 'st_14', 1033, 500, 5, 592)
        self.add('statictext', 'st_8', 1298, 500, 5, 592)
        self.add('statictext', 'st_6', 1504, 500, 5, 592)
        self.add('statictext', 'st_10', 1829, 500, 5, 592)
        self.add('statictext', 'st_11', 2089, 500, 5, 592)
        self.add('statictext', 'st_12', 2295, 500, 5, 592)
        self.add('statictext', 'st_13', 2546, 500, 5, 592)
        self.add('commandbutton', 'cb_add', 14, 996, 233, 80, text='&Add', taborder=70)
        self.add('commandbutton', 'cb_delete', 256, 996, 233, 80, text='&Delete', taborder=80)
        self.add('statictext', 'st_stktype', 498, 1004, 192, 64)
        self.add('oval', 'oval_1', 1038, 1100, 640, 220)
        self.add('commandbutton', 'cb_ok', 1097, 1164, 242, 92, text='&OK', taborder=50)
        self.add('commandbutton', 'cb_exit', 1358, 1164, 242, 92, text='E&xit', taborder=60)
