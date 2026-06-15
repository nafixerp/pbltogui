"""
Accounting voucher screen (Phase 4) — conversion of GMINE ``w_rcpt`` (Receipt),
``w_pmnt`` (Payment) and ``w_journal`` (Journal).

One double-entry voucher form serves all three, pre-wired per voucher type:

  * Receipt  — debit Cash/Bank, credit the party (money in)
  * Payment  — credit Cash/Bank, debit the party (money out)
  * Journal  — free debit/credit selection

Posting goes through :mod:`app.services.accounting_service` (balanced rows) and
:mod:`app.repositories.accounting_repository` (writes ``daybook`` +
``daybookpart``). A live day-book grid and the running balance of each selected
account are shown.
"""

from __future__ import annotations

import datetime

from PySide6.QtWidgets import (
    QComboBox, QFormLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QMessageBox, QPlainTextEdit, QPushButton, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget,
)
from PySide6.QtGui import QDoubleValidator

from app import modules
from app.services import accounting_service as acc
from app.repositories import accounting_repository as repo


class AccountingVoucherForm(QWidget):
    def __init__(self, control: str = acc.JOURNAL, window=None, parent=None):
        super().__init__(parent)
        self.control = control
        repo.ensure_schema()
        self.accounts = repo.list_accounts()
        self._build()
        self._refresh_daybook()
        self._apply_type_defaults()

    # -- layout ------------------------------------------------------------
    def _build(self):
        root = QVBoxLayout(self)
        self.title = QLabel()
        self.title.setStyleSheet("font-size:16px;font-weight:700;padding:4px;")
        root.addWidget(self.title)

        entry = QGroupBox("Voucher")
        form = QFormLayout(entry)
        self.cb_type = QComboBox()
        for code in (acc.RECEIPT, acc.PAYMENT, acc.JOURNAL):
            self.cb_type.addItem(acc.VOUCHER_LABELS[code], code)
        self.cb_type.setCurrentIndex(
            [acc.RECEIPT, acc.PAYMENT, acc.JOURNAL].index(self.control))
        self.cb_type.currentIndexChanged.connect(self._type_changed)

        self.ed_date = QLineEdit(str(datetime.date.today()))
        self.cb_debit = self._account_combo()
        self.cb_credit = self._account_combo()
        self.ed_amount = QLineEdit()
        self.ed_amount.setValidator(QDoubleValidator(0, 1e12, 2))
        self.ed_narration = QPlainTextEdit()
        self.ed_narration.setMaximumHeight(60)

        self.cb_debit.currentIndexChanged.connect(self._update_balances)
        self.cb_credit.currentIndexChanged.connect(self._update_balances)

        form.addRow("Type", self.cb_type)
        form.addRow("Date", self.ed_date)
        form.addRow("Debit A/c", self.cb_debit)
        form.addRow("Credit A/c", self.cb_credit)
        form.addRow("Amount", self.ed_amount)
        form.addRow("Narration", self.ed_narration)
        self.lbl_balances = QLabel()
        form.addRow("Balances", self.lbl_balances)
        root.addWidget(entry)

        btns = QHBoxLayout()
        post = QPushButton("Post Voucher"); post.clicked.connect(self._post)
        clear = QPushButton("Clear"); clear.clicked.connect(self._clear)
        btns.addWidget(post); btns.addWidget(clear); btns.addStretch(1)
        root.addLayout(btns)

        book = QGroupBox("Day Book (latest)")
        blay = QVBoxLayout(book)
        self.grid = QTableWidget(0, 0)
        self.grid.setEditTriggers(QTableWidget.NoEditTriggers)
        blay.addWidget(self.grid)
        root.addWidget(book, 1)

    def _account_combo(self) -> QComboBox:
        cb = QComboBox()
        for a in self.accounts:
            cb.addItem(f"{a['accode']} - {a['name']}", a["accode"])
        return cb

    def _select_account(self, combo: QComboBox, accode: str):
        idx = combo.findData(accode)
        if idx >= 0:
            combo.setCurrentIndex(idx)

    # -- voucher-type behaviour -------------------------------------------
    def _type_changed(self):
        self.control = self.cb_type.currentData()
        self._apply_type_defaults()

    def _apply_type_defaults(self):
        self.title.setText(f"{acc.VOUCHER_LABELS[self.control]} Voucher")
        # Receipt: money into Cash; Payment: money out of Cash.
        if self.control == acc.RECEIPT:
            self._select_account(self.cb_debit, "CASH")
            self._select_account(self.cb_credit, "SUNDRD")
        elif self.control == acc.PAYMENT:
            self._select_account(self.cb_credit, "CASH")
            self._select_account(self.cb_debit, "SUNDRC")
        self._update_balances()

    def _update_balances(self):
        d = self.cb_debit.currentData()
        c = self.cb_credit.currentData()
        db_bal = repo.account_balance(d) if d else 0
        cr_bal = repo.account_balance(c) if c else 0
        self.lbl_balances.setText(f"{d}: {float(db_bal):,.2f}   |   "
                                  f"{c}: {float(cr_bal):,.2f}")

    # -- actions -----------------------------------------------------------
    def _post(self):
        try:
            amount = self.ed_amount.text().strip()
            slno = repo.post_voucher(
                tdate=self.ed_date.text().strip(),
                debit=self.cb_debit.currentData(),
                credit=self.cb_credit.currentData(),
                amount=amount or 0,
                control=self.control,
                narration=self.ed_narration.toPlainText().strip())
        except ValueError as ve:
            QMessageBox.warning(self, "Voucher", str(ve))
            return
        except Exception as exc:
            QMessageBox.critical(self, "Voucher", f"Post failed: {exc}")
            return
        QMessageBox.information(self, "Voucher",
                               f"Posted {acc.VOUCHER_LABELS[self.control]} #{slno}.")
        self._clear()
        self._refresh_daybook()
        self._update_balances()

    def _clear(self):
        self.ed_amount.clear()
        self.ed_narration.clear()
        self.ed_date.setText(str(datetime.date.today()))

    def _refresh_daybook(self):
        rows = repo.list_daybook()
        cols = ["slno", "tdate", "accode", "amount", "control", "opaccode"]
        self.grid.setColumnCount(len(cols))
        self.grid.setHorizontalHeaderLabels(cols)
        self.grid.setRowCount(len(rows))
        for r, row in enumerate(rows):
            for c, col in enumerate(cols):
                val = row.get(col)
                self.grid.setItem(r, c, QTableWidgetItem(
                    "" if val is None else str(val)))
        self.grid.resizeColumnsToContents()


def _factory(control):
    def factory(window):
        return AccountingVoucherForm(control=control, window=window)
    return factory


modules.register("w_rcpt")(_factory(acc.RECEIPT))
modules.register("w_pmnt")(_factory(acc.PAYMENT))
modules.register("w_journal")(_factory(acc.JOURNAL))
