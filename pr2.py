# # api key = jowjetxcudqm
# # import pdftables_api
# import tabula
# import pandas
# df = tabula.read_pdf('2016.pdf', pages = 3, lattice = True)[0]
# # print(df.head(10))
# # print(df.columns)
# df.columns = df.columns.str.replace('\r',' ')
# # print(df.columns)
# data = df.dropna()
# data.to_excel('2016.xlsx')
# print(data.head())



#------------------------Attempt-2---------------------------------------------------------------#

import tabula
# Read a PDF File
df = tabula.read_pdf("2016.pdf", pages='all')[0]
# convert PDF into CSV
df = df.dropna()
tabula.convert_into("2016.pdf", "2016.csv", output_format="csv", pages='all')

print(df)
