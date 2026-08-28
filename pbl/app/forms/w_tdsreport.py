"""TDS Report — w_tdsreport.

Generated from the PowerBuilder window ``w_tdsreport.srw`` by
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
    name='w_tdsreport',
    title='TDS Report',
    width=3675,
    height=2300,
    controls=[],
    tables=['accountm'],
    source_path='w_tdsreport.srw',
    report={'dataobject': 'd_tdsreport', 'sql': 'SELECT smithm.tdate AS smithm_tdate, smithm.docno AS smithm_docno, smithm.smithcode AS smithm_smithcode, smithm.tmcharge AS smithm_tmcharge, smithm.tdsperc AS smithm_tdsperc, smithm.tdsamt AS smithm_tdsamt, (select clients.name from clients where clients.code = smithm.smithcode) as name, (select clients.ctype from clients where clients.code = smithm.smithcode) as ctype FROM smithm ORDER BY smithm.tdate ASC, smithm.docno ASC', 'args': ['rdate1', 'rdate2', 'rlevel'], 'arg_types': {'rdate1': 'date', 'rdate2': 'date', 'rlevel': 'number'}, 'tables': ['smithm'], 'columns': [{'name': 'tdate', 'label': 'Date', 'type': 'date'}, {'name': 'docno', 'label': 'Doc No', 'type': 'char'}, {'name': 'smithcode', 'label': 'Party', 'type': 'char'}, {'name': 'tmcharge', 'label': 'MC+St.Amt', 'type': 'decimal'}, {'name': 'tdsperc', 'label': 'TDS%', 'type': 'decimal'}, {'name': 'tdsamt', 'label': 'TDS Amt', 'type': 'decimal'}, {'name': 'name', 'label': 'name', 'type': 'char'}, {'name': 'ctype', 'label': 'ctype', 'type': 'char'}]},
    opens=['w_clientshelp'],
)


class TdsReportForm(GeneratedForm):
    """TDS Report"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 219, 0, 366, 92, taborder=10)
        self.add('editmask', 'em_date2', 786, 0, 366, 92, taborder=20)
        self.add('dropdownlistbox', 'ddlb_type', 1225, 0, 567, 432, text='Jewellery', items=['Jewellery', 'Goldsmith', 'All'], taborder=30)
        self.add('datawindow', 'dw_accode', 2075, 0, 434, 92, dataobject='d_jewl', taborder=40)
        self.add('commandbutton', 'cb_show', 2542, 0, 261, 96, text='&Show', taborder=50)
        self.add('commandbutton', 'cb_3', 2811, 0, 261, 96, text='Save &As', taborder=80)
        self.add('commandbutton', 'cb_1', 3077, 0, 265, 96, text='&Print', taborder=90)
        self.add('commandbutton', 'cb_2', 3342, 0, 265, 96, text='E&xit', taborder=70)
        self.add('statictext', 'st_2', 622, 4, 146, 72, text='To :')
        self.add('statictext', 'st_1', 0, 8, 210, 64, text='From :')
        self.add('statictext', 'st_3', 1838, 8, 229, 72, text='Party :')
        self.add('datawindow', 'dw_1', 0, 104, 3616, 2084, dataobject='d_tdsreport', taborder=60)
