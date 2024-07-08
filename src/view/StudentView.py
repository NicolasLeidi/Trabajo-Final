from tkinter import IntVar
from view.View import View
from view.components.frames.FooterCreatingFrame import FooterCreatingFrame
from view.components.frames.FooterTestingFrame import FooterTestingFrame
from view.components.frames.HeaderFrame import HeaderFrame
from view.components.frames.KnowledgeBaseFrame import KnowledgeBaseFrame
from view.components.frames.LoadedExamplesFrame import LoadedExamplesFrame
from view.components.frames.ManualCreatingFrame import ManualCreatingFrame
from view.components.frames.TestingFrame import TestingFrame

class StudentView(View):

    def __init__(self, root, presenter):
        self.presenter = presenter
        self._ordered = IntVar()
        self._first_only = IntVar()
        self._base_window_dimension(root)
        self.__create_widgets(root)
    
    def __create_widgets(self, root):
        self._upper_side_frame = HeaderFrame(root, bg="blue", width=800, height=50, pady=3, padx=10, functions=(self._load_knowledge_base, self._test_mode, self._manual_create_mode))
        self._middle_side_knowledge_base_frame = KnowledgeBaseFrame(root, bg="red", width=320, pady=3, padx=5)
        self._middle_side_testing_frame = TestingFrame(root, bg="pink", width=480, pady=3, padx=5, functions=(self._handle_test_text_box_click))
        self._middle_side_manual_creating_frame = ManualCreatingFrame(root, bg="yellow", width=480, pady=3, padx=5)
        self._middle_side_loaded_examples_frame = LoadedExamplesFrame(root, bg="purple", width=480, pady=3, padx=5)
        self._lower_side_testing_frame = FooterTestingFrame(root, bg="green", width=800, height=50, pady=3, functions=(self._test_solution, self._clean_tests, self._pop_test))
        self._lower_side_batch_creating_frame = FooterCreatingFrame(root, bg="cyan", width=800, height=50, pady=3, variables=(self._ordered, self._first_only), functions=(self._add_example, self._save_examples, self._clean_examples, self._pop_examples))
        
        # Ubico los frames
        
        self._upper_side_frame.grid(row = 0, stick="ew", columnspan = 2)
        self._middle_side_knowledge_base_frame.grid(row = 1, column = 0, rowspan = 2, sticky="nsew")
        self._middle_side_testing_frame.grid(row = 1, column = 1, rowspan = 2, sticky="nsew")
    
    def _add_example(self):
        if not self._middle_side_manual_creating_frame.manual_create_query_text_box.compare("end-1c", "==", "1.0") and not self._middle_side_manual_creating_frame.manual_create_expected_result_text_box.compare("end-1c", "==", "1.0"): 
            self.presenter.add_manual_example(self._middle_side_manual_creating_frame.manual_create_query_text_box.get("1.0",'end'), self._middle_side_manual_creating_frame.manual_create_expected_result_text_box.get("1.0",'end'), self._ordered.get(), self._first_only.get())
