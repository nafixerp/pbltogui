"""Smith List — w_suculist.

Generated from the PowerBuilder window ``w_suculist.srw`` by
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
    name='w_suculist',
    title='Smith List',
    width=3675,
    height=2268,
    controls=[],
    tables=['clients'],
    source_path='w_suculist.srw',
    grid={'control': 'dw_suculist', 'dataobject': 'd_suculist', 'table': 'clients', 'keys': ['code'], 'columns': [{'name': 'code', 'label': 'Code', 'type': 'char'}, {'name': 'name', 'label': 'Name', 'type': 'char'}, {'name': 'addr1', 'label': 'addr1', 'type': 'char'}, {'name': 'addr2', 'label': 'addr2', 'type': 'char'}, {'name': 'addr3', 'label': 'addr3', 'type': 'char'}, {'name': 'city', 'label': 'city', 'type': 'char'}, {'name': 'telephone', 'label': 'Phone', 'type': 'char'}, {'name': 'mobile', 'label': 'Mobile', 'type': 'char'}, {'name': 'ctype', 'label': 'ctype', 'type': 'char'}, {'name': 'prn', 'label': 'Prn', 'type': 'long'}, {'name': 'adate', 'label': 'adate', 'type': 'date'}, {'name': 'cocode', 'label': 'cocode', 'type': 'char'}, {'name': 'grp', 'label': 'grp', 'type': 'char'}, {'name': 'route', 'label': 'route', 'type': 'char'}, {'name': 'religion', 'label': 'religion', 'type': 'char'}, {'name': 'addr', 'label': 'Addr', 'type': 'char'}, {'name': 'email', 'label': 'Email', 'type': 'char'}, {'name': 'carea', 'label': 'carea', 'type': 'char'}]},
    report={'dataobject': 'd_suculist', 'sql': 'SELECT "clients"."code",   \r\n         "clients"."name",   \r\n         "clients"."addr1",   \r\n         "clients"."addr2",   \r\n         "clients"."addr3",   \r\n         "clients"."city",   \r\n         "clients"."telephone",   \r\n         "clients"."mobile",   \r\n         "clients"."ctype",   \r\n         "clients"."prn",   \r\n         "clients"."adate",   \r\n         "clients"."cocode",   \r\n         "clients"."grp",   \r\n         "clients"."route",   \r\n         "clients"."religion",   \r\n         ( addr1 +\', \'+ addr2 +\', \'+ addr3 +\', \'+ city  ) as addr,   \r\n         "clients"."email",   \r\n         "clients"."carea"  \r\n    FROM "clients"  \r\n   WHERE clients.ctype = :rmcs   \r\nORDER BY "clients"."ctype" ASC,   \r\n         "clients"."name" ASC', 'args': ['rmcs'], 'arg_types': {}, 'tables': ['clients'], 'columns': [{'name': 'code', 'label': 'Code', 'type': 'char'}, {'name': 'name', 'label': 'Name', 'type': 'char'}, {'name': 'addr1', 'label': 'addr1', 'type': 'char'}, {'name': 'addr2', 'label': 'addr2', 'type': 'char'}, {'name': 'addr3', 'label': 'addr3', 'type': 'char'}, {'name': 'city', 'label': 'city', 'type': 'char'}, {'name': 'telephone', 'label': 'Phone', 'type': 'char'}, {'name': 'mobile', 'label': 'Mobile', 'type': 'char'}, {'name': 'ctype', 'label': 'ctype', 'type': 'char'}, {'name': 'prn', 'label': 'Prn', 'type': 'long'}, {'name': 'adate', 'label': 'adate', 'type': 'date'}, {'name': 'cocode', 'label': 'cocode', 'type': 'char'}, {'name': 'grp', 'label': 'grp', 'type': 'char'}, {'name': 'route', 'label': 'route', 'type': 'char'}, {'name': 'religion', 'label': 'religion', 'type': 'char'}, {'name': 'addr', 'label': 'Addr', 'type': 'char'}, {'name': 'email', 'label': 'Email', 'type': 'char'}, {'name': 'carea', 'label': 'carea', 'type': 'char'}]},
    opens=['w_lettermerge'],
)


class SmithListForm(GeneratedForm):
    """Smith List"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 187, 0, 443, 92, taborder=10)
        self.add('editmask', 'em_date2', 763, 0, 443, 92, taborder=20)
        self.add('commandbutton', 'cb_filter', 1211, 0, 265, 96, text='Filter', taborder=30)
        self.add('commandbutton', 'cb_3', 1481, 0, 265, 96, text='&Save As', taborder=80)
        self.add('commandbutton', 'cb_1', 1746, 0, 270, 96, text='&Print', taborder=90)
        self.add('commandbutton', 'cb_sort', 2021, 0, 270, 96, text='Sort', taborder=90)
        self.add('commandbutton', 'cb_selectall', 2299, 0, 311, 96, text='Select All', taborder=70)
        self.add('commandbutton', 'cb_sendletters', 2633, 0, 402, 96, text='Send Letters', taborder=70)
        self.add('commandbutton', 'cb_updt', 3063, 0, 265, 96, text='Update', taborder=50)
        self.add('commandbutton', 'cb_2', 3328, 0, 270, 96, text='E&xit', taborder=40)
        self.add('statictext', 'st_1', 14, 4, 219, 76, text='From :')
        self.add('statictext', 'st_2', 640, 8, 123, 76, text='To :')
        self.add('datawindow', 'dw_suculist', 0, 96, 3602, 1956, dataobject='d_suculist', taborder=60)
        self.add('checkbox', 'cbx_form2', 3177, 100, 311, 76, text='&Form 2')
