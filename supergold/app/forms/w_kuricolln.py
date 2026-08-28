"""Kuri Collection — w_kuricolln.

Generated from the PowerBuilder window ``w_kuricolln.srw`` by
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
    name='w_kuricolln',
    title='Kuri Collection',
    width=4466,
    height=1992,
    controls=[],
    tables=['kuricolln', 'daybook', 'clients_kuridet', 'clients', 'accountm', 'pos', 'ratehistory', 'kuritype', 'generali', 'daybookpart', 'userd'],
    source_path='w_kuricolln.srw',
    report={'dataobject': 'd_kuricolln', 'sql': "SELECT kuricolln.tdate AS kuricolln_tdate, kuricolln.code AS kuricolln_code, kuricolln.rcptno AS kuricolln_rcptno, kuricolln.amount AS kuricolln_amount, kuricolln.agent AS kuricolln_agent, kuricolln.slno AS kuricolln_slno, kuricolln.wgt AS kuricolln_wgt, (select daybookpart.vchno from daybookpart where daybookpart.slno = kuricolln.slno) as vchno, (1) as prnt, (0.00) as ob, (0.00) as minlimit, (0.00) as maxlimit, (0.00) as totcolln, (0.0001) as obwgt, ('N') as showwgt FROM kuricolln ORDER BY kuricolln.sno ASC", 'computes': [{'name': 'compute_1', 'expression': ' code ', 'format': '[GENERAL]', 'label': 'compute_1', 'band': 'detail'}, {'name': 'cb', 'expression': 'if(isnull( ob),0,ob)  +  if(isnull( amount ),0,amount)', 'format': '############0.00', 'label': 'cb', 'band': 'detail'}, {'name': 'compute_2', 'expression': 'if(isnull( obwgt),0,obwgt)  +  if(isnull( wgt),0,wgt )', 'format': '##########0.000', 'label': 'compute_2', 'band': 'detail'}], 'args': ['rdate'], 'arg_types': {'rdate': 'date'}, 'tables': ['kuricolln'], 'columns': [{'name': 'tdate', 'label': 'Date', 'type': 'date'}, {'name': 'code', 'label': 'Party', 'type': 'char'}, {'name': 'rcptno', 'label': 'Rcpt No', 'type': 'char'}, {'name': 'amount', 'label': 'Amount', 'type': 'decimal'}, {'name': 'agent', 'label': 'Coln Agent', 'type': 'char'}, {'name': 'slno', 'label': 'slno', 'type': 'decimal'}, {'name': 'vchno', 'label': 'vchno', 'type': 'char'}, {'name': 'prnt', 'label': 'Prnt', 'type': 'long'}, {'name': 'ob', 'label': 'OB (Amt)', 'type': 'decimal'}, {'name': 'minlimit', 'label': 'minlimit', 'type': 'decimal'}, {'name': 'maxlimit', 'label': 'maxlimit', 'type': 'decimal'}, {'name': 'totcolln', 'label': 'totcolln', 'type': 'decimal'}, {'name': 'obwgt', 'label': 'OB (Wgt)', 'type': 'decimal'}, {'name': 'wgt', 'label': 'In Wgt', 'type': 'decimal'}, {'name': 'showwgt', 'label': 'showwgt', 'type': 'char'}]},
    opens=['w_rcptpmnt_view', 'w_clientshelp'],
)


class KuriCollectionForm(GeneratedForm):
    """Kuri Collection"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date', 626, 0, 434, 96, taborder=10)
        self.add('commandbutton', 'cb_edit', 1230, 0, 343, 96, text='&Edit')
        self.add('commandbutton', 'cb_updtfrompos', 2551, 0, 512, 96, text='Update From POS')
        self.add('statictext', 'st_10', 96, 4, 517, 76, text='Collection Date :')
        self.add('statictext', 'st_woodqbic', 2053, 24, 82, 76)
        self.add('statictext', 'st_others', 1906, 28, 119, 76)
        self.add('editmask', 'em_goldrate', 626, 100, 434, 96, taborder=20)
        self.add('statictext', 'st_1', 96, 104, 517, 76, text='Gold Rate :')
        self.add('checkbox', 'cbx_autorate', 1230, 124, 402, 56, text='Auto Rate')
        self.add('checkbox', 'cbx_autoincreasercptno', 1682, 124, 745, 56, text='Auto Increase Rcpt No')
        self.add('statictext', 'st_2', 96, 200, 517, 76, text='Cash A/c :')
        self.add('datawindow', 'dw_cashbank', 626, 200, 882, 88, dataobject='d_cashbankcode', taborder=30)
        self.add('commandbutton', 'cb_selall', 2551, 200, 512, 96, text='Sel All')
        self.add('checkbox', 'cbx_sortonrcptno', 1682, 208, 745, 56, text='Sort On Rcpt No in Edit')
        self.add('datawindow', 'dw_dim', 5, 296, 4443, 1304, dataobject='d_kuricolln', taborder=40)
        self.add('commandbutton', 'cb_ad', 18, 1516, 206, 76, text='&Add', taborder=70)
        self.add('commandbutton', 'cb_del', 229, 1516, 215, 76, text='&Delete', taborder=80)
        self.add('singlelineedit', 'sle_nerration', 494, 1620, 2011, 112, taborder=90)
        self.add('roundrectangle', 'rr_1', 2843, 1620, 649, 144)
        self.add('checkbox', 'cbx_fr', 14, 1632, 174, 80, text='Fr')
        self.add('statictext', 'st_3', 210, 1636, 293, 76, text='Nerration :')
        self.add('commandbutton', 'cb_save', 2889, 1644, 279, 92, text='&Save', taborder=50)
        self.add('commandbutton', 'cb_exit', 3177, 1644, 279, 92, text='E&xit', taborder=60)
        self.add('checkbox', 'cbx_sendsms', 2117, 1760, 402, 80, text='Send Sms')
