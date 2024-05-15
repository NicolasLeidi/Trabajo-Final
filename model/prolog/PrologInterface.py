from pyswip.core import *
from pyswip.prolog import Prolog
from model.prolog.predicate.PredicateDefinition import PredicateDefinition

class PrologInterface():
    
    def __init__(self):
        self.prolog = Prolog()
        self.examples_base = []
    
    def consult_knowledge_base(self):
        print(self.knowledge_base)
        self.prolog.consult(self.knowledge_base)
    
    def set_knowledge_base(self, knowledge_base):
        self.knowledge_base = knowledge_base
    
    def query(self, query):
        print(query)
        return list(self.prolog.query(query))
    
    def set_prolog_predicate(self, predicate):
        self.prolog_predicate = PredicateDefinition(predicate)
        print("Nombre: ", self.prolog_predicate.name)
        print("Input: ", self.prolog_predicate.input_parameters)
        print("Output: ", self.prolog_predicate.output_parameters)
        print("Input u Output: ", self.prolog_predicate.input_or_output_parameters)
        print("Predicado recuperado: ", self.prolog_predicate)
    
    def add_example(self, example):
        result = self.query(example)
        self.examples_base.append([example, result])
    
    def get_examples(self):
        return self.examples_base
    
    def test_examples(self):        
        feedback = ""
        for example, expected_result in self.examples_base:
            feedback += self._run_example(example, expected_result)
        return feedback
    
    def test_examples(self, examples):
        feedback = ""
        for example, expected_result in examples:
            feedback += self._run_example(example, expected_result)
        return feedback
    
    def _run_example(self, example, expected_result):
        result = self.query(example)
            
        print("Example: ", example)
        print("Expected result: ", expected_result)
        print("Actual result: ", result)
        
        if result == expected_result:
            return("Test passed")
        else:
            return("Test failed")
            
    