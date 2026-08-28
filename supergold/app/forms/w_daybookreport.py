"""Day Book — w_daybookreport.

Generated from the PowerBuilder window ``w_daybookreport.srw`` by
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
    name='w_daybookreport',
    title='Day Book',
    width=3657,
    height=2376,
    controls=[],
    tables=['daybook', 'accountm', 'salesm', 'purchasem', 'daybookpart'],
    source_path='w_daybookreport.srw',
    report={'dataobject': 'd_daybook3', 'sql': "SELECT daybook.tdate AS daybook_tdate, daybook.accode AS daybook_accode, accountm.name AS accountm_name, daybookpart.vchno AS daybookpart_vchno, (select sum(db.amount) from daybook db, daybookpart dbp where db.slno = dbp.slno and db.tdate = daybook.tdate and db.accode = daybook.accode and dbp.vchno = daybookpart.vchno and db.control <= :rlevel) as daybook_amount, ('') as part FROM accountm, daybook, daybookpart WHERE accountm.accode = daybook.accode AND daybook.slno = daybookpart.slno AND daybook.control <= :rlevel AND daybook.tdate >= :rdate AND daybook.tdate <= :rdate2 AND accountm.accode <> 'CASH' ORDER BY daybook.tdate ASC", 'args': ['rdate', 'rdate2', 'rlevel', 'rOpbal', 'rClbal'], 'arg_types': {'rdate': 'date', 'rdate2': 'date', 'rlevel': 'number', 'rOpbal': 'decimal', 'rClbal': 'decimal'}, 'tables': ['accountm', 'daybook', 'daybookpart'], 'columns': [{'name': 'daybook_tdate', 'label': 'daybook_tdate', 'type': 'date'}, {'name': 'daybook_accode', 'label': 'daybook_accode', 'type': 'char'}, {'name': 'accountm_name', 'label': 'accountm_name', 'type': 'char'}, {'name': 'daybookpart_vchno', 'label': 'daybookpart_vchno', 'type': 'char'}, {'name': 'daybook_amount', 'label': 'daybook_amount', 'type': 'decimal'}, {'name': 'part', 'label': 'part', 'type': 'char'}]},
)


class DayBookForm(GeneratedForm):
    """Day Book"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 411, 0, 430, 100, taborder=10)
        self.add('editmask', 'em_date2', 1266, 0, 430, 100, taborder=20)
        self.add('commandbutton', 'cb_show', 1801, 0, 315, 100, text='&Show', taborder=30)
        self.add('dropdownlistbox', 'ddlb_type', 2235, 4, 535, 516, text='Form 1', items=['Form 1', 'Form 2', 'Form 3', 'Form 4'], taborder=40)
        self.add('commandbutton', 'cb_1', 2793, 4, 261, 100, text='Save &As', taborder=70)
        self.add('commandbutton', 'cb_print', 3063, 4, 265, 100, text='&Print', taborder=80)
        self.add('commandbutton', 'cb_exit', 3333, 4, 265, 100, text='E&xit', taborder=60)
        self.add('statictext', 'st_date1', 32, 16, 370, 76, text='Date From :')
        self.add('statictext', 'st_date2', 887, 16, 370, 76, text='Date  To :')
        self.add('commandbutton', 'cb_del', 1271, 108, 425, 76, text='Del', taborder=60)
        self.add('commandbutton', 'cb_sort', 1801, 108, 315, 76, text='So&rt', taborder=70)
        self.add('checkbox', 'cbx_breakday', 411, 112, 507, 64, text='Break Day Total')
        self.add('checkbox', 'cbx_withdiff', 2235, 112, 448, 64, text='With Diff Only')
        self.add('checkbox', 'cbx_speed', 2793, 112, 251, 64, text='Speed')
        self.add('checkbox', 'cbx_newpage', 3058, 112, 379, 64, text='Page Skip')
        self.add('datawindow', 'dw_daybook', 0, 184, 3602, 1992, dataobject='d_daybook3', taborder=50)
