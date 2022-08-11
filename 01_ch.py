# import PyPDF2
# a=PyPDF2.PdfFileReader('2016.pdf')
# print(a.documentInfo)
from PyPDF2 import PdfReader

reader = PdfReader("2016.pdf")
page = reader.pages[0]
print(page.extract_text(0,90))