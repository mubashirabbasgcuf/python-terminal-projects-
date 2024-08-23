# from PyPDF2 import PdfWriter

# merger = PdfWriter()

# for pdf in ["pf1.pdf", "pf2.pdf", "pf3.pdf"]:
#     merger.append(pdf)
# merger.write("merged-pdf.pdf")
# merger.close()
from PyPDF2 import PdfReader

reader = PdfReader("pf1.pdf")
page = reader.pages[2]
print(page.extract_text())