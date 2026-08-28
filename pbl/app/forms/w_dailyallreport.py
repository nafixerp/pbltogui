"""Daily All Report — w_dailyallreport.

Generated from the PowerBuilder window ``w_dailyallreport.srw`` by
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
    name='w_dailyallreport',
    title='Daily All Report',
    width=3666,
    height=2296,
    controls=[],
    tables=['salesd', 'salesm', 'purchased', 'orderm', 'sman', 'salesrd', 'items', 'incharge'],
    source_path='w_dailyallreport.srw',
)


class DailyAllReportForm(GeneratedForm):
    """Daily All Report"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('dropdownlistbox', 'ddlb_reptype', 1577, 0, 1216, 832, text='Item Trans Summary', items=['Item Trans Summary', 'Sales-SMWise', 'Sales-Itemwise', 'Cash-Sectionwise'], taborder=30)
        self.add('commandbutton', 'cb_show', 2821, 0, 274, 92, text='&Show', taborder=40)
        self.add('commandbutton', 'cb_print', 3113, 0, 274, 92, text='&Print', taborder=50)
        self.add('commandbutton', 'cb_exit', 3401, 0, 233, 92, text='E&xit', taborder=60)
        self.add('editmask', 'em_date1', 224, 4, 384, 92, taborder=10)
        self.add('editmask', 'em_date2', 805, 4, 384, 92, taborder=20)
        self.add('statictext', 'st_10', 0, 12, 215, 64, text='From :')
        self.add('statictext', 'st_2', 1216, 12, 352, 64, text='Rep Type :')
        self.add('statictext', 'st_1', 663, 16, 133, 64, text='To :')
        self.add('multilineedit', 'mle_1', 0, 100, 3639, 2108, taborder=70)
