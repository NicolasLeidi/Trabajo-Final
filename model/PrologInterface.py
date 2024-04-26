from pyswip.core import *
from pyswip.prolog import Prolog
from pyswip import Functor, Variable, Query, call
from utils.PrologPredicate import PrologPredicate

class PrologInterface():
    
    def __init__(self):
        self.prolog = Prolog()
    
    def consult_knowledge_base(self):
        print(self.knowledge_base)
        self.prolog.consult(self.knowledge_base)
    
    def set_knowledge_base(self, knowledge_base):
        self.knowledge_base = knowledge_base
    
    def query(self, query):
        print(query)
        return list(self.prolog.query(query))
    
    def set_prolog_predicate(self, predicate):
        self.prolog_predicate = PrologPredicate(predicate)
        print("Nombre: ", self.prolog_predicate.name)
        print("Input: ", self.prolog_predicate.input_parameters)
        print("Output: ", self.prolog_predicate.output_parameters)
        print("Input u Output: ", self.prolog_predicate.input_or_output_parameters)
    