"""Summary — w_staffsummary.

Generated from the PowerBuilder window ``w_staffsummary.srw`` by
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
    name='w_staffsummary',
    title='Summary',
    width=3648,
    height=2360,
    controls=[],
    tables=['clients'],
    source_path='w_staffsummary.srw',
    report={'dataobject': 'd_staffsummary2', 'sql': "SELECT clients.name AS clients_name, accountm.accode AS accountm_accode, clients.addr1 AS clients_addr1, clients.addr2 AS clients_addr2, clients.addr3 AS clients_addr3, accountm.opbal AS accountm_opbal, accountm.opbalb AS accountm_opbalb, accountm.actype2 AS accountm_actype2, clients.code AS clients_code, clients.removed AS clients_removed, (select sum(daybook.amount) from daybook where accountm.accode = daybook.accode and daybook.amount > 0 and daybook.control <= :rlevel and daybook.tdate <= :rdate) as tcreditamt, (select sum(abs(daybook.amount)) from daybook where accountm.accode = daybook.accode and daybook.amount < 0 and daybook.control <= :rlevel and daybook.tdate <= :rdate) as tdebitamt, (1) as sel FROM accountm, clients WHERE accountm.accode = clients.code AND accountm.actype2 = 'F' AND accountm.control <= :rlevel ORDER BY accountm.actype2 ASC, clients.name ASC", 'computes': [{'name': 'address', 'expression': 'clients_name + \'  \' +if(trim(  clients_addr1 ) = ~"~",~"~",trim(  clients_addr1 )+~",~") + if(trim(  clients_addr2 ) = ~"~",~"~",trim(  clients_addr2 )+~",~") + if(trim(   clients_addr3 ) = ~"~",~"~",trim(   clients_addr3 )+~",~")  ', 'format': '[general]', 'label': 'address', 'band': 'detail'}, {'name': 'tbal', 'expression': ' abs(balance)', 'format': '########0.00', 'label': 'tbal', 'band': 'detail'}, {'name': 'balance', 'expression': '(if(rlevel = 1 , accountm_opbal, accountm_opbalb) - if(isnull(ctdebitamt),0, ctdebitamt)  +  if(isnull(ctcreditamt),0, ctcreditamt) )', 'format': '[general]', 'label': 'balance', 'band': 'detail'}, {'name': 'compute_3', 'expression': 'abs( sum(balance  for all) )', 'format': '#########0.00', 'label': 'compute_3', 'band': 'summary'}], 'args': ['rlevel', 'rdate'], 'arg_types': {'rlevel': 'number', 'rdate': 'date'}, 'tables': ['accountm', 'clients'], 'columns': [{'name': 'clients_name', 'label': 'clients_name', 'type': 'char'}, {'name': 'accountm_accode', 'label': 'accountm_accode', 'type': 'char'}, {'name': 'clients_addr1', 'label': 'clients_addr1', 'type': 'char'}, {'name': 'clients_addr2', 'label': 'clients_addr2', 'type': 'char'}, {'name': 'clients_addr3', 'label': 'clients_addr3', 'type': 'char'}, {'name': 'accountm_opbal', 'label': 'accountm_opbal', 'type': 'decimal'}, {'name': 'accountm_opbalb', 'label': 'accountm_opbalb', 'type': 'decimal'}, {'name': 'ctcreditamt', 'label': 'ctcreditamt', 'type': 'decimal'}, {'name': 'accountm_actype2', 'label': 'accountm_actype2', 'type': 'char'}, {'name': 'ctdebitamt', 'label': 'ctdebitamt', 'type': 'decimal'}, {'name': 'sel', 'label': 'sel', 'type': 'long'}, {'name': 'clients_code', 'label': 'clients_code', 'type': 'char'}, {'name': 'clients_removed', 'label': 'clients_removed', 'type': 'long'}]},
    opens=['w_acledgerpopup'],
)


class SummaryForm(GeneratedForm):
    """Summary"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date', 366, 0, 448, 92, taborder=10)
        self.add('editmask', 'em_date2', 1138, 0, 448, 92, taborder=20)
        self.add('dropdownlistbox', 'ddlb_type', 1861, 0, 603, 532, text='All', items=['All', 'Receivable Only', 'Payable Only', 'With Balance Only'], taborder=50)
        self.add('commandbutton', 'cb_show', 2510, 0, 261, 92, text='&Show', taborder=30)
        self.add('commandbutton', 'cb_3', 2825, 0, 265, 92, text='Save &As', taborder=30)
        self.add('commandbutton', 'cb_1', 3118, 0, 238, 92, text='&Print', taborder=70)
        self.add('commandbutton', 'cb_2', 3365, 0, 238, 92, text='E&xit', taborder=60)
        self.add('statictext', 'st_dt1', 0, 8, 347, 76, text='Upto Date :')
        self.add('statictext', 'st_1', 1646, 8, 197, 76, text='Type :')
        self.add('statictext', 'st_dt2', 841, 12, 288, 76, text='Date To :')
        self.add('datawindow', 'dw_1', 0, 96, 3621, 2120, dataobject='d_staffsummary2', taborder=40)
        self.add('commandbutton', 'cb_homemsg', 2519, 100, 571, 92, text='Send Home Msg', taborder=60)
        self.add('checkbox', 'cbx_dosprint', 3141, 104, 338, 76, text='Dos print')
        self.add('checkbox', 'cbx_form2', 1861, 112, 274, 68, text='Form 2')
        self.add('checkbox', 'cbx_noremoved', 1861, 180, 416, 68, text='No Removed')
