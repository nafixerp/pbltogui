"""Stock Type — w_stktype.

Generated from the PowerBuilder window ``w_stktype.srw`` by
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
    name='w_stktype',
    title='Stock Type',
    width=1742,
    height=968,
    controls=[],
    tables=['stktype', 'itemsstk', 'salesd', 'salesrd', 'purchased', 'purchaserd', 'smithd', 'refineryd', 'repaird', 'itemadj'],
    source_path='w_stktype.srw',
    opens=['w_defstktypeset', 'w_stktypehlp'],
)


class StockTypeForm(GeneratedForm):
    """Stock Type"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('statictext', 'st_head', 146, 12, 1435, 76)
        self.add('singlelineedit', 'sle_code', 430, 172, 471, 96, limit=10, taborder=10)
        self.add('checkbox', 'cbx_compare', 1033, 180, 535, 76, text='Compare with Fr')
        self.add('statictext', 'st_1', 105, 192, 311, 72, text='Code :')
        self.add('singlelineedit', 'sle_name', 430, 292, 1161, 96, limit=30, taborder=20)
        self.add('statictext', 'st_2', 105, 308, 311, 80, text='Name :')
        self.add('checkbox', 'cbx_def', 430, 424, 489, 76, text='Default &Type')
        self.add('checkbox', 'cbx_del', 1029, 424, 471, 76, text='Delete anyway')
        self.add('roundrectangle', 'rr_1', 41, 532, 1641, 200)
        self.add('commandbutton', 'cb_add', 78, 580, 247, 100, text='&Add', taborder=40)
        self.add('commandbutton', 'cb_edit', 334, 580, 247, 100, text='&Edit', taborder=50)
        self.add('commandbutton', 'cb_delete', 590, 580, 247, 100, text='&Delete', taborder=60)
        self.add('commandbutton', 'cb_save', 887, 580, 247, 100, text='&Save', taborder=80)
        self.add('commandbutton', 'cb_cancel', 1143, 580, 247, 100, text='&Cancel', taborder=70)
        self.add('commandbutton', 'cb_exit', 1399, 580, 247, 100, text='E&xit', taborder=90)
        self.add('commandbutton', 'cb_modulewise', 293, 756, 1134, 84, text='Module wise default stock type settings', taborder=100)
        self.add('editmask', 'em_balanceb', 773, 1600, 439, 96, taborder=30)
        self.add('radiobutton', 'rb_debitb', 1253, 1608, 407, 60, text='To receive')
        self.add('statictext', 'st_opbalb', 261, 1624, 471, 72, text='Op. Balance B :')
        self.add('radiobutton', 'rb_creditb', 1253, 1672, 297, 60, text='To give')
