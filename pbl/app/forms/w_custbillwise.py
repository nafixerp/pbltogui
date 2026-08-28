"""Billwise Details — w_custbillwise.

Generated from the PowerBuilder window ``w_custbillwise.srw`` by
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
    name='w_custbillwise',
    title='Billwise Details',
    width=3657,
    height=2252,
    controls=[],
    tables=['salesm', 'accountm', 'collection'],
    source_path='w_custbillwise.srw',
    grid={'control': 'dw_acsummary', 'dataobject': 'd_custbillwise', 'table': 'salesm', 'keys': ['slno'], 'columns': [{'name': 'tdate', 'label': 'tdate', 'type': 'date'}, {'name': 'billamt', 'label': 'billamt', 'type': 'decimal'}, {'name': 'staxamt', 'label': 'staxamt', 'type': 'decimal'}, {'name': 'discount', 'label': 'discount', 'type': 'decimal'}, {'name': 'eamt', 'label': 'eamt', 'type': 'decimal'}, {'name': 'sretamt', 'label': 'sretamt', 'type': 'decimal'}, {'name': 'ramt', 'label': 'ramt', 'type': 'decimal'}, {'name': 'ramtafter', 'label': 'ramtafter', 'type': 'decimal'}, {'name': 'duedate', 'label': 'duedate', 'type': 'date'}, {'name': 'billno', 'label': 'billno', 'type': 'char'}, {'name': 'slno', 'label': 'slno', 'type': 'decimal'}, {'name': 'custname', 'label': 'custname', 'type': 'char'}, {'name': 'round', 'label': 'round', 'type': 'decimal'}, {'name': 'netamt', 'label': 'netamt', 'type': 'decimal'}, {'name': 'rcvdaftamt', 'label': 'rcvdaftamt', 'type': 'decimal'}, {'name': 'discaftamt', 'label': 'discaftamt', 'type': 'decimal'}, {'name': 'balwgt', 'label': 'balwgt', 'type': 'decimal'}]},
    report={'dataobject': 'd_custbillwise', 'sql': 'SELECT salesm.tdate AS salesm_tdate, salesm.billamt AS salesm_billamt, salesm.staxamt AS salesm_staxamt, salesm.discount AS salesm_discount, salesm.eamt AS salesm_eamt, salesm.sretamt AS salesm_sretamt, salesm.ramt AS salesm_ramt, salesm.ramtafter AS salesm_ramtafter, salesm.duedate AS salesm_duedate, salesm.billno AS salesm_billno, salesm.slno AS salesm_slno, salesm.custname AS salesm_custname, salesm.round AS salesm_round, salesm.netamt AS salesm_netamt, salesm.balwgt AS salesm_balwgt, (select sum(collection.tranamt) from collection where collection.islno = salesm.slno) as rcvdaftamt, (select sum(collection.discount) from collection where collection.islno = salesm.slno) as discaftamt FROM salesm WHERE salesm.tdate between :rdate1 and :rdate2 AND salesm.custcode = :rcode AND salesm.control <= :rlevel ORDER BY salesm.tdate ASC, salesm.slno ASC', 'args': ['rdate1', 'rdate2', 'rlevel', 'rcode', 'racname', 'ropbal'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date', 'rlevel': 'number', 'rcode': 'string', 'racname': 'string', 'ropbal': 'decimal'}, 'tables': ['salesm'], 'columns': [{'name': 'tdate', 'label': 'tdate', 'type': 'date'}, {'name': 'billamt', 'label': 'billamt', 'type': 'decimal'}, {'name': 'staxamt', 'label': 'staxamt', 'type': 'decimal'}, {'name': 'discount', 'label': 'discount', 'type': 'decimal'}, {'name': 'eamt', 'label': 'eamt', 'type': 'decimal'}, {'name': 'sretamt', 'label': 'sretamt', 'type': 'decimal'}, {'name': 'ramt', 'label': 'ramt', 'type': 'decimal'}, {'name': 'ramtafter', 'label': 'ramtafter', 'type': 'decimal'}, {'name': 'duedate', 'label': 'duedate', 'type': 'date'}, {'name': 'billno', 'label': 'billno', 'type': 'char'}, {'name': 'slno', 'label': 'slno', 'type': 'decimal'}, {'name': 'custname', 'label': 'custname', 'type': 'char'}, {'name': 'round', 'label': 'round', 'type': 'decimal'}, {'name': 'netamt', 'label': 'netamt', 'type': 'decimal'}, {'name': 'rcvdaftamt', 'label': 'rcvdaftamt', 'type': 'decimal'}, {'name': 'discaftamt', 'label': 'discaftamt', 'type': 'decimal'}, {'name': 'balwgt', 'label': 'balwgt', 'type': 'decimal'}]},
)


class BillwiseDetailsForm(GeneratedForm):
    """Billwise Details"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 1221, 0, 430, 100, taborder=20)
        self.add('editmask', 'em_date2', 1979, 0, 425, 100, taborder=30)
        self.add('commandbutton', 'cb_show', 2459, 0, 261, 100, text='&Show', taborder=40)
        self.add('commandbutton', 'cb_saveas', 2793, 0, 283, 100, text='Save &As', taborder=80)
        self.add('commandbutton', 'cb_1', 3090, 0, 256, 100, text='&Print', taborder=100)
        self.add('commandbutton', 'cb_2', 3346, 0, 256, 100, text='E&xit', taborder=90)
        self.add('datawindow', 'dw_accode', 338, 4, 402, 88, dataobject='d_cust', taborder=10)
        self.add('statictext', 'st_3', 9, 8, 320, 72, text='Customer :')
        self.add('statictext', 'st_1', 841, 16, 366, 64, text='Date From :')
        self.add('statictext', 'st_2', 1669, 16, 302, 72, text='Date To :')
        self.add('datawindow', 'dw_acsummary', 0, 108, 3598, 2036, dataobject='d_custbillwise', taborder=50)
        self.add('commandbutton', 'cb_3', 3173, 112, 247, 96, text='Filter', taborder=70)
        self.add('singlelineedit', 'sle_filter', 2560, 120, 594, 88, taborder=60)
        self.add('statictext', 'st_4', 2203, 132, 347, 76, text='Cust Name :')
        self.add('checkbox', 'cbx_withbal', 2560, 216, 581, 76, text='With Balance Only')
