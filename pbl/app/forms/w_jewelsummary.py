"""Sales/Purchase Item Report — w_jewelsummary.

Generated from the PowerBuilder window ``w_jewelsummary.srw`` by
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
    name='w_jewelsummary',
    title='Sales/Purchase Item Report',
    width=3675,
    height=2300,
    controls=[],
    tables=['accountm', 'daybook'],
    source_path='w_jewelsummary.srw',
    report={'dataobject': 'd_jewlsummary', 'sql': 'SELECT onerec.field AS onerec_field FROM onerec', 'args': ['rdate1', 'rdate2', 'rlevel', 'rcode', 'rname', 'rclbalance'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date', 'rlevel': 'number', 'rcode': 'string', 'rname': 'string', 'rclbalance': 'decimal'}, 'tables': ['onerec'], 'columns': [{'name': 'field', 'label': 'field', 'type': 'char'}]},
)


class SalesPurchaseItemReportForm(GeneratedForm):
    """Sales/Purchase Item Report"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 1189, 0, 430, 92, taborder=20)
        self.add('editmask', 'em_date2', 1975, 0, 430, 92, taborder=30)
        self.add('commandbutton', 'cb_show', 2446, 0, 261, 96, text='&Show', taborder=40)
        self.add('commandbutton', 'cb_3', 2779, 0, 261, 96, text='Save &As', taborder=70)
        self.add('commandbutton', 'cb_1', 3067, 0, 265, 96, text='&Print', taborder=80)
        self.add('commandbutton', 'cb_2', 3333, 0, 265, 96, text='E&xit', taborder=60)
        self.add('statictext', 'st_3', 0, 8, 357, 72, text='Jewellery :')
        self.add('datawindow', 'dw_accode', 361, 8, 434, 92, dataobject='d_jewl', taborder=10)
        self.add('statictext', 'st_2', 1655, 12, 302, 72, text='Date To :')
        self.add('statictext', 'st_1', 809, 20, 370, 64, text='Date From :')
        self.add('datawindow', 'dw_1', 0, 100, 3616, 2084, dataobject='d_jewlsummary', taborder=50)
