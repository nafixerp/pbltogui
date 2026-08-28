"""New — w_reprno.

Generated from the PowerBuilder window ``w_reprno.srw`` by
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
    name='w_reprno',
    title='New',
    width=1403,
    height=668,
    controls=[],
    tables=['repairm', 'smithm'],
    source_path='w_reprno.srw',
)


class NewForm(GeneratedForm):
    """New"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('dropdownlistbox', 'ddlb_rmno', 567, 12, 247, 324, text='1', items=['1', '2', '3'], taborder=10)
        self.add('statictext', 'st_1', 311, 16, 247, 76, text='Stage :')
        self.add('singlelineedit', 'sle_rmno', 567, 120, 443, 100, taborder=20)
        self.add('commandbutton', 'cb_rmhelp', 1029, 124, 165, 88, text='&Help')
        self.add('statictext', 'st_rmno', 169, 128, 389, 76, text='Remake No :')
        self.add('oval', 'oval_1', 347, 268, 713, 208)
        self.add('commandbutton', 'cb_ok', 443, 320, 233, 100, text='&OK', taborder=30)
        self.add('commandbutton', 'cb_exit', 709, 320, 233, 100, text='E&xit', taborder=40)
