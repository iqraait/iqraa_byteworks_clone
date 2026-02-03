from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from django.http import HttpResponse


def generate_patient_bill_pdf(patient):
    # Response with PDF header
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f'attachment; filename="Patient_{patient.id}.pdf"'

    # Create PDF document
    doc = SimpleDocTemplate(response, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []

    # Title
    story.append(Paragraph("<b>🏥 IQRAA HOSPITAL REGISTRATION Bill</b>", styles['Title']))
    story.append(Spacer(1, 20))

    # ✅ Patient Info Table (only first_name + middle_name)
    patient_data = [
        ["Patient Name:", f"{patient.first_name} {patient.middle_name or ''}"],
        ["Mobile:", patient.mobile_number],
        ["Gender:", patient.get_gender_display()],
        ["Patient Type:", patient.get_patient_type_display()],
        ["Department:", patient.department.name if patient.department else "N/A"],
        ["Doctor:", patient.doctor_name.name if patient.doctor_name else "N/A"],
        ["Appointment Date:", str(patient.appoinment_date)],
    ]

    table = Table(patient_data, colWidths=[150, 300])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (1, 0), colors.lightblue),
        ("TEXTCOLOR", (0, 0), (-1, -1), colors.black),
        ("ALIGN", (0, 0), (-1, -1), "LEFT"),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
    ]))
    story.append(table)
    story.append(Spacer(1, 20))

    # ✅ Fees Section (from Doctor model)
    if patient.doctor_name:
        consulting_fee = patient.doctor_name.op_consulting or 0
        service_fee = patient.doctor_name.service_fee or 0
        total = consulting_fee + service_fee

        fee_data = [
            ["Consulting Fee", f"₹ {consulting_fee}"],
            ["Service Fee", f"₹ {service_fee}"],
            ["Total", f"₹ {total}"],
        ]

        fee_table = Table(fee_data, colWidths=[200, 200])
        fee_table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
            ("ALIGN", (1, 0), (-1, -1), "RIGHT"),
            ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),
        ]))
        story.append(fee_table)

    # Build and return PDF
    doc.build(story)
    return response
