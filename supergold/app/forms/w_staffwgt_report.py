"""Wgt Trans Report — w_staffwgt_report.

Generated from the PowerBuilder window ``w_staffwgt_report.srw`` by
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
    name='w_staffwgt_report',
    title='Wgt Trans Report',
    width=3666,
    height=2204,
    controls=[],
    tables=[],
    source_path='w_staffwgt_report.srw',
    grid={'control': 'dw_acsummary', 'dataobject': 'd_staffwgtrep_stklist', 'table': 'items', 'keys': ['code'], 'columns': [{'name': 'code', 'label': 'code', 'type': 'char'}, {'name': 'name', 'label': 'Item', 'type': 'char'}, {'name': 'opqtyi', 'label': 'opqtyi', 'type': 'long'}, {'name': 'opwgti', 'label': 'opwgti', 'type': 'decimal'}, {'name': 'opqtyr', 'label': 'opqtyr', 'type': 'long'}, {'name': 'opwgtr', 'label': 'opwgtr', 'type': 'decimal'}, {'name': 'opqtys', 'label': 'opqtys', 'type': 'long'}, {'name': 'opwgts', 'label': 'opwgts', 'type': 'decimal'}, {'name': 'totqtyi', 'label': 'totqtyi', 'type': 'long'}, {'name': 'totwgti', 'label': 'totwgti', 'type': 'decimal'}, {'name': 'totqtyr', 'label': 'totqtyr', 'type': 'long'}, {'name': 'totwgtr', 'label': 'totwgtr', 'type': 'decimal'}, {'name': 'totqtys', 'label': 'totqtys', 'type': 'long'}, {'name': 'totwgts', 'label': 'totwgts', 'type': 'decimal'}, {'name': 'opqtys2', 'label': 'opqtys2', 'type': 'long'}, {'name': 'totwgts2', 'label': 'totwgts2', 'type': 'decimal'}, {'name': 'totqtys2', 'label': 'totqtys2', 'type': 'long'}, {'name': 'opwgts2', 'label': 'opwgts2', 'type': 'decimal'}, {'name': 'rate', 'label': 'rate', 'type': 'decimal'}]},
    report={'dataobject': 'd_staffwgtrep_stklist', 'sql': "SELECT items.code AS items_code, items.name AS items_name, items.rate AS items_rate, (select sum(staffwgtd.qty) from staffwgtd,staffwgtm where staffwgtd.slno = staffwgtm.slno and staffwgtm.staff = :rstaff and staffwgtm.ttype = 'I' and staffwgtm.tdate < :rdate1 and staffwgtm.control <= :rlevel and staffwgtd.code = items.code) as opqtyi, (select sum(staffwgtd.weight) from staffwgtd,staffwgtm where staffwgtd.slno = staffwgtm.slno and staffwgtm.staff = :rstaff and staffwgtm.ttype = 'I' and staffwgtm.tdate < :rdate1 and staffwgtm.control <= :rlevel and staffwgtd.code = items.code) as opwgti, (select sum(staffwgtd.qty) from staffwgtd,staffwgtm where staffwgtd.slno = staffwgtm.slno and staffwgtm.staff = :rstaff and staffwgtm.ttype = 'R' and staffwgtm.tdate < :rdate1 and staffwgtm.control <= :rlevel and staffwgtd.code = items.code) as opqtyr, (select sum(staffwgtd.weight) from staffwgtd,staffwgtm where staffwgtd.slno = staffwgtm.slno and staffwgtm.staff = :rstaff and staffwgtm.ttype = 'R' and staffwgtm.tdate < :rdate1 and staffwgtm.control <= :rlevel and staffwgtd.code = items.code) as opwgtr, (select sum(staffwgtd.qty) from staffwgtd,staffwgtm where staffwgtd.slno = staffwgtm.slno and staffwgtm.staff = :rstaff and staffwgtm.ttype = 'S' and staffwgtm.tdate < :rdate1 and staffwgtm.control <= :rlevel and staffwgtd.code = items.code) as opqtys, (select sum(staffwgtd.weight) from staffwgtd,staffwgtm where staffwgtd.slno = staffwgtm.slno and staffwgtm.staff = :rstaff and staffwgtm.ttype = 'S' and staffwgtm.tdate < :rdate1 and staffwgtm.control <= :rlevel and staffwgtd.code = items.code) as opwgts, (select sum(staffwgtd.qty) from staffwgtd,staffwgtm where staffwgtd.slno = staffwgtm.slno and staffwgtm.staff = :rstaff and staffwgtm.ttype = 'I' and staffwgtm.tdate >= :rdate1 and staffwgtm.tdate <= :rdate2 and staffwgtm.control <= :rlevel and staffwgtd.code = items.code) as totqtyi, (select sum(staffwgtd.weight) from staffwgtd,staffwgtm where staffwgtd.slno = staffwgtm.slno and staffwgtm.staff = :rstaff and staffwgtm.ttype = 'I' and staffwgtm.tdate >= :rdate1 and staffwgtm.tdate <= :rdate2 and staffwgtm.control <= :rlevel and staffwgtd.code = items.code) as totwgti, (select sum(staffwgtd.qty) from staffwgtd,staffwgtm where staffwgtd.slno = staffwgtm.slno and staffwgtm.staff = :rstaff and staffwgtm.ttype = 'R' and staffwgtm.tdate >= :rdate1 and staffwgtm.tdate <= :rdate2 and staffwgtm.control <= :rlevel and staffwgtd.code = items.code) as totqtyr, (select sum(staffwgtd.weight) from staffwgtd,staffwgtm where staffwgtd.slno = staffwgtm.slno and staffwgtm.staff = :rstaff and staffwgtm.ttype = 'R' and staffwgtm.tdate >= :rdate1 and staffwgtm.tdate <= :rdate2 and staffwgtm.control <= :rlevel and staffwgtd.code = items.code) as totwgtr, (select sum(staffwgtd.qty) from staffwgtd,staffwgtm where staffwgtd.slno = staffwgtm.slno and staffwgtm.staff = :rstaff and staffwgtm.ttype = 'S' and staffwgtm.tdate >= :rdate1 and staffwgtm.tdate <= :rdate2 and staffwgtm.control <= :rlevel and staffwgtd.code = items.code) as totqtys, (select sum(staffwgtd.weight) from staffwgtd,staffwgtm where staffwgtd.slno = staffwgtm.slno and staffwgtm.staff = :rstaff and staffwgtm.ttype = 'S' and staffwgtm.tdate >= :rdate1 and staffwgtm.tdate <= :rdate2 and staffwgtm.control <= :rlevel and staffwgtd.code = items.code) as totwgts, (select sum(salesd.qty) from salesd,salesm where salesd.slno = salesm.slno and salesm.smcode = :rstaff and salesm.tdate < :rdate1 and salesm.control <= :rlevel and salesd.code = items.code) as opqtys2, (select sum(salesd.weight) from salesd,salesm where salesd.slno = salesm.slno and salesm.smcode = :rstaff and salesm.tdate >= :rdate1 and salesm.tdate <= :rdate2 and salesm.control <= :rlevel and salesd.code = items.code) as totwgts2, (select sum(salesd.qty) from salesd,salesm where salesd.slno = salesm.slno and salesm.smcode = :rstaff and salesm.tdate >= :rdate1 and salesm.tdate <= :rdate2 and salesm.control <= :rlevel and salesd.code = items.code) as totqtys2, (select sum(salesd.weight) from salesd,salesm where salesd.slno = salesm.slno and salesm.smcode = :rstaff and salesm.tdate < :rdate1 and salesm.control <= :rlevel and salesd.code = items.code) as opwgts2 FROM items ORDER BY items.name ASC", 'args': ['rdate1', 'rdate2', 'rlevel', 'rstaff'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date', 'rlevel': 'number', 'rstaff': 'string'}, 'tables': ['items'], 'columns': [{'name': 'code', 'label': 'code', 'type': 'char'}, {'name': 'name', 'label': 'Item', 'type': 'char'}, {'name': 'opqtyi', 'label': 'opqtyi', 'type': 'long'}, {'name': 'opwgti', 'label': 'opwgti', 'type': 'decimal'}, {'name': 'opqtyr', 'label': 'opqtyr', 'type': 'long'}, {'name': 'opwgtr', 'label': 'opwgtr', 'type': 'decimal'}, {'name': 'opqtys', 'label': 'opqtys', 'type': 'long'}, {'name': 'opwgts', 'label': 'opwgts', 'type': 'decimal'}, {'name': 'totqtyi', 'label': 'totqtyi', 'type': 'long'}, {'name': 'totwgti', 'label': 'totwgti', 'type': 'decimal'}, {'name': 'totqtyr', 'label': 'totqtyr', 'type': 'long'}, {'name': 'totwgtr', 'label': 'totwgtr', 'type': 'decimal'}, {'name': 'totqtys', 'label': 'totqtys', 'type': 'long'}, {'name': 'totwgts', 'label': 'totwgts', 'type': 'decimal'}, {'name': 'opqtys2', 'label': 'opqtys2', 'type': 'long'}, {'name': 'totwgts2', 'label': 'totwgts2', 'type': 'decimal'}, {'name': 'totqtys2', 'label': 'totqtys2', 'type': 'long'}, {'name': 'opwgts2', 'label': 'opwgts2', 'type': 'decimal'}, {'name': 'rate', 'label': 'rate', 'type': 'decimal'}]},
)


class WgtTransReportForm(GeneratedForm):
    """Wgt Trans Report"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 210, 0, 352, 100, taborder=10)
        self.add('editmask', 'em_date2', 727, 0, 347, 100, taborder=20)
        self.add('commandbutton', 'cb_show', 2615, 0, 251, 100, text='&Show', taborder=30)
        self.add('commandbutton', 'cb_3', 2875, 0, 247, 100, text='Save &As', taborder=70)
        self.add('commandbutton', 'cb_1', 3131, 0, 247, 100, text='&Print', taborder=80)
        self.add('commandbutton', 'cb_2', 3383, 0, 247, 100, text='E&xit', taborder=60)
        self.add('dropdownlistbox', 'ddlb_type', 2190, 4, 411, 456, text='Stk List', items=['Details', 'Stk List'], taborder=32)
        self.add('datawindow', 'dw_smcode', 1307, 8, 672, 88, dataobject='d_smancode', taborder=40)
        self.add('statictext', 'st_1', 0, 12, 201, 64, text='From :')
        self.add('statictext', 'st_2', 590, 12, 128, 72, text='To :')
        self.add('statictext', 'st_4', 1993, 12, 192, 76, text='Type :')
        self.add('statictext', 'st_3', 1083, 16, 215, 76, text='SMan :')
        self.add('datawindow', 'dw_acsummary', 0, 108, 3634, 1988, dataobject='d_staffwgtrep_stklist', taborder=50)
