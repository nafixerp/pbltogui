"""New Entry — w_refnenter.

Generated from the PowerBuilder window ``w_refnenter.srw`` by
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
    name='w_refnenter',
    title='New Entry',
    width=3657,
    height=1644,
    controls=[],
    tables=['items', 'itemsstk', 'refinerym', 'refineryd', 'clients', 'sman', 'generali'],
    source_path='w_refnenter.srw',
    opens=['w_clientshelp', 'w_refineryprint_view', 'w_stktypeqtype', 'w_itemhelp'],
)


class NewEntryForm(GeneratedForm):
    """New Entry"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('statictext', 'st_billno', 485, 76, 411, 96)
        self.add('editmask', 'em_date', 2400, 76, 402, 96, taborder=10)
        self.add('statictext', 'st_bill', 174, 84, 297, 64, text='Doc No :')
        self.add('statictext', 'st_date', 2085, 84, 293, 64, text='Date :')
        self.add('editmask', 'em_custcode', 1001, 112, 329, 96)
        self.add('datawindow', 'dw_1', 485, 212, 416, 88, dataobject='d_refncode', taborder=20)
        self.add('statictext', 'st_custname', 1006, 212, 1038, 96)
        self.add('commandbutton', 'cb_custhelp', 914, 216, 64, 84, text='^')
        self.add('datawindow', 'dw_smcode', 2400, 220, 677, 88, dataobject='d_smancode', taborder=30)
        self.add('statictext', 'st_custcode', 155, 224, 315, 68, text='Refiner :')
        self.add('statictext', 'st_4', 2130, 232, 247, 76, text='SM :')
        self.add('datawindow', 'dw_sale', 0, 336, 3625, 796, dataobject='d_refn', taborder=40)
        self.add('statictext', 'st_7', 1221, 336, 5, 796)
        self.add('statictext', 'st_1', 1559, 336, 5, 796)
        self.add('statictext', 'st_2', 1833, 336, 5, 796)
        self.add('statictext', 'st_6', 2103, 336, 5, 796)
        self.add('statictext', 'st_9', 2382, 336, 5, 796)
        self.add('statictext', 'st_5', 2633, 336, 5, 796)
        self.add('statictext', 'st_50', 2944, 336, 5, 796)
        self.add('statictext', 'st_54', 3282, 336, 5, 796)
        self.add('statictext', 'st_3', 475, 340, 5, 692)
        self.add('commandbutton', 'cb_add', 9, 1040, 247, 76, text='&Add')
        self.add('commandbutton', 'cb_delete', 261, 1040, 247, 76, text='&Delete')
        self.add('statictext', 'st_stktype', 558, 1040, 238, 76)
        self.add('statictext', 'st_stock', 1038, 1040, 238, 76)
        self.add('editmask', 'em_expwgt', 2240, 1136, 402, 92, text='none')
        self.add('singlelineedit', 'sle_note', 238, 1140, 1138, 88, limit=30, taborder=50)
        self.add('statictext', 'st_18', 14, 1148, 274, 76, text='Note  :')
        self.add('statictext', 'st_8', 1778, 1152, 453, 64, text='Expected Wgt :')
        self.add('roundrectangle', 'rr_1', 2816, 1152, 526, 252)
        self.add('commandbutton', 'cb_save', 2875, 1168, 416, 96, text='&Save', taborder=60)
        self.add('commandbutton', 'cb_exit', 2875, 1280, 416, 96, text='E&xit', taborder=70)
