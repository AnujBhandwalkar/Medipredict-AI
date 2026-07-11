"""
report_pdf.py
Generates a branded PDF report (Patient Details, Disease Prediction,
Risk Score, Prediction Date) for MediPredict AI.

Used by app.py's /send_report route. Returns an in-memory PDF (BytesIO)
so it can be attached to an email without writing to disk.
"""

from io import BytesIO
from datetime import datetime

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT

# Brand colors (matches the HTML templates)
BRAND_RED = colors.HexColor("#e8392a")
INK = colors.HexColor("#0e0e0e")
INK3 = colors.HexColor("#6b6b6b")
BORDER = colors.HexColor("#e5e3dd")
BG = colors.HexColor("#f7f6f2")

DISEASE_COLORS = {
    "Diabetes": colors.HexColor("#2563eb"),
    "Heart Disease": colors.HexColor("#e8392a"),
    "Liver Disease": colors.HexColor("#d97706"),
    "Kidney Disease": colors.HexColor("#16a34a"),
    "Lung Disease": colors.HexColor("#7c3aed"),
}


def _risk_level(score):
    if score >= 70:
        return "High Risk", colors.HexColor("#991b1b"), colors.HexColor("#fef2f2")
    if score >= 40:
        return "Moderate Risk", colors.HexColor("#92400e"), colors.HexColor("#fffbeb")
    return "Low Risk", colors.HexColor("#166534"), colors.HexColor("#f0fdf4")


def generate_report_pdf(patient, results, prediction_date=None):
    """
    patient: dict with keys id, name, age, gender, email (any may be missing)
    results: dict of {disease_name: score_float} — one entry for a single
             prediction, or up to five for the multi-disease screening.
    prediction_date: ISO string or None (defaults to now)
    Returns: BytesIO positioned at 0, containing the PDF bytes.
    """
    buf = BytesIO()
    doc = SimpleDocTemplate(
        buf, pagesize=A4,
        topMargin=22 * mm, bottomMargin=18 * mm,
        leftMargin=20 * mm, rightMargin=20 * mm,
        title="MediPredict AI - Risk Report",
    )

    styles = getSampleStyleSheet()
    h1 = ParagraphStyle("h1", parent=styles["Title"], fontSize=20, leading=24,
                         textColor=INK, alignment=TA_LEFT, spaceAfter=2)
    sub = ParagraphStyle("sub", parent=styles["Normal"], fontSize=9.5,
                          textColor=INK3, alignment=TA_LEFT, spaceAfter=14)
    section = ParagraphStyle("section", parent=styles["Heading2"], fontSize=12,
                              textColor=INK, spaceBefore=18, spaceAfter=8)
    normal = ParagraphStyle("normal", parent=styles["Normal"], fontSize=10,
                             textColor=INK, leading=15)
    disclaimer_style = ParagraphStyle("disclaimer", parent=styles["Normal"],
                                       fontSize=8.5, textColor=colors.HexColor("#92400e"),
                                       leading=13)

    story = []

    # ── Header ──
    story.append(Paragraph("MediPredict AI", h1))
    story.append(Paragraph("Automated Disease Risk Prediction Report", sub))
    story.append(HRFlowable(width="100%", thickness=1, color=BORDER, spaceAfter=14))

    # ── Patient details ──
    story.append(Paragraph("Patient Details", section))
    patient_rows = [
        ["Patient ID", patient.get("id") or "PT-WALK-IN"],
        ["Name", patient.get("name") or "Walk-in Patient"],
        ["Age", str(patient.get("age") or "—")],
        ["Gender", patient.get("gender") or "—"],
        ["Email", patient.get("email") or "—"],
    ]
    patient_table = Table(patient_rows, colWidths=[45 * mm, 110 * mm])
    patient_table.setStyle(TableStyle([
        ("FONTSIZE", (0, 0), (-1, -1), 10),
        ("TEXTCOLOR", (0, 0), (0, -1), INK3),
        ("TEXTCOLOR", (1, 0), (1, -1), INK),
        ("FONTNAME", (0, 0), (0, -1), "Helvetica"),
        ("FONTNAME", (1, 0), (1, -1), "Helvetica-Bold"),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("LINEBELOW", (0, 0), (-1, -2), 0.5, BORDER),
    ]))
    story.append(patient_table)

    # ── Prediction date ──
    if prediction_date:
        try:
            dt = datetime.fromisoformat(prediction_date.replace("Z", "+00:00"))
        except ValueError:
            dt = datetime.now()
    else:
        dt = datetime.now()
    date_str = dt.strftime("%d %B %Y, %I:%M %p")

    story.append(Spacer(1, 4))
    story.append(Paragraph(f"<b>Prediction Date:</b> {date_str}", normal))

    # ── Disease prediction / risk score results ──
    story.append(Paragraph("Disease Prediction &amp; Risk Score", section))

    result_rows = [["Disease", "Risk Score", "Risk Level"]]
    row_styles = []
    for i, (disease, score) in enumerate(results.items(), start=1):
        level, text_color, _ = _risk_level(score)
        result_rows.append([disease, f"{score}%", level])
        row_styles.append(("TEXTCOLOR", (1, i), (2, i), text_color))

    results_table = Table(result_rows, colWidths=[65 * mm, 40 * mm, 50 * mm])
    base_style = [
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 10),
        ("BACKGROUND", (0, 0), (-1, 0), BG),
        ("TEXTCOLOR", (0, 0), (-1, 0), INK),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("GRID", (0, 0), (-1, -1), 0.5, BORDER),
        ("FONTNAME", (1, 1), (2, -1), "Helvetica-Bold"),
    ]
    results_table.setStyle(TableStyle(base_style + row_styles))
    story.append(results_table)

    # ── Highest risk callout (only meaningful for multi-disease report) ──
    if len(results) > 1:
        highest = max(results, key=results.get)
        level, text_color, bg_color = _risk_level(results[highest])
        story.append(Spacer(1, 12))
        callout = Table(
            [[f"Highest Risk: {highest} — {results[highest]}%  ({level})"]],
            colWidths=[155 * mm],
        )
        callout.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), bg_color),
            ("TEXTCOLOR", (0, 0), (-1, -1), text_color),
            ("FONTNAME", (0, 0), (-1, -1), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, -1), 10),
            ("TOPPADDING", (0, 0), (-1, -1), 10),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
            ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ]))
        story.append(callout)

    # ── Disclaimer ──
    story.append(Spacer(1, 22))
    disclaimer_table = Table(
        [[Paragraph(
            "<b>Disclaimer:</b> This result is generated by a machine learning "
            "model trained on clinical datasets and is intended for informational "
            "and screening purposes only. It does not constitute a medical "
            "diagnosis. Please consult a qualified healthcare professional before "
            "making any health-related decisions.",
            disclaimer_style
        )]],
        colWidths=[155 * mm],
    )
    disclaimer_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#fffbeb")),
        ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#fde68a")),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
    ]))
    story.append(disclaimer_table)

    story.append(Spacer(1, 18))
    story.append(HRFlowable(width="100%", thickness=0.5, color=BORDER))
    story.append(Spacer(1, 6))
    story.append(Paragraph(
        "© 2024 MediPredict AI. All rights reserved. Not a substitute for "
        "medical advice.",
        ParagraphStyle("foot", parent=styles["Normal"], fontSize=8,
                        textColor=INK3, alignment=TA_CENTER)
    ))

    doc.build(story)
    buf.seek(0)
    return buf