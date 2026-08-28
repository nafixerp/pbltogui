"""Denomination Entry — w_denom_trans.

Generated from the PowerBuilder window ``w_denom_trans.srw`` by
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
    name='w_denom_trans',
    title='Denomination Entry',
    width=2775,
    height=2128,
    controls=[],
    tables=['denom_trans'],
    source_path='w_denom_trans.srw',
    grid={'control': 'dw_1', 'dataobject': 'd_denom_trans', 'table': 'denom_master', 'keys': ['code'], 'computes': [{'name': 'amt', 'expression': ' cvalue *  nos ', 'format': '###########0.00', 'label': 'amt', 'band': 'detail'}, {'name': 'totalval', 'expression': 'sum(amt for all)', 'format': '#########0.00', 'label': 'totalval', 'band': 'summary'}, {'name': 'compute_2', 'expression': 'max(cash for all)', 'format': '########0.00', 'label': 'compute_2', 'band': 'summary'}, {'name': 'compute_1', 'expression': ' totalval  - max(cash for all)', 'format': '########0.00', 'label': 'compute_1', 'band': 'summary'}], 'columns': [{'name': 'code', 'label': 'code', 'type': 'char'}, {'name': 'name', 'label': "Denomination\t'Denomination - '+string(rdate,'dd/mm/yyyy')", 'type': 'char'}, {'name': 'cvalue', 'label': 'cvalue', 'type': 'decimal'}, {'name': 'nos', 'label': 'Nos', 'type': 'long'}, {'name': 'cash', 'label': 'cash', 'type': 'decimal'}]},
    report={'dataobject': 'd_denom_trans', 'sql': 'SELECT denom_master.code AS denom_master_code, denom_master.name AS denom_master_name, denom_master.cvalue AS denom_master_cvalue, (select sum(denom_trans.nos) from denom_trans where denom_trans.denom_code = denom_master.code and denom_trans.tdate = :rdate) as nos, (0.00001) as cash FROM denom_master ORDER BY denom_master.code ASC', 'computes': [{'name': 'amt', 'expression': ' cvalue *  nos ', 'format': '###########0.00', 'label': 'amt', 'band': 'detail'}, {'name': 'totalval', 'expression': 'sum(amt for all)', 'format': '#########0.00', 'label': 'totalval', 'band': 'summary'}, {'name': 'compute_2', 'expression': 'max(cash for all)', 'format': '########0.00', 'label': 'compute_2', 'band': 'summary'}, {'name': 'compute_1', 'expression': ' totalval  - max(cash for all)', 'format': '########0.00', 'label': 'compute_1', 'band': 'summary'}], 'args': ['rdate'], 'arg_types': {'rdate': 'date'}, 'tables': ['denom_master'], 'columns': [{'name': 'code', 'label': 'code', 'type': 'char'}, {'name': 'name', 'label': "Denomination\t'Denomination - '+string(rdate,'dd/mm/yyyy')", 'type': 'char'}, {'name': 'cvalue', 'label': 'cvalue', 'type': 'decimal'}, {'name': 'nos', 'label': 'Nos', 'type': 'long'}, {'name': 'cash', 'label': 'cash', 'type': 'decimal'}]},
)


class DenominationEntryForm(GeneratedForm):
    """Denomination Entry"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date', 146, 4, 448, 104, text='none', taborder=10)
        self.add('editmask', 'em_cash', 1070, 4, 402, 104, text='none', taborder=20)
        self.add('editmask', 'em_diff', 1879, 4, 480, 104, taborder=20)
        self.add('statictext', 'st_1', 5, 16, 174, 76, text='Date')
        self.add('statictext', 'st_2', 905, 16, 174, 76, text='Cash')
        self.add('statictext', 'st_3', 1710, 16, 155, 76, text='Diff')
        self.add('datawindow', 'dw_1', 18, 112, 2725, 1772, dataobject='d_denom_trans', taborder=10)
        self.add('commandbutton', 'cb_cancel', 690, 1892, 329, 132, text='&Cancel', taborder=40)
        self.add('commandbutton', 'cb_save', 1033, 1892, 329, 132, text='&Save', taborder=50)
        self.add('commandbutton', 'cb_print', 1371, 1892, 329, 132, text='&Print', taborder=70)
        self.add('commandbutton', 'cb_exit', 1710, 1892, 329, 132, text='E&xit', taborder=60)
