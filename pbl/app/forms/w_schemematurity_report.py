"""Scheme Maturity — w_schemematurity_report.

Generated from the PowerBuilder window ``w_schemematurity_report.srw`` by
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
    name='w_schemematurity_report',
    title='Scheme Maturity',
    width=3666,
    height=2372,
    controls=[],
    tables=['accountm'],
    source_path='w_schemematurity_report.srw',
    report={'dataobject': 'd_schemematurity_report', 'sql': 'SELECT clients.city AS clients_city, clients.name AS clients_name, clients_kuridet.startdate AS clients_kuridet_startdate, clients_kuridet.instnos AS clients_kuridet_instnos, clients_kuridet.instamt AS clients_kuridet_instamt, clients_kuridet.totamt AS clients_kuridet_totamt, clients_kuridet.finished AS clients_kuridet_finished, clients_kuridet.finisheddate AS clients_kuridet_finisheddate, clients_kuridet.kuritype AS clients_kuridet_kuritype, clients.code AS clients_code, clients.cocode AS clients_cocode, clients_kuridet.colntype AS clients_kuridet_colntype, clients.addr1 AS clients_addr1, clients.addr2 AS clients_addr2, clients.addr3 AS clients_addr3, clients.telephone AS clients_telephone, clients_kuridet.colnagent AS clients_kuridet_colnagent, clients_kuridet.showwgtdet AS clients_kuridet_showwgtdet, clients_kuridet.matdate AS clients_kuridet_matdate, (select sum(kuricolln.amount) from kuricolln where kuricolln.code = clients.code and kuricolln.tdate >= :rdate1 and kuricolln.tdate <= :rdate2 and kuricolln.control <= :rlevel) as totcolln2, (select sum(kuricolln.wgt) from kuricolln where kuricolln.code = clients.code and kuricolln.tdate >= :rdate1 and kuricolln.tdate <= :rdate2 and kuricolln.control <= :rlevel and kuricolln.grate > 0 ) as totwgt, (select sum(kurifinishdet.netgwgt) from kurifinishdet where kurifinishdet.code = clients.code) as finwgt, (select sum(kurifinishdet.avgrate) from kurifinishdet where kurifinishdet.code = clients.code) as finavgrate, ( ifnull( clients_kuridet.collnopbal , 0 , clients_kuridet.collnopbal) + ifnull(totcolln2,0,totcolln2)) as totcolln FROM clients, clients_kuridet WHERE clients.code = clients_kuridet.code ORDER BY clients_kuridet.matdate ASC, clients.name ASC', 'args': ['rdate1', 'rdate2', 'rlevel', 'rreqinst'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date', 'rlevel': 'number', 'rreqinst': 'number'}, 'tables': ['clients', 'clients_kuridet'], 'columns': [{'name': 'city', 'label': 'city', 'type': 'char'}, {'name': 'clients_name', 'label': 'Name', 'type': 'char'}, {'name': 'clients_kuridet_startdate', 'label': 'clients_kuridet_startdate', 'type': 'date'}, {'name': 'clients_kuridet_instnos', 'label': 'clients_kuridet_instnos', 'type': 'long'}, {'name': 'clients_kuridet_instamt', 'label': 'clients_kuridet_instamt', 'type': 'decimal'}, {'name': 'clients_kuridet_totamt', 'label': 'clients_kuridet_totamt', 'type': 'decimal'}, {'name': 'clients_kuridet_finished', 'label': 'clients_kuridet_finished', 'type': 'char'}, {'name': 'clients_kuridet_finisheddate', 'label': 'clients_kuridet_finisheddate', 'type': 'date'}, {'name': 'clients_kuridet_kuritype', 'label': 'clients_kuridet_kuritype', 'type': 'char'}, {'name': 'clients_code', 'label': 'clients_code', 'type': 'char'}, {'name': 'totcolln2', 'label': 'totcolln2', 'type': 'decimal'}, {'name': 'ctotwgt', 'label': 'ctotwgt', 'type': 'decimal'}, {'name': 'clients_cocode', 'label': 'clients_cocode', 'type': 'char'}, {'name': 'clients_kuridet_colntype', 'label': 'clients_kuridet_colntype', 'type': 'char'}, {'name': 'clients_addr1', 'label': 'clients_addr1', 'type': 'char'}, {'name': 'clients_addr2', 'label': 'clients_addr2', 'type': 'char'}, {'name': 'clients_addr3', 'label': 'clients_addr3', 'type': 'char'}, {'name': 'clients_telephone', 'label': 'clients_telephone', 'type': 'char'}, {'name': 'clients_kuridet_colnagent', 'label': 'clients_kuridet_colnagent', 'type': 'char'}, {'name': 'finwgt', 'label': 'finwgt', 'type': 'decimal'}, {'name': 'finavgrate', 'label': 'finavgrate', 'type': 'decimal'}, {'name': 'clients_kuridet_showwgtdet', 'label': 'clients_kuridet_showwgtdet', 'type': 'char'}, {'name': 'clients_kuridet_matdate', 'label': 'clients_kuridet_matdate', 'type': 'date'}, {'name': 'ctotcolln', 'label': 'ctotcolln', 'type': 'decimal'}]},
)


class SchemeMaturityForm(GeneratedForm):
    """Scheme Maturity"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('datawindow', 'dw_accode', 1458, 0, 1019, 92, dataobject='d_kuri_cust', taborder=30)
        self.add('commandbutton', 'cb_show', 2510, 0, 256, 96, text='&Show', taborder=110)
        self.add('commandbutton', 'cb_print', 3113, 0, 256, 100, text='&Print', taborder=140)
        self.add('commandbutton', 'cb_exit', 3378, 0, 256, 100, text='E&xit', taborder=130)
        self.add('editmask', 'em_date1', 242, 4, 398, 92, taborder=10)
        self.add('editmask', 'em_date2', 795, 4, 393, 92, taborder=20)
        self.add('statictext', 'st_1', 14, 16, 219, 64, text='From :')
        self.add('statictext', 'st_2', 654, 16, 137, 72, text='To :')
        self.add('statictext', 'st_3', 1225, 16, 224, 72, text='Party :')
        self.add('datawindow', 'dw_agent', 1458, 96, 402, 88, dataobject='d_staffcode', taborder=81)
        self.add('dropdownlistbox', 'ddlb_finished', 2505, 96, 603, 476, text='All', items=['All', 'Finished Only', 'Not Finished Only'], taborder=50)
        self.add('datawindow', 'dw_co', 242, 100, 402, 88, dataobject='d_cust', taborder=40)
        self.add('statictext', 'st_8', 1015, 108, 434, 80, text='Colln Agent :')
        self.add('statictext', 'st_co', 69, 112, 165, 76, text='C/o :')
        self.add('checkbox', 'cbx_dosprint', 3177, 112, 270, 68, text='Speed')
        self.add('dropdownlistbox', 'ddlb_sorton', 3113, 184, 512, 500, text='Date', items=['Name', 'Code', 'Inst.Finish', 'Pending', 'Date'], taborder=100)
        self.add('datawindow', 'dw_kuritype', 242, 192, 677, 88, dataobject='d_kuritype_code', taborder=70)
        self.add('editmask', 'em_mininstfinish', 1463, 192, 261, 92, taborder=80)
        self.add('editmask', 'em_pend', 2217, 192, 261, 92, taborder=90)
        self.add('statictext', 'st_6', 2848, 196, 265, 80, text='Sort On :')
        self.add('statictext', 'st_mininstfinish', 983, 200, 466, 72, text='Min Inst.Finish :')
        self.add('statictext', 'st_7', 1778, 200, 434, 80, text='Min Inst.Pend :')
        self.add('checkbox', 'cbx_withbal', 2510, 200, 315, 80, text='With Bal')
        self.add('statictext', 'st_5', 0, 204, 233, 64, text='SType :')
        self.add('datawindow', 'dw_1', 0, 288, 3634, 1872, dataobject='d_schemematurity_report', taborder=120)
