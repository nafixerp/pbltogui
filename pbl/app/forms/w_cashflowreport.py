"""Cash Flow Statement — w_cashflowreport.

Generated from the PowerBuilder window ``w_cashflowreport.srw`` by
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
    name='w_cashflowreport',
    title='Cash Flow Statement',
    width=3666,
    height=2352,
    controls=[],
    tables=['accountm', 'daybook'],
    source_path='w_cashflowreport.srw',
    report={'dataobject': 'd_cashflowreport', 'sql': 'SELECT daybook.tdate AS daybook_tdate, (select sum(abs(db.amount)) from daybook db where db.tdate = daybook.tdate and db.accode = :rcode and db.amount < 0) as tdebitamt, (select sum(db.amount) from daybook db where db.tdate = daybook.tdate and db.accode = :rcode and db.amount > 0) as tcreditamt, (select sum(db.amount) from daybook db where db.tdate <= daybook.tdate and db.accode = :rcode ) as tamt FROM daybook WHERE daybook.control <= :rlevel AND daybook.tdate >= :rdate1 AND daybook.accode = :rcode AND daybook.tdate <= :rdate2 ORDER BY daybook.tdate ASC', 'computes': [{'name': 'bal', 'expression': '-(  ropbal + if(isnull( tamt ), 0, tamt) )', 'format': '##########0.00', 'label': 'bal', 'band': 'detail'}, {'name': 'compute_3', 'expression': 'sum(tdebitamt for all)', 'format': '########0.00', 'label': 'compute_3', 'band': 'summary'}, {'name': 'compute_2', 'expression': 'sum(tcreditamt for all)', 'format': '########0.00', 'label': 'compute_2', 'band': 'summary'}], 'args': ['rdate1', 'rdate2', 'rcode', 'rlevel', 'ropbal'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date', 'rcode': 'string', 'rlevel': 'number', 'ropbal': 'decimal'}, 'tables': ['daybook'], 'columns': [{'name': 'daybook_tdate', 'label': 'daybook_tdate', 'type': 'date'}, {'name': 'tdebitamt', 'label': 'tdebitamt', 'type': 'decimal'}, {'name': 'tcreditamt', 'label': 'tcreditamt', 'type': 'decimal'}, {'name': 'tamt', 'label': 'tamt', 'type': 'decimal'}]},
)


class CashFlowStatementForm(GeneratedForm):
    """Cash Flow Statement"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 384, 4, 398, 96, taborder=10)
        self.add('editmask', 'em_date2', 1175, 4, 393, 96, taborder=20)
        self.add('commandbutton', 'cb_show', 1696, 4, 315, 96, text='&Show', taborder=30)
        self.add('commandbutton', 'cb_sort', 2112, 4, 261, 96, text='So&rt', taborder=40)
        self.add('commandbutton', 'cb_saveas', 2775, 4, 265, 96, text='Save &As', taborder=70)
        self.add('commandbutton', 'cb_print', 3049, 4, 265, 96, text='&Print', taborder=90)
        self.add('commandbutton', 'cb_exit', 3314, 4, 265, 96, text='E&xit', taborder=80)
        self.add('statictext', 'st_1', 0, 8, 375, 64, text='Date From :')
        self.add('statictext', 'st_2', 882, 8, 283, 72, text='Date To :')
        self.add('checkbox', 'cbx_speed', 2464, 8, 251, 76, text='Speed')
        self.add('datawindow', 'dw_cashbook', 14, 112, 3625, 2144, dataobject='d_cashflowreport', taborder=60)
