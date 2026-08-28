"""Simple — w_smithwasummary.

Generated from the PowerBuilder window ``w_smithwasummary.srw`` by
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
    name='w_smithwasummary',
    title='Simple',
    width=3630,
    height=2228,
    controls=[],
    tables=[],
    source_path='w_smithwasummary.srw',
    report={'dataobject': 'd_smithwasummary', 'sql': "SELECT clients.code AS clients_code, clients.name AS clients_name, clientsgs.opweight AS clientsgs_opweight, clientsgs.opweightb AS clientsgs_opweightb, clients.opbalance AS clients_opbalance, clients.opbalanceb AS clients_opbalanceb, clients.grp AS clients_grp, clientsgs.stocktouch AS clientsgs_stocktouch, clientsgs.silver AS clientsgs_silver, (select sum(daybook.amount) from daybook where clients.code = daybook.accode  and daybook.control <= :rlevel and daybook.tdate <= :rdate) as ttranamt, (select sum(smithd.netwgt) from smithd,smithm where smithm.slno = smithd.slno and clients.code = smithm.smithcode and smithd.givrec = 'R' and smithm.control <= :rlevel and smithm.tdate <= :rdate) as trcvdwgt, (select sum(smithd.netwgt) from smithd,smithm where smithm.slno = smithd.slno and clients.code = smithm.smithcode and smithd.givrec = 'G' and smithm.control <= :rlevel and smithm.tdate <= :rdate) as tissuedwgt, (select max(smithm.tdate) from smithm,smithd where smithm.smithcode = clients.code and smithd.slno = smithm.slno and smithd.givrec = 'G' and smithm.control <= :rlevel and smithm.tdate <= :rdate) as lastdt, (select sum(smithd.actwgt) from smithd,smithm where smithm.slno = smithd.slno and clients.code = smithm.smithcode and smithd.givrec = 'R' and smithm.control <= :rlevel and smithm.tdate <= :rdate) as trcvdwgtact, (select sum(smithd.actwgt) from smithd,smithm where smithm.slno = smithd.slno and clients.code = smithm.smithcode and smithd.givrec = 'G' and smithm.control <= :rlevel and smithm.tdate <= :rdate) as tissuedwgtact FROM clients, clientsgs WHERE clients.code = clientsgs.code AND clients.ctype = ifnull( :rsjtype, clients.ctype, :rsjtype) ORDER BY clients.name ASC", 'args': ['rlevel', 'rdate', 'rsjtype', 'rtype', 'rtouch', 'rrate'], 'arg_types': {'rlevel': 'number', 'rdate': 'date', 'rsjtype': 'string', 'rtype': 'string', 'rtouch': 'decimal', 'rrate': 'decimal'}, 'tables': ['clients', 'clientsgs'], 'columns': [{'name': 'clients_code', 'label': 'clients_code', 'type': 'char'}, {'name': 'clients_name', 'label': 'clients_name', 'type': 'char'}, {'name': 'clientsgs_opweight', 'label': 'clientsgs_opweight', 'type': 'decimal'}, {'name': 'clientsgs_opweightb', 'label': 'clientsgs_opweightb', 'type': 'decimal'}, {'name': 'clients_opbalance', 'label': 'clients_opbalance', 'type': 'decimal'}, {'name': 'clients_opbalanceb', 'label': 'clients_opbalanceb', 'type': 'decimal'}, {'name': 'cttranamt', 'label': 'cttranamt', 'type': 'decimal'}, {'name': 'clients_grp', 'label': 'clients_grp', 'type': 'char'}, {'name': 'ctrcvdwgt', 'label': 'ctrcvdwgt', 'type': 'decimal'}, {'name': 'ctissuedwgt', 'label': 'ctissuedwgt', 'type': 'decimal'}, {'name': 'lastdt', 'label': 'lastdt', 'type': 'date'}, {'name': 'clientsgs_stocktouch', 'label': 'clientsgs_stocktouch', 'type': 'decimal'}, {'name': 'trcvdwgtact', 'label': 'trcvdwgtact', 'type': 'decimal'}, {'name': 'tissuedwgtact', 'label': 'tissuedwgtact', 'type': 'decimal'}, {'name': 'clientsgs_silver', 'label': 'clientsgs_silver', 'type': 'char'}]},
)


class SimpleForm(GeneratedForm):
    """Simple"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('dropdownlistbox', 'ddlb_wgtstatus', 718, 0, 443, 440, text='All', items=['All', 'Only To Get', 'Only To Give'], taborder=20)
        self.add('commandbutton', 'cb_show', 2217, 0, 251, 96, text='Show', taborder=30)
        self.add('commandbutton', 'cb_3', 2482, 0, 251, 96, text='Save &As', taborder=80)
        self.add('commandbutton', 'cb_sort', 2811, 0, 251, 96, text='Sort', taborder=70)
        self.add('commandbutton', 'cb_1', 3077, 0, 251, 92, text='&Print', taborder=40)
        self.add('commandbutton', 'cb_2', 3342, 0, 251, 92, text='E&xit', taborder=70)
        self.add('editmask', 'em_date', 215, 4, 498, 92, taborder=10)
        self.add('datawindow', 'dw_grp', 1417, 4, 677, 88, dataobject='d_clientsgrp_code', taborder=60)
        self.add('statictext', 'st_1', 0, 12, 210, 76, text='Up to')
        self.add('statictext', 'st_grp', 1189, 12, 224, 76, text='Group :')
        self.add('checkbox', 'cbx_grp', 2098, 12, 82, 76)
        self.add('dropdownlistbox', 'ddlb_type', 1417, 96, 677, 508, text='Gold', items=['Gold', 'Silver'], taborder=60)
        self.add('editmask', 'em_commntouch', 2217, 96, 247, 88, text='none', taborder=70)
        self.add('dropdownlistbox', 'ddlb_ctype', 210, 100, 507, 440, text='All', items=['Smith Only', 'Jewellery Only', 'All'], taborder=10)
        self.add('checkbox', 'cbx_speed', 3191, 100, 402, 68, text='Speed Print')
        self.add('statictext', 'st_3', 1189, 104, 224, 76, text='Type :')
        self.add('checkbox', 'cbx_condense', 2811, 104, 315, 68, text='Condense')
        self.add('statictext', 'st_4', 0, 108, 210, 84, text='CType')
        self.add('dropdownlistbox', 'ddlb_sort', 2811, 176, 750, 508, text='Name', items=['Name', 'Code', 'Last Issued Dt', 'Weight Bal', 'Amount Bal'], taborder=80)
        self.add('checkbox', 'cbx_amttowgt', 2217, 188, 357, 76, text='Amt To Wgt')
        self.add('statictext', 'st_2', 2610, 192, 192, 64, text='Sort :')
        self.add('checkbox', 'cbx_tocommntouch', 1413, 196, 489, 68, text='To Common Touch')
        self.add('checkbox', 'cbx_withbalonly', 206, 204, 786, 68, text='With wgt/amt balance only')
        self.add('datawindow', 'dw_1', 0, 272, 3598, 1964, dataobject='d_smithwasummary', taborder=50)
