"""Order Sale Prof Analysis — w_order_prof_rep.

Generated from the PowerBuilder window ``w_order_prof_rep.srw`` by
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
    name='w_order_prof_rep',
    title='Order Sale Prof Analysis',
    width=3689,
    height=2300,
    controls=[],
    tables=[],
    source_path='w_order_prof_rep.srw',
    grid={'control': 'dw_1', 'dataobject': 'd_order_prof_rep', 'table': 'salesm', 'keys': ['slno'], 'computes': [{'name': 'totadvamt', 'expression': 'if(isnull( advamt1),0,advamt1)  +  if(isnull( advamt2 ),0,advamt2)', 'format': '########0.00', 'label': 'totadvamt', 'band': 'detail'}, {'name': 'totadvwgt', 'expression': 'if(isnull( advwgt1),0,advwgt1)  +  if(isnull( advwgt2 ),0,advwgt2)', 'format': '########0.000', 'label': 'totadvwgt', 'band': 'detail'}, {'name': 'totsoldamt', 'expression': ' billamt  -  totva ', 'format': '##########0.00', 'label': 'totsoldamt', 'band': 'detail'}, {'name': 'totsoldwgt', 'expression': ' soldwgt  -  soldstwgt ', 'format': '##########0.000', 'label': 'totsoldwgt', 'band': 'detail'}, {'name': 'diff', 'expression': '( ( totsoldwgt  -  totadvwgt ) *  grate + totadvamt ) - totsoldamt', 'format': '##########0.00', 'label': 'diff', 'band': 'detail'}, {'name': 'compute_1', 'expression': 'count(billno for all)', 'format': '[general]', 'label': 'compute_1', 'band': 'summary'}, {'name': 'compute_2', 'expression': 'sum( diff for all)', 'format': '##########0.00', 'label': 'compute_2', 'band': 'summary'}], 'columns': [{'name': 'tdate', 'label': 'Date', 'type': 'date'}, {'name': 'billno', 'label': 'Bill No', 'type': 'char'}, {'name': 'orderno', 'label': 'Order No', 'type': 'char'}, {'name': 'custname', 'label': 'Custname', 'type': 'char'}, {'name': 'advamt1', 'label': 'advamt1', 'type': 'decimal'}, {'name': 'advamt2', 'label': 'advamt2', 'type': 'decimal'}, {'name': 'advwgt1', 'label': 'advwgt1', 'type': 'decimal'}, {'name': 'advwgt2', 'label': 'advwgt2', 'type': 'decimal'}, {'name': 'soldwgt', 'label': 'soldwgt', 'type': 'decimal'}, {'name': 'billamt', 'label': 'billamt', 'type': 'decimal'}, {'name': 'totva', 'label': 'totva', 'type': 'decimal'}, {'name': 'soldstwgt', 'label': 'soldstwgt', 'type': 'decimal'}, {'name': 'grate', 'label': 'grate', 'type': 'decimal'}, {'name': 'slno', 'label': 'slno', 'type': 'decimal'}]},
    report={'dataobject': 'd_order_prof_rep', 'sql': 'SELECT salesm.tdate AS salesm_tdate, salesm.billno AS salesm_billno, salesm.orderno AS salesm_orderno, salesm.custname AS salesm_custname, salesm.billamt AS salesm_billamt, salesm.grate AS salesm_grate, salesm.slno AS salesm_slno, (select sum(orderm.advance + orderm.sretamt + orderm.eamt) from orderm where orderm.ordno = salesm.orderno) as advamt1, (select sum(advafter.amount) from advafter where advafter.ordno = salesm.orderno) as advamt2, (select sum( orderm.gadvance + (orderm.advance + orderm.sretamt + orderm.eamt) / orderm.rate) from orderm where orderm.ordno = salesm.orderno) as advwgt1, (select sum(advafter.amount / advafter.rate) from advafter where advafter.ordno = salesm.orderno) as advwgt2, (select sum(salesd.weight) from salesd where salesd.slno = salesm.slno) as soldwgt, (select sum(salesd.mcharge + salesd.stoneprice) from salesd where salesd.slno = salesm.slno) as totva, (select sum(salesd.stonewgt) from salesd where salesd.slno = salesm.slno) as soldstwgt FROM salesm ORDER BY salesm.tdate ASC, salesm.billno ASC', 'computes': [{'name': 'totadvamt', 'expression': 'if(isnull( advamt1),0,advamt1)  +  if(isnull( advamt2 ),0,advamt2)', 'format': '########0.00', 'label': 'totadvamt', 'band': 'detail'}, {'name': 'totadvwgt', 'expression': 'if(isnull( advwgt1),0,advwgt1)  +  if(isnull( advwgt2 ),0,advwgt2)', 'format': '########0.000', 'label': 'totadvwgt', 'band': 'detail'}, {'name': 'totsoldamt', 'expression': ' billamt  -  totva ', 'format': '##########0.00', 'label': 'totsoldamt', 'band': 'detail'}, {'name': 'totsoldwgt', 'expression': ' soldwgt  -  soldstwgt ', 'format': '##########0.000', 'label': 'totsoldwgt', 'band': 'detail'}, {'name': 'diff', 'expression': '( ( totsoldwgt  -  totadvwgt ) *  grate + totadvamt ) - totsoldamt', 'format': '##########0.00', 'label': 'diff', 'band': 'detail'}, {'name': 'compute_1', 'expression': 'count(billno for all)', 'format': '[general]', 'label': 'compute_1', 'band': 'summary'}, {'name': 'compute_2', 'expression': 'sum( diff for all)', 'format': '##########0.00', 'label': 'compute_2', 'band': 'summary'}], 'args': ['rdate1', 'rdate2', 'rlevel'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date', 'rlevel': 'number'}, 'tables': ['salesm'], 'columns': [{'name': 'tdate', 'label': 'Date', 'type': 'date'}, {'name': 'billno', 'label': 'Bill No', 'type': 'char'}, {'name': 'orderno', 'label': 'Order No', 'type': 'char'}, {'name': 'custname', 'label': 'Custname', 'type': 'char'}, {'name': 'advamt1', 'label': 'advamt1', 'type': 'decimal'}, {'name': 'advamt2', 'label': 'advamt2', 'type': 'decimal'}, {'name': 'advwgt1', 'label': 'advwgt1', 'type': 'decimal'}, {'name': 'advwgt2', 'label': 'advwgt2', 'type': 'decimal'}, {'name': 'soldwgt', 'label': 'soldwgt', 'type': 'decimal'}, {'name': 'billamt', 'label': 'billamt', 'type': 'decimal'}, {'name': 'totva', 'label': 'totva', 'type': 'decimal'}, {'name': 'soldstwgt', 'label': 'soldstwgt', 'type': 'decimal'}, {'name': 'grate', 'label': 'grate', 'type': 'decimal'}, {'name': 'slno', 'label': 'slno', 'type': 'decimal'}]},
)


class OrderSaleProfAnalysisForm(GeneratedForm):
    """Order Sale Prof Analysis"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 224, 0, 466, 92, taborder=10)
        self.add('editmask', 'em_date2', 965, 0, 466, 92, taborder=20)
        self.add('commandbutton', 'cb_show', 2610, 0, 247, 96, text='&Show', taborder=30)
        self.add('commandbutton', 'cb_3', 2862, 0, 247, 96, text='Save &As', taborder=80)
        self.add('commandbutton', 'cb_1', 3113, 0, 251, 96, text='&Print', taborder=90)
        self.add('commandbutton', 'cb_2', 3369, 0, 251, 96, text='E&xit', taborder=70)
        self.add('statictext', 'st_1', 0, 8, 215, 76, text='From :')
        self.add('statictext', 'st_2', 827, 8, 128, 76, text='To :')
        self.add('datawindow', 'dw_1', 5, 104, 3621, 1992, dataobject='d_order_prof_rep', taborder=50)
