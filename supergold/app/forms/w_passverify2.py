"""Change Password — w_passverify2.

Generated from the PowerBuilder window ``w_passverify2.srw`` by
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
    name='w_passverify2',
    title='Change Password',
    width=1426,
    height=604,
    controls=[],
    tables=['userm'],
    source_path='w_passverify2.srw',
)


class ChangePasswordForm(GeneratedForm):
    """Change Password"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('commandbutton', 'cb_ok', 1147, 208, 247, 100, text='&OK', taborder=20)
        self.add('singlelineedit', 'sle_pass', 603, 212, 526, 96, taborder=10)
        self.add('statictext', 'st_1', 41, 220, 544, 84, text='Enter Old Password')
        self.add('singlelineedit', 'sle_opass', 256, 232, 640, 60, text='delta', taborder=30)
