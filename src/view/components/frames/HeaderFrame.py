from tkinter import *
from tktooltip import ToolTip

class HeaderFrame(Frame):

    def __init__(self, master, functions, *args, **kwargs):
        super(HeaderFrame, self).__init__(master, *args, **kwargs)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.__create_widgets(functions)
    
    def __create_widgets(self, functions):
        self.submit_knowledge_base_button = Button(self, text="Cargar Base de Conocimiento", command=lambda: functions[0]())
        self.testing_mode_button = Button(self, text="Modo de Prueba", width=20, command=lambda: functions[1]())
        self.batch_creating_mode_button = Button(self, text="Modo de Creación", width=20, command=lambda: functions[2]())
        self.manual_creating_mode_button = Button(self, text="Creación Manual", width=20, command=lambda: functions[3]())
        
        ToolTip(self.submit_knowledge_base_button, msg="Carga la base de conocimiento, la cual será usada para realizar las pruebas.", delay=1.0)
        ToolTip(self.testing_mode_button, msg="Entra al modo prueba, en el cual permite correr una batería de tests sobre la base de conocimiento cargada.", delay=1.0)
        ToolTip(self.batch_creating_mode_button, msg="Entra al modo creación en grupos, en el cual permite crear una batería de tests utilizando la base de conocimiento cargada para obtener los resultados esperados.", delay=1.0)
        ToolTip(self.manual_creating_mode_button, msg="Entra al modo de creación manualmente, en el cual permite colocar queries y sus resultados esperados para armar una batería de tests.", delay=1.0)
        self.testing_mode_button.config(state = "disabled")
        self.batch_creating_mode_button.config(state = "disabled")
        
        self.submit_knowledge_base_button.grid(row = 0, column = 0, pady = 2)
        self.testing_mode_button.grid(row = 0, column = 2, pady = 2, padx=(10,0))
        self.batch_creating_mode_button.grid(row = 0, column = 3, pady = 2, padx = 10)
        self.manual_creating_mode_button.grid(row = 0, column = 4, pady = 2)
