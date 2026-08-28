"""Integrity Checking — w_account_checking.

Generated from the PowerBuilder window ``w_account_checking.srw`` by
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
    name='w_account_checking',
    title='Integrity Checking',
    width=3442,
    height=2216,
    controls=[],
    tables=['accountm', 'daybook', 'itemadj', 'salesm', 'purchasem', 'items', 'salesd', 'salesrd', 'purchased', 'purchaserd', 'smithd', 'refineryd', 'without', 'repaird', 'orderdga', 'accountg', 'accountgbs', 'daybookpart'],
    source_path='w_account_checking.srw',
)


class IntegrityCheckingForm(GeneratedForm):
    """Integrity Checking"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('commandbutton', 'cb_check', 1129, 0, 562, 108, text='&Check Now', taborder=10)
        self.add('commandbutton', 'cb_print', 2043, 0, 283, 108, text='&Print', taborder=11)
        self.add('commandbutton', 'cb_1', 2405, 0, 297, 108, text='E&xit', taborder=20)
        self.add('listbox', 'lb_result', 55, 116, 3296, 1968, taborder=30)
