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
        """
        Consults the knowledge base using the Prolog consult method.
        """
        self.prolog.consult(self.knowledge_base)
    
    def set_knowledge_base(self, knowledge_base):
        """
        Set the knowledge base for the PrologInterface.

        Parameters:
            knowledge_base (str): The path to the knowledge base file.
        """
        self.knowledge_base = knowledge_base
    
    def query(self, query):
        """
        Executes a query in the Prolog knowledge base.

        Parameters:
            query (str): The Prolog query to execute.

        Returns:
            list: A list of the results of the query. [{}] represents a true and [] a false.
        """
        prolog_result = []
        try:
            results = self.prolog.query(query)
            if results == [] or results == [{}]:
                prolog_result = results
            else:
                for result in results:
                    prolog_result.append(StringHandler.replace_byte_strings(result))
        except Exception:
            return []
        return list(prolog_result)
    
    def create_example(self, example, ordered, first_only):
        """
        Creates an example in the examples base.

        Parameters:
            example (str): The example to be added to the examples base.
            ordered (bool): Flag indicating if the order of the results should not be preserved.
            first_only (bool): Flag indicating if only the first example should matter.

        Raises:
            PrologSyntaxException: If the syntax of the example is incorrect. The brackets are not balanced.

        This function checks if the example has balanced brackets. If it does, it executes the example query and appends the result to the examples base. If the brackets are not balanced, it clears the examples base and raises a PrologSyntaxException.
        """
        if StringHandler.check_brackets_are_balanced(example):
            result = self.query(example)
            self.examples_base.append([example, result, ordered, first_only])
        else:
            self.empty_examples_base()
            raise PrologSyntaxException("La sintaxis de los ejemplos no es correcta. Los paréntesis o llaves no están balanceados.")
    
    def empty_examples_base(self):
        """
        Clears the examples base by setting it to an empty list.
        """
        self.examples_base = []
    
    def pop_example_from_base(self, index = -1):
        """
        Removes an example from the examples base.

        Parameters:
            index (int, optional): The index of the example to be removed. Defaults to -1, which removes the last example.

        Returns:
            example(list): The removed example, result, order flag, and first-only flag.

        Raises:
            IndexError: If the index is out of range.
        """
        if self.examples_base:
            if index == -1:
                return self.examples_base.pop()
            else:
                return self.examples_base.pop(index)
    
    def add_example_to_base(self, example_with_result):
        """
        Adds an example with its result, order flag, and first-only flag to the examples base.

        Args:
            example_with_result (list): A list containing the example, result, order flag, and first-only flag.
        """
        example = example_with_result[0]
        result = example_with_result[1]
        ordered = example_with_result[2]
        first_only = example_with_result[3]
        self.examples_base.append([example, result, ordered, first_only])
    
    def get_examples(self):
        """
        Returns the examples base, which is a list of lists containing example strings, their results,
        order flags, and first-only flags.

        Returns: 
            A list of lists. Each inner list contains an example string, its result, an order flag,
            and a first-only flag.
        """
        return self.examples_base
    
    def test_examples(self):
        """
        Tests all examples in the examples base and returns a list of feedbacks.

        This function iterates over each example in the examples base and calls the private
        method `__run_example` to evaluate the example. The result of each evaluation is
        appended to the `feedback` list. Finally, the `feedback` list is returned.

        Returns:
            A list of feedbacks. Each feedback is a tuple containing the query, result code,
            actual results, expected results, and explanation (if any).
        """
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
        if ListOfDictsComparer.equals(result_first_only, expected_result_first_only, comparator=self.identical):
            return(query, FeedbackEnum.SUCCESS, result, expected_result_first_only, "")
        else:
            explanation = "La primera respuesta devuelta no coincide con la esperada."
            
            return(query, FeedbackEnum.ERROR, result_first_only, expected_result_first_only, explanation),
    
    def __run_example_ordered(self, query, result, expected_result):
        if ListOfDictsComparer.equal_set(result, expected_result, comparator=self.identical):
            return(query, FeedbackEnum.SUCCESS, result, expected_result, "")
        else:
            explanation = "Las respuestas devueltas no coinciden con las esperadas."
            
            if ListOfDictsComparer.includes(result, expected_result, comparator=self.identical):
                explanation = "Las respuestas devueltas tienen la respuesta esperada, pero también devuelve respuestas adicionales."
            
            return(query, FeedbackEnum.ERROR, result, expected_result, explanation)
    
    def __run_example_first_only(self, query, result, expected_result):
        expected_result_first_only = [expected_result[0]]
        if ListOfDictsComparer.includes(result, expected_result_first_only, comparator=self.identical):
            return(query, FeedbackEnum.SUCCESS, result, expected_result_first_only, "")
        else:
            explanation = "La respuesta esperada no se encuentra entre las devueltas."
            
            return(query, FeedbackEnum.ERROR, result, expected_result_first_only, explanation)
    
    def __run_example_base(self, query, result, expected_result):
        if ListOfDictsComparer.equals(result, expected_result, comparator=self.identical):
            return(query, FeedbackEnum.SUCCESS, result, expected_result, "")
        else:
            explanation = "Las respuestas devueltas no coinciden con las esperadas."
            
            if ListOfDictsComparer.includes(result, expected_result, comparator=self.identical):
                explanation = "Las respuestas devueltas tienen la respuesta esperada, pero también devuelve respuestas adicionales."
            
            if ListOfDictsComparer.equal_set(result, expected_result, comparator=self.identical):
                explanation = "Las respuestas devueltas no están en el orden correcto."
            
            return(query, FeedbackEnum.ERROR, result, expected_result, explanation)
    
    def identical(self, first, second):
        """
        Checks if two given terms are identical in the Prolog engine.

        Parameters:
            first (term): The first term to compare.
            second (term): The second term to compare.

        Returns:
            bool: True if the terms are identical, False otherwise.
        """
        query = str(first) + " = " + str(second)
        result = self.query(query)
        return result == [{}]