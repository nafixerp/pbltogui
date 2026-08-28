"""
The screens that reach outside the software.

These six windows talk to something the ERP does not own — another company's
database, a POS device file, the PSR file, a weighing machine, or a head-office
copy of the data. Each is implemented here as far as it can be without that
external piece in front of it:

* **Company Select** (``w_companyselect``) — lists the companies in ``company``
  (or the SQLite databases beside the software) and switches
  ``db_config.ini`` to the one you choose.
* **POS Download** (``w_pos_update``) and **PSR Reader** (``w_psr_viewer``) —
  open a delimited file, show what is in it, and import the rows into a table
  you choose, column by column, so nothing is guessed.
* **Update from HO** (``w_jewl_update``) and **Update from Jewelleries**
  (``w_order_update``) — copy rows that are missing locally from another
  database file of the same schema.
* **Show WM Weight** (``w_wgtshow``) — reads the weighing machine over a serial
  port when ``pyserial`` is installed, and always allows the weight to be typed.
"""

from __future__ import annotations

import configparser
import csv
import glob
import os
import sqlite3

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QComboBox, QFileDialog, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QMessageBox, QPushButton, QTableWidget, QTableWidgetItem, QTextEdit,
    QVBoxLayout, QWidget,
)

import db
from app import modules
from app.modules.extras import _edit, _fetch, _fill, _grid, _row, _title


# ---------------------------------------------------------------------------
# Company select
# ---------------------------------------------------------------------------

class CompanySelectForm(QWidget):
    """Choose which company database the software works on."""

    def __init__(self, parsed=None, parent=None, seed=None):
        super().__init__(parent)
        lay = QVBoxLayout(self)
        lay.addWidget(_title("Company Select"))
        lay.addWidget(QLabel(
            f"Current engine <b>{db.ENGINE}</b> — "
            f"<code>{db.SQLITE_PATH if db.ENGINE == 'sqlite' else db.CONFIG_PATH}</code>"))

        self.choice = QComboBox()
        self.choice.setMinimumWidth(420)
        self.choice.setEditable(True)
        for path in self._candidates():
            self.choice.addItem(path)
        browse = QPushButton("Browse…")
        browse.clicked.connect(self._browse)
        apply = QPushButton("&Select")
        apply.clicked.connect(self.apply)
        lay.addLayout(_row("Company database", self.choice, browse, apply))

        self.status = QLabel()
        lay.addWidget(self.status)
        self.grid = _grid()
        lay.addWidget(self.grid, 1)
        self.refresh()

    def _candidates(self) -> list:
        folder = os.path.dirname(os.path.abspath(db.SQLITE_PATH))
        found = sorted(glob.glob(os.path.join(folder, "*.db")))
        return found

    def refresh(self):
        rows = _fetch("SELECT * FROM company") or []
        if rows:
            _fill(self.grid, rows)
        self.status.setText("Choosing a company changes db_config.ini; "
                            "restart the software for it to take effect.")

    def _browse(self):
        path, _ = QFileDialog.getOpenFileName(self, "Company database",
                                              os.path.dirname(db.SQLITE_PATH),
                                              "Databases (*.db *.sqlite);;All files (*)")
        if path:
            self.choice.setEditText(path)

    def apply(self):
        path = self.choice.currentText().strip()
        if not path or not os.path.exists(path):
            self.status.setText("That database file does not exist.")
            return
        if QMessageBox.question(
                self, "Company Select",
                f"Work on {os.path.basename(path)} from the next start?",
                QMessageBox.Yes | QMessageBox.No, QMessageBox.No) != QMessageBox.Yes:
            return
        parser = configparser.ConfigParser()
        parser.read(db.CONFIG_PATH)
        if not parser.has_section("database"):
            parser.add_section("database")
        parser.set("database", "engine", "sqlite")
        if not parser.has_section("sqlite"):
            parser.add_section("sqlite")
        parser.set("sqlite", "path", path)
        with open(db.CONFIG_PATH, "w", encoding="utf-8") as fh:
            parser.write(fh)
        db.SQLITE_PATH = path
        self.status.setText(f"Company set to {path}. Restart to load it.")


# ---------------------------------------------------------------------------
# File import (POS download, PSR reader)
# ---------------------------------------------------------------------------

class FileImportForm(QWidget):
    """Read a delimited file and import the rows into a table."""

    def __init__(self, title: str, default_table: str = "", parsed=None,
                 parent=None, seed=None):
        super().__init__(parent)
        self._rows: list = []
        self._headers: list = []

        lay = QVBoxLayout(self)
        lay.addWidget(_title(title))
        lay.addWidget(QLabel(
            "Open the file, check the rows below, choose the table and map each "
            "column. Nothing is imported until you press Import."))

        self.path = _edit(380)
        browse = QPushButton("Open file…")
        browse.clicked.connect(self.open_file)
        lay.addLayout(_row("File", self.path, browse))

        self.table = QComboBox()
        self.table.setEditable(True)
        self.table.setMinimumWidth(200)
        if default_table:
            self.table.addItem(default_table)
        self.table.currentTextChanged.connect(lambda _t: self._build_mapping())
        self.mapping_box = QGroupBox("Columns")
        self.mapping_lay = QVBoxLayout(self.mapping_box)
        run = QPushButton("&Import")
        run.clicked.connect(self.do_import)
        lay.addLayout(_row("Into table", self.table, run))
        lay.addWidget(self.mapping_box)

        self.grid = _grid()
        lay.addWidget(self.grid, 1)
        self.status = QLabel()
        lay.addWidget(self.status)
        self._maps: list = []

    def open_file(self):
        path, _ = QFileDialog.getOpenFileName(
            self, "Open file", "", "Data files (*.csv *.txt *.dat);;All files (*)")
        if path:
            self.path.setText(path)
            self.load(path)

    def load(self, path: str = ""):
        """Read the file at ``path`` (or the one in the box) into the preview."""
        path = path or self.path.text().strip()
        try:
            with open(path, newline="", encoding="utf-8", errors="replace") as fh:
                sample = fh.read(4096)
                fh.seek(0)
                try:
                    dialect = csv.Sniffer().sniff(sample, delimiters=",;|\t")
                except csv.Error:
                    dialect = csv.excel
                reader = csv.reader(fh, dialect)
                rows = [r for r in reader if any(str(c).strip() for c in r)]
        except Exception as exc:
            self.status.setText(f"Could not read the file: {exc}")
            return
        if not rows:
            self.status.setText("The file is empty.")
            return
        self._headers = [c.strip() or f"col{i + 1}"
                         for i, c in enumerate(rows[0])]
        self._rows = [dict(zip(self._headers, r)) for r in rows[1:]]
        _fill(self.grid, self._rows[:200], self._headers)
        self.status.setText(f"{len(self._rows)} row(s) in the file")
        self._build_mapping()

    def _build_mapping(self):
        while self.mapping_lay.count():
            item = self.mapping_lay.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        self._maps = []
        table = self.table.currentText().strip()
        if not table or not self._headers:
            return
        columns = [c["name"] for c in db.table_columns(table)]
        if not columns:
            self.mapping_lay.addWidget(QLabel(f"Table '{table}' is not in this "
                                              f"database."))
            return
        for header in self._headers:
            box = QComboBox()
            box.addItem("(skip)", "")
            for column in columns:
                box.addItem(column, column)
            match = next((c for c in columns if c.lower() == header.lower()), None)
            if match:
                box.setCurrentText(match)
            self.mapping_lay.addLayout(_row(header, box))
            self._maps.append((header, box))

    def do_import(self):
        table = self.table.currentText().strip()
        pairs = [(h, b.currentData()) for h, b in self._maps if b.currentData()]
        if not (table and pairs and self._rows):
            self.status.setText("Open a file, choose the table and map at least "
                                "one column.")
            return
        columns = [c for _h, c in pairs]
        placeholders = ", ".join("?" for _ in columns)
        imported = 0
        try:
            with db.transaction():
                for row in self._rows:
                    db.execute(
                        f"INSERT INTO {table} ({', '.join(columns)}) "
                        f"VALUES ({placeholders})",
                        [row.get(h) for h, _c in pairs])
                    imported += 1
        except Exception as exc:
            self.status.setText(f"Import failed after {imported} row(s), "
                                f"nothing was written: {exc}")
            return
        self.status.setText(f"Imported {imported} row(s) into {table}.")


# ---------------------------------------------------------------------------
# Copy from another database (HO / jewellery branch)
# ---------------------------------------------------------------------------

class DatabaseSyncForm(QWidget):
    """Copy rows that are missing locally from another database of the same schema."""

    def __init__(self, title: str, tables: list, parsed=None, parent=None, seed=None):
        super().__init__(parent)
        self.tables = tables
        lay = QVBoxLayout(self)
        lay.addWidget(_title(title))
        lay.addWidget(QLabel(
            "Choose the other copy of the database. Rows whose key is not here "
            "yet are copied in; nothing already here is overwritten."))

        self.path = _edit(380)
        browse = QPushButton("Choose database…")
        browse.clicked.connect(self._browse)
        self.table = QComboBox()
        self.table.addItems(tables)
        run = QPushButton("&Update")
        run.clicked.connect(self.sync)
        lay.addLayout(_row("Source", self.path, browse, "Table", self.table, run))

        self.log = QTextEdit()
        self.log.setReadOnly(True)
        lay.addWidget(self.log, 1)

    def _browse(self):
        path, _ = QFileDialog.getOpenFileName(
            self, "Source database", "", "Databases (*.db *.sqlite);;All files (*)")
        if path:
            self.path.setText(path)

    def sync(self):
        source = self.path.text().strip()
        table = self.table.currentText()
        if not os.path.exists(source):
            self.log.append("Choose the source database first.")
            return
        try:
            conn = sqlite3.connect(source)
            conn.row_factory = sqlite3.Row
            rows = [dict(r) for r in conn.execute(f"SELECT * FROM {table}")]
            conn.close()
        except Exception as exc:
            self.log.append(f"Could not read {table} from the source: {exc}")
            return

        local = {c["name"] for c in db.table_columns(table)}
        if not local:
            self.log.append(f"Table '{table}' is not in this database.")
            return
        key = "slno" if "slno" in local else next(iter(sorted(local)))
        existing = {str(r[key]) for r in _fetch(f"SELECT {key} FROM {table}")}
        copied = 0
        try:
            with db.transaction():
                for row in rows:
                    if str(row.get(key)) in existing:
                        continue
                    usable = {k: v for k, v in row.items() if k in local}
                    if not usable:
                        continue
                    db.execute(
                        f"INSERT INTO {table} ({', '.join(usable)}) "
                        f"VALUES ({', '.join('?' for _ in usable)})",
                        list(usable.values()))
                    copied += 1
        except Exception as exc:
            self.log.append(f"Update failed, nothing written: {exc}")
            return
        self.log.append(f"{table}: {copied} new row(s) copied "
                        f"({len(rows)} in the source).")


# ---------------------------------------------------------------------------
# Weighing machine
# ---------------------------------------------------------------------------

class WeighingMachineForm(QWidget):
    """Show the weight from the weighing machine (``w_wgtshow``)."""

    def __init__(self, parsed=None, parent=None, seed=None):
        super().__init__(parent)
        lay = QVBoxLayout(self)
        lay.addWidget(_title("Weighing Machine"))

        self.port = QComboBox()
        self.port.setEditable(True)
        self.port.addItems(self._ports())
        read = QPushButton("&Read")
        read.clicked.connect(self.read_weight)
        lay.addLayout(_row("Port", self.port, read))

        self.weight = QLabel("0.000")
        font = self.weight.font()
        font.setPointSize(36)
        font.setBold(True)
        self.weight.setFont(font)
        self.weight.setAlignment(Qt.AlignCenter)
        lay.addWidget(self.weight, 1)

        self.manual = _edit(140)
        use = QPushButton("Use typed weight")
        use.clicked.connect(lambda: self.weight.setText(self.manual.text().strip()
                                                        or "0.000"))
        lay.addLayout(_row("Or type", self.manual, use))
        self.status = QLabel()
        lay.addWidget(self.status)

    def _ports(self) -> list:
        try:
            from serial.tools import list_ports
        except Exception:
            return ["COM1", "COM2", "COM3", "/dev/ttyUSB0"]
        return [p.device for p in list_ports.comports()] or ["COM1"]

    def read_weight(self):
        try:
            import serial
        except Exception:
            self.status.setText(
                "pyserial is not installed, so the machine cannot be read here. "
                "Install it (pip install pyserial) or type the weight below.")
            return
        try:
            with serial.Serial(self.port.currentText(), 9600, timeout=2) as link:
                line = link.readline().decode("ascii", "ignore").strip()
        except Exception as exc:
            self.status.setText(f"Could not read the machine: {exc}")
            return
        digits = "".join(ch for ch in line if ch.isdigit() or ch == ".")
        self.weight.setText(digits or "0.000")
        self.status.setText(f"Read: {line!r}")


modules.register("w_companyselect")(
    lambda parsed=None, **kw: CompanySelectForm(parsed))
modules.register("w_pos_update")(
    lambda parsed=None, **kw: FileImportForm("POS Download", "kuricolln", parsed))
modules.register("w_psr_viewer")(
    lambda parsed=None, **kw: FileImportForm("PSR Reader", "", parsed))
modules.register("w_jewl_update")(
    lambda parsed=None, **kw: DatabaseSyncForm(
        "Update from HO", ["smithm", "smithd", "items", "clients"], parsed))
modules.register("w_order_update")(
    lambda parsed=None, **kw: DatabaseSyncForm(
        "Update from Jewelleries", ["orderm", "orderd", "smithm", "smithd"], parsed))
modules.register("w_wgtshow")(
    lambda parsed=None, **kw: WeighingMachineForm(parsed))
