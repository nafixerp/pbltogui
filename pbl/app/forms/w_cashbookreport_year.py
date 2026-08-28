"""Yearly Cash Balance — w_cashbookreport_year.

Generated from the PowerBuilder window ``w_cashbookreport_year.srw`` by
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
    name='w_cashbookreport_year',
    title='Yearly Cash Balance',
    width=3657,
    height=2384,
    controls=[],
    tables=['accountm', 'daybook'],
    source_path='w_cashbookreport_year.srw',
    opens=['w_acledgerpopup'],
)


class YearlyCashBalanceForm(GeneratedForm):
    """Yearly Cash Balance"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('datawindow', 'dw_cashbook', 0, 0, 3625, 2216, dataobject='d_cashbook_yearly', taborder=10)
        self.add('commandbutton', 'cb_print', 1531, 2220, 329, 72, text='&Print', taborder=20)
        self.add('commandbutton', 'cb_exit', 1865, 2220, 329, 72, text='E&xit', taborder=11)
