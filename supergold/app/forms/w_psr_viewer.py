"""PSR Reader — w_psr_viewer.

Generated from the PowerBuilder window ``w_psr_viewer.srw`` by
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
    name='w_psr_viewer',
    title='PSR Reader',
    width=3666,
    height=2272,
    controls=[],
    tables=['items'],
    source_path='w_psr_viewer.srw',
)


class PsrReaderForm(GeneratedForm):
    """PSR Reader"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('commandbutton', 'cb_select', 9, 0, 576, 84, text='&Select PSR Report...', taborder=60)
        self.add('commandbutton', 'cb_print', 617, 0, 242, 84, text='&Print', taborder=70)
        self.add('commandbutton', 'cb_ppage', 905, 0, 425, 84, text='Previous Page', taborder=50)
        self.add('commandbutton', 'cb_npage', 1353, 0, 320, 84, text='Next Page', taborder=80)
        self.add('commandbutton', 'cb_setup', 1691, 0, 274, 84, text='Setup', taborder=30)
        self.add('commandbutton', 'cb_sort', 1979, 0, 274, 84, text='Sort', taborder=90)
        self.add('commandbutton', 'cb_close', 2263, 0, 242, 84, text='&Close', taborder=90)
        self.add('statictext', 'st_file', 2551, 0, 1070, 68)
        self.add('datawindow', 'dw_1', 0, 92, 3630, 1972, taborder=10)
        self.add('checkbox', 'cbx_manual', 2414, 112, 430, 76, text='Manual Page')
        self.add('singlelineedit', 'sle_search', 288, 2072, 727, 88, taborder=40)
        self.add('commandbutton', 'cb_updtstk', 2496, 2072, 416, 88, text='Update Stock', taborder=20)
        self.add('commandbutton', 'cb_updtststk', 2930, 2072, 430, 88, text='Update St.Det', taborder=31)
        self.add('statictext', 'st_1', 32, 2076, 247, 76, text='Search :')
