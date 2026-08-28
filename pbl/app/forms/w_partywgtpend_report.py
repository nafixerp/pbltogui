"""Wgt Balance Summary — w_partywgtpend_report.

Generated from the PowerBuilder window ``w_partywgtpend_report.srw`` by
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
    name='w_partywgtpend_report',
    title='Wgt Balance Summary',
    width=3634,
    height=2252,
    controls=[],
    tables=['accountm'],
    source_path='w_partywgtpend_report.srw',
    grid={'control': 'dw_acsummary', 'dataobject': 'd_partywgtpend_report', 'table': 'clients', 'keys': ['code'], 'columns': [{'name': 'code', 'label': 'code', 'type': 'char'}, {'name': 'name', 'label': 'clients_name', 'type': 'char'}, {'name': 'addr1', 'label': 'clients_addr1', 'type': 'char'}, {'name': 'addr2', 'label': 'clients_addr2', 'type': 'char'}, {'name': 'ctype', 'label': 'ctype', 'type': 'char'}, {'name': 'telephone', 'label': 'telephone', 'type': 'char'}, {'name': 'cocode', 'label': 'cocode', 'type': 'char'}, {'name': 'duedate', 'label': 'duedate', 'type': 'date'}, {'name': 'opweight', 'label': 'opweight', 'type': 'decimal'}, {'name': 'twgtr', 'label': 'twgtr', 'type': 'decimal'}, {'name': 'twgtg', 'label': 'twgtg', 'type': 'decimal'}, {'name': 'opdepwgtbal', 'label': 'opdepwgtbal', 'type': 'decimal'}]},
    report={'dataobject': 'd_partywgtpend_report', 'sql': "SELECT clients.code AS clients_code, clients.name AS clients_name, clients.addr1 AS clients_addr1, clients.addr2 AS clients_addr2, clients.ctype AS clients_ctype, clients.telephone AS clients_telephone, clients.cocode AS clients_cocode, clients.duedate AS clients_duedate, clients.opweight AS clients_opweight, clients.opdepwgtbal AS clients_opdepwgtbal, (select sum(wgt.netwgt) from wgtrcptpmnt wgt where wgt.pcode = clients.code and wgt.tdate <= :rdate and wgt.ttype = 'R' and wgt.control <= :rlevel ) as twgtr, (select sum(wgt.netwgt) from wgtrcptpmnt wgt where wgt.pcode = clients.code and wgt.tdate <= :rdate and wgt.ttype = 'P' and wgt.control <= :rlevel ) as twgtg FROM clients ORDER BY clients.name ASC, clients.code ASC", 'args': ['rdate', 'rlevel'], 'arg_types': {'rdate': 'date', 'rlevel': 'number'}, 'tables': ['clients'], 'columns': [{'name': 'code', 'label': 'code', 'type': 'char'}, {'name': 'clients_name', 'label': 'clients_name', 'type': 'char'}, {'name': 'clients_addr1', 'label': 'clients_addr1', 'type': 'char'}, {'name': 'clients_addr2', 'label': 'clients_addr2', 'type': 'char'}, {'name': 'ctype', 'label': 'ctype', 'type': 'char'}, {'name': 'telephone', 'label': 'telephone', 'type': 'char'}, {'name': 'cocode', 'label': 'cocode', 'type': 'char'}, {'name': 'duedate', 'label': 'duedate', 'type': 'date'}, {'name': 'opweight', 'label': 'opweight', 'type': 'decimal'}, {'name': 'twgtr', 'label': 'twgtr', 'type': 'decimal'}, {'name': 'twgtg', 'label': 'twgtg', 'type': 'decimal'}, {'name': 'opdepwgtbal', 'label': 'opdepwgtbal', 'type': 'decimal'}]},
)


class WgtBalanceSummaryForm(GeneratedForm):
    """Wgt Balance Summary"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 224, 0, 430, 96, taborder=20)
        self.add('commandbutton', 'cb_3', 2299, 0, 192, 96, text='Filter', taborder=60)
        self.add('commandbutton', 'cb_show', 2514, 0, 261, 96, text='&Show', taborder=30)
        self.add('commandbutton', 'cb_saveas', 2784, 0, 283, 96, text='Save &As', taborder=70)
        self.add('commandbutton', 'cb_1', 3081, 0, 256, 96, text='&Print', taborder=90)
        self.add('commandbutton', 'cb_2', 3346, 0, 256, 96, text='E&xit', taborder=80)
        self.add('datawindow', 'dw_accode', 1019, 4, 402, 88, dataobject='d_cust', taborder=10)
        self.add('singlelineedit', 'sle_filter', 1806, 4, 466, 88, taborder=50)
        self.add('statictext', 'st_4', 1454, 8, 347, 76, text='Cust Name :')
        self.add('statictext', 'st_1', 0, 12, 210, 64, text='Upto :')
        self.add('statictext', 'st_3', 686, 12, 329, 72, text='Customer :')
        self.add('datawindow', 'dw_acsummary', 0, 100, 3607, 2048, dataobject='d_partywgtpend_report', taborder=40)
        self.add('checkbox', 'cbx_withbal', 2299, 112, 581, 64, text='With Balance Only')
        self.add('checkbox', 'cbx_genacc', 2930, 112, 558, 64, text='General Accounts')
