"""New Issue — w_modeltrans.

Generated from the PowerBuilder window ``w_modeltrans.srw`` by
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
    name='w_modeltrans',
    title='New Issue',
    width=1801,
    height=1644,
    controls=[],
    tables=['items', 'modelm', 'barcode', 'itemadj', 'clients', 'generali'],
    source_path='w_modeltrans.srw',
)


class NewIssueForm(GeneratedForm):
    """New Issue"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('singlelineedit', 'sle_retno', 434, 12, 398, 92)
        self.add('statictext', 'st_3', 133, 16, 288, 76, text='Ret. No.  :')
        self.add('checkbox', 'cbx_retn', 933, 20, 293, 80, text='Return')
        self.add('singlelineedit', 'sle_bcode', 434, 112, 402, 88, taborder=10)
        self.add('statictext', 'st_frombcode', 55, 116, 366, 76, text='Barcode :')
        self.add('datawindow', 'dw_smcode', 434, 204, 677, 88, dataobject='d_smancode', taborder=20)
        self.add('statictext', 'st_20', 133, 216, 288, 76, text='SM Name :')
        self.add('editmask', 'em_date', 434, 296, 398, 92, taborder=30)
        self.add('statictext', 'st_14', 174, 312, 247, 76, text='Date :')
        self.add('datawindow', 'dw_1', 434, 396, 402, 88, dataobject='d_cust', taborder=40)
        self.add('commandbutton', 'cb_custhelp', 841, 400, 64, 84, text='^')
        self.add('statictext', 'st_1', 174, 404, 247, 76, text='Party :')
        self.add('singlelineedit', 'sle_partyname', 434, 492, 1134, 92, limit=40, taborder=50)
        self.add('statictext', 'st_2', 174, 504, 247, 76, text='Name :')
        self.add('singlelineedit', 'sle_icode', 434, 588, 320, 100, taborder=60)
        self.add('commandbutton', 'cb_help1', 768, 596, 64, 84, text='^')
        self.add('singlelineedit', 'sle_iname', 846, 596, 722, 92)
        self.add('statictext', 'st_4', 82, 604, 338, 76, text='Item Code :')
        self.add('editmask', 'em_qty', 434, 696, 320, 100, taborder=70)
        self.add('statictext', 'st_6', 270, 712, 151, 76, text='Qty :')
        self.add('editmask', 'em_wgt', 434, 800, 320, 100, taborder=80)
        self.add('statictext', 'st_7', 155, 816, 265, 76, text='Weight :')
        self.add('editmask', 'em_stwgt', 434, 904, 320, 100, taborder=90)
        self.add('statictext', 'st_15', 174, 912, 247, 76, text='St.Wgt :')
        self.add('datawindow', 'dw_stktype', 434, 1004, 539, 88, dataobject='d_stktypecode', taborder=100)
        self.add('statictext', 'st_17', 110, 1012, 311, 76, text='Stk Type :')
        self.add('singlelineedit', 'sle_reason', 434, 1100, 1134, 92, limit=30, taborder=110)
        self.add('statictext', 'st_5', 110, 1112, 311, 76, text='Note :')
        self.add('oval', 'oval_1', 507, 1212, 768, 224)
        self.add('commandbutton', 'cb_save', 635, 1268, 242, 104, text='&Save', taborder=120)
        self.add('commandbutton', 'cb_exit', 905, 1268, 242, 104, text='E&xit', taborder=130)
