"""V/A Check List — w_vacheck.

Generated from the PowerBuilder window ``w_vacheck.srw`` by
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
    name='w_vacheck',
    title='V/A Check List',
    width=3648,
    height=1840,
    controls=[],
    tables=[],
    source_path='w_vacheck.srw',
    report={'dataobject': 'd_vacheck', 'sql': "SELECT onerec.field AS onerec_field, (select sum(salesd.wastage) from salesd,salesm where salesm.slno = salesd.slno and salesm.tdate >= :rdate1 and salesm.tdate <= :rdate2 and salesm.control <= :rlevel ) as c_salewstg, (select sum(salesd.mcharge) from salesd,salesm where salesm.slno = salesd.slno and salesm.tdate >= :rdate1 and salesm.tdate <= :rdate2 and salesm.control <= :rlevel ) as c_salemc, (select sum(salesrd.wastage) from salesrd,salesrm where salesrm.slno = salesrd.slno and salesrm.tdate >= :rdate1 and salesrm.tdate <= :rdate2 and salesrm.control <= :rlevel ) as c_salerwstg, (select sum(salesrd.mcharge) from salesrd,salesrm where salesrm.slno = salesrd.slno and salesrm.tdate >= :rdate1 and salesrm.tdate <= :rdate2 and salesrm.control <= :rlevel ) as c_salermc, (select sum(smithd.wastage) from smithd,smithm where smithm.slno = smithd.slno and smithm.tdate >= :rdate1 and smithm.tdate <= :rdate2 and smithm.control <= :rlevel ) as c_smithwstg, (select sum(smithd.mcharge) from smithd,smithm where smithm.slno = smithd.slno and smithm.tdate >= :rdate1 and smithm.tdate <= :rdate2 and smithm.control <= :rlevel ) as c_smithmc, (select sum(salesd.mcharge + (salesd.wastage * salesd.rate)) from salesd,salesm where salesm.slno = salesd.slno and salesm.tdate >= :rdate1 and salesm.tdate <= :rdate2 and salesm.control <= :rlevel ) as c_salevaamt, (select sum(salesrd.mcharge + (salesrd.wastage * salesrd.rate)) from salesrd,salesrm where salesrm.slno = salesrd.slno and salesrm.tdate >= :rdate1 and salesrm.tdate <= :rdate2 and salesrm.control <= :rlevel ) as c_salervaamt, (select sum(smithd.mcharge + (smithd.wastage * smithm.rate)) from smithd,smithm,items where smithm.slno = smithd.slno and items.code = smithd.code and items.itype = 'G' and smithm.tdate >= :rdate1 and smithm.tdate <= :rdate2 and smithm.control <= :rlevel ) as c_smithvaamt, (select sum(salesd.stoneprice) from salesd,salesm where salesm.slno = salesd.slno and salesm.tdate >= :rdate1 and salesm.tdate <= :rdate2 and salesm.control <= :rlevel ) as c_salestprice, (select sum(smithd.stoneprice) from smithd,smithm where smithm.slno = smithd.slno and smithm.tdate >= :rdate1 and smithm.tdate <= :rdate2 and smithm.control <= :rlevel ) as c_smithstprice, (select sum(salesrd.stoneprice) from salesrd,salesrm where salesrm.slno = salesrd.slno and salesrm.tdate >= :rdate1 and salesrm.tdate <= :rdate2 and salesrm.control <= :rlevel ) as c_salerstprice, (select sum(salesd.stonewgt) from salesd,salesm where salesm.slno = salesd.slno and salesm.tdate >= :rdate1 and salesm.tdate <= :rdate2 and salesm.control <= :rlevel ) as c_salestwgt, (select sum(salesrd.stonewgt) from salesrd,salesrm where salesrm.slno = salesrd.slno and salesrm.tdate >= :rdate1 and salesrm.tdate <= :rdate2 and salesrm.control <= :rlevel ) as c_salerstwgt, (select sum(salesd.weight) from salesd,salesm where salesm.slno = salesd.slno and salesm.tdate >= :rdate1 and salesm.tdate <= :rdate2 and salesm.control <= :rlevel ) as c_tsalewgt, (select sum(salesm.discount) from salesm where salesm.tdate >= :rdate1 and salesm.tdate <= :rdate2 and salesm.control <= :rlevel ) as c_tsaledisc, (select sum( ( (salesd.mcharge / salesd.weight) / salesd.rate) * 100 ) from salesd,salesm where salesm.slno = salesd.slno and salesm.tdate >= :rdate1 and salesm.tdate <= :rdate2 and salesm.control <= :rlevel and salesd.rate > 0 and salesd.weight > 0 ) as tvaperc FROM onerec", 'computes': [{'name': 'netva', 'expression': 'c_salevaamt -  c_tsaledisc ', 'format': '########0.00', 'label': 'netva', 'band': 'detail'}, {'name': 'compute_4', 'expression': 'if(c_tsalewgt > 0,   netva /  c_tsalewgt , 0)', 'format': '[General]', 'label': 'compute_4', 'band': 'detail'}], 'args': ['rlevel', 'rdate1', 'rdate2'], 'arg_types': {'rlevel': 'number', 'rdate1': 'date', 'rdate2': 'date'}, 'tables': ['onerec'], 'columns': [{'name': 'field', 'label': 'field', 'type': 'char'}, {'name': 'c_salewstg', 'label': 'c_salewstg', 'type': 'decimal'}, {'name': 'c_salemc', 'label': 'c_salemc', 'type': 'decimal'}, {'name': 'c_salerwstg', 'label': 'c_salerwstg', 'type': 'decimal'}, {'name': 'c_salermc', 'label': 'c_salermc', 'type': 'decimal'}, {'name': 'c_smithwstg', 'label': 'c_smithwstg', 'type': 'decimal'}, {'name': 'c_smithmc', 'label': 'c_smithmc', 'type': 'decimal'}, {'name': 'c_salevaamt', 'label': 'c_salevaamt', 'type': 'decimal'}, {'name': 'c_salervaamt', 'label': 'c_salervaamt', 'type': 'decimal'}, {'name': 'c_smithvaamt', 'label': 'c_smithvaamt', 'type': 'decimal'}, {'name': 'c_salestprice', 'label': 'c_salestprice', 'type': 'decimal'}, {'name': 'c_smithstprice', 'label': 'c_smithstprice', 'type': 'decimal'}, {'name': 'c_salerstprice', 'label': 'c_salerstprice', 'type': 'decimal'}, {'name': 'c_salestwgt', 'label': 'c_salestwgt', 'type': 'decimal'}, {'name': 'c_salerstwgt', 'label': 'c_salerstwgt', 'type': 'decimal'}, {'name': 'c_tsalewgt', 'label': 'c_tsalewgt', 'type': 'decimal'}, {'name': 'c_tsaledisc', 'label': 'c_tsaledisc', 'type': 'decimal'}, {'name': 'tvaperc', 'label': 'tvaperc', 'type': 'decimal'}]},
)


class VACheckListForm(GeneratedForm):
    """V/A Check List"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 370, 0, 402, 100, taborder=10)
        self.add('editmask', 'em_date2', 1102, 0, 402, 100, taborder=20)
        self.add('commandbutton', 'cb_show', 1673, 0, 274, 100, text='&Show', taborder=30)
        self.add('commandbutton', 'cb_1', 2112, 0, 247, 100, text='&Print', taborder=60)
        self.add('commandbutton', 'cb_2', 2386, 0, 247, 100, text='E&xit', taborder=50)
        self.add('statictext', 'st_1', 32, 8, 329, 76, text='Date From :')
        self.add('statictext', 'st_2', 878, 20, 256, 76, text='Date To :')
        self.add('datawindow', 'dw_vacheck', 0, 108, 3611, 1576, dataobject='d_vacheck', taborder=40)
