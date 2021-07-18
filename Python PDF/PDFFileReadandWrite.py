import PyPDF2,os

pdfFile = open('IPR.pdf','rb') ## to open PDF file
reader = PyPDF2.PdfFileReader(pdfFile)
print('Number of pages :', reader.numPages)
page1 = reader.getPage(0)
print()

## TO read all the files of pdf
for i in range(reader.numPages):
    print('Page:'+str(i))
    print(reader.getPage(i).extractText())

pdfFile.close()
