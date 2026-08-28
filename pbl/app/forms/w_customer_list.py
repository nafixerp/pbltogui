"""Customer List — w_customer_list.

Generated from the PowerBuilder window ``w_customer_list.srw`` by
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
    name='w_customer_list',
    title='Customer List',
    width=3675,
    height=2316,
    controls=[],
    tables=['clients', 'daybook', 'accountm'],
    source_path='w_customer_list.srw',
    grid={'control': 'dw_suculist', 'dataobject': 'd_customer_list', 'table': 'clients', 'keys': ['code'], 'computes': [], 'columns': [{'name': 'code', 'label': 'Code', 'type': 'char'}, {'name': 'name', 'label': 'Name', 'type': 'char'}, {'name': 'addr1', 'label': 'addr1', 'type': 'char'}, {'name': 'addr2', 'label': 'addr2', 'type': 'char'}, {'name': 'addr3', 'label': 'addr3', 'type': 'char'}, {'name': 'city', 'label': 'city', 'type': 'char'}, {'name': 'telephone', 'label': 'Phone', 'type': 'char'}, {'name': 'mobile', 'label': 'Mobile', 'type': 'char'}, {'name': 'ctype', 'label': 'ctype', 'type': 'char'}, {'name': 'prn', 'label': 'Prn', 'type': 'long'}, {'name': 'adate', 'label': 'adate', 'type': 'date'}, {'name': 'cocode', 'label': 'cocode', 'type': 'char'}, {'name': 'grp', 'label': 'grp', 'type': 'char'}, {'name': 'route', 'label': 'route', 'type': 'char'}, {'name': 'religion', 'label': 'religion', 'type': 'char'}, {'name': 'addr', 'label': 'Addr', 'type': 'char'}, {'name': 'email', 'label': 'Email', 'type': 'char'}, {'name': 'carea', 'label': 'carea', 'type': 'char'}, {'name': 'religion', 'label': 'religion', 'type': 'char'}, {'name': 'relationway', 'label': 'relationway', 'type': 'char'}, {'name': 'relationbases', 'label': 'relationbases', 'type': 'char'}, {'name': 'working', 'label': 'working', 'type': 'char'}, {'name': 'purchtype', 'label': 'purchtype', 'type': 'char'}]},
    report={'dataobject': 'd_customer_list', 'sql': 'SELECT "clients"."code",   \r\n         "clients"."name",   \r\n         "clients"."addr1",   \r\n         "clients"."addr2",   \r\n         "clients"."addr3",   \r\n         "clients"."city",   \r\n         "clients"."telephone",   \r\n         "clients"."mobile",   \r\n         "clients"."ctype",   \r\n         "clients"."prn",   \r\n         "clients"."adate",   \r\n         "clients"."cocode",   \r\n         "clients"."grp",   \r\n         "clients"."route",   \r\n         "clients"."religion",   \r\n         ( addr1 +\', \'+ addr2 +\', \'+ addr3 +\', \'+ city  ) as addr,   \r\n         "clients"."email",   \r\n         "clients"."carea",\r\n         (select clients_advanced.religion from clients_advanced where clients_advanced.code  = clients.code) as religion,   \r\n         (select clients_advanced.relationway from clients_advanced where clients_advanced.code  = clients.code) as relationway,   \r\n         (select clients_advanced.relationbases from clients_advanced where clients_advanced.code  = clients.code) as relationbases,   \r\n         (select clients_advanced.working from clients_advanced where clients_advanced.code  = clients.code) as working,   \r\n         (select clients_advanced.purchasetype from clients_advanced where clients_advanced.code  = clients.code) as purchtype   \r\n    FROM "clients"  \r\n   WHERE clients.ctype = :rmcs   \r\nORDER BY "clients"."ctype" ASC,   \r\n         "clients"."name" ASC', 'computes': [], 'args': ['rmcs'], 'arg_types': {}, 'tables': ['clients'], 'columns': [{'name': 'code', 'label': 'Code', 'type': 'char'}, {'name': 'name', 'label': 'Name', 'type': 'char'}, {'name': 'addr1', 'label': 'addr1', 'type': 'char'}, {'name': 'addr2', 'label': 'addr2', 'type': 'char'}, {'name': 'addr3', 'label': 'addr3', 'type': 'char'}, {'name': 'city', 'label': 'city', 'type': 'char'}, {'name': 'telephone', 'label': 'Phone', 'type': 'char'}, {'name': 'mobile', 'label': 'Mobile', 'type': 'char'}, {'name': 'ctype', 'label': 'ctype', 'type': 'char'}, {'name': 'prn', 'label': 'Prn', 'type': 'long'}, {'name': 'adate', 'label': 'adate', 'type': 'date'}, {'name': 'cocode', 'label': 'cocode', 'type': 'char'}, {'name': 'grp', 'label': 'grp', 'type': 'char'}, {'name': 'route', 'label': 'route', 'type': 'char'}, {'name': 'religion', 'label': 'religion', 'type': 'char'}, {'name': 'addr', 'label': 'Addr', 'type': 'char'}, {'name': 'email', 'label': 'Email', 'type': 'char'}, {'name': 'carea', 'label': 'carea', 'type': 'char'}, {'name': 'religion', 'label': 'religion', 'type': 'char'}, {'name': 'relationway', 'label': 'relationway', 'type': 'char'}, {'name': 'relationbases', 'label': 'relationbases', 'type': 'char'}, {'name': 'working', 'label': 'working', 'type': 'char'}, {'name': 'purchtype', 'label': 'purchtype', 'type': 'char'}]},
)


class CustomerListForm(GeneratedForm):
    """Customer List"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 334, 0, 384, 92, taborder=10)
        self.add('editmask', 'em_date2', 864, 0, 384, 92, taborder=20)
        self.add('commandbutton', 'cb_filter', 1289, 0, 265, 96, text='Filter', taborder=30)
        self.add('commandbutton', 'cb_3', 1655, 0, 265, 96, text='&Save As', taborder=130)
        self.add('commandbutton', 'cb_1', 1934, 0, 270, 96, text='&Print', taborder=140)
        self.add('commandbutton', 'cb_sort', 2213, 0, 270, 96, text='Sort', taborder=50)
        self.add('commandbutton', 'cb_selectall', 2583, 0, 297, 96, text='Select All', taborder=120)
        self.add('commandbutton', 'cb_updt', 2903, 0, 251, 96, text='Update', taborder=50)
        self.add('commandbutton', 'cb_2', 3323, 0, 270, 96, text='E&xit', taborder=40)
        self.add('statictext', 'st_1', 0, 4, 329, 76, text='Date From :')
        self.add('statictext', 'st_2', 736, 8, 123, 76, text='To :')
        self.add('dropdownlistbox', 'ddlb_religion', 329, 92, 571, 544, text='All', items=['Hindu', 'Muslim', 'Christian', 'Others', 'All'], taborder=110)
        self.add('dropdownlistbox', 'ddlb_relationway', 2587, 92, 571, 544, text='All', items=['Mouth to Mouth', 'Channels', 'Newspaper', 'Hoardings', 'General Add', 'C/o', 'All'], taborder=90)
        self.add('statictext', 'st_30', 23, 100, 306, 80, text='Religion :')
        self.add('datawindow', 'dw_route', 1289, 100, 791, 88, dataobject='d_clientsroute_code', taborder=71)
        self.add('statictext', 'st_3', 2139, 104, 443, 80, text='Known through :')
        self.add('statictext', 'st_7', 1061, 112, 224, 80, text='Route :')
        self.add('dropdownlistbox', 'ddlb_working', 329, 188, 571, 544, text='All', items=['Employee', 'Business', 'Gulf', 'Agriculture', 'All'], taborder=61)
        self.add('dropdownlistbox', 'ddlb_relationbases', 2587, 188, 571, 544, text='All', items=['Owner Family', 'Manager', 'PRO', 'Staff', 'Others', 'All'], taborder=80)
        self.add('datawindow', 'dw_area', 1289, 192, 745, 88, dataobject='d_clientsarea_code', taborder=100)
        self.add('statictext', 'st_6', 23, 200, 297, 80, text='Work :')
        self.add('statictext', 'st_4', 2240, 200, 343, 80, text='Related To :')
        self.add('statictext', 'st_31', 1061, 204, 224, 80, text='Area :')
        self.add('checkbox', 'cbx_form2', 3314, 224, 311, 76, text='&Form 2')
        self.add('datawindow', 'dw_group', 1289, 284, 677, 88, dataobject='d_clientsgrp_code', taborder=110)
        self.add('dropdownlistbox', 'ddlb_purchtype', 2592, 284, 571, 544, text='All', items=['Ordinary', 'Culcutta', 'Antic', 'Diamond', 'All'], taborder=70)
        self.add('commandbutton', 'cb_delunusedcust', 5, 288, 901, 96, text='Del All Unused Customers', taborder=120)
        self.add('statictext', 'st_5', 2245, 292, 343, 80, text='Item Type :')
        self.add('statictext', 'st_8', 1042, 296, 242, 80, text='Group :')
        self.add('datawindow', 'dw_suculist', 0, 384, 3602, 1776, dataobject='d_customer_list', taborder=60)
