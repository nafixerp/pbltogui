"""Position Settings — w_accounts_position.

Generated from the PowerBuilder window ``w_accounts_position.srw`` by
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
    name='w_accounts_position',
    title='Position Settings',
    width=2875,
    height=1788,
    controls=[],
    tables=['accountm', 'accountg', 'accountgbs'],
    source_path='w_accounts_position.srw',
    grid={'control': 'dw_updaterep', 'dataobject': 'd_accounts_position', 'table': 'accountm', 'keys': ['accode'], 'columns': [{'name': 'accode', 'label': 'A/c Code', 'type': 'char'}, {'name': 'name', 'label': 'A/c Name', 'type': 'char'}, {'name': 'grcode', 'label': 'grcode', 'type': 'char'}, {'name': 'tplpos', 'label': 'tplpos', 'type': 'long'}, {'name': 'bshead', 'label': 'bshead', 'type': 'char'}, {'name': 'shepos', 'label': 'shepos', 'type': 'long'}, {'name': 'shedgrp', 'label': 'shedgrp', 'type': 'char'}]},
    report={'dataobject': 'd_accounts_position', 'sql': 'SELECT accountm.accode AS accountm_accode, accountm.name AS accountm_name, accountm.grcode AS accountm_grcode, accountm.tplpos AS accountm_tplpos, accountm.bshead AS accountm_bshead, accountm.shepos AS accountm_shepos, accountm.shedgrp AS accountm_shedgrp FROM accountm ORDER BY accountm.name ASC', 'args': [], 'arg_types': {}, 'tables': ['accountm'], 'columns': [{'name': 'accode', 'label': 'A/c Code', 'type': 'char'}, {'name': 'name', 'label': 'A/c Name', 'type': 'char'}, {'name': 'grcode', 'label': 'grcode', 'type': 'char'}, {'name': 'tplpos', 'label': 'tplpos', 'type': 'long'}, {'name': 'bshead', 'label': 'bshead', 'type': 'char'}, {'name': 'shepos', 'label': 'shepos', 'type': 'long'}, {'name': 'shedgrp', 'label': 'shedgrp', 'type': 'char'}]},
)


class PositionSettingsForm(GeneratedForm):
    """Position Settings"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('commandbutton', 'cb_sortpos', 1413, 0, 370, 88, text='Position', taborder=20)
        self.add('commandbutton', 'cb_sorttradepos', 1806, 0, 466, 88, text='Trade,Prof Grp', taborder=30)
        self.add('commandbutton', 'cb_sortschedpos', 2290, 0, 453, 88, text='Schedule Pos.', taborder=31)
        self.add('dropdownlistbox', 'ddlb_type', 297, 4, 814, 492, text='Accounts Position', items=['Accounts Position', 'Group Position', 'BS Head Position'], taborder=10)
        self.add('statictext', 'st_1', 27, 12, 247, 76, text='Type :')
        self.add('statictext', 'st_2', 1138, 16, 247, 76, text='Sort On')
        self.add('datawindow', 'dw_updaterep', 0, 108, 2843, 1344, dataobject='d_accounts_position', taborder=50)
        self.add('oval', 'oval_1', 1006, 1432, 891, 228)
        self.add('commandbutton', 'cb_update', 1179, 1500, 270, 96, text='&Update', taborder=60)
        self.add('commandbutton', 'cb_2', 1490, 1500, 270, 96, text='E&xit', taborder=40)
