"""
The cancellation screens.

One screen serves all of them: pick the document, see what it holds, confirm,
and :mod:`app.services.cancel_service` performs the reversal the original
window performed — stock back (or out), barcodes released, the document and its
ledger rows removed, an audit line in ``delpart`` — in a single transaction.
"""

from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QGroupBox, QHBoxLayout, QLabel, QLineEdit, QMessageBox, QPushButton,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget,
)

import db
from app import modules
from app.services import cancel_service

TITLES = {
    "w_scancel": "Cancel Sales Bill",
    "w_sretcancel": "Cancel Sales Return",
    "w_pcancel": "Cancel Purchase",
    "w_gsmthcancel": "Cancel Goldsmith / Jewellery Document",
    "w_ocancel": "Cancel Order",
    "w_rprcancel": "Cancel Repair / Remake Memo",
    "w_oitcancel": "Cancel Other-Item Document",
    "w_refncancel": "Cancel Refinery Document",
    "w_accancel": "Cancel Receipt / Payment / Journal",
    "w_loancancel": "Cancel Loan",
}


class CancelForm(QWidget):
    """Pick a document and cancel it, reversing everything it posted."""

    def __init__(self, window: str, parsed=None, parent=None, seed=None):
        super().__init__(parent)
        self.window_name = window
        self.table, self.key, _handler = cancel_service.HANDLERS[window]
        self._rows: list = []

        lay = QVBoxLayout(self)
        lay.addWidget(QLabel(f"<h3>{TITLES.get(window, 'Cancel Document')}</h3>"))
        lay.addWidget(QLabel(
            "Cancelling reverses the stock, weights and ledger entries this "
            "document posted, then removes it. It cannot be undone."))

        bar = QHBoxLayout()
        bar.addWidget(QLabel("Find"))
        self.search = QLineEdit()
        self.search.setPlaceholderText(f"{self.key} …")
        self.search.setMaximumWidth(220)
        self.search.returnPressed.connect(self.refresh)
        bar.addWidget(self.search)
        find = QPushButton("Search")
        find.clicked.connect(self.refresh)
        bar.addWidget(find)
        cancel = QPushButton("&Cancel Document")
        cancel.setStyleSheet("font-weight:600;")
        cancel.clicked.connect(self.cancel_selected)
        bar.addWidget(cancel)
        bar.addStretch(1)
        self.status = QLabel()
        bar.addWidget(self.status)
        lay.addLayout(bar)

        box = QGroupBox(f"Documents — {self.table}")
        box_lay = QVBoxLayout(box)
        self.grid = QTableWidget(0, 0)
        self.grid.setEditTriggers(QTableWidget.NoEditTriggers)
        self.grid.setSelectionBehavior(QTableWidget.SelectRows)
        self.grid.setSelectionMode(QTableWidget.SingleSelection)
        box_lay.addWidget(self.grid)
        lay.addWidget(box, 1)

        if seed and seed.get("slno"):
            self.search.setText(str(seed.get(self.key) or ""))
        self.refresh()

    # -- data --------------------------------------------------------------
    def _columns(self) -> list:
        names = {c["name"].lower() for c in db.table_columns(self.table)}
        wanted = [c for c in ("slno", self.key, "tdate", "custname", "acname",
                              "name", "netamt", "billamt", "amount", "control")
                  if c in names]
        return wanted or sorted(names)[:6]

    def refresh(self):
        columns = self._columns()
        if not columns:
            self.status.setText(f"Table '{self.table}' is not in this database.")
            return
        sql = f"SELECT {', '.join(columns)} FROM {self.table}"
        params: list = []
        text = self.search.text().strip()
        if text:
            sql += f" WHERE UPPER(CAST({self.key} AS VARCHAR(50))) LIKE ?"
            params = [f"%{text.upper()}%"]
        sql += " ORDER BY slno DESC" if "slno" in columns else ""
        try:
            self._rows = db.fetch_all(sql, params)[:300]
        except Exception as exc:
            self._rows = []
            self.status.setText(f"Could not read {self.table}: {exc}")
            return
        self.grid.clear()
        self.grid.setColumnCount(len(columns))
        self.grid.setHorizontalHeaderLabels(columns)
        self.grid.setRowCount(len(self._rows))
        for r, row in enumerate(self._rows):
            for c, col in enumerate(columns):
                value = row.get(col)
                self.grid.setItem(r, c, QTableWidgetItem(
                    "" if value is None else str(value)))
        self.grid.resizeColumnsToContents()
        self.status.setText(f"{len(self._rows)} document(s)")

    # -- action ------------------------------------------------------------
    def selected(self) -> dict:
        idx = self.grid.currentRow()
        return dict(self._rows[idx]) if 0 <= idx < len(self._rows) else {}

    def cancel_selected(self):
        row = self.selected()
        if not row:
            QMessageBox.information(self, "Cancel", "Select the document first.")
            return
        document = row.get(self.key) or row.get("slno")
        question = (f"Cancel {document}?\n\n"
                    "The stock, weights and ledger entries it posted are "
                    "reversed and the document is removed. This cannot be "
                    "undone.")
        if QMessageBox.question(self, "Cancel document", question,
                                QMessageBox.Yes | QMessageBox.No,
                                QMessageBox.No) != QMessageBox.Yes:
            return
        try:
            result = cancel_service.cancel_document(self.window_name,
                                                    row.get("slno"))
        except Exception as exc:
            QMessageBox.warning(self, "Cancel failed",
                                f"Nothing was changed.\n\n{exc}")
            return
        self.status.setText(result.summary())
        QMessageBox.information(self, "Cancelled", result.summary()
                                + (f"\n{result.note}" if result.note else ""))
        self.refresh()


def _register():
    for window in cancel_service.HANDLERS:
        modules.register(window)(
            lambda parsed=None, seed=None, _w=window, **kw: CancelForm(
                _w, parsed, seed=seed))


_register()
