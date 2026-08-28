"""
The refinery screens: issue, returns and all-in-one entry.

``w_refnenter`` issues metal to a refiner, ``w_refnretdocno`` takes the refined
metal back against that issue, and ``w_refinary`` does both on one screen.
Stock moves as the metal moves — see :mod:`app.services.refinery_service`.
"""

from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QComboBox, QGroupBox, QHBoxLayout, QLabel, QLineEdit, QMessageBox,
    QPushButton, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget,
)

import db
from app import modules
from app.services import refinery_service

LINE_COLUMNS = ["code", "qty", "weight", "stonewgt", "stktype"]
RETURN_COLUMNS = ["code", "qty", "weight", "bottlestk", "testpcs", "stktype"]


def _label(text: str) -> QLabel:
    label = QLabel(f"<h3>{text}</h3>")
    label.setTextFormat(Qt.RichText)
    return label


class _LineGrid(QTableWidget):
    """A small editable grid of item lines."""

    def __init__(self, columns: list, rows: int = 6):
        super().__init__(rows, len(columns))
        self.columns = columns
        self.setHorizontalHeaderLabels([c.title() for c in columns])
        self.resizeColumnsToContents()

    def lines(self) -> list:
        out = []
        for r in range(self.rowCount()):
            line = {}
            for c, name in enumerate(self.columns):
                item = self.item(r, c)
                text = item.text().strip() if item else ""
                if name in ("qty", "weight", "stonewgt", "bottlestk", "testpcs"):
                    try:
                        line[name] = float(text) if text else 0
                    except ValueError:
                        raise ValueError(f"'{text}' is not a number "
                                         f"(row {r + 1}, {name})")
                else:
                    line[name] = text
            if line.get("code"):
                out.append(line)
        return out

    def clear_lines(self):
        for r in range(self.rowCount()):
            for c in range(self.columnCount()):
                self.setItem(r, c, QTableWidgetItem(""))


class RefineryIssueForm(QWidget):
    """Issue metal to a refiner (``w_refnenter``)."""

    def __init__(self, parsed=None, parent=None, seed=None):
        super().__init__(parent)
        lay = QVBoxLayout(self)
        lay.addWidget(_label("Refinery — New Issue"))

        head = QHBoxLayout()
        head.addWidget(QLabel("Refiner"))
        self.refiner = QLineEdit()
        self.refiner.setMaximumWidth(160)
        head.addWidget(self.refiner)
        head.addWidget(QLabel("Doc no"))
        self.docno = QLineEdit()
        self.docno.setMaximumWidth(140)
        self.docno.setPlaceholderText("auto")
        head.addWidget(self.docno)
        save = QPushButton("&Issue")
        save.clicked.connect(self.save)
        head.addWidget(save)
        head.addStretch(1)
        self.status = QLabel()
        head.addWidget(self.status)
        lay.addLayout(head)

        box = QGroupBox("Items issued")
        box_lay = QVBoxLayout(box)
        self.grid = _LineGrid(LINE_COLUMNS)
        box_lay.addWidget(self.grid)
        lay.addWidget(box, 1)

    def save(self):
        try:
            slno = refinery_service.issue(self.refiner.text(), self.grid.lines(),
                                          docno=self.docno.text().strip())
        except Exception as exc:
            QMessageBox.warning(self, "Refinery", str(exc))
            return
        self.status.setText(f"Issued — document {slno}.")
        self.grid.clear_lines()


class RefineryReturnForm(QWidget):
    """Take refined metal back against an issue (``w_refnretdocno``)."""

    def __init__(self, parsed=None, parent=None, seed=None):
        super().__init__(parent)
        lay = QVBoxLayout(self)
        lay.addWidget(_label("Refinery — Returns"))

        head = QHBoxLayout()
        head.addWidget(QLabel("Against issue"))
        self.issues = QComboBox()
        self.issues.setMinimumWidth(320)
        head.addWidget(self.issues)
        reload_btn = QPushButton("Refresh")
        reload_btn.clicked.connect(self.refresh)
        head.addWidget(reload_btn)
        save = QPushButton("&Receive")
        save.clicked.connect(self.save)
        head.addWidget(save)
        head.addStretch(1)
        self.status = QLabel()
        head.addWidget(self.status)
        lay.addLayout(head)

        box = QGroupBox("Items received")
        box_lay = QVBoxLayout(box)
        self.grid = _LineGrid(RETURN_COLUMNS)
        box_lay.addWidget(self.grid)
        lay.addWidget(box, 1)
        self.refresh()

        if seed and seed.get("slno"):
            self.select_issue(seed["slno"])

    def refresh(self):
        self._issues = refinery_service.pending_issues()
        self.issues.clear()
        for row in self._issues:
            self.issues.addItem(
                f"{row.get('docno')} — {row.get('tdate')} — "
                f"{row.get('refcode') or ''} — {row.get('issuedwgt') or 0}",
                row["slno"])
        self.status.setText(f"{len(self._issues)} pending issue(s)")

    def select_issue(self, slno):
        index = self.issues.findData(slno)
        if index >= 0:
            self.issues.setCurrentIndex(index)

    def save(self):
        slno = self.issues.currentData()
        if slno is None:
            QMessageBox.information(self, "Refinery", "Choose the issue first.")
            return
        try:
            new = refinery_service.receive(slno, self.grid.lines())
        except Exception as exc:
            QMessageBox.warning(self, "Refinery", str(exc))
            return
        self.status.setText(f"Received — document {new}.")
        self.grid.clear_lines()
        self.refresh()


class RefineryAllInOneForm(QWidget):
    """Issue and return on one screen (``w_refinary``)."""

    def __init__(self, parsed=None, parent=None, seed=None):
        super().__init__(parent)
        lay = QVBoxLayout(self)
        lay.addWidget(_label("Refinery — All in One"))
        self.issue = RefineryIssueForm()
        self.ret = RefineryReturnForm()
        lay.addWidget(self.issue, 1)
        lay.addWidget(self.ret, 1)


modules.register("w_refnenter")(lambda parsed=None, **kw: RefineryIssueForm(parsed))
modules.register("w_refnretdocno")(
    lambda parsed=None, seed=None, **kw: RefineryReturnForm(parsed, seed=seed))
modules.register("w_refinary")(lambda parsed=None, **kw: RefineryAllInOneForm(parsed))
