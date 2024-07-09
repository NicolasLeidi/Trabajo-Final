from tkinter import *
from tktooltip import ToolTip

class LoadedExamplesFrame(Frame):

    def __init__(self, master, *args, **kwargs):
        super(LoadedExamplesFrame, self).__init__(master, *args, **kwargs)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.__create_widgets()
    
    def __create_widgets(self):
        self.loaded_examples_label = Label(self, text="Ejemplos Cargados en la Batería de Pruebas")
        self.loaded_examples_text_box = Text(self, height=15, width=65)
        
        ToolTip(self.loaded_examples_text_box, msg="Ejemplos cargados actualmente a la nueva batería de tests.", delay=1.0)
        self.loaded_examples_text_box.config(state = "disabled")
        self.loaded_examples_text_box.configure(bg="gray")
        
        self.loaded_examples_label.place(relheight=0.1, relwidth=1)
        self.loaded_examples_text_box.place(rely=0.1, relheight=0.9, relwidth=1)
    
    def clean_loaded_examples_text_box(self):
        """
        Cleans the loaded examples text box by enabling it, deleting all its content, and disabling it.
        """
        self.loaded_examples_text_box.config(state = "normal")
        self.loaded_examples_text_box.delete('1.0', END)
        self.loaded_examples_text_box.config(state = "disabled")
    
    def insert_loaded_examples_text_box(self, text):
        """
        Inserts the given text into the loaded examples text box.

        Args:
            text (str): The text to be inserted.
        """
        self.loaded_examples_text_box.config(state = "normal")
        self.loaded_examples_text_box.insert(END, text)
        self.loaded_examples_text_box.config(state = "disabled")