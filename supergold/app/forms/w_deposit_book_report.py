"""Deposit Book — w_deposit_book_report.

Generated from the PowerBuilder window ``w_deposit_book_report.srw`` by
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
    name='w_deposit_book_report',
    title='Deposit Book',
    width=3694,
    height=2184,
    controls=[],
    tables=['accountm', 'wgtrcptpmnt', 'clients'],
    source_path='w_deposit_book_report.srw',
    grid={'control': 'dw_1', 'dataobject': 'd_deposit_book_report', 'table': 'wgtrcptpmnt', 'keys': ['slno'], 'computes': [{'name': 'compute_2', 'expression': "trim( clients_addr1 )+','+trim( clients_addr2 )+','+trim( clients_addr3 )", 'format': '[general]', 'label': 'compute_2', 'band': 'detail'}, {'name': 'wgt', 'expression': "if(wgtrcptpmnt_ttype ='R', wgtrcptpmnt_netwgt , -wgtrcptpmnt_netwgt)", 'format': '######0.000', 'label': 'wgt', 'band': 'detail'}, {'name': 'compute_3', 'expression': 'count(wgtrcptpmnt_docno for all)', 'format': '[general]', 'label': 'compute_3', 'band': 'summary'}, {'name': 'compute_4', 'expression': 'sum( wgt for all)', 'format': '#######0.000', 'label': 'compute_4', 'band': 'summary'}, {'name': 'compute_6', 'expression': 'ropbal + sum( wgt for all)', 'format': '#######0.000', 'label': 'compute_6', 'band': 'summary'}], 'columns': [{'name': 'tdate', 'label': 'wgtrcptpmnt_tdate', 'type': 'date'}, {'name': 'docno', 'label': 'wgtrcptpmnt_docno', 'type': 'char'}, {'name': 'ttype', 'label': 'wgtrcptpmnt_ttype', 'type': 'char'}, {'name': 'weight', 'label': 'wgtrcptpmnt_weight', 'type': 'decimal'}, {'name': 'grate', 'label': 'wgtrcptpmnt_grate', 'type': 'decimal'}, {'name': 'note', 'label': 'wgtrcptpmnt_note', 'type': 'char'}, {'name': 'smcode', 'label': 'wgtrcptpmnt_smcode', 'type': 'char'}, {'name': 'icode', 'label': 'wgtrcptpmnt_icode', 'type': 'char'}, {'name': 'qty', 'label': 'wgtrcptpmnt_qty', 'type': 'long'}, {'name': 'stwgt', 'label': 'wgtrcptpmnt_stwgt', 'type': 'decimal'}, {'name': 'netwgt', 'label': 'wgtrcptpmnt_netwgt', 'type': 'decimal'}, {'name': 'slno', 'label': 'wgtrcptpmnt_slno', 'type': 'decimal'}, {'name': 'clients_addr1', 'label': 'clients_addr1', 'type': 'char'}, {'name': 'clients_name', 'label': 'Name', 'type': 'char'}, {'name': 'clients_addr2', 'label': 'clients_addr2', 'type': 'char'}, {'name': 'clients_addr3', 'label': 'clients_addr3', 'type': 'char'}, {'name': 'pcode', 'label': 'pcode', 'type': 'char'}, {'name': 'clients_cocode', 'label': 'clients_cocode', 'type': 'char'}, {'name': 'clients_code', 'label': 'clients_code', 'type': 'char'}]},
    report={'dataobject': 'd_deposit_book_report', 'sql': 'SELECT wgtrcptpmnt.tdate AS wgtrcptpmnt_tdate, wgtrcptpmnt.docno AS wgtrcptpmnt_docno, wgtrcptpmnt.ttype AS wgtrcptpmnt_ttype, wgtrcptpmnt.weight AS wgtrcptpmnt_weight, wgtrcptpmnt.grate AS wgtrcptpmnt_grate, wgtrcptpmnt.note AS wgtrcptpmnt_note, wgtrcptpmnt.smcode AS wgtrcptpmnt_smcode, wgtrcptpmnt.icode AS wgtrcptpmnt_icode, wgtrcptpmnt.qty AS wgtrcptpmnt_qty, wgtrcptpmnt.stwgt AS wgtrcptpmnt_stwgt, wgtrcptpmnt.netwgt AS wgtrcptpmnt_netwgt, wgtrcptpmnt.slno AS wgtrcptpmnt_slno, wgtrcptpmnt.pcode AS wgtrcptpmnt_pcode, (select clients.addr1 from clients where clients.code = wgtrcptpmnt.pcode) as clients_addr1, (select accountm.name from accountm where accountm.accode = wgtrcptpmnt.pcode) as clients_name, (select clients.addr2 from clients where clients.code = wgtrcptpmnt.pcode) as clients_addr2, (select clients.addr3 from clients where clients.code = wgtrcptpmnt.pcode) as clients_addr3, (select clients.cocode from clients where clients.code = wgtrcptpmnt.pcode) as clients_cocode, (pcode) as clients_code FROM wgtrcptpmnt ORDER BY wgtrcptpmnt.tdate ASC, wgtrcptpmnt.docno ASC', 'computes': [{'name': 'compute_2', 'expression': "trim( clients_addr1 )+','+trim( clients_addr2 )+','+trim( clients_addr3 )", 'format': '[general]', 'label': 'compute_2', 'band': 'detail'}, {'name': 'wgt', 'expression': "if(wgtrcptpmnt_ttype ='R', wgtrcptpmnt_netwgt , -wgtrcptpmnt_netwgt)", 'format': '######0.000', 'label': 'wgt', 'band': 'detail'}, {'name': 'compute_3', 'expression': 'count(wgtrcptpmnt_docno for all)', 'format': '[general]', 'label': 'compute_3', 'band': 'summary'}, {'name': 'compute_4', 'expression': 'sum( wgt for all)', 'format': '#######0.000', 'label': 'compute_4', 'band': 'summary'}, {'name': 'compute_6', 'expression': 'ropbal + sum( wgt for all)', 'format': '#######0.000', 'label': 'compute_6', 'band': 'summary'}], 'args': ['rdate1', 'rdate2', 'rlevel', 'ropbal'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date', 'rlevel': 'number', 'ropbal': 'decimal'}, 'tables': ['wgtrcptpmnt'], 'columns': [{'name': 'wgtrcptpmnt_tdate', 'label': 'wgtrcptpmnt_tdate', 'type': 'date'}, {'name': 'wgtrcptpmnt_docno', 'label': 'wgtrcptpmnt_docno', 'type': 'char'}, {'name': 'wgtrcptpmnt_ttype', 'label': 'wgtrcptpmnt_ttype', 'type': 'char'}, {'name': 'wgtrcptpmnt_weight', 'label': 'wgtrcptpmnt_weight', 'type': 'decimal'}, {'name': 'wgtrcptpmnt_grate', 'label': 'wgtrcptpmnt_grate', 'type': 'decimal'}, {'name': 'wgtrcptpmnt_note', 'label': 'wgtrcptpmnt_note', 'type': 'char'}, {'name': 'wgtrcptpmnt_smcode', 'label': 'wgtrcptpmnt_smcode', 'type': 'char'}, {'name': 'wgtrcptpmnt_icode', 'label': 'wgtrcptpmnt_icode', 'type': 'char'}, {'name': 'wgtrcptpmnt_qty', 'label': 'wgtrcptpmnt_qty', 'type': 'long'}, {'name': 'wgtrcptpmnt_stwgt', 'label': 'wgtrcptpmnt_stwgt', 'type': 'decimal'}, {'name': 'wgtrcptpmnt_netwgt', 'label': 'wgtrcptpmnt_netwgt', 'type': 'decimal'}, {'name': 'wgtrcptpmnt_slno', 'label': 'wgtrcptpmnt_slno', 'type': 'decimal'}, {'name': 'clients_addr1', 'label': 'clients_addr1', 'type': 'char'}, {'name': 'clients_name', 'label': 'Name', 'type': 'char'}, {'name': 'clients_addr2', 'label': 'clients_addr2', 'type': 'char'}, {'name': 'clients_addr3', 'label': 'clients_addr3', 'type': 'char'}, {'name': 'pcode', 'label': 'pcode', 'type': 'char'}, {'name': 'clients_cocode', 'label': 'clients_cocode', 'type': 'char'}, {'name': 'clients_code', 'label': 'clients_code', 'type': 'char'}]},
    opens=['w_cbachdhelp', 'w_clientshelp'],
)


class DepositBookForm(GeneratedForm):
    """Deposit Book"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('datawindow', 'dw_accode', 1458, 0, 402, 88, dataobject='d_cust', taborder=30)
        self.add('dropdownlistbox', 'ddlb_type', 2190, 0, 526, 500, text='All', items=['Receipt Only', 'Payment Olny', 'Interest Only', 'All'], taborder=120)
        self.add('editmask', 'em_date1', 242, 4, 398, 92, taborder=10)
        self.add('editmask', 'em_date2', 795, 4, 393, 92, taborder=20)
        self.add('commandbutton', 'cb_show', 2734, 4, 256, 92, text='&Show', taborder=110)
        self.add('commandbutton', 'cb_print', 3113, 4, 256, 92, text='&Print', taborder=140)
        self.add('commandbutton', 'cb_exit', 3378, 4, 256, 92, text='E&xit', taborder=130)
        self.add('statictext', 'st_3', 1225, 8, 224, 72, text='Party :')
        self.add('statictext', 'st_4', 1952, 12, 229, 64, text='Type :')
        self.add('statictext', 'st_1', 14, 16, 219, 64, text='From :')
        self.add('statictext', 'st_2', 654, 16, 137, 72, text='To :')
        self.add('dropdownlistbox', 'ddlb_sorton', 1458, 96, 512, 500, text='Date', items=['Name', 'Code', 'Inst.Finish', 'Pending', 'Date'], taborder=100)
        self.add('datawindow', 'dw_co', 242, 100, 402, 88, dataobject='d_cust', taborder=40)
        self.add('statictext', 'st_6', 1184, 104, 265, 80, text='Sort On :')
        self.add('statictext', 'st_co', 69, 108, 165, 76, text='C/o :')
        self.add('checkbox', 'cbx_dosprint', 3177, 112, 270, 68, text='Speed')
        self.add('datawindow', 'dw_1', 0, 204, 3634, 1888, dataobject='d_deposit_book_report', taborder=120)
