from abc import ABC
from utils.FeedbackEnum import FeedbackEnum
from utils.StringHandler import StringHandler

class AppPresenter(ABC):
    
    def bind_view(self, view):
        self.view = view 
        
        # Los colores de tkinter se pueden poner en #rgb, #rrggbb o #rrrgggbbb
        self.view.set_test_text_tag_color( FeedbackEnum.NONE.value, "white" )
        self.view.set_test_text_tag_color( FeedbackEnum.ERROR.value, "#FF8686" )
        self.view.set_test_text_tag_color( FeedbackEnum.SUCCESS.value, "#99FF99" )
    
    def is_testing_mode(self):
        return self.mode == self.modes.Testing
    
    def is_manual_mode(self):
        return self.mode == self.modes.Manual_Creating

    def is_showing_results_mode(self):
        return self.mode == self.modes.Showing_Results
    
    def add_batch_examples(self, examples, ordered, first_only):
        if self.model.add_examples(examples, ordered, first_only)[0]:
            self._update_loaded_examples_text_box()
    
    def add_manual_example(self, example, expected_unformatted_results, ordered, first_only):
        if StringHandler.check_brackets_are_balanced(example) and StringHandler.check_brackets_are_balanced(expected_unformatted_results):
            expected_result = []
            
            # Remuevo el salto de línea y espacios del final
            
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
                    
                    # La última va a ser siempre una lista vacía que hay que ignorar
                    
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
        self.model.submit_examples(file_path)

    def load_knowledge_base(self, file_path):
        response = self.model.load_knowledge_base(file_path)
        
        # Si la respuesta es True, se habilitan los botones de modo. Si no, se muestra el error.
        if response[0]:
            self.view.enable_mode_buttons()
            self.view.insert_text_to_knowledge_base_text_box(response[1])
        else:
            self.open_popup("Error", response[1])
    
    def clean_examples(self):
        self.model.clean_examples()
        self.view.clean_loaded_examples_text_box()
    
    def pop_examples(self):
        self.model.pop_examples()
        self._update_loaded_examples_text_box()
    
    def load_test_file(self, file_path):
        # Si no se encuentra ya mostrando ejemplos, entonces limpia los ejemplos cargados por el usuario
        if not (self.is_testing_mode() or self.is_showing_results_mode()):
            self.model.clean_examples()
        self.model.load_examples(file_path)
        self._update_test_text_box()
        self.view.change_to_test_mode()
        self.mode = self.modes.Testing
    
    def enter_manual_create_mode(self):
        self.model.clean_examples()
        self._update_loaded_examples_text_box()
        self.view.clean_test_text_box()
        self.view.change_to_manual_create_mode()
        self.mode = self.modes.Manual_Creating
    
    def open_popup(self, type, message):
        self.view.open_popup(type, message)
    
    def run_examples(self):
        results = self.model.run_examples()
        self.view.clean_test_text_box()
        test_number = 0
        completed = 0
        total = 0
        
        for [query, result_code, results, expected_results, explanation] in results:
            test_number += 1
            if result_code == FeedbackEnum.SUCCESS:
                completed += 1
            total += 1
            self.send_example_to_view(query, test_number, result_code, explanation, expected_results, results)
        
        self.mode = self.modes.Showing_Results
        
        self.view.set_completed_test_feedback(completed, total)
    
    def clean_tests(self):
        self.model.clean_examples()
        self.view.clean_test_text_box()
    
    def send_example_to_view(self, query, test_number, result_code, explanation, expected_results, results):
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
        self.view.open_popup(type, message)
    
    def _update_test_text_box(self):
        self.view.clean_test_text_box()
         
        examples = self.model.get_loaded_examples()
               
        # Para no agregar la ultima linea vacia
        for example in examples[:-1]:
            self.view.insert_example_to_test_text_box(str(example[0]) + "\n")
        if examples[-1]:
            self.view.insert_example_to_test_text_box(str(examples[-1][0]))
    
    def _update_loaded_examples_text_box(self):
        self.view.clean_loaded_examples_text_box()
        for example in self.model.get_loaded_examples():
            self.view.insert_example_to_loaded_examples_text_box(str(example[0]) + "\n")
    
    def handle_test_text_box_click(self, line):
        self.selected_test_line = line - 1
    
    def pop_test(self):
        if self.mode == self.modes.Testing and self.selected_test_line is not None:
            self.model.pop_test(self.selected_test_line)
            self.selected_test_line = None
        elif self.mode == self.modes.Showing_Results:
            self.mode = self.modes.Testing
            
        self._update_test_text_box()