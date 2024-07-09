from enum import Enum
from presenter.Presenter import AppPresenter

class TeacherPresenter(AppPresenter):
    
    def __init__(self, model):
        self.model = model
        self.modes = Enum('Mode', ['Testing', 'Showing_Results', 'Batch_Creating', 'Manual_Creating', 'Not_Selected'])
        self.mode = self.modes.Not_Selected
        self.selected_test_line = None
    
    def is_batch_mode(self):
        """
        Check if the current mode is Batch Creating.
        """
        return self.mode == self.modes.Batch_Creating
    
    def enter_batch_create_mode(self):
        """
        A function to enter the batch create mode that handles the necessary tasks for entering the batch create mode.
        """
        self.model.clean_examples()
        self._update_loaded_examples_text_box()
        self.view.clean_test_text_box()
        self.view.change_to_batch_create_mode()
        self.mode = self.modes.Batch_Creating