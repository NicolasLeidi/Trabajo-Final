import tkinter as tk
from model.Model import Model
from presenter.TeacherPresenter import TeacherPresenter
from view.TeacherView import TeacherView

def main():
    root = tk.Tk()

    model = Model()
    presenter = TeacherPresenter(model)
    view = TeacherView(root, presenter)
    
    presenter.bind_view(view)
    model.bind_presenter(presenter)

    root.mainloop()

if __name__ == "__main__":
    main()