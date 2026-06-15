"""
Login dialog — port of ``w_passverify`` (gminestr).

The original asks for a PASSWORD only.  It encrypts the entry with
``fpencrypt(pwd, 1)`` and matches it against ``userm.pcode``.  If there are no
users yet, access is granted (the same fallback the original used on a fresh
database).  This is delegated to ``runtime.db.validate_login``.
"""

from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QFrame,
)


class LoginDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Password Verification")
        self.setMinimumWidth(360)
        self.user = None
        self._attempts = 0

        root = QVBoxLayout(self)
        title = QLabel("Jewellery ERP")
        title.setStyleSheet("font-size:18px; font-weight:bold;")
        title.setAlignment(Qt.AlignCenter)
        root.addWidget(title)

        sub = QLabel("Enter Password")
        sub.setAlignment(Qt.AlignCenter)
        root.addWidget(sub)

        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        root.addWidget(line)

        self.pwd = QLineEdit()
        self.pwd.setEchoMode(QLineEdit.Password)
        self.pwd.setPlaceholderText("Password")
        self.pwd.returnPressed.connect(self._verify)
        root.addWidget(self.pwd)

        self.status = QLabel("")
        self.status.setStyleSheet("color:#c0392b;")
        self.status.setAlignment(Qt.AlignCenter)
        root.addWidget(self.status)

        btns = QHBoxLayout()
        ok = QPushButton("OK")
        ok.setDefault(True)
        ok.clicked.connect(self._verify)
        cancel = QPushButton("Exit")
        cancel.clicked.connect(self.reject)
        btns.addStretch(1)
        btns.addWidget(ok)
        btns.addWidget(cancel)
        root.addLayout(btns)

        self.pwd.setFocus()

    def _verify(self):
        from runtime import db
        pwd = self.pwd.text()
        try:
            user = db.validate_login(pwd)
        except Exception as exc:
            self.status.setText(f"Login error: {exc}")
            return
        if user:
            self.user = user
            try:
                db.write_login_history(user.get("code", ""))
            except Exception:
                pass
            self.accept()
        else:
            self._attempts += 1
            self.status.setText("Wrong Password...")
            self.pwd.clear()
            self.pwd.setFocus()
            if self._attempts >= 5:
                self.reject()
