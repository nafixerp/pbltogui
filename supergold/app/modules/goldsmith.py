"""
Goldsmith / Jewellery weight transaction screen (Phase 4) — conversion of GMINE
``w_gsmith``.

Header (memo no / date / goldsmith / Given|Received), an item grid that computes
net weight and fine (touch) weight live, running totals, and the goldsmith's
outstanding fine-weight balance. Math from
:mod:`app.services.goldsmith_service`; persistence from
:mod:`app.repositories.goldsmith_repository`.
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
from app.services.goldsmith_service import (
    SmithLine, compute_totals, GIVEN, RECEIVED, DIR_LABELS)
from app.services.sales_service import D
from app.repositories import goldsmith_repository as repo

COLS = [
    ("Item Code", "code", True), ("Description", "name", True),
    ("Qty", "qty", True), ("Gross Wt", "weight", True),
    ("Stone Wt", "stone_wgt", True), ("Net Wt", "net_wgt", False),
    ("Touch %", "touch", True), ("Fine Wt", "touch_wgt", False),
    ("Making", "making", True),
]


class GoldsmithForm(QWidget):
    def __init__(self, window=None, parent=None):
        super().__init__(parent)
        repo.ensure_schema()
        self._build()
        self._new_memo()

    def _build(self):
        root = QVBoxLayout(self)
        title = QLabel("Goldsmith / Jewellery Transaction")
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
        self.cb_dir = QComboBox()
        for code in (GIVEN, RECEIVED):
            self.cb_dir.addItem(DIR_LABELS[code], code)
        self.cb_smith = QComboBox(); self.cb_smith.setEditable(True)
        for s in repo.list_smiths():
            self.cb_smith.addItem(f"{s['code']} - {s['name']}", s['code'])

        self.cb_dir.currentIndexChanged.connect(self._dir_changed)
        self.cb_smith.currentIndexChanged.connect(self._update_balance)

        grid.addWidget(QLabel("Memo No"), 0, 0); grid.addWidget(self.ed_memono, 0, 1)
        grid.addWidget(QLabel("Date"), 0, 2); grid.addWidget(self.ed_date, 0, 3)
        grid.addWidget(QLabel("Direction"), 0, 4); grid.addWidget(self.cb_dir, 0, 5)
        grid.addWidget(QLabel("Goldsmith"), 1, 0); grid.addWidget(self.cb_smith, 1, 1, 1, 3)
        self.lbl_balance = QLabel("0.000")
        self.lbl_balance.setStyleSheet("font-weight:700;color:#1f3a5f;")
        grid.addWidget(QLabel("Fine Bal (g)"), 1, 4); grid.addWidget(self.lbl_balance, 1, 5)
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
        self.lbl_net = QLabel("0.000"); self.lbl_fine = QLabel("0.000")
        self.lbl_making = QLabel("0.00")
        form.addRow("Total Qty", self.lbl_qty)
        form.addRow("Gross Wt", self.lbl_gross)
        form.addRow("Net Wt", self.lbl_net)
        form.addRow("Fine Wt", self.lbl_fine)
        form.addRow("Making", self.lbl_making)
        row.addWidget(totals)
        actions = QVBoxLayout()
        for label, slot in (("New", self._new_memo), ("Save", self._save),
                            ("Reload", self._reload)):
            b = QPushButton(label); b.clicked.connect(slot); actions.addWidget(b)
        actions.addStretch(1)
        row.addLayout(actions)
        return row

    # -- grid --------------------------------------------------------------
    def _add_row(self, line: SmithLine | None = None):
        self.table.blockSignals(True)
        r = self.table.rowCount(); self.table.insertRow(r)
        line = line or SmithLine()
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

    def _row_to_line(self, r: int) -> SmithLine:
        def cell(c):
            it = self.table.item(r, c)
            return it.text().strip() if it else ""
        idx = {attr: i for i, (_l, attr, _e) in enumerate(COLS)}
        return SmithLine(
            code=cell(idx["code"]), name=cell(idx["name"]),
            qty=D(cell(idx["qty"]) or 1), weight=D(cell(idx["weight"])),
            stone_wgt=D(cell(idx["stone_wgt"])), touch=D(cell(idx["touch"])),
            making=D(cell(idx["making"])))

    def _collect_lines(self) -> list[SmithLine]:
        out = []
        for r in range(self.table.rowCount()):
            ln = self._row_to_line(r)
            if ln.code or ln.weight:
                out.append(ln.compute())
        return out

    def _recompute(self):
        self.table.blockSignals(True)
        idx = {attr: i for i, (_l, attr, _e) in enumerate(COLS)}
        for r in range(self.table.rowCount()):
            ln = self._row_to_line(r).compute()
            self.table.item(r, idx["net_wgt"]).setText(f"{ln.net_wgt}")
            self.table.item(r, idx["touch_wgt"]).setText(f"{ln.touch_wgt}")
        self.table.blockSignals(False)
        t = compute_totals(self._collect_lines())
        self.lbl_qty.setText(f"{t.qty}")
        self.lbl_gross.setText(f"{t.gross_wgt}")
        self.lbl_net.setText(f"{t.net_wgt}")
        self.lbl_fine.setText(f"{t.fine_wgt}")
        self.lbl_making.setText(f"{t.making:.2f}")

    # -- actions -----------------------------------------------------------
    def _dir_changed(self):
        self._new_memo()

    def _update_balance(self):
        code = self.cb_smith.currentData()
        self.lbl_balance.setText(f"{repo.fine_balance(code):.3f}" if code else "0.000")

    def _new_memo(self):
        self.table.setRowCount(0)
        self.ed_date.setText(str(datetime.date.today()))
        self.ed_memono.setText(repo.next_memono(self.cb_dir.currentData()))
        self._add_row(); self._recompute(); self._update_balance()

    def _save(self):
        lines = self._collect_lines()
        if not lines:
            QMessageBox.warning(self, "Goldsmith", "Add at least one item line.")
            return
        header = {
            "billno": self.ed_memono.text(), "tdate": self.ed_date.text(),
            "smithcode": self.cb_smith.currentData() or "",
            "smithname": self.cb_smith.currentText(),
            "givrec": self.cb_dir.currentData(),
        }
        try:
            memono = repo.save_memo(header, lines)
        except Exception as exc:
            QMessageBox.critical(self, "Goldsmith", f"Save failed: {exc}")
            return
        QMessageBox.information(self, "Goldsmith", f"Saved memo {memono}.")
        self._update_balance()

    def _reload(self):
        memono = self.ed_memono.text().strip()
        head, lines = repo.load_memo(memono)
        if not head:
            QMessageBox.information(self, "Goldsmith", f"No saved memo {memono}.")
            return
        self.table.setRowCount(0)
        for ln in lines:
            self._add_row(ln)
        i = self.cb_dir.findData(head.get("givrec"))
        if i >= 0:
            self.cb_dir.blockSignals(True); self.cb_dir.setCurrentIndex(i)
            self.cb_dir.blockSignals(False)
        self._recompute()


def _factory(window):
    return GoldsmithForm(window)


modules.register("w_gsmith")(_factory)
