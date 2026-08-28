"""Lot No Report — w_smithjewl_lot_rep.

Generated from the PowerBuilder window ``w_smithjewl_lot_rep.srw`` by
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
    name='w_smithjewl_lot_rep',
    title='Lot No Report',
    width=3643,
    height=2248,
    controls=[],
    tables=[],
    source_path='w_smithjewl_lot_rep.srw',
    grid={'control': 'dw_accode', 'dataobject': 'd_smith', 'table': 'codehelp', 'keys': ['code'], 'columns': [{'name': 'code', 'label': 'code', 'type': 'char'}]},
    report={'dataobject': 'd_smith_lot_rep', 'sql': "SELECT clients.name AS clients_name, clients.code AS clients_code, smithm.lotno AS smithm_lotno, (select sum(smithd.netwgt) from smithd,smithm sm where sm.smithcode = clients.code and smithd.slno = sm.slno and sm.tdate >= :rdate1 and sm.tdate <= :rdate2 and sm.control <= :rlevel and smithd.givrec = 'G' and sm.lotno = smithm.lotno) as totissuewgt, (select sum(smithd.netwgt) from smithd,smithm sm where sm.smithcode = clients.code and smithd.slno = sm.slno and sm.tdate >= :rdate1 and sm.tdate <= :rdate2 and sm.control <= :rlevel and smithd.givrec = 'R' and sm.lotno = smithm.lotno) as totrcvdwgt, (select sum(smithd.qty) from smithd,smithm sm where sm.smithcode = clients.code and smithd.slno = sm.slno and sm.tdate >= :rdate1 and sm.tdate <= :rdate2 and sm.control <= :rlevel and smithd.givrec = 'G' and sm.lotno = smithm.lotno) as totissueqty, (select sum(smithd.qty) from smithd,smithm sm where sm.smithcode = clients.code and smithd.slno = sm.slno and sm.tdate >= :rdate1 and sm.tdate <= :rdate2 and sm.control <= :rlevel and smithd.givrec = 'R' and sm.lotno = smithm.lotno) as totrcvdqty FROM clients, smithm WHERE clients.code = smithm.smithcode ORDER BY clients.name ASC", 'args': ['rdate1', 'rdate2', 'rlevel'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date', 'rlevel': 'number'}, 'tables': ['clients', 'smithm'], 'columns': [{'name': 'name', 'label': 'name', 'type': 'char'}, {'name': 'code', 'label': 'code', 'type': 'char'}, {'name': 'totissuewgt', 'label': 'totissuewgt', 'type': 'decimal'}, {'name': 'smithm_lotno', 'label': 'smithm_lotno', 'type': 'char'}, {'name': 'totrcvdwgt', 'label': 'totrcvdwgt', 'type': 'decimal'}, {'name': 'totissueqty', 'label': 'totissueqty', 'type': 'long'}, {'name': 'totrcvdqty', 'label': 'totrcvdqty', 'type': 'long'}]},
    opens=['w_clientshelp'],
)


class LotNoReportForm(GeneratedForm):
    """Lot No Report"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 384, 0, 448, 100, taborder=10)
        self.add('editmask', 'em_date2', 1134, 0, 448, 100, taborder=20)
        self.add('commandbutton', 'cb_show', 2528, 0, 279, 100, text='&Show', taborder=40)
        self.add('commandbutton', 'cb_3', 2816, 0, 256, 100, text='Save &As', taborder=80)
        self.add('commandbutton', 'cb_1', 3077, 0, 265, 100, text='&Print', taborder=70)
        self.add('commandbutton', 'cb_2', 3342, 0, 265, 100, text='E&xit', taborder=60)
        self.add('datawindow', 'dw_accode', 1993, 4, 434, 92, dataobject='d_smith', taborder=30)
        self.add('statictext', 'st_1', 5, 16, 366, 64, text='Date From :')
        self.add('statictext', 'st_2', 846, 16, 283, 72, text='Date To :')
        self.add('statictext', 'st_type', 1609, 16, 375, 72, text='Smith/Jewl :')
        self.add('datawindow', 'dw_1', 0, 116, 3611, 1972, dataobject='d_smith_lot_rep', taborder=50)
