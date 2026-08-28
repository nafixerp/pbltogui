"""Profit Report — w_jewlprof_rep.

Generated from the PowerBuilder window ``w_jewlprof_rep.srw`` by
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
    name='w_jewlprof_rep',
    title='Profit Report',
    width=3643,
    height=2248,
    controls=[],
    tables=[],
    source_path='w_jewlprof_rep.srw',
    grid={'control': 'dw_1', 'dataobject': 'd_jewlprof_rep', 'table': 'clients', 'keys': ['code'], 'columns': [{'name': 'name', 'label': 'name', 'type': 'char'}, {'name': 'code', 'label': 'code', 'type': 'char'}, {'name': 'totissuewgt', 'label': 'totissuewgt', 'type': 'decimal'}, {'name': 'totissuestwgt', 'label': 'totissuestwgt', 'type': 'decimal'}, {'name': 'totjsmithmc', 'label': 'totjsmithmc', 'type': 'decimal'}, {'name': 'totjewlmc', 'label': 'totjewlmc', 'type': 'decimal'}]},
    report={'dataobject': 'd_jewlprof_rep', 'sql': "SELECT clients.name AS clients_name, clients.code AS clients_code, (select sum(smithd.weight) from smithd,smithm where smithm.smithcode = clients.code and smithd.slno = smithm.slno and smithm.tdate >= :rdate1 and smithm.tdate <= :rdate2 and smithm.control <= :rlevel and smithd.givrec = 'G') as totissuewgt, (select sum(smithd.stonewgt) from smithd,smithm where smithm.smithcode = clients.code and smithd.slno = smithm.slno and smithm.tdate >= :rdate1 and smithm.tdate <= :rdate2 and smithm.control <= :rlevel and smithd.givrec = 'G') as totissuestwgt, (select sum(smithd.smithmc) from smithd,smithm where smithm.smithcode = clients.code and smithd.slno = smithm.slno and smithm.tdate >= :rdate1 and smithm.tdate <= :rdate2 and smithm.control <= :rlevel and smithd.givrec = 'G') as totjsmithmc, (select sum(abs(smithd.mcharge)) from smithd,smithm where smithm.smithcode = clients.code and smithd.slno = smithm.slno and smithm.tdate >= :rdate1 and smithm.tdate <= :rdate2 and smithm.control <= :rlevel and smithd.givrec = 'G') as totjewlmc FROM clients ORDER BY clients.name ASC", 'args': ['rdate1', 'rdate2', 'rlevel'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date', 'rlevel': 'number'}, 'tables': ['clients'], 'columns': [{'name': 'name', 'label': 'name', 'type': 'char'}, {'name': 'code', 'label': 'code', 'type': 'char'}, {'name': 'totissuewgt', 'label': 'totissuewgt', 'type': 'decimal'}, {'name': 'totissuestwgt', 'label': 'totissuestwgt', 'type': 'decimal'}, {'name': 'totjsmithmc', 'label': 'totjsmithmc', 'type': 'decimal'}, {'name': 'totjewlmc', 'label': 'totjewlmc', 'type': 'decimal'}]},
)


class ProfitReportForm(GeneratedForm):
    """Profit Report"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 384, 0, 448, 100, taborder=10)
        self.add('editmask', 'em_date2', 1134, 0, 448, 100, taborder=20)
        self.add('commandbutton', 'cb_show', 2528, 0, 279, 100, text='&Show', taborder=40)
        self.add('commandbutton', 'cb_3', 2816, 0, 256, 100, text='Save &As', taborder=80)
        self.add('commandbutton', 'cb_1', 3077, 0, 265, 100, text='&Print', taborder=70)
        self.add('commandbutton', 'cb_2', 3342, 0, 265, 100, text='E&xit', taborder=60)
        self.add('datawindow', 'dw_accode', 1993, 4, 416, 88, dataobject='d_jewl', taborder=30)
        self.add('statictext', 'st_1', 5, 16, 366, 64, text='Date From :')
        self.add('statictext', 'st_2', 846, 16, 283, 72, text='Date To :')
        self.add('statictext', 'st_type', 1632, 16, 352, 72, text='Jewellery :')
        self.add('datawindow', 'dw_1', 0, 116, 3611, 1972, dataobject='d_jewlprof_rep', taborder=50)
