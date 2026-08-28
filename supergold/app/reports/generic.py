"""
Run any window's own DataWindow as a working data view.

Every list and report window in GMINE is driven by a DataWindow whose retrieval
statement is part of the export. :func:`app.pb_parser.parse_datawindow` converts
that statement to SQL and :mod:`tools.build_catalog` stores it, so this module
can give *every* such window the behaviour it had originally: ask for the
retrieval arguments (date range, party, level, …), run the query, show the rows
under their original column headings, total the numeric columns, and
print/export the result.

It reuses the same export helpers as the hand-written reports, so a converted
report and an auto-generated one produce the same CSV and PDF.
"""

from __future__ import annotations

import datetime
import re

from PySide6.QtCore import QDate, Qt
from PySide6.QtWidgets import (
    QDateEdit, QFileDialog, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QMessageBox, QPushButton, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget,
)

import db
from app.reports.framework import export_csv, export_pdf

_ARG_RE = re.compile(r":(\w+)")
_NUMERIC_TYPES = ("decimal", "number", "long", "int", "real", "double", "money")
_DATE_TYPES = ("date", "datetime", "time")


def bind(sql: str, values: dict) -> tuple:
    """``... WHERE tdate between :rdate1 and :rdate2`` -> ``?`` + parameters."""
    params: list = []

    def swap(m):
        params.append(values.get(m.group(1)))
        return "?"

    return _ARG_RE.sub(swap, sql), params


def default_for(name: str, kind: str):
    kind = (kind or "").lower()
    if kind in _DATE_TYPES or name.lower().startswith(("rdate", "date")):
        return datetime.date.today()
    if name.lower() in ("rlevel", "level", "control"):
        return 9
    if kind in _NUMERIC_TYPES:
        return 0
    return ""


class GenericDataView(QWidget):
    """The original DataWindow of a screen, running as a real data view."""

    def __init__(self, spec: dict, title: str = "", parent=None):
        super().__init__(parent)
        self.spec = spec or {}
        self.title = title or self.spec.get("dataobject", "Data")
        self._rows: list = []
        self._columns: list = []
        self._param_widgets: dict = {}
        self._build()

    # -- construction ------------------------------------------------------
    def _build(self):
        outer = QVBoxLayout(self)

        args = self.spec.get("args") or []
        types = self.spec.get("arg_types") or {}
        if args:
            box = QGroupBox("Selection")
            row = QHBoxLayout(box)
            for name in args:
                row.addWidget(QLabel(self._arg_label(name)))
                row.addWidget(self._param_widget(name, types.get(name, "")))
            row.addStretch(1)
            outer.addWidget(box)

        actions = QHBoxLayout()
        for caption, slot in (("Run", self.run), ("Export CSV", self._export_csv),
                              ("Export PDF", self._export_pdf)):
            btn = QPushButton(caption)
            btn.clicked.connect(slot)
            actions.addWidget(btn)
        actions.addStretch(1)
        self._status = QLabel()
        self._status.setStyleSheet("color:#4a5a6a;")
        actions.addWidget(self._status)
        outer.addLayout(actions)

        self._grid = QTableWidget(0, 0)
        self._grid.setEditTriggers(QTableWidget.NoEditTriggers)
        self._grid.setSelectionBehavior(QTableWidget.SelectRows)
        outer.addWidget(self._grid, 1)

        self.run()

    def _arg_label(self, name: str) -> str:
        pretty = name[1:] if name.lower().startswith("r") and len(name) > 1 else name
        return pretty.replace("_", " ").title()

    def _param_widget(self, name: str, kind: str) -> QWidget:
        default = default_for(name, kind)
        if isinstance(default, datetime.date):
            w = QDateEdit()
            w.setCalendarPopup(True)
            w.setDisplayFormat("dd-MM-yyyy")
            w.setDate(QDate(default.year, default.month, default.day))
        else:
            w = QLineEdit(str(default))
            w.setMaximumWidth(140)
            w.returnPressed.connect(self.run)
        self._param_widgets[name] = w
        return w

    # -- values ------------------------------------------------------------
    def values(self) -> dict:
        out = {}
        for name, w in self._param_widgets.items():
            if isinstance(w, QDateEdit):
                out[name] = w.date().toString("yyyy-MM-dd")
            else:
                text = w.text().strip()
                out[name] = _as_number(text)
        return out

    # -- running -----------------------------------------------------------
    def run(self):
        sql = self.spec.get("sql", "")
        if not sql:
            self._message("This screen has no query definition.")
            return
        statement, params = bind(sql, self.values())
        try:
            self._rows = db.fetch_all(statement, params)
        except Exception as exc:
            self._rows = []
            self._message(f"Query failed: {exc}")
            return
        self._columns = list(self._rows[0].keys()) if self._rows else \
            [c["name"] for c in self.spec.get("columns", [])]
        self._fill()
        self._status.setText(f"{len(self._rows)} rows")

    def _labels(self) -> list:
        labels = {c["name"].lower(): (c.get("label") or c["name"])
                  for c in self.spec.get("columns", [])}
        return [labels.get(c.lower(), c.replace("_", " ").title())
                for c in self._columns]

    def _numeric_columns(self) -> list:
        typed = {c["name"].lower(): (c.get("type") or "").lower()
                 for c in self.spec.get("columns", [])}
        out = []
        for col in self._columns:
            if any(t in typed.get(col.lower(), "") for t in _NUMERIC_TYPES):
                out.append(col)
        return out

    def _fill(self):
        totals = {c: 0.0 for c in self._numeric_columns()}
        self._grid.clear()
        self._grid.setColumnCount(len(self._columns))
        self._grid.setHorizontalHeaderLabels(self._labels())
        self._grid.setRowCount(len(self._rows) + (1 if totals else 0))
        for r, row in enumerate(self._rows):
            for c, col in enumerate(self._columns):
                value = row.get(col)
                item = QTableWidgetItem("" if value is None else str(value))
                if col in totals:
                    item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    try:
                        totals[col] += float(value or 0)
                    except (TypeError, ValueError):
                        pass
                self._grid.setItem(r, c, item)
        if totals:
            r = len(self._rows)
            for c, col in enumerate(self._columns):
                text = f"{totals[col]:,.2f}" if col in totals else (
                    "TOTAL" if c == 0 else "")
                item = QTableWidgetItem(text)
                font = item.font()
                font.setBold(True)
                item.setFont(font)
                item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                self._grid.setItem(r, c, item)
        self._grid.resizeColumnsToContents()

    def _message(self, text: str):
        self._grid.setRowCount(1)
        self._grid.setColumnCount(1)
        self._grid.setHorizontalHeaderLabels(["info"])
        self._grid.setItem(0, 0, QTableWidgetItem(text))
        self._grid.resizeColumnsToContents()
        self._status.setText("")

    # -- export ------------------------------------------------------------
    def _export_csv(self):
        if not self._rows:
            QMessageBox.information(self, self.title, "Run the query first.")
            return
        path, _ = QFileDialog.getSaveFileName(self, "Export CSV", "report.csv",
                                              "CSV (*.csv)")
        if path:
            export_csv(path, self._columns, self._rows)
            self._status.setText(f"Saved {path}")

    def _export_pdf(self):
        if not self._rows:
            QMessageBox.information(self, self.title, "Run the query first.")
            return
        path, _ = QFileDialog.getSaveFileName(self, "Export PDF", "report.pdf",
                                              "PDF (*.pdf)")
        if path:
            export_pdf(path, self.title, self._columns, self._rows)
            self._status.setText(f"Saved {path}")


def _as_number(text: str):
    try:
        return int(text)
    except ValueError:
        pass
    try:
        return float(text)
    except ValueError:
        return text
