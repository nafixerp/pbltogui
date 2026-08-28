"""Receipt — w_rcpt.

Generated from the PowerBuilder window ``w_rcpt.srw`` by
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
    name='w_rcpt',
    title='Receipt',
    width=3479,
    height=2000,
    controls=[],
    tables=['daybook', 'accountm', 'daybookratewgt', 'pdclist', 'kuricolln', 'clients', 'stkandprofit', 'advafter', 'sman', 'stkandprof', 'generali', 'daybookpart', 'userd', 'generals', 'delpart'],
    source_path='w_rcpt.srw',
    report={'dataobject': 'd_rcptpmntprint_thermal', 'sql': "SELECT daybookpart.vchno AS daybookpart_vchno, daybook.tdate AS daybook_tdate, accountm.name AS accountm_name, daybookpart.particular AS daybookpart_particular, daybook.amount AS daybook_amount, daybook.control AS daybook_control, accountm.actype2 AS accountm_actype2, accountm.opbal AS accountm_opbal, accountm.opbalb AS accountm_opbalb, daybookpart.rate AS daybookpart_rate, daybookpart.taxperc AS daybookpart_taxperc, daybookpart.taxamt AS daybookpart_taxamt, daybookpart.interstate AS daybookpart_interstate, (select sum(db.amount) from daybook db where db.accode = daybook.accode and db.tdate <= daybook.tdate and db.control <= daybook.control and db.slno <> :rslno) as obtran, (select sum(db.amount) from daybook db where db.accode = daybook.accode and db.control <= daybook.control and db.slno = :rslno + 1 and db.opaccode = 'DISC') as discamt, (select kuricolln.wgt from kuricolln where kuricolln.slno = daybook.slno) as kuriwgt, (select kuricolln.grate from kuricolln where kuricolln.slno = daybook.slno) as kurigrate, (select advafter.ordno from advafter where advafter.slno = daybook.slno) as ordno, (select kuricolln.note from kuricolln where kuricolln.slno = daybook.slno) as kurinote, (select kuricolln.rcptno from kuricolln where kuricolln.slno = daybook.slno) as kurircptno, (select max(db.amount) from daybook db where db.slno = daybook.slno) as maxamt FROM daybook, daybookpart, accountm WHERE daybook.slno = daybookpart.slno AND daybook.accode = accountm.accode", 'args': ['rslno'], 'arg_types': {'rslno': 'number'}, 'tables': ['daybook', 'daybookpart', 'accountm'], 'columns': [{'name': 'daybookpart_vchno', 'label': 'daybookpart_vchno', 'type': 'char'}, {'name': 'daybook_tdate', 'label': 'daybook_tdate', 'type': 'date'}, {'name': 'accountm_name', 'label': 'accountm_name', 'type': 'char'}, {'name': 'daybookpart_particular', 'label': 'daybookpart_particular', 'type': 'char'}, {'name': 'daybook_amount', 'label': 'daybook_amount', 'type': 'decimal'}, {'name': 'daybook_control', 'label': 'daybook_control', 'type': 'long'}, {'name': 'accountm_actype2', 'label': 'accountm_actype2', 'type': 'char'}, {'name': 'obtran', 'label': 'obtran', 'type': 'decimal'}, {'name': 'accountm_opbal', 'label': 'accountm_opbal', 'type': 'decimal'}, {'name': 'accountm_opbalb', 'label': 'accountm_opbalb', 'type': 'decimal'}, {'name': 'discamt', 'label': 'discamt', 'type': 'decimal'}, {'name': 'kuriwgt', 'label': 'kuriwgt', 'type': 'decimal'}, {'name': 'kurigrate', 'label': 'kurigrate', 'type': 'decimal'}, {'name': 'ordno', 'label': 'ordno', 'type': 'char'}, {'name': 'daybookpart_rate', 'label': 'daybookpart_rate', 'type': 'decimal'}, {'name': 'kurinote', 'label': 'kurinote', 'type': 'char'}, {'name': 'kurircptno', 'label': 'kurircptno', 'type': 'char'}, {'name': 'maxamt', 'label': 'maxamt', 'type': 'decimal'}, {'name': 'daybookpart_taxperc', 'label': 'daybookpart_taxperc', 'type': 'decimal'}, {'name': 'daybookpart_taxamt', 'label': 'daybookpart_taxamt', 'type': 'decimal'}, {'name': 'daybookpart_interstate', 'label': 'daybookpart_interstate', 'type': 'char'}]},
    opens=['w_cbachdhelp', 'w_rcptpmnt_view'],
)


class ReceiptForm(GeneratedForm):
    """Receipt"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('line', 'ln_1', 0, 0, 0, 0)
        self.add('statictext', 'st_vchno', 681, 92, 411, 88)
        self.add('commandbutton', 'cb_prev', 1166, 92, 197, 92, text='<', taborder=10)
        self.add('commandbutton', 'cb_next', 1362, 92, 197, 92, text='>', taborder=10)
        self.add('checkbox', 'cbx_kuri', 1682, 96, 457, 80, text='Kuri/Scheme')
        self.add('statictext', 'st_vchnot', 238, 104, 425, 72, text='Voucher No. :')
        self.add('editmask', 'em_date', 681, 200, 407, 88, taborder=10)
        self.add('statictext', 'st_8', 389, 204, 274, 72, text='Date :')
        self.add('checkbox', 'cbx_updtfr', 2345, 300, 165, 80, text='&Fr')
        self.add('checkbox', 'cbx_updtsys', 2578, 300, 197, 80, text='Sys')
        self.add('datawindow', 'dw_cashbank', 681, 308, 882, 88, dataobject='d_cashbankcode', taborder=20)
        self.add('statictext', 'st_1', 128, 320, 535, 72, text='Cash/Bank Code :')
        self.add('statictext', 'st_9', 1792, 344, 416, 76, text='Select a/c type')
        self.add('datawindow', 'dw_staff', 681, 420, 677, 88, dataobject='d_smancode', taborder=30)
        self.add('dropdownlistbox', 'ddlb_type', 1664, 424, 585, 772, text='All', items=['All', 'Customers', 'Suppliers', 'Jewelleries', 'Goldsmiths', 'Refiners', 'Staffs', 'General A/c'])
        self.add('statictext', 'st_staff', 293, 428, 370, 76, text='SMan :')
        self.add('singlelineedit', 'sle_part', 681, 532, 1563, 88, limit=70, taborder=40)
        self.add('statictext', 'st_3', 215, 540, 448, 72, text='Description :')
        self.add('rectangle', 'r_1', 210, 652, 2523, 400)
        self.add('statictext', 'st_5', 759, 700, 882, 72, text='Description')
        self.add('statictext', 'st_4', 242, 704, 425, 72, text='A/C Code')
        self.add('statictext', 'st_6', 2309, 704, 379, 72, text='Amount')
        self.add('statictext', 'st_7', 1755, 708, 389, 72, text='Balance')
        self.add('editmask', 'em_balance', 1760, 848, 398, 96)
        self.add('editmask', 'em_amount', 2304, 848, 393, 96, taborder=60)
        self.add('datawindow', 'dw_accode', 233, 852, 430, 88, dataobject='d_accode', taborder=50)
        self.add('statictext', 'st_desc', 754, 856, 837, 88)
        self.add('statictext', 'st_10', 1632, 856, 123, 84, text='OB :')
        self.add('commandbutton', 'cb_achelp', 686, 860, 64, 84, text='^')
        self.add('editmask', 'em_wgtbal', 1760, 948, 398, 96, taborder=70)
        self.add('editmask', 'em_cb', 2304, 952, 393, 88)
        self.add('statictext', 'st_dbcr', 1769, 956, 393, 76)
        self.add('statictext', 'st_11', 2171, 956, 123, 80, text='CB :')
        self.add('statictext', 'st_wgtbal', 1477, 960, 279, 84, text='Wgt Bal :')
        self.add('statictext', 'st_amt', 206, 1056, 2528, 76)
        self.add('editmask', 'em_chqdate', 681, 1148, 407, 88, taborder=80)
        self.add('singlelineedit', 'sle_chqno', 1467, 1148, 517, 88, limit=15, taborder=90)
        self.add('editmask', 'em_discount', 2304, 1148, 393, 88, taborder=100)
        self.add('statictext', 'st_chqdate', 210, 1152, 425, 80, text='Cheque Date')
        self.add('statictext', 'st_chqno', 1129, 1156, 338, 80, text='Cheque No')
        self.add('statictext', 'st_discount', 1998, 1156, 297, 76, text='Discount :')
        self.add('editmask', 'em_rate', 681, 1240, 407, 88, taborder=110)
        self.add('statictext', 'st_mcp', 1129, 1240, 233, 80, text='MC %')
        self.add('editmask', 'em_mcp', 1467, 1240, 238, 88, taborder=120)
        self.add('editmask', 'em_duedate', 2304, 1240, 393, 88, taborder=150)
        self.add('checkbox', 'cbx_pdc', 1769, 1244, 210, 80, text='PDC')
        self.add('statictext', 'st_duedate', 1998, 1248, 297, 76, text='Duedate :')
        self.add('statictext', 'st_rate', 210, 1252, 425, 80, text='Rate')
        self.add('editmask', 'em_taxperc', 681, 1336, 238, 88, taborder=140)
        self.add('editmask', 'em_taxamt', 1467, 1336, 407, 88, taborder=130)
        self.add('checkbox', 'cbx_showwgt', 2309, 1348, 690, 84, text='Show Wgt in Ledger')
        self.add('statictext', 'st_2', 210, 1352, 425, 80, text='Tax %')
        self.add('statictext', 'st_12', 1129, 1352, 306, 80, text='Tax Amt')
        self.add('checkbox', 'cbx_printslip', 2309, 1436, 416, 84, text='Pri&nt Slip')
        self.add('checkbox', 'cbx_interstate', 1472, 1440, 402, 80, text='Interstate')
        self.add('checkbox', 'cbx_taxreverse', 681, 1448, 613, 80, text='Tax Reverse Charge')
        self.add('datawindow', 'dw_print', 155, 1524, 206, 176, dataobject='d_rcptpmntprint_thermal')
        self.add('checkbox', 'cbx_printobcb', 2309, 1528, 466, 84, text='Print OB/CB')
        self.add('oval', 'oval_1', 905, 1560, 1015, 260)
        self.add('checkbox', 'cbx_sendsms', 2309, 1612, 402, 80, text='Send Sms')
        self.add('commandbutton', 'cb_ok', 1065, 1636, 238, 100, text='&Save', taborder=160)
        self.add('commandbutton', 'cb_cancel', 1312, 1636, 238, 100, text='&Cancel', taborder=170)
        self.add('commandbutton', 'cb_exit', 1559, 1636, 238, 100, text='&Exit', taborder=180)
