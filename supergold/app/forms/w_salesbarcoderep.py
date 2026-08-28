"""Barcode Register — w_salesbarcoderep.

Generated from the PowerBuilder window ``w_salesbarcoderep.srw`` by
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
    name='w_salesbarcoderep',
    title='Barcode Register',
    width=3680,
    height=2256,
    controls=[],
    tables=[],
    source_path='w_salesbarcoderep.srw',
    report={'dataobject': 'd_salesbarcoderep', 'sql': 'SELECT salesm.slno AS salesm_slno, salesm.tdate AS salesm_tdate, salesm.billno AS salesm_billno, salesm.custname AS salesm_custname, salesm.billamt AS salesm_billamt, salesm.status AS salesm_status, salesm.discount AS salesm_discount, salesm.ramt AS salesm_ramt, salesm.eamt AS salesm_eamt, salesm.staxamt AS salesm_staxamt, salesm.duedate AS salesm_duedate, salesm.sretamt AS salesm_sretamt, salesm.ramtafter AS salesm_ramtafter, salesm.round AS salesm_round, salesd.code AS salesd_code, salesd.qty AS salesd_qty, salesd.weight AS salesd_weight, salesd.dmdwgt AS salesd_dmdwgt, salesd.dmdunit AS salesd_dmdunit, salesd.dmdamt AS salesd_dmdamt, salesd.bcode AS salesd_bcode, salesd.amount AS salesd_amount, salesd.stonewgt AS salesd_stonewgt, salesd.stoneprice AS salesd_stoneprice, salesd.mcharge AS salesd_mcharge, salesd.wastage AS salesd_wastage, items.name AS items_name FROM salesm, salesd, items WHERE salesm.slno = salesd.slno AND salesd.code = items.code AND salesm.control <= :rlevel ORDER BY salesm.tdate ASC, salesm.slno ASC', 'args': ['rdate1', 'rdate2', 'rlevel'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date', 'rlevel': 'number'}, 'tables': ['salesm', 'salesd', 'items'], 'columns': [{'name': 'salesm_slno', 'label': 'salesm_slno', 'type': 'decimal'}, {'name': 'salesm_tdate', 'label': 'salesm_tdate', 'type': 'date'}, {'name': 'salesm_billno', 'label': 'salesm_billno', 'type': 'char'}, {'name': 'salesm_custname', 'label': 'salesm_custname', 'type': 'char'}, {'name': 'salesm_billamt', 'label': 'salesm_billamt', 'type': 'decimal'}, {'name': 'salesm_status', 'label': 'salesm_status', 'type': 'long'}, {'name': 'salesm_discount', 'label': 'salesm_discount', 'type': 'decimal'}, {'name': 'salesm_ramt', 'label': 'salesm_ramt', 'type': 'decimal'}, {'name': 'salesm_eamt', 'label': 'salesm_eamt', 'type': 'decimal'}, {'name': 'salesm_staxamt', 'label': 'salesm_staxamt', 'type': 'decimal'}, {'name': 'salesm_duedate', 'label': 'salesm_duedate', 'type': 'date'}, {'name': 'salesm_sretamt', 'label': 'salesm_sretamt', 'type': 'decimal'}, {'name': 'salesm_ramtafter', 'label': 'salesm_ramtafter', 'type': 'decimal'}, {'name': 'round', 'label': 'round', 'type': 'decimal'}, {'name': 'salesd_code', 'label': 'salesd_code', 'type': 'char'}, {'name': 'salesd_qty', 'label': 'salesd_qty', 'type': 'long'}, {'name': 'salesd_weight', 'label': 'salesd_weight', 'type': 'decimal'}, {'name': 'salesd_dmdwgt', 'label': 'salesd_dmdwgt', 'type': 'decimal'}, {'name': 'salesd_dmdunit', 'label': 'salesd_dmdunit', 'type': 'char'}, {'name': 'salesd_dmdamt', 'label': 'salesd_dmdamt', 'type': 'decimal'}, {'name': 'salesd_bcode', 'label': 'salesd_bcode', 'type': 'decimal'}, {'name': 'salesd_amount', 'label': 'salesd_amount', 'type': 'decimal'}, {'name': 'salesd_stonewgt', 'label': 'salesd_stonewgt', 'type': 'decimal'}, {'name': 'salesd_stoneprice', 'label': 'salesd_stoneprice', 'type': 'decimal'}, {'name': 'salesd_mcharge', 'label': 'salesd_mcharge', 'type': 'decimal'}, {'name': 'salesd_wastage', 'label': 'salesd_wastage', 'type': 'decimal'}, {'name': 'items_name', 'label': 'items_name', 'type': 'char'}]},
)


class BarcodeRegisterForm(GeneratedForm):
    """Barcode Register"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 370, 0, 425, 92, taborder=10)
        self.add('editmask', 'em_date2', 1179, 0, 425, 92, taborder=20)
        self.add('commandbutton', 'cb_show', 1691, 0, 293, 96, text='&Show', taborder=30)
        self.add('commandbutton', 'cb_sort', 2469, 0, 247, 92, text='So&rt', taborder=31)
        self.add('commandbutton', 'cb_1', 2747, 0, 270, 92, text='Save &As', taborder=70)
        self.add('commandbutton', 'cb_print', 3022, 0, 233, 92, text='&Print', taborder=50)
        self.add('commandbutton', 'cb_exit', 3259, 0, 233, 92, text='E&xit', taborder=60)
        self.add('statictext', 'st_11', 869, 12, 302, 72, text='Date To :')
        self.add('statictext', 'st_10', 0, 20, 361, 64, text='Date From :')
        self.add('datawindow', 'dw_saleregister', 0, 96, 3625, 2032, dataobject='d_salesbarcoderep', taborder=40)
