"""Cancel — w_rprcancel.

Generated from the PowerBuilder window ``w_rprcancel.srw`` by
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
    name='w_rprcancel',
    title='Cancel',
    width=1559,
    height=628,
    controls=[],
    tables=['repairm', 'items', 'itemsstk', 'repaird', 'daybook', 'delpart', 'daybookpart'],
    source_path='w_rprcancel.srw',
    opens=['w_repairhelp'],
)


class CancelForm(GeneratedForm):
    """Cancel"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('singlelineedit', 'sle_bno', 558, 132, 462, 100, limit=10, taborder=10)
        self.add('commandbutton', 'cb_help', 1056, 136, 229, 92, text='&Help', taborder=11)
        self.add('statictext', 'st_1', 50, 160, 498, 72, text='Enter Doc. No.  :')
        self.add('oval', 'oval_1', 398, 292, 759, 220)
        self.add('commandbutton', 'cb_ok', 544, 352, 238, 100, text='&OK', taborder=20)
        self.add('commandbutton', 'cb_exit', 795, 352, 238, 100, text='E&xit', taborder=30)
