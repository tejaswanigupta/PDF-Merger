from pypdf import PdfWriter
merger = PdfWriter()

# import pypdf
# merger = pypdf.PdfWriter()

for pdf in ["1 Semester Result.pdf", "2 Semester Result.pdf", "3 Semester Result.pdf", "4 Semester Result.pdf", "5 Semester Result.pdf", "6 Semester Result.pdf"]:
    merger.append(pdf)

merger.write("mergedResult.pdf")
