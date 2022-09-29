with open(self._archivos, 'rb') as path:
                pdfReader = PyPDF2.PdfFileReader(path)
                self.title(self._archivos)