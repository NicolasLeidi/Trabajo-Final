from enum import Enum
from utils.FeedbackEnum import FeedbackEnum

class AppPresenter():
    
    def __init__(self, model):
        self.model = model
        self.modes = Enum('Mode', ['Testing', 'Creating', 'NotSelected'])
        self.mode = self.modes.NotSelected

    def bind_view(self, view):
        self.view = view 
    
    def examples(self, file_path, examples):
        if not file_path:
            return
        
        self.model.submit_examples(examples, file_path)

    def load_knowledge_base(self, file_path):
        response = self.model.load_knowledge_base(file_path)
        
        if (not response[0]):
            self.open_popup("Error", response[1])

    def test_examples(self, file_path):
        return (self.model.test_examples(file_path))
    
    def enter_test_mode(self, file_path):      
        self.view.clean_feedback()
         
        response = self.model.load_examples(file_path)
        
        self.mode = self.modes.Testing
               
        for [query, description] in response:
            self.view.insert_example_to_list(query, description)
    
    def enter_create_mode(self):
        self.mode = self.modes.Creating
    
    def open_popup(self, type, message):
        self.view.open_popup(type, message)
    
    def run_examples(self):
        results = self.model.run_examples()
        self.view.clean_feedback()
        for [query, description, result] in results:
            self.view.insert_example_to_list(query, description, result)