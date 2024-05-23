import json
import logging
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
            return(True, "Base de conocimiento cargada")
        else:
            logging.warning("Archivo no encontrado o no se pudo leer.")
            return(False, "Error")
    
    def query(self, query):
        return(self.prolog_interface.query(query))
    
    def submit_examples(self, examples, file_path):
        examples_list = examples.splitlines()
        print(examples_list)
        for example in examples_list:
            self.prolog_interface.add_example(example)
            
        FileHandler.write_text_file(file_path, json.dumps(self.prolog_interface.get_examples()))
        
        # Para probar los ejemplos
        recovered = json.loads(FileHandler.read_text_file(file_path))
        
        self.prolog_interface.test_examples(recovered)
    
    def load_examples(self, file_path):
        self.prolog_interface.empty_examples_base()
        
        examples = json.loads(FileHandler.read_text_file(file_path))
        
        # Hay que recuperar los ejemplos y devolverlos sin correrlos
        
        for example in examples:
            self.prolog_interface.add_example_to_base(example)
        
        return(self.prolog_interface.get_examples())
    
    def test_examples(self, file_path):
        return self.prolog_interface.test_examples(json.loads(FileHandler.read_text_file(file_path)))
    
    def run_examples(self):
        return self.prolog_interface.test_examples()
    