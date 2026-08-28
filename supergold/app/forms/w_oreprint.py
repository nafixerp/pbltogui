"""Reprint — w_oreprint.

Generated from the PowerBuilder window ``w_oreprint.srw`` by
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
    name='w_oreprint',
    title='Reprint',
    width=1403,
    height=668,
    controls=[],
    tables=['orderm', 'salesm'],
    source_path='w_oreprint.srw',
    report={'dataobject': 'd_orderprint_thermal', 'sql': 'SELECT items.name AS items_name, items.itype AS items_itype, items.printvaamt AS items_printvaamt, orderm.ordno AS orderm_ordno, orderm.tdate AS orderm_tdate, orderm.custname AS orderm_custname, orderm.duedate AS orderm_duedate, orderm.rate AS orderm_rate, orderm.billamt AS orderm_billamt, orderm.eamt AS orderm_eamt, orderm.advance AS orderm_advance, orderm.smcode AS orderm_smcode, orderm.gadvance AS orderm_gadvance, orderm.sretamt AS orderm_sretamt, orderm.addr AS orderm_addr, orderm.refund AS orderm_refund, orderm.phone AS orderm_phone, orderm.tax AS orderm_tax, orderm.note AS orderm_note, orderm.cbcode AS orderm_cbcode, orderm.bcharge AS orderm_bcharge, orderm.addbcharge AS orderm_addbcharge, orderm.ccamt AS orderm_ccamt, orderm.chqno AS orderm_chqno, orderm.chqdate AS orderm_chqdate, orderm.chqamt AS orderm_chqamt, orderm.chqbank AS orderm_chqbank, orderm.cocode AS orderm_cocode, orderd.rate AS orderd_rate, orderd.qty AS orderd_qty, orderd.weight AS orderd_weight, orderd.mcharge AS orderd_mcharge, orderd.stonewgt AS orderd_stonewgt, orderd.stoneprice AS orderd_stoneprice, orderd.amount AS orderd_amount, orderd.part AS orderd_part, (orderm.eamt + orderm.sretamt ) as ordadv, (select sum(purchased.weight ) from purchased where purchased.slno = orderm.slno) as exchwgt, (select sum(purchased.stwgt) from purchased where purchased.slno = orderm.slno) as exchstwgt, (select sum(salesrd.weight ) from salesrd where salesrd.slno = orderm.slno) as sretwgt, (select sum(salesrd.stonewgt ) from salesrd where salesrd.slno = orderm.slno) as sretstwgt FROM items, orderd, orderm WHERE items.code = orderd.code AND orderd.slno = orderm.slno ORDER BY orderd.sno ASC', 'args': ['rslno'], 'arg_types': {'rslno': 'number'}, 'tables': ['items', 'orderd', 'orderm'], 'columns': [{'name': 'items_name', 'label': 'items_name', 'type': 'char'}, {'name': 'items_itype', 'label': 'items_itype', 'type': 'char'}, {'name': 'items_printvaamt', 'label': 'items_printvaamt', 'type': 'char'}, {'name': 'ordadv', 'label': 'ordadv', 'type': 'decimal'}, {'name': 'exchwgt', 'label': 'exchwgt', 'type': 'decimal'}, {'name': 'exchstwgt', 'label': 'exchstwgt', 'type': 'decimal'}, {'name': 'sretwgt', 'label': 'sretwgt', 'type': 'decimal'}, {'name': 'sretstwgt', 'label': 'sretstwgt', 'type': 'decimal'}, {'name': 'orderm_ordno', 'label': 'orderm_ordno', 'type': 'char'}, {'name': 'orderm_tdate', 'label': 'orderm_tdate', 'type': 'date'}, {'name': 'orderm_custname', 'label': 'orderm_custname', 'type': 'char'}, {'name': 'orderm_duedate', 'label': 'orderm_duedate', 'type': 'date'}, {'name': 'orderm_rate', 'label': 'orderm_rate', 'type': 'decimal'}, {'name': 'orderm_billamt', 'label': 'orderm_billamt', 'type': 'decimal'}, {'name': 'orderm_eamt', 'label': 'orderm_eamt', 'type': 'decimal'}, {'name': 'orderm_advance', 'label': 'orderm_advance', 'type': 'decimal'}, {'name': 'orderm_smcode', 'label': 'orderm_smcode', 'type': 'char'}, {'name': 'orderm_gadvance', 'label': 'orderm_gadvance', 'type': 'decimal'}, {'name': 'orderm_sretamt', 'label': 'orderm_sretamt', 'type': 'decimal'}, {'name': 'orderm_addr', 'label': 'orderm_addr', 'type': 'char'}, {'name': 'orderm_refund', 'label': 'orderm_refund', 'type': 'decimal'}, {'name': 'orderm_phone', 'label': 'orderm_phone', 'type': 'char'}, {'name': 'orderm_tax', 'label': 'orderm_tax', 'type': 'decimal'}, {'name': 'orderm_note', 'label': 'orderm_note', 'type': 'char'}, {'name': 'orderm_cbcode', 'label': 'orderm_cbcode', 'type': 'char'}, {'name': 'orderm_bcharge', 'label': 'orderm_bcharge', 'type': 'decimal'}, {'name': 'orderm_addbcharge', 'label': 'orderm_addbcharge', 'type': 'char'}, {'name': 'orderm_ccamt', 'label': 'orderm_ccamt', 'type': 'decimal'}, {'name': 'orderm_chqno', 'label': 'orderm_chqno', 'type': 'char'}, {'name': 'orderm_chqdate', 'label': 'orderm_chqdate', 'type': 'date'}, {'name': 'orderm_chqamt', 'label': 'orderm_chqamt', 'type': 'decimal'}, {'name': 'orderm_chqbank', 'label': 'orderm_chqbank', 'type': 'char'}, {'name': 'orderm_cocode', 'label': 'orderm_cocode', 'type': 'char'}, {'name': 'orderd_rate', 'label': 'orderd_rate', 'type': 'decimal'}, {'name': 'orderd_qty', 'label': 'orderd_qty', 'type': 'long'}, {'name': 'orderd_weight', 'label': 'orderd_weight', 'type': 'decimal'}, {'name': 'orderd_mcharge', 'label': 'orderd_mcharge', 'type': 'decimal'}, {'name': 'orderd_stonewgt', 'label': 'orderd_stonewgt', 'type': 'decimal'}, {'name': 'orderd_stoneprice', 'label': 'orderd_stoneprice', 'type': 'decimal'}, {'name': 'orderd_amount', 'label': 'orderd_amount', 'type': 'decimal'}, {'name': 'orderd_part', 'label': 'orderd_part', 'type': 'char'}]},
    opens=['w_orderhelp', 'w_orderprint_view'],
)


class ReprintForm(GeneratedForm):
    """Reprint"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('commandbutton', 'cb_help', 942, 136, 215, 92, text='&Help', taborder=20)
        self.add('singlelineedit', 'sle_billno', 512, 140, 411, 96, taborder=10)
        self.add('statictext', 'st_1', 27, 164, 494, 64, text='Enter Order no :')
        self.add('datawindow', 'dw_print', 32, 308, 229, 188, dataobject='d_orderprint_thermal', taborder=50)
        self.add('oval', 'oval_1', 398, 312, 731, 216)
        self.add('commandbutton', 'cb_ok', 485, 376, 261, 96, text='&OK', taborder=30)
        self.add('commandbutton', 'cb_exit', 782, 376, 261, 96, text='E&xit', taborder=40)
