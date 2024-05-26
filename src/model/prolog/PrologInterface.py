from pyswip.core import *
from pyswip.prolog import Prolog
from utils.FeedbackEnum import FeedbackEnum
from utils.ListOfDictsComparer import ListOfDictsComparer

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
    
    def create_example(self, example, ordered, first_only):
        result = self.query(example)
        self.examples_base.append([example, result, ordered, first_only])
    
    def empty_examples_base(self):
        self.examples_base = []
        
    def add_example_to_base(self, example_with_result):
        example = example_with_result[0]
        result = example_with_result[1]
        ordered = example_with_result[2]
        first_only = example_with_result[3]
        self.examples_base.append([example, result, ordered, first_only])
    
    def get_examples(self):
        return self.examples_base
    
    def test_examples(self):        
        feedback = []
        for query, expected_result, ordered, first_only in self.examples_base:
            feedback.append(self._run_example(query, expected_result, ordered, first_only))
        return feedback
    
    def _run_example(self, query, expected_result, is_ordered, is_first_only):
        result = self.query(query)
        
        match (is_ordered, is_first_only):
            case (1, 1):
                result = [result[0]]
                expected_result = [expected_result[0]]
                if ListOfDictsComparer.equals(result, expected_result):
                    return(query, "Test passed", FeedbackEnum.SUCCESS)
                else:
                    return(query, "Test failed", FeedbackEnum.ERROR)
                
            case (1, 0):
                if ListOfDictsComparer.equals(result, expected_result):
                    return(query, "Test passed", FeedbackEnum.SUCCESS)
                else:
                    return(query, "Test failed", FeedbackEnum.ERROR)
                
            case (0, 1):
                expected_result = [expected_result[0]]
                if ListOfDictsComparer.includes(result, expected_result):
                    return(query, "Test passed", FeedbackEnum.SUCCESS)
                else:
                    return(query, "Test failed", FeedbackEnum.ERROR)
                
            case (0, 0):
                if ListOfDictsComparer.equal_set(result, expected_result):
                    return(query, "Test passed", FeedbackEnum.SUCCESS)
                else:
                    return(query, "Test failed", FeedbackEnum.ERROR)
            
    