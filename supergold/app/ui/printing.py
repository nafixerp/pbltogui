"""
Printing.

Every screen and every report can be printed: the rows on show are rendered as
a simple table document and sent through the standard print dialog, so a screen
prints on whatever printer Windows has — the behaviour the original's
``PrintSetup``/``Print`` menu provided.
"""

from __future__ import annotations

import datetime
import html

from PySide6.QtGui import QTextDocument
from PySide6.QtPrintSupport import QPrintDialog, QPrinter


def render_html(title: str, columns: list, rows: list) -> str:
    head = "".join(f"<th>{html.escape(str(c))}</th>" for c in columns)
    body = []
    for row in rows:
        cells = "".join(
            f"<td>{html.escape('' if row.get(c) is None else str(row.get(c)))}</td>"
            for c in columns)
        body.append(f"<tr>{cells}</tr>")
    stamp = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
    return f"""
    <html><body>
      <h3 style="margin:0">{html.escape(title)}</h3>
      <div style="color:#555;font-size:9pt">{stamp} — {len(rows)} rows</div>
      <table border="1" cellspacing="0" cellpadding="3"
             style="border-collapse:collapse;font-size:8pt;margin-top:8px">
        <tr style="background:#e8eef5">{head}</tr>
        {''.join(body)}
      </table>
    </body></html>
    """


def print_table(parent, title: str, columns: list, rows: list) -> bool:
    """Show the print dialog and print ``rows``. False if the user cancelled."""
    printer = QPrinter(QPrinter.HighResolution)
    printer.setPageOrientation(printer.pageLayout().Orientation.Landscape
                               if len(columns) > 6 else
                               printer.pageLayout().Orientation.Portrait)
    dialog = QPrintDialog(printer, parent)
    if dialog.exec() != QPrintDialog.Accepted:
        return False
    doc = QTextDocument()
    doc.setHtml(render_html(title, columns, rows))
    doc.print_(printer)
    return True
