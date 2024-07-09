from pyswip.core import *
from pyswip.prolog import Prolog
from model.exception.PrologSyntaxException import PrologSyntaxException
from utils.FeedbackEnum import FeedbackEnum
from utils.ListOfDictsComparer import ListOfDictsComparer
from utils.StringHandler import StringHandler

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
        try:
            prolog_result = self.prolog.query(query)
        except Exception:
            return []
        return list(prolog_result)
    
    def create_example(self, example, ordered, first_only):
        if StringHandler.check_brackets_are_balanced(example):
            result = self.query(example)
            self.examples_base.append([example, result, ordered, first_only])
        else:
            self.empty_examples_base()
            raise PrologSyntaxException("La sintaxis de los ejemplos no es correcta. Los paréntesis o llaves no están balanceados.")
    
    def empty_examples_base(self):
        self.examples_base = []
    
    def pop_example_from_base(self, index = -1):
        # Si no se recibe un index, se elimina el último elemento de la batería
        if self.examples_base:
            if index == -1:
                return self.examples_base.pop()
            else:
                return self.examples_base.pop(index)
    
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
            feedback.append(self.__run_example(query, expected_result, ordered, first_only))
        return feedback
    
    def __run_example(self, query, expected_result, is_ordered, is_first_only):
        result = self.query(query)
        
        if not expected_result:
            return self.__run_example_negative_case(query, result)
        else:
            match (is_ordered, is_first_only):
                case (1, 1):
                    return self.__run_example_ordered_and_first_only(query, result, expected_result)
                case (1, 0):
                    return self.__run_example_ordered(query, result, expected_result)
                case (0, 1):
                    return self.__run_example_first_only(query, result, expected_result)
                case (0, 0):
                    return self.__run_example_base(query, result, expected_result)
    
    def __run_example_negative_case(self, query, result):
        if not result:
            return(query, FeedbackEnum.SUCCESS, result, [], "")
        else:
            explanation = "El predicado unifica cuando no lo debería hacer."
            
            return(query, FeedbackEnum.ERROR, result, [], explanation)
    
    def __run_example_ordered_and_first_only(self, query, result, expected_result):
        result_first_only = [result[0]]
        expected_result_first_only = [expected_result[0]]
        if ListOfDictsComparer.equals(result_first_only, expected_result_first_only, comparator=self.unification):
            return(query, FeedbackEnum.SUCCESS, result, expected_result_first_only, "")
        else:
            explanation = "La primera respuesta devuelta no coincide con la esperada."
            
            return(query, FeedbackEnum.ERROR, result_first_only, expected_result_first_only, explanation),
    
    def __run_example_ordered(self, query, result, expected_result):
        if ListOfDictsComparer.equal_set(result, expected_result, comparator=self.unification):
            return(query, FeedbackEnum.SUCCESS, result, expected_result, "")
        else:
            explanation = "Las respuestas devueltas no coinciden con las esperadas."
            
            if ListOfDictsComparer.includes(result, expected_result, comparator=self.unification):
                explanation = "Las respuestas devueltas tienen la respuesta esperada, pero también devuelve respuestas adicionales."
            
            return(query, FeedbackEnum.ERROR, result, expected_result, explanation)
    
    def __run_example_first_only(self, query, result, expected_result):
        expected_result_first_only = [expected_result[0]]
        if ListOfDictsComparer.includes(result, expected_result_first_only, comparator=self.unification):
            return(query, FeedbackEnum.SUCCESS, result, expected_result_first_only, "")
        else:
            explanation = "La respuesta esperada no se encuentra entre las devueltas."
            
            return(query, FeedbackEnum.ERROR, result, expected_result_first_only, explanation)
    
    def __run_example_base(self, query, result, expected_result):
        if ListOfDictsComparer.equals(result, expected_result, comparator=self.unification):
            return(query, FeedbackEnum.SUCCESS, result, expected_result, "")
        else:
            explanation = "Las respuestas devueltas no coinciden con las esperadas."
            
            if ListOfDictsComparer.includes(result, expected_result, comparator=self.unification):
                explanation = "Las respuestas devueltas tienen la respuesta esperada, pero también devuelve respuestas adicionales."
            
            if ListOfDictsComparer.equal_set(result, expected_result, comparator=self.unification):
                explanation = "Las respuestas devueltas no están en el orden correcto."
            
            return(query, FeedbackEnum.ERROR, result, expected_result, explanation)
    
    def unification(self, first, second):
        query = str(first) + " = " + str(second)
        result = self.query(query)
        return result == [{}]