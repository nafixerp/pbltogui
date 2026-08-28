"""
Kuri / Scheme collection screen (Phase 4) — conversion of GMINE ``w_kuricolln``.

Header (receipt no / date / member / gold rate), an amount entry that converts
to gold weight live (weight = amount / rate), and the member's collection ledger
with running totals. Saving records the ``kuricolln`` row and posts a cash
receipt to the day book (Dr Cash, Cr Kuri). Math from
:mod:`app.services.kuri_service`; persistence from
:mod:`app.repositories.kuri_repository`.
"""

from __future__ import annotations

import datetime

from PySide6.QtGui import QDoubleValidator
from PySide6.QtWidgets import (
    QComboBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QMessageBox, QPushButton, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget,
)

from app import modules
from app.services.kuri_service import installment_weight, summarise
from app.repositories import kuri_repository as repo

LEDGER_COLS = ["rcptno", "tdate", "sno", "amount", "grate", "wgt", "note"]


class KuriCollectionForm(QWidget):
    def __init__(self, window=None, parent=None):
        super().__init__(parent)
        repo.ensure_schema()
        self._build()
        self._new()

    def _build(self):
        root = QVBoxLayout(self)
        title = QLabel("Kuri / Scheme Collection")
        title.setStyleSheet("font-size:16px;font-weight:700;padding:4px;")
        root.addWidget(title)

        box = QGroupBox("Collection")
        grid = QGridLayout(box)
        self.ed_rcptno = QLineEdit(); self.ed_rcptno.setReadOnly(True)
        self.ed_date = QLineEdit()
        self.cb_member = QComboBox(); self.cb_member.setEditable(True)
        for m in repo.list_members():
            self.cb_member.addItem(f"{m['code']} - {m.get('name','')}", m['code'])
        self.cb_member.currentIndexChanged.connect(self._member_changed)
        self.ed_rate = QLineEdit("6000")
        self.ed_amount = QLineEdit()
        self.ed_amount.setValidator(QDoubleValidator(0, 1e12, 2))
        self.lbl_wgt = QLabel("0.000")
        self.ed_note = QLineEdit()
        self.ed_rate.textChanged.connect(self._recalc)
        self.ed_amount.textChanged.connect(self._recalc)

        grid.addWidget(QLabel("Receipt No"), 0, 0); grid.addWidget(self.ed_rcptno, 0, 1)
        grid.addWidget(QLabel("Date"), 0, 2); grid.addWidget(self.ed_date, 0, 3)
        grid.addWidget(QLabel("Member"), 1, 0); grid.addWidget(self.cb_member, 1, 1, 1, 3)
        grid.addWidget(QLabel("Gold Rate"), 2, 0); grid.addWidget(self.ed_rate, 2, 1)
        grid.addWidget(QLabel("Amount"), 2, 2); grid.addWidget(self.ed_amount, 2, 3)
        grid.addWidget(QLabel("Weight (g)"), 2, 4); grid.addWidget(self.lbl_wgt, 2, 5)
        grid.addWidget(QLabel("Note"), 3, 0); grid.addWidget(self.ed_note, 3, 1, 1, 5)
        root.addWidget(box)

        btns = QHBoxLayout()
        save = QPushButton("Save Collection"); save.clicked.connect(self._save)
        new = QPushButton("New"); new.clicked.connect(self._new)
        btns.addWidget(save); btns.addWidget(new); btns.addStretch(1)
        root.addLayout(btns)

        led = QGroupBox("Member Ledger")
        llay = QVBoxLayout(led)
        self.grid = QTableWidget(0, 0)
        self.grid.setEditTriggers(QTableWidget.NoEditTriggers)
        llay.addWidget(self.grid)
        self.lbl_summary = QLabel("0 installments")
        self.lbl_summary.setStyleSheet("font-weight:700;")
        llay.addWidget(self.lbl_summary)
        root.addWidget(led, 1)

    # -- behaviour ---------------------------------------------------------
    def _gold_scheme(self) -> bool:
        code = self.cb_member.currentData()
        return repo.is_gold_scheme(code) if code else True

    def _recalc(self):
        wgt = installment_weight(self.ed_amount.text() or 0, self.ed_rate.text() or 0,
                                 self._gold_scheme())
        self.lbl_wgt.setText(f"{wgt}")

    def _member_changed(self):
        self._recalc()
        self._load_ledger()

    def _load_ledger(self):
        code = self.cb_member.currentData()
        rows = repo.member_ledger(code) if code else []
        self.grid.setColumnCount(len(LEDGER_COLS))
        self.grid.setHorizontalHeaderLabels(LEDGER_COLS)
        self.grid.setRowCount(len(rows))
        for r, row in enumerate(rows):
            for c, col in enumerate(LEDGER_COLS):
                val = row.get(col)
                self.grid.setItem(r, c, QTableWidgetItem("" if val is None else str(val)))
        self.grid.resizeColumnsToContents()
        s = summarise(rows)
        self.lbl_summary.setText(
            f"{s.installments} installments   |   Amount {s.total_amount:.2f}   "
            f"|   Weight {s.total_weight} g")

    # -- actions -----------------------------------------------------------
    def _new(self):
        self.ed_date.setText(str(datetime.date.today()))
        self.ed_rcptno.setText("(auto)")
        self.ed_amount.clear(); self.ed_note.clear()
        self._recalc(); self._load_ledger()

    def _save(self):
        code = self.cb_member.currentData()
        if not code:
            QMessageBox.warning(self, "Kuri", "Select a member.")
            return
        amount = self.ed_amount.text().strip()
        if not amount or float(amount) <= 0:
            QMessageBox.warning(self, "Kuri", "Enter a positive amount.")
            return
        wgt = installment_weight(amount, self.ed_rate.text() or 0, self._gold_scheme())
        try:
            rcptno = repo.save_collection(
                code, self.cb_member.currentText(), self.ed_date.text().strip(),
                amount, self.ed_rate.text() or 0, wgt, self.ed_note.text().strip())
        except Exception as exc:
            QMessageBox.critical(self, "Kuri", f"Save failed: {exc}")
            return
        self.ed_rcptno.setText(rcptno)
        QMessageBox.information(self, "Kuri", f"Saved collection {rcptno}.")
        self.ed_amount.clear()
        self._load_ledger()


def _factory(window):
    return KuriCollectionForm(window)


modules.register("w_kuricolln")(_factory)
