import PyPDF2

pdfFileObj = open('example.pdf','rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

print(pdfReader.numPages)

pageObj = pdfReader.getPage(3)

print(pageObj.extractText())

pdfFileObj.close()