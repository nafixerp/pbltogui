"""Password-only login dialog — port of the GMINE ``w_passverify`` window."""

from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QDialog, QFormLayout, QHBoxLayout, QLabel, QLineEdit, QMessageBox,
    QPushButton, QVBoxLayout,
)

import db


class LoginDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Jewellery ERP — Login")
        self.setModal(True)
        self.user = None

        layout = QVBoxLayout(self)
        title = QLabel("Jewellery ERP Enterprise")
        title.setStyleSheet("font-size:18px;font-weight:600;")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        layout.addWidget(QLabel("Enter password to continue."))

        form = QFormLayout()
        self.pwd = QLineEdit()
        self.pwd.setEchoMode(QLineEdit.Password)
        self.pwd.returnPressed.connect(self._accept)
        form.addRow("Password:", self.pwd)
        layout.addLayout(form)

        buttons = QHBoxLayout()
        ok = QPushButton("Login")
        ok.setDefault(True)
        ok.clicked.connect(self._accept)
        cancel = QPushButton("Cancel")
        cancel.clicked.connect(self.reject)
        buttons.addStretch(1)
        buttons.addWidget(ok)
        buttons.addWidget(cancel)
        layout.addLayout(buttons)
        self.resize(360, 160)

    def _accept(self):
        try:
            user = db.validate_login(self.pwd.text())
        except Exception as exc:  # connection/setup problems
            QMessageBox.critical(self, "Login", f"Login failed:\n{exc}")
            return
        if user is None:
            QMessageBox.warning(self, "Login", "Invalid password.")
            self.pwd.selectAll()
            return
        self.user = user
        try:
            db.write_login_history(user.get("code", ""))
        except Exception:
            pass
        self.accept()
