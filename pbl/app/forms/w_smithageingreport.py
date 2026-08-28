"""Ageing Report — w_smithageingreport.

Generated from the PowerBuilder window ``w_smithageingreport.srw`` by
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
    name='w_smithageingreport',
    title='Ageing Report',
    width=3657,
    height=2468,
    controls=[],
    tables=['smithd', 'smithm', 'clientsgs', 'clients'],
    source_path='w_smithageingreport.srw',
    report={'dataobject': 'd_smithageing_rcvble_report', 'sql': "SELECT clients.code AS clients_code, clients.name AS clients_name, clientsgs.opweight AS clientsgs_opweight, clientsgs.opweightb AS clientsgs_opweightb, clients.opbalance AS clients_opbalance, clients.opbalanceb AS clients_opbalanceb, clients.grp AS clients_grp, clients.ctype AS clients_ctype, (select sum(smithd.balwgt) from smithd,smithm where smithd.slno = smithm.slno and smithm.smithcode = clients.code and smithd.givrec = 'G' and smithm.tdate <= :rdate and smithm.tdate > :rdate0015 ) as bal0015, (select sum(smithd.balwgt) from smithd,smithm where smithd.slno = smithm.slno and smithm.smithcode = clients.code and smithd.givrec = 'G' and smithm.tdate <= :rdate0015 and smithm.tdate > :rdate1530 ) as bal1530, (select sum(smithd.balwgt) from smithd,smithm where smithd.slno = smithm.slno and smithm.smithcode = clients.code and smithd.givrec = 'G' and smithm.tdate <= :rdate1530 and smithm.tdate > :rdate3045 ) as bal3045, (select sum(smithd.balwgt) from smithd,smithm where smithd.slno = smithm.slno and smithm.smithcode = clients.code and smithd.givrec = 'G' and smithm.tdate <= :rdate3045 ) as bal4500, (select sum(smithd.netwgt) from smithd,smithm where smithm.slno = smithd.slno and clients.code = smithm.smithcode and smithd.givrec = 'R' and smithm.control <= :rlevel and smithm.tdate <= :rdate) as trcvdwgt, (select sum(smithd.netwgt) from smithd,smithm where smithm.slno = smithd.slno and clients.code = smithm.smithcode and smithd.givrec = 'G' and smithm.control <= :rlevel and smithm.tdate <= :rdate) as tissuedwgt FROM clients, clientsgs WHERE clients.code = clientsgs.code AND clients.ctype = 'G' ORDER BY clients.name ASC", 'computes': [{'name': 'total', 'expression': 'if(isnull( bal0015 ),0,bal0015) +  if(isnull( bal1530 ),0,bal1530) +  if(isnull( bal3045 ),0,bal3045) +  if(isnull( bal4500 ),0,bal4500)', 'format': '#######0.000', 'label': 'total', 'band': 'detail'}, {'name': 'clbal', 'expression': '(if(rlevel = 1, clientsgs_opweight,clientsgs_opweightb)  +  if(isnull(trcvdwgt),0, trcvdwgt)  -  if(isnull(tissuedwgt),0, tissuedwgt)) * -1', 'format': '########0.000', 'label': 'clbal', 'band': 'detail'}, {'name': 'compute_3', 'expression': 'sum(bal0015 for all)', 'format': '#######0.000', 'label': 'compute_3', 'band': 'summary'}, {'name': 'compute_4', 'expression': 'sum(bal1530 for all)', 'format': '#######0.000', 'label': 'compute_4', 'band': 'summary'}, {'name': 'compute_5', 'expression': 'sum(bal3045 for all)', 'format': '#######0.000', 'label': 'compute_5', 'band': 'summary'}, {'name': 'compute_6', 'expression': 'sum(bal4500 for all)', 'format': '#######0.000', 'label': 'compute_6', 'band': 'summary'}, {'name': 'compute_2', 'expression': 'sum( total for all)', 'format': '#######0.000', 'label': 'compute_2', 'band': 'summary'}, {'name': 'compute_7', 'expression': 'sum( clbal for all)', 'format': '########0.000', 'label': 'compute_7', 'band': 'summary'}], 'args': ['rlevel', 'rdate', 'rdate2', 'rdate0015', 'rdate1530', 'rdate3045', 'rdate4500'], 'arg_types': {'rlevel': 'number', 'rdate': 'date', 'rdate2': 'date', 'rdate0015': 'date', 'rdate1530': 'date', 'rdate3045': 'date', 'rdate4500': 'date'}, 'tables': ['clients', 'clientsgs'], 'columns': [{'name': 'clients_code', 'label': 'clients_code', 'type': 'char'}, {'name': 'clients_name', 'label': 'clients_name', 'type': 'char'}, {'name': 'clientsgs_opweight', 'label': 'clientsgs_opweight', 'type': 'decimal'}, {'name': 'clientsgs_opweightb', 'label': 'clientsgs_opweightb', 'type': 'decimal'}, {'name': 'clients_opbalance', 'label': 'clients_opbalance', 'type': 'decimal'}, {'name': 'clients_opbalanceb', 'label': 'clients_opbalanceb', 'type': 'decimal'}, {'name': 'clients_grp', 'label': 'clients_grp', 'type': 'char'}, {'name': 'bal0015', 'label': 'bal0015', 'type': 'decimal'}, {'name': 'bal1530', 'label': 'bal1530', 'type': 'decimal'}, {'name': 'bal3045', 'label': 'bal3045', 'type': 'decimal'}, {'name': 'bal4500', 'label': 'bal4500', 'type': 'decimal'}, {'name': 'clients_ctype', 'label': 'clients_ctype', 'type': 'char'}, {'name': 'trcvdwgt', 'label': 'trcvdwgt', 'type': 'decimal'}, {'name': 'tissuedwgt', 'label': 'tissuedwgt', 'type': 'decimal'}]},
    opens=['w_smithledger'],
)


class AgeingReportForm(GeneratedForm):
    """Ageing Report"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('commandbutton', 'cb_show', 2217, 0, 247, 96, text='Show', taborder=30)
        self.add('commandbutton', 'cb_3', 2473, 0, 270, 96, text='Save &As', taborder=80)
        self.add('commandbutton', 'cb_sort', 2752, 0, 270, 96, text='Sort', taborder=70)
        self.add('commandbutton', 'cb_1', 3026, 0, 279, 96, text='&Print', taborder=40)
        self.add('commandbutton', 'cb_2', 3310, 0, 279, 96, text='E&xit', taborder=70)
        self.add('editmask', 'em_date', 206, 4, 402, 92, taborder=10)
        self.add('datawindow', 'dw_grp', 1417, 4, 677, 88, dataobject='d_clientsgrp_code', taborder=60)
        self.add('statictext', 'st_grp', 1189, 12, 224, 76, text='Group :')
        self.add('checkbox', 'cbx_grp', 2098, 12, 82, 76)
        self.add('statictext', 'st_1', 0, 16, 206, 76, text='Up to :')
        self.add('dropdownlistbox', 'ddlb_type', 206, 100, 750, 440, text='Debtors Ageing', items=['Debtors Ageing', 'Creditors Ageing'], taborder=20)
        self.add('dropdownlistbox', 'ddlb_ctype', 1417, 100, 750, 440, text='All', items=['All', 'Jewellery Only', 'GoldSmith Only'], taborder=30)
        self.add('checkbox', 'cbx_speed', 3026, 108, 402, 72, text='Speed Print')
        self.add('datawindow', 'dw_1', 0, 200, 3598, 2128, dataobject='d_smithageing_rcvble_report', taborder=50)
