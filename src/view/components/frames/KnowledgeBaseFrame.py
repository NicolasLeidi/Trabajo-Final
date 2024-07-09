from tkinter import *
from tktooltip import ToolTip

class KnowledgeBaseFrame(Frame):

    def __init__(self, master, *args, **kwargs):
        super(KnowledgeBaseFrame, self).__init__(master, *args, **kwargs)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.__create_widgets()
    
    def __create_widgets(self):
        self.knowledge_base_label = Label(self, text="Base de Conocimiento")
        self.knowledge_base_text_box = Text(self)
        
        ToolTip(self.knowledge_base_text_box, msg="Base de conocimiento cargada, será usada para realizar pruebas.", delay=1.0)
        self.knowledge_base_text_box.config(state = "disabled")
        self.knowledge_base_text_box.configure(bg="gray")
        
        self.knowledge_base_label.place(relheight=0.05, relwidth=1)
        self.knowledge_base_text_box.place(rely=0.05,relheight=0.95, relwidth=1)
    
    def insert_knowledge_base_text_box(self, text):
        """
        Inserts the given text into the knowledge base text box.

        Args:
            text (str): The text to be inserted.
        """
        self.knowledge_base_text_box.config(state = "normal")
        self.knowledge_base_text_box.insert(END, text)
        self.knowledge_base_text_box.config(state = "disabled")
    
    def clean_knowledge_base_text_box(self):
        """
        Cleans the knowledge base text box by resetting its content and disabling editing.
        """
        self.knowledge_base_text_box.config(state = "normal")
        self.knowledge_base_text_box.delete('1.0', END)
        self.knowledge_base_text_box.config(state = "disabled")