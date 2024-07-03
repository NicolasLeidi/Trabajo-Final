from tkinter import *
from tktooltip import ToolTip

class TestingFrame(Frame):

    def __init__(self, master, *args, **kwargs):
        super(TestingFrame, self).__init__(master, *args, **kwargs)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.__create_widgets()
    
    def __create_widgets(self):
        self.test_label = Label(self, text="Batería de Tests")
        self.test_text_box = Text(self)
        
        ToolTip(self.test_text_box, msg="Batería de test cargada actualmente, la cual será ejecutada al presionar Correr.", delay=1.0)
        self.test_text_box.config(state = "disabled")
        
        self.test_label.place(relheight=0.05, relwidth=1)
        self.test_text_box.place(rely=0.05, relheight=0.95, relwidth=1)
    
    def insert_test_text_box(self, text):
        self.test_text_box.config(state = "normal")
        self.test_text_box.insert(END, text)
        self.test_text_box.config(state = "disabled")
    
    def clean_test_text_box(self):
        self.test_text_box.config(state = "normal")
        self.test_text_box.delete('1.0', END)
        self.test_text_box.config(state = "disabled")