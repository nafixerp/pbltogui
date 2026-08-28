"""Barcode History — w_barcode_history.

Generated from the PowerBuilder window ``w_barcode_history.srw`` by
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
    name='w_barcode_history',
    title='Barcode History',
    width=2903,
    height=1824,
    controls=[],
    tables=['itemadj', 'salesm', 'salesrm', 'smithm', 'barcode', 'items', 'date'],
    source_path='w_barcode_history.srw',
)


class BarcodeHistoryForm(GeneratedForm):
    """Barcode History"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('singlelineedit', 'sle_itemcode', 306, 0, 416, 96, limit=10, taborder=10)
        self.add('editmask', 'em_date1', 1129, 0, 375, 96, taborder=20)
        self.add('editmask', 'em_date2', 1664, 0, 379, 96, taborder=30)
        self.add('commandbutton', 'cb_show', 2071, 0, 288, 96, text='&Show', taborder=40)
        self.add('commandbutton', 'cb_print', 2373, 0, 247, 96, text='&Print', taborder=70)
        self.add('commandbutton', 'cb_exit', 2629, 0, 247, 96, text='E&xit', taborder=60)
        self.add('commandbutton', 'cb_help', 727, 4, 178, 92, text='&Help')
        self.add('statictext', 'st_3', 9, 8, 297, 72, text='Barcode :')
        self.add('statictext', 'st_1', 914, 8, 206, 76, text='From :')
        self.add('statictext', 'st_2', 1536, 8, 119, 76, text='To :')
        self.add('datawindow', 'dw_history', 5, 104, 2875, 1628, dataobject='d_barcode_history', taborder=50)
        self.add('statictext', 'st_date', 1929, 116, 421, 84)
