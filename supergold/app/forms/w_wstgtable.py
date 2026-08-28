"""Wastage Table — w_wstgtable.

Generated from the PowerBuilder window ``w_wstgtable.srw`` by
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
    name='w_wstgtable',
    title='Wastage Table',
    width=1687,
    height=1572,
    controls=[],
    tables=['wstgtable', 'items'],
    source_path='w_wstgtable.srw',
    report={'dataobject': 'd_wstgmast', 'sql': 'SELECT wstgtable.weight1 AS wstgtable_weight1, wstgtable.weight2 AS wstgtable_weight2, wstgtable.wastage AS wstgtable_wastage, wstgtable.perc AS wstgtable_perc FROM wstgtable', 'args': ['rcode', 'rtype'], 'arg_types': {'rcode': 'string', 'rtype': 'string'}, 'tables': ['wstgtable'], 'columns': [{'name': 'weight1', 'label': 'From Wgt', 'type': 'decimal'}, {'name': 'weight2', 'label': 'To Wgt', 'type': 'decimal'}, {'name': 'wastage', 'label': 'Wastage', 'type': 'decimal'}, {'name': 'perc', 'label': '%', 'type': 'decimal'}]},
)


class WastageTableForm(GeneratedForm):
    """Wastage Table"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('singlelineedit', 'sle_itemcode', 219, 4, 421, 88, limit=10, taborder=10)
        self.add('datawindow', 'dw_type', 1047, 4, 443, 88, dataobject='d_itemqtypecode', taborder=11)
        self.add('statictext', 'st_1', 18, 8, 183, 76, text='Item :')
        self.add('commandbutton', 'cb_help', 654, 8, 169, 84, text='&Help')
        self.add('statictext', 'st_2', 846, 12, 192, 76, text='Type :')
        self.add('commandbutton', 'cb_show', 1495, 12, 169, 84, text='Show', taborder=20)
        self.add('datawindow', 'dw_wstgset', 14, 116, 1632, 1132, dataobject='d_wstgmast', taborder=30)
        self.add('roundrectangle', 'rr_1', 279, 1276, 1125, 184)
        self.add('commandbutton', 'cb_add', 306, 1312, 251, 108, text='&Add', taborder=50)
        self.add('commandbutton', 'cb_delete', 567, 1312, 251, 108, text='&Delete', taborder=60)
        self.add('commandbutton', 'cb_ok', 841, 1312, 251, 108, text='&Save', taborder=40)
        self.add('commandbutton', 'cb_1', 1106, 1312, 251, 108, text='E&xit', taborder=70)
