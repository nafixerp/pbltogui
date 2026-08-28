"""Barcode List — w_barcodelist.

Generated from the PowerBuilder window ``w_barcodelist.srw`` by
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
    name='w_barcodelist',
    title='Barcode List',
    width=4603,
    height=2224,
    controls=[],
    tables=['barcode_dmddet', 'purchasem', 'smithm', 'barcode', 'items', 'userd'],
    source_path='w_barcodelist.srw',
    report={'dataobject': 'd_barcodelist', 'sql': "SELECT items.name AS items_name, barcode.bcode AS barcode_bcode, barcode.icode AS barcode_icode, barcode.qty AS barcode_qty, barcode.weight AS barcode_weight, barcode.stweight AS barcode_stweight, barcode.stprice AS barcode_stprice, barcode.wastage AS barcode_wastage, barcode.mc AS barcode_mc, barcode.tdate AS barcode_tdate, barcode.smcode AS barcode_smcode, barcode.part AS barcode_part, barcode.mcrate AS barcode_mcrate, barcode.stk AS barcode_stk, barcode.qtype AS barcode_qtype, barcode.qunit AS barcode_qunit, barcode.vap AS barcode_vap, barcode.docno AS barcode_docno, barcode.tamt AS barcode_tamt, barcode.smithcode AS barcode_smithcode, barcode.rate AS barcode_rate, items.grpcode AS items_grpcode, items.dmdplt AS items_dmdplt, items.itype AS items_itype, barcode.subgrp AS barcode_subgrp, barcode.cost AS barcode_cost, barcode.serialno AS barcode_serialno, barcode.nodisc AS barcode_nodisc, barcode.costperc AS barcode_costperc, barcode.transtouch AS barcode_transtouch, barcode.stktouch AS barcode_stktouch, barcode.costmc AS barcode_costmc, barcode.grate AS barcode_grate, barcode.coststone AS barcode_coststone, barcode.pqty AS barcode_pqty, barcode.pwgt AS barcode_pwgt, barcode.pstwgt AS barcode_pstwgt, barcode.costamt AS barcode_costamt, barcode.control AS barcode_control, barcode.rslno AS barcode_rslno, barcode.islno AS barcode_islno, barcode.counter AS barcode_counter, barcode.smithmcrate AS barcode_smithmcrate, barcode.sdate AS barcode_sdate, barcode.weight2 AS barcode_weight2, barcode.goldct AS barcode_goldct, barcode.stkinnos AS barcode_stkinnos, barcode.note AS barcode_note, barcode.sizemodel AS barcode_sizemodel, barcode.model AS barcode_model, barcode.minvap AS barcode_minvap, barcode.status AS barcode_status, barcode.huid AS barcode_huid, 0 as prn, (select barcodedmd.dmdwgt from barcodedmd where barcodedmd.bcode = barcode.bcode) as dmdwgt, (select barcodedmd.dmdamt from barcodedmd where barcodedmd.bcode = barcode.bcode) as dmdamt, (select barcodedmd.dmdnos from barcodedmd where barcodedmd.bcode = barcode.bcode) as dmdnos, (select barcodedmd.dmdunit from barcodedmd where barcodedmd.bcode = barcode.bcode) as dmdunit, (select max(barcodedoc.smith) from barcodedoc where barcodedoc.docno = barcode.docno) as smith, ('') as bcph, (select max(purchasem.suppcode) from purchasem where purchasem.docno = barcode.docno) as scode FROM items, barcode WHERE items.code = barcode.icode AND barcode.tdate >= :rdate1 AND barcode.control <= :rlevel AND barcode.tdate <= :rdate2 ORDER BY barcode.bcode ASC", 'args': ['rdate1', 'rdate2', 'rlevel'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date', 'rlevel': 'number'}, 'tables': ['items', 'barcode'], 'columns': [{'name': 'items_name', 'label': 'items_name', 'type': 'char'}, {'name': 'barcode_bcode', 'label': 'barcode_bcode', 'type': 'decimal'}, {'name': 'barcode_icode', 'label': 'barcode_icode', 'type': 'char'}, {'name': 'barcode_qty', 'label': 'barcode_qty', 'type': 'long'}, {'name': 'barcode_weight', 'label': 'barcode_weight', 'type': 'decimal'}, {'name': 'barcode_stweight', 'label': 'barcode_stweight', 'type': 'decimal'}, {'name': 'barcode_stprice', 'label': 'barcode_stprice', 'type': 'decimal'}, {'name': 'barcode_wastage', 'label': 'barcode_wastage', 'type': 'decimal'}, {'name': 'barcode_mc', 'label': 'barcode_mc', 'type': 'decimal'}, {'name': 'barcode_tdate', 'label': 'barcode_tdate', 'type': 'date'}, {'name': 'barcode_smcode', 'label': 'barcode_smcode', 'type': 'char'}, {'name': 'barcode_part', 'label': 'barcode_part', 'type': 'char'}, {'name': 'barcode_mcrate', 'label': 'barcode_mcrate', 'type': 'decimal'}, {'name': 'barcode_stk', 'label': 'barcode_stk', 'type': 'char'}, {'name': 'items_prn', 'label': 'items_prn', 'type': 'long'}, {'name': 'cdmdwgt', 'label': 'cdmdwgt', 'type': 'decimal'}, {'name': 'cdmdamt', 'label': 'cdmdamt', 'type': 'decimal'}, {'name': 'cdmdnos', 'label': 'cdmdnos', 'type': 'long'}, {'name': 'cdmdunit', 'label': 'cdmdunit', 'type': 'char'}, {'name': 'barcode_qtype', 'label': 'barcode_qtype', 'type': 'char'}, {'name': 'barcode_qunit', 'label': 'barcode_qunit', 'type': 'char'}, {'name': 'barcode_vap', 'label': 'barcode_vap', 'type': 'decimal'}, {'name': 'barcode_docno', 'label': 'barcode_docno', 'type': 'char'}, {'name': 'smith', 'label': 'smith', 'type': 'char'}, {'name': 'barcode_tamt', 'label': 'barcode_tamt', 'type': 'decimal'}, {'name': 'bcph', 'label': 'bcph', 'type': 'char'}, {'name': 'barcode_smithcode', 'label': 'barcode_smithcode', 'type': 'char'}, {'name': 'barcode_rate', 'label': 'barcode_rate', 'type': 'decimal'}, {'name': 'scode', 'label': 'scode', 'type': 'char'}, {'name': 'items_grpcode', 'label': 'items_grpcode', 'type': 'char'}, {'name': 'items_dmdplt', 'label': 'items_dmdplt', 'type': 'char'}, {'name': 'items_itype', 'label': 'items_itype', 'type': 'char'}, {'name': 'barcode_subgrp', 'label': 'barcode_subgrp', 'type': 'char'}, {'name': 'barcode_cost', 'label': 'barcode_cost', 'type': 'decimal'}, {'name': 'barcode_serialno', 'label': 'barcode_serialno', 'type': 'char'}, {'name': 'barcode_nodisc', 'label': 'barcode_nodisc', 'type': 'char'}, {'name': 'barcode_costperc', 'label': 'barcode_costperc', 'type': 'decimal'}, {'name': 'barcode_transtouch', 'label': 'barcode_transtouch', 'type': 'decimal'}, {'name': 'barcode_stktouch', 'label': 'barcode_stktouch', 'type': 'decimal'}, {'name': 'barcode_costmc', 'label': 'barcode_costmc', 'type': 'decimal'}, {'name': 'barcode_grate', 'label': 'barcode_grate', 'type': 'decimal'}, {'name': 'barcode_coststone', 'label': 'barcode_coststone', 'type': 'decimal'}, {'name': 'barcode_pqty', 'label': 'barcode_pqty', 'type': 'long'}, {'name': 'barcode_pwgt', 'label': 'barcode_pwgt', 'type': 'decimal'}, {'name': 'barcode_pstwgt', 'label': 'barcode_pstwgt', 'type': 'decimal'}, {'name': 'barcode_costamt', 'label': 'barcode_costamt', 'type': 'decimal'}, {'name': 'barcode_control', 'label': 'barcode_control', 'type': 'long'}, {'name': 'barcode_rslno', 'label': 'barcode_rslno', 'type': 'decimal'}, {'name': 'barcode_islno', 'label': 'barcode_islno', 'type': 'decimal'}, {'name': 'barcode_counter', 'label': 'barcode_counter', 'type': 'char'}, {'name': 'barcode_smithmcrate', 'label': 'barcode_smithmcrate', 'type': 'decimal'}, {'name': 'barcode_sdate', 'label': 'barcode_sdate', 'type': 'date'}, {'name': 'barcode_weight2', 'label': 'barcode_weight2', 'type': 'decimal'}, {'name': 'barcode_goldct', 'label': 'barcode_goldct', 'type': 'decimal'}, {'name': 'barcode_stkinnos', 'label': 'barcode_stkinnos', 'type': 'char'}, {'name': 'barcode_note', 'label': 'barcode_note', 'type': 'char'}, {'name': 'barcode_sizemodel', 'label': 'barcode_sizemodel', 'type': 'char'}, {'name': 'barcode_model', 'label': 'barcode_model', 'type': 'char'}, {'name': 'barcode_minvap', 'label': 'barcode_minvap', 'type': 'decimal'}, {'name': 'barcode_status', 'label': 'barcode_status', 'type': 'char'}, {'name': 'barcode_huid', 'label': 'barcode_huid', 'type': 'char'}]},
    opens=['w_barcode_entry', 'w_clientshelp', 'w_barcode_dochelp', 'w_barcode_rename', 'w_itemhelp', 'w_barcode_history'],
)


class BarcodeListForm(GeneratedForm):
    """Barcode List"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 219, 0, 425, 92, taborder=10)
        self.add('editmask', 'em_date2', 1019, 0, 421, 92, taborder=20)
        self.add('singlelineedit', 'sle_docno', 1851, 0, 379, 92, limit=10, taborder=30)
        self.add('commandbutton', 'cb_dochlp', 2235, 0, 160, 92, text='&Help')
        self.add('commandbutton', 'cb_show', 2423, 0, 315, 92, text='&Show', taborder=40)
        self.add('commandbutton', 'cb_sort', 2857, 0, 247, 92, text='So&rt', taborder=60)
        self.add('commandbutton', 'cb_1', 3136, 0, 270, 92, text='Save &As', taborder=140)
        self.add('commandbutton', 'cb_bcodeprint', 3483, 0, 233, 92, text='&Print', taborder=130)
        self.add('commandbutton', 'cb_exit', 3721, 0, 233, 92, text='E&xit', taborder=120)
        self.add('statictext', 'st_2', 1627, 4, 229, 64, text='Doc.No.:')
        self.add('statictext', 'st_11', 873, 8, 137, 72, text='To :')
        self.add('statictext', 'st_10', 0, 12, 206, 60, text='From :')
        self.add('singlelineedit', 'sle_itemcode', 219, 96, 425, 92, limit=10, taborder=50)
        self.add('commandbutton', 'cb_itemhlp', 649, 96, 187, 92, text='&Help')
        self.add('dropdownlistbox', 'ddlb_type', 1019, 96, 421, 472, text='Stock Only', items=['Stock Only', 'Not in Stock', 'Transfer Pending', 'All'], taborder=80)
        self.add('singlelineedit', 'sle_bcno', 1851, 100, 379, 92, limit=10, taborder=30)
        self.add('commandbutton', 'cb_2', 2235, 100, 160, 92, text='Search', taborder=40)
        self.add('commandbutton', 'cb_rename', 2423, 100, 315, 92, text='&Rename', taborder=90)
        self.add('commandbutton', 'cb_sel', 2857, 100, 549, 92, text='Select All', taborder=100)
        self.add('commandbutton', 'cb_print', 3483, 100, 471, 92, text='Barcode Print', taborder=110)
        self.add('statictext', 'st_1', 0, 104, 206, 76, text='Item :')
        self.add('statictext', 'st_3', 1641, 112, 210, 64, text='BCNo.:')
        self.add('datawindow', 'dw_grp', 215, 192, 800, 88, dataobject='d_itemgrpcode', taborder=110)
        self.add('datawindow', 'dw_scode', 1851, 192, 677, 84, dataobject='d_smithsuppliercode', taborder=50)
        self.add('commandbutton', 'cb_3', 3483, 192, 233, 92, text='Ph Chk', taborder=100)
        self.add('commandbutton', 'cb_filter', 3721, 192, 233, 92, text='Filter', taborder=110)
        self.add('commandbutton', 'cb_edit', 3968, 192, 233, 92, text='Edit', taborder=110)
        self.add('dropdownlistbox', 'ddlb_itype', 1019, 196, 421, 564, text='All', items=['Gold', 'Silver', 'Others', 'Diamond', 'Platinum', 'Color Stone', 'Watch'], taborder=100)
        self.add('singlelineedit', 'sle_model', 3058, 196, 343, 80, taborder=50)
        self.add('statictext', 'st_5', 0, 200, 210, 68, text='Group :')
        self.add('statictext', 'st_4', 1577, 204, 270, 64, text='Supplier')
        self.add('statictext', 'st_8', 2857, 208, 197, 60, text='Model')
        self.add('datawindow', 'dw_subgrp', 1851, 276, 800, 88, dataobject='d_itemsubgrpcode', taborder=40)
        self.add('checkbox', 'cbx_subgrp', 2656, 280, 82, 80)
        self.add('singlelineedit', 'sle_search', 3058, 280, 343, 80, taborder=110)
        self.add('statictext', 'st_7', 2857, 284, 197, 60, text='Search')
        self.add('commandbutton', 'cb_delall', 3483, 284, 471, 80, text='Delete all Barcodes', taborder=100)
        self.add('checkbox', 'cbx_costcomp', 215, 288, 443, 68, text='Cost Compire')
        self.add('checkbox', 'cbx_cpmcstamt', 690, 292, 494, 60, text='CP,MC,St.Amt List')
        self.add('statictext', 'st_6', 1399, 292, 443, 72, text='Barcode SubGrp')
        self.add('statictext', 'st_colname', 3973, 292, 288, 68)
        self.add('datawindow', 'dw_saleregister', 0, 368, 4571, 1768, dataobject='d_barcodelist', taborder=70)
