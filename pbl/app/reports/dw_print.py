"""
Print a document on its original designed form.

Every bill, memo and voucher of the original application has a print
DataWindow — ``d_salesprint``, ``d_gsmithprint`` and so on — whose ``.srd``
holds the whole layout: the bands, every label at its position, every column,
the totals and the lines that box them in. :func:`app.pb_parser.parse_layout`
reads that, and this module draws it: header band once per page, the detail
band once per row, the footer and summary at the end, on the paper size and
orientation the DataWindow was designed for.

The result is a PDF, so it prints identically from any machine.
"""

from __future__ import annotations

import datetime
import os
import re
import tempfile

from app.pb_parser import DWLayout
from app.reports import dw_expr

# Paper sizes the DataWindows use (PowerBuilder codes), in points.
PAPER = {1: (612.0, 792.0),      # Letter
         5: (612.0, 1008.0),     # Legal
         8: (842.0, 1191.0),     # A3
         9: (595.0, 842.0),      # A4
         11: (420.0, 595.0),     # A5
         }
# 64 PowerBuilder units of box height carry 10pt text in these forms.
PBU_PER_POINT = 6.4

_SUM_RE = re.compile(r"(sum|count|avg|max|min)\s*\(\s*([\w.]+)", re.I)
_DEC_RE = re.compile(r"\.(0+)")


def page_size(layout: DWLayout) -> tuple:
    width, height = PAPER.get(layout.paper, PAPER[9])
    return (height, width) if layout.orientation == 1 else (width, height)


def format_value(value, mask: str) -> str:
    """Apply a DataWindow format mask (``#####0.000``, ``dd/mm/yyyy``, …)."""
    if value is None:
        return ""
    mask = (mask or "").strip()
    if not mask or mask.upper() in ("[GENERAL]", "[GENERAL] "):
        return str(value)
    if any(part in mask.lower() for part in ("dd", "mm", "yyyy", "yy")):
        text = str(value)[:10]
        try:
            date = datetime.date.fromisoformat(text)
        except ValueError:
            return str(value)
        out = mask.lower().replace("yyyy", f"{date.year:04d}")
        out = out.replace("mm", f"{date.month:02d}").replace("dd", f"{date.day:02d}")
        return out.replace("yy", f"{date.year % 100:02d}")
    if "0" in mask or "#" in mask:
        decimals = 0
        m = _DEC_RE.search(mask)
        if m:
            decimals = len(m.group(1))
        try:
            number = float(value)
        except (TypeError, ValueError):
            return str(value)
        text = f"{number:,.{decimals}f}" if "," in mask else f"{number:{'.%df' % decimals}}"
        return text
    return str(value)


def value_for(obj, row: dict, rows: list, context: dict | None = None):
    """What a column or computed field shows for this row.

    Computed fields are the original's own calculations, evaluated by
    :mod:`app.reports.dw_expr` — totals, weight less stone, value addition,
    the GST captions, and so on.
    """
    if obj.kind == "column":
        key = obj.name
        if key in row:
            return row[key]
        short = key.split("_", 1)[-1]
        return row.get(short)
    expression = (obj.expression or "").strip()
    if not expression:
        return ""
    value = dw_expr.evaluate(expression, row, rows, context)
    return "" if value is None else value


def render_pdf(layout: DWLayout, rows: list, path: str, header: dict | None = None,
               settings: dict | None = None):
    """Draw ``rows`` on ``layout`` and write the PDF to ``path``."""
    from reportlab.pdfgen import canvas as pdfcanvas

    width, height = page_size(layout)
    margin_left = layout.margins.get("left", 110)
    margin_right = layout.margins.get("right", 110)
    scale = (width - 72.0) / max(layout.width + margin_left + margin_right, 1)

    def px(value):        # PowerBuilder units -> points
        return value * scale

    def font(obj):
        return ("Helvetica-Bold" if obj.bold else "Helvetica",
                max(obj.size * scale * PBU_PER_POINT, 4.0))

    pdf = pdfcanvas.Canvas(path, pagesize=(width, height))
    top = height - 36.0
    header_row = dict(header or (rows[0] if rows else {}))

    context = {"page": 1, "pagecount": 1, "settings": settings or {}}

    def draw_band(band: str, origin_y: float, row: dict) -> float:
        band_height = px(layout.bands.get(band, 0))
        for obj in layout.band(band):
            if obj.kind == "line":
                pdf.setLineWidth(0.6)
                pdf.line(px(obj.x1), origin_y - px(obj.y1),
                         px(obj.x2), origin_y - px(obj.y2))
                continue
            if obj.kind == "rectangle":
                pdf.setLineWidth(0.6)
                pdf.rect(px(obj.x), origin_y - px(obj.y + obj.height),
                         px(obj.width), px(obj.height), stroke=1, fill=0)
                continue
            if obj.kind == "text":
                text = obj.text
            else:
                text = format_value(value_for(obj, row, rows, context),
                                    obj.format)
            if text in (None, ""):
                continue
            name, size = font(obj)
            # PowerBuilder clips a field to its box; shrink instead, so nothing
            # is lost and neighbouring columns are not overprinted.
            box = px(obj.width)
            if box > 1 and pdf.stringWidth(str(text), name, size) > box:
                size = max(size * box / pdf.stringWidth(str(text), name, size), 3.5)
            pdf.setFont(name, size)
            baseline = origin_y - px(obj.y + obj.height) + size * 0.25
            if obj.alignment == 1:            # right
                pdf.drawRightString(px(obj.x + obj.width), baseline, str(text))
            elif obj.alignment == 2:          # centre
                pdf.drawCentredString(px(obj.x + obj.width / 2), baseline, str(text))
            else:
                pdf.drawString(px(obj.x), baseline, str(text))
        return band_height

    detail_height = px(layout.bands.get("detail", 0)) or 12.0
    footer_height = px(layout.bands.get("footer", 0))
    summary_height = px(layout.bands.get("summary", 0))

    y = top
    y -= draw_band("header", y, header_row)
    for index, row in enumerate(rows or [{}]):
        context["row_index"] = index
        if y - detail_height < 36.0 + footer_height:
            pdf.showPage()
            context["page"] += 1
            y = top
            y -= draw_band("header", y, header_row)
        y -= draw_band("detail", y, row)
    if summary_height:
        y -= draw_band("summary", y, header_row)
    if footer_height:
        draw_band("footer", 36.0 + footer_height, header_row)
    pdf.save()
    return path


def print_document(parent, layout: DWLayout, rows: list, header: dict | None = None,
                   filename: str = "") -> str:
    """Render the form and hand the PDF to the user (save / open)."""
    from PySide6.QtWidgets import QFileDialog, QMessageBox

    default = filename or os.path.join(tempfile.gettempdir(),
                                       f"{layout.name}.pdf")
    path, _ = QFileDialog.getSaveFileName(parent, "Print to PDF", default,
                                          "PDF (*.pdf)")
    if not path:
        return ""
    try:
        render_pdf(layout, rows, path, header)
    except Exception as exc:
        QMessageBox.warning(parent, "Print", f"Could not print: {exc}")
        return ""
    try:
        from PySide6.QtCore import QUrl
        from PySide6.QtGui import QDesktopServices
        QDesktopServices.openUrl(QUrl.fromLocalFile(path))
    except Exception:
        pass
    return path
