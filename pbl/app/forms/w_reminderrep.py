"""Reminder — w_reminderrep.

Generated from the PowerBuilder window ``w_reminderrep.srw`` by
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
    name='w_reminderrep',
    title='Reminder',
    width=3657,
    height=2172,
    controls=[],
    tables=['clients', 'appoint', 'salesm', 'orderm', 'ruffwrk', 'smithsusp', 'smithnewwrk', 'items', 'clients_kuridet', 'purchasem', 'daybook', 'pdclist', 'collection', 'accountm'],
    source_path='w_reminderrep.srw',
)


class ReminderForm(GeneratedForm):
    """Reminder"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('datawindow', 'dw_1', 0, 0, 3630, 1960, dataobject='d_reminderrep', taborder=10)
        self.add('commandbutton', 'cb_print', 1486, 1960, 311, 108, text='&Print', taborder=30)
        self.add('commandbutton', 'cb_ok', 1902, 1960, 311, 108, text='&Ok', taborder=40)
        self.add('dropdownlistbox', 'ddlb_type', 247, 1972, 846, 660, items=['Balance Duedate', 'Appointment', 'Order Pending', 'Ruff Work', 'Suspense Items', 'New Work', 'ROL'], taborder=20)
        self.add('commandbutton', 'cb_filter', 1093, 1972, 215, 92, text='Filter', taborder=12)
        self.add('statictext', 'st_1', 14, 1976, 210, 76, text='Type :')
