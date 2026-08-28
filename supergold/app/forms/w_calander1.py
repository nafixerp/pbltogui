"""Calendar — w_calander1.

Generated from the PowerBuilder window ``w_calander1.srw`` by
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
    name='w_calander1',
    title='Calendar',
    width=1312,
    height=1292,
    controls=[],
    tables=[],
    source_path='w_calander1.srw',
)


class CalendarForm(GeneratedForm):
    """Calendar"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('singlelineedit', 'sle_month', 530, 16, 699, 92)
        self.add('editmask', 'em_year', 64, 20, 439, 88, taborder=1)
        self.add('statictext', 'st_1', 69, 236, 137, 76, text='SUN')
        self.add('statictext', 'st_2', 238, 236, 146, 76, text='MON')
        self.add('statictext', 'st_3', 416, 236, 137, 76, text='TUE')
        self.add('statictext', 'st_4', 581, 236, 151, 76, text='WED')
        self.add('statictext', 'st_5', 754, 236, 146, 76, text='THU')
        self.add('statictext', 'st_6', 937, 236, 146, 76, text='FRI')
        self.add('statictext', 'st_7', 1093, 236, 146, 76, text='SAT')
        self.add('commandbutton', 'cb_2', 229, 332, 146, 124)
        self.add('commandbutton', 'cb_3', 398, 332, 146, 124)
        self.add('commandbutton', 'cb_4', 567, 332, 146, 124)
        self.add('commandbutton', 'cb_5', 736, 332, 146, 124)
        self.add('commandbutton', 'cb_6', 905, 332, 146, 124)
        self.add('commandbutton', 'cb_7', 1074, 332, 146, 124)
        self.add('commandbutton', 'cb_1', 59, 336, 146, 124)
        self.add('commandbutton', 'cb_8', 59, 464, 146, 124)
        self.add('commandbutton', 'cb_9', 229, 464, 146, 124)
        self.add('commandbutton', 'cb_10', 398, 464, 146, 124)
        self.add('commandbutton', 'cb_11', 567, 464, 146, 124)
        self.add('commandbutton', 'cb_12', 736, 464, 146, 124)
        self.add('commandbutton', 'cb_13', 905, 464, 146, 124)
        self.add('commandbutton', 'cb_14', 1074, 464, 146, 124)
        self.add('commandbutton', 'cb_15', 59, 596, 146, 124)
        self.add('commandbutton', 'cb_16', 229, 596, 146, 124)
        self.add('commandbutton', 'cb_17', 398, 596, 146, 124)
        self.add('commandbutton', 'cb_18', 567, 596, 146, 124)
        self.add('commandbutton', 'cb_19', 736, 596, 146, 124)
        self.add('commandbutton', 'cb_20', 905, 596, 146, 124)
        self.add('commandbutton', 'cb_21', 1074, 596, 146, 124)
        self.add('commandbutton', 'cb_22', 59, 728, 146, 124)
        self.add('commandbutton', 'cb_23', 229, 728, 146, 124)
        self.add('commandbutton', 'cb_24', 398, 728, 146, 124)
        self.add('commandbutton', 'cb_25', 567, 728, 146, 124)
        self.add('commandbutton', 'cb_26', 736, 728, 146, 124)
        self.add('commandbutton', 'cb_27', 905, 728, 146, 124)
        self.add('commandbutton', 'cb_28', 1074, 728, 146, 124)
        self.add('commandbutton', 'cb_29', 59, 860, 146, 124)
        self.add('commandbutton', 'cb_30', 229, 860, 146, 124)
        self.add('commandbutton', 'cb_31', 398, 860, 146, 124)
        self.add('commandbutton', 'cb_32', 567, 860, 146, 124)
        self.add('commandbutton', 'cb_33', 736, 860, 146, 124)
        self.add('commandbutton', 'cb_34', 905, 860, 146, 124)
        self.add('commandbutton', 'cb_35', 1074, 860, 146, 124)
        self.add('commandbutton', 'cb_36', 59, 992, 146, 124)
        self.add('commandbutton', 'cb_37', 229, 992, 146, 124)
        self.add('commandbutton', 'cb_38', 398, 992, 146, 124)
        self.add('commandbutton', 'cb_39', 567, 992, 146, 124)
        self.add('commandbutton', 'cb_40', 736, 992, 146, 124)
        self.add('commandbutton', 'cb_41', 905, 992, 146, 124)
        self.add('commandbutton', 'cb_42', 1074, 992, 146, 124)
        self.add('statictext', 'st_8', 0, 1136, 1303, 76, text='Page Up->Next Month, Page Down ->Previous Month')
