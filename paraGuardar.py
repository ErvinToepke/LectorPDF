voices = engine.getProperty('voices')
   engine.setProperty('voice', voices[1].id)

   path = open(Archivos,'rb')

   pdfReader = PyPDF2.PdfFileReader(path)

   for pages in range(pdfReader.numPages):
        text = pdfReader.getPage(pages).extractText()
        engine.say(text)
        engine.runAndWait()