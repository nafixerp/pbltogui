"""Administration — w_administration.

Generated from the PowerBuilder window ``w_administration.srw`` by
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
    name='w_administration',
    title='Administration',
    width=1321,
    height=1156,
    controls=[],
    tables=['purchasem', 'daybook', 'purchased', 'purchased_dmddet', 'purchaserd', 'purchaserm', 'daybookpart'],
    source_path='w_administration.srw',
)


class AdministrationForm(GeneratedForm):
    """Administration"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('commandbutton', 'cb_init', 91, 120, 539, 108, text='&Initialise', taborder=60)
        self.add('commandbutton', 'cb_stkupdate', 667, 120, 539, 108, text='Stock Update', taborder=100)
        self.add('commandbutton', 'cb_initdoc', 91, 240, 539, 108, text='&Initialise Doc. No.', taborder=110)
        self.add('commandbutton', 'cb_sqlupdt', 667, 240, 539, 108, text='SQL Updt', taborder=20)
        self.add('commandbutton', 'cb_changedocno', 91, 360, 539, 108, text='Change Doc. No.', taborder=70)
        self.add('commandbutton', 'cb_rearangevchno', 667, 360, 539, 108, text='Rearange Docnos', taborder=50)
        self.add('commandbutton', 'cb_slnoadd', 91, 480, 539, 108, text='Add Slno', taborder=30)
        self.add('commandbutton', 'cb_updtlogs', 667, 480, 539, 104, text='Update Log Rep', taborder=61)
        self.add('commandbutton', 'cb_2', 91, 600, 539, 108, text='Test xmlhttp', taborder=70)
        self.add('commandbutton', 'cb_exit', 667, 600, 539, 108, text='E&xit', taborder=10)
        self.add('commandbutton', 'cb_delpurchases', 91, 720, 539, 104, text='Delete Purchases', taborder=60)
        self.add('commandbutton', 'cb_pwdch', 667, 720, 539, 108, text='Admin', taborder=40)
        self.add('commandbutton', 'cb_pchange', 91, 844, 539, 108, text='&PSW Change', taborder=50)
        self.add('commandbutton', 'cb_setup', 667, 844, 539, 108, text='Lic Reset', taborder=51)
