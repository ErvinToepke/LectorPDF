from cProfile import label
from doctest import master
from importlib.resources import path
from logging import root
import PyPDF2,pyttsx3
from tkinter import Button, Frame, filedialog, PhotoImage, Label, ttk
import tkinter as tk

engine = pyttsx3.init()

class LectorPDF(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master = master)
        self.master = master
        self.grid()
             
        self.columnconfigure(0, weight=8)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
                    
        # Creación de frames y botones
        self._crear_frame()
        self._crear_botones()
        
        self.archivo = None
    
    def _crear_frame(self):
        """
        Método que crea el frame responsive
        """
        self._frame_text = Frame(root, bg= 'white', width=400, height=400)
        self._frame_text.grid(column=0, row=0, sticky='nsew', pady= 5, padx= 5)

        self._frame_control = Frame(root, bg= 'black', width=200, height=400)
        self._frame_control.grid(column=1, row=0, sticky='nsew', pady= 5, padx= 5)

        root.columnconfigure(0, weight=8)
        root.columnconfigure(1, weight=1)
        root.rowconfigure(0, weight=1)

        self._frame_text.grid_propagate(0)
        self._frame_control.grid_propagate(0)

        self._frame_text.columnconfigure(0, weight=1)
        self._frame_text.rowconfigure(0, weight=1)

        self._frame_control.columnconfigure([0,1], weight=1)
        self._frame_control.rowconfigure(list(range(9)), weight=1)
     
        
    def _crear_botones(self):
        """
        Método que crea los botones de control
        """
        
        # Botón Open
        self._button_open = Button(self._frame_control,image = image_file, compound= 'left',text= 'ABRIR ARCHIVO', font= ('Arial', 11, 'bold') , bg= 'blue', command= self.abrirArchivo)
        self._button_open.grid(columnspan=2, column=0, row=0, sticky='ew')

        # Botón Play
        self._button_play = Button(self._frame_control,image = image_play ,compound= 'left',text= 'REPRODUCIR ARCHIVO', font= ('Arial', 11, 'bold') , bg= 'blue', command= self.reproducir)
        self._button_play.grid(columnspan=2, column=0, row=1, sticky='ew')

        # Label Velocidad 
        Label(self._frame_control, bg='black', fg='blue', text= 'VELOCIDAD', font=('Arial', 11, 'bold')).grid(columnspan=2, column=0, row=2)
        
        # Scale Velocidad
        self._scale_velocidad = ttk.Scale(self._frame_control,from_= 150, to= 350, command= self.velocidad)
        self._scale_velocidad.grid(column=0, row=4, sticky='ew')

        # Signal Velocidad
        self._signal_velocidad = Label(self._frame_control, bg='black', fg='blue', text= '200', font=('Arial', 11, 'bold'))
        self._signal_velocidad.grid(column=1, row=4, sticky='ew')

        # Label Volumen 
        Label(self._frame_control, bg='black', fg='blue', text= 'VOLUMEN', font=('Arial', 11, 'bold')).grid(columnspan=2, column=0, row=5)

        # Scale Volumen
        self._scale_volumen = ttk.Scale(self._frame_control,from_= 0, to= 1)
        self._scale_volumen.grid(column=0, row=6, sticky='ew')
        
        self._signal_volumen = Label(self._frame_control, bg='black', fg='blue', text= '0', font=('Arial', 11, 'bold'))
        self._signal_volumen.grid(column=1, row=6, sticky='ew')
        
    def abrirArchivo(self):
        """
        Método que muestra un diálogo de apertura de archivos PDF 
        """
        self.archivos = filedialog.askopenfilename(title= 'abrir', initialdir='C:/', filetypes=(('Archivos pdf', '*.pdf'),('todos los archivos', '*.*')))
        
            
            
            
                
            
       
    def reproducir(self):
        """
        Método que reproduce archivos PDF 
        """
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        path = open(self.archivos, 'rb')
        pdfReader = PyPDF2.PdfFileReader(path)
        for pages in range(pdfReader.numPages):
            text = pdfReader.getPage(pages).extractText()
            engine.say(text)
            engine.runAndWait()
            
            
    def velocidad(self):
        level = int(self._signal_velocidad.get())
        engine.setProperty('rate', level)
        self._signal_velocidad['text']= str(level)
            
root = tk.Tk()
root.geometry('600x400+400+100')
root.title('Leer PDF')
root.config(bg='black')
root.minsize(500, 300)

#imagenes
image_file = PhotoImage(file=r'C:\Users\ervin\Desktop\UTN\lectorPDF\archivo.png') 
image_play = PhotoImage(file= r'C:\Users\ervin\Desktop\UTN\lectorPDF\play.png')


lector = LectorPDF(master = root)
lector.mainloop()