import tkinter as tk

from utils.FileHandler import FileHandler

class TextPresenter():
    
    def __init__(self, model):
        self.model = model

    def bind_view(self, view):
        self.view = view

    def submit_prolog_predicate(self, text):
        print("Text entered:", text)

    def load_text_file(self, file_path):
        return(self.model.load_knowledge_base(file_path))
        
        text = FileHandler.read_text_file(file_path)
        if text is not None:
            return(text)
        else:
            return("File not found or unable to read.")
    
    
    def query(self, query):
        self.model.query(query)