"""Less Comparison Report — w_lesscomparisonrep.

Generated from the PowerBuilder window ``w_lesscomparisonrep.srw`` by
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
    name='w_lesscomparisonrep',
    title='Less Comparison Report',
    width=3675,
    height=2200,
    controls=[],
    tables=[],
    source_path='w_lesscomparisonrep.srw',
    report={'dataobject': 'd_lesscomparisonrep', 'sql': 'SELECT refinerym.tdate AS refinerym_tdate, (select sum(refineryd.mudless) from refineryd, refinerym rm where refineryd.slno = rm.slno and rm.tdate = refinerym.tdate and rm.control <= :rlevel) as trefmudless, (select max(rfm.tdate) from refinerym rfm where rfm.tdate < refinerym.tdate) as lastrefdate, (select sum(purchased.mud + purchased.lesswgt) from purchased,purchasem where purchased.slno = purchasem.slno and (purchasem.tdate = refinerym.tdate or (purchasem.tdate > lastrefdate and purchasem.tdate <= refinerym.tdate)) and purchasem.control <= :rlevel ) as tpurchmudless FROM refinerym WHERE refinerym.control <= :rlevel AND refinerym.tdate between :rdate1 and :rdate2 ORDER BY refinerym.tdate ASC', 'args': ['rdate1', 'rdate2', 'rlevel'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date', 'rlevel': 'number'}, 'tables': ['refinerym'], 'columns': [{'name': 'refinerym_tdate', 'label': 'refinerym_tdate', 'type': 'date'}, {'name': 'trefmudless', 'label': 'trefmudless', 'type': 'decimal'}, {'name': 'lastrefdate', 'label': 'lastrefdate', 'type': 'date'}, {'name': 'tpurchmudless', 'label': 'tpurchmudless', 'type': 'decimal'}]},
)


class LessComparisonReportForm(GeneratedForm):
    """Less Comparison Report"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 389, 0, 430, 100, taborder=10)
        self.add('editmask', 'em_date2', 1147, 0, 425, 100, taborder=20)
        self.add('commandbutton', 'cb_show', 1595, 0, 279, 100, text='&Show', taborder=30)
        self.add('commandbutton', 'cb_3', 2807, 0, 256, 100, text='Save &As', taborder=70)
        self.add('commandbutton', 'cb_1', 3077, 0, 265, 100, text='&Print', taborder=60)
        self.add('commandbutton', 'cb_2', 3342, 0, 265, 100, text='E&xit', taborder=50)
        self.add('statictext', 'st_1', 9, 16, 366, 64, text='Date From :')
        self.add('statictext', 'st_2', 837, 16, 302, 72, text='Date To :')
        self.add('datawindow', 'dw_1', 0, 100, 3625, 1976, dataobject='d_lesscomparisonrep', taborder=40)
