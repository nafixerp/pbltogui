"""Data Sync — w_datatransfer2.

Generated from the PowerBuilder window ``w_datatransfer2.srw`` by
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
    name='w_datatransfer2',
    title='Data Sync',
    width=2277,
    height=1824,
    controls=[],
    tables=['repairm', 'refinerym', 'orderm', 'clients', 'salesm', 'smithm', 'oitemtranm', 'daybook', 'accountm', 'spdmddet', 'salesrm', 'purchasem', 'purchaserm', 'daybookratewgt', 'collection', 'advafter', 'barcode', 'wgtrcptpmnt', 'refineryd', 'oitemtrand', 'repaird', 'itemadj', 'kuricolln', 'kurifinishdet', 'kuriint', 'itemsothers', 'salesd', 'salesrd', 'purchased', 'purchased_dmddet', 'purchaserd', 'suspentry', 'orderd', 'orderdga', 'orderdmodel', 'smithd', 'barcodedoc', 'clients_kuridet', 'clientsgs', 'items', 'itemsstk', 'accountgbs', 'accountg', 'barcode_dmddet', 'barcodedmd', 'counter', 'sman', 'itemgrp', 'stktype', 'staffleave', 'pcard', 'pcardtable', 'file', 'itemsqtype', 'daybookpart', 'delpart'],
    source_path='w_datatransfer2.srw',
    opens=['w_tranwait'],
)


class DataSyncForm(GeneratedForm):
    """Data Sync"""

    WINDOW = WINDOW

    def build_controls(self):
        self.add('editmask', 'em_date1', 430, 12, 489, 100, taborder=10)
        self.add('statictext', 'st_3', 18, 24, 402, 76, text='Date From')
        self.add('editmask', 'em_date2', 430, 116, 489, 100, taborder=20)
        self.add('checkbox', 'cbx_checkall', 1243, 124, 480, 80, text='Check All Data')
        self.add('statictext', 'st_1', 18, 132, 402, 72, text='Date To')
        self.add('commandbutton', 'cb_browse', 1737, 212, 357, 100, text='Browse', taborder=100)
        self.add('dropdownlistbox', 'ddlb_type', 5, 220, 416, 400, text='To File', items=['From File', 'To File'])
        self.add('singlelineedit', 'sle_path', 430, 220, 1303, 92, taborder=110)
        self.add('commandbutton', 'cb_def', 1737, 312, 357, 100, text='Set as defauls', taborder=90)
        self.add('singlelineedit', 'sle_maxslno', 430, 316, 489, 92, taborder=80)
        self.add('singlelineedit', 'sle_increase', 1243, 316, 489, 92, taborder=60)
        self.add('statictext', 'st_5', 18, 324, 402, 76, text='Max Slno')
        self.add('statictext', 'st_6', 937, 324, 297, 76, text='Increase :')
        self.add('singlelineedit', 'sle_attach', 430, 412, 489, 92, limit=1, taborder=70)
        self.add('statictext', 'st_7', 18, 416, 402, 80, text='Attach Letter')
        self.add('checkbox', 'cbx_nw', 1243, 428, 562, 80, text='To Network Server')
        self.add('multilineedit', 'mle_2', 101, 520, 1646, 208, text='You may transfer your data into the file you mentioned above. The transfer affect new entries only, it will not consider the modification done after first transfer of the same data.', taborder=30)
        self.add('checkbox', 'cbx_sales', 96, 748, 288, 80, text='Sales')
        self.add('checkbox', 'cbx_sreturn', 512, 748, 315, 80, text='SReturn')
        self.add('checkbox', 'cbx_purchase', 997, 748, 352, 80, text='Purchase')
        self.add('checkbox', 'cbx_preturn', 1426, 748, 320, 80, text='PReturn')
        self.add('checkbox', 'cbx_smith', 96, 824, 786, 80, text='GoldSmith/Jewellery Trans')
        self.add('checkbox', 'cbx_itemadj', 1426, 828, 302, 80, text='Item Adj')
        self.add('checkbox', 'cbx_order', 997, 832, 288, 80, text='Order')
        self.add('checkbox', 'cbx_refinery', 96, 900, 329, 80, text='Refinery')
        self.add('checkbox', 'cbx_remake', 512, 900, 329, 80, text='Remake')
        self.add('checkbox', 'cbx_otheritems', 997, 900, 375, 80, text='Other Items')
        self.add('checkbox', 'cbx_pcard', 1426, 940, 539, 80, text='Prev.Card Details')
        self.add('checkbox', 'cbx_rcpts', 96, 976, 347, 80, text='A/c Rcpts')
        self.add('checkbox', 'cbx_pmnts', 512, 976, 366, 80, text='A/c Pmnts')
        self.add('checkbox', 'cbx_journals', 997, 976, 379, 80, text='A/c Journal')
        self.add('checkbox', 'cbx_kurischeme', 997, 1052, 576, 80, text='Kuri/Scheme Colln')
        self.add('commandbutton', 'cb_selall', 517, 1064, 379, 72, text='Deselect All')
        self.add('checkbox', 'cbx_chkcash', 997, 1156, 407, 80, text='Check Cash')
        self.add('checkbox', 'cbx_nostkupdt', 261, 1160, 585, 76, text="Don't update Stock")
        self.add('checkbox', 'cbx_updtmaster', 997, 1236, 814, 80, text='Update A/c Master Changes')
        self.add('checkbox', 'cbx_nobcupdt', 261, 1240, 677, 76, text="Don't update BarCode")
        self.add('checkbox', 'cbx_updtdbookrate', 997, 1316, 704, 80, text='Update daybookrate full')
        self.add('statictext', 'st_cash1', 434, 1416, 375, 96)
        self.add('statictext', 'st_cash2', 841, 1416, 375, 96)
        self.add('statictext', 'st_cashdiff', 1243, 1416, 375, 96)
        self.add('commandbutton', 'cb_transfer', 544, 1548, 489, 108, text='Sync Data', taborder=40)
        self.add('commandbutton', 'cb_exit', 1061, 1548, 489, 108, text='Exit', taborder=50)
