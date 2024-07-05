from tkinter import *
from tktooltip import ToolTip

class ManualCreatingFrame(Frame):

    def __init__(self, master, *args, **kwargs):
        super(ManualCreatingFrame, self).__init__(master, *args, **kwargs)
        self.grid_rowconfigure(0, weight=1)
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)
        self.__create_widgets()
    
    def __create_widgets(self):
        self.manual_create_query_label = Label(self, text="Crear Query de Caso de Prueba")
        self.manual_create_query_text_box = Text(self)
        self.manual_create_expected_result_label = Label(self, text="Resultado Esperado del Caso de Prueba")
        self.manual_create_expected_result_text_box = Text(self)
        
        ToolTip(self.manual_create_query_text_box, msg="Aquí puede colocar el query a probar. Limitado a una query por prueba.", delay=1.0)
        ToolTip(self.manual_create_expected_result_text_box, msg="Aquí tiene que colocar el resultado esperado de la query de arriba. Respetar sintaxis:\nVariable : Valor, múltiples variables separadas con punto y coma en el orden que aparecen. Ej: X : [1, 2]; Y : 3\nSi hay múltiples resultados, cada uno debe estar en diferentes lineas separadas por un enter. Ej:\nX: 1\nX: 2\nUn resultado True o False simplemente se escribe True o False.", delay=1.0)
        
        self.manual_create_query_label.place(relheight=0.05, relwidth=1)
        self.manual_create_query_text_box.place(rely=0.05, relheight=0.45, relwidth=1)
        self.manual_create_expected_result_label.place(rely=0.5, relheight=0.05, relwidth=1)
        self.manual_create_expected_result_text_box.place(rely=0.55, relheight=0.45, relwidth=1)