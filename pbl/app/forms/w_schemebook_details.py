"""Scheme Details — w_schemebook_details.

Generated from the PowerBuilder window ``w_schemebook_details.srw`` by
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
    name='w_schemebook_details',
    title='Scheme Details',
    width=3685,
    height=2428,
    controls=[],
    tables=['kuricolln', 'clients', 'clients_kuridet'],
    source_path='w_schemebook_details.srw',
)


class SchemeDetailsForm(GeneratedForm):
    """Scheme Details"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('datawindow', 'dw_accode', 233, 0, 1019, 92, dataobject='d_kuri_cust', taborder=30)
        self.add('commandbutton', 'cb_show', 2510, 0, 256, 96, text='&Show', taborder=110)
        self.add('commandbutton', 'cb_print', 3113, 0, 256, 100, text='&Print', taborder=140)
        self.add('commandbutton', 'cb_exit', 3378, 0, 256, 100, text='E&xit', taborder=130)
        self.add('editmask', 'em_date', 1591, 4, 398, 92, taborder=10)
        self.add('statictext', 'st_3', 0, 16, 224, 72, text='Party :')
        self.add('statictext', 'st_1', 1358, 16, 219, 64, text='As On :')
        self.add('datawindow', 'dw_1', 0, 104, 3634, 2216, dataobject='d_schemebook_details', taborder=120)
