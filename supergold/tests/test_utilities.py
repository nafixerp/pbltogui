"""Day Lock, Backup and Reminders do their real work."""

import datetime
import os
import sys

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

import db  # noqa: E402

pytest.importorskip("PySide6.QtWidgets")
from PySide6.QtWidgets import QApplication  # noqa: E402

from app.modules.utilities import (  # noqa: E402
    BackupForm, DayLockForm, ReminderForm, backup_database)


@pytest.fixture(scope="session")
def qapp():
    return QApplication.instance() or QApplication([])


@pytest.fixture()
def local_db(tmp_path, monkeypatch):
    monkeypatch.setattr(db, "ENGINE", "sqlite")
    monkeypatch.setattr(db, "SQLITE_PATH", str(tmp_path / "util.db"))
    db.execute("CREATE TABLE daylock (tdate DATE)")
    db.execute("CREATE TABLE reminder (tdate DATE, part TEXT)")
    return tmp_path


def _set_range(form, start, end):
    from PySide6.QtCore import QDate
    form.date1.setDate(QDate(*start))
    form.date2.setDate(QDate(*end))


def test_lock_inserts_one_row_per_day(qapp, local_db):
    form = DayLockForm()
    _set_range(form, (2026, 6, 1), (2026, 6, 3))
    form.lock()
    rows = db.fetch_all("SELECT tdate FROM daylock ORDER BY tdate")
    assert [r["tdate"] for r in rows] == ["2026-06-01", "2026-06-02", "2026-06-03"]
    assert "3 date(s)" in form.status.text()


def test_locking_twice_does_not_duplicate(qapp, local_db):
    form = DayLockForm()
    _set_range(form, (2026, 6, 1), (2026, 6, 2))
    form.lock()
    form.lock()
    assert db.fetch_one("SELECT COUNT(*) AS c FROM daylock")["c"] == 2


def test_unlock_clears_the_range(qapp, local_db):
    form = DayLockForm()
    _set_range(form, (2026, 6, 1), (2026, 6, 5))
    form.lock()
    _set_range(form, (2026, 6, 2), (2026, 6, 4))
    form.unlock()
    rows = [r["tdate"] for r in db.fetch_all("SELECT tdate FROM daylock ORDER BY tdate")]
    assert rows == ["2026-06-01", "2026-06-05"]


def test_backup_copies_the_sqlite_database(qapp, local_db, tmp_path):
    target = tmp_path / "backups"
    message = backup_database(str(target))
    files = list(target.glob("jewellery_*.db"))
    assert len(files) == 1 and files[0].stat().st_size > 0
    assert str(target) in message


def test_backup_form_logs_the_result(qapp, local_db, tmp_path):
    form = BackupForm()
    form.folder.setText(str(tmp_path / "b2"))
    form.run()
    assert "Backup written to" in form.log.toPlainText()


def test_reminders_add_and_delete(qapp, local_db):
    form = ReminderForm()
    form.note.setText("Call the goldsmith")
    form.add()
    rows = db.fetch_all("SELECT * FROM reminder")
    assert len(rows) == 1 and rows[0]["part"] == "Call the goldsmith"
    form.grid.selectRow(0)
    form.delete()
    assert db.fetch_all("SELECT * FROM reminder") == []


def test_change_password_updates_the_stored_code(qapp, local_db, monkeypatch):
    from pb_compat import fpencrypt
    from app.modules.utilities import ChangePasswordForm
    db.execute("CREATE TABLE userm (code TEXT, name TEXT, pcode TEXT)")
    db.execute("INSERT INTO userm VALUES ('U1','Ravi',?)", (fpencrypt("old1", 1),))

    form = ChangePasswordForm()
    form.fields["old"].setText("old1")
    form.fields["new"].setText("new2")
    form.fields["again"].setText("new2")
    form.change()

    assert form.status.text() == "Password changed."
    assert db.fetch_one("SELECT pcode FROM userm")["pcode"] == fpencrypt("new2", 1)


def test_change_password_checks_the_old_one(qapp, local_db):
    from pb_compat import fpencrypt
    from app.modules.utilities import ChangePasswordForm
    db.execute("CREATE TABLE userm (code TEXT, name TEXT, pcode TEXT)")
    db.execute("INSERT INTO userm VALUES ('U1','Ravi',?)", (fpencrypt("right", 1),))

    form = ChangePasswordForm()
    form.fields["old"].setText("wrong")
    form.fields["new"].setText("x")
    form.fields["again"].setText("x")
    form.change()
    assert "current password is wrong" in form.status.text()
    assert db.fetch_one("SELECT pcode FROM userm")["pcode"] == fpencrypt("right", 1)


def test_change_password_requires_matching_repeat(qapp, local_db):
    from app.modules.utilities import ChangePasswordForm
    form = ChangePasswordForm()
    form.fields["new"].setText("a")
    form.fields["again"].setText("b")
    form.change()
    assert "do not match" in form.status.text()
