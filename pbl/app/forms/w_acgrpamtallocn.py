"""Group Amt Allocation — w_acgrpamtallocn.

Generated from the PowerBuilder window ``w_acgrpamtallocn.srw`` by
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
    name='w_acgrpamtallocn',
    title='Group Amt Allocation',
    width=3191,
    height=1860,
    controls=[],
    tables=['daybook', 'accountm', 'generali', 'daybookpart'],
    source_path='w_acgrpamtallocn.srw',
    grid={'control': 'dw_trans', 'dataobject': 'd_acgrptrans', 'table': 'accountm', 'keys': ['accode'], 'columns': [{'name': 'ttran', 'label': 'ttran', 'type': 'decimal'}, {'name': 'name', 'label': 'Name', 'type': 'char'}, {'name': 'accode', 'label': 'accode', 'type': 'char'}, {'name': 'opbal', 'label': 'opbal', 'type': 'decimal'}, {'name': 'opbalb', 'label': 'opbalb', 'type': 'decimal'}, {'name': 'amount', 'label': 'Amount', 'type': 'decimal'}, {'name': 'aclink', 'label': 'aclink', 'type': 'char'}, {'name': 'acperc', 'label': 'acperc', 'type': 'decimal'}]},
    report={'dataobject': 'd_acgrptrans', 'sql': 'SELECT accountm.name AS accountm_name, accountm.accode AS accountm_accode, accountm.opbal AS accountm_opbal, accountm.opbalb AS accountm_opbalb, accountm.amount AS accountm_amount, accountm.aclink AS accountm_aclink, accountm.acperc AS accountm_acperc, (select sum(daybook.amount) from daybook where daybook.accode = accountm.accode and daybook.control <= :rlevel and daybook.tdate <= :rdate) ttran FROM accountm ORDER BY accountm.name ASC', 'args': ['rdate', 'rlevel', 'rgrp'], 'arg_types': {'rdate': 'date', 'rlevel': 'number', 'rgrp': 'string'}, 'tables': ['accountm'], 'columns': [{'name': 'ttran', 'label': 'ttran', 'type': 'decimal'}, {'name': 'name', 'label': 'Name', 'type': 'char'}, {'name': 'accode', 'label': 'accode', 'type': 'char'}, {'name': 'opbal', 'label': 'opbal', 'type': 'decimal'}, {'name': 'opbalb', 'label': 'opbalb', 'type': 'decimal'}, {'name': 'amount', 'label': 'Amount', 'type': 'decimal'}, {'name': 'aclink', 'label': 'aclink', 'type': 'char'}, {'name': 'acperc', 'label': 'acperc', 'type': 'decimal'}]},
)


class GroupAmtAllocationForm(GeneratedForm):
    """Group Amt Allocation"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('datawindow', 'dw_acgrp', 471, 0, 1129, 96, dataobject='d_grcode', taborder=10)
        self.add('statictext', 'st_3', 123, 8, 338, 76, text='A/c Group :')
        self.add('checkbox', 'cbx_credited', 1774, 8, 370, 80, text='Credited')
        self.add('editmask', 'em_date', 471, 100, 485, 100, taborder=20)
        self.add('commandbutton', 'cb_show', 1198, 100, 402, 112, text='&Show')
        self.add('commandbutton', 'cb_setdef', 2130, 100, 402, 112, text='Set Def', taborder=30)
        self.add('statictext', 'st_1', 215, 112, 247, 76, text='Date :')
        self.add('editmask', 'em_totamt', 471, 204, 485, 100, taborder=30)
        self.add('statictext', 'st_4', 23, 220, 439, 76, text='Total Amount :')
        self.add('commandbutton', 'cb_alloc', 1198, 296, 402, 112, text='&Allocate')
        self.add('editmask', 'em_perc', 471, 308, 485, 100, taborder=40)
        self.add('statictext', 'st_5', 23, 320, 439, 76, text='Amt % :')
        self.add('datawindow', 'dw_trans', 9, 432, 3154, 964, dataobject='d_acgrptrans', taborder=50)
        self.add('commandbutton', 'cb_delete', 18, 1300, 229, 80, text='&Delete')
        self.add('singlelineedit', 'sle_part', 448, 1412, 1330, 92, limit=40, taborder=60)
        self.add('statictext', 'st_2', 69, 1424, 361, 76, text='Particulars :')
        self.add('datawindow', 'dw_opac', 448, 1508, 1102, 88, dataobject='d_anyaccode', taborder=70)
        self.add('statictext', 'st_dbcr', 18, 1516, 411, 76, text='Debit A/c :')
        self.add('commandbutton', 'cb_process', 1253, 1632, 338, 108, text='&Save', taborder=80)
        self.add('commandbutton', 'cb_exit', 1600, 1632, 338, 108, text='E&xit', taborder=90)
