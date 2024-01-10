import PyPDF2

f = open('pdf_1.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(f)
num_pages = len(pdf_reader.pages)
page_1 = pdf_reader.pages[0]
page_1_text = page_1.extract_text()

print(f"The document consists of {num_pages} pages\n")
print(page_1_text)

pdf_text = []
for num in range(num_pages):
    page = pdf_reader.pages[num]
    pdf_text.append(page.extract_text())
    print(f"The page {num + 1} includes {len(pdf_text[num])} characters")

pdf_writer = PyPDF2.PdfWriter()
pdf_writer.add_page(page_1)
pdf_output = open('pdf_new.pdf', 'wb')
pdf_writer.write(pdf_output)
f.close()
pdf_output.close()
