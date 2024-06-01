from pyswip.core import *
from pyswip.prolog import Prolog
from utils.FeedbackEnum import FeedbackEnum
from utils.ListOfDictsComparer import ListOfDictsComparer

class PrologInterface():
    
    def __init__(self):
        self.prolog = Prolog()
        self.examples_base = []
        self.source_file = None
    
    def consult_knowledge_base(self):
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
                return self.__run_example_ordered_and_first_only(query, result, expected_result)
            case (1, 0):
                return self.__run_example_ordered(query, result, expected_result)
            case (0, 1):
                return self.__run_example_first_only(query, result, expected_result)
            case (0, 0):
                return self.__run_example_base(query, result, expected_result)
    
    def __run_example_ordered_and_first_only(self, query, result, expected_result):
        result_first_only = [result[0]]
        expected_result_first_only = [expected_result[0]]
        if ListOfDictsComparer.equals(result_first_only, expected_result_first_only):
            return(query, FeedbackEnum.SUCCESS, result, expected_result_first_only, "")
        else:
            explanation = "La primera respuesta devuelta no coincide con la esperada."
            
            return(query, FeedbackEnum.ERROR, result_first_only, expected_result_first_only, explanation),
    
    def __run_example_ordered(self, query, result, expected_result):
        if ListOfDictsComparer.equal_set(result, expected_result):
            return(query, FeedbackEnum.SUCCESS, result, expected_result, "")
        else:
            explanation = "Las respuestas devueltas no coinciden con las esperadas."
            
            if ListOfDictsComparer.includes(result, expected_result):
                explanation = "Las respuestas devueltas tienen la respuesta esperada, pero también devuelve respuestas adicionales."
            
            return(query, FeedbackEnum.ERROR, result, expected_result, explanation)
    
    def __run_example_first_only(self, query, result, expected_result):
        expected_result_first_only = [expected_result[0]]
        if ListOfDictsComparer.includes(result, expected_result_first_only):
            return(query, FeedbackEnum.SUCCESS, result, expected_result_first_only, "")
        else:
            explanation = "La respuesta esperada no se encuentra entre las devueltas."
            
            return(query, FeedbackEnum.ERROR, result, expected_result_first_only, explanation)
    
    def __run_example_base(self, query, result, expected_result):
        if ListOfDictsComparer.equals(result, expected_result):
            return(query, FeedbackEnum.SUCCESS, result, expected_result, "")
        else:
            explanation = "Las respuestas devueltas no coinciden con las esperadas."
            
            if ListOfDictsComparer.includes(result, expected_result):
                explanation = "Las respuestas devueltas tienen la respuesta esperada, pero también devuelve respuestas adicionales."
            
            if ListOfDictsComparer.equal_set(result, expected_result):
                explanation = "Las respuestas devueltas no están en el orden correcto."
            
            return(query, FeedbackEnum.ERROR, result, expected_result, explanation)