"""Daysummary Malayalam — w_daysummarydate_mala.

Generated from the PowerBuilder window ``w_daysummarydate_mala.srw`` by
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
    name='w_daysummarydate_mala',
    title='Daysummary Malayalam',
    width=1074,
    height=712,
    controls=[],
    tables=[],
    source_path='w_daysummarydate_mala.srw',
    opens=['w_daysummary_mala'],
)


class DaysummaryMalayalamForm(GeneratedForm):
    """Daysummary Malayalam"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date', 462, 64, 338, 100, taborder=10)
        self.add('statictext', 'st_1', 247, 88, 210, 76, text='Date :')
        self.add('editmask', 'em_rate', 462, 212, 338, 88, taborder=11)
        self.add('statictext', 'st_2', 137, 224, 293, 76, text='Int. Rate :')
        self.add('oval', 'oval_1', 297, 332, 507, 268)
        self.add('commandbutton', 'cb_ok', 411, 376, 293, 88, text='&Ok', taborder=20)
        self.add('commandbutton', 'cb_1', 411, 468, 293, 88, text='E&xit', taborder=30)
