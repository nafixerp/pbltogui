"""Ruff Work — w_ruffwork.

Generated from the PowerBuilder window ``w_ruffwork.srw`` by
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
    name='w_ruffwork',
    title='Ruff Work',
    width=3657,
    height=1856,
    controls=[],
    tables=['ruffwrk', 'items', 'accountm'],
    source_path='w_ruffwork.srw',
    grid={'control': 'dw_ruffwork', 'dataobject': 'd_ruffwork', 'table': 'ruffwrk', 'keys': ['slno'], 'columns': [{'name': 'slno', 'label': 'slno', 'type': 'decimal'}, {'name': 'party', 'label': 'Party', 'type': 'char'}, {'name': 'tdate', 'label': 'Date', 'type': 'date'}, {'name': 'item', 'label': 'Item', 'type': 'char'}, {'name': 'qty', 'label': 'qty', 'type': 'char'}, {'name': 'weight', 'label': 'weight', 'type': 'char'}, {'name': 'amount', 'label': 'Amount', 'type': 'char'}, {'name': 'part', 'label': 'Particulars', 'type': 'char'}, {'name': 'inexp', 'label': 'inexp', 'type': 'char'}, {'name': 'sman', 'label': 'sman', 'type': 'char'}, {'name': 'person', 'label': 'person', 'type': 'char'}, {'name': 'pend', 'label': 'In/Exp', 'type': 'long'}, {'name': 'number', 'label': 'number', 'type': 'long'}, {'name': 'control', 'label': 'control', 'type': 'long'}]},
    report={'dataobject': 'd_ruffwork', 'sql': 'SELECT ruffwrk.slno AS ruffwrk_slno, ruffwrk.party AS ruffwrk_party, ruffwrk.tdate AS ruffwrk_tdate, ruffwrk.item AS ruffwrk_item, ruffwrk.qty AS ruffwrk_qty, ruffwrk.weight AS ruffwrk_weight, ruffwrk.amount AS ruffwrk_amount, ruffwrk.part AS ruffwrk_part, ruffwrk.inexp AS ruffwrk_inexp, ruffwrk.sman AS ruffwrk_sman, ruffwrk.person AS ruffwrk_person, ruffwrk.pend AS ruffwrk_pend, ruffwrk.number AS ruffwrk_number, ruffwrk.control AS ruffwrk_control FROM ruffwrk', 'args': [], 'arg_types': {}, 'tables': ['ruffwrk'], 'columns': [{'name': 'slno', 'label': 'slno', 'type': 'decimal'}, {'name': 'party', 'label': 'Party', 'type': 'char'}, {'name': 'tdate', 'label': 'Date', 'type': 'date'}, {'name': 'item', 'label': 'Item', 'type': 'char'}, {'name': 'qty', 'label': 'qty', 'type': 'char'}, {'name': 'weight', 'label': 'weight', 'type': 'char'}, {'name': 'amount', 'label': 'Amount', 'type': 'char'}, {'name': 'part', 'label': 'Particulars', 'type': 'char'}, {'name': 'inexp', 'label': 'inexp', 'type': 'char'}, {'name': 'sman', 'label': 'sman', 'type': 'char'}, {'name': 'person', 'label': 'person', 'type': 'char'}, {'name': 'pend', 'label': 'In/Exp', 'type': 'long'}, {'name': 'number', 'label': 'number', 'type': 'long'}, {'name': 'control', 'label': 'control', 'type': 'long'}]},
)


class RuffWorkForm(GeneratedForm):
    """Ruff Work"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('datawindow', 'dw_ruffwork', 0, 0, 3634, 1448, dataobject='d_ruffwork', taborder=10)
        self.add('roundrectangle', 'rr_1', 485, 1484, 2281, 176)
        self.add('commandbutton', 'cb_add', 549, 1520, 242, 100, text='&Add', taborder=80)
        self.add('commandbutton', 'cb_delete', 800, 1520, 242, 100, text='&Delete', taborder=20)
        self.add('commandbutton', 'cb_print', 1102, 1520, 242, 100, text='&Print', taborder=70)
        self.add('commandbutton', 'cb_cancel', 1947, 1520, 242, 100, text='&Cancel', taborder=30)
        self.add('commandbutton', 'cb_save', 2199, 1520, 242, 100, text='&Save', taborder=50)
        self.add('commandbutton', 'cb_exit', 2491, 1520, 242, 100, text='E&xit', taborder=60)
        self.add('dropdownlistbox', 'ddlb_type', 1403, 1524, 503, 256, text='All', items=['All', 'Pending Only'], taborder=40)
