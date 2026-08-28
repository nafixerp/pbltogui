"""VA Check Report — w_salesvarep.

Generated from the PowerBuilder window ``w_salesvarep.srw`` by
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
    name='w_salesvarep',
    title='VA Check Report',
    width=3648,
    height=2220,
    controls=[],
    tables=[],
    source_path='w_salesvarep.srw',
    grid={'control': 'dw_saleregister', 'dataobject': 'd_salesvarep', 'table': 'salesm', 'keys': ['slno'], 'columns': [{'name': 'slno', 'label': 'salesm_slno', 'type': 'decimal'}, {'name': 'tdate', 'label': 'salesm_tdate', 'type': 'date'}, {'name': 'billno', 'label': 'salesm_billno', 'type': 'char'}, {'name': 'custname', 'label': 'salesm_custname', 'type': 'char'}, {'name': 'billamt', 'label': 'salesm_billamt', 'type': 'decimal'}, {'name': 'status', 'label': 'salesm_status', 'type': 'long'}, {'name': 'discount', 'label': 'salesm_discount', 'type': 'decimal'}, {'name': 'discperc', 'label': 'discperc', 'type': 'decimal'}, {'name': 'ramt', 'label': 'salesm_ramt', 'type': 'decimal'}, {'name': 'eamt', 'label': 'salesm_eamt', 'type': 'decimal'}, {'name': 'staxamt', 'label': 'salesm_staxamt', 'type': 'decimal'}, {'name': 'duedate', 'label': 'salesm_duedate', 'type': 'date'}, {'name': 'sretamt', 'label': 'salesm_sretamt', 'type': 'decimal'}, {'name': 'ramtafter', 'label': 'salesm_ramtafter', 'type': 'decimal'}, {'name': 'round', 'label': 'round', 'type': 'decimal'}, {'name': 'advance', 'label': 'advance', 'type': 'decimal'}, {'name': 'billtype', 'label': 'billtype', 'type': 'char'}, {'name': 'totalva', 'label': 'totalva', 'type': 'decimal'}, {'name': 'totalstamt', 'label': 'totalstamt', 'type': 'decimal'}, {'name': 'totalwgt', 'label': 'totalwgt', 'type': 'decimal'}]},
    report={'dataobject': 'd_salesvarep', 'sql': 'SELECT "salesm"."slno",   \r\n\t\t\t"salesm"."tdate",   \r\n\t\t\t"salesm"."billno",   \r\n\t\t\t"salesm"."custname",   \r\n\t\t\t"salesm"."billamt",   \r\n\t\t\t"salesm"."status",   \r\n\t\t\t"salesm"."discount",   \r\n\t\t\t"salesm"."discperc",   \r\n\t\t\t"salesm"."ramt",   \r\n\t\t\t"salesm"."eamt",   \r\n\t\t\t"salesm"."staxamt",   \r\n\t\t\t"salesm"."duedate",   \r\n\t\t\t"salesm"."sretamt",   \r\n\t\t\t"salesm"."ramtafter",   \r\n\t\t\t"salesm"."round",   \r\n\t\t\t"salesm"."advance",\r\n\t\t\t"salesm"."billtype",\r\n\t\t\t(select sum(salesd.mcharge + salesd.wastage * salesd.rate) from salesd,items  where salesd.slno = salesm.slno and items.code = salesd.code and items.itype = \'G\') as totalva,   \r\n\t\t\t(select sum(salesd.stoneprice) from salesd,items  where salesd.slno = salesm.slno and items.code = salesd.code and items.itype = \'G\') as totalstamt,   \r\n\t\t\t(select sum(salesd.weight - salesd.stonewgt) from salesd,items  where salesd.slno = salesm.slno and items.code = salesd.code and items.itype = \'G\') as totalwgt\r\n\t FROM "salesm"  \r\n\tWHERE ( salesm.tdate between :rdate1 and :rdate2 ) AND  \r\n\t\t\t( salesm.control <= :rlevel ) AND  \r\n\t\t\t( "salesm"."opbill" <> 1 )   \r\nORDER BY "salesm"."status" ASC,   \r\n\t\t\t"salesm"."tdate" ASC,   \r\n\t\t\t"salesm"."slno" ASC', 'args': ['rdate1', 'rdate2', 'rlevel'], 'arg_types': {}, 'tables': ['salesm'], 'columns': [{'name': 'salesm_slno', 'label': 'salesm_slno', 'type': 'decimal'}, {'name': 'salesm_tdate', 'label': 'salesm_tdate', 'type': 'date'}, {'name': 'salesm_billno', 'label': 'salesm_billno', 'type': 'char'}, {'name': 'salesm_custname', 'label': 'salesm_custname', 'type': 'char'}, {'name': 'salesm_billamt', 'label': 'salesm_billamt', 'type': 'decimal'}, {'name': 'salesm_status', 'label': 'salesm_status', 'type': 'long'}, {'name': 'salesm_discount', 'label': 'salesm_discount', 'type': 'decimal'}, {'name': 'discperc', 'label': 'discperc', 'type': 'decimal'}, {'name': 'salesm_ramt', 'label': 'salesm_ramt', 'type': 'decimal'}, {'name': 'salesm_eamt', 'label': 'salesm_eamt', 'type': 'decimal'}, {'name': 'salesm_staxamt', 'label': 'salesm_staxamt', 'type': 'decimal'}, {'name': 'salesm_duedate', 'label': 'salesm_duedate', 'type': 'date'}, {'name': 'salesm_sretamt', 'label': 'salesm_sretamt', 'type': 'decimal'}, {'name': 'salesm_ramtafter', 'label': 'salesm_ramtafter', 'type': 'decimal'}, {'name': 'round', 'label': 'round', 'type': 'decimal'}, {'name': 'advance', 'label': 'advance', 'type': 'decimal'}, {'name': 'billtype', 'label': 'billtype', 'type': 'char'}, {'name': 'totalva', 'label': 'totalva', 'type': 'decimal'}, {'name': 'totalstamt', 'label': 'totalstamt', 'type': 'decimal'}, {'name': 'totalwgt', 'label': 'totalwgt', 'type': 'decimal'}]},
)


class VaCheckReportForm(GeneratedForm):
    """VA Check Report"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 215, 0, 425, 92, taborder=10)
        self.add('editmask', 'em_date2', 855, 0, 425, 92, taborder=20)
        self.add('datawindow', 'dw_billtype', 1531, 0, 425, 88, dataobject='d_billtypecode', taborder=50)
        self.add('commandbutton', 'cb_show', 2240, 0, 293, 96, text='&Show', taborder=30)
        self.add('commandbutton', 'cb_sort', 2601, 0, 247, 92, text='So&rt', taborder=40)
        self.add('commandbutton', 'cb_1', 2880, 0, 270, 92, text='Save &As', taborder=80)
        self.add('commandbutton', 'cb_print', 3154, 0, 233, 92, text='&Print', taborder=60)
        self.add('commandbutton', 'cb_exit', 3392, 0, 233, 92, text='E&xit', taborder=70)
        self.add('checkbox', 'cbx_btype', 1961, 4, 78, 76)
        self.add('statictext', 'st_10', 5, 12, 201, 64, text='From :')
        self.add('statictext', 'st_11', 699, 12, 146, 72, text='To :')
        self.add('statictext', 'st_4', 1321, 12, 206, 72, text='BType :')
        self.add('datawindow', 'dw_saleregister', 0, 96, 3625, 2032, dataobject='d_salesvarep', taborder=50)
