"""Purity Certificate — w_puritycertificate.

Generated from the PowerBuilder window ``w_puritycertificate.srw`` by
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
    name='w_puritycertificate',
    title='Purity Certificate',
    width=2437,
    height=1684,
    controls=[],
    tables=['items'],
    source_path='w_puritycertificate.srw',
)


class PurityCertificateForm(GeneratedForm):
    """Purity Certificate"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('datawindow', 'dw_1', 18, 0, 2363, 1428, dataobject='d_puritycertificate', taborder=30)
        self.add('commandbutton', 'cb_add', 32, 1336, 233, 80, text='&Add', taborder=40)
        self.add('commandbutton', 'cb_del', 283, 1336, 233, 80, text='&Del', taborder=20)
        self.add('commandbutton', 'cb_print', 923, 1460, 306, 108, text='&Print', taborder=10)
        self.add('commandbutton', 'cb_exit', 1248, 1460, 306, 108, text='E&xit', taborder=4)
