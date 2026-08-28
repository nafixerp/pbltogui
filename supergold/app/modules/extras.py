"""
The last of the screens: stock movements, settings, and small utilities.

* **Stock Transfer** / **Stock Transfer Multi Entry** (``w_itemadj``,
  ``w_itemadj_multi``) and **Stock Add - Less** (``w_stockaddless``) move stock
  between items and in or out of the shop, writing the ``itemadj`` row the
  original wrote (so the Item Adjustment report and the cancel screen see them).
* **Settings** (``w_setup``, ``w_bookstock``, ``w_stockvalueset``) edit the
  key/value settings tables ``generali``/``generald``/``generals``.
* **Block / Unblock an Order** (``w_order_block``) sets ``orderm.blocked``.
* **Staff Log Update** (``w_staff_attand_update``) adds attendance punches.
* **Reprint** (``w_acreprint``, ``w_gsmthreprint``) finds a document and prints
  it, and **Administration** (``w_administration``) shows what the database
  holds.
"""

from __future__ import annotations

import datetime

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QComboBox, QDateEdit, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QMessageBox, QPushButton, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget,
)

import db
from app import modules
from app.services import stock_service
from app.ui.printing import print_table


def _title(text: str) -> QLabel:
    label = QLabel(f"<h3>{text}</h3>")
    label.setTextFormat(Qt.RichText)
    return label


def _row(*widgets) -> QHBoxLayout:
    lay = QHBoxLayout()
    for w in widgets:
        lay.addWidget(QLabel(w) if isinstance(w, str) else w)
    lay.addStretch(1)
    return lay


def _edit(width=120, text="") -> QLineEdit:
    w = QLineEdit(text)
    w.setMaximumWidth(width)
    return w


def _grid() -> QTableWidget:
    grid = QTableWidget(0, 0)
    grid.setEditTriggers(QTableWidget.NoEditTriggers)
    grid.setSelectionBehavior(QTableWidget.SelectRows)
    return grid


def _fill(grid: QTableWidget, rows: list, columns: list | None = None):
    columns = columns or (list(rows[0].keys()) if rows else [])
    grid.clear()
    grid.setColumnCount(len(columns))
    grid.setHorizontalHeaderLabels(columns)
    grid.setRowCount(len(rows))
    for r, row in enumerate(rows):
        for c, col in enumerate(columns):
            value = row.get(col)
            grid.setItem(r, c, QTableWidgetItem("" if value is None else str(value)))
    grid.resizeColumnsToContents()


def _fetch(sql, params=()):
    try:
        return db.fetch_all(sql, params)
    except Exception:
        return []


# ---------------------------------------------------------------------------
# Stock transfer / add-less
# ---------------------------------------------------------------------------

class StockTransferForm(QWidget):
    """Move stock from one item to another (``w_itemadj``)."""

    def __init__(self, parsed=None, parent=None, seed=None):
        super().__init__(parent)
        lay = QVBoxLayout(self)
        lay.addWidget(_title("Stock Transfer"))

        self.from_code = _edit(140)
        self.from_stk = _edit(120)
        self.to_code = _edit(140)
        self.to_stk = _edit(120)
        self.qty = _edit(80, "0")
        self.weight = _edit(100, "0")
        self.stone = _edit(100, "0")
        lay.addLayout(_row("From item", self.from_code, "Stock type", self.from_stk))
        lay.addLayout(_row("To item", self.to_code, "Stock type", self.to_stk))
        lay.addLayout(_row("Qty", self.qty, "Weight", self.weight,
                           "Stone wgt", self.stone))

        save = QPushButton("&Transfer")
        save.clicked.connect(self.save)
        lay.addLayout(_row(save))
        self.status = QLabel()
        lay.addWidget(self.status)

        box = QGroupBox("Recent transfers")
        box_lay = QVBoxLayout(box)
        self.grid = _grid()
        box_lay.addWidget(self.grid)
        lay.addWidget(box, 1)
        self.refresh()

    def refresh(self):
        _fill(self.grid, _fetch("SELECT slno, tdate, fromcode, tocode, fromqty, "
                                "fromwgt FROM itemadj ORDER BY slno DESC")[:100])

    def save(self):
        try:
            slno = stock_service.transfer_stock(
                self.from_code.text(), self.to_code.text(),
                qty=float(self.qty.text() or 0),
                weight=float(self.weight.text() or 0),
                stonewgt=float(self.stone.text() or 0),
                from_stktype=self.from_stk.text().strip(),
                to_stktype=self.to_stk.text().strip())
        except Exception as exc:
            QMessageBox.warning(self, "Stock Transfer", str(exc))
            return
        self.status.setText(f"Transferred — entry {slno}.")
        self.refresh()


class StockAddLessForm(QWidget):
    """Add stock to an item or take it out (``w_stockaddless``)."""

    def __init__(self, parsed=None, parent=None, seed=None):
        super().__init__(parent)
        lay = QVBoxLayout(self)
        lay.addWidget(_title("Stock Add / Less"))

        self.code = _edit(140)
        self.stk = _edit(120)
        self.mode = QComboBox()
        self.mode.addItems(["Add", "Less"])
        self.qty = _edit(80, "0")
        self.weight = _edit(100, "0")
        self.stone = _edit(100, "0")
        self.note = _edit(220)
        lay.addLayout(_row("Item", self.code, "Stock type", self.stk, self.mode))
        lay.addLayout(_row("Qty", self.qty, "Weight", self.weight,
                           "Stone wgt", self.stone))
        lay.addLayout(_row("Reason", self.note))

        save = QPushButton("&Save")
        save.clicked.connect(self.save)
        lay.addLayout(_row(save))
        self.status = QLabel()
        lay.addWidget(self.status)

        box = QGroupBox("Recent entries")
        box_lay = QVBoxLayout(box)
        self.grid = _grid()
        box_lay.addWidget(self.grid)
        lay.addWidget(box, 1)
        self.refresh()

    def refresh(self):
        _fill(self.grid, _fetch("SELECT slno, tdate, fromcode, tocode, fromwgt, "
                                "towgt FROM itemadj ORDER BY slno DESC")[:100])

    def save(self):
        try:
            slno = stock_service.add_less_stock(
                self.code.text(), qty=float(self.qty.text() or 0),
                weight=float(self.weight.text() or 0),
                stonewgt=float(self.stone.text() or 0),
                stktype=self.stk.text().strip(),
                add=self.mode.currentText() == "Add",
                note=self.note.text().strip())
        except Exception as exc:
            QMessageBox.warning(self, "Stock Add / Less", str(exc))
            return
        self.status.setText(f"Saved — entry {slno}.")
        self.refresh()


# ---------------------------------------------------------------------------
# Settings (key/value tables)
# ---------------------------------------------------------------------------

class SettingsForm(QWidget):
    """Edit the application's settings tables (``generali`` and friends)."""

    def __init__(self, tables, title="Settings", parsed=None, parent=None, seed=None):
        super().__init__(parent)
        self.tables = tables
        lay = QVBoxLayout(self)
        lay.addWidget(_title(title))

        self.table = QComboBox()
        self.table.addItems(tables)
        self.table.currentTextChanged.connect(lambda _t: self.refresh())
        self.key = _edit(180)
        self.value = _edit(180)
        set_btn = QPushButton("&Set")
        set_btn.clicked.connect(self.save)
        delete = QPushButton("&Delete")
        delete.clicked.connect(self.delete)
        lay.addLayout(_row("Table", self.table, "Setting", self.key,
                           "Value", self.value, set_btn, delete))

        self.grid = _grid()
        self.grid.itemSelectionChanged.connect(self._selected)
        lay.addWidget(self.grid, 1)
        self.status = QLabel()
        lay.addWidget(self.status)
        self.refresh()

    def _current(self) -> str:
        return self.table.currentText()

    def refresh(self):
        self._rows = _fetch(f"SELECT code, cvalue FROM {self._current()} "
                            f"ORDER BY code")
        _fill(self.grid, self._rows, ["code", "cvalue"])
        self.status.setText(f"{len(self._rows)} setting(s) in {self._current()}")

    def _selected(self):
        idx = self.grid.currentRow()
        if 0 <= idx < len(self._rows):
            self.key.setText(str(self._rows[idx].get("code") or ""))
            self.value.setText(str(self._rows[idx].get("cvalue") or ""))

    def save(self):
        code = self.key.text().strip()
        if not code:
            self.status.setText("Enter the setting name.")
            return
        table = self._current()
        try:
            exists = db.fetch_one(f"SELECT 1 AS x FROM {table} WHERE TRIM(code) = ?",
                                  (code,))
            if exists:
                db.execute(f"UPDATE {table} SET cvalue = ? WHERE TRIM(code) = ?",
                           (self.value.text().strip(), code))
            else:
                db.execute(f"INSERT INTO {table} (code, cvalue) VALUES (?, ?)",
                           (code, self.value.text().strip()))
        except Exception as exc:
            QMessageBox.warning(self, "Settings", f"Could not save: {exc}")
            return
        self.refresh()
        self.status.setText(f"{code} saved.")

    def delete(self):
        code = self.key.text().strip()
        if not code:
            return
        try:
            db.execute(f"DELETE FROM {self._current()} WHERE TRIM(code) = ?", (code,))
        except Exception as exc:
            QMessageBox.warning(self, "Settings", f"Could not delete: {exc}")
            return
        self.refresh()


# ---------------------------------------------------------------------------
# Order block / staff log / reprint / administration
# ---------------------------------------------------------------------------

class OrderBlockForm(QWidget):
    """Block or unblock an order (``w_order_block``)."""

    def __init__(self, parsed=None, parent=None, seed=None):
        super().__init__(parent)
        lay = QVBoxLayout(self)
        lay.addWidget(_title("Block / Unblock an Order"))
        self.ordno = _edit(160)
        block = QPushButton("&Block")
        block.clicked.connect(lambda: self.set_blocked("Y"))
        unblock = QPushButton("&Unblock")
        unblock.clicked.connect(lambda: self.set_blocked("N"))
        lay.addLayout(_row("Order no", self.ordno, block, unblock))
        self.status = QLabel()
        lay.addWidget(self.status)
        self.grid = _grid()
        lay.addWidget(self.grid, 1)
        self.refresh()

    def refresh(self):
        _fill(self.grid, _fetch("SELECT ordno, tdate, custname, blocked, status "
                                "FROM orderm ORDER BY slno DESC")[:200])

    def set_blocked(self, flag: str):
        ordno = self.ordno.text().strip()
        if not ordno:
            self.status.setText("Enter the order number.")
            return
        try:
            db.execute("UPDATE orderm SET blocked = ? WHERE TRIM(ordno) = ?",
                       (flag, ordno))
        except Exception as exc:
            QMessageBox.warning(self, "Order", f"Could not update: {exc}")
            return
        self.status.setText(f"Order {ordno} {'blocked' if flag == 'Y' else 'unblocked'}.")
        self.refresh()


class StaffLogForm(QWidget):
    """Add an attendance punch (``w_staff_attand_update``)."""

    def __init__(self, parsed=None, parent=None, seed=None):
        super().__init__(parent)
        lay = QVBoxLayout(self)
        lay.addWidget(_title("Staff Log Update"))
        self.scode = _edit(120)
        self.date = QDateEdit()
        self.date.setCalendarPopup(True)
        self.date.setDisplayFormat("dd-MM-yyyy")
        self.date.setDate(self.date.date().currentDate())
        self.time = _edit(100, datetime.datetime.now().strftime("%H:%M"))
        self.mode = QComboBox()
        self.mode.addItems(["IN", "OUT"])
        add = QPushButton("&Add")
        add.clicked.connect(self.add)
        lay.addLayout(_row("Staff code", self.scode, "Date", self.date,
                           "Time", self.time, self.mode, add))
        self.status = QLabel()
        lay.addWidget(self.status)
        self.grid = _grid()
        lay.addWidget(self.grid, 1)
        self.refresh()

    def refresh(self):
        _fill(self.grid, _fetch("SELECT scode, tdate, ttime, status FROM staff_log "
                                "ORDER BY tdate DESC, ttime DESC")[:200])

    def add(self):
        code = self.scode.text().strip()
        if not code:
            self.status.setText("Enter the staff code.")
            return
        try:
            db.execute("INSERT INTO staff_log (scode, tdate, ttime, status) "
                       "VALUES (?, ?, ?, ?)",
                       (code, self.date.date().toString("yyyy-MM-dd"),
                        self.time.text().strip(), self.mode.currentText()))
        except Exception as exc:
            QMessageBox.warning(self, "Staff Log", f"Could not add: {exc}")
            return
        self.status.setText("Punch added.")
        self.refresh()


class ReprintForm(QWidget):
    """Find a document and print it again (``w_acreprint``, ``w_gsmthreprint``)."""

    SOURCES = {
        "w_acreprint": ("daybook", "sno", "Voucher"),
        "w_gsmthreprint": ("smithm", "docno", "Goldsmith document"),
    }

    def __init__(self, window: str, parsed=None, parent=None, seed=None):
        super().__init__(parent)
        self.table, self.key, label = self.SOURCES[window]
        lay = QVBoxLayout(self)
        lay.addWidget(_title(f"Reprint — {label}"))
        self.search = _edit(180)
        find = QPushButton("&Search")
        find.clicked.connect(self.refresh)
        printer = QPushButton("&Print")
        printer.clicked.connect(self.print_selected)
        lay.addLayout(_row(self.key, self.search, find, printer))
        self.grid = _grid()
        lay.addWidget(self.grid, 1)
        self.status = QLabel()
        lay.addWidget(self.status)
        self._rows: list = []
        self.refresh()

    def refresh(self):
        text = self.search.text().strip()
        sql = f"SELECT * FROM {self.table}"
        params: list = []
        if text:
            sql += f" WHERE UPPER(CAST({self.key} AS VARCHAR(50))) LIKE ?"
            params = [f"%{text.upper()}%"]
        self._rows = _fetch(sql, params)[:200]
        _fill(self.grid, self._rows)
        self.status.setText(f"{len(self._rows)} document(s)")

    def print_selected(self):
        idx = self.grid.currentRow()
        if idx < 0 or idx >= len(self._rows):
            QMessageBox.information(self, "Reprint", "Select a document first.")
            return
        row = self._rows[idx]
        print_table(self, f"{self.table} {row.get(self.key)}", list(row.keys()), [row])


class AdministrationForm(QWidget):
    """What the database holds, for the administrator (``w_administration``)."""

    WATCH = ("salesm", "salesrm", "purchasem", "purchaserm", "smithm", "orderm",
             "repairm", "refinerym", "daybook", "items", "barcode", "clients",
             "accountm", "userm", "delpart", "daylock")

    def __init__(self, parsed=None, parent=None, seed=None):
        super().__init__(parent)
        lay = QVBoxLayout(self)
        lay.addWidget(_title("Administration"))
        lay.addWidget(QLabel(f"Database engine: <b>{db.ENGINE}</b>"))
        refresh = QPushButton("&Refresh")
        refresh.clicked.connect(self.refresh)
        lay.addLayout(_row(refresh))
        self.grid = _grid()
        lay.addWidget(self.grid, 1)
        self.refresh()

    def refresh(self):
        rows = []
        for table in self.WATCH:
            row = None
            try:
                row = db.fetch_one(f"SELECT COUNT(*) AS c FROM {table}")
            except Exception:
                pass
            rows.append({"table": table,
                         "rows": row["c"] if row else "not in this database"})
        _fill(self.grid, rows, ["table", "rows"])


# ---------------------------------------------------------------------------
# Registration
# ---------------------------------------------------------------------------

modules.register("w_itemadj")(lambda parsed=None, **kw: StockTransferForm(parsed))
modules.register("w_itemadj_multi")(lambda parsed=None, **kw: StockTransferForm(parsed))
modules.register("w_stockaddless")(lambda parsed=None, **kw: StockAddLessForm(parsed))
modules.register("w_setup")(
    lambda parsed=None, **kw: SettingsForm(["generali", "generald", "generals"],
                                           "Application Settings", parsed))
modules.register("w_bookstock")(
    lambda parsed=None, **kw: SettingsForm(["generals", "generald"],
                                           "Book Stock", parsed))
modules.register("w_stockvalueset")(
    lambda parsed=None, **kw: SettingsForm(["generald", "generali"],
                                           "Opening Stock Value", parsed))
modules.register("w_order_block")(lambda parsed=None, **kw: OrderBlockForm(parsed))
modules.register("w_staff_attand_update")(
    lambda parsed=None, **kw: StaffLogForm(parsed))
modules.register("w_administration")(
    lambda parsed=None, **kw: AdministrationForm(parsed))
for _window in ReprintForm.SOURCES:
    modules.register(_window)(
        lambda parsed=None, _w=_window, **kw: ReprintForm(_w, parsed))


# ---------------------------------------------------------------------------
# All Report Print, Incharge change, Purity certificate
# ---------------------------------------------------------------------------

class AllReportsForm(QWidget):
    """Run several reports one after another and print them (``w_allinone_report``)."""

    def __init__(self, parsed=None, parent=None, seed=None):
        super().__init__(parent)
        from app.reports import analysis, final_accounts

        self.specs = {}
        for source in (final_accounts.SPECS, analysis.SPECS):
            for window, spec in source.items():
                self.specs[spec.title] = spec

        lay = QVBoxLayout(self)
        lay.addWidget(_title("All Report Print"))
        self.report = QComboBox()
        self.report.addItems(sorted(self.specs))
        self.date1 = QDateEdit()
        self.date2 = QDateEdit()
        for widget in (self.date1, self.date2):
            widget.setCalendarPopup(True)
            widget.setDisplayFormat("dd-MM-yyyy")
            widget.setDate(widget.date().currentDate())
        run = QPushButton("&Run")
        run.clicked.connect(self.run)
        printer = QPushButton("&Print")
        printer.clicked.connect(self.print_current)
        lay.addLayout(_row("Report", self.report, "From", self.date1,
                           "To", self.date2, run, printer))
        self.grid = _grid()
        lay.addWidget(self.grid, 1)
        self.status = QLabel()
        lay.addWidget(self.status)
        self._columns: list = []
        self._rows: list = []

    def _values(self) -> dict:
        start = self.date1.date().toString("yyyy-MM-dd")
        end = self.date2.date().toString("yyyy-MM-dd")
        return {"from": start, "to": end, "upto": end, "accode": "", "bcode": "",
                "grcode": "", "loanno": "", "year": end[:4]}

    def run(self):
        spec = self.specs.get(self.report.currentText())
        if spec is None:
            return
        try:
            self._columns, self._rows = spec.run(self._values())
        except Exception as exc:
            self._columns, self._rows = [], []
            self.status.setText(f"{spec.title} failed: {exc}")
            return
        _fill(self.grid, self._rows, self._columns)
        self.status.setText(f"{spec.title} — {len(self._rows)} rows")

    def print_current(self):
        if not self._rows:
            self.run()
        if not self._rows:
            QMessageBox.information(self, "All Report Print", "Nothing to print.")
            return
        print_table(self, self.report.currentText(), self._columns, self._rows)


class InchargeChangeForm(QWidget):
    """Change who is in charge (``w_incharge_select``)."""

    SETTING = "INCHARGE"

    def __init__(self, parsed=None, parent=None, seed=None):
        super().__init__(parent)
        lay = QVBoxLayout(self)
        lay.addWidget(_title("Change Incharge"))
        self.person = QComboBox()
        self.person.setEditable(True)
        self.person.setMinimumWidth(240)
        for row in _fetch("SELECT code, name FROM incharge_master ORDER BY name") or \
                _fetch("SELECT code, name FROM userm ORDER BY name"):
            self.person.addItem(f"{row.get('code')} — {row.get('name')}",
                                row.get("code"))
        apply = QPushButton("&Set")
        apply.clicked.connect(self.apply)
        lay.addLayout(_row("Incharge", self.person, apply))
        self.status = QLabel()
        lay.addWidget(self.status)
        lay.addStretch(1)
        self.refresh()

    def current(self) -> str:
        row = None
        try:
            row = db.fetch_one("SELECT cvalue FROM generali WHERE TRIM(code) = ?",
                               (self.SETTING,))
        except Exception:
            pass
        return str(row["cvalue"]) if row else ""

    def refresh(self):
        self.status.setText(f"Currently in charge: {self.current() or '(not set)'}")

    def apply(self):
        code = self.person.currentData() or self.person.currentText().strip()
        if not code:
            self.status.setText("Choose who is in charge.")
            return
        try:
            if self.current():
                db.execute("UPDATE generali SET cvalue = ? WHERE TRIM(code) = ?",
                           (code, self.SETTING))
            else:
                db.execute("INSERT INTO generali (code, cvalue) VALUES (?, ?)",
                           (self.SETTING, code))
        except Exception as exc:
            QMessageBox.warning(self, "Incharge", f"Could not set: {exc}")
            return
        self.refresh()


class PurityCertificateForm(QWidget):
    """Print a purity certificate for a sold piece (``w_puritycertificate``)."""

    def __init__(self, parsed=None, parent=None, seed=None):
        super().__init__(parent)
        lay = QVBoxLayout(self)
        lay.addWidget(_title("Purity Certificate"))
        self.billno = _edit(160)
        load = QPushButton("&Load bill")
        load.clicked.connect(self.load)
        printer = QPushButton("&Print")
        printer.clicked.connect(self.print_certificate)
        lay.addLayout(_row("Bill no", self.billno, load, printer))
        self.grid = _grid()
        lay.addWidget(self.grid, 1)
        self.status = QLabel()
        lay.addWidget(self.status)
        self._rows: list = []

    def load(self):
        billno = self.billno.text().strip()
        if not billno:
            self.status.setText("Enter the bill number.")
            return
        self._rows = _fetch(
            "SELECT m.billno AS billno, m.tdate AS tdate, m.custname AS customer, "
            "d.code AS code, d.qty AS qty, d.weight AS weight, "
            "d.stonewgt AS stonewgt, d.purity AS purity "
            "FROM salesm m, salesd d WHERE d.slno = m.slno AND TRIM(m.billno) = ?",
            (billno,))
        if not self._rows:
            self._rows = _fetch(
                "SELECT m.billno AS billno, m.tdate AS tdate, "
                "m.custname AS customer, d.code AS code, d.qty AS qty, "
                "d.weight AS weight, d.stonewgt AS stonewgt "
                "FROM salesm m, salesd d WHERE d.slno = m.slno "
                "AND TRIM(m.billno) = ?", (billno,))
        _fill(self.grid, self._rows)
        self.status.setText(f"{len(self._rows)} item(s) on bill {billno}")

    def print_certificate(self):
        if not self._rows:
            self.load()
        if not self._rows:
            QMessageBox.information(self, "Purity Certificate", "Nothing to print.")
            return
        print_table(self, f"Purity Certificate — {self.billno.text().strip()}",
                    list(self._rows[0].keys()), self._rows)


modules.register("w_allinone_report")(lambda parsed=None, **kw: AllReportsForm(parsed))
modules.register("w_incharge_select")(
    lambda parsed=None, **kw: InchargeChangeForm(parsed))
modules.register("w_puritycertificate")(
    lambda parsed=None, **kw: PurityCertificateForm(parsed))
