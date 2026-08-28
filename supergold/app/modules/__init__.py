"""
Business-logic module registry (Phase 4).

Every window in the original menu renders automatically through the generic
:class:`app.ui.pb_form.PBWindowForm`. As individual modules get a faithful,
hand-written business-logic implementation, they register here keyed by the
PowerBuilder window name (e.g. ``"w_sales"``). The main window consults this
registry first and falls back to the generic renderer otherwise, so coverage is
always complete and fidelity improves module by module.

A factory takes the parsed :class:`app.pb_parser.Window` (may be ``None`` if the
source was not found) and returns a ``QWidget``.
"""

from __future__ import annotations

from typing import Callable

_REGISTRY: dict[str, Callable] = {}


def register(window_name: str):
    def deco(factory: Callable):
        _REGISTRY[window_name.lower()] = factory
        return factory
    return deco


def get_factory(window_name: str):
    return _REGISTRY.get((window_name or "").lower())


def registered_windows() -> set[str]:
    return set(_REGISTRY)


# Import concrete modules so their @register decorators run. Add new modules
# here as they are converted in Phase 4.
from app.modules import masters  # noqa: E402,F401
from app.modules import sales    # noqa: E402,F401
from app.modules import purchase  # noqa: E402,F401
from app.modules import accounting  # noqa: E402,F401
from app.modules import order  # noqa: E402,F401
from app.modules import repair  # noqa: E402,F401
from app.modules import goldsmith  # noqa: E402,F401
from app.modules import kuri  # noqa: E402,F401
from app.modules import utilities  # noqa: E402,F401
from app.modules import cancel  # noqa: E402,F401
# Bridges for menu items whose PB source is missing from the export (loaded last
# so real modules/reports above take precedence).
from app.modules import bridges  # noqa: E402,F401
# Converted reports (register through the same module registry).
from app.reports import sales_register  # noqa: E402,F401
from app.reports import purchase_register  # noqa: E402,F401
from app.reports import day_book  # noqa: E402,F401
from app.reports import trial_balance  # noqa: E402,F401
from app.reports import ac_ledger  # noqa: E402,F401
from app.reports import cash_book  # noqa: E402,F401
from app.reports import stock_register  # noqa: E402,F401
from app.reports import final_accounts  # noqa: E402,F401
