"""Exit — w_about.

Generated from the PowerBuilder window ``w_about.srw`` by
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
    name='w_about',
    title='Exit',
    width=1527,
    height=1224,
    controls=[],
    tables=[],
    source_path='w_about.srw',
)


class ExitForm(GeneratedForm):
    """Exit"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('roundrectangle', 'rr_1', 91, 8, 1344, 500)
        self.add('statictext', 'st_2', 329, 32, 837, 76, text='GoldMine - 2023')
        self.add('statictext', 'st_3', 329, 128, 837, 76, text='Version 23.0')
        self.add('statictext', 'st_4', 329, 212, 837, 76, text='Copyright ~hA9 reserved with')
        self.add('statictext', 'st_1', 238, 292, 1006, 80, text='MK Soft Technologies')
        self.add('statictext', 'st_assoc', 114, 384, 1294, 80)
        self.add('statictext', 'st_5', 233, 524, 1015, 76, text='This Software is licensed to')
        self.add('statictext', 'st_name', 233, 608, 1015, 76, text='Mr.Naser')
        self.add('statictext', 'st_company', 233, 704, 1015, 76, text='M.P.C. Jewellery')
        self.add('statictext', 'st_subver', 233, 860, 1015, 104)
        self.add('statictext', 'st_test', 923, 968, 526, 172)
        self.add('commandbutton', 'cb_1', 626, 1000, 242, 104, text='Ok', taborder=1)
