import tkinter as tk
from tkinter import filedialog
from tktooltip import ToolTip

class HeaderFrame(tk.Frame):

    def __init__(self, master, functions, *args, **kwargs):
        super(HeaderFrame, self).__init__(master, *args, **kwargs)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.__create_widgets(functions)
    
    def __create_widgets(self, functions):
        self.__submit_knowledge_base_button = tk.Button(self, text="Cargar Base de Conocimiento", command=lambda: functions[0]())
        self.__testing_mode_button = tk.Button(self, text="Modo de Prueba", width=20, command=lambda: functions[1]())
        self.__batch_creating_mode_button = tk.Button(self, text="Modo de Creación", width=20, command=lambda: functions[2]())
        self.__manual_creating_mode_button = tk.Button(self, text="Creación Manual", width=20, command=lambda: functions[3]())
        
        ToolTip(self.__submit_knowledge_base_button, msg="Carga la base de conocimiento, la cual será usada para realizar las pruebas.", delay=1.0)
        ToolTip(self.__testing_mode_button, msg="Entra al modo prueba, en el cual permite correr una batería de tests sobre la base de conocimiento cargada.", delay=1.0)
        ToolTip(self.__batch_creating_mode_button, msg="Entra al modo creación en grupos, en el cual permite crear una batería de tests utilizando la base de conocimiento cargada para obtener los resultados esperados.", delay=1.0)
        ToolTip(self.__manual_creating_mode_button, msg="Entra a l modo de creación manualmente, en el cual permite colocar queries y sus resultados esperados para armar una batería de tests.", delay=1.0)
        self.__testing_mode_button.config(state = "disabled")
        self.__batch_creating_mode_button.config(state = "disabled")
        
        self.__submit_knowledge_base_button.grid(row = 0, column = 0, pady = 2)
        self.__testing_mode_button.grid(row = 0, column = 2, pady = 2, padx=(10,0))
        self.__batch_creating_mode_button.grid(row = 0, column = 3, pady = 2, padx = 10)
        self.__manual_creating_mode_button.grid(row = 0, column = 4, pady = 2)
    
    def config_submit_knowledge_base_button(self, **kwargs):
        self.__submit_knowledge_base_button.config(**kwargs)
    
    def config_testing_mode_button(self, **kwargs):
        self.__testing_mode_button.config(**kwargs)
    
    def config_batch_creating_mode_button(self, **kwargs):
        self.__batch_creating_mode_button.config(**kwargs)
    
    def config_manual_creating_mode_button(self, **kwargs):
        self.__manual_creating_mode_button.config(**kwargs)
