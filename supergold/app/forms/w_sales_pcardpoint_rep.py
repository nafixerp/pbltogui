"""Prev. Card Point Report — w_sales_pcardpoint_rep.

Generated from the PowerBuilder window ``w_sales_pcardpoint_rep.srw`` by
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
    name='w_sales_pcardpoint_rep',
    title='Prev. Card Point Report',
    width=3739,
    height=2256,
    controls=[],
    tables=['salesm', 'clients'],
    source_path='w_sales_pcardpoint_rep.srw',
    report={'dataobject': 'd_sales_pcardpointrep', 'sql': 'SELECT clients.code AS clients_code, clients.name AS clients_name, pcardtable.pcard AS pcardtable_pcard, pcardtable.isubgrp AS pcardtable_isubgrp, pcardtable.pointbasedon AS pcardtable_pointbasedon, pcardtable.valuefor1point AS pcardtable_valuefor1point, pcardtable.valueperpoint AS pcardtable_valueperpoint, pcardtable.minsalesamt AS pcardtable_minsalesamt, pcardtable.rounddown AS pcardtable_rounddown, (select pcard.name from pcard where pcard.code = clients.pcard) as pcardname, (0.0001) as swgt, (0.001) as samt, (0.001) as spoints, (0.001) as pointvalue, (select itemsubgrp.name from itemsubgrp where itemsubgrp.code = pcardtable.isubgrp) as subgrpname, (0.001) as redeem, (0.001) as oppoints, (0.001) as clpoints, (0.001) as clpointvalue FROM clients, pcardtable WHERE clients.pcard = pcardtable.pcard ORDER BY clients.name ASC, clients.code ASC, 15 ASC', 'args': ['rdate1', 'rdate2', 'rlevel', 'rccode'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date', 'rlevel': 'number', 'rccode': 'string'}, 'tables': ['clients', 'pcardtable'], 'columns': [{'name': 'clients_code', 'label': 'Code', 'type': 'char'}, {'name': 'clients_name', 'label': 'Party Name', 'type': 'char'}, {'name': 'pcardtable_pcard', 'label': 'pcardtable_pcard', 'type': 'char'}, {'name': 'pcardtable_isubgrp', 'label': 'pcardtable_isubgrp', 'type': 'char'}, {'name': 'pcardtable_pointbasedon', 'label': 'Point Based On', 'type': 'char'}, {'name': 'pcardtable_valuefor1point', 'label': 'pcardtable_valuefor1point', 'type': 'decimal'}, {'name': 'pcardtable_valueperpoint', 'label': 'pcardtable_valueperpoint', 'type': 'decimal'}, {'name': 'pcardtable_minsalesamt', 'label': 'pcardtable_minsalesamt', 'type': 'decimal'}, {'name': 'pcardtable_rounddown', 'label': 'pcardtable_rounddown', 'type': 'decimal'}, {'name': 'pcardname', 'label': 'Prev. Card', 'type': 'char'}, {'name': 'swgt', 'label': 'Sales Wgt', 'type': 'decimal'}, {'name': 'samt', 'label': 'Sales Amt', 'type': 'decimal'}, {'name': 'spoints', 'label': 'Sales Points', 'type': 'decimal'}, {'name': 'pointvalue', 'label': 'Point Value', 'type': 'decimal'}, {'name': 'subgrpname', 'label': 'Item Sub Grp', 'type': 'char'}, {'name': 'redeem', 'label': 'Redeemed Points', 'type': 'decimal'}, {'name': 'oppoints', 'label': 'Opening Points', 'type': 'decimal'}, {'name': 'clpoints', 'label': 'Closing Points', 'type': 'decimal'}, {'name': 'clpointvalue', 'label': 'Cl Point Value', 'type': 'decimal'}]},
)


class PrevCardPointReportForm(GeneratedForm):
    """Prev. Card Point Report"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 206, 0, 430, 92, taborder=10)
        self.add('editmask', 'em_date2', 859, 0, 430, 92, taborder=20)
        self.add('datawindow', 'dw_custcode', 1536, 0, 402, 88, dataobject='d_cust', taborder=41)
        self.add('commandbutton', 'cb_show', 2158, 0, 293, 96, text='&Show', taborder=30)
        self.add('commandbutton', 'cb_sort', 2469, 0, 247, 92, text='So&rt', taborder=31)
        self.add('commandbutton', 'cb_1', 2747, 0, 270, 92, text='Save &As', taborder=70)
        self.add('commandbutton', 'cb_print', 3022, 0, 233, 92, text='&Print', taborder=50)
        self.add('commandbutton', 'cb_exit', 3259, 0, 233, 92, text='E&xit', taborder=60)
        self.add('statictext', 'st_1', 1321, 4, 201, 72, text='Party :')
        self.add('statictext', 'st_10', 0, 12, 197, 64, text='From :')
        self.add('statictext', 'st_11', 718, 12, 133, 72, text='To :')
        self.add('datawindow', 'dw_saleregister', 0, 96, 3721, 2032, dataobject='d_sales_pcardpointrep', taborder=40)
