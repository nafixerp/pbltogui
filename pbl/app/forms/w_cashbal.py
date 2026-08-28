"""Cash Balance — w_cashbal.

Generated from the PowerBuilder window ``w_cashbal.srw`` by
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
    name='w_cashbal',
    title='Cash Balance',
    width=1490,
    height=512,
    controls=[],
    tables=['accountm', 'daybook'],
    source_path='w_cashbal.srw',
)


class CashBalanceForm(GeneratedForm):
    """Cash Balance"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('statictext', 'st_bal', 503, 120, 901, 112)
        self.add('statictext', 'st_1', 46, 144, 471, 76, text='Cash Balance :')
        self.add('commandbutton', 'cb_1', 626, 316, 169, 84, text='Ok', taborder=1)
