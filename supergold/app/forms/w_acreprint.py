"""Reprint — w_acreprint.

Generated from the PowerBuilder window ``w_acreprint.srw`` by
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
    name='w_acreprint',
    title='Reprint',
    width=1362,
    height=696,
    controls=[],
    tables=['pdclist', 'daybookpart'],
    source_path='w_acreprint.srw',
)


class ReprintForm(GeneratedForm):
    """Reprint"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('singlelineedit', 'sle_bno', 471, 96, 425, 100, limit=10, taborder=10)
        self.add('commandbutton', 'cb_help', 951, 100, 215, 96, text='&Help', taborder=20)
        self.add('statictext', 'st_1', 46, 116, 443, 72, text='Voucher No  :')
        self.add('checkbox', 'cbx_printobcb', 475, 224, 425, 76, text='Print OB/CB')
        self.add('oval', 'oval_1', 347, 352, 654, 224)
        self.add('commandbutton', 'cb_ok', 443, 420, 229, 92, text='OK', taborder=30)
        self.add('commandbutton', 'cb_exit', 681, 420, 229, 92, text='E&xit', taborder=21)
