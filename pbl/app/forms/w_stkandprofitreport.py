"""StockValue And Profit Report — w_stkandprofitreport.

Generated from the PowerBuilder window ``w_stkandprofitreport.srw`` by
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
    name='w_stkandprofitreport',
    title='StockValue And Profit Report',
    width=3621,
    height=2208,
    controls=[],
    tables=['stkandprofit'],
    source_path='w_stkandprofitreport.srw',
    report={'dataobject': 'd_stkandprof_profsummary', 'sql': 'SELECT stkandprofit.tdate AS stkandprofit_tdate, (select sum(stkprof.profit) from stkandprofit stkprof where stkprof.tdate = stkandprofit.tdate and stkprof.control <= :rlevel) as totprof FROM stkandprofit ORDER BY stkandprofit.tdate ASC', 'args': ['rdate1', 'rdate2', 'rlevel'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date', 'rlevel': 'number'}, 'tables': ['stkandprofit'], 'columns': [{'name': 'tdate', 'label': 'tdate', 'type': 'date'}, {'name': 'totprof', 'label': 'totprof', 'type': 'decimal'}]},
)


class StockvalueAndProfitReportForm(GeneratedForm):
    """StockValue And Profit Report"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 224, 0, 430, 100, taborder=10)
        self.add('editmask', 'em_date2', 864, 0, 430, 100, taborder=20)
        self.add('commandbutton', 'cb_show', 2473, 0, 315, 100, text='&Show', taborder=30)
        self.add('commandbutton', 'cb_1', 2802, 0, 261, 100, text='Save &As', taborder=70)
        self.add('commandbutton', 'cb_print', 3072, 0, 265, 100, text='&Print', taborder=80)
        self.add('commandbutton', 'cb_exit', 3342, 0, 265, 100, text='E&xit', taborder=60)
        self.add('dropdownlistbox', 'ddlb_type', 1440, 4, 914, 740, text='Profit Summary', items=['Profit Summary', 'Profit Details', 'Stock Summary', 'Stock Details'], taborder=40)
        self.add('statictext', 'st_date2', 722, 8, 133, 76, text='To :')
        self.add('statictext', 'st_date1', 18, 12, 197, 76, text='From :')
        self.add('datawindow', 'dw_1', 0, 108, 3602, 2008, dataobject='d_stkandprof_profsummary', taborder=50)
