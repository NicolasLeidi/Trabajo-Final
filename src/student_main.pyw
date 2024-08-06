import tkinter as tk
from model.Model import Model
from presenter.StudentPresenter import StudentPresenter
from view.StudentView import StudentView

def main():
    root = tk.Tk()

    model = Model()
    presenter = StudentPresenter(model)
    view = StudentView(root, presenter)
    
    presenter.bind_view(view)
    model.bind_presenter(presenter)

    root.mainloop()

if __name__ == "__main__":
    main()