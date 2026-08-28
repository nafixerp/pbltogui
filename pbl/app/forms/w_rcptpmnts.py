"""Rcpt/Pmnt Report — w_rcptpmnts.

Generated from the PowerBuilder window ``w_rcptpmnts.srw`` by
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
    name='w_rcptpmnts',
    title='Rcpt/Pmnt Report',
    width=3662,
    height=2312,
    controls=[],
    tables=['daybook', 'accountm', 'collection', 'salesm', 'salesrm', 'purchasem', 'purchaserm', 'orderm', 'refinerym', 'repairm', 'smithm', 'daybookpart', 'generali'],
    source_path='w_rcptpmnts.srw',
    report={'dataobject': 'd_rcptpmnts', 'sql': 'SELECT daybook.tdate AS daybook_tdate, daybook.amount AS daybook_amount, daybookpart.vchno AS daybookpart_vchno, daybookpart.particular AS daybookpart_particular, daybook.slno AS daybook_slno, daybookpart.staff AS daybookpart_staff, (select max(dbk.accode) from daybook dbk where dbk.accode <> daybook.accode and dbk.slno = daybook.slno) as othercode, (select accountm.name from accountm where accountm.accode = othercode) as othername, (select accountm.actype2 from accountm where accountm.accode = othercode) as otheractype, (select accountm.grcode from accountm where accountm.accode = othercode) as otheracgrp, (select accountm.actype1 from accountm where accountm.accode = othercode) as otheractype2, (0) as sel, (select count(clients_kuridet.code) from clients_kuridet where clients_kuridet.code = othercode) as ksparty FROM daybook, daybookpart WHERE daybook.slno = daybookpart.slno AND daybook.control <= :rlevel AND daybook.tdate between :rdate1 and :rdate2 AND daybook.accode = :rcode ORDER BY daybook.tdate ASC, daybook.slno ASC', 'computes': [{'name': 'part', 'expression': 'trim( daybookpart_particular )', 'format': '[general]', 'label': 'part', 'band': 'detail'}, {'name': 'rcpt', 'expression': 'if(daybook_amount < 0,string(abs(daybook_amount),~"######0.00~"), ~" ~")', 'format': '[general]', 'label': 'rcpt', 'band': 'detail'}, {'name': 'compute_4', 'expression': 'if(daybook_amount > 0,string(daybook_amount,~"######0.00~"),~" ~")', 'format': '[general]', 'label': 'compute_4', 'band': 'detail'}, {'name': 'compute_22', 'expression': 'sum(if(daybook_amount < 0,abs(daybook_amount),0) for all)', 'format': '########0.00', 'label': 'compute_22', 'band': 'summary'}, {'name': 'compute_5', 'expression': 'sum(if(daybook_amount > 0,daybook_amount,0) for all)', 'format': '########0.00', 'label': 'compute_5', 'band': 'summary'}, {'name': 'compute_20', 'expression': 'if(ropbal > 0,ropbal,0)', 'format': '#######0.00', 'label': 'compute_20', 'band': 'summary'}, {'name': 'compute_19', 'expression': 'if(ropbal < 0,abs(ropbal),0)', 'format': '#######0.00', 'label': 'compute_19', 'band': 'summary'}, {'name': 'compute_21', 'expression': 'if(rsaleamt > 0,rsaleamt,0)', 'format': '#######0.00', 'label': 'compute_21', 'band': 'summary'}, {'name': 'compute_6', 'expression': 'if( rsaleamt< 0,abs(rsaleamt),0)', 'format': '#######0.00', 'label': 'compute_6', 'band': 'summary'}, {'name': 'compute_7', 'expression': 'if(  rpurhamt < 0,abs(  rpurhamt ),0)', 'format': '#######0.00', 'label': 'compute_7', 'band': 'summary'}, {'name': 'compute_8', 'expression': 'if(  rpurhamt > 0,  rpurhamt ,0)', 'format': '#######0.00', 'label': 'compute_8', 'band': 'summary'}, {'name': 'compute_10', 'expression': 'if(   rsmith < 0,abs(   rsmith ),0)', 'format': '#######0.00', 'label': 'compute_10', 'band': 'summary'}, {'name': 'compute_9', 'expression': 'if(   rsmith > 0,   rsmith ,0)', 'format': '#######0.00', 'label': 'compute_9', 'band': 'summary'}, {'name': 'compute_11', 'expression': 'if(    rrefine < 0,abs(    rrefine ),0)', 'format': '#######0.00', 'label': 'compute_11', 'band': 'summary'}, {'name': 'compute_12', 'expression': 'if(    rrefine > 0,    rrefine ,0)', 'format': '#######0.00', 'label': 'compute_12', 'band': 'summary'}, {'name': 'compute_13', 'expression': 'if(     rrepair > 0,     rrepair ,0)', 'format': '#######0.00', 'label': 'compute_13', 'band': 'summary'}, {'name': 'compute_14', 'expression': 'if(     rrepair < 0,abs(     rrepair ),0)', 'format': '#######0.00', 'label': 'compute_14', 'band': 'summary'}, {'name': 'compute_16', 'expression': 'if( rorder  > 0,  rorder  ,0)', 'format': '#######0.00', 'label': 'compute_16', 'band': 'summary'}, {'name': 'compute_15', 'expression': 'if(  rorder  < 0,abs(  rorder ),0)', 'format': '#######0.00', 'label': 'compute_15', 'band': 'summary'}, {'name': 'compute_18', 'expression': 'if(  rclbal > 0,   rclbal ,0)', 'format': '#######0.00', 'label': 'compute_18', 'band': 'summary'}, {'name': 'compute_17', 'expression': 'if(   rclbal < 0,abs(   rclbal ),0)', 'format': '#######0.00', 'label': 'compute_17', 'band': 'summary'}], 'args': ['rdate1', 'rdate2', 'rlevel', 'rcode', 'ropbal', 'rsaleamt', 'rpurhamt', 'rorder', 'rrepair', 'rsmith', 'rrefine', 'rclbal'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date', 'rlevel': 'number', 'rcode': 'string', 'ropbal': 'decimal', 'rsaleamt': 'decimal', 'rpurhamt': 'decimal', 'rorder': 'decimal', 'rrepair': 'decimal', 'rsmith': 'decimal', 'rrefine': 'decimal', 'rclbal': 'decimal'}, 'tables': ['daybook', 'daybookpart'], 'columns': [{'name': 'daybook_tdate', 'label': 'daybook_tdate', 'type': 'date'}, {'name': 'daybook_amount', 'label': 'daybook_amount', 'type': 'decimal'}, {'name': 'daybookpart_vchno', 'label': 'daybookpart_vchno', 'type': 'char'}, {'name': 'daybookpart_particular', 'label': 'daybookpart_particular', 'type': 'char'}, {'name': 'daybook_slno', 'label': 'daybook_slno', 'type': 'decimal'}, {'name': 'cothercode', 'label': 'cothercode', 'type': 'char'}, {'name': 'cothername', 'label': 'cothername', 'type': 'char'}, {'name': 'daybookpart_staff', 'label': 'daybookpart_staff', 'type': 'char'}, {'name': 'otheractype', 'label': 'otheractype', 'type': 'char'}, {'name': 'otheracgrp', 'label': 'otheracgrp', 'type': 'char'}, {'name': 'otheractype2', 'label': 'otheractype2', 'type': 'char'}, {'name': 'sel', 'label': 'sel', 'type': 'long'}, {'name': 'ksparty', 'label': 'ksparty', 'type': 'long'}]},
)


class RcptPmntReportForm(GeneratedForm):
    """Rcpt/Pmnt Report"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 247, 0, 430, 100, taborder=10)
        self.add('editmask', 'em_date2', 951, 0, 425, 100, taborder=20)
        self.add('commandbutton', 'cb_show', 1554, 0, 279, 100, text='&Show', taborder=30)
        self.add('commandbutton', 'cb_sort', 2624, 0, 233, 100, text='So&rt', taborder=50)
        self.add('commandbutton', 'cb_3', 2866, 0, 247, 100, text='Save &As', taborder=90)
        self.add('commandbutton', 'cb_1', 3122, 0, 242, 100, text='&Print', taborder=120)
        self.add('commandbutton', 'cb_2', 3369, 0, 242, 100, text='E&xit', taborder=70)
        self.add('checkbox', 'cbx_sort', 1970, 8, 571, 76, text='Sort On A/c Name')
        self.add('statictext', 'st_1', 5, 16, 229, 64, text='From :')
        self.add('statictext', 'st_2', 727, 16, 215, 72, text='To :')
        self.add('datawindow', 'dw_grp', 247, 104, 1129, 96, dataobject='d_grcode', taborder=110)
        self.add('dropdownlistbox', 'ddlb_type', 1554, 104, 718, 936, text='All', items=['All', 'Customers', 'Suppliers', 'Jewelleries', 'Goldsmiths', 'Refiners', 'Staff', 'General', 'Kuri/Scheme Customers'], taborder=80)
        self.add('dropdownlistbox', 'ddlb_actype', 2624, 104, 741, 740, text='All', items=['Expense Only', 'Revenue Only', 'Asset Only', 'Liability Only', 'All'], taborder=100)
        self.add('checkbox', 'cbx_grp', 1385, 112, 73, 80)
        self.add('statictext', 'st_3', 0, 116, 233, 64, text='Group :')
        self.add('statictext', 'st_4', 2405, 120, 210, 64, text='Actype:')
        self.add('datawindow', 'dw_acsummary', 0, 204, 3616, 1936, dataobject='d_rcptpmnts', taborder=40)
        self.add('commandbutton', 'cb_selall', 1554, 216, 402, 88, text='Select All', taborder=60)
        self.add('commandbutton', 'cb_delete', 1961, 216, 283, 88, text='Delete')
        self.add('commandbutton', 'cb_rearrange', 2249, 216, 283, 88, text='Rearrange')
        self.add('checkbox', 'cbx_summary', 2811, 216, 503, 76, text='Show Summary')
        self.add('checkbox', 'cbx_selonly', 2811, 300, 457, 80, text='Selected Only')
