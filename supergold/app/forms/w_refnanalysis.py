"""Analysis — w_refnanalysis.

Generated from the PowerBuilder window ``w_refnanalysis.srw`` by
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
    name='w_refnanalysis',
    title='Analysis',
    width=3675,
    height=2200,
    controls=[],
    tables=[],
    source_path='w_refnanalysis.srw',
    report={'dataobject': 'd_refnanalysis', 'sql': "SELECT refinerym.docno AS refinerym_docno, refinerym.tdate AS refinerym_tdate, refinerym.refcode AS refinerym_refcode, (select min(rfn.slno) from refinerym rfn where rfn.docno = refinerym.docno) as minslno, (select max(rfn.slno) from refinerym rfn where rfn.docno = refinerym.docno) as maxslno, (select min(rfn.status) from refinerym rfn where rfn.docno = refinerym.docno ) as minstatus, (select min(rfn.sno) from refineryd rfn where rfn.slno = minslno) as minsno, (select max(rfn.sno) from refineryd rfn where rfn.slno = maxslno) as maxsno, (select sum(refineryd.rcvdwgtamt) from refineryd where refineryd.slno = maxslno and refineryd.sno = maxsno ) as rcvdamt, (select sum(refineryd.rcvdwgt) from refineryd where refineryd.slno = maxslno and refineryd.sno = maxsno ) as rcvdwgt, (select sum(refineryd.testpcs) from refineryd,refinerym rfn where refineryd.slno = rfn.slno and rfn.docno = refinerym.docno) as testpcswgt, (select sum(rfn.charge) from refinerym rfn where rfn.docno = refinerym.docno) as totcharge, (select sum(refineryd.mudless) from refineryd where refineryd.slno = minslno) as tmudless, (select sum(refineryd.testpcs * ifnull(refineryd.ao, refineryd.rcvdwgtamt / refineryd.rcvdwgt, refineryd.issuedwgtamt / refineryd.issuedwgt )) from refineryd,refinerym rfn where refineryd.slno = rfn.slno and rfn.docno = refinerym.docno and ifnull(refineryd.ao,refineryd.rcvdwgt,refineryd.issuedwgt)  > 0  ) as testpcsamt, (select max(refineryd.code) from refineryd,items where refineryd.slno = minslno and refineryd.code = items.code and items.itype = 'G' and refineryd.issuedwgt > 0 and refineryd.sno = minsno) as issueditem, (select max(refineryd.code) from refineryd,items where refineryd.slno = maxslno and refineryd.code = items.code and items.itype = 'G' and refineryd.rcvdwgt > 0 and refineryd.sno = maxsno ) as rcvditem, (select items.name from items where items.code = issueditem ) as issueditemname, (select items.name from items where items.code = rcvditem ) as rcvditemname, (select max(rfn.testperc) from refinerym rfn where rfn.docno = refinerym.docno and rfn.testperc < 96) as ctestperc, (select sum(refineryd.issuedwgtamt) from refineryd where refineryd.slno = minslno) as issuedamt, (select sum( refineryd.issuedwgt ) from refineryd where refineryd.slno = minslno) as issuedwgt FROM refinerym WHERE refinerym.control <= :rlevel AND refinerym.tdate between :rdate1 and :rdate2 AND minstatus <> 1 ORDER BY refinerym.tdate ASC, refinerym.docno ASC", 'computes': [{'name': 'tissuedamt', 'expression': 'if(isnull(issuedamt),0,issuedamt) + if(isnull(totcharge),0,totcharge)', 'format': '########.00', 'label': 'tissuedamt', 'band': 'detail'}, {'name': 'amtdiff', 'expression': 'if(isnull( rcvdamt),0,rcvdamt) + if(isnull(testpcsamt),0,testpcsamt)  -  tissuedamt ', 'format': '########0.00', 'label': 'amtdiff', 'band': 'detail'}, {'name': 'diffwgt', 'expression': 'if(isnull( issuedwgt ),0,issuedwgt) -  if(isnull( rcvdwgt ),0,rcvdwgt) - if(isnull( testpcswgt ),0,testpcswgt)', 'format': '#####.000', 'label': 'diffwgt', 'band': 'detail'}, {'name': 'compute_4', 'expression': 'sum(issuedwgt for all)', 'format': '#######0.000', 'label': 'compute_4', 'band': 'summary'}, {'name': 'compute_6', 'expression': 'sum(tissuedamt for all)', 'format': '#######0.00', 'label': 'compute_6', 'band': 'summary'}, {'name': 'compute_7', 'expression': 'sum(rcvdwgt for all)', 'format': '#######0.000', 'label': 'compute_7', 'band': 'summary'}, {'name': 'compute_11', 'expression': 'sum(testpcswgt for all)', 'format': '###0.000', 'label': 'compute_11', 'band': 'summary'}, {'name': 'compute_12', 'expression': 'avg(ctestperc for all)', 'format': '##0.00', 'label': 'compute_12', 'band': 'summary'}, {'name': 'compute_8', 'expression': 'sum(rcvdamt for all)', 'format': '#######0.00', 'label': 'compute_8', 'band': 'summary'}, {'name': 'compute_9', 'expression': 'sum( amtdiff  for all)', 'format': '########0.00', 'label': 'compute_9', 'band': 'summary'}, {'name': 'compute_10', 'expression': 'sum( diffwgt  for all)', 'format': '#####.000', 'label': 'compute_10', 'band': 'summary'}, {'name': 'compute_5', 'expression': 'sum(tmudless for all)', 'format': '######0.000', 'label': 'compute_5', 'band': 'summary'}], 'args': ['rdate1', 'rdate2', 'rlevel'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date', 'rlevel': 'number'}, 'tables': ['refinerym'], 'columns': [{'name': 'refinerym_docno', 'label': 'refinerym_docno', 'type': 'char'}, {'name': 'refinerym_tdate', 'label': 'refinerym_tdate', 'type': 'date'}, {'name': 'refinerym_refcode', 'label': 'refinerym_refcode', 'type': 'char'}, {'name': 'minslno', 'label': 'minslno', 'type': 'decimal'}, {'name': 'maxslno', 'label': 'maxslno', 'type': 'decimal'}, {'name': 'minstatus', 'label': 'minstatus', 'type': 'long'}, {'name': 'minsno', 'label': 'minsno', 'type': 'long'}, {'name': 'maxsno', 'label': 'maxsno', 'type': 'long'}, {'name': 'rcvdamt', 'label': 'rcvdamt', 'type': 'decimal'}, {'name': 'rcvdwgt', 'label': 'rcvdwgt', 'type': 'decimal'}, {'name': 'testpcswgt', 'label': 'testpcswgt', 'type': 'decimal'}, {'name': 'totcharge', 'label': 'totcharge', 'type': 'decimal'}, {'name': 'tmudless', 'label': 'tmudless', 'type': 'decimal'}, {'name': 'testpcsamt', 'label': 'testpcsamt', 'type': 'decimal'}, {'name': 'issueditem', 'label': 'issueditem', 'type': 'char'}, {'name': 'rcvditem', 'label': 'rcvditem', 'type': 'char'}, {'name': 'issueditemname', 'label': 'issueditemname', 'type': 'char'}, {'name': 'rcvditemname', 'label': 'rcvditemname', 'type': 'char'}, {'name': 'ctestperc', 'label': 'ctestperc', 'type': 'decimal'}, {'name': 'issuedamt', 'label': 'issuedamt', 'type': 'decimal'}, {'name': 'issuedwgt', 'label': 'issuedwgt', 'type': 'decimal'}]},
    opens=['w_clientshelp'],
)


class AnalysisForm(GeneratedForm):
    """Analysis"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 1298, 0, 430, 100, taborder=20)
        self.add('editmask', 'em_date2', 2057, 0, 425, 100, taborder=30)
        self.add('commandbutton', 'cb_show', 2505, 0, 279, 100, text='&Show', taborder=40)
        self.add('commandbutton', 'cb_3', 2807, 0, 256, 100, text='Save &As', taborder=80)
        self.add('commandbutton', 'cb_1', 3077, 0, 265, 100, text='&Print', taborder=70)
        self.add('commandbutton', 'cb_2', 3342, 0, 265, 100, text='E&xit', taborder=60)
        self.add('datawindow', 'dw_accode', 334, 4, 416, 88, dataobject='d_refncode', taborder=10)
        self.add('checkbox', 'cbx_code', 754, 8, 73, 76)
        self.add('statictext', 'st_3', 27, 12, 297, 72, text='Refiner  :')
        self.add('statictext', 'st_1', 919, 16, 366, 64, text='Date From :')
        self.add('statictext', 'st_2', 1746, 16, 302, 72, text='Date To :')
        self.add('datawindow', 'dw_1', 0, 100, 3625, 1976, dataobject='d_refnanalysis', taborder=50)
        self.add('checkbox', 'cbx_expwgtcompare', 2505, 116, 978, 80, text='Expected Wgt Compare Report')
