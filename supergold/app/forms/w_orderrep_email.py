"""Send Mail To HO — w_orderrep_email.

Generated from the PowerBuilder window ``w_orderrep_email.srw`` by
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
    name='w_orderrep_email',
    title='Send Mail To HO',
    width=3689,
    height=2300,
    controls=[],
    tables=['clients'],
    source_path='w_orderrep_email.srw',
    grid={'control': 'dw_smith', 'dataobject': 'd_smith', 'table': 'codehelp', 'keys': ['code'], 'columns': [{'name': 'code', 'label': 'code', 'type': 'char'}]},
    report={'dataobject': 'd_orderrep_email', 'sql': 'SELECT orderm.slno AS orderm_slno, orderm.ordno AS orderm_ordno, orderm.tdate AS orderm_tdate, orderm.custcode AS orderm_custcode, orderm.custname AS orderm_custname, orderm.duedate AS orderm_duedate, orderm.rate AS orderm_rate, orderm.billamt AS orderm_billamt, orderm.eamt AS orderm_eamt, orderm.advance AS orderm_advance, orderm.status AS orderm_status, orderm.control AS orderm_control, orderm.salebill AS orderm_salebill, orderm.smcode AS orderm_smcode, orderm.gadvance AS orderm_gadvance, orderm.sretamt AS orderm_sretamt, orderm.ichadv AS orderm_ichadv, orderm.iexadv AS orderm_iexadv, orderm.isradv AS orderm_isradv, orderm.ob AS orderm_ob, orderm.addr AS orderm_addr, orderm.refund AS orderm_refund, orderm.closed AS orderm_closed, orderd.code AS orderd_code, orderd.rate AS orderd_rate, orderd.qty AS orderd_qty, orderd.weight AS orderd_weight, orderd.wastage AS orderd_wastage, orderd.mcharge AS orderd_mcharge, orderd.stonewgt AS orderd_stonewgt, orderd.stoneprice AS orderd_stoneprice, orderd.amount AS orderd_amount, orderd.cost AS orderd_cost, orderd.sno AS orderd_sno, orderd.iqtype AS orderd_iqtype, orderd.smith AS orderd_smith, orderm.jewlcode AS orderm_jewlcode, orderd.part AS orderd_part, orderd.stage AS orderd_stage, (select items.name from items where items.code = orderd.code) as itemname FROM orderd, orderm WHERE orderd.slno = orderm.slno ORDER BY orderm.tdate ASC, orderm.ordno ASC, orderd.sno ASC', 'args': ['rdate1', 'rdate2', 'rlevel', 'rBranch'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date', 'rlevel': 'number', 'rBranch': 'string'}, 'tables': ['orderd', 'orderm'], 'columns': [{'name': 'orderm_slno', 'label': 'orderm_slno', 'type': 'decimal'}, {'name': 'orderm_ordno', 'label': 'orderm_ordno', 'type': 'char'}, {'name': 'orderm_tdate', 'label': 'Date', 'type': 'date'}, {'name': 'orderm_custcode', 'label': 'orderm_custcode', 'type': 'char'}, {'name': 'orderm_custname', 'label': 'Party', 'type': 'char'}, {'name': 'orderm_duedate', 'label': 'orderm_duedate', 'type': 'date'}, {'name': 'orderm_rate', 'label': 'orderm_rate', 'type': 'decimal'}, {'name': 'orderm_billamt', 'label': 'orderm_billamt', 'type': 'decimal'}, {'name': 'orderm_eamt', 'label': 'orderm_eamt', 'type': 'decimal'}, {'name': 'orderm_advance', 'label': 'orderm_advance', 'type': 'decimal'}, {'name': 'orderm_status', 'label': 'orderm_status', 'type': 'long'}, {'name': 'orderm_control', 'label': 'orderm_control', 'type': 'long'}, {'name': 'orderm_salebill', 'label': 'orderm_salebill', 'type': 'char'}, {'name': 'orderm_smcode', 'label': 'orderm_smcode', 'type': 'char'}, {'name': 'orderm_gadvance', 'label': 'orderm_gadvance', 'type': 'decimal'}, {'name': 'orderm_sretamt', 'label': 'orderm_sretamt', 'type': 'decimal'}, {'name': 'orderm_ichadv', 'label': 'orderm_ichadv', 'type': 'long'}, {'name': 'orderm_iexadv', 'label': 'orderm_iexadv', 'type': 'long'}, {'name': 'orderm_isradv', 'label': 'orderm_isradv', 'type': 'long'}, {'name': 'orderm_ob', 'label': 'orderm_ob', 'type': 'decimal'}, {'name': 'orderm_addr', 'label': 'orderm_addr', 'type': 'char'}, {'name': 'orderm_refund', 'label': 'orderm_refund', 'type': 'decimal'}, {'name': 'orderm_closed', 'label': 'orderm_closed', 'type': 'long'}, {'name': 'orderd_code', 'label': 'orderd_code', 'type': 'char'}, {'name': 'orderd_rate', 'label': 'orderd_rate', 'type': 'decimal'}, {'name': 'orderd_qty', 'label': 'orderd_qty', 'type': 'long'}, {'name': 'orderd_weight', 'label': 'orderd_weight', 'type': 'decimal'}, {'name': 'orderd_wastage', 'label': 'orderd_wastage', 'type': 'decimal'}, {'name': 'orderd_mcharge', 'label': 'orderd_mcharge', 'type': 'decimal'}, {'name': 'orderd_stonewgt', 'label': 'orderd_stonewgt', 'type': 'decimal'}, {'name': 'orderd_stoneprice', 'label': 'orderd_stoneprice', 'type': 'decimal'}, {'name': 'orderd_amount', 'label': 'orderd_amount', 'type': 'decimal'}, {'name': 'orderd_cost', 'label': 'orderd_cost', 'type': 'decimal'}, {'name': 'orderd_sno', 'label': 'orderd_sno', 'type': 'long'}, {'name': 'orderd_iqtype', 'label': 'orderd_iqtype', 'type': 'char'}, {'name': 'orderd_smith', 'label': 'orderd_smith', 'type': 'char'}, {'name': 'citemname', 'label': 'citemname', 'type': 'char'}, {'name': 'orderm_jewlcode', 'label': 'orderm_jewlcode', 'type': 'char'}, {'name': 'orderd_part', 'label': 'orderd_part', 'type': 'char'}, {'name': 'orderd_stage', 'label': 'orderd_stage', 'type': 'long'}]},
    opens=['w_clientshelp'],
)


class SendMailToHoForm(GeneratedForm):
    """Send Mail To HO"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('dropdownlistbox', 'ddlb_type', 1317, 0, 585, 384, text='Pending Only', items=['All', 'Pending Only', 'Returned Only'], taborder=100)
        self.add('commandbutton', 'cb_show', 2107, 0, 261, 96, text='&Show', taborder=70)
        self.add('commandbutton', 'cb_sendmail', 2427, 0, 352, 96, text='Send Mail', taborder=90)
        self.add('commandbutton', 'cb_3', 2830, 0, 261, 92, text='Save &As', taborder=120)
        self.add('commandbutton', 'cb_1', 3095, 0, 265, 92, text='&Print', taborder=130)
        self.add('commandbutton', 'cb_2', 3360, 0, 265, 92, text='E&xit', taborder=110)
        self.add('editmask', 'em_date1', 233, 4, 448, 92, taborder=10)
        self.add('editmask', 'em_date2', 841, 4, 448, 92, taborder=20)
        self.add('statictext', 'st_1', 18, 12, 206, 76, text='From :')
        self.add('statictext', 'st_2', 699, 16, 133, 76, text='To :')
        self.add('dropdownlistbox', 'ddlb_stagepref', 1312, 96, 315, 288, text='Only', items=['Only', 'Not'], taborder=50)
        self.add('dropdownlistbox', 'ddlb_stage', 1637, 96, 549, 440, text='All', items=['All', 'New Work', 'Work In Progress', 'Finished'], taborder=42)
        self.add('singlelineedit', 'sle_email', 233, 100, 1061, 84, taborder=60)
        self.add('datawindow', 'dw_smith', 2491, 100, 443, 84, dataobject='d_smith', taborder=30)
        self.add('datawindow', 'dw_jewl', 3191, 100, 425, 84, dataobject='d_jewl', taborder=40)
        self.add('statictext', 'st_4', 0, 104, 224, 76, text='e-mail :')
        self.add('statictext', 'st_10', 2258, 104, 219, 76, text='Smith :')
        self.add('statictext', 'st_5', 2990, 112, 192, 76, text='Jewl :')
        self.add('datawindow', 'dw_1', 0, 188, 3621, 1992, dataobject='d_orderrep_email', taborder=80)
