"""POS Upload — w_pos_update_tofile.

Generated from the PowerBuilder window ``w_pos_update_tofile.srw`` by
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
    name='w_pos_update_tofile',
    title='POS Upload',
    width=2482,
    height=1496,
    controls=[],
    tables=['clients', 'clients_kuridet', 'master', 'daybook', 'login', 'transact', 'olecustomcontrol', 'kuricolln', 'pos'],
    source_path='w_pos_update_tofile.srw',
    grid={'control': 'dw_possys', 'dataobject': 'd_possyssel', 'table': 'codehelp', 'keys': ['code'], 'columns': [{'name': 'code', 'label': 'code', 'type': 'char'}]},
    report={'dataobject': 'd_possyssel', 'sql': 'SELECT codehelp.code AS codehelp_code FROM codehelp', 'args': [], 'arg_types': {}, 'tables': ['codehelp'], 'columns': [{'name': 'code', 'label': 'code', 'type': 'char'}]},
    opens=['w_cbachdhelp', 'w_possysentry'],
)


class PosUploadForm(GeneratedForm):
    """POS Upload"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('singlelineedit', 'sle_posfile', 421, 64, 1673, 100, taborder=10)
        self.add('commandbutton', 'cb_setdef', 2094, 68, 219, 96, text='Set Def')
        self.add('statictext', 'st_1', 50, 76, 352, 72, text='POS File :')
        self.add('commandbutton', 'cb_update', 1550, 176, 544, 96, text='&Update MST By Txt', taborder=70)
        self.add('datawindow', 'dw_possys', 421, 180, 832, 84, dataobject='d_possyssel', taborder=20)
        self.add('commandbutton', 'cb_new', 1266, 184, 224, 80, text='New')
        self.add('statictext', 'st_3', 50, 188, 352, 72, text='System :')
        self.add('datawindow', 'dw_rout', 421, 280, 791, 88, dataobject='d_clientsroute_code', taborder=30)
        self.add('commandbutton', 'cb_update2', 1221, 280, 882, 96, text='&Update To Paycollect(MDB)', taborder=60)
        self.add('statictext', 'st_5', 50, 284, 352, 72, text='Route :')
        self.add('datawindow', 'dw_staff', 421, 380, 402, 88, dataobject='d_staffcode', taborder=40)
        self.add('statictext', 'st_staffname', 837, 380, 1257, 88)
        self.add('statictext', 'st_7', 50, 388, 352, 72, text='Agent :')
        self.add('editmask', 'em_date', 421, 496, 439, 96, taborder=50)
        self.add('statictext', 'st_date', 50, 504, 352, 72, text='Date  :')
        self.add('checkbox', 'cbx_deleteall', 1115, 504, 837, 80, text='Delete all Datas from POS')
        self.add('olecustomcontrol', 'ds_chits_obj', 2034, 508, 1317, 768, taborder=60)
        self.add('checkbox', 'cbx_customermaster', 421, 612, 567, 80, text='Customer Master')
        self.add('checkbox', 'cbx_balance', 1115, 612, 805, 80, text='Update Cur.Balance Also')
        self.add('checkbox', 'cbx_agentmaster', 421, 708, 567, 80, text='Agent Master')
        self.add('commandbutton', 'cb_updttoserver', 421, 908, 544, 96, text='Update To Server', taborder=70)
        self.add('commandbutton', 'cb_directupdt', 987, 908, 544, 96, text='Direct Update', taborder=80)
        self.add('commandbutton', 'cb_exit', 1550, 908, 544, 96, text='&Exit', taborder=70)
        self.add('statictext', 'st_status', 421, 1064, 1664, 92)
        self.add('statictext', 'st_rec', 421, 1184, 1664, 92)
