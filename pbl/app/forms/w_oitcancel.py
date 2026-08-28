"""Cancel — w_oitcancel.

Generated from the PowerBuilder window ``w_oitcancel.srw`` by
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
    name='w_oitcancel',
    title='Cancel',
    width=1586,
    height=640,
    controls=[],
    tables=['itemsothers', 'oitemtranm', 'oitemtrand', 'daybook', 'stkandprofit', 'delpart', 'daybookpart'],
    source_path='w_oitcancel.srw',
)


class CancelForm(GeneratedForm):
    """Cancel"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('singlelineedit', 'sle_bno', 562, 132, 425, 100, limit=13, taborder=10)
        self.add('commandbutton', 'cb_help', 1019, 132, 229, 100, text='&Help', taborder=20)
        self.add('statictext', 'st_1', 82, 156, 480, 72, text='Enter Doc No.  :')
        self.add('oval', 'oval_1', 430, 288, 722, 212)
        self.add('commandbutton', 'cb_ok', 539, 340, 247, 100, text='&OK', taborder=30)
        self.add('commandbutton', 'cb_exit', 809, 340, 247, 100, text='E&xit', taborder=21)
