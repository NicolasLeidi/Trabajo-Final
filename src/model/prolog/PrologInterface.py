from pyswip.core import *
from pyswip.prolog import Prolog
from utils.FeedbackEnum import FeedbackEnum

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
        prolog_result = self.prolog.query(query)
        return list(prolog_result)
    
    def create_example(self, example):
        result = self.query(example)
        self.examples_base.append([example, result])
    
    def empty_examples_base(self):
        self.examples_base = []
        
    def add_example_to_base(self, example_with_result):
        example = example_with_result[0]
        result = example_with_result[1]
        self.examples_base.append([example, result])
    
    def get_examples(self):
        return self.examples_base
    
    def test_examples(self):        
        feedback = []
        for example, expected_result in self.examples_base:
            feedback.append(self._run_example(example, expected_result))
        return feedback
    
    def _run_example(self, example, expected_result):
        result = self.query(example)
        
        if result == expected_result:
            return(example, "Test passed", FeedbackEnum.SUCCESS)
        else:
            return(example, "Test failed", FeedbackEnum.ERROR)
            
    