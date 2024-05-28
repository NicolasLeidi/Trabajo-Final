import tkinter as tk
from tkinter import filedialog
from tkinter import * 
from utils.FeedbackEnum import FeedbackEnum

class MainView():
    
    def __init__(self, root, presenter):
        self.root = root
        self.presenter = presenter
        self.ordered = IntVar()
        self.first_only = IntVar()
        self.create_widgets()
        self.set_initial_dimensions()
        self.test_counter = 0


    def create_widgets(self):
        self.root.title("Nombre a colocar")
        
        self.submit_knowledge_base_button = tk.Button(self.root, text="Cargar Base de conocimiento", command=lambda: self.load_knowledge_base())
        self.submit_knowledge_base_button.grid(row = 0, column = 0, pady = 2)
        
        self.testing_mode_button = tk.Button(self.root, text="Modo de prueba", width=20, command=lambda: self.test_mode())
        self.testing_mode_button.config(state = "disabled")
        self.testing_mode_button.grid(row = 0, column = 1, pady = 2)
        
        self.creating_mode_button = tk.Button(self.root, text="Modo de creación", width=20, command=lambda: self.create_mode())
        self.creating_mode_button.config(state = "disabled")
        self.creating_mode_button.grid(row = 0, column = 2, pady = 2)
        
        self.main_text_box = Text(self.root, height=30, width=100)
        self.main_text_box.config(state = "disabled")
        self.main_text_box.grid(row = 1, column = 0, columnspan = 3, pady = 2)
        
        self.ordered_checkbox = tk.Checkbutton(self.root, text="Ordenado", variable= self.ordered)
        
        self.first_only_checkbox = tk.Checkbutton(self.root, text="Primer Resultado", variable= self.first_only)
        
        self.run_tests = tk.Button(self.root, text="Correr", width=20, command=lambda: self.test_solution())
        
        self.save_tests = tk.Button(self.root, text="Guardar", width=20, command=lambda: self.load_examples())
    
    def load_examples(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        
        if not file_path:
            return
        
        self.presenter.examples(file_path, self.main_text_box.get("1.0",'end'), self.ordered.get(), self.first_only.get())
    
    def load_knowledge_base(self):
        file_path = filedialog.askopenfilename(filetypes=[("Archivo PROLOG", "*.pl")])
        
        if not file_path:
            return
        
        self.presenter.load_knowledge_base(file_path)
    
    def test_solution(self):
        # results = self.presenter.test_examples(filedialog.askopenfilename(filetypes=[("Batería de test", "*.txt")]))
        self.presenter.run_examples()
        
    def test_mode(self):
        # Para entrar al modo de testeo, primero se debe cargar una batería de tests válida
        file_path = filedialog.askopenfilename(filetypes=[("Batería de test", "*.txt")])
        
        if not file_path:
            return
        
        self.presenter.enter_test_mode(file_path)
    
    def create_mode(self):
        self.presenter.enter_create_mode()
        
    def open_popup(self, type, message):
        popup = tk.Tk()
        popup.wm_title(type)
        label = tk.Label(popup, text=message)
        label.pack(side="top", fill="x", pady=10)
        ok_button = tk.Button(popup, text="Ok", command=popup.destroy)
        ok_button.pack()
    
    def insert_example_to_main_text_box(self, query, result = FeedbackEnum.NONE, explanation = "", expected = "", obtained = ""):
        self.main_text_box.config(state = "normal")
        line_number = self.main_text_box.index('end-1c').split('.')[0]
        line_number_to_str = str(line_number) + ".0"
        
        self.test_counter += 1
        
        match result:
            case FeedbackEnum.NONE:
                text = f"Test {self.test_counter} - {query}\n"
                tag = "none"
                self.main_text_box.tag_config(tag, background="gray")
            case FeedbackEnum.SUCCESS:
                text = f"Test {self.test_counter} - {query} - Test passed.\n"
                tag = "success"
                self.main_text_box.tag_config(tag, background="green")
            case FeedbackEnum.ERROR:
                text = f"Test {self.test_counter} - {query} - Test failed.\n{explanation}\nSe esperaba: {expected}\nSe obtuvo: {obtained}\n"
                tag = "error"
                self.main_text_box.tag_config(tag, background="red")

        self.main_text_box.insert(END, text)
        
        # Coloreo una cantidad de lineas igual a la cantidad de lineas que ocupó la respuesta
        
        self.main_text_box.tag_add(tag, line_number_to_str, line_number_to_str + "+" + str(len(text.split("\n")) - 1) + "lines")
        
    
    def clean_main_text_box(self):
        self.main_text_box.config(state = "normal")
        self.main_text_box.delete('1.0', END)
        self.test_counter = 0
    
    def change_to_test_mode(self):
        self.creating_mode_button.config(state = "normal")
        self.main_text_box.config(state = "disabled")
        self.testing_mode_button.config(text = "Cambiar ejemplos")
        self.show_test_mode_widgets()
        self.ordered_checkbox.grid_forget()
        self.first_only_checkbox.grid_forget()
        self.save_tests.grid_forget()
    
    def change_to_create_mode(self):
        self.creating_mode_button.config(state = "disabled")
        self.testing_mode_button.config(text = "Modo de prueba")
        self.run_tests.grid_forget()
        self.show_create_mode_widgets()
    
    def set_initial_dimensions(self):
        self.root.minsize(300, 565)
        
        for col in range(3):
            self.root.grid_columnconfigure(col, minsize=100)
    
    def show_test_mode_widgets(self):
        self.run_tests.grid(row = 2, column = 1, pady = 10)
    
    def show_create_mode_widgets(self):
        self.save_tests.grid(row = 2, column = 2, pady = 10)
        self.first_only_checkbox.grid(row = 2, column = 1, pady = 10)
        self.save_tests.grid(row = 2, column = 2, pady = 10)
    
    def enable_mode_buttons(self):
        self.testing_mode_button.config(state = "normal")
        self.creating_mode_button.config(state = "normal")
        