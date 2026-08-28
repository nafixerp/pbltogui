"""Op.Stock Value Set — w_stockvalueset.

Generated from the PowerBuilder window ``w_stockvalueset.srw`` by
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
    name='w_stockvalueset',
    title='Op.Stock Value Set',
    width=1614,
    height=944,
    controls=[],
    tables=['accountm', 'stkandprofit'],
    source_path='w_stockvalueset.srw',
)


class OpStockValueSetForm(GeneratedForm):
    """Op.Stock Value Set"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date', 704, 184, 507, 116, taborder=10)
        self.add('statictext', 'st_2', 160, 200, 517, 76, text='Date :')
        self.add('editmask', 'em_stock', 704, 336, 507, 116, taborder=20)
        self.add('statictext', 'st_1', 187, 348, 489, 80, text='Stock Value :')
        self.add('commandbutton', 'cb_ok', 699, 564, 302, 120, text='OK', taborder=30)
