"""Stock Ledger — w_oistockledger.

Generated from the PowerBuilder window ``w_oistockledger.srw`` by
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
    name='w_oistockledger',
    title='Stock Ledger',
    width=3630,
    height=2244,
    controls=[],
    tables=[],
    source_path='w_oistockledger.srw',
    grid={'control': 'dw_1', 'dataobject': 'd_oistockledger', 'table': 'itemsothers', 'keys': ['code'], 'computes': [{'name': 'costvalue', 'expression': 'stock * cost', 'format': '###########0.00', 'label': 'costvalue', 'band': 'detail'}, {'name': 'opstk', 'expression': 'opstock  +  if(isnull( oppqty ),0,oppqty) -  if(isnull( opsqty ),0,opsqty)', 'format': '########0', 'label': 'opstk', 'band': 'detail'}, {'name': 'stock', 'expression': 'opstk +  if(isnull( tpqty ),0, tpqty) -  if(isnull(tsqty ),0,tsqty)', 'format': '########0', 'label': 'stock', 'band': 'detail'}, {'name': 'compute_5', 'expression': 'sum(opstk for all)', 'format': '########0', 'label': 'compute_5', 'band': 'summary'}, {'name': 'compute_4', 'expression': 'sum(tpqty for all)', 'format': '########0', 'label': 'compute_4', 'band': 'summary'}, {'name': 'compute_3', 'expression': 'sum(tsqty for all)', 'format': '########0', 'label': 'compute_3', 'band': 'summary'}, {'name': 'compute_6', 'expression': 'sum( stock  for all)', 'format': '########0', 'label': 'compute_6', 'band': 'summary'}, {'name': 'compute_2', 'expression': 'sum( costvalue for all)', 'format': '###########0.00', 'label': 'compute_2', 'band': 'summary'}], 'columns': [{'name': 'code', 'label': 'Code', 'type': 'char'}, {'name': 'name', 'label': 'Item Name', 'type': 'char'}, {'name': 'grp', 'label': 'grp', 'type': 'char'}, {'name': 'keepstk', 'label': 'keepstk', 'type': 'long'}, {'name': 'cost', 'label': 'cost', 'type': 'decimal'}, {'name': 'oppqty', 'label': 'oppqty', 'type': 'decimal'}, {'name': 'opsqty', 'label': 'opsqty', 'type': 'decimal'}, {'name': 'tpqty', 'label': 'tpqty', 'type': 'decimal'}, {'name': 'tsqty', 'label': 'tsqty', 'type': 'decimal'}, {'name': 'opstock', 'label': 'opstock', 'type': 'long'}]},
    report={'dataobject': 'd_oistockledger', 'sql': "SELECT itemsothers.code AS itemsothers_code, itemsothers.name AS itemsothers_name, itemsothers.grp AS itemsothers_grp, itemsothers.keepstk AS itemsothers_keepstk, itemsothers.cost AS itemsothers_cost, itemsothers.opstock AS itemsothers_opstock, (select sum(oitemtrand.qty) from oitemtranm, oitemtrand where oitemtrand.slno = oitemtranm.slno and oitemtrand.code = itemsothers.code and oitemtranm.control <= :rlevel  and oitemtranm.tdate < :rdate1 and oitemtranm.tr = 'P') as oppqty, (select sum(oitemtrand.qty) from oitemtranm, oitemtrand where oitemtrand.slno = oitemtranm.slno and oitemtranm.tdate < :rdate1 and oitemtrand.code = itemsothers.code and oitemtranm.control <= :rlevel and oitemtranm.tr = 'S') as opsqty, (select sum(oitemtrand.qty) from oitemtranm, oitemtrand where oitemtrand.slno = oitemtranm.slno and oitemtranm.tdate >= :rdate1 and oitemtranm.tdate <= :rdate2 and oitemtrand.code = itemsothers.code and oitemtranm.control <= :rlevel and oitemtranm.tr = 'P') as tpqty, (select sum(oitemtrand.qty) from oitemtranm, oitemtrand where oitemtrand.slno = oitemtranm.slno and oitemtranm.tdate >= :rdate1 and oitemtranm.tdate <= :rdate2 and oitemtrand.code = itemsothers.code and oitemtranm.control <= :rlevel and oitemtranm.tr = 'S') as tsqty FROM itemsothers ORDER BY itemsothers.name ASC", 'computes': [{'name': 'costvalue', 'expression': 'stock * cost', 'format': '###########0.00', 'label': 'costvalue', 'band': 'detail'}, {'name': 'opstk', 'expression': 'opstock  +  if(isnull( oppqty ),0,oppqty) -  if(isnull( opsqty ),0,opsqty)', 'format': '########0', 'label': 'opstk', 'band': 'detail'}, {'name': 'stock', 'expression': 'opstk +  if(isnull( tpqty ),0, tpqty) -  if(isnull(tsqty ),0,tsqty)', 'format': '########0', 'label': 'stock', 'band': 'detail'}, {'name': 'compute_5', 'expression': 'sum(opstk for all)', 'format': '########0', 'label': 'compute_5', 'band': 'summary'}, {'name': 'compute_4', 'expression': 'sum(tpqty for all)', 'format': '########0', 'label': 'compute_4', 'band': 'summary'}, {'name': 'compute_3', 'expression': 'sum(tsqty for all)', 'format': '########0', 'label': 'compute_3', 'band': 'summary'}, {'name': 'compute_6', 'expression': 'sum( stock  for all)', 'format': '########0', 'label': 'compute_6', 'band': 'summary'}, {'name': 'compute_2', 'expression': 'sum( costvalue for all)', 'format': '###########0.00', 'label': 'compute_2', 'band': 'summary'}], 'args': ['rdate1', 'rdate2', 'rlevel'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date', 'rlevel': 'number'}, 'tables': ['itemsothers'], 'columns': [{'name': 'code', 'label': 'Code', 'type': 'char'}, {'name': 'name', 'label': 'Item Name', 'type': 'char'}, {'name': 'grp', 'label': 'grp', 'type': 'char'}, {'name': 'keepstk', 'label': 'keepstk', 'type': 'long'}, {'name': 'cost', 'label': 'cost', 'type': 'decimal'}, {'name': 'oppqty', 'label': 'oppqty', 'type': 'decimal'}, {'name': 'opsqty', 'label': 'opsqty', 'type': 'decimal'}, {'name': 'tpqty', 'label': 'tpqty', 'type': 'decimal'}, {'name': 'tsqty', 'label': 'tsqty', 'type': 'decimal'}, {'name': 'opstock', 'label': 'opstock', 'type': 'long'}]},
)


class StockLedgerForm(GeneratedForm):
    """Stock Ledger"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 293, 0, 375, 92, taborder=60)
        self.add('editmask', 'em_date2', 1280, 0, 379, 92, taborder=70)
        self.add('commandbutton', 'cb_show', 2281, 0, 288, 96, text='&Show', taborder=80)
        self.add('commandbutton', 'cb_saveas', 2757, 0, 279, 96, text='Save &As', taborder=50)
        self.add('commandbutton', 'cb_print', 3049, 0, 265, 96, text='&Print', taborder=60)
        self.add('commandbutton', 'cb_exit', 3328, 0, 265, 96, text='E&xit', taborder=30)
        self.add('statictext', 'st_1', 78, 8, 206, 76, text='From :')
        self.add('statictext', 'st_2', 1152, 8, 119, 76, text='To :')
        self.add('dropdownlistbox', 'ddlb_type3', 1280, 92, 590, 556, text='With Not Zero Stock', items=['All', 'With Stock Only', 'With -ve Stock', 'With Zero Stock', 'With Not Zero Stock'], taborder=20)
        self.add('datawindow', 'dw_grp', 293, 96, 800, 88, dataobject='d_itemgrpcode', taborder=40)
        self.add('statictext', 'st_grp', 37, 100, 247, 76, text='Group :')
        self.add('checkbox', 'cbx_grp', 1102, 104, 78, 76)
        self.add('checkbox', 'cbx_speed', 3049, 108, 425, 76, text='Speed Print')
        self.add('datawindow', 'dw_1', 0, 188, 3602, 1872, dataobject='d_oistockledger', taborder=10)
