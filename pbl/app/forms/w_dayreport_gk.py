"""Day Report — w_dayreport_gk.

Generated from the PowerBuilder window ``w_dayreport_gk.srw`` by
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
    name='w_dayreport_gk',
    title='Day Report',
    width=1760,
    height=1628,
    controls=[],
    tables=['salesm', 'salesd', 'purchased'],
    source_path='w_dayreport_gk.srw',
)


class DayReportForm(GeneratedForm):
    """Day Report"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 567, 76, 480, 100, taborder=10)
        self.add('statictext', 'st_1', 165, 84, 375, 76, text='Date From :')
        self.add('editmask', 'em_date2', 567, 208, 480, 100, taborder=20)
        self.add('statictext', 'st_2', 238, 216, 302, 76, text='Date To :')
        self.add('checkbox', 'cbx_salesbook', 567, 348, 581, 80, text='Sales Book Report')
        self.add('checkbox', 'cbx_stkreport', 567, 448, 613, 80, text='Print &Stock Report')
        self.add('checkbox', 'cbx_cashreport', 567, 528, 594, 80, text='Print &Cash Report')
        self.add('checkbox', 'cbx_sundbreport', 567, 620, 622, 80, text='Print Debtors Report')
        self.add('checkbox', 'cbx_suncrreport', 567, 704, 654, 80, text='Print Creditors Report')
        self.add('checkbox', 'cbx_expreport', 567, 784, 654, 80, text='Print Expense Report')
        self.add('checkbox', 'cbx_cashsummaryreport', 567, 868, 827, 80, text='Print Cash Summary Report')
        self.add('checkbox', 'cbx_stockreport', 567, 956, 846, 80, text='Print Stock Summary Report')
        self.add('checkbox', 'cbx_ogreport', 567, 1044, 846, 80, text='Print OG Summary Report')
        self.add('checkbox', 'cbx_smithreport', 567, 1128, 846, 80, text='Print Smith Summary Report')
        self.add('checkbox', 'cbx_view', 567, 1244, 530, 80, text='View before Print')
        self.add('commandbutton', 'cb_print', 622, 1368, 247, 108, text='&Print', taborder=30)
        self.add('commandbutton', 'cb_1', 882, 1368, 247, 108, text='E&xit', taborder=40)
