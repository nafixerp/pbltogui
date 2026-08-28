"""Update from HO — w_jewl_update.

Generated from the PowerBuilder window ``w_jewl_update.srw`` by
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
    name='w_jewl_update',
    title='Update from HO',
    width=3698,
    height=2380,
    controls=[],
    tables=['items', 'itemsstk', 'daybook', 'barcode', 'barcode_dmddet', 'smithm', 'smithd', 'barcodedmd', 'other', 'generals', 'generali', 'daybookpart'],
    source_path='w_jewl_update.srw',
)


class UpdateFromHoForm(GeneratedForm):
    """Update from HO"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('commandbutton', 'cb_selectupdation', 5, 0, 544, 96, text='Select Updations', taborder=30)
        self.add('commandbutton', 'cb_update', 2542, 0, 549, 96, text='&Update', taborder=10)
        self.add('commandbutton', 'cb_1', 3095, 0, 265, 96, text='&Print', taborder=60)
        self.add('commandbutton', 'cb_2', 3360, 0, 265, 96, text='E&xit', taborder=50)
        self.add('datawindow', 'dw_counter', 965, 4, 654, 88, dataobject='d_countercode', taborder=50)
        self.add('listbox', 'lb_errors', 1710, 4, 192, 164, items=['Errors'], taborder=40)
        self.add('checkbox', 'cbx_barcodeonly', 1911, 8, 626, 80, text='Update Barcode Only')
        self.add('statictext', 'st_2', 654, 12, 297, 76, text='Counter :')
        self.add('datawindow', 'dw_1', 5, 100, 3621, 2084, taborder=20)
        self.add('statictext', 'st_from', 2784, 116, 617, 72)
