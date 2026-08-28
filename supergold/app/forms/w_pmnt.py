"""Payment — w_pmnt.

Generated from the PowerBuilder window ``w_pmnt.srw`` by
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
    name='w_pmnt',
    title='Payment',
    width=2935,
    height=1892,
    controls=[],
    tables=['daybook', 'accountm', 'pdclist', 'stkandprofit', 'clients', 'sman', 'generali', 'daybookpart', 'userd', 'generals', 'delpart'],
    source_path='w_pmnt.srw',
    report={'dataobject': 'd_rcptpmntprint_thermal', 'sql': "SELECT daybookpart.vchno AS daybookpart_vchno, daybook.tdate AS daybook_tdate, accountm.name AS accountm_name, daybookpart.particular AS daybookpart_particular, daybook.amount AS daybook_amount, daybook.control AS daybook_control, accountm.actype2 AS accountm_actype2, accountm.opbal AS accountm_opbal, accountm.opbalb AS accountm_opbalb, daybookpart.rate AS daybookpart_rate, daybookpart.taxperc AS daybookpart_taxperc, daybookpart.taxamt AS daybookpart_taxamt, daybookpart.interstate AS daybookpart_interstate, (select sum(db.amount) from daybook db where db.accode = daybook.accode and db.tdate <= daybook.tdate and db.control <= daybook.control and db.slno <> :rslno) as obtran, (select sum(db.amount) from daybook db where db.accode = daybook.accode and db.control <= daybook.control and db.slno = :rslno + 1 and db.opaccode = 'DISC') as discamt, (select kuricolln.wgt from kuricolln where kuricolln.slno = daybook.slno) as kuriwgt, (select kuricolln.grate from kuricolln where kuricolln.slno = daybook.slno) as kurigrate, (select advafter.ordno from advafter where advafter.slno = daybook.slno) as ordno, (select kuricolln.note from kuricolln where kuricolln.slno = daybook.slno) as kurinote, (select kuricolln.rcptno from kuricolln where kuricolln.slno = daybook.slno) as kurircptno, (select max(db.amount) from daybook db where db.slno = daybook.slno) as maxamt FROM daybook, daybookpart, accountm WHERE daybook.slno = daybookpart.slno AND daybook.accode = accountm.accode", 'args': ['rslno'], 'arg_types': {'rslno': 'number'}, 'tables': ['daybook', 'daybookpart', 'accountm'], 'columns': [{'name': 'daybookpart_vchno', 'label': 'daybookpart_vchno', 'type': 'char'}, {'name': 'daybook_tdate', 'label': 'daybook_tdate', 'type': 'date'}, {'name': 'accountm_name', 'label': 'accountm_name', 'type': 'char'}, {'name': 'daybookpart_particular', 'label': 'daybookpart_particular', 'type': 'char'}, {'name': 'daybook_amount', 'label': 'daybook_amount', 'type': 'decimal'}, {'name': 'daybook_control', 'label': 'daybook_control', 'type': 'long'}, {'name': 'accountm_actype2', 'label': 'accountm_actype2', 'type': 'char'}, {'name': 'obtran', 'label': 'obtran', 'type': 'decimal'}, {'name': 'accountm_opbal', 'label': 'accountm_opbal', 'type': 'decimal'}, {'name': 'accountm_opbalb', 'label': 'accountm_opbalb', 'type': 'decimal'}, {'name': 'discamt', 'label': 'discamt', 'type': 'decimal'}, {'name': 'kuriwgt', 'label': 'kuriwgt', 'type': 'decimal'}, {'name': 'kurigrate', 'label': 'kurigrate', 'type': 'decimal'}, {'name': 'ordno', 'label': 'ordno', 'type': 'char'}, {'name': 'daybookpart_rate', 'label': 'daybookpart_rate', 'type': 'decimal'}, {'name': 'kurinote', 'label': 'kurinote', 'type': 'char'}, {'name': 'kurircptno', 'label': 'kurircptno', 'type': 'char'}, {'name': 'maxamt', 'label': 'maxamt', 'type': 'decimal'}, {'name': 'daybookpart_taxperc', 'label': 'daybookpart_taxperc', 'type': 'decimal'}, {'name': 'daybookpart_taxamt', 'label': 'daybookpart_taxamt', 'type': 'decimal'}, {'name': 'daybookpart_interstate', 'label': 'daybookpart_interstate', 'type': 'char'}]},
    opens=['w_cbachdhelp', 'w_smith', 'w_sucu', 'w_achd', 'w_rcptpmnt_view'],
    prints=['d_rcptpmntprint_thermal'],
)


class PaymentForm(GeneratedForm):
    """Payment"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('line', 'ln_1', 0, 0, 0, 0)
        self.add('statictext', 'st_9', 1742, 64, 416, 76, text='Select a/c type')
        self.add('commandbutton', 'cb_prev', 1152, 76, 197, 92, text='<', taborder=10)
        self.add('commandbutton', 'cb_next', 1349, 76, 197, 92, text='>', taborder=20)
        self.add('statictext', 'st_vchno', 658, 80, 416, 88)
        self.add('statictext', 'st_vchnot', 219, 84, 425, 72, text='Voucher No. :')
        self.add('dropdownlistbox', 'ddlb_type', 1746, 152, 485, 488, text='All', items=['All', 'Customers', 'Suppliers', 'Jewelleries', 'Goldsmiths', 'Refiners', 'Staff', 'General A/c'])
        self.add('editmask', 'em_date', 658, 184, 416, 92, taborder=10)
        self.add('statictext', 'st_8', 370, 196, 274, 72, text='Date :')
        self.add('datawindow', 'dw_cashbank', 658, 288, 882, 88, dataobject='d_cashbankcode', taborder=20)
        self.add('editmask', 'em_cashbal', 1746, 288, 475, 88, taborder=70)
        self.add('checkbox', 'cbx_updtfr', 2313, 292, 165, 76, text='&Fr')
        self.add('statictext', 'st_1', 96, 300, 549, 72, text='Cash/Bank Code :')
        self.add('statictext', 'st_12', 1559, 300, 178, 64, text='Bal :')
        self.add('datawindow', 'dw_staff', 658, 388, 677, 88, dataobject='d_smancode', taborder=30)
        self.add('statictext', 'st_2', 398, 404, 247, 76, text='SMan :')
        self.add('checkbox', 'cbx_updtsys', 2313, 420, 247, 80, text='Sys')
        self.add('singlelineedit', 'sle_part', 658, 488, 1563, 88, limit=70, taborder=40)
        self.add('statictext', 'st_3', 197, 492, 448, 72, text='Description :')
        self.add('rectangle', 'r_1', 215, 600, 2523, 400)
        self.add('statictext', 'st_5', 773, 648, 882, 72, text='Description')
        self.add('statictext', 'st_4', 247, 652, 425, 72, text='A/C Code')
        self.add('statictext', 'st_6', 2327, 652, 379, 72, text='Amount')
        self.add('statictext', 'st_7', 1810, 656, 389, 72, text='Balance')
        self.add('editmask', 'em_amount', 2313, 792, 393, 96, taborder=60)
        self.add('editmask', 'em_balance', 1801, 796, 398, 96)
        self.add('datawindow', 'dw_accode', 242, 804, 430, 88, dataobject='d_accode', taborder=50)
        self.add('statictext', 'st_desc', 768, 804, 896, 88)
        self.add('commandbutton', 'cb_achelp', 686, 808, 64, 84, text='^')
        self.add('statictext', 'st_10', 1673, 812, 123, 80, text='OB :')
        self.add('editmask', 'em_cb', 2313, 900, 393, 84)
        self.add('statictext', 'st_dbcr', 1792, 908, 407, 76)
        self.add('statictext', 'st_11', 2190, 908, 123, 80, text='CB :')
        self.add('statictext', 'st_amt', 206, 1008, 2537, 80)
        self.add('editmask', 'em_chqdate', 640, 1100, 407, 88, taborder=80)
        self.add('singlelineedit', 'sle_chqno', 1440, 1100, 562, 88, limit=15, taborder=90)
        self.add('editmask', 'em_discount', 2341, 1100, 393, 88, taborder=100)
        self.add('statictext', 'st_chqno', 1111, 1104, 329, 84, text='Cheque No')
        self.add('statictext', 'st_discount', 2039, 1108, 297, 76, text='Discount :')
        self.add('statictext', 'st_chqdate', 215, 1112, 425, 80, text='Cheque Date :')
        self.add('editmask', 'em_rate', 640, 1192, 407, 88, taborder=110)
        self.add('editmask', 'em_duedate', 2341, 1192, 393, 88, taborder=120)
        self.add('checkbox', 'cbx_pdc', 1445, 1196, 251, 80, text='PDC')
        self.add('statictext', 'st_duedate', 2039, 1200, 297, 76, text='Duedate :')
        self.add('statictext', 'st_rate', 215, 1204, 425, 80, text='Rate')
        self.add('editmask', 'em_taxperc', 640, 1292, 238, 88, taborder=130)
        self.add('editmask', 'em_taxamt', 1440, 1292, 407, 88, taborder=130)
        self.add('statictext', 'st_14', 215, 1308, 425, 80, text='Tax %')
        self.add('statictext', 'st_13', 1111, 1308, 306, 80, text='Tax Amt')
        self.add('checkbox', 'cbx_printslip', 2313, 1316, 393, 76, text='&Print Slip')
        self.add('checkbox', 'cbx_printslip2', 2313, 1388, 485, 76, text='Print Ruff Slip')
        self.add('checkbox', 'cbx_taxreverse', 640, 1396, 613, 80, text='Tax Reverse Charge')
        self.add('checkbox', 'cbx_interstate', 1440, 1396, 402, 80, text='Interstate')
        self.add('checkbox', 'cbx_printobcb', 2313, 1460, 466, 76, text='Print OB/CB')
        self.add('datawindow', 'dw_print', 233, 1464, 206, 176, dataobject='d_rcptpmntprint_thermal', taborder=140)
        self.add('oval', 'oval_1', 1001, 1516, 1125, 224)
        self.add('commandbutton', 'cb_ok', 1202, 1584, 229, 92, text='&Save', taborder=130)
        self.add('commandbutton', 'cb_cancel', 1445, 1584, 229, 92, text='&Cancel', taborder=140)
        self.add('commandbutton', 'cb_exit', 1687, 1584, 229, 92, text='&Exit', taborder=150)
