"""Kuri Finish — w_kuri_finish.

Generated from the PowerBuilder window ``w_kuri_finish.srw`` by
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
    name='w_kuri_finish',
    title='Kuri Finish',
    width=3141,
    height=1988,
    controls=[],
    tables=['daybook', 'kurifinishdet', 'clients_kuridet', 'clients', 'generali', 'daybookpart'],
    source_path='w_kuri_finish.srw',
    report={'dataobject': 'd_kuri_finish', 'sql': 'SELECT clients.code AS clients_code, clients.name AS clients_name, clients_kuridet.totamt AS clients_kuridet_totamt, clients_kuridet.bonus AS clients_kuridet_bonus, clients_kuridet.collnopbal AS clients_kuridet_collnopbal, (select sum(kuricolln.amount) from kuricolln where kuricolln.code = clients.code and kuricolln.tdate <= :rdate and kuricolln.control <= :rlevel) as totcolln2, (clients_kuridet.collnopbal + ifnull(totcolln2,0,totcolln2) ) as totcolln FROM clients, clients_kuridet WHERE clients.code = clients_kuridet.code ORDER BY clients.code ASC', 'args': ['rdate', 'rktype', 'rlevel', 'rgrate'], 'arg_types': {'rdate': 'date', 'rktype': 'string', 'rlevel': 'number', 'rgrate': 'number'}, 'tables': ['clients', 'clients_kuridet'], 'columns': [{'name': 'clients_code', 'label': 'clients_code', 'type': 'char'}, {'name': 'clients_name', 'label': 'clients_name', 'type': 'char'}, {'name': 'clients_kuridet_totamt', 'label': 'clients_kuridet_totamt', 'type': 'decimal'}, {'name': 'totcolln2', 'label': 'totcolln2', 'type': 'decimal'}, {'name': 'clients_kuridet_bonus', 'label': 'clients_kuridet_bonus', 'type': 'decimal'}, {'name': 'clients_kuridet_collnopbal', 'label': 'clients_kuridet_collnopbal', 'type': 'decimal'}, {'name': 'ctotcolln', 'label': 'ctotcolln', 'type': 'decimal'}]},
)


class KuriFinishForm(GeneratedForm):
    """Kuri Finish"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date', 494, 0, 434, 96, taborder=10)
        self.add('datawindow', 'dw_kuritype', 1312, 0, 677, 88, dataobject='d_kuritype_code', taborder=30)
        self.add('commandbutton', 'cb_print', 2176, 0, 343, 100, text='Print', taborder=31)
        self.add('commandbutton', 'cb_edit', 2578, 0, 343, 100, text='&Edit')
        self.add('statictext', 'st_10', 0, 4, 480, 76, text='Finished Date :')
        self.add('statictext', 'st_2', 960, 8, 343, 80, text='Kuri Type :')
        self.add('editmask', 'em_goldrate', 494, 100, 434, 96, taborder=20)
        self.add('commandbutton', 'cb_show', 1312, 100, 306, 96, text='Show', taborder=40)
        self.add('statictext', 'st_1', 0, 104, 480, 76, text='Gold Rate :')
        self.add('datawindow', 'dw_dim', 37, 204, 3063, 1532, dataobject='d_kuri_finish', taborder=50)
        self.add('statictext', 'st_woodqbic', 2395, 1092, 82, 76)
        self.add('statictext', 'st_others', 2249, 1096, 119, 76)
        self.add('commandbutton', 'cb_ad', 55, 1652, 206, 76, text='&Add', taborder=80)
        self.add('commandbutton', 'cb_del', 265, 1652, 215, 76, text='&Delete', taborder=90)
        self.add('roundrectangle', 'rr_1', 1262, 1732, 699, 144)
        self.add('commandbutton', 'cb_save', 1335, 1756, 279, 92, text='&Save', taborder=60)
        self.add('commandbutton', 'cb_exit', 1623, 1756, 279, 92, text='E&xit', taborder=70)
        self.add('checkbox', 'cbx_fr', 955, 1764, 210, 80, text='Fr')
