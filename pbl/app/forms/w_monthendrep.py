"""Month End Report — w_monthendrep.

Generated from the PowerBuilder window ``w_monthendrep.srw`` by
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
    name='w_monthendrep',
    title='Month End Report',
    width=3506,
    height=2100,
    controls=[],
    tables=['smithd', 'items', 'repaird', 'refineryd', 'itemadj', 'purchased', 'salesrd', 'orderdga', 'salesd', 'clientsgs'],
    source_path='w_monthendrep.srw',
    report={'dataobject': 'd_monthendrep', 'sql': "SELECT onerec.field AS onerec_field, (select opbal from accountm where trim(accode) = 'DECORAT') decopa, (select opbalb from  accountm  where trim(accode) = 'DECORAT') decopb, (select sum(opbal) from  accountm  where left(accode,4) = 'PCAP') capopa, (select sum(opbalb) from  accountm  where left(accode,4) = 'PCAP') capopb, (select sum(orderdga.weight) from orderdga,orderm where orderdga.slno = orderm.slno and orderm.status = 1 and orderm.tdate <= :rdate and orderm.control <= :rlevel) partyadv, (select sum(opbal) from accountm where accountm.actype2 = 'C' and accountm.opbal < 0) acrcvbopbala, (select sum(opbalb) from accountm where accountm.actype2 = 'C' and  accountm.opbalb < 0) acrcvbopbalb, (select sum(opbal) from accountm where  accountm.actype2 = 'S' and  accountm.opbal > 0) acpaybopbala, (select sum(opbalb) from accountm where  accountm.actype2  = 'S' and  accountm.opbalb > 0) acpaybopbalb, (select sum(opbal) from  accountm  where  accountm.actype2  = 'H') cashopbala, (select sum(opbalb) from  accountm  where  accountm.actype2  = 'H') cashopbalb, (select sum(amount) from daybook where accode = 'ADVANCE' and daybook.tdate <= :rdate and control <= :rlevel) advbal, (select sum(amount) from daybook where left(accode,4) = 'PCAP' and tdate <= :rdate and control <= :rlevel) capbal, (select sum(amount) from daybook where trim(accode) = 'DECORAT' and tdate <= :rdate and control <= :rlevel) decbal, (select sum(daybook.amount) from daybook,accountm  where daybook.accode =  accountm.accode and accountm.actype2  = 'H' and daybook.tdate <= :rdate and  daybook.control <= :rlevel) cashbalance, (select sum(daybook.amount) from daybook,accountm where daybook.accode = accountm.accode and accountm.actype2 = 'S' and daybook.tdate <= :rdate and daybook.control <= :rlevel ) acpaybbalance, (select sum(daybook.amount) from daybook,accountm where daybook.accode = accountm.accode and accountm.actype2 = 'C' and daybook.control <= :rlevel and daybook.tdate <= :rdate and daybook.slno not in (select orderm.slno from orderm where orderm.slno = daybook.slno) ) acrcvbbalance FROM onerec", 'computes': [{'name': 'c_capital', 'expression': '(if(rlevel = 1,if(isnull(capopa),0,capopa),if(isnull(capopb),0,capopb))) + if(isnull(capbal),0,capbal)', 'format': '[general]', 'label': 'c_capital', 'band': 'detail'}, {'name': '', 'expression': 'abs(c_capital)', 'format': '########0.00', 'label': '', 'band': 'detail'}, {'name': 'c_decorate', 'expression': 'if(rlevel = 1,if(isnull(decopa),0,decopa),if(isnull(decopb),0,decopb)) + if(isnull(decbal),0,decbal)', 'format': '[general]', 'label': 'c_decorate', 'band': 'detail'}, {'name': '', 'expression': 'abs(c_decorate )', 'format': '########0.00', 'label': '', 'band': 'detail'}, {'name': '', 'expression': 'abs( c_advance  ) ', 'format': '########0.00', 'label': '', 'band': 'detail'}, {'name': 'c_advance', 'expression': 'if(isnull( advbal ),0,advbal)', 'format': '[general]', 'label': 'c_advance', 'band': 'detail'}, {'name': '', 'expression': 'abs( c_acreceivable )', 'format': '########0.00', 'label': '', 'band': 'detail'}, {'name': 'c_acreceivable', 'expression': 'if(rlevel = 1,  if(isnull(acrcvbopbala),0,acrcvbopbala)  , if(isnull( acrcvbopbalb),0,acrcvbopbalb) ) +   if(isnull(acrcvbbalance),0,acrcvbbalance ) ', 'format': '[general]', 'label': 'c_acreceivable', 'band': 'detail'}, {'name': '', 'expression': 'abs( c_cashbalance )', 'format': '########0.00', 'label': '', 'band': 'detail'}, {'name': 'c_cashbalance', 'expression': 'if(rlevel = 1, if(isnull(cashopbala),0,cashopbala), if(isnull(cashopbalb),0,cashopbalb)) + if(isnull(cashbalance),0,cashbalance)', 'format': '[general]', 'label': 'c_cashbalance', 'band': 'detail'}, {'name': 'c_gstock', 'expression': 'rgoldstock', 'format': '#######0.000', 'label': 'c_gstock', 'band': 'detail'}, {'name': '', 'expression': ' rsmithrcvb ', 'format': '#####0.000', 'label': '', 'band': 'detail'}, {'name': '', 'expression': ' rsmithpayb ', 'format': '#####0.000', 'label': '', 'band': 'detail'}, {'name': '', 'expression': 'partyadv', 'format': '#####0.000', 'label': '', 'band': 'detail'}, {'name': '', 'expression': 'rsilverstock', 'format': '#######0.000', 'label': '', 'band': 'detail'}], 'args': ['rdate', 'rlevel', 'rmonth', 'rsmithrcvb', 'rsmithpayb', 'rcost', 'rgoldstock', 'rsilverstock'], 'arg_types': {'rdate': 'date', 'rlevel': 'number', 'rmonth': 'string', 'rsmithrcvb': 'number', 'rsmithpayb': 'number', 'rcost': 'number', 'rgoldstock': 'number', 'rsilverstock': 'number'}, 'tables': ['onerec'], 'columns': [{'name': 'field', 'label': 'field', 'type': 'char'}, {'name': 'decopa', 'label': 'decopa', 'type': 'decimal'}, {'name': 'decopb', 'label': 'decopb', 'type': 'decimal'}, {'name': 'capopa', 'label': 'capopa', 'type': 'decimal'}, {'name': 'capopb', 'label': 'capopb', 'type': 'decimal'}, {'name': 'partyadv', 'label': 'partyadv', 'type': 'decimal'}, {'name': 'acrcvbopbala', 'label': 'acrcvbopbala', 'type': 'decimal'}, {'name': 'acrcvbopbalb', 'label': 'acrcvbopbalb', 'type': 'decimal'}, {'name': 'acpaybopbala', 'label': 'acpaybopbala', 'type': 'decimal'}, {'name': 'acpaybopbalb', 'label': 'acpaybopbalb', 'type': 'decimal'}, {'name': 'cashopbala', 'label': 'cashopbala', 'type': 'decimal'}, {'name': 'cashopbalb', 'label': 'cashopbalb', 'type': 'decimal'}, {'name': 'advbal', 'label': 'advbal', 'type': 'decimal'}, {'name': 'capbal', 'label': 'capbal', 'type': 'decimal'}, {'name': 'decbal', 'label': 'decbal', 'type': 'decimal'}, {'name': 'cashbalance', 'label': 'cashbalance', 'type': 'decimal'}, {'name': 'acpaybbalance', 'label': 'acpaybbalance', 'type': 'decimal'}, {'name': 'acrcvbbalance', 'label': 'acrcvbbalance', 'type': 'decimal'}]},
    opens=['w_monthenddet'],
)


class MonthEndReportForm(GeneratedForm):
    """Month End Report"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('datawindow', 'dw_daysumm', 0, 0, 3506, 1980, dataobject='d_monthendrep', taborder=10)
        self.add('commandbutton', 'cb_detail', 1984, 24, 265, 88, text='&Detail', taborder=30)
        self.add('commandbutton', 'cb_print', 2263, 24, 265, 88, text='&Print', taborder=40)
        self.add('commandbutton', 'cb_exit', 2542, 24, 265, 88, text='E&xit', taborder=20)
        self.add('editmask', 'em_date', 2368, 128, 352, 88, taborder=31)
        self.add('statictext', 'st_1', 2176, 144, 192, 76, text='Date :')
