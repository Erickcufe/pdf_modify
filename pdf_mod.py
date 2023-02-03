# coding=utf-8
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger
import StringIO
import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

packet = StringIO.StringIO()
# create a new PDF with Reportlab

#sign2 = input("Nombre que quiero poner")
#sing2 = str(sing2)

can = canvas.Canvas(packet, pagesize=letter)

# CAMPO DE VALIDÓ
can.setFont('Helvetica-Bold', 10)
can.drawString(184, 263, "VALIDÓ")

can.setFont('Helvetica-Bold', 10)
can.drawString(118, 216, "ING. GLORIA LAURA SEGOVIA CRUZ")

can.setFont('Helvetica-Bold', 10)
can.drawString(116, 204, "GERENTE DE INFRAESTRUCTURA DE")

can.setFont('Helvetica-Bold', 10)
can.drawString(122, 192, "TECNOLOGÍAS DE INFORMACIÓN")

# CAMPO DE AUTORIZÓ
can.drawString(390, 263, "AUTORIZÓ")

can.drawString(330, 216, "LIC. CHRISTIAN VARGAS AGUILAR")

can.drawString(324, 204,"SUBDIRECTOR DE TECNOLOGÍAS DE")

can.drawString(380, 192, "INFORMACIÓN")

can.save()

#move to the beginning of the StringIO buffer
packet.seek(0)
new_pdf = PdfFileReader(packet)
# read your existing PDFs
#path_pdf = input("Pon el PATH o ruta de la carpeta donde se encuentran tus PDFs:")
docs = os.listdir("pdfs_firmar")
for entry in docs:
    path_pdf = "pdfs_firmar/" + entry
    existing_pdf = PdfFileReader(path_pdf)
    output = PdfFileWriter()
    page = existing_pdf.getPage(0)
    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)
    # finally, write "output" to a real file
    path_dt = entry + "_" + "FIRMADO"
    outputStream = open(path_dt, "wb")
    output.write(outputStream)
    outputStream.close()


#existing_pdf = PdfFileReader("ejemplo.pdf")
#output = PdfFileWriter()
# add the "watermark" (which is the new pdf) on the existing page
#page = existing_pdf.getPage(0)
#page.mergePage(new_pdf.getPage(0))
#output.addPage(page)
# finally, write "output" to a real file
#outputStream = open("destination.pdf", "wb")
#output.write(outputStream)
#outputStream.close()

