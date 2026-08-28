"""
Jewellery ERP Enterprise — application entry point.

Migrated from the GMINE PowerBuilder application to PySide6. Boots the database
layer, authenticates the user (password-only, like the original ``w_passverify``)
and opens the full ERP shell with every Master, Transaction, Report and Utility
module available.
"""

from __future__ import annotations

import sys

from PySide6.QtWidgets import QApplication, QMessageBox

import db
from app.ui.login import LoginDialog
from app.ui.main_window import MainWindow


def main() -> int:
    app = QApplication(sys.argv)
    app.setApplicationName("Jewellery ERP Enterprise")

    # Prepare the database (creates/seeds the SQLite test schema; connects only
    # for an existing external database, per db.init_db()).
    try:
        db.init_db()
    except Exception as exc:
        QMessageBox.warning(None, "Database",
                            f"Database initialisation warning:\n{exc}\n\n"
                            "The application will continue; some screens may be "
                            "unavailable until the database is reachable.")

    login = LoginDialog()
    if login.exec() != LoginDialog.Accepted:
        return 0

    window = MainWindow(user=login.user)
    window.show()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
