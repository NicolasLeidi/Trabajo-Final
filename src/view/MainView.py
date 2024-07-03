from tkinter import filedialog
from tkinter import * 
from tktooltip import ToolTip
from view.components.frames.BatchCreatingFrame import BatchCreatingFrame
from view.components.frames.HeaderFrame import HeaderFrame
from view.components.frames.KnowledgeBaseFrame import KnowledgeBaseFrame
from view.components.frames.ManualCreatingFrame import ManualCreatingFrame
from view.components.frames.TestingFrame import TestingFrame

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
        
        self.__upper_side_frame = HeaderFrame(root, bg="blue", width=800, height=50, pady=3, padx=10, functions=(self.__load_knowledge_base, self.__test_mode, self.__batch_create_mode, self.__manual_create_mode))
        self.__middle_side_knowledge_base_frame = KnowledgeBaseFrame(root, bg="red", width=320, pady=3, padx=5)
        self.__middle_side_testing_frame = TestingFrame(root, bg="pink", width=480, pady=3, padx=5)
        self.__middle_side_batch_creating_frame = BatchCreatingFrame(root, bg="orange", width=480, pady=3, padx=5)
        self.__middle_side_manual_creating_frame = ManualCreatingFrame(root, bg="yellow", width=480, pady=3, padx=5)
        self.__middle_side_loaded_examples_frame = Frame(root, bg="purple", width=480, pady=3, padx=5)
        self.__lower_side_testing_frame = Frame(root, bg="green", width=800, height=50, pady=3)
        self.__lower_side_batch_creating_frame = Frame(root, bg="cyan", width=800, height=50, pady=3)
        
        # Ubico los frames
        
        self.__upper_side_frame.grid(row = 0, stick="ew", columnspan = 2)
        self.__middle_side_knowledge_base_frame.grid(row = 1, column = 0, rowspan = 2, sticky="nsew")
        self.__middle_side_testing_frame.grid(row = 1, column = 1, rowspan = 2, sticky="nsew")
        
        # Configuro los frames
        
        
        self.__middle_side_loaded_examples_frame.grid_rowconfigure(0, weight=1)
        self.__middle_side_loaded_examples_frame.grid_columnconfigure(0, weight=1)
        
        self.__lower_side_testing_frame.grid_rowconfigure(0, weight=1)
        for i in range(6):
            self.__lower_side_testing_frame.grid_columnconfigure(i, weight=1)
        
        self.__lower_side_batch_creating_frame.grid_rowconfigure(0, weight=1)
        for i in range(3):
            self.__lower_side_batch_creating_frame.grid_columnconfigure(i, weight=1)
        
        # Widgets del frame intermedio
        
        loaded_examples_label = Label(self.__middle_side_loaded_examples_frame, text="Ejemplos Cargados")
        self.__loaded_examples_text_box = Text(self.__middle_side_loaded_examples_frame, height=15, width=65)
        
        # Widgets del frame inferior
        
        run_tests_button = Button(self.__lower_side_testing_frame, text="Correr", width=20, command=lambda: self.__test_solution())
        clean_tests_button = Button(self.__lower_side_testing_frame, text="Limpiar", width=20, command=lambda: self.__clean_tests())
        pop_test_button = Button(self.__lower_side_testing_frame, text="Remover", width=20, command=lambda: self.__pop_test())
        self.__completed_tests_label = Label(self.__lower_side_testing_frame, text="Tests completados: 0 de 0")
        
        ordered_checkbox = Checkbutton(self.__lower_side_batch_creating_frame, text="Sin Orden", variable= self.__ordered)
        first_only_checkbox = Checkbutton(self.__lower_side_batch_creating_frame, text="Primer Resultado", variable= self.__first_only)
        add_tests_button = Button(self.__lower_side_batch_creating_frame, text="Agregar", width=20, command=lambda: self.__add_example())
        save_tests_button = Button(self.__lower_side_batch_creating_frame, text="Guardar", width=20, command=lambda: self.__save_examples())
        clean_examples_button = Button(self.__lower_side_batch_creating_frame, text="Limpiar", width=20, command=lambda: self.__clean_examples())
        pop_examples_button = Button(self.__lower_side_batch_creating_frame, text="Deshacer", width=20, command=lambda: self.__pop_examples())
        
        # Configuro widgets del frame intermedio
        
        self.__middle_side_testing_frame.test_text_box.bind("<Button 1>", self.__handle_test_text_box_click)
        
        
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
        
        # Coloco widgets del frame intermedio
        
        loaded_examples_label.place(relheight=0.1, relwidth=1)
        self.__loaded_examples_text_box.place(rely=0.1, relheight=0.9, relwidth=1)
        
        # Coloco widgets del frame inferior
        
        run_tests_button.grid(row = 0, column = 1)
        clean_tests_button.grid(row = 0, column = 2)
        pop_test_button.grid(row = 0, column = 3)
        self.__completed_tests_label.grid(row = 0, column = 4)
        
        ordered_checkbox.grid(row = 0, column = 0, padx = 10)
        first_only_checkbox.grid(row = 0, column = 1, padx = 10)
        add_tests_button.grid(row = 0, column = 2, padx = 10)
        pop_examples_button.grid(row = 0, column = 3, padx = 10)
        clean_examples_button.grid(row = 1, column = 0, padx = 10)
        save_tests_button.grid(row = 1, column = 3, padx = 10)

    def __handle_test_text_box_click(self, event):
        self.presenter.handle_test_text_box_click(self.__middle_side_testing_frame.test_text_box, event)
    
    def __test_solution(self):
        self.presenter.run_examples()
    
    def __clean_tests(self):
        self.presenter.clean_tests()
    
    def __pop_test(self):
        self.presenter.pop_test()
        
    def __add_example(self):
        if self.presenter.is_batch_mode():
            if not self.__middle_side_batch_creating_frame.batch_create_text_box.compare("end-1c", "==", "1.0"): 
                self.presenter.add_batch_examples(self.__middle_side_batch_creating_frame.batch_create_text_box.get("1.0",'end'), self.__ordered.get(), self.__first_only.get())
        else:
            if self.presenter.is_manual_mode():
                if not self.__middle_side_manual_creating_frame.manual_create_query_text_box.compare("end-1c", "==", "1.0") and not self.__middle_side_manual_creating_frame.manual_create_expected_result_text_box.compare("end-1c", "==", "1.0"): 
                    self.presenter.add_manual_example(self.__middle_side_manual_creating_frame.manual_create_query_text_box.get("1.0",'end'), self.__middle_side_manual_creating_frame.manual_create_expected_result_text_box.get("1.0",'end'), self.__ordered.get(), self.__first_only.get())
    
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
        self.__lower_side_testing_frame.grid(row = 3, sticky="ew", columnspan = 5)
    
    def __hide_test_mode_widgets(self):
        self.__middle_side_testing_frame.grid_forget()
        self.__lower_side_testing_frame.grid_forget()
    
    def __hide_batch_create_mode_widgets(self):
        self.__middle_side_batch_creating_frame.grid_forget()
        self.__middle_side_loaded_examples_frame.grid_forget()
        self.__lower_side_batch_creating_frame.grid_forget()
    
    def __show_batch_create_mode_widgets(self):
        self.__middle_side_batch_creating_frame.grid(row = 1, column = 1, sticky="nsew")
        self.__middle_side_loaded_examples_frame.grid(row = 2, column = 1, sticky="nsew")
        self.__lower_side_batch_creating_frame.grid(row = 3, sticky="ew", columnspan = 2)
    
    def __hide_manual_create_mode_widgets(self):
        self.__middle_side_manual_creating_frame.grid_forget()
        self.__middle_side_loaded_examples_frame.grid_forget()
        self.__lower_side_batch_creating_frame.grid_forget()
    
    def __show_manual_create_mode_widgets(self):
        self.__middle_side_manual_creating_frame.grid(row = 1, column = 1, sticky="nsew")
        self.__middle_side_loaded_examples_frame.grid(row = 2, column = 1, sticky="nsew")
        self.__lower_side_batch_creating_frame.grid(row = 3, sticky="ew", columnspan = 2)
    
    def open_popup(self, type, message):
        popup = Tk()
        popup.wm_title(type)
        label = Label(popup, text=message)
        label.pack(side="top", fill="x", pady=10)
        ok_button = Button(popup, text="Ok", command=popup.destroy)
        ok_button.pack()
    
    def insert_example_to_test_text_box(self, text, tag = 0):
        line_number = self.__middle_side_testing_frame.test_text_box.index('end-1c').split('.')[0]
        line_number_to_str = str(line_number) + ".0"

        self.__middle_side_testing_frame.insert_test_text_box(text)
                
        # Coloreo una cantidad de lineas igual a la cantidad de lineas que ocupó la respuesta
        
        self.__middle_side_testing_frame.test_text_box.tag_add(tag, line_number_to_str, line_number_to_str + "+" + str(len(text.split("\n")) - 1) + "lines")
    
    def insert_example_to_loaded_examples_text_box(self, text):
        self.__loaded_examples_text_box.config(state = "normal")
        self.__loaded_examples_text_box.insert(END, text)
        self.__loaded_examples_text_box.config(state = "disabled")
    
    def insert_text_to_knowledge_base_text_box(self, text):
        self.__middle_side_knowledge_base_frame.insert_knowledge_base_text_box(text)
    
    def set_test_text_tag_color(self, tag, color):
        self.__middle_side_testing_frame.test_text_box.tag_config(tag, background = color)
    
    def clean_test_text_box(self):
        self.__middle_side_testing_frame.clean_test_text_box()
    
    def clean_create_text_box(self):
        self.__batch_create_text_box.delete('1.0', END)
        
    def clean_loaded_examples_text_box(self):
        self.__loaded_examples_text_box.config(state = "normal")
        self.__loaded_examples_text_box.delete('1.0', END)    
    
    def set_completed_test_feedback(self, completed = 0, total = 0):
        self.__completed_tests_label.config(text = "Tests completados: " + str(completed) + " de " + str(total))

    def change_to_test_mode(self):
        self.__upper_side_frame.batch_creating_mode_button.config(state = "disabled")
        self.__upper_side_frame.manual_creating_mode_button.config(state = "normal")
        self.__upper_side_frame.testing_mode_button.config(text = "Agregar Ejemplos")
        self.__hide_batch_create_mode_widgets()
        self.__hide_manual_create_mode_widgets()
        self.__show_test_mode_widgets()
    
    def change_to_batch_create_mode(self):
        self.__upper_side_frame.batch_creating_mode_button.config(state = "disabled")
        self.__upper_side_frame.manual_creating_mode_button.config(state = "normal")
        self.__upper_side_frame.testing_mode_button.config(text = "Modo de Prueba")
        self.__hide_test_mode_widgets()
        self.__hide_manual_create_mode_widgets()
        self.__show_batch_create_mode_widgets()
    
    def change_to_manual_create_mode(self):
        if self.presenter.is_batch_mode():
            self.__upper_side_frame.batch_creating_mode_button.config(state = "normal")
        self.__upper_side_frame.manual_creating_mode_button.config(state = "disabled")
        self.__upper_side_frame.testing_mode_button.config(text = "Modo de Prueba")
        self.__hide_test_mode_widgets()
        self.__hide_batch_create_mode_widgets()
        self.__show_manual_create_mode_widgets()
    
    def enable_mode_buttons(self):
        self.__upper_side_frame.testing_mode_button.config(state = "normal")
        self.__upper_side_frame.batch_creating_mode_button.config(state = "normal")
        self.__upper_side_frame.submit_knowledge_base_button.config(state = "disabled")
        