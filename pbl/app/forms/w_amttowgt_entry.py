"""Amt, Wgt Transfer Entry — w_amttowgt_entry.

Generated from the PowerBuilder window ``w_amttowgt_entry.srw`` by
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
    name='w_amttowgt_entry',
    title='Amt, Wgt Transfer Entry',
    width=2021,
    height=1440,
    controls=[],
    tables=['daybook', 'daybookratewgt', 'clients', 'generali', 'daybookpart'],
    source_path='w_amttowgt_entry.srw',
)


class AmtWgtTransferEntryForm(GeneratedForm):
    """Amt, Wgt Transfer Entry"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date', 713, 0, 402, 92, taborder=10)
        self.add('statictext', 'st_2', 448, 12, 247, 76, text='Date :')
        self.add('datawindow', 'dw_accode', 713, 96, 402, 88, dataobject='d_cust', taborder=20)
        self.add('statictext', 'st_10', 357, 108, 338, 72, text='Party  :')
        self.add('singlelineedit', 'sle_name', 713, 188, 1253, 92)
        self.add('statictext', 'st_9', 352, 196, 343, 80, text='Name :')
        self.add('editmask', 'em_balance', 713, 284, 421, 96)
        self.add('editmask', 'em_pwgtbal', 1545, 284, 421, 96)
        self.add('statictext', 'st_11', 274, 296, 421, 80, text='Amt Balance :')
        self.add('statictext', 'st_14', 1225, 296, 302, 80, text='Wgt Bal :')
        self.add('dropdownlistbox', 'ddlb_ttype', 713, 384, 421, 400, text='Amt To Wgt', items=['Amt To Wgt', 'Wgt To Amt'], taborder=30)
        self.add('statictext', 'st_3', 247, 392, 448, 76, text='Transfer Type :')
        self.add('editmask', 'em_amt', 713, 484, 421, 100, taborder=40)
        self.add('statictext', 'st_1', 197, 496, 498, 80, text='Amt To Convert :')
        self.add('editmask', 'em_rate', 713, 588, 421, 100, taborder=50)
        self.add('statictext', 'st_4', 366, 600, 329, 76, text='Rate :')
        self.add('editmask', 'em_weight', 713, 692, 421, 100, taborder=60)
        self.add('statictext', 'st_7', 384, 704, 311, 76, text='Weight :')
        self.add('editmask', 'em_clbalance', 713, 800, 421, 96)
        self.add('statictext', 'st_8', 219, 808, 475, 76, text='A/c Cl.Balance :')
        self.add('editmask', 'em_clwgtbal', 713, 904, 421, 96)
        self.add('statictext', 'st_13', 197, 908, 498, 76, text='Wgt Cl.Balance :')
        self.add('oval', 'oval_1', 622, 1088, 681, 168)
        self.add('commandbutton', 'cb_ok', 713, 1124, 251, 96, text='&Ok', taborder=70)
        self.add('commandbutton', 'cb_exit', 969, 1124, 251, 96, text='E&xit', taborder=80)
