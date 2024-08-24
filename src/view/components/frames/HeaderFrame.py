from tkinter import *
from tktooltip import ToolTip

class HeaderFrame(Frame):

    def __init__(self, master, functions, *args, **kwargs):
        super(HeaderFrame, self).__init__(master, *args, **kwargs)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self._create_widgets(functions)
    
    def _create_widgets(self, functions):
        self.submit_knowledge_base_button = Button(self, text="Cargar Base de Conocimiento", command=lambda: functions[0]())
        self.testing_mode_button = Button(self, text="Probar", width=20, command=lambda: functions[1]())
        self.manual_creating_mode_button = Button(self, text="Crear Tests", width=20, command=lambda: functions[2]())
        
        ToolTip(self.submit_knowledge_base_button, msg="Carga la base de conocimiento, la cual será usada para realizar los tests.", delay=1.0)
        ToolTip(self.testing_mode_button, msg="Permite correr una batería de tests sobre la base de conocimiento cargada.", delay=1.0)
        ToolTip(self.manual_creating_mode_button, msg="Permite colocar queries y sus resultados esperados para armar una batería de tests para su futuro uso.", delay=1.0)
        self.testing_mode_button.config(state = "disabled")
        
        self.submit_knowledge_base_button.grid(row = 0, column = 0, pady = 2)
        self.testing_mode_button.grid(row = 0, column = 2, pady = 2, padx= 10)
        self.manual_creating_mode_button.grid(row = 0, column = 3, pady = 2)
