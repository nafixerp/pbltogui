"""Marked List — w_markeditemlist.

Generated from the PowerBuilder window ``w_markeditemlist.srw`` by
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
    name='w_markeditemlist',
    title='Marked List',
    width=3643,
    height=2268,
    controls=[],
    tables=[],
    source_path='w_markeditemlist.srw',
    report={'dataobject': 'd_markeditemrep', 'sql': 'SELECT salesm.billno AS salesm_billno, salesm.tdate AS salesm_tdate, salesm.billamt AS salesm_billamt, salesm.eamt AS salesm_eamt, salesm.sretamt AS salesm_sretamt, salesm.staxamt AS salesm_staxamt, salesm.discount AS salesm_discount, salesm.ramt AS salesm_ramt, salesm.ramtafter AS salesm_ramtafter, salesm.slno AS salesm_slno, salesd.slno AS salesd_slno, items.name AS items_name, salesd.qty AS salesd_qty, salesd.weight AS salesd_weight, items.itype AS items_itype, salesd.jcode AS salesd_jcode, items.ornament AS items_ornament, salesd.amount AS salesd_amount, salesm.smcode AS salesm_smcode, salesd.name AS salesd_name, items.code AS items_code, salesd.rmno AS salesd_rmno, salesd.mark AS salesd_mark, salesd.stonewgt AS salesd_stonewgt, (select barcode.smithmcrate from barcode where barcode.bcode = salesd.bcode) as smithmc FROM salesd, salesm, items WHERE salesd.slno = salesm.slno AND salesd.code = items.code AND salesm.tdate between :rdate1 and :rdate2 AND salesm.control <= :rlevel ORDER BY salesm.tdate ASC, salesm.slno ASC', 'args': ['rdate1', 'rdate2', 'rlevel'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date', 'rlevel': 'number'}, 'tables': ['salesd', 'salesm', 'items'], 'columns': [{'name': 'salesm_billno', 'label': 'salesm_billno', 'type': 'char'}, {'name': 'salesm_tdate', 'label': 'salesm_tdate', 'type': 'date'}, {'name': 'salesm_billamt', 'label': 'salesm_billamt', 'type': 'decimal'}, {'name': 'salesm_eamt', 'label': 'salesm_eamt', 'type': 'decimal'}, {'name': 'salesm_sretamt', 'label': 'salesm_sretamt', 'type': 'decimal'}, {'name': 'salesm_staxamt', 'label': 'salesm_staxamt', 'type': 'decimal'}, {'name': 'salesm_discount', 'label': 'salesm_discount', 'type': 'decimal'}, {'name': 'salesm_ramt', 'label': 'salesm_ramt', 'type': 'decimal'}, {'name': 'salesm_ramtafter', 'label': 'salesm_ramtafter', 'type': 'decimal'}, {'name': 'salesm_slno', 'label': 'salesm_slno', 'type': 'decimal'}, {'name': 'salesd_slno', 'label': 'salesd_slno', 'type': 'decimal'}, {'name': 'items_name', 'label': 'items_name', 'type': 'char'}, {'name': 'salesd_qty', 'label': 'salesd_qty', 'type': 'long'}, {'name': 'salesd_weight', 'label': 'salesd_weight', 'type': 'decimal'}, {'name': 'items_itype', 'label': 'items_itype', 'type': 'char'}, {'name': 'salesd_jcode', 'label': 'salesd_jcode', 'type': 'char'}, {'name': 'items_ornament', 'label': 'items_ornament', 'type': 'char'}, {'name': 'salesd_amount', 'label': 'salesd_amount', 'type': 'decimal'}, {'name': 'salesm_smcode', 'label': 'salesm_smcode', 'type': 'char'}, {'name': 'salesd_name', 'label': 'salesd_name', 'type': 'char'}, {'name': 'items_code', 'label': 'items_code', 'type': 'char'}, {'name': 'salesd_rmno', 'label': 'salesd_rmno', 'type': 'char'}, {'name': 'salesd_mark', 'label': 'salesd_mark', 'type': 'char'}, {'name': 'salesd_stonewgt', 'label': 'salesd_stonewgt', 'type': 'decimal'}, {'name': 'smithmc', 'label': 'smithmc', 'type': 'decimal'}]},
    opens=['w_itemhelp'],
)


class MarkedListForm(GeneratedForm):
    """Marked List"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 393, 0, 384, 92, taborder=10)
        self.add('editmask', 'em_date2', 1463, 0, 384, 92, taborder=20)
        self.add('commandbutton', 'cb_show', 1888, 0, 274, 96, text='&Show', taborder=30)
        self.add('commandbutton', 'cb_sort', 2450, 0, 247, 92, text='So&rt', taborder=80)
        self.add('commandbutton', 'cb_print', 2725, 0, 233, 92, text='&Print', taborder=90)
        self.add('commandbutton', 'cb_1', 2962, 0, 261, 92, text='Save &As', taborder=110)
        self.add('commandbutton', 'cb_exit', 3227, 0, 233, 92, text='E&xit', taborder=120)
        self.add('statictext', 'st_11', 1152, 12, 302, 72, text='Date To :')
        self.add('statictext', 'st_10', 18, 20, 361, 64, text='Date From :')
        self.add('dropdownlistbox', 'ddlb_type', 1463, 100, 608, 532, text='All', items=['All', 'Ornaments Only', 'Not Ornaments', 'Gold', 'Silver', 'Others'], taborder=50)
        self.add('datawindow', 'dw_smcode', 393, 104, 672, 88, dataobject='d_smancode', taborder=40)
        self.add('statictext', 'st_1', 169, 112, 210, 76, text='SMan :')
        self.add('statictext', 'st_2', 1207, 112, 247, 76, text='Type :')
        self.add('checkbox', 'cbx_speed', 3278, 112, 297, 76, text='Speed')
        self.add('checkbox', 'cbx_itemwise', 2441, 124, 384, 76, text='&Itemwise')
        self.add('dropdownlistbox', 'ddlb_mark', 1463, 200, 603, 316, text='All', items=['All', 'Marked Items Only', 'Not Marked Items'], taborder=70)
        self.add('commandbutton', 'cb_4', 809, 204, 187, 96, text='&Help')
        self.add('singlelineedit', 'sle_itemcode', 393, 208, 393, 92, limit=10, taborder=60)
        self.add('statictext', 'st_3', 14, 212, 366, 72, text='Item Code :')
        self.add('checkbox', 'cbx_rmnowise', 2441, 212, 626, 76, text='&Remake No. wise')
        self.add('statictext', 'st_4', 1189, 220, 265, 76, text='Marked :')
        self.add('datawindow', 'dw_saleregister', 0, 304, 3593, 1848, dataobject='d_markeditemrep', taborder=100)
