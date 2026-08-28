"""Scheme Collection — w_schemecolln_report.

Generated from the PowerBuilder window ``w_schemecolln_report.srw`` by
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
    name='w_schemecolln_report',
    title='Scheme Collection',
    width=3685,
    height=2336,
    controls=[],
    tables=['accountm', 'kuricolln'],
    source_path='w_schemecolln_report.srw',
    report={'dataobject': 'd_schemecolln_report', 'sql': 'SELECT kuricolln.tdate AS kuricolln_tdate, clients.name AS clients_name, kuricolln.amount AS kuricolln_amount, kuricolln.grate AS kuricolln_grate, clients.code AS clients_code, clients.cocode AS clients_cocode, clients_kuridet.kuritype AS clients_kuridet_kuritype, clients.addr1 AS clients_addr1, clients.addr2 AS clients_addr2, clients.addr3 AS clients_addr3, clients_kuridet.finished AS clients_kuridet_finished, clients_kuridet.colnagent AS clients_kuridet_colnagent, clients_kuridet.showwgtdet AS clients_kuridet_showwgtdet, kuricolln.agent AS kuricolln_agent, kuricolln.wgt AS kuricolln_wgt, clients.route AS clients_route, clients.carea AS clients_carea FROM kuricolln, clients, clients_kuridet WHERE kuricolln.code = clients.code AND clients.code = clients_kuridet.code ORDER BY kuricolln.tdate ASC, clients.name ASC', 'args': ['rdate1', 'rdate2', 'rlevel', 'rreqinst', 'ropamt', 'ropwgt'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date', 'rlevel': 'number', 'rreqinst': 'number', 'ropamt': 'decimal', 'ropwgt': 'decimal'}, 'tables': ['kuricolln', 'clients', 'clients_kuridet'], 'columns': [{'name': 'kuricolln_tdate', 'label': 'Date', 'type': 'date'}, {'name': 'clients_name', 'label': 'Name', 'type': 'char'}, {'name': 'kuricolln_amount', 'label': 'Collection', 'type': 'decimal'}, {'name': 'kuricolln_grate', 'label': 'Grate', 'type': 'decimal'}, {'name': 'clients_code', 'label': 'clients_code', 'type': 'char'}, {'name': 'clients_cocode', 'label': 'clients_cocode', 'type': 'char'}, {'name': 'clients_kuridet_kuritype', 'label': 'clients_kuridet_kuritype', 'type': 'char'}, {'name': 'clients_addr1', 'label': 'clients_addr1', 'type': 'char'}, {'name': 'clients_addr2', 'label': 'clients_addr2', 'type': 'char'}, {'name': 'clients_addr3', 'label': 'clients_addr3', 'type': 'char'}, {'name': 'clients_kuridet_finished', 'label': 'clients_kuridet_finished', 'type': 'char'}, {'name': 'clients_kuridet_colnagent', 'label': 'clients_kuridet_colnagent', 'type': 'char'}, {'name': 'clients_kuridet_showwgtdet', 'label': 'clients_kuridet_showwgtdet', 'type': 'char'}, {'name': 'kuricolln_agent', 'label': 'kuricolln_agent', 'type': 'char'}, {'name': 'kuricolln_wgt', 'label': 'kuricolln_wgt', 'type': 'decimal'}, {'name': 'clients_route', 'label': 'clients_route', 'type': 'char'}, {'name': 'clients_carea', 'label': 'clients_carea', 'type': 'char'}]},
)


class SchemeCollectionForm(GeneratedForm):
    """Scheme Collection"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('datawindow', 'dw_accode', 1760, 0, 1019, 92, dataobject='d_kuri_cust', taborder=30)
        self.add('commandbutton', 'cb_show', 2816, 0, 256, 92, text='&Show', taborder=110)
        self.add('editmask', 'em_date1', 242, 4, 398, 92, taborder=10)
        self.add('editmask', 'em_date2', 1042, 4, 393, 92, taborder=20)
        self.add('commandbutton', 'cb_print', 3113, 4, 256, 92, text='&Print', taborder=140)
        self.add('commandbutton', 'cb_exit', 3378, 4, 256, 92, text='E&xit', taborder=130)
        self.add('statictext', 'st_1', 14, 16, 219, 64, text='From :')
        self.add('statictext', 'st_2', 901, 16, 137, 72, text='To :')
        self.add('statictext', 'st_3', 1527, 16, 224, 72, text='Party :')
        self.add('commandbutton', 'cb_3', 2816, 92, 256, 96, text='&Save As', taborder=91)
        self.add('datawindow', 'dw_route', 1760, 96, 791, 88, dataobject='d_clientsroute_code', taborder=91)
        self.add('datawindow', 'dw_co', 242, 100, 402, 88, dataobject='d_cust', taborder=40)
        self.add('datawindow', 'dw_agent', 1042, 100, 402, 88, dataobject='d_staffcode', taborder=81)
        self.add('statictext', 'st_7', 1527, 108, 224, 80, text='Route :')
        self.add('statictext', 'st_co', 69, 112, 165, 76, text='C/o :')
        self.add('statictext', 'st_8', 658, 112, 384, 80, text='Colln Agent :')
        self.add('checkbox', 'cbx_dosprint', 3177, 112, 270, 68, text='Speed')
        self.add('dropdownlistbox', 'ddlb_sorton', 3113, 184, 512, 500, text='Date', items=['Name', 'Code', 'Inst.Finish', 'Pending', 'Date'], taborder=100)
        self.add('datawindow', 'dw_area', 1760, 188, 745, 88, dataobject='d_clientsarea_code', taborder=80)
        self.add('datawindow', 'dw_kuritype', 242, 192, 677, 88, dataobject='d_kuritype_code', taborder=70)
        self.add('statictext', 'st_6', 2816, 196, 265, 80, text='Sort On :')
        self.add('checkbox', 'cbx_withrcptno', 1033, 200, 439, 80, text='With Rcpt No')
        self.add('statictext', 'st_31', 1527, 200, 224, 80, text='Area :')
        self.add('statictext', 'st_5', 0, 204, 233, 64, text='SType :')
        self.add('datawindow', 'dw_1', 0, 288, 3634, 1872, dataobject='d_schemecolln_report', taborder=120)
        self.add('checkbox', 'cbx_nocollnlist', 2834, 300, 549, 80, text='No Collection List')
