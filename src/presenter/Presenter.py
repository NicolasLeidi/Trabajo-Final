from enum import Enum
from utils.FeedbackEnum import FeedbackEnum

class AppPresenter():
    
    def __init__(self, model):
        self.model = model
        self.modes = Enum('Mode', ['Testing', 'Creating', 'NotSelected'])
        self.mode = self.modes.NotSelected

    def bind_view(self, view):
        self.view = view 
        
        # Los colores de tkinter se pueden poner en #rgb, #rrggbb o #rrrgggbbb
        self.view.set_test_text_tag_color( FeedbackEnum.NONE.value, "white" )
        self.view.set_test_text_tag_color( FeedbackEnum.ERROR.value, "#FF8686" )
        self.view.set_test_text_tag_color( FeedbackEnum.SUCCESS.value, "#99FF99" )
    
    def add_examples(self, examples, ordered, first_only):
        if self.model.add_examples(examples, ordered, first_only)[0]:
            self.view.clean_test_text_box()
            self.__update_loaded_examples_text_box()
    
    def save_examples(self, file_path):        
        self.model.submit_examples(file_path)

    def load_knowledge_base(self, file_path):
        response = self.model.load_knowledge_base(file_path)
        
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
        self.__update_loaded_examples_text_box()
    
    def enter_test_mode(self, file_path):      
        self.view.clean_test_text_box()
         
        response = self.model.load_examples(file_path)
        
        self.mode = self.modes.Testing
               
        for example in response:
            self.view.insert_example_to_test_text_box(str(example[0]) + "\n")
            
        self.view.change_to_test_mode()
    
    def enter_create_mode(self):
        self.mode = self.modes.Creating
        self.model.clean_examples()
        
        self.view.clean_test_text_box()
        self.view.change_to_create_mode()
    
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
        
        self.view.set_completed_test_feedback(completed, total)
    
    def send_example_to_view(self, query, test_number, result_code, explanation, expected_results, results):
        text = f"Test {test_number} - {query}\n"
        
        match result_code:
            case FeedbackEnum.SUCCESS:
                text = f"Test {test_number} - {query} - Test passed.\n"
            case FeedbackEnum.ERROR:
                text = f"Test {test_number} - {query} - Test failed.\n{explanation}\n\n>Se esperaba:\n"
                text += self.__result_formatter(expected_results)
                text += "\n>Se obtuvo:\n"
                text += self.__result_formatter(results)
        
        self.view.insert_example_to_test_text_box(text, result_code.value)
    
    def __result_formatter(self, results):
        text = ""
        if results:
            if results == [{}]:
                text += ">>true\n"
            else:
                for result in results:
                    text += f">>{result}\n"
        else:
            text += ">>false\n"
        
        return text
    
    def show_message(self, type, message):
        self.view.open_popup(type, message)
    
    def __update_loaded_examples_text_box(self):
        self.view.clean_loaded_examples_text_box()
        for example in self.model.get_loaded_examples():
            self.view.insert_example_to_loaded_examples_text_box(str(example[0]) + "\n")