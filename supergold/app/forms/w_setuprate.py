"""Current Rate Settings — w_setuprate.

Generated from the PowerBuilder window ``w_setuprate.srw`` by
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
    name='w_setuprate',
    title='Current Rate Settings',
    width=1870,
    height=1468,
    controls=[],
    tables=['ratehistory', 'generald', 'userd', 'generals'],
    source_path='w_setuprate.srw',
)


class CurrentRateSettingsForm(GeneratedForm):
    """Current Rate Settings"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('dropdownlistbox', 'ddlb_bultouch', 485, 64, 224, 400, text='99.5', items=['99.5', '99.9'], taborder=20)
        self.add('editmask', 'em_bulrate', 713, 68, 343, 88, taborder=10)
        self.add('statictext', 'st_10', 59, 72, 416, 76, text='Bullion Rate')
        self.add('checkbox', 'cbx_autocalcrates', 1097, 76, 672, 80, text='Autocalc Other rates')
        self.add('editmask', 'em_grate', 713, 168, 343, 88, taborder=30)
        self.add('statictext', 'st_34', 192, 172, 489, 76, text='Gold Rate(22ct) :')
        self.add('oval', 'oval_1', 1083, 228, 498, 364)
        self.add('editmask', 'em_g18rate', 713, 268, 343, 88, taborder=40)
        self.add('statictext', 'st_7', 192, 272, 489, 76, text='Gold Rate(18ct) :')
        self.add('commandbutton', 'cb_ok', 1152, 304, 343, 100, text='&Save')
        self.add('editmask', 'em_thrate', 713, 368, 343, 88, taborder=50)
        self.add('statictext', 'st_6', 242, 376, 439, 76, text='TH Rate(24Ct) :')
        self.add('commandbutton', 'cb_cancel', 1152, 408, 343, 100, text='E&xit')
        self.add('editmask', 'em_prate', 713, 468, 343, 88, taborder=60)
        self.add('statictext', 'st_9', 192, 472, 489, 76, text='Platinum :')
        self.add('editmask', 'em_srate', 713, 568, 343, 88, taborder=70)
        self.add('statictext', 'st_35', 279, 572, 402, 76, text='Silver Rate :')
        self.add('editmask', 'em_jrate', 713, 668, 343, 88, taborder=80)
        self.add('statictext', 'st_36', 178, 672, 503, 76, text='Jewellery Rate :')
        self.add('editmask', 'em_ograte', 713, 768, 343, 88, taborder=90)
        self.add('statictext', 'st_2', 361, 772, 320, 76, text='OG Rate :')
        self.add('statictext', 'st_8', 1307, 820, 110, 68, text='none')
        self.add('editmask', 'em_osrate', 713, 868, 343, 88, taborder=100)
        self.add('statictext', 'st_1', 329, 872, 352, 76, text='OS Rate :')
        self.add('statictext', 'st_3', 379, 988, 571, 76, text='Message of the day')
        self.add('singlelineedit', 'sle_mod', 379, 1060, 923, 92, limit=70, taborder=110)
        self.add('statictext', 'st_4', 110, 1080, 247, 76, text='English :')
        self.add('singlelineedit', 'sle_mod_mal', 379, 1176, 923, 92, limit=70, taborder=120)
        self.add('statictext', 'st_5', 0, 1192, 366, 76, text='Malayalam :')
