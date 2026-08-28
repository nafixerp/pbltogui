"""Duedate Report — w_duedaterep.

Generated from the PowerBuilder window ``w_duedaterep.srw`` by
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
    name='w_duedaterep',
    title='Duedate Report',
    width=3630,
    height=2396,
    controls=[],
    tables=['accountm'],
    source_path='w_duedaterep.srw',
    report={'dataobject': 'd_duedaterep', 'sql': 'SELECT salesm.tdate AS salesm_tdate, salesm.billno AS salesm_billno, salesm.custname AS salesm_custname, salesm.billamt AS salesm_billamt, salesm.eamt AS salesm_eamt, salesm.staxamt AS salesm_staxamt, salesm.discount AS salesm_discount, salesm.ramt AS salesm_ramt, salesm.ramtafter AS salesm_ramtafter, salesm.sretamt AS salesm_sretamt, salesm.duedate AS salesm_duedate, salesm.status AS salesm_status, salesm.custcode AS salesm_custcode, salesm.cocode AS salesm_cocode, salesm.round AS salesm_round, salesm.netamt AS salesm_netamt, salesm.advance AS salesm_advance, (select clients.addr1 from clients where clients.code = salesm.custcode) as caddr1, (select clients.addr2 from clients where clients.code = salesm.custcode) as caddr2, (select sum(tranamt + discount) from collection where collection.islno = salesm.slno) as trcvdafter, (select clients.addr3 from clients where clients.code = salesm.custcode) as caddr3, (select clients.telephone from clients where clients.code = salesm.custcode) as cphone FROM salesm WHERE salesm.control <= :rlevel ORDER BY salesm.duedate ASC, salesm.custname ASC', 'args': ['rdate1', 'rdate2', 'rlevel'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date', 'rlevel': 'number'}, 'tables': ['salesm'], 'columns': [{'name': 'tdate', 'label': 'tdate', 'type': 'date'}, {'name': 'billno', 'label': 'billno', 'type': 'char'}, {'name': 'custname', 'label': 'custname', 'type': 'char'}, {'name': 'billamt', 'label': 'billamt', 'type': 'decimal'}, {'name': 'eamt', 'label': 'eamt', 'type': 'decimal'}, {'name': 'staxamt', 'label': 'staxamt', 'type': 'decimal'}, {'name': 'discount', 'label': 'discount', 'type': 'decimal'}, {'name': 'ramt', 'label': 'ramt', 'type': 'decimal'}, {'name': 'ramtafter', 'label': 'ramtafter', 'type': 'decimal'}, {'name': 'sretamt', 'label': 'sretamt', 'type': 'decimal'}, {'name': 'duedate', 'label': 'duedate', 'type': 'date'}, {'name': 'status', 'label': 'status', 'type': 'long'}, {'name': 'caddr1', 'label': 'caddr1', 'type': 'char'}, {'name': 'caddr2', 'label': 'caddr2', 'type': 'char'}, {'name': 'custcode', 'label': 'custcode', 'type': 'char'}, {'name': 'cocode', 'label': 'cocode', 'type': 'char'}, {'name': 'round', 'label': 'round', 'type': 'decimal'}, {'name': 'trcvdafter', 'label': 'trcvdafter', 'type': 'decimal'}, {'name': 'netamt', 'label': 'netamt', 'type': 'decimal'}, {'name': 'advance', 'label': 'advance', 'type': 'decimal'}, {'name': 'caddr3', 'label': 'caddr3', 'type': 'char'}, {'name': 'cphone', 'label': 'cphone', 'type': 'char'}]},
    opens=['w_cbachdhelp', 'w_clientshelp'],
)


class DuedateReportForm(GeneratedForm):
    """Duedate Report"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date2', 1385, 0, 425, 92, taborder=20)
        self.add('datawindow', 'dw_co', 2034, 0, 402, 88, dataobject='d_cust', taborder=30)
        self.add('commandbutton', 'cb_show', 2505, 0, 261, 100, text='&Show', taborder=60)
        self.add('commandbutton', 'cb_3', 2775, 0, 265, 100, text='Save &As', taborder=90)
        self.add('commandbutton', 'cb_1', 3063, 0, 261, 100, text='&Print', taborder=100)
        self.add('commandbutton', 'cb_2', 3333, 0, 261, 100, text='E&xit', taborder=80)
        self.add('editmask', 'em_date1', 503, 4, 430, 92, taborder=10)
        self.add('statictext', 'st_2', 969, 4, 407, 72, text='Due Date To :')
        self.add('statictext', 'st_16', 1861, 8, 165, 76, text='C/o :')
        self.add('statictext', 'st_1', 5, 12, 485, 64, text='Due Date From :')
        self.add('dropdownlistbox', 'ddlb_sort', 2505, 100, 667, 596, text='Duedate', items=['Duedate', 'Customer', 'Balance', 'Date'], taborder=50)
        self.add('datawindow', 'dw_accode', 498, 104, 430, 88, dataobject='d_accode', taborder=40)
        self.add('statictext', 'st_party', 69, 112, 416, 72, text='Client Code :')
        self.add('checkbox', 'cbx_all', 1038, 112, 485, 76, text='All Duedates')
        self.add('checkbox', 'cbx_withbal', 1559, 112, 663, 76, text='With Balance Only')
        self.add('statictext', 'st_3', 2299, 116, 192, 76, text='Sort :')
        self.add('datawindow', 'dw_duedaterep', 5, 200, 3593, 1980, dataobject='d_duedaterep', taborder=70)
