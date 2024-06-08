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


    def create_widgets(self):
        self.root.title("Nombre a colocar")
        
        upper_side = Frame(self.root)
        middle_side = Frame(self.root)
        lower_side = Frame(self.root)
        
        upper_side.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 5)
        middle_side.grid(row = 1, column = 0, columnspan = 4, padx = 10)
        lower_side.grid(row = 2, column = 0, columnspan = 4, padx = 10, pady = 5)
        
        # upper_side.grid_columnconfigure((0, 3), minsize=150)
        upper_side.grid_columnconfigure(1, weight=1, minsize=150)
        
        self.submit_knowledge_base_button = tk.Button(upper_side, text="Cargar Base de conocimiento", command=lambda: self.load_knowledge_base())
        self.submit_knowledge_base_button.grid(row = 0, column = 0, pady = 2, sticky=W)
        
        self.testing_mode_button = tk.Button(upper_side, text="Modo de prueba", width=20, command=lambda: self.test_mode())
        self.testing_mode_button.config(state = "disabled")
        self.testing_mode_button.grid(row = 0, column = 2, pady = 2, padx = 10, sticky=E)
        
        self.creating_mode_button = tk.Button(upper_side, text="Modo de creación", width=20, command=lambda: self.create_mode())
        self.creating_mode_button.config(state = "disabled")
        self.creating_mode_button.grid(row = 0, column = 3, pady = 2, sticky=E)
        
        self.main_text_box = Text(middle_side, height=30, width=100)
        self.main_text_box.config(state = "disabled")
        self.main_text_box.grid(row = 0, column = 0, columnspan = 4, pady = 2)
        
        self.ordered_checkbox = tk.Checkbutton(lower_side, text="Ordenado", variable= self.ordered)
        
        self.first_only_checkbox = tk.Checkbutton(lower_side, text="Primer Resultado", variable= self.first_only)
        
        self.run_tests = tk.Button(lower_side, text="Correr", width=20, command=lambda: self.test_solution())
        
        self.add_tests = tk.Button(lower_side, text="Agregar", width=20, command=lambda: self.load_examples())
        
        self.save_tests = tk.Button(lower_side, text="Guardar", width=20, command=lambda: self.save_examples())
    
    def load_examples(self):        
        self.presenter.add_examples(self.main_text_box.get("1.0",'end'), self.ordered.get(), self.first_only.get())
    
    def save_examples(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        
        if not file_path:
            return
        
        self.presenter.save_examples(file_path, self.main_text_box.get("1.0",'end'), self.ordered.get(), self.first_only.get())
    
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
    
    def insert_example_to_main_text_box(self, text, tag = 0):
        self.main_text_box.config(state = "normal")
        line_number = self.main_text_box.index('end-1c').split('.')[0]
        line_number_to_str = str(line_number) + ".0"

        self.main_text_box.insert(END, text)
                
        # Coloreo una cantidad de lineas igual a la cantidad de lineas que ocupó la respuesta
        
        self.main_text_box.tag_add(tag, line_number_to_str, line_number_to_str + "+" + str(len(text.split("\n")) - 1) + "lines")
    
    def set_main_text_tag_color(self, tag, color):
        self.main_text_box.tag_config(tag, background = color)
    
    def clean_main_text_box(self):
        self.main_text_box.config(state = "normal")
        self.main_text_box.delete('1.0', END)
    
    def change_to_test_mode(self):
        self.creating_mode_button.config(state = "normal")
        self.main_text_box.config(state = "disabled")
        self.testing_mode_button.config(text = "Cambiar ejemplos")
        self.hide_create_mode_widgets()
        self.show_test_mode_widgets()
    
    def change_to_create_mode(self):
        self.creating_mode_button.config(state = "disabled")
        self.testing_mode_button.config(text = "Modo de prueba")
        self.hide_test_mode_widgets()
        self.show_create_mode_widgets()
    
    def set_initial_dimensions(self):
        self.root.minsize(300, 565)
        
        for col in range(3):
            self.root.grid_columnconfigure(col, minsize=100)
    
    def show_test_mode_widgets(self):
        self.run_tests.grid(row = 2, column = 1)
    
    def hide_test_mode_widgets(self):
        self.run_tests.grid_forget()
    
    def hide_create_mode_widgets(self):
        self.ordered_checkbox.grid_forget()
        self.first_only_checkbox.grid_forget()
        self.add_tests.grid_forget()
        self.save_tests.grid_forget()
    
    def show_create_mode_widgets(self):
        self.ordered_checkbox.grid(row = 2, column = 0, padx = 10)
        self.first_only_checkbox.grid(row = 2, column = 1, padx = 10)
        self.add_tests.grid(row = 2, column = 2, padx = 10)
        self.save_tests.grid(row = 2, column = 3, padx = 10)
    
    def enable_mode_buttons(self):
        self.testing_mode_button.config(state = "normal")
        self.creating_mode_button.config(state = "normal")
        