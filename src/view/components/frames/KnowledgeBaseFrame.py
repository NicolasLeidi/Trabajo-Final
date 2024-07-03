import tkinter as tk
from tkinter import *
from tktooltip import ToolTip

class KnowledgeBaseFrame(tk.Frame):

    def __init__(self, master, *args, **kwargs):
        super(KnowledgeBaseFrame, self).__init__(master, *args, **kwargs)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.__create_widgets()
    
    def __create_widgets(self):
        self.knowledge_base_label = tk.Label(self, text="Base de Conocimiento")
        self.__knowledge_base_text_box = Text(self)
        
        ToolTip(self.__knowledge_base_text_box, msg="Base de conocimiento cargada, será usada para realizar pruebas.", delay=1.0)
        self.__knowledge_base_text_box.config(state = "disabled")
        self.__knowledge_base_text_box.configure(bg="gray")
        
        self.knowledge_base_label.place(relheight=0.05, relwidth=1)
        self.__knowledge_base_text_box.place(rely=0.05,relheight=0.95, relwidth=1)
    
    def config_knowledge_base_label(self, **kwargs):
        self.knowledge_base_label.config(**kwargs)
    
    def config_knowledge_base_text_box(self, **kwargs):
        self.__knowledge_base_text_box.config(**kwargs)
    
    def insert_knowledge_base_text_box(self, text):
        self.__knowledge_base_text_box.config(state = "normal")
        self.__knowledge_base_text_box.insert(END, text)
        self.__knowledge_base_text_box.config(state = "disabled")