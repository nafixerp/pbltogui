"""Cancel — w_gsmthcancel.

Generated from the PowerBuilder window ``w_gsmthcancel.srw`` by
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
    name='w_gsmthcancel',
    title='Cancel',
    width=1582,
    height=596,
    controls=[],
    tables=['items', 'itemsstk', 'smithm', 'barcode', 'smithd', 'itemadj', 'daybook', 'stkandprofit', 'oglist', 'delpart', 'daybookpart'],
    source_path='w_gsmthcancel.srw',
    opens=['w_gsmthhelp', 'w_tran_view'],
)


class CancelForm(GeneratedForm):
    """Cancel"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('singlelineedit', 'sle_bno', 558, 132, 462, 100, limit=10, taborder=10)
        self.add('commandbutton', 'cb_help', 1056, 136, 229, 92, text='&Help', taborder=11)
        self.add('statictext', 'st_1', 50, 140, 498, 72, text='Enter Doc. No.  :')
        self.add('oval', 'oval_1', 398, 272, 759, 220)
        self.add('commandbutton', 'cb_ok', 549, 332, 219, 100, text='&OK', taborder=20)
        self.add('commandbutton', 'cb_exit', 791, 336, 219, 96, text='E&xit', taborder=30)
