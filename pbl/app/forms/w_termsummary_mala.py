"""Term Summary Malayalam — w_termsummary_mala.

Generated from the PowerBuilder window ``w_termsummary_mala.srw`` by
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
    name='w_termsummary_mala',
    title='Term Summary Malayalam',
    width=3685,
    height=2360,
    controls=[],
    tables=['accountm', 'daybook'],
    source_path='w_termsummary_mala.srw',
    report={'dataobject': 'd_termsummary_mala', 'sql': "SELECT onerec.field AS onerec_field, (select sum(billamt) from salesm where control <= :rlevel and tdate >= :rdate and tdate <= :rdate2) as saleamt, (select sum(salesd.weight) from salesd,salesm,items where salesm.slno = salesd.slno and items.code = salesd.code and salesm.tdate >= :rdate and salesm.tdate <= :rdate2 and salesm.control <= :rlevel and items.itype = 'G') as cgsaleswgt, (select sum(salesd.weight) from salesd,salesm,items where salesm.slno = salesd.slno and items.code = salesd.code and salesm.tdate >= :rdate and salesm.tdate <= :rdate2 and salesm.control <= :rlevel and items.itype = 'S') as cssaleswgt, (select sum(purchased.weight) from purchased,purchasem where purchasem.slno = purchased.slno and purchased.code = 'OG' and purchasem.tdate >= :rdate and purchasem.tdate <= :rdate2 and purchasem.control <= :rlevel ) as cogpurchwgt, (select sum(salesd.amount) from salesd,salesm,items where salesm.slno = salesd.slno and items.code = salesd.code and salesm.tdate >= :rdate and salesm.tdate <= :rdate2 and salesm.control <= :rlevel and items.itype = 'S') as cssalesamt, (select sum(advance) from orderm where control <= :rlevel and tdate >= :rdate and tdate <= :rdate2) as cadvamt, (select sum(purchased.lesswgt) from purchased,purchasem where purchasem.slno = purchased.slno and purchased.code = 'OG' and purchasem.tdate >= :rdate and purchasem.tdate <= :rdate2 and purchasem.control <= :rlevel ) as coglesswgt, (select sum(ramt) from salesm where control <= :rlevel and tdate >= :rdate and tdate <= :rdate2 and ramt < 0) as crefundamt, (select sum(salesrd.weight) from salesrd,salesrm,items where salesrm.slno = salesrd.slno and items.code = salesrd.code and salesrm.tdate >= :rdate and salesrm.tdate <= :rdate2 and salesrm.control <= :rlevel and items.itype = 'G') as cgsaleswgtr, (select sum(salesrd.amount) from salesrd,salesrm,items where salesrm.slno = salesrd.slno and items.code = salesrd.code and salesrm.tdate >= :rdate and salesrm.tdate <= :rdate2 and salesrm.control <= :rlevel and items.itype = 'G') as cgsalesamtr, (select sum(purchased.amount) from purchased,purchasem,items where purchasem.slno = purchased.slno and items.code = purchased.code and purchasem.tdate >= :rdate and purchasem.tdate <= :rdate2 and purchasem.control <= :rlevel and items.itype = 'S') as cspurchamt, (select sum(purchased.weight) from purchased,purchasem,items where purchasem.slno = purchased.slno and items.code = purchased.code and purchasem.tdate >= :rdate and purchasem.tdate <= :rdate2 and purchasem.control <= :rlevel and items.itype = 'S') as cspurchwgt, (select sum(salesm.eamt) from salesm,daybook where daybook.slno = salesm.slno and daybook.accode = 'EP' and salesm.control <= :rlevel and salesm.tdate >= :rdate and salesm.tdate <= :rdate2) as saleexamt, (select sum(purchased.amount) from purchased,purchasem where purchasem.slno = purchased.slno and purchased.code = 'OG' and purchasem.tdate >= :rdate and purchasem.tdate <= :rdate2 and purchasem.control <= :rlevel ) as cogpurchamt, (select sum(amount) from daybook,daybookpart,clients where daybookpart.slno = daybook.slno and clients.code = daybook.accode and daybook.control <= :rlevel and daybook.tdate  >=:rdate and daybook.tdate <= :rdate2 and left(daybookpart.vchno,2) = 'VR' and daybook.accode = 'CASH' and daybook.accode <> 'DISC' ) as ocustrcptamt, (select sum(staxamt) from salesm where control <= :rlevel and tdate >= :rdate and tdate <= :rdate2) as saletaxamt, (select sum(salesd.amount) from salesd,salesm,items where salesm.slno = salesd.slno and items.code = salesd.code and salesm.tdate >= :rdate and salesm.tdate <= :rdate2 and salesm.control <= :rlevel and items.itype = 'G') as cgsalesamt, (select sum(amount) from daybook,daybookpart where daybookpart.slno = daybook.slno and daybook.control <= :rlevel and daybook.tdate >= :rdate and daybook.tdate <= :rdate2 and left(daybookpart.vchno,2) = 'VP' and daybook.accode = 'CASH'  ) as opmntamt, (select sum(discount) from salesm where control <= :rlevel and tdate >= :rdate and tdate <= :rdate2) as salediscamt, (select sum(amount) from daybook,daybookpart where daybookpart.slno = daybook.slno and daybook.control <= :rlevel and daybook.tdate  >=:rdate and daybook.tdate <= :rdate2 and left(daybookpart.vchno,2) = 'VR' and daybook.accode = 'CASH' ) as orcptamt, (select sum(netamt) from salesm where control <= :rlevel and tdate >= :rdate and tdate <= :rdate2) as tnetamt, (select sum(ramt) from salesm where control <= :rlevel and tdate >= :rdate and tdate <= :rdate2) as trcvdamt FROM onerec", 'args': ['rlevel', 'rdate', 'rdate2', 'rdaycashbal', 'rcashbal', 'rclgornwgt', 'rclgoldwgt', 'rclgotherwgt', 'rclsornwgt', 'rclsoldwgt'], 'arg_types': {'rlevel': 'number', 'rdate': 'date', 'rdate2': 'date', 'rdaycashbal': 'number', 'rcashbal': 'number', 'rclgornwgt': 'number', 'rclgoldwgt': 'number', 'rclgotherwgt': 'number', 'rclsornwgt': 'number', 'rclsoldwgt': 'number'}, 'tables': ['onerec'], 'columns': [{'name': 'field', 'label': 'field', 'type': 'char'}, {'name': 'saleamt', 'label': 'saleamt', 'type': 'decimal'}, {'name': 'cgsaleswgt', 'label': 'cgsaleswgt', 'type': 'decimal'}, {'name': 'cssaleswgt', 'label': 'cssaleswgt', 'type': 'decimal'}, {'name': 'cogpurchwgt', 'label': 'cogpurchwgt', 'type': 'decimal'}, {'name': 'cssalesamt', 'label': 'cssalesamt', 'type': 'decimal'}, {'name': 'cadvamt', 'label': 'cadvamt', 'type': 'decimal'}, {'name': 'coglesswgt', 'label': 'coglesswgt', 'type': 'decimal'}, {'name': 'crefundamt', 'label': 'crefundamt', 'type': 'decimal'}, {'name': 'cgsaleswgtr', 'label': 'cgsaleswgtr', 'type': 'decimal'}, {'name': 'cgsalesamtr', 'label': 'cgsalesamtr', 'type': 'decimal'}, {'name': 'cspurchamt', 'label': 'cspurchamt', 'type': 'decimal'}, {'name': 'cspurchwgt', 'label': 'cspurchwgt', 'type': 'decimal'}, {'name': 'saleexamt', 'label': 'saleexamt', 'type': 'decimal'}, {'name': 'cogpurchamt', 'label': 'cogpurchamt', 'type': 'decimal'}, {'name': 'ocustrcptamt', 'label': 'ocustrcptamt', 'type': 'decimal'}, {'name': 'saletaxamt', 'label': 'saletaxamt', 'type': 'decimal'}, {'name': 'cgsalesamt', 'label': 'cgsalesamt', 'type': 'decimal'}, {'name': 'opmntamt', 'label': 'opmntamt', 'type': 'decimal'}, {'name': 'salediscamt', 'label': 'salediscamt', 'type': 'decimal'}, {'name': 'orcptamt', 'label': 'orcptamt', 'type': 'decimal'}, {'name': 'tnetamt', 'label': 'tnetamt', 'type': 'decimal'}, {'name': 'trcvdamt', 'label': 'trcvdamt', 'type': 'decimal'}]},
)


class TermSummaryMalayalamForm(GeneratedForm):
    """Term Summary Malayalam"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date2', 983, 0, 389, 84, taborder=20)
        self.add('editmask', 'em_date1', 338, 4, 389, 84, taborder=10)
        self.add('commandbutton', 'cb_show', 1833, 4, 261, 84, text='&Show', taborder=30)
        self.add('commandbutton', 'cb_1', 2382, 4, 247, 84, text='&Print', taborder=60)
        self.add('commandbutton', 'cb_2', 2629, 4, 247, 84, text='E&xit', taborder=50)
        self.add('statictext', 'st_2', 741, 8, 247, 76, text='Date To :')
        self.add('statictext', 'st_1', 14, 12, 329, 76, text='Date From :')
        self.add('datawindow', 'dw_history', 0, 96, 3621, 2080, dataobject='d_termsummary_mala', taborder=40)
