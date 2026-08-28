"""Bill Collection Details — w_custcollectionrep.

Generated from the PowerBuilder window ``w_custcollectionrep.srw`` by
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
    name='w_custcollectionrep',
    title='Bill Collection Details',
    width=3639,
    height=2272,
    controls=[],
    tables=['collection', 'salesm', 'daybook', 'clients'],
    source_path='w_custcollectionrep.srw',
    report={'dataobject': 'd_custcollectionrep', 'sql': 'SELECT salesm.tdate AS salesm_tdate, salesm.billamt AS salesm_billamt, salesm.staxamt AS salesm_staxamt, salesm.discount AS salesm_discount, salesm.eamt AS salesm_eamt, salesm.sretamt AS salesm_sretamt, salesm.ramt AS salesm_ramt, salesm.ramtafter AS salesm_ramtafter, salesm.duedate AS salesm_duedate, salesm.billno AS salesm_billno, salesm.slno AS salesm_slno, collection.tdate AS collection_tdate, collection.billno AS collection_billno, collection.tranamt AS collection_tranamt, collection.discount AS collection_discount, collection.duedate AS collection_duedate, salesm.custname AS salesm_custname, salesm.round AS salesm_round, salesm.netamt AS salesm_netamt, collection.slno AS collection_slno, salesm.grate AS salesm_grate, collection.grate2 AS collection_grate2, collection.grate AS collection_grate, (select daybookpart.vchno from daybookpart where daybookpart.slno = collection.slno) as vchno FROM salesm, collection WHERE salesm.slno = collection.islno AND salesm.tdate between :rdate1 and :rdate2 AND salesm.custcode = :rcode AND salesm.control <= :rlevel ORDER BY salesm.tdate ASC, salesm.slno ASC, salesm.billno ASC', 'computes': [{'name': 'compute_7', 'expression': "'('+string( collection_grate2 ,'######0.00')+')'", 'format': '[GENERAL]', 'label': 'compute_7', 'band': 'detail'}, {'name': 'tot', 'expression': 'balance - cumulativeSum( (collection_tranamt  -  collection_discount ) for group 1) +  (collection_tranamt  -  collection_discount ) ', 'format': '######0.00', 'label': 'tot', 'band': 'detail'}, {'name': 'netbal', 'expression': 'tot -  collection_discount  -  collection_tranamt ', 'format': '######0.00', 'label': 'netbal', 'band': 'detail'}, {'name': 'wgt2', 'expression': ' collection_tranamt  /    collection_grate', 'format': '######0.000', 'label': 'wgt2', 'band': 'detail'}], 'args': ['rdate1', 'rdate2', 'rlevel', 'rcode', 'racname'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date', 'rlevel': 'number', 'rcode': 'string', 'racname': 'string'}, 'tables': ['salesm', 'collection'], 'columns': [{'name': 'tdate', 'label': 'tdate', 'type': 'date'}, {'name': 'billamt', 'label': 'billamt', 'type': 'decimal'}, {'name': 'staxamt', 'label': 'staxamt', 'type': 'decimal'}, {'name': 'discount', 'label': 'discount', 'type': 'decimal'}, {'name': 'eamt', 'label': 'eamt', 'type': 'decimal'}, {'name': 'sretamt', 'label': 'sretamt', 'type': 'decimal'}, {'name': 'ramt', 'label': 'ramt', 'type': 'decimal'}, {'name': 'ramtafter', 'label': 'ramtafter', 'type': 'decimal'}, {'name': 'duedate', 'label': 'duedate', 'type': 'date'}, {'name': 'billno', 'label': 'billno', 'type': 'char'}, {'name': 'slno', 'label': 'slno', 'type': 'decimal'}, {'name': 'collection_tdate', 'label': 'collection_tdate', 'type': 'date'}, {'name': 'collection_billno', 'label': 'collection_billno', 'type': 'char'}, {'name': 'collection_tranamt', 'label': 'collection_tranamt', 'type': 'decimal'}, {'name': 'collection_discount', 'label': 'collection_discount', 'type': 'decimal'}, {'name': 'collection_duedate', 'label': 'collection_duedate', 'type': 'date'}, {'name': 'salesm_custname', 'label': 'salesm_custname', 'type': 'char'}, {'name': 'salesm_round', 'label': 'salesm_round', 'type': 'decimal'}, {'name': 'salesm_netamt', 'label': 'salesm_netamt', 'type': 'decimal'}, {'name': 'collection_slno', 'label': 'collection_slno', 'type': 'decimal'}, {'name': 'cvchno', 'label': 'cvchno', 'type': 'char'}, {'name': 'salesm_grate', 'label': 'salesm_grate', 'type': 'decimal'}, {'name': 'collection_grate2', 'label': 'collection_grate2', 'type': 'decimal'}, {'name': 'collection_grate', 'label': 'collection_grate', 'type': 'decimal'}]},
    opens=['w_clientshelp'],
)


class BillCollectionDetailsForm(GeneratedForm):
    """Bill Collection Details"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date2', 1915, 0, 389, 84, taborder=30)
        self.add('commandbutton', 'cb_3', 2318, 0, 261, 96, text='&Show', taborder=40)
        self.add('commandbutton', 'cb_4', 2766, 0, 283, 96, text='&Save As', taborder=60)
        self.add('commandbutton', 'cb_1', 3072, 0, 256, 96, text='&Print', taborder=100)
        self.add('commandbutton', 'cb_2', 3342, 0, 256, 96, text='E&xit', taborder=90)
        self.add('editmask', 'em_date1', 1198, 4, 389, 84, taborder=20)
        self.add('statictext', 'st_3', 1632, 4, 274, 76, text='Date To :')
        self.add('datawindow', 'dw_accode', 347, 8, 430, 88, dataobject='d_accode', taborder=10)
        self.add('statictext', 'st_2', 837, 12, 352, 76, text='Date From :')
        self.add('statictext', 'st_1', 14, 16, 325, 76, text='Customer :')
        self.add('checkbox', 'cbx_all', 1193, 96, 325, 76, text='&All Bills')
        self.add('singlelineedit', 'sle_filter', 1733, 96, 567, 80, taborder=80)
        self.add('commandbutton', 'cb_del', 2770, 96, 283, 84, text='Delete', taborder=61)
        self.add('statictext', 'st_4', 1518, 100, 206, 76, text='Name :')
        self.add('commandbutton', 'cb_5', 2318, 100, 256, 80, text='Filter', taborder=70)
        self.add('checkbox', 'cbx_withbal', 338, 104, 581, 76, text='With Balance Only')
        self.add('datawindow', 'dw_acsummary', 0, 180, 3607, 1972, dataobject='d_custcollectionrep', taborder=50)
