"""Cash Book — w_cashbookreport.

Generated from the PowerBuilder window ``w_cashbookreport.srw`` by
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
    name='w_cashbookreport',
    title='Cash Book',
    width=3648,
    height=2192,
    controls=[],
    tables=['accountm', 'daybook', 'salesm', 'spdmddet'],
    source_path='w_cashbookreport.srw',
    report={'dataobject': 'd_cashbook', 'sql': 'SELECT daybook.slno AS daybook_slno, daybook.tdate AS daybook_tdate, daybook.accode AS daybook_accode, daybook.amount AS daybook_amount, daybookpart.vchno AS daybookpart_vchno, daybookpart.particular AS daybookpart_particular, daybookpart.ic AS daybookpart_ic, (select accountm.name from accountm where accountm.accode = daybook.opaccode ) as othacname, (0) as sel FROM daybook, daybookpart WHERE daybook.slno = daybookpart.slno AND daybook.control <= :rlevel AND daybook.tdate >= :rdate1 AND daybook.accode = :rcode AND daybook.tdate <= :rdate2 ORDER BY daybook.tdate ASC, daybook.slno ASC', 'args': ['rdate1', 'rdate2', 'rcode', 'rlevel', 'ropbal'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date', 'rcode': 'string', 'rlevel': 'number', 'ropbal': 'decimal'}, 'tables': ['daybook', 'daybookpart'], 'columns': [{'name': 'daybook_slno', 'label': 'daybook_slno', 'type': 'decimal'}, {'name': 'daybook_tdate', 'label': 'daybook_tdate', 'type': 'date'}, {'name': 'daybook_accode', 'label': 'daybook_accode', 'type': 'char'}, {'name': 'daybook_amount', 'label': 'daybook_amount', 'type': 'decimal'}, {'name': 'daybookpart_vchno', 'label': 'daybookpart_vchno', 'type': 'char'}, {'name': 'daybookpart_particular', 'label': 'daybookpart_particular', 'type': 'char'}, {'name': 'cothacname', 'label': 'cothacname', 'type': 'char'}, {'name': 'daybookpart_ic', 'label': 'daybookpart_ic', 'type': 'char'}, {'name': 'sel', 'label': 'sel', 'type': 'long'}]},
    opens=['w_sales_view', 'w_diamond_sales_print'],
)


class CashBookForm(GeneratedForm):
    """Cash Book"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 453, 4, 430, 92, taborder=10)
        self.add('editmask', 'em_date2', 1243, 4, 425, 92, taborder=20)
        self.add('commandbutton', 'cb_show', 1696, 4, 315, 96, text='&Show', taborder=30)
        self.add('commandbutton', 'cb_sort', 2112, 4, 261, 96, text='So&rt', taborder=40)
        self.add('commandbutton', 'cb_saveas', 2775, 4, 265, 96, text='Save &As', taborder=70)
        self.add('commandbutton', 'cb_print', 3058, 4, 265, 96, text='&Print', taborder=90)
        self.add('commandbutton', 'cb_exit', 3342, 4, 265, 96, text='E&xit', taborder=80)
        self.add('statictext', 'st_1', 0, 8, 375, 64, text='Date From :')
        self.add('statictext', 'st_2', 882, 8, 283, 72, text='Date To :')
        self.add('checkbox', 'cbx_speed', 2464, 8, 251, 76, text='Speed')
        self.add('datawindow', 'dw_ic', 384, 100, 695, 88, dataobject='d_incharge_code', taborder=50)
        self.add('statictext', 'st_20', 64, 104, 311, 80, text='Incharge :')
        self.add('checkbox', 'cbx_ic', 1088, 108, 87, 76)
        self.add('statictext', 'st_status', 1184, 108, 389, 64)
        self.add('checkbox', 'cbx_selonly', 1696, 108, 402, 68, text='Sel Only')
        self.add('checkbox', 'cbx_breakday', 2464, 112, 507, 76, text='Break Day Total')
        self.add('checkbox', 'cbx_newpage', 3008, 112, 379, 80, text='Page Skip')
        self.add('datawindow', 'dw_cashbook', 0, 192, 3616, 1876, dataobject='d_cashbook', taborder=60)
        self.add('commandbutton', 'cb_billprint', 3031, 196, 325, 88, text='Bill Print', taborder=60)
