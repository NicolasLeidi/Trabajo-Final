from model.prolog.PrologInterface import PrologInterface
from utils.FileHandler import FileHandler

class Model():
    def __init__(self):
        self.prolog_interface = PrologInterface()
    
    def bind_presenter(self, presenter):
        self.presenter = presenter
    
    def load_knowledge_base(self, knowledge_base_path):
        text = FileHandler.read_text_file(knowledge_base_path)
        if text is not None:
            self.prolog_interface.set_knowledge_base(knowledge_base_path)
            self.prolog_interface.consult_knowledge_base()
            return(text)
        else:
            return("File not found or unable to read.")
    
    def query(self, query):
        return(self.prolog_interface.query(query))
    
    def submit_prolog_predicate(self, prolog_predicate):
        self.prolog_interface.set_prolog_predicate(prolog_predicate)
    
    def submit_examples(self, examples):
        examples_list = examples.splitlines()
        for example in examples_list:
            PrologInterface.
    
    