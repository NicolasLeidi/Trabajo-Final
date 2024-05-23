import tkinter as tk
from model.Model import Model
from view.MainView import MainView
from presenter.Presenter import AppPresenter

def main():
    root = tk.Tk()

    model = Model()
    presenter = AppPresenter(model)
    view = MainView(root, presenter)
    
    presenter.bind_view(view)
    model.bind_presenter(presenter)

    root.mainloop()

if __name__ == "__main__":
    main()