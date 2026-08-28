"""Item Report — w_loanentry_item_rep.

Generated from the PowerBuilder window ``w_loanentry_item_rep.srw`` by
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
    name='w_loanentry_item_rep',
    title='Item Report',
    width=3671,
    height=2416,
    controls=[],
    tables=[],
    source_path='w_loanentry_item_rep.srw',
    report={'dataobject': 'd_loanentry_item_rep', 'sql': 'SELECT loan_items.item AS loan_items_item, (select items.name from items where items.code = loan_items.item) as itemname, (select sum(item.qty) from loan_items item, loan where item.slno = loan.slno and loan.tdate >= :rdate1 and loan.tdate <= :rdate2 and loan.loantype = :rloantype and loan.closed = ifnull(:rpend , loan.closed, :rpend) ) as tqty, (select sum(item.weight) from loan_items item, loan where item.slno = loan.slno and loan.tdate >= :rdate1 and loan.tdate <= :rdate2 and loan.loantype = :rloantype and loan.closed = ifnull(:rpend , loan.closed, :rpend) ) as twgt FROM loan_items, loan WHERE loan_items.slno = loan.slno ORDER BY 2 ASC', 'computes': [{'name': 'compute_1', 'expression': 'sum(tqty for all)', 'format': '#######0', 'label': 'compute_1', 'band': 'summary'}, {'name': 'compute_2', 'expression': 'sum(twgt for all)', 'format': '#######0.000', 'label': 'compute_2', 'band': 'summary'}], 'args': ['rdate1', 'rdate2', 'rloantype', 'rpend'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date', 'rloantype': 'string', 'rpend': 'string'}, 'tables': ['loan_items', 'loan'], 'columns': [{'name': 'loan_items_item', 'label': 'Item Code', 'type': 'char'}, {'name': 'itemname', 'label': 'Item Name', 'type': 'char'}, {'name': 'tqty', 'label': 'Qty', 'type': 'long'}, {'name': 'twgt', 'label': 'Weight', 'type': 'decimal'}]},
)


class ItemReportForm(GeneratedForm):
    """Item Report"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 206, 0, 379, 92, taborder=10)
        self.add('editmask', 'em_date2', 745, 0, 379, 92, taborder=20)
        self.add('dropdownlistbox', 'ddlb_type', 1152, 0, 608, 676, text='Guarantee Items', items=['Guarantee Items', 'Sales Items'], taborder=60)
        self.add('commandbutton', 'cb_show', 2386, 0, 261, 92, text='&Show', taborder=30)
        self.add('commandbutton', 'cb_sort', 2656, 0, 247, 92, text='So&rt', taborder=40)
        self.add('commandbutton', 'cb_1', 2907, 0, 251, 92, text='Save &As', taborder=90)
        self.add('commandbutton', 'cb_print', 3163, 0, 233, 92, text='&Print', taborder=80)
        self.add('commandbutton', 'cb_exit', 3397, 0, 233, 92, text='E&xit', taborder=100)
        self.add('statictext', 'st_1', 0, 8, 197, 64, text='From :')
        self.add('statictext', 'st_2', 613, 12, 123, 72, text='To :')
        self.add('checkbox', 'cbx_pendingonly', 1801, 16, 480, 80, text='Pending Only')
        self.add('datawindow', 'dw_1', 0, 100, 3630, 2036, dataobject='d_loanentry_item_rep', taborder=70)
