import tkinter as tk
from tkinter import filedialog
from presenter.Presenter import TextPresenter

class MainView():
    
    def __init__(self, root, presenter):
        self.root = root
        self.presenter = presenter
        self.create_widgets()


    def create_widgets(self):
        self.root.title("Nombre a colocar")
        
        text_label = tk.Label(self.root, text="Ingrese la definición del predicado:")
        text_label.pack()

        text_entry = tk.Entry(self.root)
        text_entry.pack()
        
        submit_button = tk.Button(self.root, text="Submit", command=lambda: self.submit_prolog_predicate(text_entry))
        submit_button.pack()
        
        file_label = tk.Label(self.root, text="Ingrese la resolucion de prolog:")
        file_label.pack()

        prologResolution = tk.Text(self.root, state="disabled", height=10, width=50)
        prologResolution.pack()
        
        load_button = tk.Button(self.root, text="Load Text File", command=lambda: self.load_file(prologResolution))
        load_button.pack()
        
        query_label = tk.Label(self.root, text="Ingrese el query:")
        query_label.pack()

        query_entry = tk.Entry(self.root)
        query_entry.pack()
        
        query_response = tk.Text(self.root, state="disabled", height=3, width=30)
        
        query_button = tk.Button(self.root, text="Query", command=lambda: self.query_submit(query_entry, query_response))
        query_button.pack()
        
        query_response.pack()
        
    
    def submit_prolog_predicate(self, text_entry):
        self.presenter.submit_prolog_predicate(text_entry.get())
    
    def load_file(self, text_entry):
        text = self.presenter.load_text_file(filedialog.askopenfilename(filetypes=[("Prolog files", "*.pl")]))
        
        text_entry.configure(state="normal")
        text_entry.delete(1.0, tk.END)
        text_entry.insert(tk.END, text)
        text_entry.configure(state="disabled")
    
    def query_submit(self, query_entry, query_response):
        text = self.presenter.query(query_entry.get())
        
        query_response.configure(state="normal")
        query_response.delete(1.0, tk.END)
        query_response.insert(tk.END, text)
        query_response.configure(state="disabled")