import PyPDF2,os

pdfFile1 = open('IPR.pdf','rb') ## to open PDF file
reader1 = PyPDF2.PdfFileReader(pdfFile1)


pdfFile2 = open('InformationSheet.pdf','rb') ## to open PDF file
reader2 = PyPDF2.PdfFileReader(pdfFile2)


writer = PyPDF2.PdfFileWriter()


## TO read and write files from 1st pdf file to other
for i in range(reader1.numPages):
    writer.addPage(reader1.getPage(i))

## TO read and write files from 1st pdf file to other
for i in range(reader2.numPages):
    writer.addPage(reader2.getPage(i))


##To create and write a new file
pdf3 = open('MergedFile.pdf','wb')
writer.write(pdf3)
pdf3.close()
pdfFile1.close()
pdfFile2.close()
