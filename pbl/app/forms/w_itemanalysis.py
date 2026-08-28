"""Item Movement — w_itemanalysis.

Generated from the PowerBuilder window ``w_itemanalysis.srw`` by
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
    name='w_itemanalysis',
    title='Item Movement',
    width=3657,
    height=2196,
    controls=[],
    tables=[],
    source_path='w_itemanalysis.srw',
    report={'dataobject': 'd_itemanalysis', 'sql': 'SELECT items.name AS items_name, salesd.qty AS salesd_qty, salesd.weight AS salesd_weight, salesm.slno AS salesm_slno, salesm.control AS salesm_control FROM items, salesd, salesm WHERE items.code = salesd.code AND salesd.slno = salesm.slno AND salesm.control <= :rlevel AND items.itype = :rtype ORDER BY items.name ASC', 'computes': [], 'args': ['rdate1', 'rdate2', 'rlevel', 'rtype', 'rcode'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date', 'rlevel': 'number', 'rtype': 'string', 'rcode': 'string'}, 'tables': ['items', 'salesd', 'salesm'], 'columns': [{'name': 'items_name', 'label': 'items_name', 'type': 'char'}, {'name': 'salesd_qty', 'label': 'salesd_qty', 'type': 'long'}, {'name': 'salesd_weight', 'label': 'salesd_weight', 'type': 'decimal'}, {'name': 'salesm_slno', 'label': 'salesm_slno', 'type': 'decimal'}, {'name': 'salesm_control', 'label': 'salesm_control', 'type': 'long'}]},
    opens=['w_itemhelp'],
)


class ItemMovementForm(GeneratedForm):
    """Item Movement"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('singlelineedit', 'sle_itemcode', 402, 0, 416, 96, limit=10, taborder=31)
        self.add('commandbutton', 'cb_help', 827, 0, 187, 96, text='&Help', taborder=41)
        self.add('editmask', 'em_date1', 1298, 0, 375, 96, taborder=51)
        self.add('editmask', 'em_date2', 2194, 0, 379, 96, taborder=61)
        self.add('commandbutton', 'cb_1', 3118, 0, 247, 100, text='&Print', taborder=30)
        self.add('commandbutton', 'cb_2', 3369, 0, 247, 100, text='E&xit', taborder=20)
        self.add('commandbutton', 'cb_show', 2610, 4, 247, 92, text='Show', taborder=31)
        self.add('statictext', 'st_3', 41, 8, 347, 72, text='Item Code :')
        self.add('statictext', 'st_1', 1083, 8, 206, 76, text='From :')
        self.add('statictext', 'st_2', 2066, 8, 119, 76, text='To :')
        self.add('statictext', 'st_4', 0, 96, 389, 72, text='Graph Type :')
        self.add('dropdownlistbox', 'ddlb_graphtype', 402, 100, 512, 400, text='Itemwise', items=['Item Wise', 'Monthly Wise'], taborder=31)
        self.add('dropdownlistbox', 'ddlb_itemtype', 1298, 100, 498, 400, text='Gold', items=['Gold', 'Silver', 'Others'], taborder=41)
        self.add('dropdownlistbox', 'ddlb_valuetype', 2194, 100, 498, 400, text='Weight wise', items=['Weight Wise', 'Qty Wise', 'Amt Wise'], taborder=21)
        self.add('statictext', 'st_6', 951, 108, 338, 76, text='Item Type :')
        self.add('statictext', 'st_5', 1810, 112, 379, 76, text='Value Type :')
        self.add('datawindow', 'dw_history', 0, 196, 3630, 1900, dataobject='d_itemanalysis', taborder=10)
