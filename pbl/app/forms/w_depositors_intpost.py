"""Interest Posting — w_depositors_intpost.

Generated from the PowerBuilder window ``w_depositors_intpost.srw`` by
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
    name='w_depositors_intpost',
    title='Interest Posting',
    width=2528,
    height=1776,
    controls=[],
    tables=['daybook', 'smithm', 'smithd', 'sman', 'clients', 'generali', 'daybookpart'],
    source_path='w_depositors_intpost.srw',
    grid={'control': 'dw_dim', 'dataobject': 'd_depositors_intpost', 'table': 'clients', 'keys': ['code'], 'columns': [{'name': 'code', 'label': 'Party', 'type': 'char'}, {'name': 'name', 'label': 'name', 'type': 'char'}, {'name': 'intamt', 'label': 'intamt', 'type': 'decimal'}, {'name': 'intwgt', 'label': 'intwgt', 'type': 'decimal'}, {'name': 'sel', 'label': 'sel', 'type': 'long'}]},
    report={'dataobject': 'd_depositors_intpost', 'sql': 'SELECT clients.code AS clients_code, clients.name AS clients_name, (select clientsgs.intamt from clientsgs where clientsgs.code = clients.code) as intamt, (select clientsgs.intwgt from clientsgs where clientsgs.code = clients.code) as intwgt, (1) as sel FROM clients WHERE intwgt > 0 OR intamt > 0 ORDER BY clients.name ASC', 'args': ['rdate', 'rlevel'], 'arg_types': {'rdate': 'date', 'rlevel': 'number'}, 'tables': ['clients'], 'columns': [{'name': 'code', 'label': 'Party', 'type': 'char'}, {'name': 'name', 'label': 'name', 'type': 'char'}, {'name': 'intamt', 'label': 'intamt', 'type': 'decimal'}, {'name': 'intwgt', 'label': 'intwgt', 'type': 'decimal'}, {'name': 'sel', 'label': 'sel', 'type': 'long'}]},
    opens=['w_clientshelp'],
)


class InterestPostingForm(GeneratedForm):
    """Interest Posting"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date', 238, 0, 466, 100, taborder=10)
        self.add('datawindow', 'dw_smcode', 937, 0, 677, 88, dataobject='d_smancode', taborder=20)
        self.add('commandbutton', 'cb_show', 1655, 0, 329, 104, text='Show', taborder=30)
        self.add('commandbutton', 'cb_edit', 2011, 0, 343, 100, text='&Edit')
        self.add('statictext', 'st_10', 50, 8, 210, 76, text='Date')
        self.add('statictext', 'st_50', 722, 12, 178, 76, text='Staff')
        self.add('datawindow', 'dw_dim', 37, 120, 2459, 1388, dataobject='d_depositors_intpost', taborder=20)
        self.add('statictext', 'st_woodqbic', 2395, 1092, 82, 76)
        self.add('statictext', 'st_others', 2249, 1096, 119, 76)
        self.add('commandbutton', 'cb_ad', 55, 1424, 206, 76, text='&Add', taborder=50)
        self.add('commandbutton', 'cb_del', 265, 1424, 215, 76, text='&Delete', taborder=60)
        self.add('roundrectangle', 'rr_1', 910, 1520, 699, 144)
        self.add('commandbutton', 'cb_save', 983, 1544, 279, 92, text='&Save', taborder=30)
        self.add('commandbutton', 'cb_exit', 1271, 1544, 279, 92, text='E&xit', taborder=40)
        self.add('checkbox', 'cbx_fr', 256, 1548, 183, 80, text='Fr')
