"""Company Select — w_companyselect.

Generated from the PowerBuilder window ``w_companyselect.srw`` by
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
    name='w_companyselect',
    title='Company Select',
    width=1467,
    height=1208,
    controls=[],
    tables=['olecontrol', 'generals'],
    source_path='w_companyselect.srw',
)


class CompanySelectForm(GeneratedForm):
    """Company Select"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('datawindow', 'dw_1', 0, 64, 1440, 968, dataobject='d_selectcompany', taborder=1)
        self.add('olecontrol', 'ole_vpn', 1307, 1064, 165, 144, taborder=11)
        self.add('statictext', 'st_status', 137, 1068, 1175, 116)
