"""
Reporting framework — the PySide6 equivalent of a GMINE report window driving a
DataWindow.

A report is described by a :class:`ReportSpec`: a title, a list of parameters
(date range / text / choice), and a ``run(params)`` callable returning
``(columns, rows)``. :class:`ReportView` renders the parameter bar, runs the
query into a grid, and exports the result to CSV or PDF — the on-screen +
print/export behaviour every GMINE report window provides.

This is reused by every converted report (see :mod:`app.reports.sales_register`);
new reports only need a :class:`ReportSpec`.
"""

from __future__ import annotations

import csv
import datetime
from dataclasses import dataclass, field
from typing import Callable

from PySide6.QtWidgets import (
    QComboBox, QFileDialog, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QMessageBox, QPushButton, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget,
)


@dataclass
class ReportParam:
    name: str
    label: str
    kind: str = "text"          # "date" | "text" | "choice"
    default: str = ""
    options: list = field(default_factory=list)


@dataclass
class ReportSpec:
    title: str
    params: list
    run: Callable           # run(values: dict) -> (columns: list[str], rows: list[dict])


def export_csv(path: str, columns: list[str], rows: list[dict]):
    with open(path, "w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh)
        writer.writerow(columns)
        for row in rows:
            writer.writerow([row.get(c, "") for c in columns])


def export_pdf(path: str, title: str, columns: list[str], rows: list[dict]):
    """Render a simple tabular PDF via reportlab."""
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import A4, landscape
    from reportlab.lib.units import mm
    from reportlab.platypus import (
        SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer)
    from reportlab.lib.styles import getSampleStyleSheet

    doc = SimpleDocTemplate(path, pagesize=landscape(A4),
                            leftMargin=10 * mm, rightMargin=10 * mm,
                            topMargin=12 * mm, bottomMargin=12 * mm)
    styles = getSampleStyleSheet()
    elements = [Paragraph(title, styles["Title"]), Spacer(1, 6)]
    data = [columns] + [[str(r.get(c, "")) for c in columns] for r in rows]
    table = Table(data, repeatRows=1)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1f3a5f")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTSIZE", (0, 0), (-1, -1), 7),
        ("GRID", (0, 0), (-1, -1), 0.25, colors.grey),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#eef2f7")]),
    ]))
    elements.append(table)
    doc.build(elements)


class ReportView(QWidget):
    def __init__(self, spec: ReportSpec, parent=None):
        super().__init__(parent)
        self.spec = spec
        self._inputs: dict[str, QWidget] = {}
        self._columns: list[str] = []
        self._rows: list[dict] = []
        self._build()

    def _build(self):
        root = QVBoxLayout(self)
        title = QLabel(self.spec.title)
        title.setStyleSheet("font-size:16px;font-weight:700;padding:4px;")
        root.addWidget(title)

        bar = QGroupBox("Parameters")
        lay = QHBoxLayout(bar)
        today = str(datetime.date.today())
        for p in self.spec.params:
            lay.addWidget(QLabel(p.label))
            if p.kind == "choice":
                w = QComboBox(); w.addItems(p.options or [])
                if p.default:
                    w.setCurrentText(p.default)
            else:
                default = p.default or (today if p.kind == "date" else "")
                w = QLineEdit(default)
                if p.kind == "date":
                    w.setPlaceholderText("YYYY-MM-DD")
                    w.setMaximumWidth(120)
            self._inputs[p.name] = w
            lay.addWidget(w)
        run = QPushButton("Run"); run.clicked.connect(self.run)
        lay.addWidget(run); lay.addStretch(1)
        root.addWidget(bar)

        self.grid = QTableWidget(0, 0)
        self.grid.setEditTriggers(QTableWidget.NoEditTriggers)
        self.grid.setSelectionBehavior(QTableWidget.SelectRows)
        root.addWidget(self.grid, 1)

        actions = QHBoxLayout()
        self.lbl_count = QLabel("0 rows")
        csv_btn = QPushButton("Export CSV"); csv_btn.clicked.connect(self._export_csv)
        pdf_btn = QPushButton("Export PDF"); pdf_btn.clicked.connect(self._export_pdf)
        actions.addWidget(self.lbl_count); actions.addStretch(1)
        actions.addWidget(csv_btn); actions.addWidget(pdf_btn)
        root.addLayout(actions)

    def values(self) -> dict:
        out = {}
        for name, w in self._inputs.items():
            out[name] = w.currentText() if isinstance(w, QComboBox) else w.text().strip()
        return out

    def run(self):
        try:
            self._columns, self._rows = self.spec.run(self.values())
        except Exception as exc:
            QMessageBox.critical(self, self.spec.title, f"Report failed: {exc}")
            return
        self._fill_grid()

    def _fill_grid(self):
        self.grid.setColumnCount(len(self._columns))
        self.grid.setHorizontalHeaderLabels(self._columns)
        self.grid.setRowCount(len(self._rows))
        for r, row in enumerate(self._rows):
            for c, col in enumerate(self._columns):
                val = row.get(col)
                self.grid.setItem(r, c, QTableWidgetItem("" if val is None else str(val)))
        self.grid.resizeColumnsToContents()
        self.lbl_count.setText(f"{len(self._rows)} rows")

    def _export_csv(self):
        if not self._rows:
            QMessageBox.information(self, self.spec.title, "Run the report first.")
            return
        path, _ = QFileDialog.getSaveFileName(self, "Export CSV", "report.csv",
                                              "CSV (*.csv)")
        if path:
            export_csv(path, self._columns, self._rows)
            QMessageBox.information(self, self.spec.title, f"Saved {path}")

    def _export_pdf(self):
        if not self._rows:
            QMessageBox.information(self, self.spec.title, "Run the report first.")
            return
        path, _ = QFileDialog.getSaveFileName(self, "Export PDF", "report.pdf",
                                              "PDF (*.pdf)")
        if not path:
            return
        try:
            export_pdf(path, self.spec.title, self._columns, self._rows)
        except Exception as exc:
            QMessageBox.critical(self, self.spec.title, f"PDF export failed: {exc}")
            return
        QMessageBox.information(self, self.spec.title, f"Saved {path}")
