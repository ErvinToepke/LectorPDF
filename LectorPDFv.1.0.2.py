import PyPDF2, pyttsx3
from tkinter import Button, Tk, Frame, filedialog, PhotoImage, Label, ttk, Text
from threading import Thread
import os


class LectorPDF(Tk):
    def __init__(self):
        super().__init__()
        
        # Configuración de la ventana
        self.geometry('600x400+400+100')
        self.title('Leer PDF')
        self.config(bg='black')
        self.minsize(500, 300)
        self.columnconfigure(0, weight=8)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        
        # Definición del motor (?)
        self._engine = pyttsx3.init()
        self._reproduciendo = False
        
        # Imágenes
        self._image_file = PhotoImage(file= r'./archivo.png') 
        self._image_play = PhotoImage(file= r'./play.png')
        self._image_pause = PhotoImage(file= r'./pause.png')
        
        # Creación de frames y botones
        self._crear_frame()
        self._crear_botones()
    
    def _crear_frame(self):
        """
        Método que crea el frame principal (?)
        """
        # Frame Text
        self._frame_text = Frame(self, bg= 'white', width=400, height=400)
        self._frame_text.grid(column=0, row=0, sticky='nsew', pady= 5, padx= 5)
        self._frame_text.columnconfigure(0, weight=1)
        self._frame_text.rowconfigure(0, weight=1)
        self._campo_texto = Text(self._frame_text, wrap='word')
        self._campo_texto.grid(row=0, column=1, sticky='nsew')
        
        # Frame Control
        self._frame_control = Frame(self, bg= 'black', width=200, height=400)
        self._frame_control.grid(column=1, row=0, sticky='nsew', pady= 5, padx= 5)
        self._frame_text.grid_propagate(0)
        self._frame_control.grid_propagate(0)
        self._frame_control.columnconfigure([0,1], weight=1)
        self._frame_control.rowconfigure(list(range(9)), weight=1)
        
    def _crear_botones(self):
        """
        Método que crea los botones de control
        """
        # Botón Open
        self._button_open = Button(self._frame_control,image = self._image_file,compound= 'left',text= 'ABRIR ARCHIVO', font= ('Arial', 11, 'bold') , bg= 'blue', command= self._abrirArchivo)
        self._button_open.grid(columnspan=2, column=0, row=0, sticky='ew')

        # Botón Play
        self._button_play = Button(self._frame_control,image = self._image_play,compound= 'left',text= 'LEER', font= ('Arial', 11, 'bold') , bg= 'blue', command= self._cambiarPause)
        self._button_play.grid(columnspan=2, column=0, row=1, sticky='ew')
        

        # Label Velocidad 
        Label(self._frame_control, bg='black', fg='blue', text= 'VELOCIDAD', font=('Arial', 11, 'bold')).grid(columnspan=2, column=0, row=2)
        
        # Scale Velocidad
        self._scale_velocidad = ttk.Scale(self._frame_control,from_= 150, to= 350)
        self._scale_velocidad.grid(column=0, row=4, sticky='ew')

        # Signal Velocidad
        self._signal_velocidad = Label(self._frame_control, bg='black', fg='blue', text= '200', font=('Arial', 11, 'bold'))
        self._signal_velocidad.grid(column=1, row=4, sticky='ew')

        # Label Volumen 
        Label(self._frame_control, bg='black', fg='blue', text= 'VOLUMEN', font=('Arial', 11, 'bold')).grid(columnspan=2, column=0, row=5)

        # Scale Volumen
        self._scale_volumen = ttk.Scale(self._frame_control,from_= 0, to= 1)
        self._scale_volumen.grid(column=0, row=6, sticky='ew')
        
         # Signal Volumen
        self._signal_volumen = Label(self._frame_control, bg='black', fg='blue', text= '200', font=('Arial', 11, 'bold'))
        self._signal_volumen.grid(column=1, row=4, sticky='ew')
        
    def _abrirArchivo(self):
        """
        Método que muestra un diálogo de apertura de archivos PDF 
        """
        self._archivos = filedialog.askopenfilename(title= 'abrir', initialdir='C:/', filetypes=(('Archivos pdf', '*.pdf'),('todos los archivos', '*.*')))
        if self._archivos:
            with open(self._archivos, 'rb') as path:
                pdfReader = PyPDF2.PdfFileReader(path)
                self._q_pages = pdfReader.numPages
                for pages in range(self._q_pages):
                    self._text = pdfReader.getPage(pages).extractText()
            self.title(self._archivos) # ???
            
    def _cambiarPause(self):
        """
        Metodo de cambio de iconos play/pause
        """
        if not self._reproduciendo:
            self._reproduciendo = True
            self._button_play ['image'] = self._image_play
            
            self._leer()
        else:
            self._reproduciendo = False
            self._button_play ['image'] = self._image_pause
            self._engine.endLoop()
        
    def _reproducir(self):
        """
        Método que reproduce el texto del PDF en español
        """
        if self._reproduciendo:  
            self._text          
            thread = Thread(target=self._leer, args=(self._text,), daemon=True)
            thread.start()
            self.poll_thread(thread)     
            
    def poll_thread(self, thread):
        if Thread.is_alive():
            self.after(100, lambda : self.poll_thread(thread))
        else:
            # self.next_page()
            pass
        
    def _leer(self):
        voices = self._engine.getProperty('voices')
        self._engine.setProperty('voice', voices[1].id)
        self._engine.say(self._text)
        self._engine.startLoop() 


if __name__ == '__main__':
    
    app = LectorPDF()
    app.mainloop()