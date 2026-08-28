"""Itemwise Profit — w_itemwiseprofit.

Generated from the PowerBuilder window ``w_itemwiseprofit.srw`` by
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
    name='w_itemwiseprofit',
    title='Itemwise Profit',
    width=3589,
    height=2256,
    controls=[],
    tables=[],
    source_path='w_itemwiseprofit.srw',
    grid={'control': 'dw_1', 'dataobject': 'd_itemwiseprofit', 'table': 'items', 'keys': ['code'], 'columns': [{'name': 'code', 'label': 'Code', 'type': 'char'}, {'name': 'name', 'label': 'Name', 'type': 'char'}, {'name': 'saleamt', 'label': 'Sales Amt', 'type': 'decimal'}, {'name': 'stkinnos', 'label': 'stkinnos', 'type': 'char'}, {'name': 'qtycostamt', 'label': 'qtycostamt', 'type': 'decimal'}, {'name': 'wgtcostamt', 'label': 'wgtcostamt', 'type': 'decimal'}, {'name': 'tqty', 'label': 'tqty', 'type': 'long'}, {'name': 'twgt', 'label': 'twgt', 'type': 'decimal'}]},
    report={'dataobject': 'd_itemwiseprofit', 'sql': 'SELECT items.code AS items_code, items.name AS items_name, items.stkinnos AS items_stkinnos, (select sum(salesd.amount) from salesd,salesm where salesd.slno = salesm.slno and salesd.code = items.code and salesm.tdate >= :rdate1 and salesm.tdate <= :rdate2 and salesm.control <= :rlevel) as saleamt, (select sum(salesd.cost * salesd.qty) from salesd,salesm where salesd.slno = salesm.slno and salesd.code = items.code and salesm.tdate >= :rdate1 and salesm.tdate <= :rdate2 and salesm.control <= :rlevel) as qtycostamt, (select sum(salesd.cost * salesd.weight) from salesd,salesm where salesd.slno = salesm.slno and salesd.code = items.code and salesm.tdate >= :rdate1 and salesm.tdate <= :rdate2 and salesm.control <= :rlevel) as wgtcostamt, (select sum(salesd.qty) from salesd,salesm where salesd.slno = salesm.slno and salesd.code = items.code and salesm.tdate >= :rdate1 and salesm.tdate <= :rdate2 and salesm.control <= :rlevel) as tqty, (select sum(salesd.weight) from salesd,salesm where salesd.slno = salesm.slno and salesd.code = items.code and salesm.tdate >= :rdate1 and salesm.tdate <= :rdate2 and salesm.control <= :rlevel) as twgt FROM items WHERE saleamt > 0 ORDER BY items.name ASC', 'args': ['rdate1', 'rdate2', 'rlevel'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date', 'rlevel': 'number'}, 'tables': ['items'], 'columns': [{'name': 'code', 'label': 'Code', 'type': 'char'}, {'name': 'name', 'label': 'Name', 'type': 'char'}, {'name': 'saleamt', 'label': 'Sales Amt', 'type': 'decimal'}, {'name': 'stkinnos', 'label': 'stkinnos', 'type': 'char'}, {'name': 'qtycostamt', 'label': 'qtycostamt', 'type': 'decimal'}, {'name': 'wgtcostamt', 'label': 'wgtcostamt', 'type': 'decimal'}, {'name': 'tqty', 'label': 'tqty', 'type': 'long'}, {'name': 'twgt', 'label': 'twgt', 'type': 'decimal'}]},
)


class ItemwiseProfitForm(GeneratedForm):
    """Itemwise Profit"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 215, 0, 375, 92, taborder=10)
        self.add('editmask', 'em_date2', 818, 0, 379, 92, taborder=20)
        self.add('singlelineedit', 'sle_itemcode', 1632, 0, 375, 92, limit=10, taborder=30)
        self.add('commandbutton', 'cb_show', 2455, 0, 288, 96, text='&Show', taborder=40)
        self.add('commandbutton', 'cb_saveas', 2784, 0, 274, 96, text='Save &As', taborder=70)
        self.add('commandbutton', 'cb_print', 3067, 0, 247, 96, text='&Print', taborder=80)
        self.add('commandbutton', 'cb_exit', 3323, 0, 247, 96, text='E&xit', taborder=60)
        self.add('commandbutton', 'cb_help', 2016, 4, 160, 88, text='&Help')
        self.add('statictext', 'st_1', 0, 8, 206, 76, text='From :')
        self.add('statictext', 'st_2', 686, 8, 119, 76, text='To :')
        self.add('statictext', 'st_3', 1275, 8, 347, 72, text='Item Code :')
        self.add('datawindow', 'dw_1', 5, 104, 3561, 2056, dataobject='d_itemwiseprofit', taborder=50)
        self.add('statictext', 'st_date', 1929, 116, 421, 84)
