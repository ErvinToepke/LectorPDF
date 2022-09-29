def abrirArchivo():
   Archivos = filedialog.askopenfilename(title= 'abrir', initialdir='C:/', filetypes=(('Archivos pdf', '*.pdf'),('todos los archivos', '*.*')))
   if Archivos != ' ':
        path = open(Archivos,'rb')
        content = path.read()
        pdfReader = PyPDF2.PdfFileReader(path)
        vent.title(Archivos)
        
     
       
def reproducir():
        text = pdfReader.getPage(pages).extractText()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
              
        for pages in range(pdfReader.numPages):
                engine.say(text)
                engine.runAndWait()
                
              