"""
Render any PowerBuilder window as a PySide6 screen.

This is the engine that converts every GMINE window — masters, transactions,
reports and utilities alike — without skipping any. It parses the window's
``.srw`` source (see :mod:`app.pb_parser`) and rebuilds the screen control for
control, preserving the original layout, captions and field lengths, then wires
the standard PowerBuilder data toolbar (Add / Save / Delete / Edit / Cancel /
Exit) over a live, editable grid on the window's own table: selecting a row
loads it into the fields, and New / Save / Delete perform real inserts, updates
and deletes through :mod:`app.services.crud_service`.

Modules that have a hand-written business-logic implementation (Phase 4) are
registered in :mod:`app.modules` and take over from this generic renderer.
"""

from __future__ import annotations

from PySide6.QtCore import Qt, QRect
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QCheckBox, QComboBox, QFrame, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QMessageBox, QPushButton, QRadioButton, QScrollArea, QTableWidget,
    QTableWidgetItem, QTextEdit, QVBoxLayout, QWidget,
)

from app import pb_parser
from app.reports.generic import GenericDataView
from app.services import crud_service
from app.ui import navigation
from app.ui.printing import print_table
from app.reports import layouts as dw_layouts
from app.reports.dw_print import print_document


def _pretty_window(name: str) -> str:
    """w_sales -> Sales, for a button caption."""
    return name[2:].replace("_", " ").title() if name.startswith("w_") else name
from app.pb_parser import PBU

import db

_STD_BUTTON = {
    "cb_add": "add", "cb_save": "save", "cb_delete": "delete",
    "cb_edit": "edit", "cb_cancel": "cancel", "cb_exit": "exit",
    "cb_close": "exit", "cb_new": "add", "cb_update": "save",
}


class PBWindowForm(QWidget):
    """Generic, faithful renderer for a parsed PowerBuilder window."""

    def __init__(self, window: pb_parser.Window, parent=None, seed: dict | None = None):
        super().__init__(parent)
        self.window_def = window
        self.seed = seed or {}
        self._inputs: dict[str, QWidget] = {}
        self._rows: list = []
        self._current_row: dict | None = None
        self._grid: QTableWidget | None = None
        self._search: QLineEdit | None = None
        self._status: QLabel | None = None
        self.grid_mode = False
        self._view = None
        self._build()

    # -- construction ------------------------------------------------------
    def _build(self):
        outer = QVBoxLayout(self)
        outer.setContentsMargins(0, 0, 0, 0)

        outer.addWidget(self._header())

        scroll = QScrollArea()
        scroll.setWidgetResizable(False)
        canvas = QWidget()
        canvas.setFixedSize(int(self.window_def.width * PBU) + 40,
                            int(self.window_def.height * PBU) + 40)
        self._render_controls(canvas)
        # The field list is known only after the controls exist.
        self.mapping = self._build_mapping()
        scroll.setWidget(canvas)
        outer.addWidget(scroll, 1)

        panel = self._records_panel()
        if panel is not None:
            outer.addWidget(panel)

    def _header(self) -> QWidget:
        bar = QFrame()
        bar.setStyleSheet("background:#1f3a5f;color:white;")
        lay = QHBoxLayout(bar)
        lay.setContentsMargins(12, 8, 12, 8)
        title = QLabel(self.window_def.title)
        f = QFont()
        f.setPointSize(12)
        f.setBold(True)
        title.setFont(f)
        title.setStyleSheet("color:white;")
        lay.addWidget(title)
        lay.addStretch(1)
        meta = QLabel(f"{self.window_def.name}")
        meta.setStyleSheet("color:#b9c7da;")
        lay.addWidget(meta)
        return bar

    def _render_controls(self, canvas: QWidget):
        for c in self.window_def.controls:
            widget = self._make_widget(c, canvas)
            if widget is None:
                continue
            widget.setParent(canvas)
            widget.setGeometry(QRect(
                int(c.x * PBU) + 8, int(c.y * PBU) + 8,
                max(int(c.width * PBU), 16), max(int(c.height * PBU), 16)))
            widget.show()

    def _make_widget(self, c: pb_parser.Control, canvas):
        kind = c.kind
        if kind == "statictext":
            w = QLabel(c.text)
            w.setWordWrap(True)
            return w
        if kind in ("singlelineedit", "editmask"):
            w = QLineEdit()
            if c.limit:
                w.setMaxLength(c.limit)
            self._inputs[c.name] = w
            return w
        if kind == "multilineedit":
            w = QTextEdit()
            self._inputs[c.name] = w
            return w
        if kind == "checkbox":
            w = QCheckBox(c.text)
            self._inputs[c.name] = w
            return w
        if kind == "radiobutton":
            w = QRadioButton(c.text)
            self._inputs[c.name] = w
            return w
        if kind in ("dropdownlistbox", "listbox"):
            w = QComboBox()
            w.addItems(c.items)
            self._inputs[c.name] = w
            return w
        if kind == "commandbutton":
            return self._make_button(c)
        if kind == "groupbox":
            w = QGroupBox(c.text)
            return w
        if kind == "datawindow":
            w = QTableWidget(0, 0)
            w.setToolTip(f"DataWindow: {c.dataobject}")
            return w
        if kind in pb_parser.DECORATION_KINDS:
            w = QFrame()
            w.setFrameShape(QFrame.Box if kind != "line" else QFrame.HLine)
            w.setStyleSheet("color:#c0c6cc;")
            return w
        # Unknown control: show a small placeholder so nothing silently vanishes.
        lbl = QLabel(c.text or kind)
        lbl.setStyleSheet("color:#888;border:1px dashed #ccc;")
        return lbl

    def _make_button(self, c: pb_parser.Control) -> QPushButton:
        btn = QPushButton(c.text or c.name)
        action = _STD_BUTTON.get(c.name.lower())
        if action == "exit":
            btn.clicked.connect(self._close_tab)
        elif action == "save":
            btn.clicked.connect(lambda: self._save_grid() if self.grid_mode
                                else self._save())
        elif action == "delete":
            btn.clicked.connect(lambda: self._delete_grid_row() if self.grid_mode
                                else self._delete())
        elif action == "add":
            btn.clicked.connect(lambda: self._add_row() if self.grid_mode
                                else self._new())
        elif action == "edit":
            btn.clicked.connect(self._grid_selected)
        elif action == "cancel":
            btn.clicked.connect(self._clear)
        else:
            btn.clicked.connect(lambda: self._info(c.text or c.name))
        return btn

    # -- record editing ----------------------------------------------------
    def _primary_table(self) -> str | None:
        return self.window_def.tables[0] if self.window_def.tables else None

    def _build_mapping(self):
        """Work out what this screen edits, and how.

        Two ways, in order of authority:

        1. the window's own DataWindow (``.srd``) — it names the table it
           updates and its key columns, exactly as the original application
           did, and the screen becomes an editable grid of those columns;
        2. otherwise the screen's input fields are matched onto the columns of
           the table its SQL uses.
        """
        try:
            if self.window_def.grid:
                mapping = crud_service.build_grid_mapping(self.window_def.grid)
                if mapping.writable:
                    self.grid_mode = True
                    return mapping
            table = self._primary_table()
            if not table:
                return None
            return crud_service.build_mapping(table, list(self._inputs),
                                              window=self.window_def.name)
        except Exception:
            return None

    # -- widget values -----------------------------------------------------
    def _widget_value(self, w: QWidget):
        if isinstance(w, QLineEdit):
            return w.text()
        if isinstance(w, QTextEdit):
            return w.toPlainText()
        if isinstance(w, (QCheckBox, QRadioButton)):
            return w.isChecked()
        if isinstance(w, QComboBox):
            return w.currentText()
        return None

    def _set_widget_value(self, w: QWidget, value):
        text = "" if value is None else str(value)
        if isinstance(w, QLineEdit):
            w.setText(text)
        elif isinstance(w, QTextEdit):
            w.setPlainText(text)
        elif isinstance(w, (QCheckBox, QRadioButton)):
            w.setChecked(str(value).strip().lower() in ("1", "y", "yes", "true"))
        elif isinstance(w, QComboBox):
            idx = w.findText(text)
            w.setCurrentIndex(idx if idx >= 0 else -1)

    def _collect(self) -> dict:
        return {name: self._widget_value(w) for name, w in self._inputs.items()}

    # -- data area ---------------------------------------------------------
    def _records_panel(self) -> QWidget | None:
        """The screen's data area, in order of what the window actually is.

        An editable DataWindow grid, then a record list for a screen whose
        fields map onto a table, then the window's own DataWindow query as a
        data view (this is what report and list windows are), and nothing at
        all for a window with no data behind it.
        """
        if self.grid_mode or (self.mapping is not None and self.mapping.writable):
            return self._data_grid()
        if self.window_def.report:
            view = GenericDataView(self.window_def.report, self.window_def.title,
                                   seed=self.seed)
            box = QGroupBox(f"Data — {self.window_def.report.get('dataobject', '')}")
            lay = QVBoxLayout(box)
            lay.addWidget(view)
            self._view = view
            return box
        return self._data_grid()

    def _data_grid(self) -> QWidget | None:
        table = (self.mapping.table if self.mapping else None) or self._primary_table()
        if not table:
            return None
        box = QGroupBox(f"Records — {table}"
                        + ("  (edit cells directly)" if self.grid_mode else ""))
        lay = QVBoxLayout(box)

        tools = QHBoxLayout()
        self._search = QLineEdit()
        self._search.setPlaceholderText("Search…")
        self._search.setMaximumWidth(220)
        self._search.returnPressed.connect(self._refresh)
        tools.addWidget(self._search)
        actions = (("Search", self._refresh), ("Add Row", self._add_row),
                   ("Save", self._save_grid), ("Delete Row", self._delete_grid_row),
                   ("Refresh", self._refresh)) if self.grid_mode else \
                  (("Search", self._refresh), ("New", self._new),
                   ("Save", self._save), ("Delete", self._delete),
                   ("Refresh", self._refresh))
        for caption, slot in actions:
            btn = QPushButton(caption)
            btn.clicked.connect(slot)
            tools.addWidget(btn)
        print_btn = QPushButton("Print")
        print_btn.clicked.connect(self._print_records)
        tools.addWidget(print_btn)
        if self._printed_forms():
            form_btn = QPushButton("Print Form")
            form_btn.setToolTip("Print on the original designed form")
            form_btn.clicked.connect(self._print_form)
            tools.addWidget(form_btn)
        for target in self._flow_targets()[:2]:
            btn = QPushButton(f"Open {_pretty_window(target)}")
            btn.clicked.connect(lambda _=False, w=target: self._open_next(w))
            tools.addWidget(btn)
        tools.addStretch(1)
        self._status = QLabel()
        self._status.setStyleSheet("color:#4a5a6a;")
        tools.addWidget(self._status)
        lay.addLayout(tools)

        self._grid = QTableWidget(0, 0)
        if self.grid_mode:
            # The original screen edits its rows in place; so does this one.
            self._grid.setEditTriggers(QTableWidget.DoubleClicked
                                       | QTableWidget.EditKeyPressed
                                       | QTableWidget.AnyKeyPressed)
        else:
            self._grid.setEditTriggers(QTableWidget.NoEditTriggers)
            self._grid.itemSelectionChanged.connect(self._grid_selected)
            if self._flow_targets():
                self._grid.itemDoubleClicked.connect(lambda *_: self._open_next())
        self._grid.setSelectionBehavior(QTableWidget.SelectRows)
        self._grid.setSelectionMode(QTableWidget.SingleSelection)
        lay.addWidget(self._grid)

        box.setMaximumHeight(420 if self.grid_mode else 280)
        self._update_status()
        self._refresh()
        return box

    def _flash(self, text: str):
        """Show a short result message in the record bar (no modal popup)."""
        if self._status is not None:
            self._status.setText(text)

    def _grid_columns(self) -> list:
        """Columns shown in the editable grid (grid mode only)."""
        if not self.grid_mode or self.mapping is None:
            return []
        names = list(self.mapping.fields.values())
        return names or self.mapping.column_names

    def _grid_headers(self) -> list:
        labels = {c["name"].lower(): c.get("label") or c["name"]
                  for c in (self.window_def.grid or {}).get("columns", [])}
        return [labels.get(c.lower(), c) for c in self._grid_columns()]

    def _fill_editable_grid(self, rows: list):
        cols = self._grid_columns()
        self._grid.blockSignals(True)
        self._grid.clear()
        self._grid.setColumnCount(len(cols))
        self._grid.setHorizontalHeaderLabels(self._grid_headers())
        self._grid.setRowCount(len(rows))
        for r, row in enumerate(rows):
            for c, col in enumerate(cols):
                value = row.get(col)
                self._grid.setItem(r, c, QTableWidgetItem(
                    "" if value is None else str(value)))
        self._grid.blockSignals(False)
        self._grid.resizeColumnsToContents()

    def _row_values(self, r: int) -> dict:
        cols = self._grid_columns()
        out = {}
        for c, col in enumerate(cols):
            item = self._grid.item(r, c)
            out[col] = item.text() if item is not None else ""
        return out

    def _add_row(self):
        self._grid.insertRow(self._grid.rowCount())
        self._rows.append(None)                     # marks an unsaved row
        self._grid.setCurrentCell(self._grid.rowCount() - 1, 0)
        self._flash("New row added — fill it in and press Save.")

    def _save_grid(self):
        inserted = updated = 0
        try:
            for r in range(self._grid.rowCount()):
                raw = self._row_values(r)
                original = self._rows[r] if r < len(self._rows) else None
                values = {c: crud_service.coerce(v, self.mapping.column(c))
                          for c, v in raw.items()}
                if original is None:
                    if not any(v not in (None, "") for v in values.values()):
                        continue
                    crud_service.insert(self.mapping, values)
                    inserted += 1
                    continue
                changed = {c: v for c, v in values.items()
                           if str(original.get(c) if original.get(c) is not None else "")
                           != str(v if v is not None else "")}
                if not changed:
                    continue
                key = crud_service.key_for_row(self.mapping, original)
                matches = crud_service.count_matching(self.mapping, key)
                if matches == 0:
                    self._info("A record you edited is no longer in the database. "
                               "Press Refresh and try again.")
                    return
                if matches > 1 and not self._confirm(
                        f"{matches} records match one of the rows you edited. "
                        f"Update all {matches}?"):
                    return
                crud_service.update(self.mapping, changed, key)
                updated += 1
        except Exception as exc:
            QMessageBox.warning(self, "Save failed", str(exc))
            return
        self._refresh()
        self._flash(f"Saved — {inserted} added, {updated} updated."
                    if inserted or updated else "Nothing changed.")

    def _delete_grid_row(self):
        r = self._grid.currentRow()
        if r < 0:
            self._info("Select the row to delete first.")
            return
        original = self._rows[r] if r < len(self._rows) else None
        if original is None:                        # never saved: just drop it
            self._grid.removeRow(r)
            if r < len(self._rows):
                self._rows.pop(r)
            return
        try:
            key = crud_service.key_for_row(self.mapping, original)
            matches = crud_service.count_matching(self.mapping, key)
            question = ("Delete this record permanently?" if matches == 1 else
                        f"{matches} records match this row. Delete all {matches}?")
            if matches == 0 or not self._confirm(question):
                self._refresh()
                return
            crud_service.delete(self.mapping, key)
        except Exception as exc:
            QMessageBox.warning(self, "Delete failed", str(exc))
            return
        self._refresh()
        self._flash("Deleted.")

    # -- flow to the next screen ------------------------------------------
    def _flow_targets(self) -> list:
        """Screens this window leads to (its own scripts name them).

        Only screens this build actually has, and the entry screens before the
        record-picker helpers — this window already lists the records itself.
        """
        from app import forms

        known = [w for w in (self.window_def.opens or [])
                 if w and forms.get_form(w) is not None]
        entry = [w for w in known if "help" not in w]
        return entry + [w for w in known if w not in entry]

    def _selected_record(self) -> dict:
        """The row the user is on, whichever data area this screen uses."""
        if self._current_row:
            return dict(self._current_row)
        if self._view is not None and self._view.selected_row():
            return dict(self._view.selected_row())
        if self._grid is not None and self._rows:
            idx = self._grid.currentRow()
            if 0 <= idx < len(self._rows) and self._rows[idx]:
                return dict(self._rows[idx])
        return {}

    def _open_next(self, window: str = ""):
        targets = self._flow_targets()
        if not targets:
            return
        target = window or targets[0]
        record = self._selected_record()
        if not navigation.open_window(target, record, self.window_def.title):
            self._info(f"This option opens {target}.")

    def _update_status(self):
        if self._status is None:
            return
        if self.mapping is None:
            self._status.setText("No table for this screen — nothing to edit.")
        else:
            self._status.setText(self.mapping.describe())

    def _editable(self) -> bool:
        return self.mapping is not None and self.mapping.writable

    # -- toolbar actions ---------------------------------------------------
    def _refresh(self):
        if self._grid is None:
            return
        self._rows = []
        self._current_row = None
        if self.mapping is None or not self.mapping.columns:
            self._grid_message(f"Table '{self._primary_table()}' is not available "
                               f"in the current database.")
            return
        try:
            self._rows = crud_service.select_rows(
                self.mapping, search=self._search.text() if self._search else "")
        except Exception as exc:
            self._grid_message(f"Could not read {self.mapping.table}: {exc}")
            return
        if self.grid_mode:
            self._fill_editable_grid(self._rows)
        else:
            self._fill_grid(self._rows)

    def _grid_message(self, text: str):
        self._grid.setRowCount(1)
        self._grid.setColumnCount(1)
        self._grid.setHorizontalHeaderLabels(["info"])
        self._grid.setItem(0, 0, QTableWidgetItem(text))
        self._grid.resizeColumnsToContents()

    def _fill_grid(self, rows: list):
        cols = self.mapping.column_names if self.mapping else []
        if rows:
            cols = list(rows[0].keys())
        self._grid.clear()
        self._grid.setColumnCount(len(cols))
        self._grid.setHorizontalHeaderLabels(cols)
        self._grid.setRowCount(len(rows))
        for r, row in enumerate(rows):
            for c, col in enumerate(cols):
                value = row.get(col)
                self._grid.setItem(r, c, QTableWidgetItem(
                    "" if value is None else str(value)))
        self._grid.resizeColumnsToContents()

    def _grid_selected(self):
        if not self._rows or self._grid is None:
            return
        if not self._grid.selectedItems():      # cleared selection: keep the form
            return
        idx = self._grid.currentRow()
        if idx < 0 or idx >= len(self._rows):
            return
        self._current_row = self._rows[idx]
        if self.mapping is None:
            return
        for ctrl, column in self.mapping.fields.items():
            if column in self._current_row:
                self._set_widget_value(self._inputs[ctrl], self._current_row[column])

    def _new(self):
        self._current_row = None
        self._clear()

    def _save(self):
        if not self._editable():
            self._info(self.mapping.describe() if self.mapping else
                       "This screen has no table to save to.")
            return
        try:
            editing = self._current_row is not None
            values = crud_service.prepare_values(
                self.mapping, self._collect(), for_insert=not editing)
            if editing:
                key = crud_service.key_for_row(self.mapping, self._current_row)
                matches = crud_service.count_matching(self.mapping, key)
                if matches == 0:
                    self._info("That record is no longer in the database "
                               "(someone else may have changed it). "
                               "Press Refresh and try again.")
                    return
                if matches > 1 and not self._confirm(
                        f"{matches} records match this row (the table has no "
                        f"primary key). Update all {matches}?"):
                    return
                crud_service.update(self.mapping, values, key)
            else:
                crud_service.insert(self.mapping, values)
        except Exception as exc:
            QMessageBox.warning(self, "Save failed", str(exc))
            return
        self._refresh()
        self._flash("Saved." if editing is False else "Changes saved.")

    def _delete(self):
        if not self._editable():
            self._info(self.mapping.describe() if self.mapping else
                       "This screen has no table to delete from.")
            return
        if self._current_row is None:
            self._info("Select the record to delete in the list below first.")
            return
        try:
            key = crud_service.key_for_row(self.mapping, self._current_row)
            matches = crud_service.count_matching(self.mapping, key)
            if matches == 0:
                self._info("That record is no longer in the database.")
                self._refresh()
                return
            question = ("Delete this record permanently?" if matches == 1 else
                        f"{matches} records match this row (the table has no "
                        f"primary key). Delete all {matches}?")
            if not self._confirm(question):
                return
            crud_service.delete(self.mapping, key)
        except Exception as exc:
            QMessageBox.warning(self, "Delete failed", str(exc))
            return
        self._current_row = None
        self._clear()
        self._refresh()
        self._flash("Deleted.")

    def _clear(self):
        for w in self._inputs.values():
            if isinstance(w, QLineEdit):
                w.clear()
            elif isinstance(w, QTextEdit):
                w.clear()
            elif isinstance(w, QCheckBox):
                w.setChecked(False)
            elif isinstance(w, QComboBox):
                w.setCurrentIndex(-1)
        if self._grid is not None:
            self._grid.clearSelection()
        self._current_row = None

    def _close_tab(self):
        parent = self.parent()
        from PySide6.QtWidgets import QTabWidget
        while parent is not None and not isinstance(parent, QTabWidget):
            parent = parent.parent()
        if isinstance(parent, QTabWidget):
            parent.removeTab(parent.indexOf(self))

    def _print_records(self):
        rows = self._rows if self._rows else []
        if self.grid_mode or not rows:
            rows = [self._row_values(r) for r in range(self._grid.rowCount())] \
                if (self._grid is not None and self.grid_mode) else rows
        if not rows:
            self._info("Nothing to print — load some records first.")
            return
        columns = list(rows[0].keys())
        print_table(self, self.window_def.title, columns, rows)

    def _printed_forms(self) -> list:
        """The document forms this window can print on."""
        return dw_layouts.for_window(self.window_def)

    def _print_form(self):
        """Print the selected record on the original designed form."""
        forms = self._printed_forms()
        if not forms:
            return
        name = forms[0]
        if len(forms) > 1:
            from PySide6.QtWidgets import QInputDialog
            name, ok = QInputDialog.getItem(self, "Print Form", "Form",
                                            forms, 0, False)
            if not ok:
                return
        layout = dw_layouts.load(name)
        if layout is None:
            self._info(f"The form {name} is not in this build.")
            return
        record = self._selected_record()
        rows = [record] if record else (self._rows or [])
        print_document(self, layout, rows, record or None)

    def _confirm(self, question: str) -> bool:
        return QMessageBox.question(
            self, self.window_def.title, question,
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No) == QMessageBox.Yes

    def _info(self, msg: str):
        QMessageBox.information(self, self.window_def.title, msg)
