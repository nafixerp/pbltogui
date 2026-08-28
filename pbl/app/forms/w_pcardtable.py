"""Prev. Card Table — w_pcardtable.

Generated from the PowerBuilder window ``w_pcardtable.srw`` by
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
    name='w_pcardtable',
    title='Prev. Card Table',
    width=2770,
    height=1376,
    controls=[],
    tables=[],
    source_path='w_pcardtable.srw',
    grid={'control': 'dw_1', 'dataobject': 'd_pcardtable', 'table': 'pcardtable', 'keys': ['pcard', 'isubgrp'], 'columns': [{'name': 'pcard', 'label': 'Prev.Card', 'type': 'char'}, {'name': 'isubgrp', 'label': 'Item Sub Grp', 'type': 'char'}, {'name': 'pointbasedon', 'label': 'Point Based On', 'type': 'char'}, {'name': 'valuefor1point', 'label': 'Value for 1 Point', 'type': 'decimal'}, {'name': 'valueperpoint', 'label': 'RS Value / Point', 'type': 'decimal'}, {'name': 'minsalesamt', 'label': 'Min Sales Amt', 'type': 'decimal'}, {'name': 'rounddown', 'label': 'Round Down', 'type': 'decimal'}]},
    report={'dataobject': 'd_pcardtable', 'sql': 'SELECT pcardtable.pcard AS pcardtable_pcard, pcardtable.isubgrp AS pcardtable_isubgrp, pcardtable.pointbasedon AS pcardtable_pointbasedon, pcardtable.valuefor1point AS pcardtable_valuefor1point, pcardtable.valueperpoint AS pcardtable_valueperpoint, pcardtable.minsalesamt AS pcardtable_minsalesamt, pcardtable.rounddown AS pcardtable_rounddown FROM pcardtable', 'args': [], 'arg_types': {}, 'tables': ['pcardtable'], 'columns': [{'name': 'pcard', 'label': 'Prev.Card', 'type': 'char'}, {'name': 'isubgrp', 'label': 'Item Sub Grp', 'type': 'char'}, {'name': 'pointbasedon', 'label': 'Point Based On', 'type': 'char'}, {'name': 'valuefor1point', 'label': 'Value for 1 Point', 'type': 'decimal'}, {'name': 'valueperpoint', 'label': 'RS Value / Point', 'type': 'decimal'}, {'name': 'minsalesamt', 'label': 'Min Sales Amt', 'type': 'decimal'}, {'name': 'rounddown', 'label': 'Round Down', 'type': 'decimal'}]},
)


class PrevCardTableForm(GeneratedForm):
    """Prev. Card Table"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('datawindow', 'dw_1', 5, 0, 2738, 1140, dataobject='d_pcardtable', taborder=10)
        self.add('roundrectangle', 'rr_1', 713, 1148, 1358, 140)
        self.add('commandbutton', 'cb_add', 750, 1168, 242, 92, text='&Add', taborder=20)
        self.add('commandbutton', 'cb_delete', 1001, 1168, 242, 92, text='&Delete', taborder=30)
        self.add('commandbutton', 'cb_cancel', 1285, 1168, 242, 92, text='&Cancel', taborder=40)
        self.add('commandbutton', 'cb_save', 1536, 1168, 242, 92, text='&Save', taborder=50)
        self.add('commandbutton', 'cb_exit', 1787, 1168, 242, 92, text='E&xit', taborder=60)
