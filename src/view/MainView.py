import tkinter as tk
from tkinter import filedialog
from tkinter import * 

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
        
        upper_side.grid_columnconfigure(1, weight=1, minsize=150)
        
        self.submit_knowledge_base_button = tk.Button(upper_side, text="Cargar Base de Conocimiento", command=lambda: self.load_knowledge_base())
        self.submit_knowledge_base_button.grid(row = 0, column = 0, pady = 2, sticky=W)
        
        self.testing_mode_button = tk.Button(upper_side, text="Modo de Prueba", width=20, command=lambda: self.test_mode())
        self.testing_mode_button.config(state = "disabled")
        self.testing_mode_button.grid(row = 0, column = 2, pady = 2, padx = 10, sticky=E)
        
        self.creating_mode_button = tk.Button(upper_side, text="Modo de Creación", width=20, command=lambda: self.create_mode())
        self.creating_mode_button.config(state = "disabled")
        self.creating_mode_button.grid(row = 0, column = 3, pady = 2, sticky=E)
        
        self.knowledge_base_text_box = Text(middle_side, height=30, width=30)
        self.knowledge_base_text_box.config(state = "disabled")
        self.knowledge_base_text_box.configure(bg="gray")
        self.knowledge_base_text_box.grid(row = 0, column = 0, rowspan=2, pady = 2)
        
        self.test_text_box = Text(middle_side, height=30, width=65)
        self.test_text_box.config(state = "disabled")
        self.test_text_box.grid(row = 0, column = 1, columnspan = 3, pady = 2)
        
        self.create_text_box = Text(middle_side, height=15, width=65)
        self.loaded_examples_text_box = Text(middle_side, height=15, width=65)
        self.loaded_examples_text_box.config(state = "disabled")
        self.loaded_examples_text_box.configure(bg="gray")
        
        self.ordered_checkbox = tk.Checkbutton(lower_side, text="Sin Orden", variable= self.ordered)
        self.first_only_checkbox = tk.Checkbutton(lower_side, text="Primer Resultado", variable= self.first_only)
        self.run_tests_button = tk.Button(lower_side, text="Correr", width=20, command=lambda: self.test_solution())
        self.add_tests_button = tk.Button(lower_side, text="Agregar", width=20, command=lambda: self.add_example())
        self.save_tests_button = tk.Button(lower_side, text="Guardar", width=20, command=lambda: self.save_examples())
        self.clean_examples_button = tk.Button(lower_side, text="Limpiar", width=20, command=lambda: self.clean_examples())
        self.pop_examples_button = tk.Button(lower_side, text="Deshacer", width=20, command=lambda: self.pop_examples())
    
    def test_solution(self):
        self.presenter.run_examples()
        
    def add_example(self):        
        self.presenter.add_examples(self.create_text_box.get("1.0",'end'), self.ordered.get(), self.first_only.get())
    
    def save_examples(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        
        if not file_path:
            return
        
        self.presenter.save_examples(file_path)
    
    def clean_examples(self):
        self.presenter.clean_examples()
    
    def pop_examples(self):
        self.presenter.pop_examples()
    
    def load_knowledge_base(self):
        file_path = filedialog.askopenfilename(filetypes=[("Archivo PROLOG", "*.pl")])
        
        if not file_path:
            return
        
        self.presenter.load_knowledge_base(file_path)
        
    def test_mode(self):
        # Para entrar al modo de testeo, primero se debe cargar una batería de tests válida
        file_path = filedialog.askopenfilename(filetypes=[("Batería de test", "*.json")])
        
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
    
    def insert_example_to_test_text_box(self, text, tag = 0):
        self.test_text_box.config(state = "normal")
        line_number = self.test_text_box.index('end-1c').split('.')[0]
        line_number_to_str = str(line_number) + ".0"

        self.test_text_box.insert(END, text)
                
        # Coloreo una cantidad de lineas igual a la cantidad de lineas que ocupó la respuesta
        
        self.test_text_box.tag_add(tag, line_number_to_str, line_number_to_str + "+" + str(len(text.split("\n")) - 1) + "lines")
    
    def insert_example_to_loaded_examples_text_box(self, text):
        self.loaded_examples_text_box.config(state = "normal")
        self.loaded_examples_text_box.insert(END, text)
        self.loaded_examples_text_box.config(state = "disabled")
    
    def insert_text_to_knowledge_base_text_box(self, text):
        self.knowledge_base_text_box.config(state = "normal")
        self.knowledge_base_text_box.insert(END, text)
        self.knowledge_base_text_box.config(state = "disabled")
    
    def set_test_text_tag_color(self, tag, color):
        self.test_text_box.tag_config(tag, background = color)
    
    def clean_test_text_box(self):
        self.test_text_box.config(state = "normal")
        self.test_text_box.delete('1.0', END)
    
    def clean_create_text_box(self):
        self.create_text_box.delete('1.0', END)
        
    def clean_loaded_examples_text_box(self):
        self.loaded_examples_text_box.config(state = "normal")
        self.loaded_examples_text_box.delete('1.0', END)    
        
    def change_to_test_mode(self):
        self.creating_mode_button.config(state = "normal")
        self.test_text_box.config(state = "disabled")
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
        self.run_tests_button.grid(row = 2, column = 1)
        self.test_text_box.grid(row = 0, column = 1, columnspan = 3, pady = 2)
    
    def hide_test_mode_widgets(self):
        self.run_tests_button.grid_forget()
        self.test_text_box.grid_forget()
    
    def hide_create_mode_widgets(self):
        self.ordered_checkbox.grid_forget()
        self.first_only_checkbox.grid_forget()
        self.add_tests_button.grid_forget()
        self.pop_examples_button.grid_forget()
        self.clean_examples_button.grid_forget()
        self.save_tests_button.grid_forget()
        self.create_text_box.grid_forget()
        self.loaded_examples_text_box.grid_forget()
    
    def show_create_mode_widgets(self):
        self.create_text_box.grid(row = 0, column = 1, columnspan = 3, pady = 0)
        self.loaded_examples_text_box.grid(row = 1, column = 1, columnspan = 3, pady = 0)
        
        self.ordered_checkbox.grid(row = 0, column = 0, padx = 10)
        self.first_only_checkbox.grid(row = 0, column = 1, padx = 10)
        self.add_tests_button.grid(row = 0, column = 2, padx = 10)
        self.pop_examples_button.grid(row = 0, column = 3, padx = 10)
        
        self.clean_examples_button.grid(row = 1, column = 0, padx = 10)
        self.save_tests_button.grid(row = 1, column = 3, padx = 10)
    
    def enable_mode_buttons(self):
        self.testing_mode_button.config(state = "normal")
        self.creating_mode_button.config(state = "normal")
        self.submit_knowledge_base_button.config(state = "disabled")
        