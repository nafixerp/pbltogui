"""Sales Check List — w_salechklist.

Generated from the PowerBuilder window ``w_salechklist.srw`` by
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
    name='w_salechklist',
    title='Sales Check List',
    width=3648,
    height=2204,
    controls=[],
    tables=['clients'],
    source_path='w_salechklist.srw',
    grid={'control': 'dw_salechklist', 'dataobject': 'd_schecklist', 'table': 'salesm', 'keys': ['slno'], 'columns': [{'name': 'slno', 'label': 'salesm_slno', 'type': 'decimal'}, {'name': 'billno', 'label': 'salesm_billno', 'type': 'char'}, {'name': 'custcode', 'label': 'salesm_custcode', 'type': 'char'}, {'name': 'custname', 'label': 'salesm_custname', 'type': 'char'}, {'name': 'billamt', 'label': 'salesm_billamt', 'type': 'decimal'}, {'name': 'eamt', 'label': 'salesm_eamt', 'type': 'decimal'}, {'name': 'staxamt', 'label': 'salesm_staxamt', 'type': 'decimal'}, {'name': 'discount', 'label': 'salesm_discount', 'type': 'decimal'}, {'name': 'ramt', 'label': 'salesm_ramt', 'type': 'decimal'}, {'name': 'sretamt', 'label': 'salesm_sretamt', 'type': 'decimal'}, {'name': 'duedate', 'label': 'salesm_duedate', 'type': 'date'}, {'name': 'grate', 'label': 'salesm_grate', 'type': 'decimal'}, {'name': 'c_smname', 'label': 'c_smname', 'type': 'char'}, {'name': 'tdate', 'label': 'salesm_tdate', 'type': 'date'}, {'name': 'ttime', 'label': 'ttime', 'type': 'time'}, {'name': 'smcode', 'label': 'smcode', 'type': 'char'}, {'name': 'round', 'label': 'round', 'type': 'decimal'}, {'name': 'advance', 'label': 'advance', 'type': 'decimal'}, {'name': 'astamt', 'label': 'astamt', 'type': 'decimal'}, {'name': 'addr', 'label': 'addr', 'type': 'char'}, {'name': 'note', 'label': 'note', 'type': 'char'}, {'name': 'pan', 'label': 'pan', 'type': 'char'}]},
    report={'dataobject': 'd_schecklist', 'sql': "SELECT salesm.slno AS salesm_slno, salesm.billno AS salesm_billno, salesm.custcode AS salesm_custcode, salesm.custname AS salesm_custname, salesm.billamt AS salesm_billamt, salesm.eamt AS salesm_eamt, salesm.staxamt AS salesm_staxamt, salesm.discount AS salesm_discount, salesm.ramt AS salesm_ramt, salesm.sretamt AS salesm_sretamt, salesm.duedate AS salesm_duedate, salesm.grate AS salesm_grate, salesm.tdate AS salesm_tdate, salesm.ttime AS salesm_ttime, salesm.smcode AS salesm_smcode, salesm.round AS salesm_round, salesm.advance AS salesm_advance, salesm.astamt AS salesm_astamt, salesm.addr AS salesm_addr, salesm.note AS salesm_note, salesm.pan AS salesm_pan, (select name from sman where sman.code = salesm.smcode) as c_smname FROM salesm WHERE salesm.tdate between :rdate1 and :rdate2 AND salesm.control <= :rlevel AND salesm.sr = 'S' ORDER BY salesm.tdate ASC, salesm.slno ASC", 'args': ['rdate1', 'rdate2', 'rlevel'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date', 'rlevel': 'number'}, 'tables': ['salesm'], 'columns': [{'name': 'salesm_slno', 'label': 'salesm_slno', 'type': 'decimal'}, {'name': 'salesm_billno', 'label': 'salesm_billno', 'type': 'char'}, {'name': 'salesm_custcode', 'label': 'salesm_custcode', 'type': 'char'}, {'name': 'salesm_custname', 'label': 'salesm_custname', 'type': 'char'}, {'name': 'salesm_billamt', 'label': 'salesm_billamt', 'type': 'decimal'}, {'name': 'salesm_eamt', 'label': 'salesm_eamt', 'type': 'decimal'}, {'name': 'salesm_staxamt', 'label': 'salesm_staxamt', 'type': 'decimal'}, {'name': 'salesm_discount', 'label': 'salesm_discount', 'type': 'decimal'}, {'name': 'salesm_ramt', 'label': 'salesm_ramt', 'type': 'decimal'}, {'name': 'salesm_sretamt', 'label': 'salesm_sretamt', 'type': 'decimal'}, {'name': 'salesm_duedate', 'label': 'salesm_duedate', 'type': 'date'}, {'name': 'salesm_grate', 'label': 'salesm_grate', 'type': 'decimal'}, {'name': 'c_smname', 'label': 'c_smname', 'type': 'char'}, {'name': 'salesm_tdate', 'label': 'salesm_tdate', 'type': 'date'}, {'name': 'ttime', 'label': 'ttime', 'type': 'time'}, {'name': 'smcode', 'label': 'smcode', 'type': 'char'}, {'name': 'round', 'label': 'round', 'type': 'decimal'}, {'name': 'advance', 'label': 'advance', 'type': 'decimal'}, {'name': 'astamt', 'label': 'astamt', 'type': 'decimal'}, {'name': 'addr', 'label': 'addr', 'type': 'char'}, {'name': 'note', 'label': 'note', 'type': 'char'}, {'name': 'pan', 'label': 'pan', 'type': 'char'}]},
)


class SalesCheckListForm(GeneratedForm):
    """Sales Check List"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 1207, 0, 425, 92, taborder=20)
        self.add('editmask', 'em_date2', 1947, 0, 425, 92, taborder=30)
        self.add('commandbutton', 'cb_show', 2437, 0, 274, 96, text='&Show', taborder=40)
        self.add('commandbutton', 'cb_1', 2779, 0, 270, 92, text='Save &As', taborder=90)
        self.add('commandbutton', 'cb_print', 3054, 0, 265, 92, text='&Print', taborder=80)
        self.add('commandbutton', 'cb_exit', 3319, 0, 265, 92, text='E&xit', taborder=70)
        self.add('datawindow', 'dw_custcode', 347, 4, 402, 88, dataobject='d_cust', taborder=10)
        self.add('statictext', 'st_3', 5, 8, 334, 76, text='Customer :')
        self.add('statictext', 'st_11', 1637, 12, 302, 72, text='Date To :')
        self.add('statictext', 'st_10', 841, 20, 361, 64, text='Date From :')
        self.add('datawindow', 'dw_smcode', 1947, 100, 672, 88, dataobject='d_smancode', taborder=60)
        self.add('singlelineedit', 'sle_billno', 347, 104, 407, 88, taborder=61)
        self.add('statictext', 'st_2', 0, 112, 343, 80, text='Bill No :')
        self.add('statictext', 'st_1', 1728, 112, 210, 76, text='SMan :')
        self.add('datawindow', 'dw_salechklist', 9, 204, 3611, 1996, dataobject='d_schecklist', taborder=50)
