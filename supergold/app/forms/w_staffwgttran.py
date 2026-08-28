"""Wgt Transaction — w_staffwgttran.

Generated from the PowerBuilder window ``w_staffwgttran.srw`` by
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
    name='w_staffwgttran',
    title='Wgt Transaction',
    width=3136,
    height=2208,
    controls=[],
    tables=['staffwgtm', 'staffwgtd', 'sman', 'items', 'generali'],
    source_path='w_staffwgttran.srw',
)


class WgtTransactionForm(GeneratedForm):
    """Wgt Transaction"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date', 2194, 0, 379, 100, taborder=20)
        self.add('statictext', 'st_1', 1984, 4, 197, 76, text='Date :')
        self.add('datawindow', 'dw_smcode', 265, 8, 672, 88, dataobject='d_smancode', taborder=10)
        self.add('statictext', 'st_docno', 1376, 8, 389, 88)
        self.add('statictext', 'st_2', 32, 12, 224, 76, text='SMan :')
        self.add('statictext', 'st_6', 1102, 12, 256, 76, text='Doc No :')
        self.add('dropdownlistbox', 'ddlb_ttype', 2190, 100, 471, 356, text='Issue', items=['Issue', 'Rcpt', 'Sales'], taborder=40)
        self.add('singlelineedit', 'sle_route', 265, 104, 1093, 92, taborder=30)
        self.add('statictext', 'st_5', 1810, 112, 370, 76, text='Trans Type :')
        self.add('statictext', 'st_3', 9, 116, 247, 76, text='Route :')
        self.add('datawindow', 'dw_1', 14, 204, 3099, 1792, dataobject='d_staffwgttran', taborder=50)
        self.add('statictext', 'st_25', 402, 208, 5, 1680)
        self.add('statictext', 'st_4', 1243, 208, 5, 1788)
        self.add('statictext', 'st_20', 1495, 208, 5, 1788)
        self.add('statictext', 'st_21', 1833, 208, 5, 1788)
        self.add('statictext', 'st_22', 2094, 208, 5, 1788)
        self.add('statictext', 'st_23', 2382, 208, 5, 1788)
        self.add('statictext', 'st_58', 2670, 208, 5, 1788)
        self.add('commandbutton', 'cb_add', 23, 1888, 187, 84, text='&Add')
        self.add('commandbutton', 'cb_delete', 215, 1888, 192, 84, text='&Delete')
        self.add('commandbutton', 'cb_update', 1518, 2016, 261, 100, text='&Save', taborder=70)
        self.add('commandbutton', 'cb_1', 1792, 2016, 261, 100, text='&Print', taborder=80)
        self.add('commandbutton', 'cb_2', 2066, 2016, 261, 100, text='E&xit', taborder=60)
        self.add('commandbutton', 'cb_edit', 23, 2020, 402, 88, text='Edit Trans')
        self.add('commandbutton', 'cb_cancel', 443, 2020, 402, 88, text='Cancel Trans')
        self.add('checkbox', 'cbx_speed', 2359, 2024, 425, 76, text='Speed Print')
