"""Details — w_smithwasummary2.

Generated from the PowerBuilder window ``w_smithwasummary2.srw`` by
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
    name='w_smithwasummary2',
    title='Details',
    width=3639,
    height=2200,
    controls=[],
    tables=[],
    source_path='w_smithwasummary2.srw',
    report={'dataobject': 'd_smithwasummary2', 'sql': "SELECT clients.code AS clients_code, clients.name AS clients_name, clientsgs.opweight AS clientsgs_opweight, clientsgs.opweightb AS clientsgs_opweightb, clients.opbalance AS clients_opbalance, clients.opbalanceb AS clients_opbalanceb, clients.grp AS clients_grp, (select sum(daybook.amount) from daybook where clients.code = daybook.accode  and daybook.control <= :rlevel and daybook.tdate <= :rdate2 ) as ttranamt, (select sum(daybook.amount) from daybook where clients.code = daybook.accode  and daybook.control <= :rlevel and daybook.tdate < :rdate1 ) as ttranamtop, (select sum(abs(daybook.amount)) from daybook where clients.code = daybook.accode  and daybook.control <= :rlevel and daybook.tdate >= :rdate1 and daybook.tdate <= :rdate2 and daybook.amount < 0 ) as ttranamtdb, (select sum(daybook.amount) from daybook where clients.code = daybook.accode  and daybook.control <= :rlevel and daybook.tdate >= :rdate1 and daybook.tdate <= :rdate2 and daybook.amount > 0 ) as ttranamtcr, (select sum(smithd.netwgt) from smithd,smithm where smithm.slno = smithd.slno and clients.code = smithm.smithcode and smithd.givrec = 'R' and smithm.control <= :rlevel and smithm.tdate < :rdate1) as trcvdwgtop, (select sum(smithd.netwgt) from smithd,smithm where smithm.slno = smithd.slno and clients.code = smithm.smithcode and smithd.givrec = 'G' and smithm.control <= :rlevel and smithm.tdate <= :rdate2) as tissuedwgtcl, (select sum(smithd.netwgt) from smithd,smithm where smithm.slno = smithd.slno and clients.code = smithm.smithcode and smithd.givrec = 'G' and smithm.control <= :rlevel and smithm.tdate < :rdate1) as tissuedwgtop, (select sum(smithd.netwgt) from smithd,smithm where smithm.slno = smithd.slno and clients.code = smithm.smithcode and smithd.givrec = 'R' and smithm.control <= :rlevel and smithm.tdate <= :rdate2) as trcvdwgtcl, (select sum(smithd.netwgt ) from smithd,smithm where smithm.slno = smithd.slno and clients.code = smithm.smithcode and smithd.givrec = 'G' and smithm.control <= :rlevel and smithm.tdate >= :rdate1 and smithm.tdate <= :rdate2) as tissuedwgt, (select sum(smithd.netwgt ) from smithd,smithm where smithm.slno = smithd.slno and clients.code = smithm.smithcode and smithd.givrec = 'R' and smithm.control <= :rlevel and smithm.tdate >= :rdate1 and smithm.tdate <= :rdate2) as trcvdwgt FROM clients, clientsgs WHERE clients.code = clientsgs.code AND clients.ctype = :rtype ORDER BY clients.name ASC", 'args': ['rlevel', 'rdate1', 'rdate2', 'rtype', 'rmethod'], 'arg_types': {'rlevel': 'number', 'rdate1': 'date', 'rdate2': 'date', 'rtype': 'string', 'rmethod': 'string'}, 'tables': ['clients', 'clientsgs'], 'columns': [{'name': 'clients_code', 'label': 'clients_code', 'type': 'char'}, {'name': 'clients_name', 'label': 'clients_name', 'type': 'char'}, {'name': 'clientsgs_opweight', 'label': 'clientsgs_opweight', 'type': 'decimal'}, {'name': 'clientsgs_opweightb', 'label': 'clientsgs_opweightb', 'type': 'decimal'}, {'name': 'clients_opbalance', 'label': 'clients_opbalance', 'type': 'decimal'}, {'name': 'clients_opbalanceb', 'label': 'clients_opbalanceb', 'type': 'decimal'}, {'name': 'cttranamt', 'label': 'cttranamt', 'type': 'decimal'}, {'name': 'cttranamtop', 'label': 'cttranamtop', 'type': 'decimal'}, {'name': 'cttranamtdb', 'label': 'cttranamtdb', 'type': 'decimal'}, {'name': 'cttranamtcr', 'label': 'cttranamtcr', 'type': 'decimal'}, {'name': 'ctrcvdwgtop', 'label': 'ctrcvdwgtop', 'type': 'decimal'}, {'name': 'ctissuedwgtcl', 'label': 'ctissuedwgtcl', 'type': 'decimal'}, {'name': 'ctissuedwgtop', 'label': 'ctissuedwgtop', 'type': 'decimal'}, {'name': 'ctrcvdwgtcl', 'label': 'ctrcvdwgtcl', 'type': 'decimal'}, {'name': 'ctissuedwgt', 'label': 'ctissuedwgt', 'type': 'decimal'}, {'name': 'ctrcvdwgt', 'label': 'ctrcvdwgt', 'type': 'decimal'}, {'name': 'clients_grp', 'label': 'clients_grp', 'type': 'char'}]},
)


class DetailsForm(GeneratedForm):
    """Details"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 238, 0, 352, 88, taborder=10)
        self.add('editmask', 'em_date2', 768, 0, 352, 88, taborder=20)
        self.add('commandbutton', 'cb_show', 1874, 0, 261, 92, text='&Show', taborder=30)
        self.add('dropdownlistbox', 'ddlb_wgtstatus', 2190, 0, 517, 516, text='All', items=['All', 'Only To Get', 'Only To Give', 'Only With Bal'], taborder=80)
        self.add('commandbutton', 'cb_3', 2843, 0, 251, 96, text='Save &As', taborder=40)
        self.add('commandbutton', 'cb_1', 3104, 0, 238, 92, text='&Print', taborder=70)
        self.add('commandbutton', 'cb_2', 3346, 0, 238, 92, text='E&xit', taborder=60)
        self.add('statictext', 'st_1', 18, 8, 210, 76, text='From :')
        self.add('statictext', 'st_2', 613, 8, 146, 76, text='To :')
        self.add('checkbox', 'cbx_iwgtclbal', 1211, 8, 590, 80, text='Based Issu.wgt.Cl.Bal')
        self.add('datawindow', 'dw_grp', 238, 96, 677, 88, dataobject='d_clientsgrp_code', taborder=60)
        self.add('dropdownlistbox', 'ddlb_sort', 2190, 96, 667, 508, text='Name', items=['Name', 'Code', 'Weight Bal', 'Amount Bal', 'Issued Wgt', 'Rcvd Wgt'], taborder=50)
        self.add('statictext', 'st_grp', 5, 104, 224, 76, text='Group :')
        self.add('checkbox', 'cbx_grp', 919, 104, 82, 76)
        self.add('statictext', 'st_3', 1989, 108, 192, 64, text='Sort :')
        self.add('datawindow', 'dw_1', 0, 196, 3611, 1896, dataobject='d_smithwasummary2', taborder=50)
