"""A/c Receivable — w_acrcvblesummary.

Generated from the PowerBuilder window ``w_acrcvblesummary.srw`` by
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
    name='w_acrcvblesummary',
    title='A/c Receivable',
    width=3680,
    height=2324,
    controls=[],
    tables=['accountm', 'clients', 'date', 'salesm'],
    source_path='w_acrcvblesummary.srw',
    report={'dataobject': 'd_acrcvblesummary2', 'sql': 'SELECT accountm.accode AS accountm_accode, clients.name AS clients_name, clients.addr1 AS clients_addr1, clients.addr2 AS clients_addr2, clients.addr3 AS clients_addr3, clients.city AS clients_city, accountm.opbal AS accountm_opbal, accountm.opbalb AS accountm_opbalb, accountm.actype2 AS accountm_actype2, clients.telephone AS clients_telephone, clients.cocode AS clients_cocode, clients.grp AS clients_grp, clients.duedate AS clients_duedate, clients.route AS clients_route, clients.billdate AS clients_billdate, clients.mobile AS clients_mobile, clients.opweight AS clients_opweight, clients.carea AS clients_carea, (select max(salesm.duedate) from salesm where salesm.custcode = clients.code) as maxduedate, 0 as sel, (select sum(daybook.amount) from daybook where accountm.accode = daybook.accode and daybook.tdate <= :rdate and daybook.control <= :rlevel ) as ttranamt, (select max(daybook.tdate) from daybook where daybook.accode = clients.code and daybook.amount > 0) as lcdate, (select count(clients_kuridet.code) from clients_kuridet where clients_kuridet.code = clients.code) as kuri, (select max(purchasem.duedate) from purchasem where purchasem.suppcode = clients.code) as smaxduedate, (select am.name from accountm am where am.accode = clients.cocode) as coname, (select sum(daybookratewgt.wgt) from daybookratewgt where daybookratewgt.code = clients.code and daybookratewgt.tdate <= :rdate and daybookratewgt.control <= :rlevel ) as ttranwgt, (select max(salesm.duedate) from salesm where salesm.custcode = clients.code and salesm.duedate < clients.duedate) as maxduedate2, (select max(purchasem.duedate) from purchasem where purchasem.suppcode = clients.code and purchasem.duedate < clients.duedate) as smaxduedate2 FROM accountm, clients WHERE accountm.accode = clients.code AND accountm.actype2 = ifnull(:rCs,accountm.actype2,:rCs) AND accountm.control <= :rlevel ORDER BY accountm.actype2 ASC, clients.name ASC', 'computes': [{'name': 'address', 'expression': 'trim(clients_name)+\', \' + if(clients_telephone <> \'\', \' Ph : \'+ trim( clients_telephone )+\', \', \'\') +  if(clients_mobile <> \'\', \'Mob : \'+trim(  clients_mobile)+\', \',\'\' ) + if(trim( clients_addr1 ) = ~"~",~"~",trim( clients_addr1 )+~",~") + if(trim( clients_addr2 ) = ~"~",~"~",trim( clients_addr2 )+~",~") + if(trim(  clients_addr3 ) = ~"~",~"~",trim(  clients_addr3 )+~",~") +  trim(  clients_city ) + if(trim(  coname ) = ~"~" or isnull(coname) ,~"~",\' C/o \'+trim(  coname ))', 'format': '[general]', 'label': 'address', 'band': 'detail'}, {'name': 'cduedate', 'expression': "if(isnull(if(rCs = 'C',cmaxduedate,smaxduedate)),if(year(clients_duedate) > 1940,clients_duedate,if(rCs = 'C',cmaxduedate,smaxduedate)), if(clients_duedate > if(rCs = 'C',cmaxduedate,smaxduedate) , clients_duedate, if(rCs = 'C',cmaxduedate,smaxduedate)))", 'format': 'dd/mm/yy', 'label': 'cduedate', 'band': 'detail'}, {'name': 'tbal', 'expression': ' abs( netbal )', 'format': '#######0.00', 'label': 'tbal', 'band': 'detail'}, {'name': 'netbal', 'expression': '(if(rlevel = 1 , accountm_opbal, accountm_opbalb) + if(isnull(cttranamt),0,cttranamt) )', 'format': '#######0.00', 'label': 'netbal', 'band': 'detail'}, {'name': 'toget', 'expression': 'if(netbal < 0,abs(netbal),0)', 'format': '#######0.00', 'label': 'toget', 'band': 'detail'}, {'name': 'wgtbal', 'expression': '-( clients_opweight + if(isnull( ttranwgt ),0,ttranwgt) )', 'format': '#######0.000', 'label': 'wgtbal', 'band': 'detail'}, {'name': 'togive', 'expression': 'if(netbal > 0,abs(netbal),0)', 'format': '#######0.00', 'label': 'togive', 'band': 'detail'}, {'name': 'compute_8', 'expression': 'count(accountm_accode for all)', 'format': '[general]', 'label': 'compute_8', 'band': 'summary'}, {'name': 'compute_4', 'expression': 'sum( toget for all)', 'format': '#######0.00', 'label': 'compute_4', 'band': 'summary'}, {'name': 'twgtbal', 'expression': 'sum(wgtbal for all)', 'format': '#######0.000', 'label': 'twgtbal', 'band': 'summary'}, {'name': 'cduedate2', 'expression': "if(rCs = 'C', maxduedate2 , smaxduedate2 )", 'format': 'dd/mm/yy', 'label': 'cduedate2', 'band': 'detail'}, {'name': 'compute_5', 'expression': 'sum( togive for all)', 'format': '#######0.00', 'label': 'compute_5', 'band': 'summary'}, {'name': 'compute_6', 'expression': 'abs(sum(netbal  for all))', 'format': '#######0.00', 'label': 'compute_6', 'band': 'summary'}], 'args': ['rdate', 'rlevel', 'rCs'], 'arg_types': {'rdate': 'date', 'rlevel': 'number', 'rCs': 'string'}, 'tables': ['accountm', 'clients'], 'columns': [{'name': 'accountm_accode', 'label': 'accountm_accode', 'type': 'char'}, {'name': 'clients_name', 'label': 'clients_name', 'type': 'char'}, {'name': 'clients_addr1', 'label': 'clients_addr1', 'type': 'char'}, {'name': 'clients_addr2', 'label': 'clients_addr2', 'type': 'char'}, {'name': 'clients_addr3', 'label': 'clients_addr3', 'type': 'char'}, {'name': 'clients_city', 'label': 'clients_city', 'type': 'char'}, {'name': 'accountm_opbal', 'label': 'accountm_opbal', 'type': 'decimal'}, {'name': 'accountm_opbalb', 'label': 'accountm_opbalb', 'type': 'decimal'}, {'name': 'accountm_actype2', 'label': 'accountm_actype2', 'type': 'char'}, {'name': 'clients_telephone', 'label': 'clients_telephone', 'type': 'char'}, {'name': 'clients_cocode', 'label': 'clients_cocode', 'type': 'char'}, {'name': 'clients_grp', 'label': 'clients_grp', 'type': 'char'}, {'name': 'cmaxduedate', 'label': 'cmaxduedate', 'type': 'date'}, {'name': 'clients_duedate', 'label': 'clients_duedate', 'type': 'date'}, {'name': 'accountm_sel', 'label': 'accountm_sel', 'type': 'long'}, {'name': 'cttranamt', 'label': 'cttranamt', 'type': 'decimal'}, {'name': 'clients_route', 'label': 'clients_route', 'type': 'char'}, {'name': 'clients_billdate', 'label': 'clients_billdate', 'type': 'date'}, {'name': 'lcdate', 'label': 'lcdate', 'type': 'date'}, {'name': 'clients_mobile', 'label': 'clients_mobile', 'type': 'char'}, {'name': 'kuri', 'label': 'kuri', 'type': 'long'}, {'name': 'smaxduedate', 'label': 'smaxduedate', 'type': 'date'}, {'name': 'coname', 'label': 'coname', 'type': 'char'}, {'name': 'ttranwgt', 'label': 'ttranwgt', 'type': 'decimal'}, {'name': 'clients_opweight', 'label': 'clients_opweight', 'type': 'decimal'}, {'name': 'clients_carea', 'label': 'clients_carea', 'type': 'char'}, {'name': 'maxduedate2', 'label': 'maxduedate2', 'type': 'date'}, {'name': 'smaxduedate2', 'label': 'smaxduedate2', 'type': 'date'}]},
    opens=['w_duedate_change', 'w_clientshelp', 'w_cbachdhelp', 'w_acledger'],
)


class ACReceivableForm(GeneratedForm):
    """A/c Receivable"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date', 261, 0, 393, 88, taborder=10)
        self.add('statictext', 'st_date2', 955, 0, 187, 76, text='To :')
        self.add('editmask', 'em_date2', 1161, 0, 393, 88, taborder=20)
        self.add('datawindow', 'dw_co', 1911, 0, 402, 88, dataobject='d_cust', taborder=50)
        self.add('commandbutton', 'cb_show', 2354, 0, 270, 92, text='&Show', taborder=30)
        self.add('commandbutton', 'cb_tell', 2633, 0, 247, 92, text='Tell', taborder=110)
        self.add('commandbutton', 'cb_3', 2889, 0, 256, 92, text='Save &As', taborder=120)
        self.add('commandbutton', 'cb_1', 3154, 0, 238, 92, text='Print', taborder=140)
        self.add('commandbutton', 'cb_2', 3406, 0, 238, 92, text='E&xit', taborder=130)
        self.add('statictext', 'st_date1', 0, 4, 251, 76, text='From :')
        self.add('statictext', 'st_16', 1728, 16, 165, 76, text='C/o :')
        self.add('dropdownlistbox', 'ddlb_type', 261, 92, 562, 592, text='Receivable Only', items=['All', 'Receivable Only', 'Payable Only', 'With Balance Only', 'With Term Transaction'], taborder=40)
        self.add('dropdownlistbox', 'ddlb_sort', 1161, 92, 480, 648, text='Clients Name', items=['Clients Name', 'Clients Code', 'Balance', 'Duedate', 'LBDate', 'LCDate'], taborder=100)
        self.add('datawindow', 'dw_grp', 1911, 96, 677, 88, dataobject='d_clientsgrp_code', taborder=90)
        self.add('checkbox', 'cbx_form2', 2889, 96, 270, 76, text='Form 2')
        self.add('checkbox', 'cbx_speed', 3328, 100, 343, 76, text='Speed Print')
        self.add('statictext', 'st_3', 887, 104, 256, 76, text='Sort On :')
        self.add('statictext', 'st_2', 1673, 104, 219, 76, text='Group :')
        self.add('checkbox', 'cbx_grp', 2592, 104, 91, 76)
        self.add('statictext', 'st_1', 0, 108, 247, 68, text='Type :')
        self.add('statictext', 'st_status', 2665, 108, 215, 80)
        self.add('checkbox', 'cbx_selonly', 2354, 184, 466, 52, text='Selected Only')
        self.add('checkbox', 'cbx_printcode', 2889, 184, 334, 52, text='Print Code')
        self.add('checkbox', 'cbx_printco', 3328, 184, 343, 52, text='Print C/o')
        self.add('editmask', 'em_minamt', 1911, 188, 402, 92, taborder=70)
        self.add('statictext', 'st_5', 0, 192, 247, 68, text='Route :')
        self.add('datawindow', 'dw_route', 261, 192, 791, 88, dataobject='d_clientsroute_code', taborder=101)
        self.add('checkbox', 'cbx_route', 1051, 196, 78, 76)
        self.add('commandbutton', 'cb_filter', 1161, 196, 197, 88, text='Filter', taborder=80)
        self.add('statictext', 'st_4', 1650, 200, 242, 84, text='Min Amt :')
        self.add('checkbox', 'cbx_duedate', 2354, 248, 507, 52, text='Based On Duedate')
        self.add('checkbox', 'cbx_printlines', 2889, 248, 366, 52, text='Print Lines')
        self.add('checkbox', 'cbx_condense', 3328, 248, 329, 52, text='Condense')
        self.add('editmask', 'em_maxamt', 1911, 284, 402, 92, taborder=111)
        self.add('datawindow', 'dw_area', 261, 288, 745, 88, dataobject='d_clientsarea_code', taborder=130)
        self.add('statictext', 'st_9', 0, 292, 247, 68, text='Area :')
        self.add('datawindow', 'dw_srch', 1358, 292, 279, 88, dataobject='d_srch', taborder=110)
        self.add('checkbox', 'cbx_area', 1010, 296, 78, 76)
        self.add('statictext', 'st_8', 1646, 300, 247, 84, text='Max Amt :')
        self.add('statictext', 'st_6', 1102, 308, 247, 68, text='In Name :')
        self.add('commandbutton', 'cb_toexcel', 2350, 308, 265, 92, text='To Excel', taborder=130)
        self.add('dropdownlistbox', 'ddlb_partytype', 2889, 308, 389, 820, text='Customers', items=['All', 'Customers', 'Suppliers', 'GoldSmith', 'Jewelery', 'Refiners', 'Staffs', 'Kuri/Scheme Party'], taborder=110)
        self.add('commandbutton', 'cb_duedate', 3310, 316, 347, 76, text='Change DDate', taborder=120)
        self.add('statictext', 'st_7', 2629, 324, 261, 68, text='Party type :')
        self.add('datawindow', 'dw_1', 0, 400, 3657, 1824, dataobject='d_acrcvblesummary2', taborder=60)
        self.add('checkbox', 'cbx_showwgt', 2889, 412, 443, 80, text='Show Wgt Bal')
