"""Colln Commision Report — w_schemebook_comnrep.

Generated from the PowerBuilder window ``w_schemebook_comnrep.srw`` by
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
    name='w_schemebook_comnrep',
    title='Colln Commision Report',
    width=3666,
    height=2372,
    controls=[],
    tables=[],
    source_path='w_schemebook_comnrep.srw',
    grid={'control': 'dw_1', 'dataobject': 'd_schemebook_comnrep', 'table': 'clients', 'keys': ['code'], 'computes': [{'name': 'totcomn', 'expression': 'if(colncomn > 0, round( ctotcolln  *  colncomn / 100,0) ,  tjoint * comnrate)', 'format': '########0.00', 'label': 'totcomn', 'band': 'detail'}, {'name': 'compute_4', 'expression': 'count(clients_code for all)', 'format': '[general]', 'label': 'compute_4', 'band': 'summary'}, {'name': 'compute_5', 'expression': 'sum(tjoint for all)', 'format': '#######0', 'label': 'compute_5', 'band': 'summary'}, {'name': 'compute_6', 'expression': 'sum(tjointcolln for all)', 'format': '#########0.00', 'label': 'compute_6', 'band': 'summary'}, {'name': 'compute_3', 'expression': 'sum(ctotcolln for all)', 'format': '########0.00', 'label': 'compute_3', 'band': 'summary'}, {'name': 'compute_7', 'expression': 'sum(ctotwgt for all)', 'format': '########0.000', 'label': 'compute_7', 'band': 'summary'}, {'name': 'compute_2', 'expression': 'sum(totcomn for all)', 'format': '########0.00', 'label': 'compute_2', 'band': 'summary'}], 'columns': [{'name': 'city', 'label': 'city', 'type': 'char'}, {'name': 'name', 'label': 'Name', 'type': 'char'}, {'name': 'code', 'label': 'clients_code', 'type': 'char'}, {'name': 'totcolln', 'label': 'ctotcolln', 'type': 'decimal'}, {'name': 'totwgt', 'label': 'ctotwgt', 'type': 'decimal'}, {'name': 'cocode', 'label': 'clients_cocode', 'type': 'char'}, {'name': 'addr1', 'label': 'clients_addr1', 'type': 'char'}, {'name': 'addr2', 'label': 'clients_addr2', 'type': 'char'}, {'name': 'addr3', 'label': 'clients_addr3', 'type': 'char'}, {'name': 'telephone', 'label': 'clients_telephone', 'type': 'char'}, {'name': 'colncomn', 'label': 'colncomn', 'type': 'decimal'}, {'name': 'tjoint', 'label': 'tjoint', 'type': 'long'}, {'name': 'tjointcolln', 'label': 'tjointcolln', 'type': 'decimal'}, {'name': 'comnrate', 'label': 'comnrate', 'type': 'decimal'}, {'name': 'kuritype', 'label': 'kuritype', 'type': 'char'}]},
    report={'dataobject': 'd_schemebook_comnrep', 'sql': 'SELECT clients.city AS clients_city, clients.name AS clients_name, clients.code AS clients_code, clients.cocode AS clients_cocode, clients.addr1 AS clients_addr1, clients.addr2 AS clients_addr2, clients.addr3 AS clients_addr3, clients.telephone AS clients_telephone, clients.colncomn AS clients_colncomn, (select sum(kuricolln.amount) from kuricolln,clients_kuridet where kuricolln.agent = clients.code and kuricolln.tdate >= :rdate1 and kuricolln.tdate <= :rdate2 and kuricolln.control <= :rlevel and kuricolln.code = clients_kuridet.code and clients_kuridet.kuritype =  ifnull(:rktype, clients_kuridet.kuritype, :rktype) ) as totcolln, (select sum(kuricolln.wgt) from kuricolln,clients_kuridet where kuricolln.agent = clients.code and kuricolln.tdate >= :rdate1 and kuricolln.tdate <= :rdate2 and kuricolln.control <= :rlevel and kuricolln.grate > 0 and kuricolln.code = clients_kuridet.code and clients_kuridet.kuritype =  ifnull(:rktype, clients_kuridet.kuritype, :rktype) ) as totwgt, (select count(clients_kuridet.code) from clients_kuridet where clients_kuridet.colnagent = clients.code and clients_kuridet.startdate >= :rdate1 and clients_kuridet.startdate <= :rdate2 and clients_kuridet.kuritype = ifnull(:rktype, clients_kuridet.kuritype, :rktype) ) as tjoint, (select sum(kuricolln.amount) from clients_kuridet,kuricolln where kuricolln.code = clients_kuridet.code and kuricolln.agent = clients.code and clients_kuridet.startdate >= :rdate1 and clients_kuridet.startdate <= :rdate2 and clients_kuridet.kuritype = ifnull(:rktype, clients_kuridet.kuritype, :rktype) ) as tjointcolln, (select kuritype.comnrate from kuritype where kuritype.code = kuritype) as comnrate, (select clients_kuridet.kuritype from clients_kuridet where clients_kuridet.code = clients.code) as kuritype FROM clients ORDER BY clients.name ASC', 'computes': [{'name': 'totcomn', 'expression': 'if(colncomn > 0, round( ctotcolln  *  colncomn / 100,0) ,  tjoint * comnrate)', 'format': '########0.00', 'label': 'totcomn', 'band': 'detail'}, {'name': 'compute_4', 'expression': 'count(clients_code for all)', 'format': '[general]', 'label': 'compute_4', 'band': 'summary'}, {'name': 'compute_5', 'expression': 'sum(tjoint for all)', 'format': '#######0', 'label': 'compute_5', 'band': 'summary'}, {'name': 'compute_6', 'expression': 'sum(tjointcolln for all)', 'format': '#########0.00', 'label': 'compute_6', 'band': 'summary'}, {'name': 'compute_3', 'expression': 'sum(ctotcolln for all)', 'format': '########0.00', 'label': 'compute_3', 'band': 'summary'}, {'name': 'compute_7', 'expression': 'sum(ctotwgt for all)', 'format': '########0.000', 'label': 'compute_7', 'band': 'summary'}, {'name': 'compute_2', 'expression': 'sum(totcomn for all)', 'format': '########0.00', 'label': 'compute_2', 'band': 'summary'}], 'args': ['rdate1', 'rdate2', 'rlevel', 'rreqinst', 'rktype'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date', 'rlevel': 'number', 'rreqinst': 'number', 'rktype': 'string'}, 'tables': ['clients'], 'columns': [{'name': 'city', 'label': 'city', 'type': 'char'}, {'name': 'clients_name', 'label': 'Name', 'type': 'char'}, {'name': 'clients_code', 'label': 'clients_code', 'type': 'char'}, {'name': 'ctotcolln', 'label': 'ctotcolln', 'type': 'decimal'}, {'name': 'ctotwgt', 'label': 'ctotwgt', 'type': 'decimal'}, {'name': 'clients_cocode', 'label': 'clients_cocode', 'type': 'char'}, {'name': 'clients_addr1', 'label': 'clients_addr1', 'type': 'char'}, {'name': 'clients_addr2', 'label': 'clients_addr2', 'type': 'char'}, {'name': 'clients_addr3', 'label': 'clients_addr3', 'type': 'char'}, {'name': 'clients_telephone', 'label': 'clients_telephone', 'type': 'char'}, {'name': 'colncomn', 'label': 'colncomn', 'type': 'decimal'}, {'name': 'tjoint', 'label': 'tjoint', 'type': 'long'}, {'name': 'tjointcolln', 'label': 'tjointcolln', 'type': 'decimal'}, {'name': 'comnrate', 'label': 'comnrate', 'type': 'decimal'}, {'name': 'kuritype', 'label': 'kuritype', 'type': 'char'}]},
)


class CollnCommisionReportForm(GeneratedForm):
    """Colln Commision Report"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('commandbutton', 'cb_show', 2875, 0, 256, 96, text='&Show', taborder=110)
        self.add('commandbutton', 'cb_print', 3127, 0, 256, 96, text='&Print', taborder=140)
        self.add('commandbutton', 'cb_exit', 3378, 0, 256, 96, text='E&xit', taborder=130)
        self.add('editmask', 'em_date1', 201, 4, 375, 92, taborder=10)
        self.add('editmask', 'em_date2', 713, 4, 370, 92, taborder=20)
        self.add('datawindow', 'dw_agent', 1472, 4, 402, 88, dataobject='d_staffcode', taborder=81)
        self.add('statictext', 'st_3', 1920, 8, 215, 80, text='SType :')
        self.add('datawindow', 'dw_kuritype', 2139, 8, 677, 88, dataobject='d_kuritype_code', taborder=91)
        self.add('statictext', 'st_8', 1093, 12, 375, 80, text='CollnAgent :')
        self.add('statictext', 'st_1', 9, 16, 187, 64, text='From :')
        self.add('statictext', 'st_2', 571, 16, 137, 72, text='To :')
        self.add('datawindow', 'dw_1', 0, 108, 3634, 1996, dataobject='d_schemebook_comnrep', taborder=120)
        self.add('checkbox', 'cbx_stypewise', 2875, 124, 658, 80, text='Scheme Typewise All')
