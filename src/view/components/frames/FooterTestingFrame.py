from tkinter import *
from tktooltip import ToolTip

class FooterTestingFrame(Frame):

    def __init__(self, master, functions, *args, **kwargs):
        super(FooterTestingFrame, self).__init__(master, *args, **kwargs)
        self.grid_rowconfigure(0, weight=1)
        for i in range(6):
            self.grid_columnconfigure(i, weight=1)
        self.__create_widgets(functions)
    
    def __create_widgets(self, functions):
        self.run_tests_button = Button(self, text="Correr", width=20, command=lambda: functions[0]())
        self.clean_tests_button = Button(self, text="Limpiar", width=20, command=lambda: functions[1]())
        self.pop_test_button = Button(self, text="Remover", width=20, command=lambda: functions[2]())
        self.completed_tests_label = Label(self, text="Tests exitosos: 0 de 0")
        
        ToolTip(self.run_tests_button, msg="Corre la batería de tests cargada actualmente sobre la base de conocimiento cargada.", delay=1.0)
        
        self.run_tests_button.grid(row = 0, column = 1)
        self.clean_tests_button.grid(row = 0, column = 2)
        self.pop_test_button.grid(row = 0, column = 3)
        self.completed_tests_label.grid(row = 0, column = 4)