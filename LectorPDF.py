from cProfile import label
from importlib.resources import path
from webbrowser import BackgroundBrowser
import PyPDF2,pyttsx3
from tkinter import *
from tkinter import Button, Tk, Frame, font, filedialog, PhotoImage, Label, Scale, ttk, messagebox
from tkinter.scrolledtext import ScrolledText

   
def abrirArchivo(self):
 archivos = filedialog.askopenfilename(title= 'abrir', initialdir='C:/', filetypes=(('Archivos pdf', '*.pdf'),('todos los archivos', '*.*')))
 if archivos:
        with open(archivos, 'rb') as path:
                pdfReader = PyPDF2.PdfFileReader(path)
                vent.title(archivos)
       
def reproducir():
        
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        with open(archivos,'rb') as path:
            pdfReader = PyPDF2.PdfFileReader(path)
        for pages in range(pdfReader.numPages):
            text = pdfReader.getPage(pages).extractText()
            engine.say(text)
            engine.runAndWait()
              
       

        
vent=Tk()
engine = pyttsx3.init()
vent.geometry('600x400+400+100')
vent.title('Leer PDF')
vent.config(bg='black')
vent.minsize(500, 300)

image_file = PhotoImage(file= r'C:\Users\ervin\Desktop\UTN\lectorPDF\archivo.png') 
image_play = PhotoImage(file= r'C:\Users\ervin\Desktop\UTN\lectorPDF\play.png') 

Frame_text = Frame(vent, bg= 'white', width=400, height=400)
Frame_text.grid(column=0, row=0, sticky='nsew', pady= 5, padx= 5)

Frame_control = Frame(vent, bg= 'black', width=200, height=400)
Frame_control.grid(column=1, row=0, sticky='nsew', pady= 5, padx= 5)

vent.columnconfigure(0, weight=8)
vent.columnconfigure(1, weight=1)
vent.rowconfigure(0, weight=1)

Frame_text.grid_propagate(0)
Frame_control.grid_propagate(0)

Frame_text.columnconfigure(0, weight=1)
Frame_text.rowconfigure(0, weight=1)

Frame_control.columnconfigure([0,1], weight=1)
Frame_control.rowconfigure([0,1,2,3,4,5,6,7,8], weight=1)
     

button_open = Button(Frame_control,image = image_file,compound= 'left',text= 'ABRIR ARCHIVO', font= ('Arial', 11, 'bold') , bg= 'blue', command= abrirArchivo)
button_open.grid(columnspan=2, column=0, row=0, sticky='ew')


button_play = Button(Frame_control,image = image_play,compound= 'left',text= 'REPRODUCIR ARCHIVO', font= ('Arial', 11, 'bold') , bg= 'blue', command= reproducir)
button_play.grid(columnspan=2, column=0, row=1, sticky='ew')

Label(Frame_control, bg='black', fg='blue', text= 'VELOCIDAD', font=('Arial', 11, 'bold')).grid(columnspan=2, column=0, row=2)

Scale_velocidad = ttk.Scale(Frame_control,from_= 150, to= 350)
Scale_velocidad.grid(column=0, row=4, sticky='ew')

signal_velocidad = Label(Frame_control, bg='black', fg='blue', text= '200', font=('Arial', 11, 'bold'))
signal_velocidad.grid(column=1, row=4, sticky='ew')

Label(Frame_control, bg='black', fg='blue', text= 'VOLUMEN', font=('Arial', 11, 'bold')).grid(columnspan=2, column=0, row=5)

Scale_volumen = ttk.Scale(Frame_control,from_= 0, to= 1)
Scale_volumen.grid(column=0, row=6, sticky='ew')

signal_volumen = Label(Frame_control, bg='black', fg='blue', text= '1', font=('Arial', 11, 'bold'))
signal_volumen.grid(column=1, row=6, sticky='ew')

style = ttk.Style()
style.configure('Horizontal.TScale', background='black')

vent.mainloop()