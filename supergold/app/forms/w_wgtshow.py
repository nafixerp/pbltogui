"""Show WM Weight — w_wgtshow.

Generated from the PowerBuilder window ``w_wgtshow.srw`` by
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
    name='w_wgtshow',
    title='Show WM Weight',
    width=1202,
    height=196,
    controls=[],
    tables=['olecustomcontrol'],
    source_path='w_wgtshow.srw',
)


class ShowWmWeightForm(GeneratedForm):
    """Show WM Weight"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('statictext', 'st_wgt', 0, 0, 1193, 180)
        self.add('olecustomcontrol', 'ole_sport', 1010, 12, 174, 152)
