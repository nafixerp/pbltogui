"""
Repair / Remake memo screen (Phase 4) — conversion of GMINE ``w_reprenter``
(Receipt Memo from party) and ``w_reprno`` (Issue Memo to party).

A job-card style memo: header (memo no / date / due date / customer / salesman),
an item grid (code, description, qty, weight, stone wt, net wt, complaint,
purity, stock type, est. cost) with live net-weight, and running totals. The
same form serves both directions via the ``givrec`` flag.

Math from :mod:`app.services.repair_service`; persistence from
:mod:`app.repositories.repair_repository`.
"""

from __future__ import annotations

import datetime

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QComboBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMessageBox, QPushButton, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget,
)

from app import modules
from app.services.repair_service import (
    RepairLine, compute_totals, RECEIPT, ISSUE, MEMO_LABELS)
from app.services.sales_service import D
from app.repositories import repair_repository as repo

COLS = [
    ("Item Code", "code", True), ("Description", "name", True),
    ("Qty", "qty", True), ("Gross Wt", "weight", True),
    ("Stone Wt", "stone_wgt", True), ("Net Wt", "net_wgt", False),
    ("Complaint", "complaint", True), ("Purity", "purity", True),
    ("Stock Type", "stktype", True), ("Est. Cost", "cost", True),
]


class RepairMemoForm(QWidget):
    def __init__(self, givrec: str = RECEIPT, window=None, parent=None):
        super().__init__(parent)
        self.givrec = givrec
        repo.ensure_schema()
        self._build()
        self._new_memo()

    def _build(self):
        root = QVBoxLayout(self)
        title = QLabel(f"Remake / Repair — {MEMO_LABELS[self.givrec]}")
        title.setStyleSheet("font-size:16px;font-weight:700;padding:4px;")
        root.addWidget(title)
        root.addWidget(self._header_card())
        root.addWidget(self._line_grid(), 1)
        root.addLayout(self._bottom_row())

    def _header_card(self) -> QWidget:
        box = QGroupBox("Memo")
        grid = QGridLayout(box)
        self.ed_memono = QLineEdit(); self.ed_memono.setReadOnly(True)
        self.ed_date = QLineEdit()
        self.ed_due = QLineEdit()
        self.cb_cust = QComboBox(); self.cb_cust.setEditable(True)
        for c in repo.list_customers():
            self.cb_cust.addItem(f"{c['code']} - {c['name']}", c['code'])
        self.ed_sman = QLineEdit()

        grid.addWidget(QLabel("Memo No"), 0, 0); grid.addWidget(self.ed_memono, 0, 1)
        grid.addWidget(QLabel("Date"), 0, 2); grid.addWidget(self.ed_date, 0, 3)
        grid.addWidget(QLabel("Due Date"), 0, 4); grid.addWidget(self.ed_due, 0, 5)
        grid.addWidget(QLabel("Customer"), 1, 0); grid.addWidget(self.cb_cust, 1, 1, 1, 3)
        grid.addWidget(QLabel("Salesman"), 1, 4); grid.addWidget(self.ed_sman, 1, 5)
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
        self.lbl_qty = QLabel("0"); self.lbl_gross = QLabel("0.000")
        self.lbl_net = QLabel("0.000"); self.lbl_cost = QLabel("0.00")
        form.addRow("Total Qty", self.lbl_qty)
        form.addRow("Gross Wt", self.lbl_gross)
        form.addRow("Net Wt", self.lbl_net)
        form.addRow("Est. Cost", self.lbl_cost)
        row.addWidget(totals)
        actions = QVBoxLayout()
        for label, slot in (("New", self._new_memo), ("Save", self._save),
                            ("Reload", self._reload)):
            b = QPushButton(label); b.clicked.connect(slot); actions.addWidget(b)
        actions.addStretch(1)
        row.addLayout(actions)
        return row

    # -- grid --------------------------------------------------------------
    def _add_row(self, line: RepairLine | None = None):
        self.table.blockSignals(True)
        r = self.table.rowCount(); self.table.insertRow(r)
        line = line or RepairLine()
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

    def _row_to_line(self, r: int) -> RepairLine:
        def cell(c):
            it = self.table.item(r, c)
            return it.text().strip() if it else ""
        idx = {attr: i for i, (_l, attr, _e) in enumerate(COLS)}
        return RepairLine(
            code=cell(idx["code"]), name=cell(idx["name"]),
            qty=D(cell(idx["qty"]) or 1), weight=D(cell(idx["weight"])),
            stone_wgt=D(cell(idx["stone_wgt"])), complaint=cell(idx["complaint"]),
            purity=cell(idx["purity"]), stktype=cell(idx["stktype"]),
            cost=D(cell(idx["cost"])))

    def _collect_lines(self) -> list[RepairLine]:
        out = []
        for r in range(self.table.rowCount()):
            ln = self._row_to_line(r)
            if ln.code or ln.weight or ln.complaint:
                out.append(ln.compute())
        return out

    def _recompute(self):
        self.table.blockSignals(True)
        idx = {attr: i for i, (_l, attr, _e) in enumerate(COLS)}
        for r in range(self.table.rowCount()):
            ln = self._row_to_line(r).compute()
            self.table.item(r, idx["net_wgt"]).setText(f"{ln.net_wgt}")
        self.table.blockSignals(False)
        t = compute_totals(self._collect_lines())
        self.lbl_qty.setText(f"{t.qty}")
        self.lbl_gross.setText(f"{t.gross_wgt}")
        self.lbl_net.setText(f"{t.net_wgt}")
        self.lbl_cost.setText(f"{t.cost:.2f}")

    # -- actions -----------------------------------------------------------
    def _new_memo(self):
        self.table.setRowCount(0)
        self.ed_date.setText(str(datetime.date.today()))
        self.ed_due.setText(str(datetime.date.today() + datetime.timedelta(days=7)))
        self.ed_memono.setText(repo.next_memono(self.givrec))
        self._add_row(); self._recompute()

    def _save(self):
        lines = self._collect_lines()
        if not lines:
            QMessageBox.warning(self, "Repair", "Add at least one item line.")
            return
        header = {
            "billno": self.ed_memono.text(), "tdate": self.ed_date.text(),
            "duedate": self.ed_due.text(), "custcode": self.cb_cust.currentData() or "",
            "custname": self.cb_cust.currentText(), "givrec": self.givrec,
            "sman": self.ed_sman.text(),
        }
        try:
            memono = repo.save_memo(header, lines)
        except Exception as exc:
            QMessageBox.critical(self, "Repair", f"Save failed: {exc}")
            return
        QMessageBox.information(self, "Repair", f"Saved memo {memono}.")

    def _reload(self):
        memono = self.ed_memono.text().strip()
        head, lines = repo.load_memo(memono)
        if not head:
            QMessageBox.information(self, "Repair", f"No saved memo {memono}.")
            return
        self.table.setRowCount(0)
        for ln in lines:
            self._add_row(ln)
        self.ed_due.setText(str(head.get("duedate", "")))
        self.ed_sman.setText(str(head.get("sman", "")))
        self._recompute()


def _factory(givrec):
    def factory(window):
        return RepairMemoForm(givrec=givrec, window=window)
    return factory


modules.register("w_reprenter")(_factory(RECEIPT))
modules.register("w_reprno")(_factory(ISSUE))
