from tkinter import Button

from tktooltip import ToolTip
from view.components.frames.HeaderFrame import HeaderFrame

class TeacherHeaderFrame(HeaderFrame):
    
    def _create_widgets(self, functions):
        self.submit_knowledge_base_button = Button(self, text="Cargar Base de Conocimiento", command=lambda: functions[0]())
        self.testing_mode_button = Button(self, text="Probar", width=20, command=lambda: functions[1]())
        self.batch_creating_mode_button = Button(self, text="Crear Tests Asistido", width=20, command=lambda: functions[2]())
        self.manual_creating_mode_button = Button(self, text="Crear Tests", width=20, command=lambda: functions[3]())
        
        ToolTip(self.submit_knowledge_base_button, msg="Carga la base de conocimiento, la cual será usada para realizar los tests.", delay=1.0)
        ToolTip(self.testing_mode_button, msg="Permite correr una batería de tests sobre la base de conocimiento cargada.", delay=1.0)
        ToolTip(self.batch_creating_mode_button, msg="Permite crear una batería de tests colocando queries y utilizando la base de conocimiento cargada para obtener los resultados esperados.", delay=1.0)
        ToolTip(self.manual_creating_mode_button, msg="Permite colocar queries y sus resultados esperados para armar una batería de tests para su futuro uso.", delay=1.0)
        self.testing_mode_button.config(state = "disabled")
        self.batch_creating_mode_button.config(state = "disabled")
        
        self.submit_knowledge_base_button.grid(row = 0, column = 0, pady = 2)
        self.testing_mode_button.grid(row = 0, column = 2, pady = 2, padx=(10,0))
        self.batch_creating_mode_button.grid(row = 0, column = 3, pady = 2, padx = 10)
        self.manual_creating_mode_button.grid(row = 0, column = 4, pady = 2)