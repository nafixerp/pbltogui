"""Backup — w_backup.

Generated from the PowerBuilder window ``w_backup.srw`` by
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
    name='w_backup',
    title='Backup',
    width=1870,
    height=1492,
    controls=[],
    tables=['olecontrol'],
    source_path='w_backup.srw',
)


class BackupForm(GeneratedForm):
    """Backup"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('multilineedit', 'mle_1', 37, 76, 1742, 368, text='You should take backup daily. Then you can recover the data if the database is corrupted due to the power failure or any other reasons. Take the backup to floppy occasionally.')
        self.add('groupbox', 'gb_1', 46, 476, 699, 288, text='Backup', taborder=20)
        self.add('checkbox', 'cbx_dateattach', 878, 512, 727, 76, text='Attach Date')
        self.add('radiobutton', 'rb_disk', 101, 556, 489, 76, text='To Hard &Disk')
        self.add('checkbox', 'cbx_nozip', 878, 620, 402, 80, text="Don't Zip")
        self.add('radiobutton', 'rb_toanotherplace', 101, 644, 631, 76, text='To Another Place')
        self.add('olecontrol', 'ole_zip', 1559, 716, 146, 128, taborder=30)
        self.add('singlelineedit', 'sle_place', 55, 876, 1499, 92, taborder=60)
        self.add('commandbutton', 'cb_help', 1563, 876, 270, 96, text='Browse', taborder=50)
        self.add('commandbutton', 'cb_def', 686, 976, 357, 88, text='Set as defauls', taborder=10)
        self.add('roundrectangle', 'rr_1', 366, 1092, 997, 164)
        self.add('commandbutton', 'cb_backup', 407, 1120, 457, 108, text='&Take Backup', taborder=30)
        self.add('commandbutton', 'cb_exit', 873, 1120, 457, 108, text='E&xit', taborder=40)
