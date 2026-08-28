"""Upto a Date — w_pandlac_trading.

Generated from the PowerBuilder window ``w_pandlac_trading.srw`` by
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
    name='w_pandlac_trading',
    title='Upto a Date',
    width=3666,
    height=2200,
    controls=[],
    tables=['accountm', 'daybook', 'date'],
    source_path='w_pandlac_trading.srw',
)


class UptoADateForm(GeneratedForm):
    """Upto a Date"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('commandbutton', 'cb_show', 1806, 0, 297, 92, text='&Show', taborder=40)
        self.add('commandbutton', 'cb_saveas', 2656, 0, 293, 92, text='Saveas', taborder=30)
        self.add('commandbutton', 'cb_1', 3131, 0, 233, 92, text='&Print', taborder=70)
        self.add('commandbutton', 'cb_2', 3378, 0, 238, 92, text='E&xit', taborder=60)
        self.add('editmask', 'em_date1', 443, 4, 434, 84, taborder=10)
        self.add('editmask', 'em_date2', 1339, 4, 430, 84, taborder=20)
        self.add('statictext', 'st_date1', 0, 8, 434, 76, text='Up to Date :')
        self.add('statictext', 'st_date2', 882, 8, 434, 76, text='Up to Date :')
        self.add('datawindow', 'dw_1', 0, 104, 3625, 2016, dataobject='d_pandlac_trading', taborder=50)
