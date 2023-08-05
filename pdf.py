import PyPDF2

template = PyPDF2.PdfReader('super.pdf', 'rb')
watermark = PyPDF2.PdfReader('wtr.pdf', 'rb')
output = PyPDF2.PdfWriter()

for i in range(len(template.pages)):
    page = template.pages[i]
    page.merge_page(watermark.pages[0])
    output.add_page(page)

with open('watermarked_output_new_pdf.pdf', 'wb') as file:
    output.write(file)
