from enum import Enum
from utils.FeedbackEnum import FeedbackEnum

class AppPresenter():
    
    def __init__(self, model):
        self.model = model
        self.modes = Enum('Mode', ['Testing', 'Creating', 'NotSelected'])
        self.mode = self.modes.NotSelected

    def bind_view(self, view):
        self.view = view 
    
    def examples(self, file_path, examples, ordered, first_only):        
        self.model.submit_examples(examples, file_path, ordered, first_only)

    def load_knowledge_base(self, file_path):
        response = self.model.load_knowledge_base(file_path)
        
        if response[0]:
            self.view.enable_mode_buttons()
        else:
            self.open_popup("Error", response[1])

    def test_examples(self, file_path):
        return (self.model.test_examples(file_path))
    
    def enter_test_mode(self, file_path):      
        self.view.clean_main_text_box()
         
        response = self.model.load_examples(file_path)
        
        self.mode = self.modes.Testing
               
        for example in response:
            self.view.insert_example_to_main_text_box(example[0])
            
        self.view.change_to_test_mode()
    
    def enter_create_mode(self):
        self.mode = self.modes.Creating
        
        self.view.clean_main_text_box()
        self.view.change_to_create_mode()
    
    def open_popup(self, type, message):
        self.view.open_popup(type, message)
    
    def run_examples(self):
        results = self.model.run_examples()
        self.view.clean_main_text_box()
        for [query, result_code, result, expected_result, explanation] in results:
            self.view.insert_example_to_main_text_box(query, result_code, explanation, expected_result, result)