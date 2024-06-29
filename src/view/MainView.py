import tkinter as tk
from tkinter import filedialog
from tkinter import * 
from tktooltip import ToolTip

class MainView():
    
    def __init__(self, root, presenter):
        self.presenter = presenter
        self.__ordered = IntVar()
        self.__first_only = IntVar()
        self.__create_widgets(root)

    def __create_widgets(self, root):
        # Configuro la ventana
        
        root.title("Nombre a colocar")
        root.geometry('{}x{}'.format(800, 600))
        root.grid_rowconfigure(1, weight=1)
        root.grid_rowconfigure(2, weight=1)
        root.grid_columnconfigure(0, weight=1)
        root.grid_columnconfigure(1, weight=2)
        
        # Creo los frames
        
        self.__upper_side_frame = Frame(root, bg="blue", width=800, height=50, pady=3, padx=10)
        self.__middle_side_knowledge_base_frame = Frame(root, bg="red", width=320, pady=3, padx=5)
        self.__middle_side_testing_frame = Frame(root, bg="pink", width=480, pady=3, padx=5)
        self.__middle_side_batch_creating_frame = Frame(root, bg="pink", width=480, pady=3, padx=5)
        self.__middle_side_manual_creating_frame = Frame(root, bg="pink", width=480, pady=3, padx=5)
        self.__middle_side_loaded_examples_frame = Frame(root, bg="pink", width=480, pady=3, padx=5)
        self.__lower_side_testing_frame = Frame(root, bg="green", width=800, height=50, pady=3)
        self.__lower_side_batch_creating_frame = Frame(root, bg="green", width=800, height=50, pady=3)
        
        # Ubico los frames
        
        self.__upper_side_frame.grid(row = 0, stick="ew", columnspan = 2)
        self.__middle_side_knowledge_base_frame.grid(row = 1, column = 0, rowspan = 2, sticky="nsew")
        self.__middle_side_testing_frame.grid(row = 1, column = 1, rowspan = 2, sticky="nsew")
        
        # Configuro los frames
        
        self.__upper_side_frame.grid_rowconfigure(0, weight=1)
        self.__upper_side_frame.grid_columnconfigure(1, weight=1)
        
        self.__middle_side_knowledge_base_frame.grid_rowconfigure(0, weight=1)
        self.__middle_side_knowledge_base_frame.grid_columnconfigure(0, weight=1)
        
        self.__middle_side_testing_frame.grid_rowconfigure(0, weight=1)
        self.__middle_side_testing_frame.grid_columnconfigure(0, weight=1)
        
        self.__middle_side_batch_creating_frame.grid_rowconfigure(0, weight=1)
        self.__middle_side_batch_creating_frame.grid_columnconfigure(0, weight=1)
        self.__middle_side_batch_creating_frame.grid_columnconfigure(1, weight=1)
        
        self.__middle_side_manual_creating_frame.grid_rowconfigure(0, weight=1)
        for i in range(4):
            self.__middle_side_manual_creating_frame.grid_columnconfigure(i, weight=1)
        
        self.__middle_side_loaded_examples_frame.grid_rowconfigure(0, weight=1)
        self.__middle_side_loaded_examples_frame.grid_columnconfigure(0, weight=1)
        
        self.__lower_side_testing_frame.grid_rowconfigure(0, weight=1)
        for i in range(4):
            self.__lower_side_testing_frame.grid_columnconfigure(i, weight=1)
        
        self.__lower_side_batch_creating_frame.grid_rowconfigure(0, weight=1)
        for i in range(3):
            self.__lower_side_batch_creating_frame.grid_columnconfigure(i, weight=1)
        
        # Widgets del frame superior
        
        self.__submit_knowledge_base_button = tk.Button(self.__upper_side_frame, text="Cargar Base de Conocimiento", command=lambda: self.__load_knowledge_base())
        self.__testing_mode_button = tk.Button(self.__upper_side_frame, text="Modo de Prueba", width=20, command=lambda: self.__test_mode())
        self.__batch_creating_mode_button = tk.Button(self.__upper_side_frame, text="Modo de Creación", width=20, command=lambda: self.__batch_create_mode())
        self.__manual_creating_mode_button = tk.Button(self.__upper_side_frame, text="Creación Manual", width=20, command=lambda: self.__manual_create_mode())
        
        # Widgets del frame intermedio
        
        knowledge_base_label = tk.Label(self.__middle_side_knowledge_base_frame, text="Base de Conocimiento")
        self.__knowledge_base_text_box = Text(self.__middle_side_knowledge_base_frame)
        
        test_label = tk.Label(self.__middle_side_testing_frame, text="Batería de Tests")
        self.__test_text_box = Text(self.__middle_side_testing_frame)
        
        batch_create_label = tk.Label(self.__middle_side_batch_creating_frame, text="Crear Ejemplo")
        self.__batch_create_text_box = Text(self.__middle_side_batch_creating_frame, height=15, width=65)
        
        manual_create_query_label = tk.Label(self.__middle_side_manual_creating_frame, text="Crear Query de Ejemplo")
        self.__manual_create_query_text_box = Text(self.__middle_side_manual_creating_frame)
        manual_create_expected_result_label = tk.Label(self.__middle_side_manual_creating_frame, text="Resultado Esperado")
        self.__manual_create_expected_result_text_box = Text(self.__middle_side_manual_creating_frame)
        
        loaded_examples_label = tk.Label(self.__middle_side_loaded_examples_frame, text="Ejemplos Cargados")
        self.__loaded_examples_text_box = Text(self.__middle_side_loaded_examples_frame, height=15, width=65)
        
        # Widgets del frame inferior
        
        run_tests_button = tk.Button(self.__lower_side_testing_frame, text="Correr", width=20, command=lambda: self.__test_solution())
        self.__completed_tests_label = tk.Label(self.__lower_side_testing_frame, text="Tests completados: 0 de 0")
        
        ordered_checkbox = tk.Checkbutton(self.__lower_side_batch_creating_frame, text="Sin Orden", variable= self.__ordered)
        first_only_checkbox = tk.Checkbutton(self.__lower_side_batch_creating_frame, text="Primer Resultado", variable= self.__first_only)
        add_tests_button = tk.Button(self.__lower_side_batch_creating_frame, text="Agregar", width=20, command=lambda: self.__add_example(self.__batch_create_text_box))
        save_tests_button = tk.Button(self.__lower_side_batch_creating_frame, text="Guardar", width=20, command=lambda: self.__save_examples())
        clean_examples_button = tk.Button(self.__lower_side_batch_creating_frame, text="Limpiar", width=20, command=lambda: self.__clean_examples())
        pop_examples_button = tk.Button(self.__lower_side_batch_creating_frame, text="Deshacer", width=20, command=lambda: self.__pop_examples())
        
        # Configuro widgets del frame superior
        
        ToolTip(self.__submit_knowledge_base_button, msg="Carga la base de conocimiento, la cual será usada para realizar las pruebas.", delay=1.0)
        ToolTip(self.__testing_mode_button, msg="Entra al modo prueba, en el cual permite correr una batería de tests sobre la base de conocimiento cargada.", delay=1.0)
        ToolTip(self.__batch_creating_mode_button, msg="Entra al modo creación en grupos, en el cual permite crear una batería de tests utilizando la base de conocimiento cargada para obtener los resultados esperados.", delay=1.0)
        ToolTip(self.__manual_creating_mode_button, msg="Entra a l modo de creación manualmente, en el cual permite colocar queries y sus resultados esperados para armar una batería de tests.", delay=1.0)
        self.__testing_mode_button.config(state = "disabled")
        self.__batch_creating_mode_button.config(state = "disabled")
        
        # Configuro widgets del frame intermedio
        
        ToolTip(self.__knowledge_base_text_box, msg="Base de conocimiento cargada, será usada para realizar pruebas.", delay=1.0)
        self.__knowledge_base_text_box.config(state = "disabled")
        self.__knowledge_base_text_box.configure(bg="gray")
        
        ToolTip(self.__test_text_box, msg="Batería de test cargada actualmente, la cual será ejecutada al presionar Correr.", delay=1.0)
        self.__test_text_box.config(state = "disabled")
        
        ToolTip(self.__batch_create_text_box, msg="Aquí puede escribir queries que usarán el programa cargado para crear una batería de tests.", delay=1.0)
        
        ToolTip(self.__manual_create_query_text_box, msg="Aquí puede colocar el query a probar. Limitado a una query por prueba.", delay=1.0)
        ToolTip(self.__manual_create_expected_result_text_box, msg="Aquí tiene que colocar el resultado esperado de la query de arriba. Respetar sintaxis:\nVariable : Valor, múltiples variables separadas con comas. Ej: X : [1, 2], Y : 3\nSi hay múltiples resultados, cada uno debe estar dentro de llaves \{\}", delay=1.0)
        
        ToolTip(self.__loaded_examples_text_box, msg="Ejemplos cargados actualmente a la nueva batería de tests.", delay=1.0)
        self.__loaded_examples_text_box.config(state = "disabled")
        self.__loaded_examples_text_box.configure(bg="gray")
        
        # Configuro widgets del frame inferior
        
        ToolTip(run_tests_button, msg="Corre la batería de tests cargada actualmente sobre la base de conocimiento cargada.", delay=1.0)
        
        ToolTip(add_tests_button, msg="Agrega un ejemplo a la batería de tests cargada actualmente.", delay=1.0)
        ToolTip(save_tests_button, msg="Guarda la batería de tests cargada actualmente.", delay=1.0)
        ToolTip(clean_examples_button, msg="Limpia todos los ejemplos cargados actualmente.", delay=1.0)
        ToolTip(pop_examples_button, msg="Deshace el último ejemplo cargado actualmente.", delay=1.0)
        ToolTip(ordered_checkbox, msg="Cambia el comportamiento de la batería de tests, compara los conjuntos de resultados sin importar el orden.", delay=1.0)
        ToolTip(first_only_checkbox, msg="Cambia el comportamiento de la batería de tests, solo compara la primera unificación.", delay=1.0)
        
        # Coloco widgets del frame superior
        
        self.__submit_knowledge_base_button.grid(row = 0, column = 0, pady = 2)
        self.__testing_mode_button.grid(row = 0, column = 2, pady = 2, padx=(10,0))
        self.__batch_creating_mode_button.grid(row = 0, column = 3, pady = 2, padx = 10)
        self.__manual_creating_mode_button.grid(row = 0, column = 4, pady = 2)
        
        # Coloco widgets del frame intermedio
        
        knowledge_base_label.place(relheight=0.05, relwidth=1)
        self.__knowledge_base_text_box.place(rely=0.05,relheight=0.95, relwidth=1)
        
        test_label.place(relheight=0.05, relwidth=1)
        self.__test_text_box.place(rely=0.05, relheight=0.95, relwidth=1)
        
        batch_create_label.place(relheight=0.1, relwidth=1)
        self.__batch_create_text_box.place(rely=0.1, relheight=0.9, relwidth=1)
        
        manual_create_query_label.place(relheight=0.05, relwidth=1)
        self.__manual_create_query_text_box.place(rely=0.05, relheight=0.45, relwidth=1)
        manual_create_expected_result_label.place(rely=0.5, relheight=0.05, relwidth=1)
        self.__manual_create_expected_result_text_box.place(rely=0.55, relheight=0.45, relwidth=1)
        
        loaded_examples_label.place(relheight=0.1, relwidth=1)
        self.__loaded_examples_text_box.place(rely=0.1, relheight=0.9, relwidth=1)
        
        # Coloco widgets del frame inferior
        
        run_tests_button.grid(row = 0, column = 1)
        self.__completed_tests_label.grid(row = 0, column = 2)
        
        ordered_checkbox.grid(row = 0, column = 0, padx = 10)
        first_only_checkbox.grid(row = 0, column = 1, padx = 10)
        add_tests_button.grid(row = 0, column = 2, padx = 10)
        pop_examples_button.grid(row = 0, column = 3, padx = 10)
        clean_examples_button.grid(row = 1, column = 0, padx = 10)
        save_tests_button.grid(row = 1, column = 3, padx = 10)

    def __test_solution(self):
        self.presenter.run_examples()
        
    def __add_example(self, text_box):
        if not text_box.compare("end-1c", "==", "1.0"): 
            self.presenter.add_examples(text_box.get("1.0",'end'), self.__ordered.get(), self.__first_only.get())
    
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
    
    def __batch_create_mode(self):
        self.presenter.enter_batch_create_mode()
    
    def __manual_create_mode(self):
        self.presenter.enter_manual_create_mode()
    
    def __show_test_mode_widgets(self):
        self.__middle_side_testing_frame.grid(row = 1, column = 1, rowspan = 2, sticky="nsew")
        self.__lower_side_testing_frame.grid(row = 3, sticky="ew", columnspan = 2)
    
    def __hide_test_mode_widgets(self):
        self.__middle_side_testing_frame.grid_forget()
        self.__lower_side_testing_frame.grid_forget()
    
    def __hide_create_mode_widgets(self):
        self.__middle_side_batch_creating_frame.grid_forget()
        self.__middle_side_loaded_examples_frame.grid_forget()
        self.__lower_side_batch_creating_frame.grid_forget()
    
    def __show_create_mode_widgets(self):
        self.__middle_side_batch_creating_frame.grid(row = 1, column = 1, sticky="nsew")
        self.__middle_side_loaded_examples_frame.grid(row = 2, column = 1, sticky="nsew")
        self.__lower_side_batch_creating_frame.grid(row = 3, sticky="ew", columnspan = 2)
    
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
        self.__batch_create_text_box.delete('1.0', END)
        
    def clean_loaded_examples_text_box(self):
        self.__loaded_examples_text_box.config(state = "normal")
        self.__loaded_examples_text_box.delete('1.0', END)    
    
    def set_completed_test_feedback(self, completed = 0, total = 0):
        self.__completed_tests_label.config(text = "Tests completados: " + str(completed) + " de " + str(total))

    def change_to_test_mode(self):
        self.__batch_creating_mode_button.config(state = "normal")
        self.__test_text_box.config(state = "disabled")
        self.__testing_mode_button.config(text = "Cambiar ejemplos")
        self.__hide_create_mode_widgets()
        self.__show_test_mode_widgets()
    
    def change_to_create_mode(self):
        self.__batch_creating_mode_button.config(state = "disabled")
        self.__testing_mode_button.config(text = "Modo de Prueba")
        self.__hide_test_mode_widgets()
        self.__show_create_mode_widgets()
    
    def enable_mode_buttons(self):
        self.__testing_mode_button.config(state = "normal")
        self.__batch_creating_mode_button.config(state = "normal")
        self.__submit_knowledge_base_button.config(state = "disabled")
        