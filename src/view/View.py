from tkinter import filedialog
from tkinter import *
from abc import ABC, abstractmethod

class View(ABC):

    def _base_window_dimension(self, root):
        root.title("SwipTesting")
        root.geometry('{}x{}'.format(800, 600))
        root.grid_rowconfigure(1, weight=1)
        root.grid_rowconfigure(2, weight=1)
        root.grid_columnconfigure(0, weight=1)
        root.grid_columnconfigure(1, weight=2)

    def _handle_test_text_box_click(self, line):
        self.presenter.handle_test_text_box_click(line)
    
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
        # Loads a test file and updates the test text box
        file_path = filedialog.askopenfilenames(filetypes=[("Batería de test", "*.json")])
        
        if not file_path:
            return
        
        self.presenter.load_test_file(file_path)
    
    def _batch_create_mode(self):
        self.presenter.enter_batch_create_mode()
    
    def _manual_create_mode(self):
        self.presenter.enter_manual_create_mode()
    
    def _show_test_mode_widgets(self):
        self._middle_side_testing_frame.grid(row = 1, column = 1, rowspan = 2, sticky="nsew")
        self._lower_side_testing_frame.grid(row = 3, sticky="ew", columnspan = 5)
        self._lower_side_testing_frame.show_tests()
    
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
        """
        Opens a popup window with the given type and message.

        Parameters:
            type (str): The title of the popup window.
            message (str): The message to display in the popup window.
        """
        popup = Tk()
        popup.wm_title(type)
        label = Label(popup, text=message)
        label.pack(side="top", fill="x", pady=10)
        ok_button = Button(popup, text="Ok", command=popup.destroy)
        ok_button.pack()
    
    def insert_example_to_test_text_box(self, text, tag = 0):
        """
        Inserts the given text into the test text box and colors the corresponding lines.

        Parameters:
            text (str): The text to be inserted.
            tag (int, optional): The tag to be applied to the inserted text. Defaults to 0.
        """
        line_number = self._middle_side_testing_frame.test_text_box.index('end-1c').split('.')[0]
        line_number_to_str = str(line_number) + ".0"

        self._middle_side_testing_frame.insert_test_text_box(text)
        
        # Color a number of lines equal to the number of lines that the result has
        
        self._middle_side_testing_frame.test_text_box.tag_add(tag, line_number_to_str, line_number_to_str + "+" + str(len(text.split("\n")) - 1) + "lines")
    
    def insert_example_to_loaded_examples_text_box(self, text):
        """
        Inserts the given text into the loaded examples text box.

        Parameters:
            text (str): The text to be inserted.
        """
        self._middle_side_loaded_examples_frame.insert_loaded_examples_text_box(text)
    
    def insert_text_to_knowledge_base_text_box(self, text):
        """
        Inserts the given text into the knowledge base text box.

        Parameters:
            text (str): The text to be inserted.
        """
        self._middle_side_knowledge_base_frame.insert_knowledge_base_text_box(text)
    
    def set_test_text_tag_color(self, tag, color):
        """
        Sets the background color for the specified tag in the test text box.

        Parameters:
            tag: The tag to be configured.
            color: The background color to set for the tag.
        """
        self._middle_side_testing_frame.test_text_box.tag_config(tag, background = color)
    
    def clean_test_text_box(self):
        """
        Cleans the test text box of the testing frame.
        """
        self._middle_side_testing_frame.clean_test_text_box()
        
    def clean_loaded_examples_text_box(self):
        """
        Cleans the loaded examples text box of the loaded examples frame.
        """
        self._middle_side_loaded_examples_frame.clean_loaded_examples_text_box()
    
    def set_completed_test_feedback(self, completed = 0, total = 0):
        """
        Sets the completed test feedback in the lower side testing frame.

        Parameters:
            completed (int): The number of completed tests. Defaults to 0.
            total (int): The total number of tests. Defaults to 0.
        """
        self._lower_side_testing_frame.completed_tests_label.config(text = "Tests exitosos: " + str(completed) + " de " + str(total))

    def change_to_test_mode(self):
        """
        Change the view to test mode.
        """
        self._upper_side_frame.manual_creating_mode_button.config(state = "normal")
        self._upper_side_frame.testing_mode_button.config(text = "Agregar Ejemplos")
        self._hide_manual_create_mode_widgets()
        self._show_test_mode_widgets()
    
    def change_to_showing_results_mode(self):
        """
        Change the view to show results mode.
        """
        self._upper_side_frame.manual_creating_mode_button.config(state = "normal")
        self._upper_side_frame.testing_mode_button.config(text = "Agregar Ejemplos")
        self._hide_manual_create_mode_widgets()
        self._lower_side_testing_frame.show_results()
    
    def change_to_manual_create_mode(self):
        """
        Changes the view to manual create mode by disabling the manual creating mode button, updating the text of the testing mode button to "Modo de Prueba", hiding the test mode widgets, and showing the manual create mode widgets.
        """
        self._upper_side_frame.manual_creating_mode_button.config(state = "disabled")
        self._upper_side_frame.testing_mode_button.config(text = "Probar")
        self._hide_test_mode_widgets()
        self._show_manual_create_mode_widgets()
    
    def enable_mode_buttons(self):
        """
        Enables the mode buttons by setting the state of the testing mode button to "normal" and the submit knowledge base button to "disabled".
        """
        self._upper_side_frame.testing_mode_button.config(state = "normal")
        self._upper_side_frame.submit_knowledge_base_button.config(state = "disabled")