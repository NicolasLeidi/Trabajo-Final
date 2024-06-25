import json
import logging
from model.exception.PrologSyntaxException import PrologSyntaxException
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
    
    def add_examples(self, examples, ordered, first_only):
        examples_list = examples.splitlines()
        try:
            for example in examples_list:
                self.prolog_interface.create_example(example, ordered, first_only)
            return (True, "Ejemplos agregados correctamente.")
        except PrologSyntaxException:
            logging.warning("Error al correr los ejemplos.")
            self.presenter.show_message("Error", "Error al correr los ejemplos. Verifique la sintaxis de los ejemplos.")
            return (False, "Error")
            
    def submit_examples(self, file_path):        
        FileHandler.write_text_file(file_path, json.dumps(self.prolog_interface.get_examples()))
        self.clean_examples()      
    
    def get_loaded_examples(self):
        return self.prolog_interface.get_examples()
    
    def clean_examples(self):
        self.prolog_interface.empty_examples_base()
        
    def load_examples(self, file_path):
        self.prolog_interface.empty_examples_base()
        
        examples = json.loads(FileHandler.read_text_file(file_path))
        
        # Hay que recuperar los ejemplos y devolverlos sin correrlos
        try:
            for example in examples:
                self.prolog_interface.add_example_to_base(example)
            
            return(self.prolog_interface.get_examples())
        except Exception:
            self.prolog_interface.empty_examples_base()
            self.presenter.show_message("Error", "Error al cargar los ejemplos.")
    
    def test_examples(self, file_path):
        try:
            return self.prolog_interface.test_examples(json.loads(FileHandler.read_text_file(file_path)))            
        except Exception:
            logging.warning("Error al correr las pruebas.")
            self.presenter.show_message("Error", "Error al correr las pruebas.")
            
    
    def run_examples(self):
        try:
            return self.prolog_interface.test_examples()
        except Exception:
            logging.warning("Error al correr las pruebas.")
            self.presenter.show_message("Error", "Error al correr las pruebas.")
    
    def clean_examples(self):
        self.prolog_interface.empty_examples_base()
    
    def pop_examples(self):
        self.prolog_interface.pop_example_from_base()