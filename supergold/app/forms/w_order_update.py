"""Update from Jewelleries — w_order_update.

Generated from the PowerBuilder window ``w_order_update.srw`` by
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
    name='w_order_update',
    title='Update from Jewelleries',
    width=3689,
    height=2300,
    controls=[],
    tables=['orderm', 'orderd', 'other'],
    source_path='w_order_update.srw',
)


class UpdateFromJewelleriesForm(GeneratedForm):
    """Update from Jewelleries"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('commandbutton', 'cb_selectupdation', 5, 0, 544, 96, text='Select Updations', taborder=30)
        self.add('commandbutton', 'cb_update', 2107, 0, 549, 96, text='&Update', taborder=10)
        self.add('commandbutton', 'cb_1', 3095, 0, 265, 96, text='&Print', taborder=50)
        self.add('commandbutton', 'cb_2', 3360, 0, 265, 96, text='E&xit', taborder=40)
        self.add('datawindow', 'dw_1', 5, 100, 3621, 2084, taborder=20)
