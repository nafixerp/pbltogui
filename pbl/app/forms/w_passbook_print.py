"""Pass Book Print — w_passbook_print.

Generated from the PowerBuilder window ``w_passbook_print.srw`` by
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
    name='w_passbook_print',
    title='Pass Book Print',
    width=1696,
    height=1148,
    controls=[],
    tables=['kuricolln', 'clients', 'clients_kuridet', 'kuritype', 'date'],
    source_path='w_passbook_print.srw',
    opens=['w_clientshelp'],
    prints=['d_passbook_print', 'd_passbook_print_addr'],
)


class PassBookPrintForm(GeneratedForm):
    """Pass Book Print"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('datawindow', 'dw_accode', 485, 128, 1019, 92, dataobject='d_kuri_cust', taborder=10)
        self.add('statictext', 'st_3', 123, 144, 320, 72, text='Party')
        self.add('singlelineedit', 'sle_name', 485, 224, 1019, 92)
        self.add('statictext', 'st_1', 123, 236, 320, 80, text='Address')
        self.add('editmask', 'em_date1', 485, 320, 434, 100, taborder=20)
        self.add('editmask', 'em_linesperpage', 1262, 320, 238, 92, taborder=100)
        self.add('statictext', 'st_7', 933, 332, 329, 64, text='Lines / page')
        self.add('statictext', 'st_4', 123, 336, 320, 80, text='From Date')
        self.add('editmask', 'em_date2', 485, 424, 434, 100, taborder=30)
        self.add('editmask', 'em_lineshalfpage', 1262, 424, 238, 92, taborder=110)
        self.add('statictext', 'st_2', 123, 440, 320, 80, text='To Date')
        self.add('statictext', 'st_8', 933, 444, 329, 64, text='Lines / Half')
        self.add('editmask', 'em_startline', 485, 528, 434, 100, taborder=40)
        self.add('editmask', 'em_skipmiddle', 1262, 528, 238, 92, taborder=120)
        self.add('statictext', 'st_5', 123, 540, 320, 80, text='Start Line')
        self.add('statictext', 'st_9', 933, 548, 329, 64, text='Skip Middle')
        self.add('singlelineedit', 'sle_docno', 485, 632, 434, 100, taborder=50)
        self.add('editmask', 'em_topmargin', 1262, 632, 238, 92, taborder=130)
        self.add('statictext', 'st_6', 123, 640, 357, 80, text='Start DocNo')
        self.add('statictext', 'st_10', 933, 640, 329, 64, text='Top Margin')
        self.add('editmask', 'em_leftmargin', 1262, 732, 238, 92, taborder=140)
        self.add('singlelineedit', 'sle_slno', 485, 736, 434, 100, taborder=60)
        self.add('statictext', 'st_11', 933, 740, 329, 64, text='Left Margin')
        self.add('statictext', 'st_12', 123, 744, 357, 80, text='Start Slno')
        self.add('datawindow', 'dw_print', 9, 824, 96, 80, dataobject='d_passbook_print')
        self.add('datawindow', 'dw_addr', 133, 824, 96, 80, dataobject='d_passbook_print_addr')
        self.add('editmask', 'em_footermargin', 1262, 832, 238, 92, taborder=150)
        self.add('checkbox', 'cbx_reset', 489, 840, 343, 76, text='Reset')
        self.add('statictext', 'st_13', 910, 840, 352, 64, text='Footer Margin')
        self.add('commandbutton', 'cb_printaddr', 146, 940, 265, 104, text='&Print Addr', taborder=90)
        self.add('commandbutton', 'cb_print', 489, 940, 302, 104, text='&Print', taborder=70)
        self.add('commandbutton', 'cb_exit', 873, 940, 302, 104, text='Exit', taborder=80)
        self.add('commandbutton', 'cb_1', 1262, 940, 238, 104, text='Set Def')
