"""Interest Posting — w_kuri_intpost.

Generated from the PowerBuilder window ``w_kuri_intpost.srw`` by
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
    name='w_kuri_intpost',
    title='Interest Posting',
    width=2414,
    height=1776,
    controls=[],
    tables=['daybook', 'kuriint', 'kuricolln', 'clients_kuridet', 'clients', 'generali', 'daybookpart'],
    source_path='w_kuri_intpost.srw',
    grid={'control': 'dw_dim', 'dataobject': 'd_kuri_intpost', 'table': 'clients', 'keys': ['code'], 'columns': [{'name': 'code', 'label': 'Party', 'type': 'char'}, {'name': 'name', 'label': 'name', 'type': 'char'}, {'name': 'tcolln', 'label': 'tcolln', 'type': 'decimal'}, {'name': 'intamt', 'label': 'intamt', 'type': 'decimal'}]},
    report={'dataobject': 'd_kuri_intpost', 'sql': 'SELECT clients.code AS clients_code, clients.name AS clients_name, (select sum(kuricolln.amount) from kuricolln where kuricolln.code = clients.code and kuricolln.tdate <= :rdate and kuricolln.control <= :rlevel) as tcolln, 0.001 as intamt FROM clients', 'args': ['rdate', 'rlevel'], 'arg_types': {'rdate': 'date', 'rlevel': 'number'}, 'tables': ['clients'], 'columns': [{'name': 'code', 'label': 'Party', 'type': 'char'}, {'name': 'name', 'label': 'name', 'type': 'char'}, {'name': 'tcolln', 'label': 'tcolln', 'type': 'decimal'}, {'name': 'intamt', 'label': 'intamt', 'type': 'decimal'}]},
    opens=['w_clientshelp'],
)


class InterestPostingForm(GeneratedForm):
    """Interest Posting"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date', 261, 0, 434, 100, taborder=10)
        self.add('commandbutton', 'cb_show', 1449, 0, 370, 100, text='&Calculate', taborder=11)
        self.add('commandbutton', 'cb_edit', 1966, 0, 343, 100, text='&Edit')
        self.add('statictext', 'st_10', 37, 8, 210, 76, text='Date :')
        self.add('checkbox', 'cbx_withzero', 855, 8, 521, 80, text='With Zero Intamt')
        self.add('datawindow', 'dw_dim', 37, 120, 2336, 1388, dataobject='d_kuri_intpost', taborder=20)
        self.add('statictext', 'st_woodqbic', 2395, 1092, 82, 76)
        self.add('statictext', 'st_others', 2249, 1096, 119, 76)
        self.add('commandbutton', 'cb_ad', 55, 1424, 206, 76, text='&Add', taborder=50)
        self.add('commandbutton', 'cb_del', 265, 1424, 215, 76, text='&Delete', taborder=60)
        self.add('roundrectangle', 'rr_1', 896, 1520, 699, 144)
        self.add('commandbutton', 'cb_save', 969, 1544, 279, 92, text='&Save', taborder=30)
        self.add('commandbutton', 'cb_exit', 1257, 1544, 279, 92, text='E&xit', taborder=40)
        self.add('checkbox', 'cbx_fr', 256, 1548, 183, 80, text='Fr')
