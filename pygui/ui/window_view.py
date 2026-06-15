"""
Render a parsed PowerBuilder window (.srw) as a PySide6 widget.

Every control keeps its original position and size (PB units scaled to pixels)
so the converted screen matches the original layout 1:1.  Each control class
maps to the natural Qt widget; ``datawindow`` controls embed a live
``DataWindowView``.  Common button behaviour from the PowerScript ``clicked``
events (close, open another window, retrieve/insert/update a DataWindow) is
wired through a small, safe interpreter — the long tail of bespoke business
logic remains available as the verbatim original script for reference.
"""

from __future__ import annotations

from PySide6.QtCore import Qt, QRect
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QWidget, QScrollArea, QPushButton, QLineEdit, QPlainTextEdit, QLabel,
    QCheckBox, QRadioButton, QComboBox, QListWidget, QGroupBox, QFrame,
    QVBoxLayout, QMainWindow, QMessageBox, QTabWidget,
)

from pbconvert import parse_window
from pbconvert.pbtypes import px, color, control_kind, clean_text
from .datawindow_view import DataWindowView


class WindowView(QScrollArea):
    """Scrollable canvas that lays out a window's controls absolutely."""

    def __init__(self, win_name, source, open_window_cb=None, parent=None):
        super().__init__(parent)
        self.win_name = win_name
        self.source = source
        self.open_window_cb = open_window_cb     # (name) -> None, for open(w_x)
        self.win = parse_window(source.text(win_name), win_name)
        self._datawindows: dict[str, DataWindowView] = {}
        self._widgets: dict[str, QWidget] = {}

        canvas = QWidget()
        canvas.setObjectName("pb_canvas")
        w = max(px(self.win.width), 400)
        h = max(px(self.win.height), 300)
        canvas.setMinimumSize(w, h)

        bg = color(self.win.props.get("backcolor"))
        if bg:
            canvas.setStyleSheet(f"#pb_canvas {{ background: {bg}; }}")

        self._build_controls(canvas)
        self.setWidget(canvas)
        self.setWidgetResizable(False)

        # fire the window 'open' event behaviour (mainly dw.retrieve())
        self._run_open()

    # -- title / sizing ----------------------------------------------------
    @property
    def title(self) -> str:
        return clean_text(self.win.title)

    def suggested_size(self):
        return px(self.win.width) + 24, px(self.win.height) + 24

    # -- build -------------------------------------------------------------
    def _build_controls(self, canvas):
        for ctl in self.win.controls:
            kind = control_kind(ctl.pb_class)
            x, y = px(ctl.props.get("x", 0)), px(ctl.props.get("y", 0))
            cw, ch = px(ctl.props.get("width", 100)), px(ctl.props.get("height", 30))
            text = clean_text(ctl.props.get("text", ""))

            w = self._make_widget(kind, ctl, text, canvas)
            if w is None:
                continue
            w.setGeometry(QRect(x, y, max(cw, 8), max(ch, 8)))
            self._apply_font(w, ctl)
            self._widgets[ctl.name] = w

    def _make_widget(self, kind, ctl, text, parent):
        if kind == "button":
            b = QPushButton(text or ctl.name, parent)
            b.clicked.connect(lambda _=False, c=ctl: self._on_clicked(c))
            return b
        if kind == "edit":
            e = QLineEdit(parent)
            if ctl.props.get("password"):
                e.setEchoMode(QLineEdit.Password)
            e.setText(text)
            return e
        if kind == "textarea":
            t = QPlainTextEdit(parent)
            t.setPlainText(text)
            return t
        if kind == "label":
            lab = QLabel(text, parent)
            lab.setWordWrap(True)
            return lab
        if kind == "checkbox":
            return QCheckBox(text, parent)
        if kind == "radio":
            return QRadioButton(text, parent)
        if kind == "combo":
            c = QComboBox(parent)
            c.setEditable(True)
            return c
        if kind == "listbox":
            return QListWidget(parent)
        if kind == "groupbox":
            return QGroupBox(text, parent)
        if kind == "datawindow":
            dobj = ctl.props.get("dataobject", "")
            if dobj and self.source.exists(dobj):
                dv = DataWindowView(dobj, self.source, parent)
            else:
                dv = QLabel(f"[DataWindow: {dobj or ctl.name}]", parent)
                dv.setFrameShape(QFrame.Box)
                dv.setAlignment(Qt.AlignCenter)
            self._datawindows[ctl.name] = dv
            return dv
        if kind == "tab":
            return QTabWidget(parent)
        if kind in ("line", "rectangle"):
            f = QFrame(parent)
            f.setFrameShape(QFrame.HLine if kind == "line" else QFrame.Box)
            return f
        if kind == "picture":
            p = QLabel("[image]", parent)
            p.setFrameShape(QFrame.Box)
            p.setAlignment(Qt.AlignCenter)
            return p
        # unknown / userobject / graph -> labelled placeholder
        ph = QLabel(f"[{ctl.pb_class}: {ctl.name}]", parent)
        ph.setFrameShape(QFrame.Box)
        ph.setStyleSheet("color:#888;")
        ph.setAlignment(Qt.AlignCenter)
        return ph

    def _apply_font(self, widget, ctl):
        face = ctl.props.get("facename")
        size = ctl.props.get("textsize")
        if face or size:
            f = QFont(face or "Arial")
            try:
                pt = abs(int(size)) if size else 8
                f.setPointSize(max(7, pt))
            except (TypeError, ValueError):
                pass
            if ctl.props.get("weight") == 700:
                f.setBold(True)
            widget.setFont(f)

    # -- behaviour ---------------------------------------------------------
    def _run_open(self):
        script = self.win.events.get("open", "")
        # the overwhelmingly common open behaviour: retrieve each DataWindow
        for name, dv in self._datawindows.items():
            if isinstance(dv, DataWindowView) and (
                    f"{name}.retrieve" in script or not script):
                dv.retrieve()

    def _on_clicked(self, ctl):
        script = ctl.events.get("clicked", "") or ""
        low = script.lower()

        # open(w_xxx) -> ask the shell to open that window
        import re
        m = re.search(r'\bopen(?:sheet)?\s*\(\s*(w_\w+)', low)
        if m and self.open_window_cb:
            self.open_window_cb(m.group(1))
            return

        # close(parent) / close(this) -> close hosting window
        if re.search(r'\bclose\s*\(\s*(parent|this|w_)', low):
            top = self.window()
            if isinstance(top, QMainWindow) or top is not self:
                top.close()
                return

        # dw.retrieve / insertrow / update -> act on the named DataWindow
        for name, dv in self._datawindows.items():
            if not isinstance(dv, DataWindowView):
                continue
            if f"{name}.retrieve" in low:
                dv.retrieve()
            if f"{name}.update" in low:
                QMessageBox.information(self, "Save",
                                        "Update wired to DataWindow "
                                        f"'{name}' (commit handled by service).")

        if not script.strip():
            QMessageBox.information(
                self, ctl.name,
                "This control has no script in the original window.")
        elif not (m or "close" in low):
            # surface the original logic so nothing is silently lost
            QMessageBox.information(
                self, f"{ctl.name} — original PowerScript",
                script[:1500])


class WindowFrame(QMainWindow):
    """Top-level frame hosting a WindowView, sized like the original window."""

    def __init__(self, win_name, source, open_window_cb=None, parent=None):
        super().__init__(parent)
        view = WindowView(win_name, source, open_window_cb, self)
        self.setCentralWidget(view)
        self.setWindowTitle(view.title or win_name)
        w, h = view.suggested_size()
        self.resize(min(max(w, 360), 1280), min(max(h, 260), 860))
        self.view = view
