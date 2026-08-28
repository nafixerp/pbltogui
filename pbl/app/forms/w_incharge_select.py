"""Change — w_incharge_select.

Generated from the PowerBuilder window ``w_incharge_select.srw`` by
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
    name='w_incharge_select',
    title='Change',
    width=1394,
    height=828,
    controls=[],
    tables=[],
    source_path='w_incharge_select.srw',
)


class ChangeForm(GeneratedForm):
    """Change"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('datawindow', 'dw_incharge', 402, 188, 690, 88, dataobject='d_incharge_code', taborder=1)
        self.add('statictext', 'st_1', 46, 192, 343, 80, text='Incharge :')
        self.add('commandbutton', 'cb_ok', 631, 384, 288, 116, text='OK', taborder=2)
