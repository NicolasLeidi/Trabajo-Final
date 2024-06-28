import tkinter as tk
from tkinter import filedialog
from tkinter import * 

class MainView():
    
    def __init__(self, root, presenter):
        self.presenter = presenter
        self.__ordered = IntVar()
        self.__first_only = IntVar()
        self.__create_widgets(root)

    def __create_widgets(self, root):
        root.title("Nombre a colocar")
        root.geometry('{}x{}'.format(800, 600))
        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)
        
        # Creo, ubico y configuro frames
        
        upper_side_frame = Frame(root, bg="blue", width=800, height=50, pady=3)
        middle_side_frame = Frame(root, bg="red", width=800, pady=3)
        lower_side_frame = Frame(root, bg="green", width=800, height=50, pady=3)
        
        upper_side_frame.grid(row = 0, stick="ew")
        middle_side_frame.grid(row = 1, sticky="nsew")
        lower_side_frame.grid(row = 2, sticky="ew")
        
        upper_side_frame.grid_rowconfigure(0, weight=1)
        upper_side_frame.grid_columnconfigure(1, weight=1)
        
        middle_side_frame.grid_rowconfigure(0, weight=1)
        middle_side_frame.grid_columnconfigure(0, weight=1)
        middle_side_frame.grid_columnconfigure(1, weight=1)
        
        lower_side_frame.grid_rowconfigure(0, weight=1)
        for i in range(3):
            lower_side_frame.grid_columnconfigure(i, weight=1)
        
        # Widgets del frame superior
        
        self.__submit_knowledge_base_button = tk.Button(upper_side_frame, text="Cargar Base de Conocimiento", command=lambda: self.__load_knowledge_base())
        self.__testing_mode_button = tk.Button(upper_side_frame, text="Modo de Prueba", width=20, command=lambda: self.__test_mode())
        self.__creating_mode_button = tk.Button(upper_side_frame, text="Modo de Creación", width=20, command=lambda: self.__create_mode())
        
        # Widgets del frame intermedio
        
        self.__knowledge_base_text_box = Text(middle_side_frame, height=30, width=30)
        self.__test_text_box = Text(middle_side_frame, height=30, width=65)
        self.__create_text_box = Text(middle_side_frame, height=15, width=65)
        self.__loaded_examples_text_box = Text(middle_side_frame, height=15, width=65)
        
        # Widgets del frame inferior
        
        self.__ordered_checkbox = tk.Checkbutton(lower_side_frame, text="Sin Orden", variable= self.__ordered)
        self.__first_only_checkbox = tk.Checkbutton(lower_side_frame, text="Primer Resultado", variable= self.__first_only)
        self.__run_tests_button = tk.Button(lower_side_frame, text="Correr", width=20, command=lambda: self.__test_solution())
        self.__add_tests_button = tk.Button(lower_side_frame, text="Agregar", width=20, command=lambda: self.__add_example())
        self.__save_tests_button = tk.Button(lower_side_frame, text="Guardar", width=20, command=lambda: self.__save_examples())
        self.__clean_examples_button = tk.Button(lower_side_frame, text="Limpiar", width=20, command=lambda: self.__clean_examples())
        self.__pop_examples_button = tk.Button(lower_side_frame, text="Deshacer", width=20, command=lambda: self.__pop_examples())
        
        # Configuro widgets
        
        self.__testing_mode_button.config(state = "disabled")
        self.__creating_mode_button.config(state = "disabled")
        self.__knowledge_base_text_box.config(state = "disabled")
        self.__knowledge_base_text_box.configure(bg="gray")
        self.__test_text_box.config(state = "disabled")
        self.__loaded_examples_text_box.config(state = "disabled")
        self.__loaded_examples_text_box.configure(bg="gray")
        
        # Coloco widgets
        
        self.__submit_knowledge_base_button.grid(row = 0, column = 0, pady = 2)
        self.__testing_mode_button.grid(row = 0, column = 2, pady = 2, padx = 10)
        self.__creating_mode_button.grid(row = 0, column = 3, pady = 2)
        self.__knowledge_base_text_box.grid(row = 0, column = 0, rowspan=2, pady = 2)
        self.__test_text_box.grid(row = 0, column = 1, columnspan = 3, pady = 2)
        
    def __test_solution(self):
        self.presenter.run_examples()
        
    def __add_example(self):        
        self.presenter.add_examples(self.__create_text_box.get("1.0",'end'), self.__ordered.get(), self.__first_only.get())
    
    def __save_examples(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        
        if not file_path:
            return
        
        self.presenter.save_examples(file_path)
    
    def __clean_examples(self):
        self.presenter.clean_examples()
    
    def __pop_examples(self):
        self.presenter.pop_examples()
    
    def __load_knowledge_base(self):
        file_path = filedialog.askopenfilename(filetypes=[("Archivo PROLOG", "*.pl")])
        
        if not file_path:
            return
        
        self.presenter.load_knowledge_base(file_path)
        
    def __test_mode(self):
        # Para entrar al modo de testeo, primero se debe cargar una batería de tests válida
        file_path = filedialog.askopenfilename(filetypes=[("Batería de test", "*.json")])
        
        if not file_path:
            return
        
        self.presenter.enter_test_mode(file_path)
    
    def __create_mode(self):
        self.presenter.enter_create_mode()
    
    def __show_test_mode_widgets(self):
        self.__run_tests_button.grid(row = 2, column = 1)
        self.__test_text_box.grid(row = 0, column = 1, columnspan = 3, pady = 2)
    
    def __hide_test_mode_widgets(self):
        self.__run_tests_button.grid_forget()
        self.__test_text_box.grid_forget()
    
    def __hide_create_mode_widgets(self):
        self.__ordered_checkbox.grid_forget()
        self.__first_only_checkbox.grid_forget()
        self.__add_tests_button.grid_forget()
        self.__pop_examples_button.grid_forget()
        self.__clean_examples_button.grid_forget()
        self.__save_tests_button.grid_forget()
        self.__create_text_box.grid_forget()
        self.__loaded_examples_text_box.grid_forget()
    
    def __show_create_mode_widgets(self):
        self.__create_text_box.grid(row = 0, column = 1, columnspan = 3, pady = 0)
        self.__loaded_examples_text_box.grid(row = 1, column = 1, columnspan = 3, pady = 0)
        
        self.__ordered_checkbox.grid(row = 0, column = 0, padx = 10)
        self.__first_only_checkbox.grid(row = 0, column = 1, padx = 10)
        self.__add_tests_button.grid(row = 0, column = 2, padx = 10)
        self.__pop_examples_button.grid(row = 0, column = 3, padx = 10)
        
        self.__clean_examples_button.grid(row = 1, column = 0, padx = 10)
        self.__save_tests_button.grid(row = 1, column = 3, padx = 10)
    
    def open_popup(self, type, message):
        popup = tk.Tk()
        popup.wm_title(type)
        label = tk.Label(popup, text=message)
        label.pack(side="top", fill="x", pady=10)
        ok_button = tk.Button(popup, text="Ok", command=popup.destroy)
        ok_button.pack()
    
    def insert_example_to_test_text_box(self, text, tag = 0):
        self.__test_text_box.config(state = "normal")
        line_number = self.__test_text_box.index('end-1c').split('.')[0]
        line_number_to_str = str(line_number) + ".0"

        self.__test_text_box.insert(END, text)
                
        # Coloreo una cantidad de lineas igual a la cantidad de lineas que ocupó la respuesta
        
        self.__test_text_box.tag_add(tag, line_number_to_str, line_number_to_str + "+" + str(len(text.split("\n")) - 1) + "lines")
    
    def insert_example_to_loaded_examples_text_box(self, text):
        self.__loaded_examples_text_box.config(state = "normal")
        self.__loaded_examples_text_box.insert(END, text)
        self.__loaded_examples_text_box.config(state = "disabled")
    
    def insert_text_to_knowledge_base_text_box(self, text):
        self.__knowledge_base_text_box.config(state = "normal")
        self.__knowledge_base_text_box.insert(END, text)
        self.__knowledge_base_text_box.config(state = "disabled")
    
    def set_test_text_tag_color(self, tag, color):
        self.__test_text_box.tag_config(tag, background = color)
    
    def clean_test_text_box(self):
        self.__test_text_box.config(state = "normal")
        self.__test_text_box.delete('1.0', END)
    
    def clean_create_text_box(self):
        self.__create_text_box.delete('1.0', END)
        
    def clean_loaded_examples_text_box(self):
        self.__loaded_examples_text_box.config(state = "normal")
        self.__loaded_examples_text_box.delete('1.0', END)    
        
    def change_to_test_mode(self):
        self.__creating_mode_button.config(state = "normal")
        self.__test_text_box.config(state = "disabled")
        self.__testing_mode_button.config(text = "Cambiar ejemplos")
        self.__hide_create_mode_widgets()
        self.__show_test_mode_widgets()
    
    def change_to_create_mode(self):
        self.__creating_mode_button.config(state = "disabled")
        self.__testing_mode_button.config(text = "Modo de prueba")
        self.__hide_test_mode_widgets()
        self.__show_create_mode_widgets()
    
    def enable_mode_buttons(self):
        self.__testing_mode_button.config(state = "normal")
        self.__creating_mode_button.config(state = "normal")
        self.__submit_knowledge_base_button.config(state = "disabled")
        