"""Rate — w_setuprate_international.

Generated from the PowerBuilder window ``w_setuprate_international.srw`` by
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
    name='w_setuprate_international',
    title='Rate',
    width=1330,
    height=1788,
    controls=[],
    tables=['ratehistory', 'itemsqtype', 'internet', 'generald', 'userd', 'generals'],
    source_path='w_setuprate_international.srw',
    grid={'control': 'dw_1', 'dataobject': 'd_ratesetup', 'table': 'itemsqtype', 'keys': ['code'], 'computes': [], 'columns': [{'name': 'code', 'label': 'Purity', 'type': 'char'}, {'name': 'touch', 'label': 'Touch', 'type': 'decimal'}, {'name': 'rate', 'label': 'Rate', 'type': 'decimal'}]},
    report={'dataobject': 'd_ratesetup', 'sql': 'SELECT itemsqtype.code AS itemsqtype_code, itemsqtype.touch AS itemsqtype_touch, itemsqtype.rate AS itemsqtype_rate FROM itemsqtype', 'computes': [], 'args': [], 'arg_types': {}, 'tables': ['itemsqtype'], 'columns': [{'name': 'code', 'label': 'Purity', 'type': 'char'}, {'name': 'touch', 'label': 'Touch', 'type': 'decimal'}, {'name': 'rate', 'label': 'Rate', 'type': 'decimal'}]},
)


class RateForm(GeneratedForm):
    """Rate"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('statictext', 'st_hd', 9, 4, 1307, 88)
        self.add('commandbutton', 'cb_auto', 1129, 104, 178, 96, text='Auto', taborder=20)
        self.add('editmask', 'em_ouncerate', 709, 108, 416, 88, taborder=10)
        self.add('statictext', 'st_5', 18, 112, 667, 76, text='Gold Rate/Ounce(USD)')
        self.add('editmask', 'em_conversion', 709, 200, 416, 88, taborder=20)
        self.add('statictext', 'st_conversion', 18, 204, 667, 76, text='Conversion Rate')
        self.add('datawindow', 'dw_1', 18, 296, 1271, 1032, dataobject='d_ratesetup', taborder=30)
        self.add('editmask', 'em_srate', 846, 1336, 443, 88, taborder=40)
        self.add('statictext', 'st_35', 18, 1344, 402, 76, text='Silver Rate')
        self.add('commandbutton', 'cb_ok', 283, 1520, 343, 100, text='&Save')
        self.add('commandbutton', 'cb_cancel', 663, 1520, 343, 100, text='E&xit')
