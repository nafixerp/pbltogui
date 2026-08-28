"""Payment Confirmation — w_payment_confirm.

Generated from the PowerBuilder window ``w_payment_confirm.srw`` by
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
    name='w_payment_confirm',
    title='Payment Confirmation',
    width=3369,
    height=1540,
    controls=[],
    tables=['daybook', 'pdclist', 'userd', 'delpart'],
    source_path='w_payment_confirm.srw',
    report={'dataobject': 'd_payment_confirm', 'sql': "SELECT daybookpart.vchno AS daybookpart_vchno, daybook.tdate AS daybook_tdate, daybook.amount AS daybook_amount, daybookpart.particular AS daybookpart_particular, daybookpart.chequeno AS daybookpart_chequeno, daybook.slno AS daybook_slno, (select accountm.name from accountm where accountm.accode = daybook.accode) as acname, (select accountm.name from accountm where accountm.accode = daybook.opaccode) as cbacname FROM daybook, daybookpart WHERE daybook.slno = daybookpart.slno AND left(daybookpart.vchno,2) = 'VP' ORDER BY daybook.tdate ASC, daybook.slno ASC", 'args': [], 'arg_types': {}, 'tables': ['daybook', 'daybookpart'], 'columns': [{'name': 'daybookpart_vchno', 'label': 'daybookpart_vchno', 'type': 'char'}, {'name': 'daybook_tdate', 'label': 'daybook_tdate', 'type': 'date'}, {'name': 'acname', 'label': 'acname', 'type': 'char'}, {'name': 'cbacname', 'label': 'cbacname', 'type': 'char'}, {'name': 'daybook_amount', 'label': 'daybook_amount', 'type': 'decimal'}, {'name': 'daybookpart_particular', 'label': 'daybookpart_particular', 'type': 'char'}, {'name': 'daybookpart_chequeno', 'label': 'daybookpart_chequeno', 'type': 'char'}, {'name': 'daybook_slno', 'label': 'daybook_slno', 'type': 'decimal'}]},
)


class PaymentConfirmationForm(GeneratedForm):
    """Payment Confirmation"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('datawindow', 'dw_1', 0, 0, 3337, 1272, dataobject='d_payment_confirm', taborder=10)
        self.add('statictext', 'st_search', 27, 1184, 416, 76)
        self.add('commandbutton', 'cb_del', 878, 1312, 366, 120, text='Delete', taborder=20)
        self.add('commandbutton', 'cb_refresh', 1257, 1312, 366, 120, text='Refresh', taborder=30)
        self.add('commandbutton', 'cb_ok', 1637, 1312, 366, 120, text='Confirm', taborder=40)
        self.add('commandbutton', 'cb_cancel', 2011, 1312, 366, 120, text='Exit', taborder=50)
