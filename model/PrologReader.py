from pyswip.core import *
from pyswip.prolog import Prolog
from pyswip import Functor, Variable, Query, call

class PrologReader():
    
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
    