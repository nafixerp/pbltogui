"""Sales Book — w_oitbook.

Generated from the PowerBuilder window ``w_oitbook.srw`` by
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
    name='w_oitbook',
    title='Sales Book',
    width=3680,
    height=2256,
    controls=[],
    tables=[],
    source_path='w_oitbook.srw',
    grid={'control': 'dw_saleregister', 'dataobject': 'd_oitsbook', 'table': 'oitemtranm', 'keys': ['docno'], 'columns': [{'name': 'tdate', 'label': 'tdate', 'type': 'date'}, {'name': 'docno', 'label': 'docno', 'type': 'char'}, {'name': 'pname', 'label': 'pname', 'type': 'char'}, {'name': 'billamt', 'label': 'billamt', 'type': 'decimal'}, {'name': 'addamt', 'label': 'addamt', 'type': 'decimal'}, {'name': 'lessamt', 'label': 'lessamt', 'type': 'decimal'}, {'name': 'ramt', 'label': 'ramt', 'type': 'decimal'}, {'name': 'sp', 'label': 'sp', 'type': 'char'}, {'name': 'slno', 'label': 'slno', 'type': 'decimal'}]},
    report={'dataobject': 'd_oitsbook', 'sql': 'SELECT oitemtranm.tdate AS oitemtranm_tdate, oitemtranm.docno AS oitemtranm_docno, oitemtranm.pname AS oitemtranm_pname, oitemtranm.billamt AS oitemtranm_billamt, oitemtranm.addamt AS oitemtranm_addamt, oitemtranm.lessamt AS oitemtranm_lessamt, oitemtranm.ramt AS oitemtranm_ramt, oitemtranm.sp AS oitemtranm_sp, oitemtranm.slno AS oitemtranm_slno FROM oitemtranm ORDER BY oitemtranm.tdate ASC, oitemtranm.docno ASC', 'args': ['rdate1', 'rdate2', 'rlevel'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date', 'rlevel': 'number'}, 'tables': ['oitemtranm'], 'columns': [{'name': 'tdate', 'label': 'tdate', 'type': 'date'}, {'name': 'docno', 'label': 'docno', 'type': 'char'}, {'name': 'pname', 'label': 'pname', 'type': 'char'}, {'name': 'billamt', 'label': 'billamt', 'type': 'decimal'}, {'name': 'addamt', 'label': 'addamt', 'type': 'decimal'}, {'name': 'lessamt', 'label': 'lessamt', 'type': 'decimal'}, {'name': 'ramt', 'label': 'ramt', 'type': 'decimal'}, {'name': 'sp', 'label': 'sp', 'type': 'char'}, {'name': 'slno', 'label': 'slno', 'type': 'decimal'}]},
)


class SalesBookForm(GeneratedForm):
    """Sales Book"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 197, 0, 425, 92, taborder=10)
        self.add('editmask', 'em_date2', 823, 0, 425, 92, taborder=20)
        self.add('dropdownlistbox', 'ddlb_reptype', 1385, 0, 672, 404, text='Sales', items=['Sales', 'Purchase'], taborder=41)
        self.add('commandbutton', 'cb_show', 2139, 0, 293, 96, text='&Show', taborder=30)
        self.add('commandbutton', 'cb_sort', 2469, 0, 247, 92, text='So&rt', taborder=40)
        self.add('commandbutton', 'cb_1', 2747, 0, 270, 92, text='Save &As', taborder=80)
        self.add('commandbutton', 'cb_print', 3022, 0, 233, 92, text='&Print', taborder=60)
        self.add('commandbutton', 'cb_exit', 3259, 0, 233, 92, text='E&xit', taborder=70)
        self.add('statictext', 'st_10', 0, 8, 197, 64, text='From :')
        self.add('statictext', 'st_11', 686, 12, 128, 72, text='To :')
        self.add('datawindow', 'dw_saleregister', 0, 96, 3625, 2032, dataobject='d_oitsbook', taborder=50)
