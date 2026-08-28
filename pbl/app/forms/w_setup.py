"""Application — w_setup.

Generated from the PowerBuilder window ``w_setup.srw`` by
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
    name='w_setup',
    title='Application',
    width=3287,
    height=2444,
    controls=[],
    tables=['daybook', 'item', 'salesm', 'purchasem', 'wgt', 'fr', 'rcvd', 'application', 'party', 'account', 'generals', 'generald', 'generali'],
    source_path='w_setup.srw',
)


class ApplicationForm(GeneratedForm):
    """Application"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('tab', 'tab_setup', 9, 8, 3227, 2224, taborder=10)
        self.add('commandbutton', 'cb_ok', 1367, 2244, 293, 104, text='&Save', taborder=30)
        self.add('commandbutton', 'cb_cancel', 1678, 2244, 293, 104, text='&Cancel', taborder=20)
