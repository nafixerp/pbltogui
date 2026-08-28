"""Visit Report — w_customer_visitreport.

Generated from the PowerBuilder window ``w_customer_visitreport.srw`` by
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
    name='w_customer_visitreport',
    title='Visit Report',
    width=3625,
    height=2332,
    controls=[],
    tables=[],
    source_path='w_customer_visitreport.srw',
    grid={'control': 'dw_suculist', 'dataobject': 'd_customer_visitreport', 'table': 'clients', 'keys': ['code'], 'computes': [{'name': 'compute_3', 'expression': "addr1 + if(addr2 <> '', ', '+  addr2,'') + if(addr3 <> '', ', '+  addr3,'') + if(city <> '', ', '+  city ,'')", 'format': '[GENERAL]', 'label': 'compute_3', 'band': 'detail'}], 'columns': [{'name': 'code', 'label': 'Code', 'type': 'char'}, {'name': 'name', 'label': 'Name', 'type': 'char'}, {'name': 'addr1', 'label': 'addr1', 'type': 'char'}, {'name': 'addr2', 'label': 'addr2', 'type': 'char'}, {'name': 'addr3', 'label': 'addr3', 'type': 'char'}, {'name': 'city', 'label': 'Mobile', 'type': 'char'}, {'name': 'telephone', 'label': 'Telephone', 'type': 'char'}, {'name': 'mobile', 'label': 'mobile', 'type': 'char'}, {'name': 'tvisit', 'label': 'tvisit', 'type': 'long'}, {'name': 'carea', 'label': 'carea', 'type': 'char'}]},
    report={'dataobject': 'd_customer_visitreport', 'sql': 'SELECT clients.code AS clients_code, clients.name AS clients_name, clients.addr1 AS clients_addr1, clients.addr2 AS clients_addr2, clients.addr3 AS clients_addr3, clients.city AS clients_city, clients.telephone AS clients_telephone, clients.mobile AS clients_mobile, clients.carea AS clients_carea, (select count(salesm.slno) from salesm where salesm.custcode = clients.code and salesm.tdate >= :rdate1 and salesm.tdate <= :rdate2) as tvisit FROM clients WHERE clients.ctype = :rmcs ORDER BY clients.name ASC', 'computes': [{'name': 'compute_3', 'expression': "addr1 + if(addr2 <> '', ', '+  addr2,'') + if(addr3 <> '', ', '+  addr3,'') + if(city <> '', ', '+  city ,'')", 'format': '[GENERAL]', 'label': 'compute_3', 'band': 'detail'}], 'args': ['rdate1', 'rdate2', 'rmcs', 'rgrp', 'rroute', 'rarea'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date', 'rmcs': 'string', 'rgrp': 'string', 'rroute': 'string', 'rarea': 'string'}, 'tables': ['clients'], 'columns': [{'name': 'code', 'label': 'Code', 'type': 'char'}, {'name': 'name', 'label': 'Name', 'type': 'char'}, {'name': 'addr1', 'label': 'addr1', 'type': 'char'}, {'name': 'addr2', 'label': 'addr2', 'type': 'char'}, {'name': 'addr3', 'label': 'addr3', 'type': 'char'}, {'name': 'city', 'label': 'Mobile', 'type': 'char'}, {'name': 'telephone', 'label': 'Telephone', 'type': 'char'}, {'name': 'mobile', 'label': 'mobile', 'type': 'char'}, {'name': 'tvisit', 'label': 'tvisit', 'type': 'long'}, {'name': 'carea', 'label': 'carea', 'type': 'char'}]},
)


class VisitReportForm(GeneratedForm):
    """Visit Report"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 224, 0, 366, 88, taborder=10)
        self.add('editmask', 'em_date2', 763, 0, 366, 88, taborder=20)
        self.add('datawindow', 'dw_route', 1385, 0, 791, 88, dataobject='d_clientsroute_code', taborder=60)
        self.add('commandbutton', 'cb_show', 2272, 0, 265, 96, text='Show', taborder=30)
        self.add('commandbutton', 'cb_3', 2533, 0, 265, 96, text='&Save As', taborder=130)
        self.add('commandbutton', 'cb_1', 2793, 0, 270, 96, text='&Print', taborder=140)
        self.add('commandbutton', 'cb_sort', 3058, 0, 270, 96, text='Sort', taborder=50)
        self.add('commandbutton', 'cb_2', 3323, 0, 270, 96, text='E&xit', taborder=40)
        self.add('checkbox', 'cbx_route', 2181, 4, 78, 76)
        self.add('statictext', 'st_1', 0, 8, 219, 76, text='From :')
        self.add('statictext', 'st_2', 613, 8, 142, 76, text='To :')
        self.add('statictext', 'st_5', 1175, 8, 206, 68, text='Route :')
        self.add('datawindow', 'dw_grp', 224, 100, 677, 88, dataobject='d_clientsgrp_code', taborder=110)
        self.add('datawindow', 'dw_area', 1385, 100, 745, 88, dataobject='d_clientsarea_code', taborder=100)
        self.add('checkbox', 'cbx_area', 2139, 104, 78, 76)
        self.add('checkbox', 'cbx_withvisit', 2281, 104, 485, 80, text='With Visit Only')
        self.add('checkbox', 'cbx_areasummary', 2798, 104, 649, 80, text='Areawise Summary')
        self.add('statictext', 'st_3', 0, 108, 219, 76, text='Group :')
        self.add('checkbox', 'cbx_grp', 914, 108, 91, 76)
        self.add('statictext', 'st_31', 1166, 108, 215, 80, text='Area :')
        self.add('datawindow', 'dw_suculist', 0, 188, 3602, 2044, dataobject='d_customer_visitreport', taborder=60)
