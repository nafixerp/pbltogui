"""Day History — w_daysumm.

Generated from the PowerBuilder window ``w_daysumm.srw`` by
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
    name='w_daysumm',
    title='Day History',
    width=3634,
    height=2200,
    controls=[],
    tables=[],
    source_path='w_daysumm.srw',
    report={'dataobject': 'd_daysummary_part1', 'sql': 'SELECT items.name AS items_name, salesd.qty AS salesd_qty, salesd.weight AS salesd_weight, salesm.slno AS salesm_slno FROM items, salesd, salesm WHERE items.code = salesd.code AND salesd.slno = salesm.slno AND salesm.tdate = :rdate AND salesm.control <= :rlevel ORDER BY items.name ASC', 'computes': [{'name': '', 'expression': 'sum(qty for all )', 'format': '###0', 'label': '', 'band': 'summary'}, {'name': '', 'expression': 'sum(weight for all )', 'format': '####0.000', 'label': '', 'band': 'summary'}], 'args': ['rdate', 'rlevel'], 'arg_types': {'rdate': 'date', 'rlevel': 'number'}, 'tables': ['items', 'salesd', 'salesm'], 'columns': [{'name': 'slno', 'label': 'Slno', 'type': 'number'}, {'name': 'qty', 'label': 'Qty', 'type': 'number'}, {'name': 'weight', 'label': 'Weight', 'type': 'number'}]},
)


class DayHistoryForm(GeneratedForm):
    """Day History"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 535, 0, 430, 100, taborder=10)
        self.add('dropdownlistbox', 'ddlb_part', 1207, 0, 585, 508, text='Part 1', items=['Part 1', 'Part 2', 'Part 3', 'Part 4'], taborder=20)
        self.add('commandbutton', 'cb_show', 1970, 0, 293, 100, text='&Show', taborder=30)
        self.add('commandbutton', 'cb_print', 2802, 8, 233, 88, text='&Print', taborder=60)
        self.add('commandbutton', 'cb_exit', 3049, 8, 233, 88, text='E&xit', taborder=50)
        self.add('statictext', 'st_1', 5, 12, 512, 64, text='Enter Date :')
        self.add('datawindow', 'dw_daysumm', 0, 108, 3589, 1984, dataobject='d_daysummary_part1', taborder=40)
