"""POS Download — w_pos_update.

Generated from the PowerBuilder window ``w_pos_update.srw`` by
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
    name='w_pos_update',
    title='POS Download',
    width=3141,
    height=2120,
    controls=[],
    tables=['clients', 'daybook', 'kuricolln', 'clients_kuridet', 'transact', 'olecustomcontrol', 'kuritype', 'kcomntable', 'pos', 'server', 'txt', 'paycollect', 'generali', 'daybookpart'],
    source_path='w_pos_update.srw',
)


class PosDownloadForm(GeneratedForm):
    """POS Download"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('olecustomcontrol', 'ds_chits_obj', 2976, 0, 1317, 768, taborder=80)
        self.add('singlelineedit', 'sle_posfile', 421, 64, 2281, 100, taborder=10)
        self.add('commandbutton', 'cb_setdef', 2711, 68, 197, 96, text='Set Def')
        self.add('statictext', 'st_1', 50, 76, 352, 72, text='POS File :')
        self.add('datawindow', 'dw_staff', 421, 172, 402, 88, dataobject='d_staffcode', taborder=40)
        self.add('commandbutton', 'cb_update', 2281, 172, 626, 96, text='&Update From Txt File', taborder=110)
        self.add('statictext', 'st_staffname', 878, 176, 1280, 88)
        self.add('statictext', 'st_7', 50, 180, 352, 72, text='Staff :')
        self.add('datawindow', 'dw_cashbank', 421, 268, 882, 88, dataobject='d_cashbankcode', taborder=50)
        self.add('statictext', 'st_6', 46, 272, 357, 72, text='Cash/Bank :')
        self.add('commandbutton', 'cb_update2', 2089, 272, 818, 96, text='&Update from Paycollect(MDB)', taborder=100)
        self.add('checkbox', 'cbx_sendsms', 1586, 364, 494, 80, text='Send SMS')
        self.add('editmask', 'em_date1', 421, 368, 439, 96, taborder=60)
        self.add('checkbox', 'cbx_rcptpmnt', 878, 368, 603, 80, text='Update Rcpt/Pmnt')
        self.add('editmask', 'em_trandate', 2464, 372, 439, 96, taborder=80)
        self.add('statictext', 'st_date', 50, 376, 352, 72, text='Date From :')
        self.add('statictext', 'st_3', 2121, 384, 334, 64, text='Tran Date :')
        self.add('commandbutton', 'cb_updtfromserver', 878, 464, 626, 108, text='Update From Server', taborder=120)
        self.add('commandbutton', 'cb_direct', 1586, 464, 626, 108, text='Direct Update', taborder=90)
        self.add('commandbutton', 'cb_exit', 2281, 464, 626, 108, text='&Exit', taborder=110)
        self.add('editmask', 'em_date2', 421, 476, 439, 96, taborder=70)
        self.add('statictext', 'st_2', 50, 484, 352, 72, text='Date To :')
        self.add('editmask', 'em_grate', 421, 584, 439, 96, taborder=80)
        self.add('statictext', 'st_status', 878, 584, 626, 96)
        self.add('statictext', 'st_rec', 1586, 584, 626, 96)
        self.add('commandbutton', 'cb_print', 2281, 584, 320, 112, text='Print', taborder=90)
        self.add('commandbutton', 'cb_saveas', 2597, 584, 306, 112, text='Save As', taborder=80)
        self.add('statictext', 'st_4', 50, 596, 352, 72, text='Gold Rate :')
        self.add('datawindow', 'dw_data', 0, 696, 3113, 1152, dataobject='d_posdata', taborder=110)
        self.add('statictext', 'st_msg', 73, 1852, 2825, 176)
