"""All Trans Report — w_trans_rearrange_report.

Generated from the PowerBuilder window ``w_trans_rearrange_report.srw`` by
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
    name='w_trans_rearrange_report',
    title='All Trans Report',
    width=3685,
    height=2368,
    controls=[],
    tables=['salesm', 'salesrm', 'items', 'purchasem', 'itemsstk', 'daybook', 'salesd', 'salesrd', 'purchased', 'barcode', 'purchaserm', 'purchaserd', 'orderm', 'orderd', 'smithm', 'smithd', 'refinerym', 'refineryd', 'itemadj', 'counter', 'generals', 'generali', 'daybookpart'],
    source_path='w_trans_rearrange_report.srw',
    grid={'control': 'dw_saleregister', 'dataobject': 'd_transrep_sales', 'table': 'salesm', 'keys': ['slno'], 'columns': [{'name': 'tdate', 'label': 'salesm_tdate', 'type': 'date'}, {'name': 'billno', 'label': 'salesm_billno', 'type': 'char'}, {'name': 'custname', 'label': 'salesm_custname', 'type': 'char'}, {'name': 'billamt', 'label': 'salesm_billamt', 'type': 'decimal'}, {'name': 'status', 'label': 'salesm_status', 'type': 'long'}, {'name': 'discount', 'label': 'salesm_discount', 'type': 'decimal'}, {'name': 'ramt', 'label': 'salesm_ramt', 'type': 'decimal'}, {'name': 'eamt', 'label': 'salesm_eamt', 'type': 'decimal'}, {'name': 'staxamt', 'label': 'salesm_staxamt', 'type': 'decimal'}, {'name': 'astamt', 'label': 'astamt', 'type': 'decimal'}, {'name': 'duedate', 'label': 'salesm_duedate', 'type': 'date'}, {'name': 'sretamt', 'label': 'salesm_sretamt', 'type': 'decimal'}, {'name': 'ramtafter', 'label': 'salesm_ramtafter', 'type': 'decimal'}, {'name': 'round', 'label': 'round', 'type': 'decimal'}, {'name': 'control', 'label': 'control', 'type': 'long'}, {'name': 'slno', 'label': 'slno', 'type': 'decimal'}, {'name': 'billtype', 'label': 'billtype', 'type': 'char'}, {'name': 'totwgt', 'label': 'totwgt', 'type': 'decimal'}, {'name': 'grosswgt', 'label': 'grosswgt', 'type': 'decimal'}, {'name': 'va', 'label': 'va', 'type': 'decimal'}, {'name': 'maxrate', 'label': 'maxrate', 'type': 'decimal'}, {'name': 'caddr', 'label': 'caddr', 'type': 'char'}, {'name': 'cplace', 'label': 'cplace', 'type': 'char'}, {'name': 'tdate', 'label': 'tdate', 'type': 'date'}, {'name': 'sel', 'label': 'sel', 'type': 'long'}]},
    report={'dataobject': 'd_transrep_sales', 'sql': 'SELECT "salesm"."tdate",   \r\n\t\t\t"salesm"."billno",   \r\n\t\t\t"salesm"."custname",   \r\n\t\t\t"salesm"."billamt",   \r\n\t\t\t"salesm"."status",   \r\n\t\t\t"salesm"."discount",   \r\n\t\t\t"salesm"."ramt",   \r\n\t\t\t"salesm"."eamt",   \r\n\t\t\t"salesm"."staxamt",   \r\n\t\t\t"salesm"."astamt",   \r\n\t\t\t"salesm"."duedate",   \r\n\t\t\t"salesm"."sretamt",   \r\n\t\t\t"salesm"."ramtafter",   \r\n\t\t\t"salesm"."round",   \r\n\t\t\t"salesm"."control",   \r\n\t\t\t"salesm"."slno" ,\r\n\t\t\t"salesm"."billtype" ,\r\n\t\t(select sum(salesd.weight - salesd.stonewgt) from salesd where salesd.slno = salesm.slno) as totwgt,    \r\n\t\t(select sum(salesd.weight) from salesd where salesd.slno = salesm.slno) as grosswgt,    \r\n\t\t(select sum(salesd.mcharge) from salesd where salesd.slno = salesm.slno) as va,    \r\n\t\t(select max(salesd.rate) from salesd where salesd.slno = salesm.slno) as maxrate,\r\n\t\t(select clients.addr1 from clients where clients.code = salesm.custcode) as caddr,    \r\n\t\t(select clients.city from clients where clients.code = salesm.custcode) as cplace,    \r\n\t\t(salesm.tdate) as tdate,\r\n\t\t\t0 as sel\r\n\t FROM "salesm"  \r\n\tWHERE ( salesm.tdate between :rdate1 and :rdate2 ) AND  \r\n\t\t\t( salesm.control <= :rlevel ) AND  \r\n\t\t\t( "salesm"."opbill" <> 1 )   \r\nORDER BY "salesm"."tdate" ASC,   \r\n\t\t\t"salesm"."billno" ASC', 'args': ['rdate1', 'rdate2', 'rlevel'], 'arg_types': {}, 'tables': ['salesm'], 'columns': [{'name': 'salesm_tdate', 'label': 'salesm_tdate', 'type': 'date'}, {'name': 'salesm_billno', 'label': 'salesm_billno', 'type': 'char'}, {'name': 'salesm_custname', 'label': 'salesm_custname', 'type': 'char'}, {'name': 'salesm_billamt', 'label': 'salesm_billamt', 'type': 'decimal'}, {'name': 'salesm_status', 'label': 'salesm_status', 'type': 'long'}, {'name': 'salesm_discount', 'label': 'salesm_discount', 'type': 'decimal'}, {'name': 'salesm_ramt', 'label': 'salesm_ramt', 'type': 'decimal'}, {'name': 'salesm_eamt', 'label': 'salesm_eamt', 'type': 'decimal'}, {'name': 'salesm_staxamt', 'label': 'salesm_staxamt', 'type': 'decimal'}, {'name': 'astamt', 'label': 'astamt', 'type': 'decimal'}, {'name': 'salesm_duedate', 'label': 'salesm_duedate', 'type': 'date'}, {'name': 'salesm_sretamt', 'label': 'salesm_sretamt', 'type': 'decimal'}, {'name': 'salesm_ramtafter', 'label': 'salesm_ramtafter', 'type': 'decimal'}, {'name': 'round', 'label': 'round', 'type': 'decimal'}, {'name': 'control', 'label': 'control', 'type': 'long'}, {'name': 'slno', 'label': 'slno', 'type': 'decimal'}, {'name': 'billtype', 'label': 'billtype', 'type': 'char'}, {'name': 'totwgt', 'label': 'totwgt', 'type': 'decimal'}, {'name': 'grosswgt', 'label': 'grosswgt', 'type': 'decimal'}, {'name': 'va', 'label': 'va', 'type': 'decimal'}, {'name': 'maxrate', 'label': 'maxrate', 'type': 'decimal'}, {'name': 'caddr', 'label': 'caddr', 'type': 'char'}, {'name': 'cplace', 'label': 'cplace', 'type': 'char'}, {'name': 'tdate', 'label': 'tdate', 'type': 'date'}, {'name': 'sel', 'label': 'sel', 'type': 'long'}]},
)


class AllTransReportForm(GeneratedForm):
    """All Trans Report"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 206, 0, 425, 92, taborder=10)
        self.add('editmask', 'em_date2', 869, 0, 425, 92, taborder=20)
        self.add('commandbutton', 'cb_show', 1623, 0, 293, 92, text='&Show', taborder=30)
        self.add('commandbutton', 'cb_selall', 2217, 0, 293, 96, text='Select All')
        self.add('commandbutton', 'cb_sort', 2505, 0, 293, 92, text='So&rt', taborder=40)
        self.add('commandbutton', 'cb_1', 2793, 0, 293, 92, text='Save &As', taborder=120)
        self.add('commandbutton', 'cb_print', 3081, 0, 293, 92, text='&Print', taborder=100)
        self.add('commandbutton', 'cb_exit', 3369, 0, 293, 92, text='E&xit', taborder=110)
        self.add('statictext', 'st_10', 5, 12, 192, 64, text='From :')
        self.add('statictext', 'st_11', 722, 12, 142, 72, text='To :')
        self.add('editmask', 'em_avgwgt', 1623, 92, 293, 92, text='none', taborder=111)
        self.add('commandbutton', 'cb_process', 1920, 92, 238, 96, text='Process', taborder=40)
        self.add('commandbutton', 'cb_tobill', 2217, 92, 293, 96, text='To Bill')
        self.add('commandbutton', 'cb_toest', 2505, 92, 293, 96, text='To Est')
        self.add('commandbutton', 'cb_delete', 2793, 92, 293, 96, text='Delete', taborder=70)
        self.add('commandbutton', 'cb_rearrange', 3081, 92, 293, 96, text='Rearrange', taborder=80)
        self.add('commandbutton', 'cb_reprint', 3369, 92, 293, 96, text='Reprint', taborder=81)
        self.add('datawindow', 'dw_billtype', 206, 96, 425, 88, dataobject='d_billtypecode', taborder=91)
        self.add('dropdownlistbox', 'ddlb_rtype', 869, 96, 425, 1364, text='Sales', items=['Sales', 'SReturn', 'Purchase', 'PReturn', 'Order', 'Smith', 'Jewellery', 'Item Adjustment', 'Receipt', 'Payment', 'Journal'], taborder=101)
        self.add('statictext', 'st_1', 645, 100, 219, 72, text='RType :')
        self.add('statictext', 'st_avgwgt', 1344, 104, 270, 64, text='AVG Wgt :')
        self.add('statictext', 'st_4', 5, 108, 192, 72, text='BType :')
        self.add('datawindow', 'dw_saleregister', 0, 188, 3657, 2076, dataobject='d_transrep_sales', taborder=90)
