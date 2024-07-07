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
        self._upper_side_frame = TeacherHeaderFrame(root, bg="blue", width=800, height=50, pady=3, padx=10, functions=(self._load_knowledge_base, self._test_mode, self._batch_create_mode, self._manual_create_mode))
        self._middle_side_knowledge_base_frame = KnowledgeBaseFrame(root, bg="red", width=320, pady=3, padx=5)
        self._middle_side_testing_frame = TestingFrame(root, bg="pink", width=480, pady=3, padx=5)
        self._middle_side_batch_creating_frame = BatchCreatingFrame(root, bg="orange", width=480, pady=3, padx=5)
        self._middle_side_manual_creating_frame = ManualCreatingFrame(root, bg="yellow", width=480, pady=3, padx=5)
        self._middle_side_loaded_examples_frame = LoadedExamplesFrame(root, bg="purple", width=480, pady=3, padx=5)
        self._lower_side_testing_frame = FooterTestingFrame(root, bg="green", width=800, height=50, pady=3, functions=(self._test_solution, self._clean_tests, self._pop_test))
        self._lower_side_batch_creating_frame = FooterCreatingFrame(root, bg="cyan", width=800, height=50, pady=3, variables=(self._ordered, self._first_only), functions=(self._add_example, self._save_examples, self._clean_examples, self._pop_examples))
        
        # Ubico los frames
        
        self._upper_side_frame.grid(row = 0, stick="ew", columnspan = 2)
        self._middle_side_knowledge_base_frame.grid(row = 1, column = 0, rowspan = 2, sticky="nsew")
        self._middle_side_testing_frame.grid(row = 1, column = 1, rowspan = 2, sticky="nsew")
        
        # Configuro widgets del frame intermedio
        
        self._middle_side_testing_frame.test_text_box.bind("<Button 1>", self._handle_test_text_box_click)
    
    def _add_example(self):
        if self.presenter.is_batch_mode():
            if not self._middle_side_batch_creating_frame.batch_create_text_box.compare("end-1c", "==", "1.0"): 
                self.presenter.add_batch_examples(self._middle_side_batch_creating_frame.batch_create_text_box.get("1.0",'end'), self._ordered.get(), self._first_only.get())
        else:
            if self.presenter.is_manual_mode():
                if not self._middle_side_manual_creating_frame.manual_create_query_text_box.compare("end-1c", "==", "1.0") and not self._middle_side_manual_creating_frame.manual_create_expected_result_text_box.compare("end-1c", "==", "1.0"): 
                    self.presenter.add_manual_example(self._middle_side_manual_creating_frame.manual_create_query_text_box.get("1.0",'end'), self._middle_side_manual_creating_frame.manual_create_expected_result_text_box.get("1.0",'end'), self._ordered.get(), self._first_only.get())
    
    def change_to_test_mode(self):
        self._upper_side_frame.batch_creating_mode_button.config(state = "normal")
        self._upper_side_frame.manual_creating_mode_button.config(state = "normal")
        self._upper_side_frame.testing_mode_button.config(text = "Agregar Ejemplos")
        self._hide_batch_create_mode_widgets()
        self._hide_manual_create_mode_widgets()
        self._show_test_mode_widgets()
    
    def change_to_batch_create_mode(self):
        self._upper_side_frame.batch_creating_mode_button.config(state = "disabled")
        self._upper_side_frame.manual_creating_mode_button.config(state = "normal")
        self._upper_side_frame.testing_mode_button.config(text = "Modo de Prueba")
        self._hide_test_mode_widgets()
        self._hide_manual_create_mode_widgets()
        self._show_batch_create_mode_widgets()
    
    def change_to_manual_create_mode(self):
        if self.presenter.is_batch_mode():
            self._upper_side_frame.batch_creating_mode_button.config(state = "normal")
        self._upper_side_frame.manual_creating_mode_button.config(state = "disabled")
        self._upper_side_frame.testing_mode_button.config(text = "Modo de Prueba")
        self._hide_test_mode_widgets()
        self._hide_batch_create_mode_widgets()
        self._show_manual_create_mode_widgets()
    
    def enable_mode_buttons(self):
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
        self._middle_side_batch_creating_frame.clean_batch_create_text_box()
