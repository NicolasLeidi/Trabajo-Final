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
        self.batch_create_label = Label(self, text="Crear Ejemplo")
        self.batch_create_text_box = Text(self, height=15, width=65)
        
        ToolTip(self.batch_create_text_box, msg="Aquí puede escribir queries que usarán el programa cargado para crear una batería de tests.", delay=1.0)
        
        self.batch_create_label.place(relheight=0.1, relwidth=1)
        self.batch_create_text_box.place(rely=0.1, relheight=0.9, relwidth=1)
        