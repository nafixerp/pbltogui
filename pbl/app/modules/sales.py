"""
Sales billing screen (Phase 4) — business-logic conversion of GMINE ``w_sales``.

A real billing form rather than a generic table editor: a header card
(customer / bill no / date / bill type / tax%), an editable line grid that
recomputes net weight, value-add and amount live as you type, a totals panel
with the CGST/SGST/IGST split and round-off, and New / Save / Reload actions.

Calculations come from :mod:`app.services.sales_service` (faithful port of the
PowerBuilder math); persistence from :mod:`app.repositories.sales_repository`.
"""

from __future__ import annotations

from decimal import Decimal

from PySide6.QtCore import Qt
from PySide6.QtGui import QDoubleValidator
from PySide6.QtWidgets import (
    QCheckBox, QComboBox, QFileDialog, QFormLayout, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit, QMessageBox, QPushButton,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget,
)

from app import modules
from app.services.sales_service import SalesLine, compute_bill, D, rnd
from app.repositories import sales_repository as repo

# Editable line columns (label, attribute, editable?)
COLS = [
    ("Item Code", "code", True), ("Description", "name", True),
    ("Qty", "qty", True), ("Gross Wt", "weight", True),
    ("Stone Wt", "stone_wgt", True), ("Stone Price", "stone_price", True),
    ("Wastage(g)", "wastage", True), ("Making", "making", True),
    ("Rate", "rate", True), ("Net Wt", "net_wgt", False),
    ("Amount", "amount", False),
]


class SalesBillingForm(QWidget):
    def __init__(self, window=None, parent=None):
        super().__init__(parent)
        repo.ensure_schema()
        self._build()
        self._new_bill()

    # -- layout ------------------------------------------------------------
    def _build(self):
        root = QVBoxLayout(self)
        title = QLabel("Sales Billing")
        title.setStyleSheet("font-size:16px;font-weight:700;padding:4px;")
        root.addWidget(title)

        root.addWidget(self._header_card())
        root.addWidget(self._line_grid(), 1)
        root.addLayout(self._bottom_row())

    def _header_card(self) -> QWidget:
        box = QGroupBox("Bill")
        grid = QGridLayout(box)

        self.ed_billno = QLineEdit(); self.ed_billno.setReadOnly(True)
        self.ed_date = QLineEdit()
        self.cb_type = QComboBox(); self.cb_type.addItems(["S", "E"])
        self.cb_type.setToolTip("S = Bill, E = Estimate")
        self.cb_cust = QComboBox(); self.cb_cust.setEditable(True)
        for c in repo.list_customers():
            self.cb_cust.addItem(f"{c['code']} - {c['name']}", c['code'])
        self.ed_taxperc = QLineEdit("3")
        self.ed_taxperc.setValidator(QDoubleValidator(0, 100, 2))
        self.chk_interstate = QCheckBox("Inter-state (IGST)")
        self.chk_inclusive = QCheckBox("Tax inclusive")

        grid.addWidget(QLabel("Bill No"), 0, 0); grid.addWidget(self.ed_billno, 0, 1)
        grid.addWidget(QLabel("Date"), 0, 2); grid.addWidget(self.ed_date, 0, 3)
        grid.addWidget(QLabel("Type"), 0, 4); grid.addWidget(self.cb_type, 0, 5)
        grid.addWidget(QLabel("Customer"), 1, 0); grid.addWidget(self.cb_cust, 1, 1, 1, 3)
        grid.addWidget(QLabel("Tax %"), 1, 4); grid.addWidget(self.ed_taxperc, 1, 5)
        grid.addWidget(self.chk_interstate, 2, 1)
        grid.addWidget(self.chk_inclusive, 2, 2)

        for w in (self.ed_taxperc,):
            w.textChanged.connect(self._recompute)
        self.chk_interstate.toggled.connect(self._recompute)
        self.chk_inclusive.toggled.connect(self._recompute)
        return box

    def _line_grid(self) -> QWidget:
        box = QGroupBox("Items")
        lay = QVBoxLayout(box)
        self.table = QTableWidget(0, len(COLS))
        self.table.setHorizontalHeaderLabels([c[0] for c in COLS])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.itemChanged.connect(self._cell_changed)
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
        self.lbl_gross = QLabel("0.00")
        self.lbl_taxable = QLabel("0.00")
        self.lbl_cgst = QLabel("0.00")
        self.lbl_sgst = QLabel("0.00")
        self.lbl_igst = QLabel("0.00")
        self.lbl_round = QLabel("0.00")
        self.lbl_total = QLabel("0.00")
        self.lbl_total.setStyleSheet("font-weight:700;font-size:14px;")
        form.addRow("Gross", self.lbl_gross)
        form.addRow("Taxable", self.lbl_taxable)
        form.addRow("CGST", self.lbl_cgst)
        form.addRow("SGST", self.lbl_sgst)
        form.addRow("IGST", self.lbl_igst)
        form.addRow("Round Off", self.lbl_round)
        form.addRow("Grand Total", self.lbl_total)
        row.addWidget(totals)

        actions = QVBoxLayout()
        for label, slot in (("New", self._new_bill), ("Save", self._save),
                            ("Reload", self._reload), ("Print", self._print)):
            b = QPushButton(label); b.clicked.connect(slot)
            actions.addWidget(b)
        actions.addStretch(1)
        row.addLayout(actions)
        return row

    # -- grid editing ------------------------------------------------------
    def _add_row(self, line: SalesLine | None = None):
        self.table.blockSignals(True)
        r = self.table.rowCount()
        self.table.insertRow(r)
        line = line or SalesLine()
        for c, (_label, attr, editable) in enumerate(COLS):
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
            self.table.removeRow(r)
            self._recompute()

    def _cell_changed(self, _item):
        self._recompute()

    def _row_to_line(self, r: int) -> SalesLine:
        def cell(c):
            it = self.table.item(r, c)
            return it.text().strip() if it else ""
        idx = {attr: i for i, (_l, attr, _e) in enumerate(COLS)}
        return SalesLine(
            code=cell(idx["code"]), name=cell(idx["name"]),
            qty=D(cell(idx["qty"]) or 1), weight=D(cell(idx["weight"])),
            stone_wgt=D(cell(idx["stone_wgt"])), stone_price=D(cell(idx["stone_price"])),
            wastage=D(cell(idx["wastage"])), making=D(cell(idx["making"])),
            rate=D(cell(idx["rate"])))

    def _collect_lines(self) -> list[SalesLine]:
        lines = []
        for r in range(self.table.rowCount()):
            ln = self._row_to_line(r)
            if ln.code or ln.weight or ln.amount:
                lines.append(ln.compute())
        return lines

    # -- recompute + totals -----------------------------------------------
    def _recompute(self):
        self.table.blockSignals(True)
        net_i = next(i for i, (_l, a, _e) in enumerate(COLS) if a == "net_wgt")
        amt_i = next(i for i, (_l, a, _e) in enumerate(COLS) if a == "amount")
        for r in range(self.table.rowCount()):
            ln = self._row_to_line(r).compute()
            self.table.item(r, net_i).setText(f"{ln.net_wgt}")
            self.table.item(r, amt_i).setText(f"{ln.amount}")
        self.table.blockSignals(False)

        lines = self._collect_lines()
        try:
            tax_perc = D(self.ed_taxperc.text() or 0)
        except Exception:
            tax_perc = Decimal("0")
        totals = compute_bill(lines, tax_perc=tax_perc,
                              interstate=self.chk_interstate.isChecked(),
                              tax_inclusive=self.chk_inclusive.isChecked())
        self._totals = totals
        self.lbl_gross.setText(f"{totals.gross:.2f}")
        self.lbl_taxable.setText(f"{totals.taxable:.2f}")
        self.lbl_cgst.setText(f"{totals.cgst:.2f}")
        self.lbl_sgst.setText(f"{totals.sgst:.2f}")
        self.lbl_igst.setText(f"{totals.igst:.2f}")
        self.lbl_round.setText(f"{totals.round_off:.2f}")
        self.lbl_total.setText(f"{totals.grand_total:.2f}")

    # -- actions -----------------------------------------------------------
    def _new_bill(self):
        import datetime
        self.table.setRowCount(0)
        self.ed_date.setText(str(datetime.date.today()))
        self.ed_billno.setText(repo.next_billno(self.cb_type.currentText()))
        self._add_row()
        self._recompute()

    def _save(self):
        lines = self._collect_lines()
        if not lines:
            QMessageBox.warning(self, "Sales", "Add at least one item line.")
            return
        t = self._totals
        header = {
            "billno": self.ed_billno.text(), "tdate": self.ed_date.text(),
            "salestype": self.cb_type.currentText(),
            "custcode": self.cb_cust.currentData() or "",
            "custname": self.cb_cust.currentText(),
            "taxperc": str(self.ed_taxperc.text() or 0),
            "interstate": self.chk_interstate.isChecked(),
            "gross": t.gross, "taxable": t.taxable, "cgst": t.cgst,
            "sgst": t.sgst, "igst": t.igst, "roundoff": t.round_off,
            "total": t.grand_total,
        }
        try:
            billno = repo.save_bill(header, lines)
        except Exception as exc:
            QMessageBox.critical(self, "Sales", f"Save failed: {exc}")
            return
        QMessageBox.information(self, "Sales", f"Saved bill {billno}.")

    def _reload(self):
        billno = self.ed_billno.text().strip()
        head, lines = repo.load_bill(billno)
        if not head:
            QMessageBox.information(self, "Sales", f"No saved bill {billno}.")
            return
        self.table.setRowCount(0)
        for ln in lines:
            self._add_row(ln)
        self.ed_taxperc.setText(str(head.get("taxperc", 0)))
        self.chk_interstate.setChecked(str(head.get("interstate")) == "Y")
        self._recompute()

    def _print(self):
        lines = self._collect_lines()
        if not lines:
            QMessageBox.warning(self, "Sales", "Nothing to print.")
            return
        billno = self.ed_billno.text() or "invoice"
        path, _ = QFileDialog.getSaveFileName(
            self, "Print Invoice", f"{billno}.pdf", "PDF (*.pdf)")
        if not path:
            return
        header = {"billno": billno, "tdate": self.ed_date.text(),
                  "salestype": self.cb_type.currentText(),
                  "custname": self.cb_cust.currentText()}
        try:
            from app.reports.invoice import build_invoice_pdf
            build_invoice_pdf(path, header, lines, self._totals)
        except Exception as exc:
            QMessageBox.critical(self, "Sales", f"Print failed: {exc}")
            return
        QMessageBox.information(self, "Sales", f"Invoice saved: {path}")


def _factory(window):
    return SalesBillingForm(window)


for _win in ("w_sales", "w_sales_full"):
    modules.register(_win)(_factory)
