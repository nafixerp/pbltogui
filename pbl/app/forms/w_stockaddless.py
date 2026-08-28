"""Stock Add - Less — w_stockaddless.

Generated from the PowerBuilder window ``w_stockaddless.srw`` by
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
    name='w_stockaddless',
    title='Stock Add - Less',
    width=4206,
    height=2208,
    controls=[],
    tables=['items', 'itemsstk', 'itemadj', 'barcode', 'generali'],
    source_path='w_stockaddless.srw',
)


class StockAddLessForm(GeneratedForm):
    """Stock Add - Less"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date', 224, 0, 448, 100, taborder=10)
        self.add('datawindow', 'dw_smcode', 2496, 0, 677, 88, dataobject='d_smancode', taborder=30)
        self.add('checkbox', 'cbx_stktransfer', 1170, 4, 626, 92, text='As Stock &Transfer', taborder=20)
        self.add('statictext', 'st_2', 2231, 8, 247, 76, text='SMan :')
        self.add('statictext', 'st_1', 18, 12, 206, 76, text='Date :')
        self.add('datawindow', 'dw_1', 14, 112, 4169, 1884, dataobject='d_stockaddless', taborder=40)
        self.add('statictext', 'st_3', 347, 116, 5, 1768)
        self.add('statictext', 'st_25', 672, 116, 5, 1768)
        self.add('statictext', 'st_4', 1143, 116, 5, 1876)
        self.add('statictext', 'st_20', 1312, 116, 5, 1876)
        self.add('statictext', 'st_6', 1573, 116, 5, 1876)
        self.add('statictext', 'st_21', 1778, 116, 5, 1876)
        self.add('statictext', 'st_22', 2002, 116, 5, 1876)
        self.add('statictext', 'st_23', 2176, 116, 5, 1876)
        self.add('statictext', 'st_30', 2441, 116, 5, 1876)
        self.add('statictext', 'st_31', 2688, 116, 5, 1876)
        self.add('statictext', 'st_50', 2898, 116, 5, 1876)
        self.add('statictext', 'st_10', 3109, 116, 5, 1876)
        self.add('statictext', 'st_36', 3369, 116, 5, 1876)
        self.add('statictext', 'st_5', 3662, 116, 5, 1876)
        self.add('commandbutton', 'cb_add', 32, 1888, 224, 88, text='&Add', taborder=50)
        self.add('commandbutton', 'cb_delete', 261, 1888, 229, 88, text='&Delete', taborder=60)
        self.add('commandbutton', 'cb_update', 1376, 1996, 315, 100, text='&Save', taborder=80)
        self.add('commandbutton', 'cb_1', 1760, 2000, 315, 100, text='&Print', taborder=90)
        self.add('commandbutton', 'cb_2', 2130, 2000, 315, 100, text='E&xit', taborder=70)
        self.add('checkbox', 'cbx_speed', 2674, 2012, 425, 76, text='Speed Print')
