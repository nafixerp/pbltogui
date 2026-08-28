"""Edit Order Entry — w_ordereditbillno.

Generated from the PowerBuilder window ``w_ordereditbillno.srw`` by
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
    name='w_ordereditbillno',
    title='Edit Order Entry',
    width=1403,
    height=668,
    controls=[],
    tables=['orderm'],
    source_path='w_ordereditbillno.srw',
)


class EditOrderEntryForm(GeneratedForm):
    """Edit Order Entry"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('singlelineedit', 'sle_billno', 544, 148, 416, 104, limit=13, taborder=10)
        self.add('commandbutton', 'cb_help', 983, 152, 229, 100, text='&Help', taborder=20)
        self.add('statictext', 'st_1', 69, 164, 480, 64, text='Enter Order no :')
        self.add('oval', 'oval_1', 347, 300, 713, 208)
        self.add('commandbutton', 'cb_ok', 462, 356, 233, 96, text='&Ok', taborder=30)
        self.add('commandbutton', 'cb_exit', 718, 356, 233, 96, text='E&xit', taborder=40)
