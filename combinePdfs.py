import PyPDF2, os

pdfFiles=[]

for filename in os.listdir('.'):
	if filename.endswith('.pdf'):
		pdfFiles.append(filename)

pdfFiles.sort(key = str.lower)

pdfWriter = PyPDF2.PdfFileWriter()

for filename in pdfFiles:
	pdfFileObj = open(filename,'rb')
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

	pageObj = pdfReader.getPage(0)
	pdfWriter.addPage(pageObj)

pdfOutput = open('thisBookHasNoChapters.pdf','wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()