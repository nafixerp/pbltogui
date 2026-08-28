"""
Order entry screen (Phase 4) — business-logic conversion of GMINE ``w_order``.

Header (order no / date / due date / customer / tax%), an editable item grid
(same jewellery line math as sales), and an advance/exchange panel that shows the
order balance live (balance = grand total − exchange − advance). Math from
:mod:`app.services.order_service`; persistence from
:mod:`app.repositories.order_repository`.
"""

from __future__ import annotations

import datetime
from decimal import Decimal

from PySide6.QtCore import Qt
from PySide6.QtGui import QDoubleValidator
from PySide6.QtWidgets import (
    QCheckBox, QComboBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMessageBox, QPushButton, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget,
)

from app import modules
from app.services.order_service import OrderLine, compute_order
from app.services.sales_service import D
from app.repositories import order_repository as repo

COLS = [
    ("Item Code", "code", True), ("Description", "name", True),
    ("Qty", "qty", True), ("Gross Wt", "weight", True),
    ("Stone Wt", "stone_wgt", True), ("Stone Price", "stone_price", True),
    ("Wastage(g)", "wastage", True), ("Making", "making", True),
    ("Rate", "rate", True), ("Net Wt", "net_wgt", False),
    ("Amount", "amount", False),
]


class OrderForm(QWidget):
    def __init__(self, window=None, parent=None):
        super().__init__(parent)
        repo.ensure_schema()
        self._build()
        self._new_order()

    def _build(self):
        root = QVBoxLayout(self)
        title = QLabel("Order Entry")
        title.setStyleSheet("font-size:16px;font-weight:700;padding:4px;")
        root.addWidget(title)
        root.addWidget(self._header_card())
        root.addWidget(self._line_grid(), 1)
        root.addLayout(self._bottom_row())

    def _header_card(self) -> QWidget:
        box = QGroupBox("Order")
        grid = QGridLayout(box)
        self.ed_ordno = QLineEdit(); self.ed_ordno.setReadOnly(True)
        self.ed_date = QLineEdit()
        self.ed_due = QLineEdit()
        self.cb_cust = QComboBox(); self.cb_cust.setEditable(True)
        for c in repo.list_customers():
            self.cb_cust.addItem(f"{c['code']} - {c['name']}", c['code'])
        self.ed_taxperc = QLineEdit("3")
        self.ed_taxperc.setValidator(QDoubleValidator(0, 100, 2))
        self.chk_interstate = QCheckBox("Inter-state (IGST)")

        grid.addWidget(QLabel("Order No"), 0, 0); grid.addWidget(self.ed_ordno, 0, 1)
        grid.addWidget(QLabel("Date"), 0, 2); grid.addWidget(self.ed_date, 0, 3)
        grid.addWidget(QLabel("Due Date"), 0, 4); grid.addWidget(self.ed_due, 0, 5)
        grid.addWidget(QLabel("Customer"), 1, 0); grid.addWidget(self.cb_cust, 1, 1, 1, 3)
        grid.addWidget(QLabel("Tax %"), 1, 4); grid.addWidget(self.ed_taxperc, 1, 5)
        grid.addWidget(self.chk_interstate, 2, 1)

        self.ed_taxperc.textChanged.connect(self._recompute)
        self.chk_interstate.toggled.connect(self._recompute)
        return box

    def _line_grid(self) -> QWidget:
        box = QGroupBox("Items")
        lay = QVBoxLayout(box)
        self.table = QTableWidget(0, len(COLS))
        self.table.setHorizontalHeaderLabels([c[0] for c in COLS])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.itemChanged.connect(lambda _i: self._recompute())
        lay.addWidget(self.table)
        btns = QHBoxLayout()
        add = QPushButton("Add Line"); add.clicked.connect(lambda: self._add_row())
        rm = QPushButton("Remove Line"); rm.clicked.connect(self._remove_row)
        btns.addWidget(add); btns.addWidget(rm); btns.addStretch(1)
        lay.addLayout(btns)
        return box

    def _bottom_row(self) -> QHBoxLayout:
        row = QHBoxLayout()
        totals = QGroupBox("Totals")
        form = QFormLayout(totals)
        self.lbl_gross = QLabel("0.00"); self.lbl_tax = QLabel("0.00")
        self.lbl_total = QLabel("0.00")
        self.ed_advance = QLineEdit("0"); self.ed_advance.setValidator(QDoubleValidator(0, 1e12, 2))
        self.ed_exchange = QLineEdit("0"); self.ed_exchange.setValidator(QDoubleValidator(0, 1e12, 2))
        self.lbl_balance = QLabel("0.00")
        self.lbl_total.setStyleSheet("font-weight:700;")
        self.lbl_balance.setStyleSheet("font-weight:700;font-size:14px;color:#1f3a5f;")
        self.ed_advance.textChanged.connect(self._recompute)
        self.ed_exchange.textChanged.connect(self._recompute)
        form.addRow("Gross", self.lbl_gross)
        form.addRow("Tax", self.lbl_tax)
        form.addRow("Grand Total", self.lbl_total)
        form.addRow("Exchange", self.ed_exchange)
        form.addRow("Advance", self.ed_advance)
        form.addRow("Balance", self.lbl_balance)
        row.addWidget(totals)
        actions = QVBoxLayout()
        for label, slot in (("New", self._new_order), ("Save", self._save),
                            ("Reload", self._reload)):
            b = QPushButton(label); b.clicked.connect(slot); actions.addWidget(b)
        actions.addStretch(1)
        row.addLayout(actions)
        return row

    # -- grid --------------------------------------------------------------
    def _add_row(self, line: OrderLine | None = None):
        self.table.blockSignals(True)
        r = self.table.rowCount(); self.table.insertRow(r)
        line = line or OrderLine()
        for c, (_l, attr, editable) in enumerate(COLS):
            val = getattr(line, attr)
            item = QTableWidgetItem("" if val in (None, "") else str(val))
            if not editable:
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                item.setBackground(Qt.lightGray)
            self.table.setItem(r, c, item)
        self.table.blockSignals(False)
        self._recompute()

    def _remove_row(self):
        r = self.table.currentRow()
        if r >= 0:
            self.table.removeRow(r); self._recompute()

    def _row_to_line(self, r: int) -> OrderLine:
        def cell(c):
            it = self.table.item(r, c)
            return it.text().strip() if it else ""
        idx = {attr: i for i, (_l, attr, _e) in enumerate(COLS)}
        return OrderLine(
            code=cell(idx["code"]), name=cell(idx["name"]),
            qty=D(cell(idx["qty"]) or 1), weight=D(cell(idx["weight"])),
            stone_wgt=D(cell(idx["stone_wgt"])), stone_price=D(cell(idx["stone_price"])),
            wastage=D(cell(idx["wastage"])), making=D(cell(idx["making"])),
            rate=D(cell(idx["rate"])))

    def _collect_lines(self) -> list[OrderLine]:
        out = []
        for r in range(self.table.rowCount()):
            ln = self._row_to_line(r)
            if ln.code or ln.weight or ln.amount:
                out.append(ln.compute())
        return out

    def _recompute(self):
        self.table.blockSignals(True)
        idx = {attr: i for i, (_l, attr, _e) in enumerate(COLS)}
        for r in range(self.table.rowCount()):
            ln = self._row_to_line(r).compute()
            self.table.item(r, idx["net_wgt"]).setText(f"{ln.net_wgt}")
            self.table.item(r, idx["amount"]).setText(f"{ln.amount}")
        self.table.blockSignals(False)

        lines = self._collect_lines()
        try:
            tax_perc = D(self.ed_taxperc.text() or 0)
        except Exception:
            tax_perc = Decimal("0")
        t = compute_order(lines, tax_perc=tax_perc,
                          interstate=self.chk_interstate.isChecked(),
                          advance=D(self.ed_advance.text() or 0),
                          exchange=D(self.ed_exchange.text() or 0))
        self._totals = t
        self.lbl_gross.setText(f"{t.bill.gross:.2f}")
        self.lbl_tax.setText(f"{t.bill.tax_amount:.2f}")
        self.lbl_total.setText(f"{t.bill.grand_total:.2f}")
        self.lbl_balance.setText(f"{t.balance:.2f}")

    # -- actions -----------------------------------------------------------
    def _new_order(self):
        self.table.setRowCount(0)
        self.ed_date.setText(str(datetime.date.today()))
        self.ed_due.setText(str(datetime.date.today() + datetime.timedelta(days=7)))
        self.ed_ordno.setText(repo.next_ordno("O"))
        self.ed_advance.setText("0"); self.ed_exchange.setText("0")
        self._add_row(); self._recompute()

    def _save(self):
        lines = self._collect_lines()
        if not lines:
            QMessageBox.warning(self, "Order", "Add at least one item line.")
            return
        t = self._totals
        header = {
            "ordno": self.ed_ordno.text(), "tdate": self.ed_date.text(),
            "duedate": self.ed_due.text(), "custcode": self.cb_cust.currentData() or "",
            "custname": self.cb_cust.currentText(), "taxperc": str(self.ed_taxperc.text() or 0),
            "interstate": self.chk_interstate.isChecked(),
            "billamt": t.bill.grand_total, "exchange": t.exchange,
            "advance": t.advance, "balance": t.balance,
        }
        try:
            ordno = repo.save_order(header, lines)
        except Exception as exc:
            QMessageBox.critical(self, "Order", f"Save failed: {exc}")
            return
        QMessageBox.information(self, "Order", f"Saved order {ordno}.")

    def _reload(self):
        ordno = self.ed_ordno.text().strip()
        head, lines = repo.load_order(ordno)
        if not head:
            QMessageBox.information(self, "Order", f"No saved order {ordno}.")
            return
        self.table.setRowCount(0)
        for ln in lines:
            self._add_row(ln)
        self.ed_taxperc.setText(str(head.get("taxperc", 0)))
        self.chk_interstate.setChecked(str(head.get("interstate")) == "Y")
        self.ed_advance.setText(str(head.get("advance", 0)))
        self.ed_exchange.setText(str(head.get("eamt", 0)))
        self.ed_due.setText(str(head.get("duedate", "")))
        self._recompute()


def _factory(window):
    return OrderForm(window)


modules.register("w_order")(_factory)
