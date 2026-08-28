"""Stone Trans Analysis — w_stonetrans_analysis.

Generated from the PowerBuilder window ``w_stonetrans_analysis.srw`` by
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
    name='w_stonetrans_analysis',
    title='Stone Trans Analysis',
    width=3675,
    height=2300,
    controls=[],
    tables=[],
    source_path='w_stonetrans_analysis.srw',
    report={'dataobject': 'd_stonetrans_analysis', 'sql': "SELECT daybook.tdate AS daybook_tdate, (select sum(abs(td.stwgt)) from purchasem tm,purchased td where tm.slno = td.slno and tm.tdate = daybook.tdate and tm.control <= :rlevel) as purchstwgt, (select sum(abs(td.stprice)) from purchasem tm,purchased td where tm.slno = td.slno and tm.tdate = daybook.tdate and tm.control <= :rlevel) as purchstamt, (select sum(abs(td.stonewgt)) from salesm tm,salesd td where tm.slno = td.slno and tm.tdate = daybook.tdate and tm.control <= :rlevel) as salestwgt, (select sum(abs(td.stoneprice)) from salesm tm,salesd td where tm.slno = td.slno and tm.tdate = daybook.tdate and tm.control <= :rlevel) as salestamt, (select sum(abs(td.stonewgt)) from smithm tm,smithd td where tm.slno = td.slno and tm.tdate = daybook.tdate and td.givrec = 'G' and tm.control <= :rlevel) as jewlissuestwgt, (select sum(abs(td.stoneprice)) from smithm tm,smithd td where tm.slno = td.slno and tm.tdate = daybook.tdate and td.givrec = 'G' and tm.control <= :rlevel) as jewlissuestamt, (select sum(abs(td.stonewgt)) from smithm tm,smithd td where tm.slno = td.slno and tm.tdate = daybook.tdate and td.givrec = 'R' and tm.control <= :rlevel) as jewlrcptstwgt, (select sum(abs(td.stoneprice)) from smithm tm,smithd td where tm.slno = td.slno and tm.tdate = daybook.tdate and td.givrec = 'R' and tm.control <= :rlevel) as jewlrcptstamt FROM daybook ORDER BY daybook.tdate ASC", 'args': ['rdate1', 'rdate2', 'rlevel', 'rrate'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date', 'rlevel': 'number', 'rrate': 'decimal'}, 'tables': ['daybook'], 'columns': [{'name': 'tdate', 'label': 'Date', 'type': 'date'}, {'name': 'purchstwgt', 'label': 'purchstwgt', 'type': 'decimal'}, {'name': 'purchstamt', 'label': 'purchstamt', 'type': 'decimal'}, {'name': 'salestwgt', 'label': 'salestwgt', 'type': 'decimal'}, {'name': 'salestamt', 'label': 'salestamt', 'type': 'decimal'}, {'name': 'jewlissuestwgt', 'label': 'jewlissuestwgt', 'type': 'decimal'}, {'name': 'jewlissuestamt', 'label': 'jewlissuestamt', 'type': 'decimal'}, {'name': 'jewlrcptstwgt', 'label': 'jewlrcptstwgt', 'type': 'decimal'}, {'name': 'jewlrcptstamt', 'label': 'jewlrcptstamt', 'type': 'decimal'}]},
)


class StoneTransAnalysisForm(GeneratedForm):
    """Stone Trans Analysis"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 219, 0, 366, 92, taborder=10)
        self.add('editmask', 'em_date2', 914, 0, 366, 92, taborder=20)
        self.add('editmask', 'em_rate', 1696, 0, 402, 92, taborder=30)
        self.add('commandbutton', 'cb_show', 2542, 0, 261, 96, text='&Show', taborder=40)
        self.add('commandbutton', 'cb_3', 2811, 0, 261, 96, text='Save &As', taborder=70)
        self.add('commandbutton', 'cb_1', 3077, 0, 265, 96, text='&Print', taborder=80)
        self.add('commandbutton', 'cb_2', 3342, 0, 265, 96, text='E&xit', taborder=60)
        self.add('statictext', 'st_2', 750, 4, 146, 72, text='To :')
        self.add('statictext', 'st_1', 0, 8, 210, 64, text='From :')
        self.add('statictext', 'st_3', 1403, 8, 279, 64, text='Rate :')
        self.add('datawindow', 'dw_1', 0, 104, 3616, 2084, dataobject='d_stonetrans_analysis', taborder=50)
