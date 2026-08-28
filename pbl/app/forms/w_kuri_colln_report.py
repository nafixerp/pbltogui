"""Collection Report — w_kuri_colln_report.

Generated from the PowerBuilder window ``w_kuri_colln_report.srw`` by
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
    name='w_kuri_colln_report',
    title='Collection Report',
    width=3657,
    height=2292,
    controls=[],
    tables=['kuricolln', 'accountm', 'clients_kuridet', 'daybook', 'here'],
    source_path='w_kuri_colln_report.srw',
    report={'dataobject': 'd_kuri_colln_report', 'sql': 'SELECT kuricolln.tdate AS kuricolln_tdate, clients.name AS clients_name, kuricolln.amount AS kuricolln_amount, kuricolln.grate AS kuricolln_grate, clients.code AS clients_code, clients.cocode AS clients_cocode, clients_kuridet.kuritype AS clients_kuridet_kuritype, clients.addr1 AS clients_addr1, clients.addr2 AS clients_addr2, clients.addr3 AS clients_addr3, clients_kuridet.finished AS clients_kuridet_finished, clients_kuridet.colnagent AS clients_kuridet_colnagent, kuricolln.rcptno AS kuricolln_rcptno, clients_kuridet.showwgtdet AS clients_kuridet_showwgtdet, clients.route AS clients_route, kuricolln.agent AS kuricolln_agent, kuricolln.slno AS kuricolln_slno, kuricolln.wgt AS kuricolln_wgt FROM kuricolln, clients, clients_kuridet WHERE kuricolln.code = clients.code AND clients.code = clients_kuridet.code ORDER BY kuricolln.tdate ASC, clients.name ASC', 'args': ['rdate1', 'rdate2', 'rlevel', 'rreqinst'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date', 'rlevel': 'number', 'rreqinst': 'number'}, 'tables': ['kuricolln', 'clients', 'clients_kuridet'], 'columns': [{'name': 'kuricolln_tdate', 'label': 'Date', 'type': 'date'}, {'name': 'clients_name', 'label': 'Name and Address', 'type': 'char'}, {'name': 'kuricolln_amount', 'label': 'Collection', 'type': 'decimal'}, {'name': 'kuricolln_grate', 'label': 'Grate', 'type': 'decimal'}, {'name': 'clients_code', 'label': 'clients_code', 'type': 'char'}, {'name': 'clients_cocode', 'label': 'clients_cocode', 'type': 'char'}, {'name': 'clients_kuridet_kuritype', 'label': 'clients_kuridet_kuritype', 'type': 'char'}, {'name': 'clients_addr1', 'label': 'clients_addr1', 'type': 'char'}, {'name': 'clients_addr2', 'label': 'clients_addr2', 'type': 'char'}, {'name': 'clients_addr3', 'label': 'clients_addr3', 'type': 'char'}, {'name': 'clients_kuridet_finished', 'label': 'clients_kuridet_finished', 'type': 'char'}, {'name': 'clients_kuridet_colnagent', 'label': 'clients_kuridet_colnagent', 'type': 'char'}, {'name': 'kuricolln_rcptno', 'label': 'kuricolln_rcptno', 'type': 'char'}, {'name': 'clients_kuridet_showwgtdet', 'label': 'clients_kuridet_showwgtdet', 'type': 'char'}, {'name': 'clients_route', 'label': 'clients_route', 'type': 'char'}, {'name': 'kuricolln_agent', 'label': 'kuricolln_agent', 'type': 'char'}, {'name': 'kuricolln_slno', 'label': 'kuricolln_slno', 'type': 'decimal'}, {'name': 'kuricolln_wgt', 'label': 'kuricolln_wgt', 'type': 'decimal'}]},
    opens=['w_cbachdhelp', 'w_clientshelp'],
)


class CollectionReportForm(GeneratedForm):
    """Collection Report"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('datawindow', 'dw_accode', 1458, 0, 1019, 92, dataobject='d_kuri_cust', taborder=30)
        self.add('commandbutton', 'cb_show', 2505, 0, 256, 92, text='&Show', taborder=140)
        self.add('checkbox', 'cbx_withbal', 2807, 0, 293, 80, text='With Bal')
        self.add('commandbutton', 'cb_print', 3113, 0, 256, 92, text='&Print', taborder=170)
        self.add('commandbutton', 'cb_exit', 3378, 0, 256, 92, text='E&xit', taborder=160)
        self.add('editmask', 'em_date1', 242, 4, 398, 92, taborder=10)
        self.add('editmask', 'em_date2', 795, 4, 393, 92, taborder=20)
        self.add('statictext', 'st_1', 14, 16, 219, 64, text='From :')
        self.add('statictext', 'st_2', 654, 16, 137, 72, text='To :')
        self.add('statictext', 'st_3', 1225, 16, 224, 72, text='Party :')
        self.add('dropdownlistbox', 'ddlb_reptype', 1458, 92, 1019, 540, text='All Collection Details', items=['All Collection Details', 'Collection Summary'], taborder=60)
        self.add('dropdownlistbox', 'ddlb_finished', 2505, 96, 603, 476, text='All', items=['All', 'Finished Only', 'Not Finished Only'], taborder=50)
        self.add('commandbutton', 'cb_1', 3378, 96, 256, 92, text='Save &As', taborder=50)
        self.add('datawindow', 'dw_co', 242, 100, 402, 88, dataobject='d_cust', taborder=40)
        self.add('statictext', 'st_4', 1047, 104, 402, 72, text='Report Type :')
        self.add('checkbox', 'cbx_dosprint', 3136, 108, 233, 68, text='Speed')
        self.add('statictext', 'st_co', 69, 112, 165, 76, text='C/o :')
        self.add('datawindow', 'dw_route', 2830, 188, 791, 88, dataobject='d_clientsroute_code', taborder=110)
        self.add('datawindow', 'dw_kuritype', 242, 192, 677, 88, dataobject='d_kuritype_code', taborder=70)
        self.add('editmask', 'em_mininstfinish', 1463, 192, 261, 92, taborder=80)
        self.add('editmask', 'em_pend', 2217, 192, 261, 92, taborder=100)
        self.add('statictext', 'st_mininstfinish', 983, 200, 466, 72, text='Min Inst.Finish :')
        self.add('statictext', 'st_7', 1778, 200, 434, 80, text='Min Inst.Pend :')
        self.add('statictext', 'st_11', 2578, 200, 242, 64, text='Route :')
        self.add('statictext', 'st_5', 0, 204, 233, 64, text='KType :')
        self.add('datawindow', 'dw_agent', 242, 284, 402, 88, dataobject='d_staffcode', taborder=90)
        self.add('dropdownlistbox', 'ddlb_sorton', 3122, 284, 512, 872, text='Date', items=['Name', 'Code', 'Inst.Finish', 'Pending', 'Date', 'Rcpt No', 'Amount', 'Balance', 'Duedate'], taborder=120)
        self.add('editmask', 'em_mininstamt', 1463, 288, 261, 92, taborder=110)
        self.add('editmask', 'em_maxinstamt', 2217, 288, 261, 92, taborder=130)
        self.add('statictext', 'st_9', 983, 292, 466, 72, text='Min Inst.Amt :')
        self.add('statictext', 'st_10', 1778, 292, 434, 80, text='Min Inst.Amt :')
        self.add('commandbutton', 'cb_activate', 2514, 292, 261, 84, text='Activate')
        self.add('statictext', 'st_8', 5, 296, 233, 72, text='C.Agent :')
        self.add('statictext', 'st_6', 2848, 296, 265, 80, text='Sort On :')
        self.add('datawindow', 'dw_1', 0, 384, 3634, 1776, dataobject='d_kuri_colln_report', taborder=150)
        self.add('commandbutton', 'cb_del', 2514, 388, 261, 72, text='Del', taborder=40)
        self.add('editmask', 'em_duedate', 3122, 392, 393, 92, taborder=30)
        self.add('statictext', 'st_12', 2743, 400, 370, 60, text='Due Dt Upto :')
