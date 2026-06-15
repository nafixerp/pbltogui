"""
Jewellery ERP — PowerBuilder → Python (PySide6) entry point.

Boots the Qt application, initialises the database (creating the SQLite demo
schema when configured that way), shows the password-only login (port of
``w_passverify``) and then the MDI frame carrying the full original menu.

    python main.py

Environment:
    PB_SOURCE   path to the pbl folder or pbl.zip (auto-detected otherwise)
    DB_CONFIG   path to db_config.ini (defaults to ./config/db_config.ini)
"""

from __future__ import annotations

import os
import sys

# allow ``python main.py`` from the pygui directory
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def main() -> int:
    from PySide6.QtWidgets import QApplication, QMessageBox

    app = QApplication(sys.argv)
    app.setApplicationName("Jewellery ERP")

    # locate the PowerBuilder source up front so we fail fast with a clear msg
    from pbconvert import default_source
    try:
        source = default_source()
    except Exception as exc:
        QMessageBox.critical(None, "PB source not found", str(exc))
        return 2

    # database init (no-op for an existing external DB; builds demo SQLite)
    from runtime import db
    try:
        db.init_db()
    except Exception as exc:
        print(f"DB init warning: {exc}")

    # company info into the shared app state
    from runtime.appstate import app_state
    here = os.path.dirname(os.path.abspath(__file__))
    for ini in (os.path.join(here, "config", "Soft.ini"),
                os.path.join(os.path.dirname(here), "Soft.ini")):
        if os.path.exists(ini):
            app_state.load_company_from_ini(ini)
            break

    # login
    from ui.login_window import LoginDialog
    dlg = LoginDialog()
    if dlg.exec() != dlg.DialogCode.Accepted:
        return 0
    if dlg.user:
        app_state.gsuserid = dlg.user.get("code", "")
        app_state.gsusername = dlg.user.get("name", "")

    # main frame
    from ui.main_window import MainWindow
    win = MainWindow(source=source, user=dlg.user)
    win.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
