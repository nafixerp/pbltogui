"""
Bridges for menu items whose PowerBuilder source is absent from the export.

`project_tree.txt` marks three menu entries "source not found" — their `.srw`
was never included in the PBL export, so the generic renderer has nothing to
parse. Rather than leave them as dead menu items, they are bridged to the
closest faithful converted screen so every one of the 331 menu items opens a
working window:

  * ``w_itemadj_wgtrcptpmnt`` — Partners Deposit (Wgt) > New. A partner weight
    receipt/payment, i.e. the same weight transaction as Party-Weight-Deposit,
    which the original menu itself routes to ``w_gsmith``. Bridged to the
    Goldsmith weight form.
  * ``wtmp`` — a throwaway temp name used by the Item-Adjustment and
    Barcode-Stock-List report entries. Bridged to the Stock Register report.

If the real sources are supplied later, registering them normally overrides
these bridges.
"""

from __future__ import annotations

from app import modules
from app.modules.goldsmith import GoldsmithForm
from app.reports.stock_register import SPEC as STOCK_SPEC
from app.reports.framework import ReportView


def _wgt_deposit(window):
    return GoldsmithForm(window)


def _stock_report(window):
    return ReportView(STOCK_SPEC)


# Only bridge if a real source-backed module has not claimed the name.
for _win, _factory in (("w_itemadj_wgtrcptpmnt", _wgt_deposit),
                       ("wtmp", _stock_report)):
    if _win not in modules.registered_windows():
        modules.register(_win)(_factory)
