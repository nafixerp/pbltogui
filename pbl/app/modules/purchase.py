"""
Purchase billing screen (Phase 4) — business-logic conversion of GMINE
``w_purchase`` / ``w_purchase_withbc``.

Header card (supplier / doc no / supplier bill / date / tax%), an editable line
grid that recomputes less weight, net weight and amount live, and a totals panel
with the GST split and round-off. Math from
:mod:`app.services.purchase_service`; persistence from
:mod:`app.repositories.purchase_repository`.
"""

from __future__ import annotations

from decimal import Decimal

from PySide6.QtCore import Qt
from PySide6.QtGui import QDoubleValidator
from PySide6.QtWidgets import (
    QCheckBox, QComboBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMessageBox, QPushButton, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget,
)

from app import modules
from app.services.purchase_service import PurchaseLine, compute_totals
from app.services.sales_service import D
from app.repositories import purchase_repository as repo

COLS = [
    ("Item Code", "code", True), ("Description", "name", True),
    ("Qty", "qty", True), ("Gross Wt", "weight", True),
    ("Stone Wt", "stone_wgt", True), ("Stone Price", "stone_price", True),
    ("Mud Wt", "mud", True), ("Less %", "less_perc", True),
    ("Making", "making", True), ("Rate", "rate", True),
    ("Less Wt", "less_wgt", False), ("Net Wt", "net_wgt", False),
    ("Amount", "amount", False),
]


class PurchaseBillingForm(QWidget):
    def __init__(self, window=None, parent=None):
        super().__init__(parent)
        repo.ensure_schema()
        self._build()
        self._new_bill()

    def _build(self):
        root = QVBoxLayout(self)
        title = QLabel("Purchase Billing")
        title.setStyleSheet("font-size:16px;font-weight:700;padding:4px;")
        root.addWidget(title)
        root.addWidget(self._header_card())
        root.addWidget(self._line_grid(), 1)
        root.addLayout(self._bottom_row())

    def _header_card(self) -> QWidget:
        box = QGroupBox("Bill")
        grid = QGridLayout(box)
        self.ed_docno = QLineEdit(); self.ed_docno.setReadOnly(True)
        self.ed_billno = QLineEdit()
        self.ed_date = QLineEdit()
        self.cb_supp = QComboBox(); self.cb_supp.setEditable(True)
        for s in repo.list_suppliers():
            self.cb_supp.addItem(f"{s['code']} - {s['name']}", s['code'])
        self.ed_taxperc = QLineEdit("3")
        self.ed_taxperc.setValidator(QDoubleValidator(0, 100, 2))
        self.chk_interstate = QCheckBox("Inter-state (IGST)")
        self.chk_inclusive = QCheckBox("Tax inclusive")

        grid.addWidget(QLabel("Doc No"), 0, 0); grid.addWidget(self.ed_docno, 0, 1)
        grid.addWidget(QLabel("Supp. Bill"), 0, 2); grid.addWidget(self.ed_billno, 0, 3)
        grid.addWidget(QLabel("Date"), 0, 4); grid.addWidget(self.ed_date, 0, 5)
        grid.addWidget(QLabel("Supplier"), 1, 0); grid.addWidget(self.cb_supp, 1, 1, 1, 3)
        grid.addWidget(QLabel("Tax %"), 1, 4); grid.addWidget(self.ed_taxperc, 1, 5)
        grid.addWidget(self.chk_interstate, 2, 1)
        grid.addWidget(self.chk_inclusive, 2, 2)

        self.ed_taxperc.textChanged.connect(self._recompute)
        self.chk_interstate.toggled.connect(self._recompute)
        self.chk_inclusive.toggled.connect(self._recompute)
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
        self.lbl_gross = QLabel("0.00"); self.lbl_taxable = QLabel("0.00")
        self.lbl_cgst = QLabel("0.00"); self.lbl_sgst = QLabel("0.00")
        self.lbl_igst = QLabel("0.00"); self.lbl_round = QLabel("0.00")
        self.lbl_total = QLabel("0.00")
        self.lbl_total.setStyleSheet("font-weight:700;font-size:14px;")
        form.addRow("Gross", self.lbl_gross); form.addRow("Taxable", self.lbl_taxable)
        form.addRow("CGST", self.lbl_cgst); form.addRow("SGST", self.lbl_sgst)
        form.addRow("IGST", self.lbl_igst); form.addRow("Round Off", self.lbl_round)
        form.addRow("Grand Total", self.lbl_total)
        row.addWidget(totals)
        actions = QVBoxLayout()
        for label, slot in (("New", self._new_bill), ("Save", self._save),
                            ("Reload", self._reload)):
            b = QPushButton(label); b.clicked.connect(slot); actions.addWidget(b)
        actions.addStretch(1)
        row.addLayout(actions)
        return row

    # -- grid --------------------------------------------------------------
    def _add_row(self, line: PurchaseLine | None = None):
        self.table.blockSignals(True)
        r = self.table.rowCount(); self.table.insertRow(r)
        line = line or PurchaseLine()
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

    def _row_to_line(self, r: int) -> PurchaseLine:
        def cell(c):
            it = self.table.item(r, c)
            return it.text().strip() if it else ""
        idx = {attr: i for i, (_l, attr, _e) in enumerate(COLS)}
        return PurchaseLine(
            code=cell(idx["code"]), name=cell(idx["name"]),
            qty=D(cell(idx["qty"]) or 1), weight=D(cell(idx["weight"])),
            stone_wgt=D(cell(idx["stone_wgt"])), stone_price=D(cell(idx["stone_price"])),
            mud=D(cell(idx["mud"])), less_perc=D(cell(idx["less_perc"])),
            making=D(cell(idx["making"])), rate=D(cell(idx["rate"])))

    def _collect_lines(self) -> list[PurchaseLine]:
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
            self.table.item(r, idx["less_wgt"]).setText(f"{ln.less_wgt}")
            self.table.item(r, idx["net_wgt"]).setText(f"{ln.net_wgt}")
            self.table.item(r, idx["amount"]).setText(f"{ln.amount}")
        self.table.blockSignals(False)

        lines = self._collect_lines()
        try:
            tax_perc = D(self.ed_taxperc.text() or 0)
        except Exception:
            tax_perc = Decimal("0")
        t = compute_totals(lines, tax_perc=tax_perc,
                           interstate=self.chk_interstate.isChecked(),
                           tax_inclusive=self.chk_inclusive.isChecked())
        self._totals = t
        self.lbl_gross.setText(f"{t.gross:.2f}"); self.lbl_taxable.setText(f"{t.taxable:.2f}")
        self.lbl_cgst.setText(f"{t.cgst:.2f}"); self.lbl_sgst.setText(f"{t.sgst:.2f}")
        self.lbl_igst.setText(f"{t.igst:.2f}"); self.lbl_round.setText(f"{t.round_off:.2f}")
        self.lbl_total.setText(f"{t.grand_total:.2f}")

    # -- actions -----------------------------------------------------------
    def _new_bill(self):
        import datetime
        self.table.setRowCount(0)
        self.ed_date.setText(str(datetime.date.today()))
        self.ed_docno.setText(repo.next_docno("P"))
        self.ed_billno.clear()
        self._add_row(); self._recompute()

    def _save(self):
        lines = self._collect_lines()
        if not lines:
            QMessageBox.warning(self, "Purchase", "Add at least one item line.")
            return
        t = self._totals
        header = {
            "docno": self.ed_docno.text(), "billno": self.ed_billno.text(),
            "tdate": self.ed_date.text(), "suppcode": self.cb_supp.currentData() or "",
            "name": self.cb_supp.currentText(), "taxperc": str(self.ed_taxperc.text() or 0),
            "interstate": self.chk_interstate.isChecked(),
            "billamt": t.gross, "netamt": t.taxable, "taxamt": t.tax_amount,
            "cgst": t.cgst, "sgst": t.sgst, "igst": t.igst,
            "round": t.round_off, "total": t.grand_total,
        }
        try:
            docno = repo.save_bill(header, lines)
        except Exception as exc:
            QMessageBox.critical(self, "Purchase", f"Save failed: {exc}")
            return
        QMessageBox.information(self, "Purchase", f"Saved purchase {docno}.")

    def _reload(self):
        docno = self.ed_docno.text().strip()
        head, lines = repo.load_bill(docno)
        if not head:
            QMessageBox.information(self, "Purchase", f"No saved purchase {docno}.")
            return
        self.table.setRowCount(0)
        for ln in lines:
            self._add_row(ln)
        self.ed_taxperc.setText(str(head.get("taxperc", 0)))
        self.chk_interstate.setChecked(str(head.get("interstate")) == "Y")
        self._recompute()


def _factory(window):
    return PurchaseBillingForm(window)


for _win in ("w_purchase", "w_purchase_withbc"):
    modules.register(_win)(_factory)
