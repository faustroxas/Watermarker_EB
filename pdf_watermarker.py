import PyPDF2

pdf_file = "many_pages.pdf"
watermark = "watermark.pdf"
merged_file = "watermarked_notebook.pdf"

input_file = open(pdf_file,'rb')
input_pdf = PyPDF2.PdfFileReader(pdf_file)

watermark_file = open(watermark,'rb')
watermark_pdf = PyPDF2.PdfFileReader(watermark_file)
watermark_page = watermark_pdf.getPage(0)

output = PyPDF2.PdfFileWriter()

# Add watermark for each page
# CHANGE input_pdf.numPages into integers to change size
for x in range(0, input_pdf.numPages):
    pdf_page = input_pdf.getPage(x)
    pdf_page.mergePage(watermark_page)
    output.addPage(pdf_page)

merged_file = open(merged_file,'wb')
output.write(merged_file)

merged_file.close()
watermark_file.close()
input_file.close()