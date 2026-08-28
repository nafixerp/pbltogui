"""Edit — w_finance_help.

Generated from the PowerBuilder window ``w_finance_help.srw`` by
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
    name='w_finance_help',
    title='Edit',
    width=2926,
    height=1276,
    controls=[],
    tables=[],
    source_path='w_finance_help.srw',
    grid={'control': 'dw_1', 'dataobject': 'd_finance_help', 'table': 'wgtrcptpmnt', 'keys': ['slno'], 'computes': [], 'columns': [{'name': 'tdate', 'label': 'tdate', 'type': 'date'}, {'name': 'docno', 'label': 'docno', 'type': 'char'}, {'name': 'pname', 'label': 'pname', 'type': 'char'}, {'name': 'ttype', 'label': 'ttype', 'type': 'char'}, {'name': 'weight', 'label': 'weight', 'type': 'decimal'}, {'name': 'note', 'label': 'note', 'type': 'char'}, {'name': 'slno', 'label': 'slno', 'type': 'decimal'}, {'name': 'pcode', 'label': 'pcode', 'type': 'char'}, {'name': 'icode', 'label': 'icode', 'type': 'char'}, {'name': 'finamt', 'label': 'finamt', 'type': 'decimal'}, {'name': 'pend', 'label': 'pend', 'type': 'char'}]},
    report={'dataobject': 'd_finance_help', 'sql': 'SELECT wgtrcptpmnt.tdate AS wgtrcptpmnt_tdate, wgtrcptpmnt.docno AS wgtrcptpmnt_docno, wgtrcptpmnt.pname AS wgtrcptpmnt_pname, wgtrcptpmnt.ttype AS wgtrcptpmnt_ttype, wgtrcptpmnt.weight AS wgtrcptpmnt_weight, wgtrcptpmnt.note AS wgtrcptpmnt_note, wgtrcptpmnt.slno AS wgtrcptpmnt_slno, wgtrcptpmnt.pcode AS wgtrcptpmnt_pcode, wgtrcptpmnt.icode AS wgtrcptpmnt_icode, wgtrcptpmnt.finamt AS wgtrcptpmnt_finamt, wgtrcptpmnt.pend AS wgtrcptpmnt_pend FROM wgtrcptpmnt ORDER BY wgtrcptpmnt.tdate DESC, wgtrcptpmnt.docno DESC', 'computes': [], 'args': ['rlevel'], 'arg_types': {'rlevel': 'number'}, 'tables': ['wgtrcptpmnt'], 'columns': [{'name': 'tdate', 'label': 'tdate', 'type': 'date'}, {'name': 'docno', 'label': 'docno', 'type': 'char'}, {'name': 'pname', 'label': 'pname', 'type': 'char'}, {'name': 'ttype', 'label': 'ttype', 'type': 'char'}, {'name': 'weight', 'label': 'weight', 'type': 'decimal'}, {'name': 'note', 'label': 'note', 'type': 'char'}, {'name': 'slno', 'label': 'slno', 'type': 'decimal'}, {'name': 'pcode', 'label': 'pcode', 'type': 'char'}, {'name': 'icode', 'label': 'icode', 'type': 'char'}, {'name': 'finamt', 'label': 'finamt', 'type': 'decimal'}, {'name': 'pend', 'label': 'pend', 'type': 'char'}]},
)


class EditForm(GeneratedForm):
    """Edit"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('datawindow', 'dw_1', 0, 0, 2898, 1076, dataobject='d_finance_help', taborder=10)
        self.add('statictext', 'st_search', 18, 992, 375, 76)
        self.add('oval', 'oval_1', 1061, 1076, 777, 188)
        self.add('commandbutton', 'cb_ok', 1202, 1124, 247, 92, text='OK', taborder=20)
        self.add('commandbutton', 'cb_cancel', 1467, 1124, 247, 92, text='Cancel', taborder=30)
