"""
Tax-invoice / estimate PDF for a sale — the print side of GMINE ``w_sales``.

Renders a GST tax invoice (or estimate) via reportlab: shop header, bill/customer
details, the item lines with weight/rate/amount, the CGST/SGST/IGST split,
round-off, grand total and the amount in words (Indian numbering). Used by the
Sales billing form's Print action.
"""

from __future__ import annotations

from decimal import Decimal

from app.services.sales_service import D, rnd

_ONES = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight",
         "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen",
         "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
_TENS = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy",
         "Eighty", "Ninety"]


def _two(n: int) -> str:
    if n < 20:
        return _ONES[n]
    return (_TENS[n // 10] + (" " + _ONES[n % 10] if n % 10 else "")).strip()


def _three(n: int) -> str:
    h, rest = divmod(n, 100)
    out = ""
    if h:
        out += _ONES[h] + " Hundred"
        if rest:
            out += " "
    if rest:
        out += _two(rest)
    return out


def amount_in_words(amount) -> str:
    """Indian-numbering words for a rupee amount, e.g. 1,23,456.50."""
    amt = rnd(amount, 2)
    rupees = int(amt)
    paise = int((amt - rupees) * 100)

    if rupees == 0:
        words = "Zero"
    else:
        crore, rem = divmod(rupees, 10_000_000)
        lakh, rem = divmod(rem, 100_000)
        thousand, rem = divmod(rem, 1000)
        parts = []
        if crore:
            parts.append(_three(crore) + " Crore")
        if lakh:
            parts.append(_two(lakh) + " Lakh")
        if thousand:
            parts.append(_two(thousand) + " Thousand")
        if rem:
            parts.append(_three(rem))
        words = " ".join(parts)

    text = f"Rupees {words}"
    if paise:
        text += f" and {_two(paise)} Paise"
    return text + " Only"


def build_invoice_pdf(path: str, header: dict, lines, totals,
                      shop_name: str = "Jewellery ERP Enterprise"):
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import mm
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.platypus import (
        SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer)

    styles = getSampleStyleSheet()
    doc = SimpleDocTemplate(path, pagesize=A4, leftMargin=14 * mm,
                            rightMargin=14 * mm, topMargin=14 * mm,
                            bottomMargin=14 * mm)
    is_estimate = (header.get("salestype") or "S").upper() == "E"
    doc_title = "ESTIMATE" if is_estimate else "TAX INVOICE"

    elements = [
        Paragraph(shop_name, styles["Title"]),
        Paragraph(doc_title, styles["Heading2"]),
        Spacer(1, 4),
        Paragraph(f"Bill No: <b>{header.get('billno','')}</b> &nbsp;&nbsp; "
                  f"Date: {header.get('tdate','')}", styles["Normal"]),
        Paragraph(f"Customer: {header.get('custname','')}", styles["Normal"]),
        Spacer(1, 8),
    ]

    head = ["#", "Item", "Qty", "Net Wt", "Rate", "Making", "Stone", "Amount"]
    data = [head]
    for i, ln in enumerate(lines, start=1):
        ln.compute()
        data.append([str(i), ln.name or ln.code, f"{ln.qty}",
                     f"{ln.net_wgt}", f"{ln.rate}", f"{ln.making}",
                     f"{ln.stone_price}", f"{ln.amount:.2f}"])
    table = Table(data, repeatRows=1,
                  colWidths=[10*mm, 45*mm, 14*mm, 20*mm, 22*mm, 20*mm, 20*mm, 25*mm])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1f3a5f")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTSIZE", (0, 0), (-1, -1), 8),
        ("ALIGN", (2, 0), (-1, -1), "RIGHT"),
        ("GRID", (0, 0), (-1, -1), 0.25, colors.grey),
    ]))
    elements.append(table)
    elements.append(Spacer(1, 8))

    summary = [
        ["Taxable", f"{totals.taxable:.2f}"],
        ["CGST", f"{totals.cgst:.2f}"],
        ["SGST", f"{totals.sgst:.2f}"],
        ["IGST", f"{totals.igst:.2f}"],
        ["Round Off", f"{totals.round_off:.2f}"],
        ["Grand Total", f"{totals.grand_total:.2f}"],
    ]
    stable = Table(summary, colWidths=[40*mm, 35*mm], hAlign="RIGHT")
    stable.setStyle(TableStyle([
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("ALIGN", (1, 0), (1, -1), "RIGHT"),
        ("LINEABOVE", (0, -1), (-1, -1), 0.5, colors.black),
        ("FONTNAME", (0, -1), (-1, -1), "Helvetica-Bold"),
    ]))
    elements.append(stable)
    elements.append(Spacer(1, 6))
    elements.append(Paragraph(f"<b>{amount_in_words(totals.grand_total)}</b>",
                              styles["Normal"]))
    elements.append(Spacer(1, 18))
    elements.append(Paragraph("For " + shop_name + "<br/><br/>Authorised Signatory",
                              styles["Normal"]))
    doc.build(elements)
