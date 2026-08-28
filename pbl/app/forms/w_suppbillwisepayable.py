"""Billwise Payable — w_suppbillwisepayable.

Generated from the PowerBuilder window ``w_suppbillwisepayable.srw`` by
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
    name='w_suppbillwisepayable',
    title='Billwise Payable',
    width=3639,
    height=2428,
    controls=[],
    tables=['purchasem', 'accountm', 'collection'],
    source_path='w_suppbillwisepayable.srw',
    grid={'control': 'dw_1', 'dataobject': 'd_suppbillwisepayble', 'table': 'clients', 'keys': ['code'], 'columns': [{'name': 'code', 'label': 'code', 'type': 'char'}, {'name': 'name', 'label': 'clients_name', 'type': 'char'}, {'name': 'addr1', 'label': 'clients_addr1', 'type': 'char'}, {'name': 'addr2', 'label': 'clients_addr2', 'type': 'char'}, {'name': 'ctype', 'label': 'ctype', 'type': 'char'}, {'name': 'telephone', 'label': 'telephone', 'type': 'char'}, {'name': 'minduedate', 'label': 'minduedate', 'type': 'date'}, {'name': 'maxduedate', 'label': 'maxduedate', 'type': 'date'}, {'name': 'cocode', 'label': 'cocode', 'type': 'char'}, {'name': 'duedate', 'label': 'duedate', 'type': 'date'}, {'name': 'optsalesamt', 'label': 'optsalesamt', 'type': 'decimal'}, {'name': 'optrcvdamt', 'label': 'optrcvdamt', 'type': 'decimal'}, {'name': 'optsalesrcvdafter', 'label': 'optsalesrcvdafter', 'type': 'decimal'}]},
    report={'dataobject': 'd_suppbillwisepayble', 'sql': 'SELECT clients.code AS clients_code, clients.name AS clients_name, clients.addr1 AS clients_addr1, clients.addr2 AS clients_addr2, clients.ctype AS clients_ctype, clients.telephone AS clients_telephone, clients.cocode AS clients_cocode, clients.duedate AS clients_duedate, (select min(purchasem.duedate) from purchasem where purchasem.suppcode = clients.code and purchasem.tdate <= :rdate and purchasem.control <= :rlevel and purchasem.bal > 0) as minduedate, (select max(purchasem.duedate) from purchasem where purchasem.suppcode = clients.code and purchasem.tdate <= :rdate and purchasem.control <= :rlevel and purchasem.bal > 0 ) as maxduedate, (select sum(purchasem.netamt) from purchasem where purchasem.suppcode = clients.code and purchasem.tdate <= :rdate and purchasem.control <= :rlevel ) as optsalesamt, (select sum(purchasem.pamt) from purchasem where purchasem.suppcode = clients.code and purchasem.tdate <= :rdate and purchasem.control <= :rlevel ) as optrcvdamt, (select sum(collection.tranamt + collection.discount) from collection,purchasem where collection.islno = purchasem.slno and purchasem.suppcode = clients.code and purchasem.tdate <= :rdate and collection.tdate <= :rdate3 and purchasem.control <= :rlevel ) as optsalesrcvdafter FROM clients ORDER BY clients.name ASC, clients.code ASC', 'args': ['rdate', 'rdate2', 'rlevel', 'rdate3'], 'arg_types': {'rdate': 'date', 'rdate2': 'date', 'rlevel': 'number', 'rdate3': 'date'}, 'tables': ['clients'], 'columns': [{'name': 'code', 'label': 'code', 'type': 'char'}, {'name': 'clients_name', 'label': 'clients_name', 'type': 'char'}, {'name': 'clients_addr1', 'label': 'clients_addr1', 'type': 'char'}, {'name': 'clients_addr2', 'label': 'clients_addr2', 'type': 'char'}, {'name': 'ctype', 'label': 'ctype', 'type': 'char'}, {'name': 'telephone', 'label': 'telephone', 'type': 'char'}, {'name': 'minduedate', 'label': 'minduedate', 'type': 'date'}, {'name': 'maxduedate', 'label': 'maxduedate', 'type': 'date'}, {'name': 'cocode', 'label': 'cocode', 'type': 'char'}, {'name': 'duedate', 'label': 'duedate', 'type': 'date'}, {'name': 'optsalesamt', 'label': 'optsalesamt', 'type': 'decimal'}, {'name': 'optrcvdamt', 'label': 'optrcvdamt', 'type': 'decimal'}, {'name': 'optsalesrcvdafter', 'label': 'optsalesrcvdafter', 'type': 'decimal'}]},
)


class BillwisePayableForm(GeneratedForm):
    """Billwise Payable"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 361, 0, 393, 88, taborder=10)
        self.add('editmask', 'em_date2', 1125, 0, 393, 88, taborder=20)
        self.add('datawindow', 'dw_co', 2053, 0, 398, 88, dataobject='d_cust', taborder=21)
        self.add('commandbutton', 'cb_show', 2542, 4, 270, 96, text='&Show', taborder=30)
        self.add('commandbutton', 'cb_3', 2821, 4, 256, 96, text='Save &As', taborder=80)
        self.add('commandbutton', 'cb_1', 3081, 4, 238, 96, text='&Print', taborder=100)
        self.add('commandbutton', 'cb_2', 3328, 4, 238, 96, text='E&xit', taborder=90)
        self.add('statictext', 'st_1', 82, 12, 265, 80, text='Upto :')
        self.add('statictext', 'st_2', 805, 12, 315, 76, text='Date  To :')
        self.add('checkbox', 'cbx_term', 1618, 12, 247, 76, text='Term')
        self.add('statictext', 'st_16', 1879, 16, 165, 76, text='C/o :')
        self.add('dropdownlistbox', 'ddlb_sort', 361, 104, 576, 708, text='Clients Name', items=['Clients Name', 'Clients Code', 'Net Bill Amt', 'Bill Balance', 'Total Balance', 'Bill Name', 'Duedate'], taborder=40)
        self.add('statictext', 'st_3', 73, 116, 274, 76, text='Sort On :')
        self.add('checkbox', 'cbx_expand', 1618, 116, 567, 76, text='Billwise Expand')
        self.add('checkbox', 'cbx_customers_only', 2235, 116, 576, 76, text='Customers Only')
        self.add('checkbox', 'cbx_withbal', 2871, 116, 645, 76, text='With Balance Only')
        self.add('datawindow', 'dw_1', 5, 208, 3607, 1980, dataobject='d_suppbillwisepayble', taborder=70)
        self.add('editmask', 'em_colndate', 2446, 216, 384, 92, taborder=60)
        self.add('statictext', 'st_5', 1938, 220, 494, 76, text='Collection Upto :')
        self.add('checkbox', 'cbx_withtran', 2875, 224, 613, 76, text='With Transactions')
        self.add('singlelineedit', 'sle_1', 279, 2196, 571, 92, taborder=50)
        self.add('statictext', 'st_4', 18, 2208, 251, 76, text='Search :')
