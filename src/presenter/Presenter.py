from abc import ABC
from utils.FeedbackEnum import FeedbackEnum
from utils.StringHandler import StringHandler

class AppPresenter(ABC):
    
    def bind_view(self, view):
        """
        Binds the given view to the presenter.

        Parameters:
            view (View): The view to be bound.

        Returns:
            None

        Sets the view attribute of the presenter to the given view. Also sets the tag colors for the test text in the view.
        The tag colors are specified using the FeedbackEnum values.
        """
        self.view = view 
        
        # The colors are specified as #rgb, #rrggbb or #rrrgggbbb
        self.view.set_test_text_tag_color( FeedbackEnum.NONE.value, "white" )
        self.view.set_test_text_tag_color( FeedbackEnum.ERROR.value, "#FF8686" )
        self.view.set_test_text_tag_color( FeedbackEnum.SUCCESS.value, "#99FF99" )
    
    def is_testing_mode(self):
        """
        Check if the presenter is in testing mode.
        """
        return self.mode == self.modes.Testing
    
    def is_manual_mode(self):
        """
        Check if the current mode is Manual Creating.
        """
        return self.mode == self.modes.Manual_Creating

    def is_showing_results_mode(self):
        """
        Check if the current mode is Showing Results.
        """
        return self.mode == self.modes.Showing_Results
    
    def add_batch_examples(self, examples, ordered, first_only):
        """
        Add batch examples to the model, and causes an update to the loaded examples text box of the binded view.
        
        Parameters:
            example (str): The example to add.
            ordered (bool): Flag indicating if the order of the results should not be preserved.
            first_only (bool): Flag indicating if only the first example should matter.

        Returns:
            None
        """
        if self.model.add_examples(examples, ordered, first_only)[0]:
            self._update_loaded_examples_text_box()
    
    def add_manual_example(self, example, expected_unformatted_results, ordered, first_only):
        """
        Add a manually entered example to the model, and causes an update to the loaded examples text box of the binded view.

        Parameters:
            example (str): The example to add.
            expected_unformatted_results (str): The expected results for the example.
            ordered (bool): Flag indicating if the order of the results should not be preserved.
            first_only (bool): Flag indicating if only the first example should matter.

        Returns:
            None: If the example is not formatted correctly or if the brackets are not balanced.

        Raises:
            Exception: If the expected results format is incorrect.

        Description:
            This function checks if the example and expected results are formatted correctly by checking if the brackets are balanced. If they are, the function proceeds to parse the expected result, looking if it is True or False. If it is neither, then it parses it by separating each result by newline, and each variable in each result by ampersand. The function then adds the result to the expected result list.
            
            After parsing the expected results, the function adds the example and expected result to the model. It then calls for an update to the loaded examples text box.
        """
        if StringHandler.check_brackets_are_balanced(example) and StringHandler.check_brackets_are_balanced(expected_unformatted_results):
            expected_result = []
            
            # Remove the new line at the end of the string and the extra empty spaces from the beginning and end of the string.

            expected_unformatted_results = expected_unformatted_results.strip('\n')
            expected_unformatted_results = expected_unformatted_results.strip()
            
            if expected_unformatted_results.lower() == "true":
                expected_result = [{}]
            elif expected_unformatted_results.lower() == "false":
                expected_result = []
            else:
                try:
                    expected_result = []
                    results = expected_unformatted_results.split('\n')
                    
                    for result in results:
                        result_to_add = {}
                        variables = result.split('&')
                        for variable in variables:
                            name, value = variable.split(':')
                            result_to_add[name.strip()] = StringHandler.unstringify(value)
                        expected_result.append(result_to_add)
                except Exception:
                    self.view.open_popup("Error", "Formato incorrecto de resultados esperados.")
                    return None
            
            self.model.add_manual_example(example[:-1], expected_result, ordered, first_only)
            self._update_loaded_examples_text_box()
        else:
            self.view.open_popup("Error", "Formato incorrecto. Paréntesis o llaves no balanceadas.")
    
    def save_examples(self, file_path):        
        """
        Save examples to a specified file path.

        Parameters:
            file_path (str): The path to the file where the examples will be saved.
        """
        self.model.submit_examples(file_path)

    def load_knowledge_base(self, file_path):
        """
        Load a knowledge base from a file.

        Parameters:
            file_path (str): The path to the file containing the knowledge base.
        """
        response = self.model.load_knowledge_base(file_path)
        
        # If the response is a tuple with a True value at index 0, then enable the mode buttons and insert the value
        if response[0]:
            self.view.enable_mode_buttons()
            self.view.insert_text_to_knowledge_base_text_box(response[1])
        else:
            self.open_popup("Error", response[1])
    
    def clean_examples(self):
        """
        Cleans the examples in the model and updates the loaded examples text box in the view.
        """
        self.model.clean_examples()
        self.view.clean_loaded_examples_text_box()
    
    def pop_examples(self):
        """
        This function pops examples from the model and updates the loaded examples text box in the view.
        """
        self.model.pop_examples()
        self._update_loaded_examples_text_box()
    
    def load_test_file(self, file_path):
        """
        Load a test file and update the test text box.

        Parameters:
            file_path (str): The path to the test file.
        """
        if not (self.is_testing_mode() or self.is_showing_results_mode()):
            self.model.clean_examples()
        self.model.load_examples(file_path)
        self._update_test_text_box()
        self.view.change_to_test_mode()
        self.mode = self.modes.Testing
    
    def enter_manual_create_mode(self):
        """
        Enter manual create mode by performing the following steps:
        1. Clean the examples in the model.
        2. Update the loaded examples text box in the view.
        3. Clean the test text box in the view.
        4. Change the view to manual create mode.
        5. Set the mode attribute to Manual_Creating.
        """
        self.model.clean_examples()
        self._update_loaded_examples_text_box()
        self.view.clean_test_text_box()
        self.view.change_to_manual_create_mode()
        self.mode = self.modes.Manual_Creating
    
    def open_popup(self, type, message):
        """
        Opens a popup with the specified type and message.
        
        Parameters:
        - type: The type of the popup.
        - message: The message to display in the popup.
        """
        self.view.open_popup(type, message)
    
    def run_examples(self):
        """
        Run the examples in the model and update the test text box with the results. Iterates over the results and calls the view to show the results to the user. Finally, it updates the view to show the number of correctly completed tests and the total number of tests.
        """
        results = self.model.run_examples()
        self.view.clean_test_text_box()
        test_number = 0
        completed = 0
        total = len(results)
        
        for [query, result_code, results, expected_results, explanation] in results:
            test_number += 1
            if result_code == FeedbackEnum.SUCCESS:
                completed += 1
            self.send_example_to_view(query, test_number, result_code, explanation, expected_results, results)
        
        self.mode = self.modes.Showing_Results
        
        self.view.set_completed_test_feedback(completed, total)
    
    def clean_tests(self):
        """
        Cleans the tests by cleaning the examples in the model and the test text box in the view.
        """
        self.model.clean_examples()
        self.view.clean_test_text_box()
    
    def send_example_to_view(self, query, test_number, result_code, explanation, expected_results, results):
        """
        Sends the example and its result to the view for display.

        This function takes in the query, test number, result code, explanation, expected results, and results
        as parameters and constructs a formatted text string to be displayed in the view. The text string
        includes information about the test number, query, and result code. If the result code is FeedbackEnum.SUCCESS,
        the text string indicates that the test passed. If the result code is FeedbackEnum.ERROR, the text string
        indicates that the test failed and includes the explanation, expected results, and actual results.

        Parameters:
            query (str): The query for the test.
            test_number (int): The number of the test.
            result_code (FeedbackEnum): The result code indicating the success or failure of the test.
            explanation (str): The explanation for the test failure.
            expected_results (list): The expected results for the test.
            results (list): The actual results for the test.
        """
        text = f"Test {test_number} - {query}\n"
        
        match result_code:
            case FeedbackEnum.SUCCESS:
                text = f"Test {test_number} - {query} - Test passed.\n"
            case FeedbackEnum.ERROR:
                text = f"Test {test_number} - {query} - Test failed.\n{explanation}\n\n>Se esperaba:\n"
                text += self._result_formatter(expected_results)
                text += "\n>Se obtuvo:\n"
                text += self._result_formatter(results)
        
        self.view.insert_example_to_test_text_box(text, result_code.value)
        self.view.insert_example_to_test_text_box("\n", FeedbackEnum.NONE)
    
    def _result_formatter(self, results):
        # Formats the results into a more readable string for the user.
        text = ""
        if results:
            if results == [{}]:
                text += ">>True\n"
            else:
                for result in results:
                    text += f">>{result}\n"
        else:
            text += ">>False\n"
        
        return text
    
    def show_message(self, type, message):
        """
        Displays a popup with the specified type and message.

        Parameters:
            type (str): The type of the popup.
            message (str): The message to display in the popup.
        """
        self.view.open_popup(type, message)
    
    def _update_test_text_box(self):
        self.view.clean_test_text_box()
         
        examples = self.model.get_loaded_examples()
               
        # Add the examples to the test text box but without ending with a new line.
        for example in examples[:-1]:
            self.view.insert_example_to_test_text_box(str(example[0]) + "\n")
        if examples[-1]:
            self.view.insert_example_to_test_text_box(str(examples[-1][0]))
    
    def _update_loaded_examples_text_box(self):
        self.view.clean_loaded_examples_text_box()
        for example in self.model.get_loaded_examples():
            self.view.insert_example_to_loaded_examples_text_box(str(example[0]) + "\n")
    
    def handle_test_text_box_click(self, line):
        """
        Updates the selected test line based on the input line.

        Parameters:
            line (int): The line number of the test text box clicked.
        """
        self.selected_test_line = line - 1
    
    def pop_test(self):
        """
        A function to delete the selected test if it is in testing mode and update the test text box. If it's showing the results of the tests, then it changes to testing mode and updates the test text box.
        """
        # Solo se borra el test seleccionado si se están mostrando los tests aún sin correr
        if self.mode == self.modes.Testing and self.selected_test_line is not None:
            self.model.pop_test(self.selected_test_line)
            self.selected_test_line = None
        elif self.mode == self.modes.Showing_Results:
            self.mode = self.modes.Testing
            
        self._update_test_text_box()