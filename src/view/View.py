from tkinter import filedialog
from tkinter import * 
from view.components.frames.BatchCreatingFrame import BatchCreatingFrame
from view.components.frames.FooterCreatingFrame import FooterCreatingFrame
from view.components.frames.FooterTestingFrame import FooterTestingFrame
from view.components.frames.HeaderFrame import HeaderFrame
from view.components.frames.KnowledgeBaseFrame import KnowledgeBaseFrame
from view.components.frames.LoadedExamplesFrame import LoadedExamplesFrame
from view.components.frames.ManualCreatingFrame import ManualCreatingFrame
from view.components.frames.TestingFrame import TestingFrame
from abc import ABC, abstractmethod

class View(ABC):

    def _base_window_dimension(self, root):
        root.title("Nombre a colocar")
        root.geometry('{}x{}'.format(800, 600))
        root.grid_rowconfigure(1, weight=1)
        root.grid_rowconfigure(2, weight=1)
        root.grid_columnconfigure(0, weight=1)
        root.grid_columnconfigure(1, weight=2)

    def _handle_test_text_box_click(self, event):
        self.presenter.handle_test_text_box_click(self._middle_side_testing_frame.test_text_box, event)
    
    def _test_solution(self):
        self.presenter.run_examples()
    
    def _clean_tests(self):
        self.presenter.clean_tests()
    
    def _pop_test(self):
        self.presenter.pop_test()
    
    @abstractmethod
    def _add_example(self):
        pass
    
    def _save_examples(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        
        if not file_path:
            return
        
        self.presenter.save_examples(file_path)
    
    def _clean_examples(self):
        self.presenter.clean_examples()
    
    def _pop_examples(self):
        self.presenter.pop_examples()
    
    def _load_knowledge_base(self):
        file_path = filedialog.askopenfilename(filetypes=[("Archivo PROLOG", "*.pl")])
        
        if not file_path:
            return
        
        self.presenter.load_knowledge_base(file_path)
        
    def _test_mode(self):
        # Para entrar al modo de testeo, primero se debe cargar una batería de tests válida
        file_path = filedialog.askopenfilename(filetypes=[("Batería de test", "*.json")], multiple = True)
        
        if not file_path:
            return
        
        self.presenter.enter_test_mode(file_path)
    
    def _batch_create_mode(self):
        self.presenter.enter_batch_create_mode()
    
    def _manual_create_mode(self):
        self.presenter.enter_manual_create_mode()
    
    def _show_test_mode_widgets(self):
        self._middle_side_testing_frame.grid(row = 1, column = 1, rowspan = 2, sticky="nsew")
        self._lower_side_testing_frame.grid(row = 3, sticky="ew", columnspan = 5)
    
    def _hide_test_mode_widgets(self):
        self._middle_side_testing_frame.grid_forget()
        self._lower_side_testing_frame.grid_forget()
    
    def _hide_manual_create_mode_widgets(self):
        self._middle_side_manual_creating_frame.grid_forget()
        self._middle_side_loaded_examples_frame.grid_forget()
        self._lower_side_batch_creating_frame.grid_forget()
    
    def _show_manual_create_mode_widgets(self):
        self._middle_side_manual_creating_frame.grid(row = 1, column = 1, sticky="nsew")
        self._middle_side_loaded_examples_frame.grid(row = 2, column = 1, sticky="nsew")
        self._lower_side_batch_creating_frame.grid(row = 3, sticky="ew", columnspan = 2)
    
    def open_popup(self, type, message):
        popup = Tk()
        popup.wm_title(type)
        label = Label(popup, text=message)
        label.pack(side="top", fill="x", pady=10)
        ok_button = Button(popup, text="Ok", command=popup.destroy)
        ok_button.pack()
    
    def insert_example_to_test_text_box(self, text, tag = 0):
        line_number = self._middle_side_testing_frame.test_text_box.index('end-1c').split('.')[0]
        line_number_to_str = str(line_number) + ".0"

        self._middle_side_testing_frame.insert_test_text_box(text)
                
        # Coloreo una cantidad de lineas igual a la cantidad de lineas que ocupó la respuesta
        
        self._middle_side_testing_frame.test_text_box.tag_add(tag, line_number_to_str, line_number_to_str + "+" + str(len(text.split("\n")) - 1) + "lines")
    
    def insert_example_to_loaded_examples_text_box(self, text):
        self._middle_side_loaded_examples_frame.insert_loaded_examples_text_box(text)
    
    def insert_text_to_knowledge_base_text_box(self, text):
        self._middle_side_knowledge_base_frame.insert_knowledge_base_text_box(text)
    
    def set_test_text_tag_color(self, tag, color):
        self._middle_side_testing_frame.test_text_box.tag_config(tag, background = color)
    
    def clean_test_text_box(self):
        self._middle_side_testing_frame.clean_test_text_box()
        
    def clean_loaded_examples_text_box(self):
        self._middle_side_loaded_examples_frame.clean_loaded_examples_text_box()
    
    def set_completed_test_feedback(self, completed = 0, total = 0):
        self._lower_side_testing_frame.completed_tests_label.config(text = "Tests completados: " + str(completed) + " de " + str(total))

    def change_to_test_mode(self):
        self._upper_side_frame.manual_creating_mode_button.config(state = "normal")
        self._upper_side_frame.testing_mode_button.config(text = "Agregar Ejemplos")
        self._hide_manual_create_mode_widgets()
        self._show_test_mode_widgets()
    
    def change_to_batch_create_mode(self):
        self._upper_side_frame.manual_creating_mode_button.config(state = "normal")
        self._upper_side_frame.testing_mode_button.config(text = "Modo de Prueba")
        self._hide_test_mode_widgets()
        self._hide_manual_create_mode_widgets()
    
    def change_to_manual_create_mode(self):
        self._upper_side_frame.manual_creating_mode_button.config(state = "disabled")
        self._upper_side_frame.testing_mode_button.config(text = "Modo de Prueba")
        self._hide_test_mode_widgets()
        self._show_manual_create_mode_widgets()
    
    def enable_mode_buttons(self):
        self._upper_side_frame.testing_mode_button.config(state = "normal")
        self._upper_side_frame.submit_knowledge_base_button.config(state = "disabled")
        