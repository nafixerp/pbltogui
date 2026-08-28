"""Cancel — w_modeltranhelp.

Generated from the PowerBuilder window ``w_modeltranhelp.srw`` by
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
    name='w_modeltranhelp',
    title='Cancel',
    width=2514,
    height=1684,
    controls=[],
    tables=[],
    source_path='w_modeltranhelp.srw',
    report={'dataobject': 'd_modeltranhelp', 'sql': 'SELECT modelm.tdate AS modelm_tdate, modelm.pname AS modelm_pname, modelm.icode AS modelm_icode, modelm.bcode AS modelm_bcode, modelm.qty AS modelm_qty, modelm.weight AS modelm_weight, modelm.stwgt AS modelm_stwgt, modelm.ir AS modelm_ir, modelm.pend AS modelm_pend, modelm.note AS modelm_note, modelm.smcode AS modelm_smcode, modelm.slno AS modelm_slno, modelm.gr AS modelm_gr, (select items.name from items where items.code = modelm.icode) as itemname FROM modelm', 'args': [], 'arg_types': {}, 'tables': ['modelm'], 'columns': [{'name': 'itemname', 'label': 'itemname', 'type': 'char'}, {'name': 'tdate', 'label': 'tdate', 'type': 'date'}, {'name': 'pname', 'label': 'pname', 'type': 'char'}, {'name': 'icode', 'label': 'icode', 'type': 'char'}, {'name': 'bcode', 'label': 'bcode', 'type': 'decimal'}, {'name': 'qty', 'label': 'qty', 'type': 'long'}, {'name': 'weight', 'label': 'weight', 'type': 'decimal'}, {'name': 'stwgt', 'label': 'stwgt', 'type': 'decimal'}, {'name': 'ir', 'label': 'ir', 'type': 'char'}, {'name': 'pend', 'label': 'pend', 'type': 'char'}, {'name': 'note', 'label': 'note', 'type': 'char'}, {'name': 'smcode', 'label': 'smcode', 'type': 'char'}, {'name': 'slno', 'label': 'slno', 'type': 'decimal'}, {'name': 'gr', 'label': 'gr', 'type': 'char'}]},
)


class CancelForm(GeneratedForm):
    """Cancel"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('datawindow', 'dw_1', 0, 0, 2501, 1440, dataobject='d_modeltranhelp', taborder=10)
        self.add('statictext', 'st_search', 18, 1356, 375, 76)
        self.add('commandbutton', 'cb_ok', 1015, 1460, 247, 92, text='OK', taborder=20)
        self.add('commandbutton', 'cb_cancel', 1280, 1460, 247, 92, text='Cancel', taborder=30)
        self.add('checkbox', 'cbx_pend', 55, 1464, 475, 80, text='Pending Only')
