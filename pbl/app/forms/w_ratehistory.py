"""Rate History — w_ratehistory.

Generated from the PowerBuilder window ``w_ratehistory.srw`` by
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
    name='w_ratehistory',
    title='Rate History',
    width=2665,
    height=2212,
    controls=[],
    tables=['ratehistory', 'salesm'],
    source_path='w_ratehistory.srw',
    report={'dataobject': 'd_ratehistory_rep', 'sql': 'SELECT ratehistory.tdate AS ratehistory_tdate, ratehistory.grate AS ratehistory_grate, ratehistory.srate AS ratehistory_srate, ratehistory.thrate AS ratehistory_thrate, ratehistory.prate AS ratehistory_prate FROM ratehistory ORDER BY ratehistory.tdate ASC', 'computes': [{'name': 'compute_4', 'expression': 'avg( grate for all )', 'format': '#####0.00', 'label': 'compute_4', 'band': 'summary'}, {'name': 'compute_5', 'expression': 'avg( prate for all )', 'format': '######0.00', 'label': 'compute_5', 'band': 'summary'}, {'name': 'compute_3', 'expression': 'avg( srate for all )', 'format': '#####0.00', 'label': 'compute_3', 'band': 'summary'}, {'name': 'compute_2', 'expression': 'avg( thrate for all )', 'format': '#####0.00', 'label': 'compute_2', 'band': 'summary'}], 'args': ['rdate1', 'rdate2'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date'}, 'tables': ['ratehistory'], 'columns': [{'name': 'tdate', 'label': 'tdate', 'type': 'date'}, {'name': 'grate', 'label': 'grate', 'type': 'decimal'}, {'name': 'srate', 'label': 'srate', 'type': 'decimal'}, {'name': 'thrate', 'label': 'thrate', 'type': 'decimal'}, {'name': 'prate', 'label': 'prate', 'type': 'decimal'}]},
)


class RateHistoryForm(GeneratedForm):
    """Rate History"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 206, 0, 448, 92, taborder=10)
        self.add('editmask', 'em_date2', 891, 0, 448, 92, taborder=20)
        self.add('commandbutton', 'cb_show', 1422, 0, 261, 92, text='&Show', taborder=30)
        self.add('commandbutton', 'cb_saveas', 1751, 0, 261, 92, text='Save &As', taborder=30)
        self.add('commandbutton', 'cb_1', 2071, 0, 261, 92, text='&Print', taborder=60)
        self.add('commandbutton', 'cb_2', 2400, 0, 261, 92, text='E&xit', taborder=50)
        self.add('statictext', 'st_dt1', 0, 4, 197, 76, text='From :')
        self.add('statictext', 'st_dt2', 754, 12, 133, 76, text='To :')
        self.add('datawindow', 'dw_1', 0, 96, 2638, 1940, dataobject='d_ratehistory_rep', taborder=40)
        self.add('commandbutton', 'cb_recalc', 5, 2044, 411, 84, text='Recalc Rates', taborder=41)
