"""PowerBuilder -> Python conversion engine.

Parses the original ERP's exported objects (.srw/.srd/.srm) into structured
models that the PySide6 runtime renders.  Pure-Python and headless-testable.
"""

from .source import PBSource, default_source
from .window_parser import parse_window, Window, Control
from .datawindow_parser import parse_datawindow, DataWindow, DWColumn
from .menu_parser import parse_menu, MenuItem, iter_leaves

__all__ = [
    "PBSource", "default_source",
    "parse_window", "Window", "Control",
    "parse_datawindow", "DataWindow", "DWColumn",
    "parse_menu", "MenuItem", "iter_leaves",
]
