"""Kuri Draw — w_kuri_draw.

Generated from the PowerBuilder window ``w_kuri_draw.srw`` by
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
    name='w_kuri_draw',
    title='Kuri Draw',
    width=1966,
    height=1172,
    controls=[],
    tables=['kurifinishdet', 'daybook', 'clients_kuridet', 'clients', 'kuricolln', 'generali', 'daybookpart'],
    source_path='w_kuri_draw.srw',
)


class KuriDrawForm(GeneratedForm):
    """Kuri Draw"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date', 485, 16, 434, 100, taborder=10)
        self.add('statictext', 'st_4', 114, 28, 352, 80, text='Draw Date :')
        self.add('editmask', 'em_goldrate', 485, 124, 434, 100, taborder=20)
        self.add('statictext', 'st_6', 0, 132, 466, 80, text='Gold Rate :')
        self.add('datawindow', 'dw_accode', 485, 228, 1019, 92, dataobject='d_kuri_cust', taborder=30)
        self.add('statictext', 'st_3', 128, 240, 338, 72, text='Party  :')
        self.add('singlelineedit', 'sle_name', 485, 324, 1399, 92)
        self.add('statictext', 'st_1', 123, 332, 343, 80, text='Address :')
        self.add('editmask', 'em_totkuriamt', 485, 420, 434, 100)
        self.add('editmask', 'em_estwgt', 1449, 420, 434, 100, taborder=31)
        self.add('statictext', 'st_5', 0, 424, 466, 80, text='Total Kuri Amt :')
        self.add('statictext', 'st_9', 1129, 428, 306, 80, text='Est. Wgt :')
        self.add('editmask', 'em_totcolln', 485, 524, 434, 100)
        self.add('statictext', 'st_2', 101, 536, 366, 80, text='Total Colln :')
        self.add('editmask', 'em_balance', 485, 628, 434, 100)
        self.add('statictext', 'st_7', 0, 640, 466, 80, text='Balance :')
        self.add('editmask', 'em_bonus', 485, 732, 434, 100, taborder=40)
        self.add('statictext', 'st_8', 0, 744, 466, 80, text='Bonus :')
        self.add('commandbutton', 'cb_ok', 745, 864, 270, 120, text='&OK', taborder=50)
        self.add('checkbox', 'cbx_fr', 480, 884, 183, 80, text='Fr')
