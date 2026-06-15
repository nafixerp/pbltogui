"""
Render a parsed DataWindow (.srd) as a live Qt grid.

A PowerBuilder DataWindow is a combined data control + visual layout.  Here we
reproduce the two things that matter for the port:

* the **columns** (names, headings, order) exactly as designed, and
* the **data**, retrieved through the real ``retrieve`` SQL against the live
  database when possible.

If the SQL cannot run (e.g. running on SQLite without the ERP tables, or a
PBSELECT we could not fully translate) the grid still shows the correct column
structure, so every screen is faithful to the original design.
"""

from __future__ import annotations

from PySide6.QtCore import Qt, QAbstractTableModel, QModelIndex
from PySide6.QtWidgets import QTableView, QHeaderView

from pbconvert import parse_datawindow
from pbconvert.source import PBSource


class _TableModel(QAbstractTableModel):
    def __init__(self, headings, rows):
        super().__init__()
        self._headings = headings
        self._rows = rows

    def rowCount(self, parent=QModelIndex()):
        return len(self._rows)

    def columnCount(self, parent=QModelIndex()):
        return len(self._headings)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None
        if role in (Qt.DisplayRole, Qt.EditRole):
            row = self._rows[index.row()]
            if index.column() < len(row):
                val = row[index.column()]
                return "" if val is None else str(val)
        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role != Qt.DisplayRole:
            return None
        if orientation == Qt.Horizontal:
            return self._headings[section] if section < len(self._headings) else ""
        return section + 1

    def setRows(self, rows):
        self.beginResetModel()
        self._rows = rows
        self.endResetModel()


class DataWindowView(QTableView):
    """A QTableView backed by a parsed DataWindow definition."""

    def __init__(self, dw_name: str, source: PBSource, parent=None):
        super().__init__(parent)
        self.dw_name = dw_name
        self.source = source
        self.dw = None
        self.status = ""

        headings, names = ["(datawindow)"], []
        try:
            self.dw = parse_datawindow(source.text(dw_name), dw_name)
            cols = sorted(self.dw.columns, key=lambda c: c.order)
            headings = [c.heading or c.name for c in cols] or ["(no columns)"]
            names = [c.name for c in cols]
        except Exception as exc:           # pragma: no cover - defensive
            self.status = f"parse error: {exc}"

        self._names = names
        self._model = _TableModel(headings, [])
        self.setModel(self._model)
        self.setAlternatingRowColors(True)
        self.setSelectionBehavior(QTableView.SelectRows)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        self.horizontalHeader().setStretchLastSection(True)
        self.setEditTriggers(QTableView.NoEditTriggers)

    # -- data -------------------------------------------------------------
    def retrieve(self, *args) -> int:
        """Run the DataWindow's SQL and load rows.  Returns the row count."""
        if not self.dw or not self.dw.retrieve_sql:
            self.status = "no retrieve SQL"
            return 0
        try:
            from runtime import db
            rows = db.fetch_all(self.dw.retrieve_sql)
        except Exception as exc:
            self.status = f"retrieve failed: {exc}"
            return 0

        if self._names:
            data = [[r.get(n) for n in self._names] for r in rows]
        else:
            data = [list(r.values()) for r in rows]
        self._model.setRows(data)
        self.status = f"{len(data)} row(s)"
        return len(data)

    def row_count(self) -> int:
        return self._model.rowCount()
