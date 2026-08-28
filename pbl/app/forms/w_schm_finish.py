"""Scheme Finished — w_schm_finish.

Generated from the PowerBuilder window ``w_schm_finish.srw`` by
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
    name='w_schm_finish',
    title='Scheme Finished',
    width=1966,
    height=1476,
    controls=[],
    tables=['kurifinishdet', 'daybook', 'clients_kuridet', 'kuricolln', 'clients', 'kuriint', 'generali', 'daybookpart'],
    source_path='w_schm_finish.srw',
)


class SchemeFinishedForm(GeneratedForm):
    """Scheme Finished"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date', 485, 16, 434, 100, taborder=10)
        self.add('statictext', 'st_4', 18, 28, 448, 80, text='Finished Date :')
        self.add('editmask', 'em_goldrate', 485, 120, 434, 100, taborder=20)
        self.add('statictext', 'st_6', 0, 128, 466, 80, text='Gold Rate :')
        self.add('datawindow', 'dw_accode', 485, 224, 1019, 92, dataobject='d_kuri_cust', taborder=30)
        self.add('statictext', 'st_3', 128, 236, 338, 72, text='Party  :')
        self.add('singlelineedit', 'sle_name', 485, 320, 1399, 92)
        self.add('statictext', 'st_1', 123, 328, 343, 80, text='Address :')
        self.add('editmask', 'em_totkuriamt', 485, 416, 434, 100)
        self.add('editmask', 'em_estwgt', 1449, 416, 434, 100)
        self.add('statictext', 'st_5', 0, 420, 466, 80, text='Scheme Amt :')
        self.add('statictext', 'st_12', 1015, 428, 421, 80, text='Scheme Wgt :')
        self.add('editmask', 'em_totcolln', 485, 520, 434, 100)
        self.add('editmask', 'em_collnwgt', 1449, 520, 434, 100)
        self.add('statictext', 'st_9', 1083, 528, 352, 80, text='Colln Wgt :')
        self.add('statictext', 'st_2', 101, 532, 366, 80, text='Total Colln :')
        self.add('editmask', 'em_intamt', 485, 624, 434, 100)
        self.add('statictext', 'st_11', 37, 628, 430, 80, text='Total Interest :')
        self.add('editmask', 'em_balance', 485, 728, 434, 100)
        self.add('statictext', 'st_7', 0, 740, 466, 80, text='Balance :')
        self.add('editmask', 'em_bonus', 485, 832, 434, 100, taborder=40)
        self.add('statictext', 'st_8', 0, 844, 466, 80, text='Bonus :')
        self.add('editmask', 'em_amttogive', 485, 936, 434, 100)
        self.add('editmask', 'em_netwgt', 1449, 936, 434, 100)
        self.add('statictext', 'st_13', 69, 940, 398, 80, text='Amt To Give :')
        self.add('statictext', 'st_10', 1001, 952, 434, 80, text='Net Gold Wgt :')
        self.add('editmask', 'em_avgrate', 1449, 1040, 434, 100)
        self.add('statictext', 'st_14', 1001, 1048, 434, 80, text='AVG Rate :')
        self.add('commandbutton', 'cb_ok', 914, 1228, 270, 120, text='&OK', taborder=50)
        self.add('checkbox', 'cbx_fr', 480, 1252, 183, 80, text='Fr')
