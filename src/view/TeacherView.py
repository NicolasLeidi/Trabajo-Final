from tkinter import IntVar
from view.View import View
from view.components.frames.BatchCreatingFrame import BatchCreatingFrame
from view.components.frames.FooterCreatingFrame import FooterCreatingFrame
from view.components.frames.FooterTestingFrame import FooterTestingFrame
from view.components.frames.KnowledgeBaseFrame import KnowledgeBaseFrame
from view.components.frames.LoadedExamplesFrame import LoadedExamplesFrame
from view.components.frames.ManualCreatingFrame import ManualCreatingFrame
from view.components.frames.TeacherHeaderFrame import TeacherHeaderFrame
from view.components.frames.TestingFrame import TestingFrame

class TeacherView(View):
    
    def __init__(self, root, presenter):
        self.presenter = presenter
        self._ordered = IntVar()
        self._first_only = IntVar()
        self._base_window_dimension(root)
        self.__create_widgets(root)
    
    def __create_widgets(self, root):
        self._upper_side_frame = TeacherHeaderFrame(root, width=800, height=50, pady=3, padx=10, functions=(self._load_knowledge_base, self._test_mode, self._batch_create_mode, self._manual_create_mode))
        self._middle_side_knowledge_base_frame = KnowledgeBaseFrame(root, width=320, pady=3, padx=5)
        self._middle_side_testing_frame = TestingFrame(root, width=480, pady=3, padx=5, functions=(self._handle_test_text_box_click))
        self._middle_side_batch_creating_frame = BatchCreatingFrame(root, width=480, pady=3, padx=5)
        self._middle_side_manual_creating_frame = ManualCreatingFrame(root, width=480, pady=3, padx=5)
        self._middle_side_loaded_examples_frame = LoadedExamplesFrame(root, width=480, pady=3, padx=5)
        self._lower_side_testing_frame = FooterTestingFrame(root, width=800, height=50, pady=3, functions=(self._test_solution, self._clean_tests, self._pop_test))
        self._lower_side_batch_creating_frame = FooterCreatingFrame(root, width=800, height=50, pady=3, variables=(self._ordered, self._first_only), functions=(self._add_example, self._save_examples, self._clean_examples, self._pop_examples))
        
        # Place the frames in their respective places
        
        self._upper_side_frame.grid(row = 0, stick="ew", columnspan = 2)
        self._middle_side_knowledge_base_frame.grid(row = 1, column = 0, rowspan = 2, sticky="nsew")
        self._middle_side_testing_frame.grid(row = 1, column = 1, rowspan = 2, sticky="nsew")
    
    def _add_example(self):
        # If the user is creating a batch of tests, it calls the corresponding method of the presenter instead
        if self.presenter.is_batch_mode():
            if not self._middle_side_batch_creating_frame.batch_create_text_box.compare("end-1c", "==", "1.0"): 
                self.presenter.add_batch_examples(self._middle_side_batch_creating_frame.batch_create_text_box.get("1.0",'end'), self._ordered.get(), self._first_only.get())
        else:
            if self.presenter.is_manual_mode():
                if not self._middle_side_manual_creating_frame.manual_create_query_text_box.compare("end-1c", "==", "1.0") and not self._middle_side_manual_creating_frame.manual_create_expected_result_text_box.compare("end-1c", "==", "1.0"): 
                    self.presenter.add_manual_example(self._middle_side_manual_creating_frame.manual_create_query_text_box.get("1.0",'end'), self._middle_side_manual_creating_frame.manual_create_expected_result_text_box.get("1.0",'end'), self._ordered.get(), self._first_only.get())
    
    def change_to_test_mode(self):
        """
        Changes the view to test mode.

        This function sets the state of the batch creating mode button to "normal" and the manual creating mode button to "normal". It also updates the text of the testing mode button to "Agregar Ejemplos". It then hides the batch create mode widgets and manual create mode widgets, and shows the test mode widgets.
        """
        self._upper_side_frame.batch_creating_mode_button.config(state = "normal")
        self._upper_side_frame.manual_creating_mode_button.config(state = "normal")
        self._upper_side_frame.testing_mode_button.config(text = "Agregar Ejemplos")
        self._hide_batch_create_mode_widgets()
        self._hide_manual_create_mode_widgets()
        self._show_test_mode_widgets()
    
    def change_to_batch_create_mode(self):
        """
        Changes the view to batch create mode by disabling the batch creating mode button, enabling the manual creating mode button, updating the text of the testing mode button to "Modo de Prueba", hiding the test mode widgets, and showing the batch create mode widgets.
        """
        self._upper_side_frame.batch_creating_mode_button.config(state = "disabled")
        self._upper_side_frame.manual_creating_mode_button.config(state = "normal")
        self._upper_side_frame.testing_mode_button.config(text = "Modo de Prueba")
        self._hide_test_mode_widgets()
        self._hide_manual_create_mode_widgets()
        self._show_batch_create_mode_widgets()
    
    def change_to_manual_create_mode(self):
        """
        Changes the view to manual create mode if not in batch mode.
        Disables the manual creating mode button, updates the text of the testing mode button to "Modo de Prueba",
        hides the test mode widgets, and shows the manual create mode widgets.
        """
        if self.presenter.is_batch_mode():
            self._upper_side_frame.batch_creating_mode_button.config(state = "normal")
        self._upper_side_frame.manual_creating_mode_button.config(state = "disabled")
        self._upper_side_frame.testing_mode_button.config(text = "Modo de Prueba")
        self._hide_test_mode_widgets()
        self._hide_batch_create_mode_widgets()
        self._show_manual_create_mode_widgets()
    
    def enable_mode_buttons(self):
        """
        Enables the mode buttons by setting the state of the testing mode button to "normal", the batch creating mode button to "normal", and the submit knowledge base button to "disabled".
        """
        self._upper_side_frame.testing_mode_button.config(state = "normal")
        self._upper_side_frame.batch_creating_mode_button.config(state = "normal")
        self._upper_side_frame.submit_knowledge_base_button.config(state = "disabled")
    
    def _hide_batch_create_mode_widgets(self):
        self._middle_side_batch_creating_frame.grid_forget()
        self._middle_side_loaded_examples_frame.grid_forget()
        self._lower_side_batch_creating_frame.grid_forget()
    
    def _show_batch_create_mode_widgets(self):
        self._middle_side_batch_creating_frame.grid(row = 1, column = 1, sticky="nsew")
        self._middle_side_loaded_examples_frame.grid(row = 2, column = 1, sticky="nsew")
        self._lower_side_batch_creating_frame.grid(row = 3, sticky="ew", columnspan = 2)
    
    def clean_create_text_box(self):
        """
        Clean the create text box in the middle side batch creating frame.
        """
        self._middle_side_batch_creating_frame.clean_batch_create_text_box()
