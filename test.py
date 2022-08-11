import PyPDF2
a=PyPDF2.PdfFileReader('2016.pdf')
str = ""
str+=a.getPage(0).extract_text()
with open("text.txt","w",encoding='utf-8') as f:
    f.write(str)