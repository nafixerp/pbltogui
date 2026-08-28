"""
Master-data business logic (Phase 4).

A reusable, fully working CRUD screen for simple master tables: it introspects
the connected database for the table's columns, lists existing rows, and
supports Add / Save / Delete with the original PowerBuilder data-toolbar feel.

Because it introspects columns at runtime it adapts to the actual database in
``db_config.ini`` (SQL Anywhere, SQL Server or the bundled SQLite test schema),
so the same screen is correct whether pointed at the seeded demo tables or the
production ERP database.
"""

from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFormLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit, QMessageBox,
    QPushButton, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget,
)

from app import modules
import db


def table_columns(table: str) -> list[str]:
    """Return column names for *table* across engines."""
    try:
        if db.ENGINE == "sqlite":
            rows = db.fetch_all(f"PRAGMA table_info({table})")
            return [r["name"] for r in rows]
        # Generic: ask for an empty result and read the cursor description.
        conn = db.get_connection()
        try:
            cur = conn.cursor()
            cur.execute(f"SELECT * FROM {table} WHERE 1=0")
            return [d[0] for d in cur.description]
        finally:
            conn.close()
    except Exception:
        return []


class MasterCRUDForm(QWidget):
    """Generic master editor for a single table with a code/PK column."""

    def __init__(self, title: str, table: str, pk: str, parent=None):
        super().__init__(parent)
        self.title = title
        self.table = table
        self.pk = pk
        self.columns = table_columns(table)
        self.editors: dict[str, QLineEdit] = {}
        self._build()
        self._reload()

    def _build(self):
        layout = QVBoxLayout(self)
        header = QLabel(self.title)
        header.setStyleSheet("font-size:15px;font-weight:600;padding:6px;")
        layout.addWidget(header)

        edit_box = QGroupBox("Entry")
        form = QFormLayout(edit_box)
        editable = [c for c in self.columns] or [self.pk, "name"]
        for col in editable:
            le = QLineEdit()
            self.editors[col] = le
            form.addRow(col, le)
        layout.addWidget(edit_box)

        buttons = QHBoxLayout()
        for label, slot in (("Add / New", self._clear), ("Save", self._save),
                            ("Delete", self._delete)):
            b = QPushButton(label)
            b.clicked.connect(slot)
            buttons.addWidget(b)
        buttons.addStretch(1)
        layout.addLayout(buttons)

        self.grid = QTableWidget(0, 0)
        self.grid.setEditTriggers(QTableWidget.NoEditTriggers)
        self.grid.setSelectionBehavior(QTableWidget.SelectRows)
        self.grid.cellClicked.connect(self._row_selected)
        layout.addWidget(self.grid, 1)

    def _reload(self):
        try:
            rows = db.fetch_all(f"SELECT * FROM {self.table}")
        except Exception as exc:
            QMessageBox.warning(self, self.title, f"Cannot read {self.table}: {exc}")
            rows = []
        self._rows = rows
        cols = self.columns or (list(rows[0].keys()) if rows else [])
        self.grid.setColumnCount(len(cols))
        self.grid.setHorizontalHeaderLabels(cols)
        self.grid.setRowCount(len(rows))
        for r, row in enumerate(rows):
            for c, col in enumerate(cols):
                self.grid.setItem(r, c, QTableWidgetItem(
                    "" if row.get(col) is None else str(row.get(col))))
        self.grid.resizeColumnsToContents()

    def _row_selected(self, row, _col):
        if 0 <= row < len(self._rows):
            data = self._rows[row]
            for col, le in self.editors.items():
                le.setText("" if data.get(col) is None else str(data.get(col)))

    def _clear(self):
        for le in self.editors.values():
            le.clear()

    def _values(self) -> dict:
        return {c: (le.text().strip() or None) for c, le in self.editors.items()
                if c.lower() not in ("",) and not c.lower().endswith("_id")}

    def _save(self):
        vals = self._values()
        key = self.editors.get(self.pk)
        if key is None or not key.text().strip():
            QMessageBox.warning(self, self.title, f"{self.pk} is required.")
            return
        keyval = key.text().strip()
        try:
            exists = db.fetch_one(
                f"SELECT 1 AS x FROM {self.table} WHERE {self.pk} = ?", (keyval,))
            if exists:
                sets = [c for c in vals if c != self.pk]
                db.execute(
                    f"UPDATE {self.table} SET " + ", ".join(f"{c}=?" for c in sets) +
                    f" WHERE {self.pk}=?",
                    tuple(vals[c] for c in sets) + (keyval,))
            else:
                cols = list(vals.keys())
                db.execute(
                    f"INSERT INTO {self.table} ({', '.join(cols)}) VALUES "
                    f"({', '.join('?' for _ in cols)})",
                    tuple(vals[c] for c in cols))
        except Exception as exc:
            QMessageBox.critical(self, self.title, f"Save failed: {exc}")
            return
        self._reload()
        QMessageBox.information(self, self.title, "Saved.")

    def _delete(self):
        key = self.editors.get(self.pk)
        if key is None or not key.text().strip():
            return
        if QMessageBox.question(self, self.title,
                                f"Delete {key.text().strip()}?") != QMessageBox.Yes:
            return
        try:
            db.execute(f"DELETE FROM {self.table} WHERE {self.pk}=?",
                       (key.text().strip(),))
        except Exception as exc:
            QMessageBox.critical(self, self.title, f"Delete failed: {exc}")
            return
        self._clear()
        self._reload()


# -- register seeded master windows -----------------------------------------
# These map PowerBuilder master windows to the working CRUD screen. The bundled
# SQLite schema (db.py) provides the demo tables; pointed at the production DB
# the same screens edit the real tables.
_SEEDED = {
    "w_itemgrp": ("Item Group Details", "category_master", "code"),
    "w_item": ("Item Details", "item_master", "code"),
    "w_sucu": ("Customer / Supplier", "customer_master", "code"),
    "w_smith": ("Goldsmith / Jewellery", "smith_master", "code"),
    "w_salestype": ("Bill Type", "tax_master", "code"),
}


def _make_factory(title, table, pk):
    def factory(window):  # window (parsed) is accepted but not required here
        return MasterCRUDForm(title, table, pk)
    return factory


for _win, (_title, _table, _pk) in _SEEDED.items():
    modules.register(_win)(_make_factory(_title, _table, _pk))
