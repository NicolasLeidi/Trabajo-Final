from enum import Enum
from presenter.Presenter import AppPresenter

class StudentPresenter(AppPresenter):

    def __init__(self, model):
        self.model = model
        self.modes = Enum('Mode', ['Testing', 'Showing_Results', 'Manual_Creating', 'Not_Selected'])
        self.mode = self.modes.Not_Selected
        self.selected_test_line = None
        self.knowledge_base_submitted = False
    
    