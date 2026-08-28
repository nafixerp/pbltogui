"""Op.Weight Entry — w_partywgtbal_opbal.

Generated from the PowerBuilder window ``w_partywgtbal_opbal.srw`` by
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
    name='w_partywgtbal_opbal',
    title='Op.Weight Entry',
    width=1934,
    height=956,
    controls=[],
    tables=['accountm'],
    source_path='w_partywgtbal_opbal.srw',
)


class OpWeightEntryForm(GeneratedForm):
    """Op.Weight Entry"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('datawindow', 'dw_accode', 567, 32, 402, 92, dataobject='d_sucucode', taborder=10)
        self.add('checkbox', 'cbx_genacc', 1202, 36, 498, 80, text='Gen. Accounts')
        self.add('statictext', 'st_3', 215, 40, 338, 72, text='Party  :')
        self.add('commandbutton', 'cb_new', 978, 40, 174, 80, text='New')
        self.add('singlelineedit', 'sle_name', 567, 128, 1152, 92)
        self.add('statictext', 'st_1', 210, 136, 343, 80, text='Name :')
        self.add('editmask', 'em_weight', 567, 224, 398, 92, taborder=20)
        self.add('statictext', 'st_5', 197, 236, 357, 80, text='Op.Weight :')
        self.add('editmask', 'em_weightb', 567, 320, 398, 92, taborder=30)
        self.add('statictext', 'st_2', 155, 332, 398, 80, text='Op.WeightB :')
        self.add('commandbutton', 'cb_save', 576, 512, 274, 108, text='&Save', taborder=40)
        self.add('commandbutton', 'cb_exit', 864, 512, 274, 108, text='E&xit', taborder=50)
