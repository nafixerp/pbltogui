"""
Utilities: Day Lock, Backup, Calendar and Reminders.

These are the housekeeping screens of the original application. Each is a small
window with a real action behind it, so they are hand-written here rather than
rendered generically:

* **Day Lock** — inserts one ``daylock`` row per date in the range (Unlock
  deletes them), exactly as ``w_daylock`` did.
* **Backup** — copies the SQLite file, or asks SQL Anywhere / SQL Server to back
  the database up into the folder you choose.
* **Calendar** — the desk calendar of ``w_calander1``.
* **Reminders** — the ``reminder`` list, with add and delete.
"""

from __future__ import annotations

import datetime
import os
import shutil

from PySide6.QtCore import QDate, Qt
from PySide6.QtWidgets import (
    QCalendarWidget, QFileDialog, QDateEdit, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QMessageBox, QPushButton, QTableWidget, QTableWidgetItem,
    QTextEdit, QVBoxLayout, QWidget,
)

import db
from app import modules


def _header(text: str) -> QLabel:
    label = QLabel(f"<h3>{text}</h3>")
    label.setTextFormat(Qt.RichText)
    return label


def _date_edit(value: datetime.date | None = None) -> QDateEdit:
    value = value or datetime.date.today()
    w = QDateEdit()
    w.setCalendarPopup(True)
    w.setDisplayFormat("dd-MM-yyyy")
    w.setDate(QDate(value.year, value.month, value.day))
    return w


# ---------------------------------------------------------------------------
# Day Lock
# ---------------------------------------------------------------------------

class DayLockForm(QWidget):
    """Lock a range of dates against further transactions (``w_daylock``)."""

    def __init__(self, parsed=None, parent=None, seed=None):
        super().__init__(parent)
        lay = QVBoxLayout(self)
        lay.addWidget(_header("Day Lock"))

        row = QHBoxLayout()
        row.addWidget(QLabel("From"))
        self.date1 = _date_edit()
        row.addWidget(self.date1)
        row.addWidget(QLabel("To"))
        self.date2 = _date_edit()
        row.addWidget(self.date2)
        lock = QPushButton("&Lock")
        lock.clicked.connect(self.lock)
        unlock = QPushButton("&Unlock")
        unlock.clicked.connect(self.unlock)
        row.addWidget(lock)
        row.addWidget(unlock)
        row.addStretch(1)
        lay.addLayout(row)

        self.status = QLabel()
        self.status.setStyleSheet("color:#b00020;font-weight:600;")
        lay.addWidget(self.status)

        box = QGroupBox("Locked dates")
        box_lay = QVBoxLayout(box)
        self.grid = QTableWidget(0, 1)
        self.grid.setHorizontalHeaderLabels(["Date"])
        self.grid.setEditTriggers(QTableWidget.NoEditTriggers)
        box_lay.addWidget(self.grid)
        lay.addWidget(box, 1)
        self.refresh()

    # -- data ------------------------------------------------------------
    def _range(self):
        return (self.date1.date().toString("yyyy-MM-dd"),
                self.date2.date().toString("yyyy-MM-dd"))

    def refresh(self):
        try:
            rows = db.fetch_all("SELECT tdate FROM daylock ORDER BY tdate")
        except Exception as exc:
            self.status.setText(f"daylock table unavailable: {exc}")
            return
        self.grid.setRowCount(len(rows))
        for r, row in enumerate(rows):
            self.grid.setItem(r, 0, QTableWidgetItem(str(row.get("tdate", ""))))

    def lock(self):
        start, end = self._range()
        if start > end:
            QMessageBox.warning(self, "Day Lock", "The From date is after the To date.")
            return
        day = datetime.date.fromisoformat(start)
        last = datetime.date.fromisoformat(end)
        added = 0
        try:
            existing = {str(r["tdate"])[:10] for r in db.fetch_all(
                "SELECT tdate FROM daylock WHERE tdate >= ? AND tdate <= ?",
                (start, end))}
            while day <= last:
                if day.isoformat() not in existing:
                    db.execute("INSERT INTO daylock (tdate) VALUES (?)",
                               (day.isoformat(),))
                    added += 1
                day += datetime.timedelta(days=1)
        except Exception as exc:
            QMessageBox.warning(self, "Day Lock", f"Could not lock: {exc}")
            return
        self.status.setText(f"Locked — {added} date(s) added.")
        self.refresh()

    def unlock(self):
        start, end = self._range()
        try:
            db.execute("DELETE FROM daylock WHERE tdate >= ? AND tdate <= ?",
                       (start, end))
        except Exception as exc:
            QMessageBox.warning(self, "Day Lock", f"Could not unlock: {exc}")
            return
        self.status.setText("Unlocked.")
        self.refresh()


# ---------------------------------------------------------------------------
# Backup
# ---------------------------------------------------------------------------

def backup_database(folder: str) -> str:
    """Back the configured database up into ``folder``; returns a message."""
    os.makedirs(folder, exist_ok=True)
    stamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    if db.ENGINE == "sqlite":
        target = os.path.join(folder, f"jewellery_{stamp}.db")
        shutil.copy2(db.SQLITE_PATH, target)
        return f"Backup written to {target}"
    if db.ENGINE == "sqlanywhere":
        db.execute(f"BACKUP DATABASE DIRECTORY '{folder}'")
        return f"SQL Anywhere backed the database up into {folder}"
    database = db._ss("database", "JewelleryERP")
    target = os.path.join(folder, f"{database}_{stamp}.bak")
    db.execute(f"BACKUP DATABASE [{database}] TO DISK = ?", (target,))
    return f"SQL Server backup written to {target}"


class BackupForm(QWidget):
    """Take a backup of the live database (``w_backup``)."""

    def __init__(self, parsed=None, parent=None, seed=None):
        super().__init__(parent)
        lay = QVBoxLayout(self)
        lay.addWidget(_header("Backup"))
        lay.addWidget(QLabel(
            f"Engine: <b>{db.ENGINE}</b>. Choose the folder to write the "
            "backup into."))

        row = QHBoxLayout()
        self.folder = QLineEdit(os.path.join(os.path.expanduser("~"), "Backup"))
        row.addWidget(self.folder, 1)
        browse = QPushButton("Browse…")
        browse.clicked.connect(self._browse)
        row.addWidget(browse)
        run = QPushButton("Take &Backup")
        run.clicked.connect(self.run)
        row.addWidget(run)
        lay.addLayout(row)

        self.log = QTextEdit()
        self.log.setReadOnly(True)
        lay.addWidget(self.log, 1)

    def _browse(self):
        path = QFileDialog.getExistingDirectory(self, "Backup folder",
                                                self.folder.text())
        if path:
            self.folder.setText(path)

    def run(self):
        try:
            message = backup_database(self.folder.text().strip())
        except Exception as exc:
            message = f"Backup failed: {exc}"
        self.log.append(f"{datetime.datetime.now():%d-%m-%Y %H:%M}  {message}")


# ---------------------------------------------------------------------------
# Calendar and reminders
# ---------------------------------------------------------------------------

class CalendarForm(QWidget):
    def __init__(self, parsed=None, parent=None, seed=None):
        super().__init__(parent)
        lay = QVBoxLayout(self)
        lay.addWidget(_header("Calendar"))
        calendar = QCalendarWidget()
        calendar.setGridVisible(True)
        lay.addWidget(calendar, 1)


class ReminderForm(QWidget):
    """The reminder list, with add and delete (``w_reminderrep``)."""

    def __init__(self, parsed=None, parent=None, seed=None):
        super().__init__(parent)
        lay = QVBoxLayout(self)
        lay.addWidget(_header("Reminders"))

        row = QHBoxLayout()
        row.addWidget(QLabel("Date"))
        self.date = _date_edit()
        row.addWidget(self.date)
        row.addWidget(QLabel("Note"))
        self.note = QLineEdit()
        row.addWidget(self.note, 1)
        add = QPushButton("&Add")
        add.clicked.connect(self.add)
        row.addWidget(add)
        remove = QPushButton("&Delete")
        remove.clicked.connect(self.delete)
        row.addWidget(remove)
        lay.addLayout(row)

        self.grid = QTableWidget(0, 0)
        self.grid.setEditTriggers(QTableWidget.NoEditTriggers)
        self.grid.setSelectionBehavior(QTableWidget.SelectRows)
        lay.addWidget(self.grid, 1)
        self.status = QLabel()
        lay.addWidget(self.status)
        self.refresh()

    def _columns(self) -> list:
        return [c["name"] for c in db.table_columns("reminder")]

    def refresh(self):
        try:
            self._rows = db.fetch_all("SELECT * FROM reminder ORDER BY 1")
        except Exception as exc:
            self._rows = []
            self.status.setText(f"reminder table unavailable: {exc}")
            return
        cols = list(self._rows[0].keys()) if self._rows else self._columns()
        self.grid.setColumnCount(len(cols))
        self.grid.setHorizontalHeaderLabels(cols)
        self.grid.setRowCount(len(self._rows))
        for r, row in enumerate(self._rows):
            for c, col in enumerate(cols):
                value = row.get(col)
                self.grid.setItem(r, c, QTableWidgetItem(
                    "" if value is None else str(value)))
        self.grid.resizeColumnsToContents()
        self.status.setText(f"{len(self._rows)} reminders")

    def add(self):
        cols = self._columns()
        date_col = next((c for c in cols if "date" in c.lower()), None)
        text_col = next((c for c in cols
                         if c.lower() in ("part", "note", "remarks", "reminder",
                                          "particulars", "name")), None)
        if not date_col or not text_col:
            QMessageBox.warning(self, "Reminders",
                                "The reminder table has no date/note columns.")
            return
        try:
            db.execute(f"INSERT INTO reminder ({date_col}, {text_col}) VALUES (?, ?)",
                       (self.date.date().toString("yyyy-MM-dd"),
                        self.note.text().strip()))
        except Exception as exc:
            QMessageBox.warning(self, "Reminders", f"Could not add: {exc}")
            return
        self.note.clear()
        self.refresh()

    def delete(self):
        idx = self.grid.currentRow()
        if idx < 0 or idx >= len(self._rows):
            QMessageBox.information(self, "Reminders", "Select a reminder first.")
            return
        row = self._rows[idx]
        clause = " AND ".join(f"{c} IS ?" if row[c] is None else f"{c} = ?"
                              for c in row)
        try:
            db.execute(f"DELETE FROM reminder WHERE {clause}", list(row.values()))
        except Exception as exc:
            QMessageBox.warning(self, "Reminders", f"Could not delete: {exc}")
            return
        self.refresh()


modules.register("w_daylock")(lambda parsed=None, **kw: DayLockForm(parsed))
modules.register("w_backup")(lambda parsed=None, **kw: BackupForm(parsed))
modules.register("w_calander1")(lambda parsed=None, **kw: CalendarForm(parsed))
modules.register("w_reminderrep")(lambda parsed=None, **kw: ReminderForm(parsed))


# ---------------------------------------------------------------------------
# Change password / About
# ---------------------------------------------------------------------------

class ChangePasswordForm(QWidget):
    """Change a user's password (``w_passverify2``).

    Passwords are stored the way the original stored them: ``userm.pcode``
    holds ``fpencrypt(password, 1)``.
    """

    def __init__(self, parsed=None, parent=None, seed=None):
        super().__init__(parent)
        from pb_compat import fpencrypt
        self._encrypt = fpencrypt

        lay = QVBoxLayout(self)
        lay.addWidget(_header("Change Password"))

        self.fields = {}
        for key, caption in (("old", "Current password"),
                             ("new", "New password"),
                             ("again", "Repeat new password")):
            row = QHBoxLayout()
            row.addWidget(QLabel(caption))
            edit = QLineEdit()
            edit.setEchoMode(QLineEdit.Password)
            edit.setMaximumWidth(220)
            row.addWidget(edit)
            row.addStretch(1)
            lay.addLayout(row)
            self.fields[key] = edit

        change = QPushButton("&Change")
        change.clicked.connect(self.change)
        lay.addWidget(change, 0, Qt.AlignLeft)
        self.status = QLabel()
        lay.addWidget(self.status)
        lay.addStretch(1)

    def change(self):
        old = self.fields["old"].text()
        new = self.fields["new"].text()
        again = self.fields["again"].text()
        if not new:
            self.status.setText("Enter a new password.")
            return
        if new != again:
            self.status.setText("The two new passwords do not match.")
            return
        user = db.validate_login(old)
        if user is None:
            self.status.setText("The current password is wrong.")
            return
        try:
            db.execute("UPDATE userm SET pcode = ? WHERE code = ?",
                       (self._encrypt(new, 1), user.get("code", "")))
        except Exception as exc:
            self.status.setText(f"Could not change the password: {exc}")
            return
        for edit in self.fields.values():
            edit.clear()
        self.status.setText("Password changed.")


class AboutForm(QWidget):
    """The About window (``w_about``)."""

    def __init__(self, parsed=None, parent=None, seed=None):
        super().__init__(parent)
        lay = QVBoxLayout(self)
        lay.addWidget(_header("Super Gold — Jewellery ERP"))
        lay.addWidget(QLabel(
            "Converted from the GMINE PowerBuilder application to Python / "
            "PySide6.<br><br>"
            f"Database engine: <b>{db.ENGINE}</b><br>"
            "Menu, screens and reports are generated from the original "
            "PowerBuilder definitions — see README.md."))
        lay.addStretch(1)


modules.register("w_passverify2")(lambda parsed=None, **kw: ChangePasswordForm(parsed))
modules.register("w_about")(lambda parsed=None, **kw: AboutForm(parsed))
