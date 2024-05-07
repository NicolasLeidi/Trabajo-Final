import tkinter as tk

from utils.FileHandler import FileHandler

class TextPresenter():
    
    def __init__(self, model):
        self.model = model

    def bind_view(self, view):
        self.view = view

    def submit_prolog_predicate(self, text):
        print("Text entered:", text)
        self.model.submit_prolog_predicate(text)

    def load_text_file(self, file_path):
        return(self.model.load_knowledge_base(file_path))    
    
    def query(self, query):
        return(self.model.query(query))
    
    def examples(self, examples):
        self.model.submit_examples(examples)