"""Sales Book — w_taxreport.

Generated from the PowerBuilder window ``w_taxreport.srw`` by
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
    name='w_taxreport',
    title='Sales Book',
    width=4050,
    height=2256,
    controls=[],
    tables=['smithm', 'smithd', 'salesm', 'salesrm', 'purchasem', 'purchaserm', 'jewellery'],
    source_path='w_taxreport.srw',
    grid={'control': 'dw_1', 'dataobject': 'd_taxrep_sales', 'table': 'salesm', 'keys': ['slno'], 'computes': [{'name': 'compute_1', 'expression': 'sum(grosswgt for all)', 'format': '#########0.000', 'label': 'compute_1', 'band': 'summary'}, {'name': 'compute_22', 'expression': 'sum(stonewgt for all)', 'format': '#####0.000', 'label': 'compute_22', 'band': 'summary'}, {'name': 'compute_2', 'expression': 'sum(totwgt for all)', 'format': '#########0.000', 'label': 'compute_2', 'band': 'summary'}, {'name': 'compute_24', 'expression': 'sum(stoneprice for all)', 'format': '######0.00', 'label': 'compute_24', 'band': 'summary'}, {'name': 'compute_3', 'expression': 'sum(va for all)', 'format': '#########0.00', 'label': 'compute_3', 'band': 'summary'}, {'name': 'compute_4', 'expression': 'sum(billamt for all)', 'format': '#########0.00', 'label': 'compute_4', 'band': 'summary'}, {'name': 'compute_5', 'expression': 'sum(sgst for all)', 'format': '#########0.00', 'label': 'compute_5', 'band': 'summary'}, {'name': 'compute_6', 'expression': 'sum(cgst for all)', 'format': '#########0.00', 'label': 'compute_6', 'band': 'summary'}, {'name': 'compute_7', 'expression': 'sum(igst for all)', 'format': '#########0.00', 'label': 'compute_7', 'band': 'summary'}, {'name': 'compute_8', 'expression': 'sum(staxamt for all)', 'format': '#########0.00', 'label': 'compute_8', 'band': 'summary'}, {'name': 'compute_9', 'expression': 'sum(discount for all)', 'format': '#########0.00', 'label': 'compute_9', 'band': 'summary'}, {'name': 'compute_10', 'expression': 'sum(totamt for all)', 'format': '#########0.00', 'label': 'compute_10', 'band': 'summary'}], 'columns': [{'name': 'billno', 'label': 'Bill No', 'type': 'char'}, {'name': 'tdate', 'label': 'Date', 'type': 'date'}, {'name': 'custname', 'label': 'Customer', 'type': 'char'}, {'name': 'addr', 'label': 'Address', 'type': 'char'}, {'name': 'pan', 'label': 'PAN/Adhar', 'type': 'char'}, {'name': 'statecode', 'label': 'StateCode', 'type': 'char'}, {'name': 'maxrate', 'label': 'Rate', 'type': 'decimal'}, {'name': 'hsncode', 'label': 'HSN Code', 'type': 'char'}, {'name': 'grosswgt', 'label': 'Gross Wgt', 'type': 'decimal'}, {'name': 'stonewgt', 'label': 'Stone Wgt', 'type': 'decimal'}, {'name': 'totwgt', 'label': 'Net Wgt', 'type': 'decimal'}, {'name': 'va', 'label': 'VA', 'type': 'decimal'}, {'name': 'stoneprice', 'label': 'Stone Amt', 'type': 'decimal'}, {'name': 'billamt', 'label': 'Amount', 'type': 'decimal'}, {'name': 'sgst', 'label': 'SGST', 'type': 'decimal'}, {'name': 'cgst', 'label': 'CGST', 'type': 'decimal'}, {'name': 'igst', 'label': 'IGST', 'type': 'decimal'}, {'name': 'staxamt', 'label': 'GST Amt', 'type': 'decimal'}, {'name': 'discount', 'label': 'Discount', 'type': 'decimal'}, {'name': 'totamt', 'label': 'Total Amt', 'type': 'decimal'}, {'name': 'billtype', 'label': 'billtype', 'type': 'char'}, {'name': 'sel', 'label': 'Sel', 'type': 'long'}, {'name': 'slno', 'label': 'slno', 'type': 'decimal'}, {'name': 'ctin', 'label': 'GSTIN', 'type': 'char'}, {'name': 'itemname', 'label': 'Item Name', 'type': 'char'}]},
    report={'dataobject': 'd_taxrep_sales', 'sql': 'SELECT "salesm"."billno",   \r\n         "salesm"."tdate",   \r\n         "salesm"."custname",   \r\n         "salesm"."addr",   \r\n         "salesm"."pan",   \r\n         "salesm"."statecode",   \r\n         (select max(salesd.rate) from salesd where salesd.slno = salesm.slno) as maxrate,   \r\n         (select max(items.vatcode) from items,salesd where items.code = salesd.code and salesd.slno = salesm.slno) as hsncode,   \r\n         (select sum(salesd.weight) from salesd where salesd.slno = salesm.slno) as grosswgt,   \r\n\t\t(select sum(salesd.stonewgt) from salesd where salesd.slno = salesm.slno) as stonewgt,   \r\n         (select sum(salesd.weight - salesd.stonewgt ) from salesd where salesd.slno = salesm.slno) as totwgt,   \r\n         (select sum(salesd.mcharge) from salesd where salesd.slno = salesm.slno) as va,   \r\n\t\t(select sum(salesd.stoneprice) from salesd where salesd.slno = salesm.slno) as stoneprice,   \r\n         "salesm"."billamt",   \r\n         "salesm"."sgst",   \r\n         "salesm"."cgst",   \r\n         "salesm"."igst",   \r\n         "salesm"."staxamt",   \r\n         "salesm"."discount",   \r\n         ( netamt ) as totamt,   \r\n         "salesm"."billtype",   \r\n         (0) as sel,   \r\n         "salesm"."slno",   \r\n\t\t(select clients.tin from clients where clients.code = salesm.custcode) as ctin,\r\n         (select max(items.name) from items,salesd where items.code = salesd.code and salesd.slno = salesm.slno) as itemname  \r\n    FROM "salesm"  \r\n   WHERE ( "salesm"."tdate" >= :rdate1 ) AND  \r\n         ( "salesm"."tdate" <= :rdate2 ) AND  \r\n         ( "salesm"."control" <= :rlevel )   \r\nORDER BY "salesm"."tdate" ASC,   \r\n         "salesm"."billno" ASC', 'computes': [{'name': 'compute_1', 'expression': 'sum(grosswgt for all)', 'format': '#########0.000', 'label': 'compute_1', 'band': 'summary'}, {'name': 'compute_22', 'expression': 'sum(stonewgt for all)', 'format': '#####0.000', 'label': 'compute_22', 'band': 'summary'}, {'name': 'compute_2', 'expression': 'sum(totwgt for all)', 'format': '#########0.000', 'label': 'compute_2', 'band': 'summary'}, {'name': 'compute_24', 'expression': 'sum(stoneprice for all)', 'format': '######0.00', 'label': 'compute_24', 'band': 'summary'}, {'name': 'compute_3', 'expression': 'sum(va for all)', 'format': '#########0.00', 'label': 'compute_3', 'band': 'summary'}, {'name': 'compute_4', 'expression': 'sum(billamt for all)', 'format': '#########0.00', 'label': 'compute_4', 'band': 'summary'}, {'name': 'compute_5', 'expression': 'sum(sgst for all)', 'format': '#########0.00', 'label': 'compute_5', 'band': 'summary'}, {'name': 'compute_6', 'expression': 'sum(cgst for all)', 'format': '#########0.00', 'label': 'compute_6', 'band': 'summary'}, {'name': 'compute_7', 'expression': 'sum(igst for all)', 'format': '#########0.00', 'label': 'compute_7', 'band': 'summary'}, {'name': 'compute_8', 'expression': 'sum(staxamt for all)', 'format': '#########0.00', 'label': 'compute_8', 'band': 'summary'}, {'name': 'compute_9', 'expression': 'sum(discount for all)', 'format': '#########0.00', 'label': 'compute_9', 'band': 'summary'}, {'name': 'compute_10', 'expression': 'sum(totamt for all)', 'format': '#########0.00', 'label': 'compute_10', 'band': 'summary'}], 'args': ['rdate1', 'rdate2', 'rlevel'], 'arg_types': {}, 'tables': ['salesm'], 'columns': [{'name': 'billno', 'label': 'Bill No', 'type': 'char'}, {'name': 'tdate', 'label': 'Date', 'type': 'date'}, {'name': 'custname', 'label': 'Customer', 'type': 'char'}, {'name': 'addr', 'label': 'Address', 'type': 'char'}, {'name': 'pan', 'label': 'PAN/Adhar', 'type': 'char'}, {'name': 'statecode', 'label': 'StateCode', 'type': 'char'}, {'name': 'maxrate', 'label': 'Rate', 'type': 'decimal'}, {'name': 'hsncode', 'label': 'HSN Code', 'type': 'char'}, {'name': 'grosswgt', 'label': 'Gross Wgt', 'type': 'decimal'}, {'name': 'stonewgt', 'label': 'Stone Wgt', 'type': 'decimal'}, {'name': 'totwgt', 'label': 'Net Wgt', 'type': 'decimal'}, {'name': 'va', 'label': 'VA', 'type': 'decimal'}, {'name': 'stoneprice', 'label': 'Stone Amt', 'type': 'decimal'}, {'name': 'billamt', 'label': 'Amount', 'type': 'decimal'}, {'name': 'sgst', 'label': 'SGST', 'type': 'decimal'}, {'name': 'cgst', 'label': 'CGST', 'type': 'decimal'}, {'name': 'igst', 'label': 'IGST', 'type': 'decimal'}, {'name': 'staxamt', 'label': 'GST Amt', 'type': 'decimal'}, {'name': 'discount', 'label': 'Discount', 'type': 'decimal'}, {'name': 'totamt', 'label': 'Total Amt', 'type': 'decimal'}, {'name': 'billtype', 'label': 'billtype', 'type': 'char'}, {'name': 'sel', 'label': 'Sel', 'type': 'long'}, {'name': 'slno', 'label': 'slno', 'type': 'decimal'}, {'name': 'ctin', 'label': 'GSTIN', 'type': 'char'}, {'name': 'itemname', 'label': 'Item Name', 'type': 'char'}]},
)


class SalesBookForm(GeneratedForm):
    """Sales Book"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 233, 0, 425, 92, taborder=10)
        self.add('editmask', 'em_date2', 827, 0, 425, 92, taborder=20)
        self.add('datawindow', 'dw_billtype', 1682, 0, 425, 88, dataobject='d_billtypecode', taborder=120)
        self.add('commandbutton', 'cb_show', 2702, 0, 293, 96, text='&Show', taborder=40)
        self.add('commandbutton', 'cb_sort', 3008, 0, 247, 92, text='So&rt', taborder=50)
        self.add('commandbutton', 'cb_1', 3264, 0, 270, 92, text='Save &As', taborder=130)
        self.add('commandbutton', 'cb_print', 3538, 0, 233, 92, text='&Print', taborder=80)
        self.add('commandbutton', 'cb_exit', 3776, 0, 233, 92, text='E&xit', taborder=90)
        self.add('statictext', 'st_11', 667, 4, 151, 72, text='To :')
        self.add('statictext', 'st_10', 0, 8, 219, 64, text='From :')
        self.add('statictext', 'st_1', 1362, 16, 306, 64, text='Bill Type :')
        self.add('dropdownlistbox', 'ddlb_gstin', 233, 96, 425, 528, text='All', items=['With GSTIN', 'Without GSTIN', 'All'], taborder=30)
        self.add('dropdownlistbox', 'ddlb_type', 827, 96, 425, 528, text='Billwise', items=['Billwise', 'Billwise Short', 'Daywise'], taborder=140)
        self.add('singlelineedit', 'sle_billno1', 1682, 96, 302, 92, taborder=100)
        self.add('singlelineedit', 'sle_billno2', 1998, 96, 302, 92, taborder=110)
        self.add('commandbutton', 'cb_efile', 3269, 96, 270, 92, text='E-File', taborder=70)
        self.add('dropdownlistbox', 'ddlb_givrec', 2706, 100, 425, 400, text='Issued', items=['Issued', 'Received'])
        self.add('checkbox', 'cbx_speed', 3552, 100, 393, 76, text='Speed Print')
        self.add('statictext', 'st_billnos', 1390, 104, 279, 64, text='Bill Nos :')
        self.add('datawindow', 'dw_1', 0, 188, 4014, 1964, dataobject='d_taxrep_sales', taborder=60)
