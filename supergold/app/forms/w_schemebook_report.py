"""Scheme Book — w_schemebook_report.

Generated from the PowerBuilder window ``w_schemebook_report.srw`` by
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
    name='w_schemebook_report',
    title='Scheme Book',
    width=3666,
    height=2408,
    controls=[],
    tables=['accountm'],
    source_path='w_schemebook_report.srw',
    report={'dataobject': 'd_schemebook_report', 'sql': 'SELECT clients.city AS clients_city, clients.name AS clients_name, clients_kuridet.startdate AS clients_kuridet_startdate, clients_kuridet.instnos AS clients_kuridet_instnos, clients_kuridet.instamt AS clients_kuridet_instamt, clients_kuridet.totamt AS clients_kuridet_totamt, clients_kuridet.finished AS clients_kuridet_finished, clients_kuridet.finisheddate AS clients_kuridet_finisheddate, clients_kuridet.kuritype AS clients_kuridet_kuritype, clients.code AS clients_code, clients.cocode AS clients_cocode, clients_kuridet.colntype AS clients_kuridet_colntype, clients.addr1 AS clients_addr1, clients.addr2 AS clients_addr2, clients.addr3 AS clients_addr3, clients.telephone AS clients_telephone, clients_kuridet.colnagent AS clients_kuridet_colnagent, clients_kuridet.showwgtdet AS clients_kuridet_showwgtdet, clients_kuridet.opwgt AS clients_kuridet_opwgt, clients_kuridet.opwgtb AS clients_kuridet_opwgtb, clients.opbalance AS clients_opbalance, clients.opbalanceb AS clients_opbalanceb, clients.opweight AS clients_opweight, clients_kuridet.collnopbal AS clients_kuridet_collnopbal, clients.route AS clients_route, clients.carea AS clients_carea, (select sum(kuricolln.amount) from kuricolln where kuricolln.code = clients.code and kuricolln.tdate >= :rdate1 and kuricolln.tdate <= :rdate2 and kuricolln.control <= :rlevel) as totcolln, (select sum(kuricolln.wgt) from kuricolln where kuricolln.code = clients.code and kuricolln.tdate >= :rdate1 and kuricolln.tdate <= :rdate2 and kuricolln.control <= :rlevel and kuricolln.grate > 0) as totwgt, (select sum(kurifinishdet.netgwgt) from kurifinishdet where kurifinishdet.code = clients.code) as finwgt, (select sum(kurifinishdet.avgrate) from kurifinishdet where kurifinishdet.code = clients.code) as finavgrate, (select sum(kuricolln.amount) from kuricolln where kuricolln.code = clients.code and kuricolln.tdate < :rdate1 and kuricolln.control <= :rlevel) as opamt2, (select sum(kuricolln.wgt) from kuricolln where kuricolln.code = clients.code and kuricolln.tdate < :rdate1 and kuricolln.control <= :rlevel and kuricolln.grate > 0) as opwgt2 FROM clients, clients_kuridet WHERE clients.code = clients_kuridet.code ORDER BY clients.name ASC', 'args': ['rdate1', 'rdate2', 'rlevel', 'rreqinst', 'rgrate'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date', 'rlevel': 'number', 'rreqinst': 'number', 'rgrate': 'decimal'}, 'tables': ['clients', 'clients_kuridet'], 'columns': [{'name': 'city', 'label': 'city', 'type': 'char'}, {'name': 'clients_name', 'label': 'Name', 'type': 'char'}, {'name': 'clients_kuridet_startdate', 'label': 'clients_kuridet_startdate', 'type': 'date'}, {'name': 'clients_kuridet_instnos', 'label': 'clients_kuridet_instnos', 'type': 'long'}, {'name': 'clients_kuridet_instamt', 'label': 'clients_kuridet_instamt', 'type': 'decimal'}, {'name': 'clients_kuridet_totamt', 'label': 'clients_kuridet_totamt', 'type': 'decimal'}, {'name': 'clients_kuridet_finished', 'label': 'clients_kuridet_finished', 'type': 'char'}, {'name': 'clients_kuridet_finisheddate', 'label': 'clients_kuridet_finisheddate', 'type': 'date'}, {'name': 'clients_kuridet_kuritype', 'label': 'clients_kuridet_kuritype', 'type': 'char'}, {'name': 'clients_code', 'label': 'clients_code', 'type': 'char'}, {'name': 'ctotcolln', 'label': 'ctotcolln', 'type': 'decimal'}, {'name': 'ctotwgt', 'label': 'ctotwgt', 'type': 'decimal'}, {'name': 'clients_cocode', 'label': 'clients_cocode', 'type': 'char'}, {'name': 'clients_kuridet_colntype', 'label': 'clients_kuridet_colntype', 'type': 'char'}, {'name': 'clients_addr1', 'label': 'clients_addr1', 'type': 'char'}, {'name': 'clients_addr2', 'label': 'clients_addr2', 'type': 'char'}, {'name': 'clients_addr3', 'label': 'clients_addr3', 'type': 'char'}, {'name': 'clients_telephone', 'label': 'clients_telephone', 'type': 'char'}, {'name': 'clients_kuridet_colnagent', 'label': 'clients_kuridet_colnagent', 'type': 'char'}, {'name': 'finwgt', 'label': 'finwgt', 'type': 'decimal'}, {'name': 'finavgrate', 'label': 'finavgrate', 'type': 'decimal'}, {'name': 'clients_kuridet_showwgtdet', 'label': 'clients_kuridet_showwgtdet', 'type': 'char'}, {'name': 'clients_kuridet_opwgt', 'label': 'clients_kuridet_opwgt', 'type': 'decimal'}, {'name': 'clients_kuridet_opwgtb', 'label': 'clients_kuridet_opwgtb', 'type': 'decimal'}, {'name': 'clients_opbalance', 'label': 'clients_opbalance', 'type': 'decimal'}, {'name': 'clients_opbalanceb', 'label': 'clients_opbalanceb', 'type': 'decimal'}, {'name': 'clients_opweight', 'label': 'clients_opweight', 'type': 'decimal'}, {'name': 'opamt2', 'label': 'opamt2', 'type': 'decimal'}, {'name': 'opwgt2', 'label': 'opwgt2', 'type': 'decimal'}, {'name': 'clients_kuridet_collnopbal', 'label': 'clients_kuridet_collnopbal', 'type': 'decimal'}, {'name': 'clients_route', 'label': 'clients_route', 'type': 'char'}, {'name': 'clients_carea', 'label': 'clients_carea', 'type': 'char'}]},
)


class SchemeBookForm(GeneratedForm):
    """Scheme Book"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('datawindow', 'dw_accode', 1760, 0, 1019, 92, dataobject='d_kuri_cust', taborder=30)
        self.add('commandbutton', 'cb_show', 2811, 0, 256, 96, text='&Show', taborder=110)
        self.add('commandbutton', 'cb_print', 3118, 0, 256, 100, text='&Print', taborder=140)
        self.add('commandbutton', 'cb_exit', 3378, 0, 256, 100, text='E&xit', taborder=130)
        self.add('editmask', 'em_date1', 242, 4, 398, 92, taborder=10)
        self.add('editmask', 'em_date2', 1042, 4, 393, 92, taborder=20)
        self.add('statictext', 'st_1', 14, 16, 219, 64, text='From :')
        self.add('statictext', 'st_2', 901, 16, 137, 72, text='To :')
        self.add('statictext', 'st_3', 1527, 16, 224, 72, text='Party :')
        self.add('datawindow', 'dw_agent', 1042, 96, 402, 88, dataobject='d_staffcode', taborder=81)
        self.add('datawindow', 'dw_accode2', 1760, 96, 1019, 92, dataobject='d_kuri_cust', taborder=10)
        self.add('commandbutton', 'cb_3', 2811, 96, 256, 96, text='&Save As', taborder=60)
        self.add('datawindow', 'dw_co', 242, 100, 402, 88, dataobject='d_cust', taborder=40)
        self.add('statictext', 'st_4', 1481, 100, 270, 72, text='Party to :')
        self.add('dropdownlistbox', 'ddlb_finished', 3118, 100, 512, 476, text='All', items=['All', 'Finished Only', 'Not Finished Only'], taborder=50)
        self.add('statictext', 'st_8', 649, 108, 389, 80, text='Colln Agent :')
        self.add('statictext', 'st_co', 69, 112, 165, 76, text='C/o :')
        self.add('datawindow', 'dw_kuritype', 242, 192, 677, 88, dataobject='d_kuritype_code', taborder=70)
        self.add('editmask', 'em_mininstfinish', 1760, 192, 261, 92, taborder=80)
        self.add('editmask', 'em_pend', 2523, 192, 261, 92, taborder=90)
        self.add('dropdownlistbox', 'ddlb_sorton', 3118, 192, 512, 772, text='Date', items=['Name', 'Code', 'Inst.Finish', 'Pending', 'Date', 'Next Date', 'Due Date'], taborder=100)
        self.add('statictext', 'st_mininstfinish', 1285, 200, 466, 72, text='Min Inst.Finish :')
        self.add('statictext', 'st_7', 2085, 200, 434, 80, text='Min Inst.Pend :')
        self.add('statictext', 'st_5', 0, 204, 233, 64, text='SType :')
        self.add('statictext', 'st_6', 2848, 204, 265, 80, text='Sort On :')
        self.add('editmask', 'em_grate', 242, 284, 398, 96, text='none', taborder=100)
        self.add('editmask', 'em_maxinstfinish', 1760, 288, 261, 92, taborder=100)
        self.add('checkbox', 'cbx_basedstartdate', 704, 292, 549, 80, text='Based on Start Date')
        self.add('editmask', 'em_nextdate', 3118, 292, 361, 92, taborder=30)
        self.add('statictext', 'st_10', 0, 296, 233, 64, text='GRate :')
        self.add('statictext', 'st_11', 1271, 300, 485, 72, text='Max Inst.Finish :')
        self.add('statictext', 'st_9', 2770, 308, 343, 68, text='Next Date :')
        self.add('datawindow', 'dw_route', 242, 384, 791, 88, dataobject='d_clientsroute_code', taborder=40)
        self.add('datawindow', 'dw_area', 1760, 384, 745, 88, dataobject='d_clientsarea_code', taborder=130)
        self.add('statictext', 'st_12', 9, 396, 224, 80, text='Route :')
        self.add('statictext', 'st_31', 1531, 396, 224, 80, text='Area :')
        self.add('datawindow', 'dw_1', 0, 480, 3634, 1836, dataobject='d_schemebook_report', taborder=120)
