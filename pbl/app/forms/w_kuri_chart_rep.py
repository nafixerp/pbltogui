"""Chart — w_kuri_chart_rep.

Generated from the PowerBuilder window ``w_kuri_chart_rep.srw`` by
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
    name='w_kuri_chart_rep',
    title='Chart',
    width=3419,
    height=2192,
    controls=[],
    tables=['accountm', 'kuricolln', 'clients_kuridet'],
    source_path='w_kuri_chart_rep.srw',
    report={'dataobject': 'd_kuri_chart_rep', 'sql': "SELECT clients.code AS clients_code, clients.name AS clients_name, clients_kuridet.startdate AS clients_kuridet_startdate, clients_kuridet.instnos AS clients_kuridet_instnos, clients_kuridet.instamt AS clients_kuridet_instamt, clients_kuridet.totamt AS clients_kuridet_totamt, clients_kuridet.bonus AS clients_kuridet_bonus, clients_kuridet.finished AS clients_kuridet_finished, clients_kuridet.finisheddate AS clients_kuridet_finisheddate, clients_kuridet.kuritype AS clients_kuridet_kuritype, clients.addr1 AS clients_addr1, clients.addr2 AS clients_addr2, clients.addr3 AS clients_addr3, clients.telephone AS clients_telephone, clients_kuridet.colntype AS clients_kuridet_colntype, clients_kuridet.opwgt AS clients_kuridet_opwgt, clients_kuridet.opwgtb AS clients_kuridet_opwgtb, (0.00) as colnamt, (0)  as cino, (' ') as duedt, (' ') as datercvd, (0.00) as iamt, (' ') as overdue FROM clients, clients_kuridet WHERE clients.code = clients_kuridet.code", 'args': ['rcode', 'rdate', 'rlevel'], 'arg_types': {'rcode': 'string', 'rdate': 'date', 'rlevel': 'number'}, 'tables': ['clients', 'clients_kuridet'], 'columns': [{'name': 'clients_code', 'label': 'clients_code', 'type': 'char'}, {'name': 'clients_name', 'label': 'clients_name', 'type': 'char'}, {'name': 'clients_kuridet_startdate', 'label': 'clients_kuridet_startdate', 'type': 'date'}, {'name': 'clients_kuridet_instnos', 'label': 'clients_kuridet_instnos', 'type': 'long'}, {'name': 'clients_kuridet_instamt', 'label': 'clients_kuridet_instamt', 'type': 'decimal'}, {'name': 'clients_kuridet_totamt', 'label': 'clients_kuridet_totamt', 'type': 'decimal'}, {'name': 'clients_kuridet_bonus', 'label': 'clients_kuridet_bonus', 'type': 'decimal'}, {'name': 'clients_kuridet_finished', 'label': 'clients_kuridet_finished', 'type': 'char'}, {'name': 'clients_kuridet_finisheddate', 'label': 'clients_kuridet_finisheddate', 'type': 'date'}, {'name': 'clients_kuridet_kuritype', 'label': 'clients_kuridet_kuritype', 'type': 'char'}, {'name': 'clients_addr1', 'label': 'clients_addr1', 'type': 'char'}, {'name': 'clients_addr2', 'label': 'clients_addr2', 'type': 'char'}, {'name': 'clients_addr3', 'label': 'clients_addr3', 'type': 'char'}, {'name': 'clients_telephone', 'label': 'clients_telephone', 'type': 'char'}, {'name': 'clients_kuridet_colntype', 'label': 'clients_kuridet_colntype', 'type': 'char'}, {'name': 'ccolnamt', 'label': 'ccolnamt', 'type': 'decimal'}, {'name': 'clients_cino', 'label': 'clients_cino', 'type': 'long'}, {'name': 'cduedt', 'label': 'cduedt', 'type': 'char'}, {'name': 'cdatercvd', 'label': 'cdatercvd', 'type': 'char'}, {'name': 'ciamt', 'label': 'ciamt', 'type': 'decimal'}, {'name': 'coverdue', 'label': 'coverdue', 'type': 'char'}, {'name': 'clients_kuridet_opwgt', 'label': 'clients_kuridet_opwgt', 'type': 'decimal'}, {'name': 'clients_kuridet_opwgtb', 'label': 'clients_kuridet_opwgtb', 'type': 'decimal'}]},
)


class ChartForm(GeneratedForm):
    """Chart"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('datawindow', 'dw_accode', 256, 0, 1019, 92, dataobject='d_kuri_cust', taborder=10)
        self.add('editmask', 'em_date1', 1723, 4, 425, 84, taborder=20)
        self.add('commandbutton', 'cb_show', 2240, 4, 247, 88, text='&Show', taborder=30)
        self.add('commandbutton', 'cb_print', 2857, 4, 247, 88, text='&Print', taborder=60)
        self.add('commandbutton', 'cb_exit', 3122, 4, 233, 88, text='E&xit', taborder=50)
        self.add('statictext', 'st_2', 5, 8, 238, 80, text='Party :')
        self.add('statictext', 'st_1', 1367, 12, 347, 76, text='Upto Date :')
        self.add('datawindow', 'dw_1', 0, 104, 3360, 1892, dataobject='d_kuri_chart_rep', taborder=40)
        self.add('checkbox', 'cbx_chartonly', 2235, 116, 389, 80, text='Chart Only')
