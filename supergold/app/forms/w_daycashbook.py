"""Day Cash Book Report — w_daycashbook.

Generated from the PowerBuilder window ``w_daycashbook.srw`` by
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
    name='w_daycashbook',
    title='Day Cash Book Report',
    width=3657,
    height=2364,
    controls=[],
    tables=['daybook', 'accountm', 'salesm', 'salesrm', 'purchasem'],
    source_path='w_daycashbook.srw',
)


class DayCashBookReportForm(GeneratedForm):
    """Day Cash Book Report"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date', 370, 0, 384, 92, taborder=10)
        self.add('commandbutton', 'cb_show', 969, 0, 274, 96, text='&Show', taborder=30)
        self.add('commandbutton', 'cb_print', 1321, 0, 274, 96, text='&Print', taborder=40)
        self.add('commandbutton', 'cb_laserprint', 1696, 0, 370, 96, text='Laser Print', taborder=50)
        self.add('richtextedit', 'rte_1', 2121, 0, 165, 92)
        self.add('commandbutton', 'cb_exit', 3319, 0, 233, 96, text='E&xit', taborder=60)
        self.add('statictext', 'st_10', 0, 12, 361, 64, text='Date :')
        self.add('multilineedit', 'mle_1', 23, 104, 3602, 2148, taborder=20)
