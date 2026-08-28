"""Fix/Unfix Report — w_smithjewl_fixunfix_rep.

Generated from the PowerBuilder window ``w_smithjewl_fixunfix_rep.srw`` by
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
    name='w_smithjewl_fixunfix_rep',
    title='Fix/Unfix Report',
    width=3643,
    height=2248,
    controls=[],
    tables=[],
    source_path='w_smithjewl_fixunfix_rep.srw',
    grid={'control': 'dw_accode', 'dataobject': 'd_smith', 'table': 'codehelp', 'keys': ['code'], 'computes': [], 'columns': [{'name': 'code', 'label': 'code', 'type': 'char'}]},
    report={'dataobject': 'd_smith_fixunfix_rep', 'sql': "SELECT clients.name AS clients_name, clients.code AS clients_code, smithm.lotno AS smithm_lotno, smithm.docno AS smithm_docno, smithm.tdate AS smithm_tdate, smithm.duedate AS smithm_duedate, (select sum(smithd.netwgt) from smithd where smithd.slno = smithm.slno and smithd.givrec = 'G') as totissuewgt, (select sum(smithd.netwgt) from smithd where smithd.slno = smithm.slno and smithd.givrec = 'R') as totrcvdwgt, (select sum(smithd.netwgt) from smithd,smithm sm where smithd.slno = sm.slno and sm.refno = smithm.docno and sm.control <= :rlevel) as totadjstdwgt FROM clients, smithm WHERE clients.code = smithm.smithcode ORDER BY clients.name ASC, smithm.tdate ASC, smithm.docno ASC", 'computes': [{'name': 'pendwgt', 'expression': 'abs( if(isnull( totissuewgt ), 0, totissuewgt)  -  if(isnull( totrcvdwgt ),0,totrcvdwgt)) - if(isnull( totadjstdwgt ),0,totadjstdwgt)', 'format': '######0.000', 'label': 'pendwgt', 'band': 'detail'}, {'name': 'compute_4', 'expression': ' sum(totrcvdwgt for all) ', 'format': '######0.000', 'label': 'compute_4', 'band': 'summary'}, {'name': 'compute_8', 'expression': ' sum(totissuewgt for all)', 'format': '#######0.000', 'label': 'compute_8', 'band': 'summary'}, {'name': 'compute_5', 'expression': 'sum(totadjstdwgt for all)', 'format': '########0.000', 'label': 'compute_5', 'band': 'summary'}, {'name': 'compute_7', 'expression': 'sum( pendwgt for all)', 'format': '######0.000', 'label': 'compute_7', 'band': 'summary'}], 'args': ['rdate1', 'rdate2', 'rlevel'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date', 'rlevel': 'number'}, 'tables': ['clients', 'smithm'], 'columns': [{'name': 'name', 'label': 'name', 'type': 'char'}, {'name': 'code', 'label': 'code', 'type': 'char'}, {'name': 'smithm_lotno', 'label': 'smithm_lotno', 'type': 'char'}, {'name': 'smithm_docno', 'label': 'smithm_docno', 'type': 'char'}, {'name': 'smithm_tdate', 'label': 'smithm_tdate', 'type': 'date'}, {'name': 'smithm_duedate', 'label': 'smithm_duedate', 'type': 'date'}, {'name': 'totissuewgt', 'label': 'totissuewgt', 'type': 'decimal'}, {'name': 'totrcvdwgt', 'label': 'totrcvdwgt', 'type': 'decimal'}, {'name': 'totadjstdwgt', 'label': 'totadjstdwgt', 'type': 'decimal'}]},
    opens=['w_clientshelp'],
)


class FixUnfixReportForm(GeneratedForm):
    """Fix/Unfix Report"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 251, 0, 512, 100, taborder=10)
        self.add('editmask', 'em_date2', 997, 0, 512, 100, taborder=20)
        self.add('commandbutton', 'cb_show', 2528, 0, 279, 100, text='&Show', taborder=40)
        self.add('commandbutton', 'cb_3', 2816, 0, 256, 100, text='Save &As', taborder=80)
        self.add('commandbutton', 'cb_1', 3077, 0, 265, 100, text='&Print', taborder=70)
        self.add('commandbutton', 'cb_2', 3342, 0, 265, 100, text='E&xit', taborder=60)
        self.add('datawindow', 'dw_accode', 1993, 4, 434, 92, dataobject='d_smith', taborder=30)
        self.add('statictext', 'st_1', 5, 16, 238, 68, text='From :')
        self.add('statictext', 'st_2', 846, 16, 137, 72, text='To :')
        self.add('statictext', 'st_type', 1609, 16, 375, 72, text='Smith/Jewl :')
        self.add('dropdownlistbox', 'ddlb_type', 251, 104, 512, 400, text='All', items=['All', 'Receivable', 'Payable'], taborder=40)
        self.add('statictext', 'st_3', 0, 112, 242, 72, text='Type :')
        self.add('datawindow', 'dw_1', 0, 200, 3611, 1896, dataobject='d_smith_fixunfix_rep', taborder=50)
