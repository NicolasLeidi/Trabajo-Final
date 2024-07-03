from tkinter import *
from tktooltip import ToolTip

class FooterCreatingFrame(Frame):

    def __init__(self, master, variables, functions, *args, **kwargs):
        super(FooterCreatingFrame, self).__init__(master, *args, **kwargs)
        self.grid_rowconfigure(0, weight=1)
        for i in range(3):
            self.grid_columnconfigure(i, weight=1)
        self.__create_widgets(variables, functions)
    
    def __create_widgets(self, variables, functions):
        self.ordered_checkbox = Checkbutton(self, text="Sin Orden", variable= variables[0])
        self.first_only_checkbox = Checkbutton(self, text="Primer Resultado", variable= variables[1])
        self.add_tests_button = Button(self, text="Agregar", width=20, command=lambda: functions[0]())
        self.save_tests_button = Button(self, text="Guardar", width=20, command=lambda: functions[1]())
        self.clean_examples_button = Button(self, text="Limpiar", width=20, command=lambda: functions[2]())
        self.pop_examples_button = Button(self, text="Deshacer", width=20, command=lambda: functions[3]())
        
        ToolTip(self.add_tests_button, msg="Agrega un ejemplo a la batería de tests cargada actualmente.", delay=1.0)
        ToolTip(self.save_tests_button, msg="Guarda la batería de tests cargada actualmente.", delay=1.0)
        ToolTip(self.clean_examples_button, msg="Limpia todos los ejemplos cargados actualmente.", delay=1.0)
        ToolTip(self.pop_examples_button, msg="Deshace el último ejemplo cargado actualmente.", delay=1.0)
        ToolTip(self.ordered_checkbox, msg="Cambia el comportamiento de la batería de tests, compara los conjuntos de resultados sin importar el orden.", delay=1.0)
        ToolTip(self.first_only_checkbox, msg="Cambia el comportamiento de la batería de tests, solo compara la primera unificación.", delay=1.0)
        
        self.ordered_checkbox.grid(row = 0, column = 0, padx = 10)
        self.first_only_checkbox.grid(row = 0, column = 1, padx = 10)
        self.add_tests_button.grid(row = 0, column = 2, padx = 10)
        self.pop_examples_button.grid(row = 0, column = 3, padx = 10)
        self.clean_examples_button.grid(row = 1, column = 0, padx = 10)
        self.save_tests_button.grid(row = 1, column = 3, padx = 10)