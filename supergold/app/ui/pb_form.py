"""
Render any PowerBuilder window as a PySide6 screen.

This is the engine that converts every GMINE window — masters, transactions,
reports and utilities alike — without skipping any. It parses the window's
``.srw`` source (see :mod:`app.pb_parser`) and rebuilds the screen control for
control, preserving the original layout, captions and field lengths, then wires
the standard PowerBuilder data toolbar (Add / Save / Delete / Edit / Cancel /
Exit) and a live data grid over the window's primary table.

Modules that have a hand-written business-logic implementation (Phase 4) are
registered in :mod:`app.modules` and take over from this generic renderer.
"""

from __future__ import annotations

from PySide6.QtCore import Qt, QRect
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QCheckBox, QComboBox, QFrame, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QMessageBox, QPushButton, QRadioButton, QScrollArea, QTableWidget,
    QTableWidgetItem, QTextEdit, QVBoxLayout, QWidget,
)

from app import pb_parser
from app.pb_parser import PBU

import db

_STD_BUTTON = {
    "cb_add": "add", "cb_save": "save", "cb_delete": "delete",
    "cb_edit": "edit", "cb_cancel": "cancel", "cb_exit": "exit",
    "cb_close": "exit", "cb_new": "add", "cb_update": "save",
}


class PBWindowForm(QWidget):
    """Generic, faithful renderer for a parsed PowerBuilder window."""

    def __init__(self, window: pb_parser.Window, parent=None):
        super().__init__(parent)
        self.window_def = window
        self._inputs: dict[str, QWidget] = {}
        self._build()

    # -- construction ------------------------------------------------------
    def _build(self):
        outer = QVBoxLayout(self)
        outer.setContentsMargins(0, 0, 0, 0)

        outer.addWidget(self._header())

        scroll = QScrollArea()
        scroll.setWidgetResizable(False)
        canvas = QWidget()
        canvas.setFixedSize(int(self.window_def.width * PBU) + 40,
                            int(self.window_def.height * PBU) + 40)
        self._render_controls(canvas)
        scroll.setWidget(canvas)
        outer.addWidget(scroll, 1)

        grid = self._data_grid()
        if grid is not None:
            outer.addWidget(grid)

    def _header(self) -> QWidget:
        bar = QFrame()
        bar.setStyleSheet("background:#1f3a5f;color:white;")
        lay = QHBoxLayout(bar)
        lay.setContentsMargins(12, 8, 12, 8)
        title = QLabel(self.window_def.title)
        f = QFont()
        f.setPointSize(12)
        f.setBold(True)
        title.setFont(f)
        title.setStyleSheet("color:white;")
        lay.addWidget(title)
        lay.addStretch(1)
        meta = QLabel(f"{self.window_def.name}")
        meta.setStyleSheet("color:#b9c7da;")
        lay.addWidget(meta)
        return bar

    def _render_controls(self, canvas: QWidget):
        for c in self.window_def.controls:
            widget = self._make_widget(c, canvas)
            if widget is None:
                continue
            widget.setParent(canvas)
            widget.setGeometry(QRect(
                int(c.x * PBU) + 8, int(c.y * PBU) + 8,
                max(int(c.width * PBU), 16), max(int(c.height * PBU), 16)))
            widget.show()

    def _make_widget(self, c: pb_parser.Control, canvas):
        kind = c.kind
        if kind == "statictext":
            w = QLabel(c.text)
            w.setWordWrap(True)
            return w
        if kind in ("singlelineedit", "editmask"):
            w = QLineEdit()
            if c.limit:
                w.setMaxLength(c.limit)
            self._inputs[c.name] = w
            return w
        if kind == "multilineedit":
            w = QTextEdit()
            self._inputs[c.name] = w
            return w
        if kind == "checkbox":
            w = QCheckBox(c.text)
            self._inputs[c.name] = w
            return w
        if kind == "radiobutton":
            w = QRadioButton(c.text)
            self._inputs[c.name] = w
            return w
        if kind in ("dropdownlistbox", "listbox"):
            w = QComboBox()
            w.addItems(c.items)
            self._inputs[c.name] = w
            return w
        if kind == "commandbutton":
            return self._make_button(c)
        if kind == "groupbox":
            w = QGroupBox(c.text)
            return w
        if kind == "datawindow":
            w = QTableWidget(0, 0)
            w.setToolTip(f"DataWindow: {c.dataobject}")
            return w
        if kind in pb_parser.DECORATION_KINDS:
            w = QFrame()
            w.setFrameShape(QFrame.Box if kind != "line" else QFrame.HLine)
            w.setStyleSheet("color:#c0c6cc;")
            return w
        # Unknown control: show a small placeholder so nothing silently vanishes.
        lbl = QLabel(c.text or kind)
        lbl.setStyleSheet("color:#888;border:1px dashed #ccc;")
        return lbl

    def _make_button(self, c: pb_parser.Control) -> QPushButton:
        btn = QPushButton(c.text or c.name)
        action = _STD_BUTTON.get(c.name.lower())
        if action == "exit":
            btn.clicked.connect(self._close_tab)
        elif action == "save":
            btn.clicked.connect(self._save)
        elif action == "delete":
            btn.clicked.connect(self._delete)
        elif action == "add":
            btn.clicked.connect(self._clear)
        elif action == "cancel":
            btn.clicked.connect(self._clear)
        else:
            btn.clicked.connect(lambda: self._info(c.text or c.name))
        return btn

    # -- data grid over the primary table ---------------------------------
    def _primary_table(self) -> str | None:
        return self.window_def.tables[0] if self.window_def.tables else None

    def _data_grid(self) -> QWidget | None:
        table = self._primary_table()
        if not table:
            return None
        box = QGroupBox(f"Records — {table}")
        lay = QVBoxLayout(box)
        grid = QTableWidget(0, 0)
        grid.setEditTriggers(QTableWidget.NoEditTriggers)
        grid.setSelectionBehavior(QTableWidget.SelectRows)
        lay.addWidget(grid)
        refresh = QPushButton("Refresh")
        refresh.clicked.connect(lambda: self._load_grid(grid, table))
        lay.addWidget(refresh, 0, Qt.AlignLeft)
        box.setMaximumHeight(240)
        self._load_grid(grid, table)
        return box

    def _load_grid(self, grid: QTableWidget, table: str):
        try:
            rows = db.fetch_all(f"SELECT * FROM {table}")
        except Exception as exc:
            grid.setRowCount(1)
            grid.setColumnCount(1)
            grid.setHorizontalHeaderLabels(["info"])
            grid.setItem(0, 0, QTableWidgetItem(
                f"Table '{table}' unavailable in current database ({exc})"))
            return
        if not rows:
            grid.setRowCount(0)
            grid.setColumnCount(0)
            return
        cols = list(rows[0].keys())
        grid.setColumnCount(len(cols))
        grid.setHorizontalHeaderLabels(cols)
        grid.setRowCount(len(rows))
        for r, row in enumerate(rows):
            for cidx, col in enumerate(cols):
                grid.setItem(r, cidx, QTableWidgetItem(
                    "" if row[col] is None else str(row[col])))
        grid.resizeColumnsToContents()

    # -- standard toolbar actions -----------------------------------------
    def _save(self):
        self._info("Save — record persistence for this window is handled by its "
                   "business-logic module (Phase 4). This generic screen does not "
                   "guess column mappings to avoid corrupting data.")

    def _delete(self):
        self._info("Delete — handled by the window's business-logic module.")

    def _clear(self):
        for w in self._inputs.values():
            if isinstance(w, QLineEdit):
                w.clear()
            elif isinstance(w, QTextEdit):
                w.clear()
            elif isinstance(w, QCheckBox):
                w.setChecked(False)
            elif isinstance(w, QComboBox):
                w.setCurrentIndex(0)

    def _close_tab(self):
        parent = self.parent()
        from PySide6.QtWidgets import QTabWidget
        while parent is not None and not isinstance(parent, QTabWidget):
            parent = parent.parent()
        if isinstance(parent, QTabWidget):
            parent.removeTab(parent.indexOf(self))

    def _info(self, msg: str):
        QMessageBox.information(self, self.window_def.title, msg)
