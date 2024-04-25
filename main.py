import tkinter as tk
from model.Model import Model
from view.MainView import MainView
from presenter.Presenter import TextPresenter

def main():
    # Initialize Tkinter root window
    root = tk.Tk()
    root.title("Text Editor")

    # Initialize Model, View, and Presenter
    model = Model()
    presenter = TextPresenter(model)
    view = MainView(root, presenter)
    
    presenter.bind_view(view)
    model.bind_presenter(presenter)

    # Start the Tkinter application loop
    root.mainloop()

if __name__ == "__main__":
    main()