"""Book Stock — w_bookstock.

Generated from the PowerBuilder window ``w_bookstock.srw`` by
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
    name='w_bookstock',
    title='Book Stock',
    width=1614,
    height=944,
    controls=[],
    tables=['generals'],
    source_path='w_bookstock.srw',
)


class BookStockForm(GeneratedForm):
    """Book Stock"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_stock', 567, 148, 603, 124, taborder=10)
        self.add('statictext', 'st_1', 206, 164, 343, 80, text='Stock :')
        self.add('editmask', 'em_cash', 567, 344, 603, 124, taborder=20)
        self.add('statictext', 'st_2', 201, 364, 343, 80, text='Cash :')
        self.add('commandbutton', 'cb_ok', 599, 540, 343, 144, text='OK', taborder=30)
