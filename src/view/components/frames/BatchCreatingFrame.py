from tkinter import *
from tktooltip import ToolTip

class BatchCreatingFrame(Frame):

    def __init__(self, master, *args, **kwargs):
        super(BatchCreatingFrame, self).__init__(master, *args, **kwargs)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.__create_widgets()
    
    def __create_widgets(self):
        self.batch_create_label = Label(self, text="Queries de Casos de Prueba")
        self.batch_create_text_box = Text(self, height=15, width=65)
        
        ToolTip(self.batch_create_text_box, msg="Aquí puede escribir queries que usarán el programa cargado para crear una batería de tests. Cada prueba diferente tiene que estar separada con un fin de linea (enter). Ej: \ndia(miercoles).\ndia(X).", delay=1.0)
        
        self.batch_create_label.place(relheight=0.1, relwidth=1)
        self.batch_create_text_box.place(rely=0.1, relheight=0.9, relwidth=1)
    
    def clean_batch_create_text_box(self):
        self.batch_create_text_box.delete('1.0', END)