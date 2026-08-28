"""
Base class for the generated form modules.

Every window of the original application has a real Python module in
:mod:`app.forms` — one file per screen, listing that screen's controls at their
original positions. Those modules only describe the layout; everything a screen
*does* (record editing through the DataWindow grid or the mapped fields, the
data view over the window's own query, search, export) is inherited from here,
which is the same behaviour :class:`app.ui.pb_form.PBWindowForm` provides.

A generated module therefore reads as plain PySide6 code::

    class ItemGroupsForm(GeneratedForm):
        WINDOW = Window(name="w_itemgrp", title="Item Groups", ...)

        def build_controls(self):
            self.add("statictext", "st_1", 40, 40, 200, 60, text="Code")
            self.add("singlelineedit", "sle_code", 260, 40, 300, 60, limit=10)
"""

from __future__ import annotations

from app.pb_parser import Control, Window
from app.ui.pb_form import PBWindowForm


class GeneratedForm(PBWindowForm):
    """A screen whose controls are declared by a generated module."""

    WINDOW: Window = Window(name="", title="", width=2400, height=1500,
                            controls=[], tables=[], source_path="")

    def __init__(self, parsed: Window | None = None, parent=None,
                 seed: dict | None = None):
        # ``parsed`` is what the module registry passes when the PowerBuilder
        # source is also available; the generated layout is used either way.
        window = Window(
            name=self.WINDOW.name, title=self.WINDOW.title,
            width=self.WINDOW.width, height=self.WINDOW.height,
            controls=[], tables=list(self.WINDOW.tables),
            source_path=self.WINDOW.source_path,
            grid=self.WINDOW.grid, report=self.WINDOW.report,
            opens=list(self.WINDOW.opens))
        self._canvas = None
        super().__init__(window, parent, seed=seed)

    # -- declaration API used by the generated modules ---------------------
    def add(self, kind: str, name: str, x: int, y: int, width: int, height: int,
            text: str = "", limit: int = 0, items: list | None = None,
            dataobject: str = "", taborder: int = 0):
        """Declare one control, exactly as the original window placed it."""
        control = Control(name=name, kind=kind, x=x, y=y, width=width,
                          height=height, text=text, taborder=taborder,
                          limit=limit, items=list(items or []),
                          dataobject=dataobject)
        self.window_def.controls.append(control)
        widget = self._make_widget(control, self._canvas)
        if widget is None:
            return None
        self._place(widget, control)
        return widget

    def build_controls(self):
        """Overridden by each generated module."""

    # -- wiring into the renderer ------------------------------------------
    def _render_controls(self, canvas):
        self._canvas = canvas
        self.build_controls()

    def _place(self, widget, control):
        from PySide6.QtCore import QRect
        from app.pb_parser import PBU
        widget.setParent(self._canvas)
        widget.setGeometry(QRect(
            int(control.x * PBU) + 8, int(control.y * PBU) + 8,
            max(int(control.width * PBU), 16), max(int(control.height * PBU), 16)))
        widget.show()
