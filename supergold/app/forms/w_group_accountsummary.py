"""Group A/c Summary — w_group_accountsummary.

Generated from the PowerBuilder window ``w_group_accountsummary.srw`` by
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
    name='w_group_accountsummary',
    title='Group A/c Summary',
    width=3680,
    height=2324,
    controls=[],
    tables=['accountm', 'daybook', 'accountg'],
    source_path='w_group_accountsummary.srw',
    report={'dataobject': 'd_group_accountsummary_sundbcr', 'sql': 'SELECT accountm.accode AS accountm_accode, clients.name AS clients_name, clients.addr1 AS clients_addr1, clients.addr2 AS clients_addr2, clients.addr3 AS clients_addr3, clients.city AS clients_city, accountm.opbal AS accountm_opbal, accountm.opbalb AS accountm_opbalb, accountm.actype2 AS accountm_actype2, clients.telephone AS clients_telephone, clients.cocode AS clients_cocode, clients.grp AS clients_grp, accountm.name AS accountm_name, accountm.clbal AS accountm_clbal, accountm.amount AS accountm_amount, (select sum(daybook.amount) from daybook where accountm.accode = daybook.accode and daybook.control <= :rlevel and daybook.tdate >= :rdate and daybook.tdate <= :rdate2) as ttran FROM accountm, clients WHERE accountm.accode = clients.code AND accountm.control <= :rlevel ORDER BY clients.name ASC', 'args': ['rdate', 'rdate2', 'rlevel', 'rgrp', 'rgrpname'], 'arg_types': {'rdate': 'date', 'rdate2': 'date', 'rlevel': 'number', 'rgrp': 'string', 'rgrpname': 'string'}, 'tables': ['accountm', 'clients'], 'columns': [{'name': 'accountm_accode', 'label': 'accountm_accode', 'type': 'char'}, {'name': 'clients_name', 'label': 'clients_name', 'type': 'char'}, {'name': 'clients_addr1', 'label': 'clients_addr1', 'type': 'char'}, {'name': 'clients_addr2', 'label': 'clients_addr2', 'type': 'char'}, {'name': 'clients_addr3', 'label': 'clients_addr3', 'type': 'char'}, {'name': 'clients_city', 'label': 'clients_city', 'type': 'char'}, {'name': 'accountm_opbal', 'label': 'accountm_opbal', 'type': 'decimal'}, {'name': 'accountm_opbalb', 'label': 'accountm_opbalb', 'type': 'decimal'}, {'name': 'accountm_actype2', 'label': 'accountm_actype2', 'type': 'char'}, {'name': 'clients_telephone', 'label': 'clients_telephone', 'type': 'char'}, {'name': 'clients_cocode', 'label': 'clients_cocode', 'type': 'char'}, {'name': 'clients_grp', 'label': 'clients_grp', 'type': 'char'}, {'name': 'accountm_name', 'label': 'accountm_name', 'type': 'char'}, {'name': 'accountm_clbal', 'label': 'accountm_clbal', 'type': 'decimal'}, {'name': 'accountm_amount', 'label': 'accountm_amount', 'type': 'decimal'}, {'name': 'cttran', 'label': 'cttran', 'type': 'decimal'}]},
    opens=['w_acledgerpopup'],
)


class GroupACSummaryForm(GeneratedForm):
    """Group A/c Summary"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date', 224, 0, 398, 88, taborder=10)
        self.add('statictext', 'st_date2', 635, 0, 128, 76, text='To :')
        self.add('editmask', 'em_date2', 773, 0, 398, 88, taborder=20)
        self.add('datawindow', 'dw_grp', 1449, 0, 1129, 96, dataobject='d_grcode', taborder=60)
        self.add('commandbutton', 'cb_show', 2606, 0, 270, 92, text='&Show', taborder=30)
        self.add('commandbutton', 'cb_3', 2885, 0, 256, 92, text='Save &As', taborder=80)
        self.add('commandbutton', 'cb_1', 3150, 0, 238, 92, text='&Print', taborder=100)
        self.add('commandbutton', 'cb_2', 3387, 0, 238, 92, text='E&xit', taborder=90)
        self.add('statictext', 'st_date1', 14, 4, 206, 76, text='From :')
        self.add('statictext', 'st_2', 1189, 8, 247, 76, text='Group :')
        self.add('dropdownlistbox', 'ddlb_type', 224, 92, 942, 804, text='With Balance or Transactions', items=['All', 'Receivable Only', 'Payable Only', 'With Balance Only', 'With Term Transaction', 'With Balance or Transactions'], taborder=40)
        self.add('dropdownlistbox', 'ddlb_sort', 1449, 100, 576, 456, text='A/c Name', items=['A/c Name', 'A/c Code', 'Balance'], taborder=70)
        self.add('checkbox', 'cbx_speed', 3150, 100, 393, 76, text='Speed Print')
        self.add('statictext', 'st_1', 23, 108, 197, 68, text='Type :')
        self.add('statictext', 'st_3', 1161, 108, 274, 76, text='Sort On :')
        self.add('checkbox', 'cbx_relativetoob', 2112, 108, 521, 80, text='Relative to OB')
        self.add('datawindow', 'dw_1', 0, 196, 3657, 2004, dataobject='d_group_accountsummary_sundbcr', taborder=50)
