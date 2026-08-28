"""Payment Details — w_pmntdetail.

Generated from the PowerBuilder window ``w_pmntdetail.srw`` by
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
    name='w_pmntdetail',
    title='Payment Details',
    width=3589,
    height=2268,
    controls=[],
    tables=['clients', 'daybook'],
    source_path='w_pmntdetail.srw',
    report={'dataobject': 'd_pmntdetail', 'sql': 'SELECT daybook.tdate AS daybook_tdate, daybook.amount AS daybook_amount, daybookpart.vchno AS daybookpart_vchno, daybookpart.particular AS daybookpart_particular, daybookpart.duedate AS daybookpart_duedate FROM daybook, daybookpart WHERE daybook.slno = daybookpart.slno AND daybook.control <= :rlevel AND daybook.tdate between :rdate1 and :rdate2 AND daybook.accode = :rcode ORDER BY daybook.tdate ASC', 'args': ['rdate1', 'rdate2', 'rlevel', 'rcode', 'racname', 'ropbal', 'rclbal'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date', 'rlevel': 'number', 'rcode': 'string', 'racname': 'string', 'ropbal': 'decimal', 'rclbal': 'decimal'}, 'tables': ['daybook', 'daybookpart'], 'columns': [{'name': 'daybook_tdate', 'label': 'daybook_tdate', 'type': 'date'}, {'name': 'daybook_amount', 'label': 'daybook_amount', 'type': 'decimal'}, {'name': 'daybookpart_vchno', 'label': 'daybookpart_vchno', 'type': 'char'}, {'name': 'daybookpart_particular', 'label': 'daybookpart_particular', 'type': 'char'}, {'name': 'daybookpart_duedate', 'label': 'daybookpart_duedate', 'type': 'date'}]},
    opens=['w_clientshelp'],
)


class PaymentDetailsForm(GeneratedForm):
    """Payment Details"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 366, 0, 430, 92, taborder=10)
        self.add('editmask', 'em_date2', 1093, 0, 425, 92, taborder=20)
        self.add('commandbutton', 'cb_show', 2715, 0, 265, 100, text='Show', taborder=60)
        self.add('commandbutton', 'cb_1', 2994, 0, 256, 100, text='&Print', taborder=80)
        self.add('commandbutton', 'cb_2', 3264, 0, 256, 100, text='E&xit', taborder=70)
        self.add('statictext', 'st_2', 814, 8, 274, 76, text='Date To :')
        self.add('datawindow', 'dw_accode', 1888, 8, 402, 88, dataobject='d_cust', taborder=30)
        self.add('checkbox', 'cbx_all', 2373, 12, 187, 76, text='All')
        self.add('statictext', 'st_1', 0, 16, 352, 76, text='Date From :')
        self.add('statictext', 'st_3', 1559, 20, 325, 76, text='Customer :')
        self.add('datawindow', 'dw_acsummary', 5, 108, 3547, 2048, dataobject='d_pmntdetail', taborder=40)
        self.add('dropdownlistbox', 'ddlb_sort', 2661, 120, 640, 484, text='Date', items=['Customer', 'Date', 'Voucher No', 'Amount'], taborder=50)
        self.add('statictext', 'st_4', 2377, 124, 256, 76, text='Sort On :')
