from model.PrologReader import PrologReader
from utils.FileHandler import FileHandler

class Model():
    def __init__(self):
        self.prolog_reader = PrologReader()
    
    def bind_presenter(self, presenter):
        self.presenter = presenter
    
    def load_knowledge_base(self, knowledge_base_path):
        text = FileHandler.read_text_file(knowledge_base_path)
        if text is not None:
            self.prolog_reader.set_knowledge_base(knowledge_base_path)
            self.prolog_reader.consult_knowledge_base()
            return(text)
        else:
            return("File not found or unable to read.")
    
    def query(self, query):
        return(self.prolog_reader.query(query))
    
    