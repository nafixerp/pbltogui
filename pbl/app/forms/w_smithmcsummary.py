"""Smith Trans Summary — w_smithmcsummary.

Generated from the PowerBuilder window ``w_smithmcsummary.srw`` by
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
    name='w_smithmcsummary',
    title='Smith Trans Summary',
    width=3621,
    height=2244,
    controls=[],
    tables=[],
    source_path='w_smithmcsummary.srw',
    report={'dataobject': 'd_smithmcsummary', 'sql': "SELECT clients.code AS clients_code, clients.name AS clients_name, clientsgs.opweight AS clientsgs_opweight, clientsgs.opweightb AS clientsgs_opweightb, clients.opbalance AS clients_opbalance, clients.opbalanceb AS clients_opbalanceb, (select sum(smithd.netwgt) from smithd,smithm where smithm.slno = smithd.slno and clients.code = smithm.smithcode and smithd.givrec = 'G' and smithm.control <= :rlevel) as tissuedwgt, (select sum(daybook.amount) from daybook where clients.code = daybook.accode  and daybook.control <= :rlevel) as ttranamt, (select sum(smithd.netwgt) from smithd,smithm where smithm.slno = smithd.slno and clients.code = smithm.smithcode and smithd.givrec = 'G' and smithm.control <= :rlevel and smithm.tdate >= :rdate1 and smithm.tdate <= :rdate2) as tissuedwgt1, (select sum(daybook.amount) from daybook where clients.code = daybook.accode  and daybook.control <= :rlevel and daybook.amount < 0 and daybook.tdate >= :rdate1 and daybook.tdate <= :rdate2) as tissuedamt1, (select sum( smithd.wastage) from smithd,smithm where smithm.slno = smithd.slno and clients.code = smithm.smithcode and smithd.givrec = 'R' and smithm.control <= :rlevel and smithm.tdate >= :rdate1 and smithm.tdate <= :rdate2) as twastage1, (select sum(smithd.mcharge) from smithd,smithm where smithd.slno = smithm.slno and clients.code = smithm.smithcode and smithm.control <= :rlevel and smithm.tdate >= :rdate1 and smithm.tdate <= :rdate2) as tmcharge1, (select sum(smithm.pamt) from smithm where clients.code = smithm.smithcode and smithm.control <= :rlevel and smithm.tdate >= :rdate1 and smithm.tdate <= :rdate2) as tmcpaid1, (select sum(smithd.stoneprice) from smithd,smithm where smithd.slno = smithm.slno and clients.code = smithm.smithcode and smithm.control <= :rlevel and smithm.tdate >= :rdate1 and smithm.tdate <= :rdate2) as tstamt, (select sum(smithd.netwgt) from smithd,smithm where smithm.slno = smithd.slno and clients.code = smithm.smithcode and smithd.givrec = 'R' and smithm.control <= :rlevel) as trcvdwgt, (select sum(smithd.netwgt) from smithd,smithm where smithm.slno = smithd.slno and clients.code = smithm.smithcode and smithd.givrec = 'R' and smithm.control <= :rlevel and smithm.tdate >= :rdate1 and smithm.tdate <= :rdate2) as trcvdwgt1 FROM clients, clientsgs WHERE clients.code = clientsgs.code AND clients.ctype = :rtype ORDER BY clients.name ASC", 'computes': [{'name': 'compute_6', 'expression': ' ctrcvdwgt1 ', 'format': '#####0.000', 'label': 'compute_6', 'band': 'detail'}, {'name': 'compute_5', 'expression': ' ctwastage1 ', 'format': '#####0.000', 'label': 'compute_5', 'band': 'detail'}, {'name': 'compute_4', 'expression': ' ctmcharge1 ', 'format': '#####0.00', 'label': 'compute_4', 'band': 'detail'}, {'name': 'totpaid', 'expression': 'if(isnull(ctissuedamt1),0,abs( ctissuedamt1) )', 'format': '#####0.00', 'label': 'totpaid', 'band': 'detail'}, {'name': 'compute_7', 'expression': ' ctissuedwgt1 ', 'format': '#####0.000', 'label': 'compute_7', 'band': 'detail'}, {'name': 'totamt', 'expression': 'if(isnull( ctmcharge1 ),0,ctmcharge1) +  if(isnull(ctstamt ),0,ctstamt)', 'format': '########0.00', 'label': 'totamt', 'band': 'detail'}, {'name': 'tottran', 'expression': 'if(isnull( ctrcvdwgt1),0,ctrcvdwgt1 ) + if(isnull( ctissuedwgt1 ),0,ctissuedwgt1 ) + totpaid', 'format': '#####0.000', 'label': 'tottran', 'band': 'detail'}, {'name': 'compute_9', 'expression': 'sum( ctrcvdwgt1  for all)', 'format': '#####0.000', 'label': 'compute_9', 'band': 'summary'}, {'name': 'compute_8', 'expression': 'sum( ctwastage1  for all)', 'format': '#####0.000', 'label': 'compute_8', 'band': 'summary'}, {'name': 'compute_14', 'expression': 'sum( ctmcharge1  for all)', 'format': '#####0.00', 'label': 'compute_14', 'band': 'summary'}, {'name': 'compute_13', 'expression': 'sum(ctstamt for all)', 'format': '#######0.00', 'label': 'compute_13', 'band': 'summary'}, {'name': 'compute_12', 'expression': 'sum(if(isnull( ctmcharge1 ),0,ctmcharge1) +  if(isnull(ctstamt ),0,ctstamt) for all)', 'format': '########0.00', 'label': 'compute_12', 'band': 'summary'}, {'name': 'compute_10', 'expression': 'sum(totpaid for all)', 'format': '#####0.00', 'label': 'compute_10', 'band': 'summary'}, {'name': 'compute_11', 'expression': 'sum( ctissuedwgt1  for all)', 'format': '#####0.000', 'label': 'compute_11', 'band': 'summary'}], 'args': ['rlevel', 'rdate1', 'rdate2', 'rtype'], 'arg_types': {'rlevel': 'number', 'rdate1': 'date', 'rdate2': 'date', 'rtype': 'string'}, 'tables': ['clients', 'clientsgs'], 'columns': [{'name': 'clients_code', 'label': 'clients_code', 'type': 'char'}, {'name': 'clients_name', 'label': 'clients_name', 'type': 'char'}, {'name': 'clientsgs_opweight', 'label': 'clientsgs_opweight', 'type': 'decimal'}, {'name': 'clientsgs_opweightb', 'label': 'clientsgs_opweightb', 'type': 'decimal'}, {'name': 'clients_opbalance', 'label': 'clients_opbalance', 'type': 'decimal'}, {'name': 'clients_opbalanceb', 'label': 'clients_opbalanceb', 'type': 'decimal'}, {'name': 'ctissuedwgt', 'label': 'ctissuedwgt', 'type': 'decimal'}, {'name': 'cttranamt', 'label': 'cttranamt', 'type': 'decimal'}, {'name': 'ctissuedwgt1', 'label': 'ctissuedwgt1', 'type': 'decimal'}, {'name': 'ctissuedamt1', 'label': 'ctissuedamt1', 'type': 'decimal'}, {'name': 'ctwastage1', 'label': 'ctwastage1', 'type': 'decimal'}, {'name': 'ctmcharge1', 'label': 'ctmcharge1', 'type': 'decimal'}, {'name': 'ctmcpaid1', 'label': 'ctmcpaid1', 'type': 'decimal'}, {'name': 'ctstamt', 'label': 'ctstamt', 'type': 'decimal'}, {'name': 'ctrcvdwgt', 'label': 'ctrcvdwgt', 'type': 'decimal'}, {'name': 'ctrcvdwgt1', 'label': 'ctrcvdwgt1', 'type': 'decimal'}]},
)


class SmithTransSummaryForm(GeneratedForm):
    """Smith Trans Summary"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('commandbutton', 'cb_3', 2167, 4, 261, 92, text='&Show', taborder=30)
        self.add('commandbutton', 'cb_4', 2798, 4, 256, 92, text='Save &As', taborder=60)
        self.add('commandbutton', 'cb_1', 3058, 4, 238, 92, text='&Print', taborder=70)
        self.add('commandbutton', 'cb_2', 3296, 4, 238, 92, text='E&xit', taborder=50)
        self.add('editmask', 'em_date1', 398, 20, 347, 84, taborder=10)
        self.add('editmask', 'em_date2', 1006, 20, 347, 84, taborder=20)
        self.add('checkbox', 'cbx_withtran', 1422, 20, 672, 80, text='With Transaction Only')
        self.add('statictext', 'st_1', 18, 28, 352, 76, text='Date From :')
        self.add('statictext', 'st_2', 837, 28, 160, 76, text='To :')
        self.add('datawindow', 'dw_1', 0, 124, 3589, 2008, dataobject='d_smithmcsummary', taborder=40)
