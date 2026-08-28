"""Sales Register — w_oitregister.

Generated from the PowerBuilder window ``w_oitregister.srw`` by
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
    name='w_oitregister',
    title='Sales Register',
    width=3680,
    height=2256,
    controls=[],
    tables=[],
    source_path='w_oitregister.srw',
    report={'dataobject': 'd_oitsreg', 'sql': 'SELECT oitemtranm.tdate AS oitemtranm_tdate, oitemtranm.docno AS oitemtranm_docno, oitemtranm.pname AS oitemtranm_pname, oitemtranm.billamt AS oitemtranm_billamt, oitemtranm.addamt AS oitemtranm_addamt, oitemtranm.lessamt AS oitemtranm_lessamt, oitemtranm.ramt AS oitemtranm_ramt, oitemtranm.sp AS oitemtranm_sp, oitemtranm.slno AS oitemtranm_slno, oitemtrand.code AS oitemtrand_code, oitemtrand.name AS oitemtrand_name, oitemtrand.rate AS oitemtrand_rate, oitemtrand.amount AS oitemtrand_amount, oitemtrand.qty AS oitemtrand_qty, oitemtranm.pcode AS oitemtranm_pcode FROM oitemtranm, oitemtrand WHERE oitemtranm.slno = oitemtrand.slno ORDER BY oitemtranm.tdate ASC, oitemtranm.docno ASC, oitemtranm.slno ASC', 'args': ['rdate1', 'rdate2', 'rlevel'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date', 'rlevel': 'number'}, 'tables': ['oitemtranm', 'oitemtrand'], 'columns': [{'name': 'tdate', 'label': 'tdate', 'type': 'date'}, {'name': 'docno', 'label': 'docno', 'type': 'char'}, {'name': 'pname', 'label': 'pname', 'type': 'char'}, {'name': 'billamt', 'label': 'billamt', 'type': 'decimal'}, {'name': 'addamt', 'label': 'addamt', 'type': 'decimal'}, {'name': 'lessamt', 'label': 'lessamt', 'type': 'decimal'}, {'name': 'ramt', 'label': 'ramt', 'type': 'decimal'}, {'name': 'sp', 'label': 'sp', 'type': 'char'}, {'name': 'slno', 'label': 'slno', 'type': 'decimal'}, {'name': 'oitemtrand_code', 'label': 'oitemtrand_code', 'type': 'char'}, {'name': 'oitemtrand_name', 'label': 'oitemtrand_name', 'type': 'char'}, {'name': 'oitemtrand_rate', 'label': 'oitemtrand_rate', 'type': 'decimal'}, {'name': 'oitemtrand_amount', 'label': 'oitemtrand_amount', 'type': 'decimal'}, {'name': 'oitemtrand_qty', 'label': 'oitemtrand_qty', 'type': 'decimal'}, {'name': 'oitemtranm_pcode', 'label': 'oitemtranm_pcode', 'type': 'char'}]},
)


class SalesRegisterForm(GeneratedForm):
    """Sales Register"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 233, 0, 425, 92, taborder=10)
        self.add('editmask', 'em_date2', 1024, 0, 425, 92, taborder=20)
        self.add('dropdownlistbox', 'ddlb_reptype', 1550, 0, 599, 404, text='Sales', items=['Sales', 'Purchase'], taborder=50)
        self.add('commandbutton', 'cb_show', 2153, 0, 293, 96, text='&Show', taborder=60)
        self.add('commandbutton', 'cb_sort', 2469, 0, 247, 92, text='So&rt', taborder=70)
        self.add('commandbutton', 'cb_1', 2747, 0, 270, 92, text='Save &As', taborder=110)
        self.add('commandbutton', 'cb_print', 3022, 0, 233, 92, text='&Print', taborder=90)
        self.add('commandbutton', 'cb_exit', 3259, 0, 233, 92, text='E&xit', taborder=100)
        self.add('statictext', 'st_10', 0, 12, 224, 64, text='From :')
        self.add('statictext', 'st_11', 882, 12, 133, 72, text='To :')
        self.add('datawindow', 'dw_party', 233, 96, 402, 88, dataobject='d_cust', taborder=30)
        self.add('statictext', 'st_2', 837, 100, 178, 72, text='Item :')
        self.add('singlelineedit', 'sle_item', 1029, 100, 421, 88, limit=30, taborder=40)
        self.add('commandbutton', 'cb_hlp', 1458, 104, 165, 80, text='Help')
        self.add('statictext', 'st_1', 0, 108, 224, 64, text='Party :')
        self.add('datawindow', 'dw_saleregister', 0, 192, 3625, 1936, dataobject='d_oitsreg', taborder=80)
