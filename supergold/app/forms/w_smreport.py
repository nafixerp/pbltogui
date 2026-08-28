"""Sales Man Report — w_smreport.

Generated from the PowerBuilder window ``w_smreport.srw`` by
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
    name='w_smreport',
    title='Sales Man Report',
    width=3666,
    height=2204,
    controls=[],
    tables=[],
    source_path='w_smreport.srw',
    grid={'control': 'dw_acsummary', 'dataobject': 'd_smreport', 'table': 'sman', 'keys': ['code'], 'columns': [{'name': 'name', 'label': 'SM Name', 'type': 'char'}, {'name': 'code', 'label': 'code', 'type': 'char'}, {'name': 'ctsalesamt', 'label': 'ctsalesamt', 'type': 'decimal'}, {'name': 'ctssaleswgt', 'label': 'Total Sales\nAmount', 'type': 'decimal'}, {'name': 'ctgsaleswgt', 'label': 'Total OG\nPurch', 'type': 'decimal'}, {'name': 'ctgsretwgt', 'label': 'ctgsretwgt', 'type': 'decimal'}, {'name': 'ctogwgt', 'label': 'Total Gold\nSold Wgt.', 'type': 'decimal'}, {'name': 'ctoswgt1', 'label': 'ctoswgt1', 'type': 'decimal'}, {'name': 'ctgsretamt', 'label': 'ctgsretamt', 'type': 'decimal'}, {'name': 'salesamt', 'label': 'salesamt', 'type': 'decimal'}, {'name': 'rcvdamt', 'label': 'rcvdamt', 'type': 'decimal'}, {'name': 'psaleswgt', 'label': 'psaleswgt', 'type': 'decimal'}, {'name': 'dmdsaleswgt', 'label': 'dmdsaleswgt', 'type': 'decimal'}, {'name': 'watchsalesqty', 'label': 'watchsalesqty', 'type': 'long'}, {'name': 'psalesamt', 'label': 'psalesamt', 'type': 'decimal'}, {'name': 'dmdsalesamt', 'label': 'dmdsalesamt', 'type': 'decimal'}, {'name': 'watchsalesamt', 'label': 'watchsalesamt', 'type': 'decimal'}, {'name': 'salesnos', 'label': 'salesnos', 'type': 'long'}]},
    report={'dataobject': 'd_smreport', 'sql': "SELECT sman.name AS sman_name, sman.code AS sman_code, (select sum(salesd.amount) from salesd,salesm where salesm.slno = salesd.slno and salesm.control <= :rlevel and salesm.smcode = sman.code and salesm.tdate between :rdate1 and :rdate2)  as ctsalesamt, (select sum(salesd.weight) from salesd,salesm,items where salesm.slno = salesd.slno and items.code = salesd.code and salesm.control <= :rlevel and salesm.smcode = sman.code and items.itype = 'S' and salesm.tdate between :rdate1 and :rdate2)  as ctssaleswgt, (select sum(salesd.weight) from salesd,salesm,items where salesm.slno = salesd.slno and items.code = salesd.code and salesm.control <= :rlevel and salesm.smcode = sman.code and items.itype = 'G' and salesm.tdate between :rdate1 and :rdate2)  as ctgsaleswgt, (select sum(salesrd.weight) from salesrd,salesrm,items where salesrm.slno = salesrd.slno and items.code = salesrd.code and salesrm.control <= :rlevel and salesrm.smcode = sman.code and items.itype = 'G' and salesrm.tdate between :rdate1 and :rdate2)  as ctgsretwgt, (select sum(purchased.weight) from purchased,purchasem where purchasem.slno = purchased.slno and purchased.code = 'OG' and purchasem.control <= :rlevel and purchasem.smcode = sman.code and purchasem.tdate between :rdate1 and :rdate2)  as ctogwgt, (select sum(purchased.weight) from purchased,purchasem where purchasem.slno = purchased.slno and purchased.code = 'OS' and purchasem.control <= :rlevel and purchasem.smcode = sman.code and purchasem.tdate between :rdate1 and :rdate2)  as ctoswgt1, (select sum(salesrd.amount) from salesrd,salesrm,items where salesrm.slno = salesrd.slno and items.code = salesrd.code and salesrm.control <= :rlevel and salesrm.smcode = sman.code and salesrm.tdate between :rdate1 and :rdate2)  as ctgsretamt, (select sum(salesm.netamt) from salesm where salesm.control <= :rlevel and salesm.smcode = sman.code and salesm.tdate between :rdate1 and :rdate2)  as salesamt, (select sum(salesm.ramt) from salesm where salesm.control <= :rlevel and salesm.smcode = sman.code and salesm.tdate between :rdate1 and :rdate2)  as rcvdamt, (select sum(salesd.weight) from salesd,salesm,items where salesm.slno = salesd.slno and items.code = salesd.code and salesm.tdate >= :rdate1 and salesm.tdate <= :rdate2 and salesm.control <= :rlevel and items.itype = 'P' and salesm.smcode = sman.code ) as psaleswgt, (select sum(salesd.dmdwgt) from salesd,salesm,items where salesm.slno = salesd.slno and items.code = salesd.code and salesm.tdate >= :rdate1 and salesm.tdate <= :rdate2 and salesm.control <= :rlevel and salesm.smcode = sman.code) as dmdsaleswgt, (select sum(salesd.qty) from salesd,salesm,items where salesm.slno = salesd.slno and items.code = salesd.code and salesm.tdate >= :rdate1 and salesm.tdate <= :rdate2 and salesm.control <= :rlevel and items.dmdplt = 'W' and salesm.smcode = sman.code) as watchsalesqty, (select sum(salesm.netamt) from salesd,salesm,items where salesm.slno = salesd.slno and items.code = salesd.code and salesm.tdate >= :rdate1 and salesm.tdate <= :rdate2 and salesm.control <= :rlevel and items.itype = 'P' and salesm.smcode = sman.code ) as psalesamt, (select sum(salesm.netamt) from salesd,salesm,items where salesm.slno = salesd.slno and items.code = salesd.code and salesm.tdate >= :rdate1 and salesm.tdate <= :rdate2 and salesm.control <= :rlevel and salesm.smcode = sman.code and salesd.dmdwgt > 0) as dmdsalesamt, (select sum(salesd.amount) from salesd,salesm,items where salesm.slno = salesd.slno and items.code = salesd.code and salesm.tdate >= :rdate1 and salesm.tdate <= :rdate2 and salesm.control <= :rlevel and items.dmdplt = 'W' and salesm.smcode = sman.code) as watchsalesamt, (select count(salesm.slno) from salesm where salesm.tdate >= :rdate1 and salesm.tdate <= :rdate2 and salesm.control <= :rlevel and salesm.smcode = sman.code ) as salesnos FROM sman ORDER BY sman.name ASC", 'args': ['rdate1', 'rdate2', 'rlevel'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date', 'rlevel': 'number'}, 'tables': ['sman'], 'columns': [{'name': 'name', 'label': 'SM Name', 'type': 'char'}, {'name': 'code', 'label': 'code', 'type': 'char'}, {'name': 'ctsalesamt', 'label': 'ctsalesamt', 'type': 'decimal'}, {'name': 'ctssaleswgt', 'label': 'Total Sales\nAmount', 'type': 'decimal'}, {'name': 'ctgsaleswgt', 'label': 'Total OG\nPurch', 'type': 'decimal'}, {'name': 'ctgsretwgt', 'label': 'ctgsretwgt', 'type': 'decimal'}, {'name': 'ctogwgt', 'label': 'Total Gold\nSold Wgt.', 'type': 'decimal'}, {'name': 'ctoswgt1', 'label': 'ctoswgt1', 'type': 'decimal'}, {'name': 'ctgsretamt', 'label': 'ctgsretamt', 'type': 'decimal'}, {'name': 'salesamt', 'label': 'salesamt', 'type': 'decimal'}, {'name': 'rcvdamt', 'label': 'rcvdamt', 'type': 'decimal'}, {'name': 'psaleswgt', 'label': 'psaleswgt', 'type': 'decimal'}, {'name': 'dmdsaleswgt', 'label': 'dmdsaleswgt', 'type': 'decimal'}, {'name': 'watchsalesqty', 'label': 'watchsalesqty', 'type': 'long'}, {'name': 'psalesamt', 'label': 'psalesamt', 'type': 'decimal'}, {'name': 'dmdsalesamt', 'label': 'dmdsalesamt', 'type': 'decimal'}, {'name': 'watchsalesamt', 'label': 'watchsalesamt', 'type': 'decimal'}, {'name': 'salesnos', 'label': 'salesnos', 'type': 'long'}]},
)


class SalesManReportForm(GeneratedForm):
    """Sales Man Report"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 379, 0, 430, 100, taborder=10)
        self.add('editmask', 'em_date2', 1138, 0, 425, 100, taborder=20)
        self.add('commandbutton', 'cb_show', 1618, 0, 261, 100, text='&Show', taborder=30)
        self.add('commandbutton', 'cb_3', 2715, 8, 256, 96, text='Save &As', taborder=60)
        self.add('commandbutton', 'cb_1', 2981, 8, 256, 96, text='&Print', taborder=70)
        self.add('commandbutton', 'cb_2', 3237, 8, 256, 96, text='E&xit', taborder=50)
        self.add('statictext', 'st_1', 0, 16, 366, 64, text='Date From :')
        self.add('statictext', 'st_2', 827, 16, 302, 72, text='Date To :')
        self.add('datawindow', 'dw_acsummary', 0, 108, 3634, 1988, dataobject='d_smreport', taborder=40)
        self.add('checkbox', 'cbx_speed', 2976, 120, 393, 80, text='Speed Print')
