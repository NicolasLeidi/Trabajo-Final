from tkinter import *
from tktooltip import ToolTip

class TestingFrame(Frame):

    def __init__(self, master, functions, *args, **kwargs):
        super(TestingFrame, self).__init__(master, *args, **kwargs)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.__create_widgets(functions)
    
    def __create_widgets(self, functions):
        self.test_label = Label(self, text="Batería de Tests")
        self.test_text_box = Text(self)
        
        ToolTip(self.test_text_box, msg="Batería de test cargada actualmente, la cual será ejecutada al presionar Correr.", delay=1.0)
        self.test_text_box.config(state = "disabled")
        self.test_text_box.bind("<Button 1>", lambda event, function=functions: self.__handle_test_text_box_click(function, event))
        
        self.test_label.place(relheight=0.05, relwidth=1)
        self.test_text_box.place(rely=0.05, relheight=0.95, relwidth=1)
    
    def __handle_test_text_box_click(self, function, event):
        line = int(self.test_text_box.index(f"@{event.x},{event.y}").split(".")[0])
        
        # Check if the selected line is empty
        selected_line_text = self.test_text_box.get(f"{line}.0", f"{line}.end").strip()
        if selected_line_text == "":
            return False
        
        start_line, end_line = self.__find_section_boundaries(line)
        section_number = self.__calculate_section_number(start_line)
        
        self.__highlight_section(start_line, end_line)
        function(section_number)

    def __find_section_boundaries(self, line):
        start_line = line
        end_line = line

        # Move up to find the start of the section
        while start_line > 1:
            previous_line_text = self.test_text_box.get(f"{start_line-1}.0", f"{start_line-1}.end")
            if previous_line_text.strip() == "":
                break
            start_line -= 1

        # Move down to find the end of the section (empty line or end of the text)
        while end_line < int(self.test_text_box.index("end-1c").split(".")[0]):
            next_line_text = self.test_text_box.get(f"{end_line+1}.0", f"{end_line+1}.end")
            if next_line_text.strip() == "":
                break
            end_line += 1

        return start_line, end_line
    
    def __calculate_section_number(self, start_line):
        section_number = 1
        current_line = 1
        
        while current_line < start_line:
            line_text = self.test_text_box.get(f"{current_line}.0", f"{current_line}.end").strip()
            if line_text == "":
                section_number += 1
            current_line += 1
        
        return section_number
    
    def __highlight_section(self, start_line, end_line):
        self.test_text_box.tag_remove("highlight", "1.0", "end")
        self.test_text_box.tag_add("highlight", f"{start_line}.0", f"{end_line}.end")
        self.test_text_box.tag_config("highlight", background="yellow")
        
    def insert_test_text_box(self, text):
        """
        Inserts the given text into the test text box.

        Parameters:
            text (str): The text to be inserted.
        """
        self.test_text_box.config(state = "normal")
        self.test_text_box.insert(END, text)
        self.test_text_box.config(state = "disabled")
    
    def clean_test_text_box(self):
        """
        Cleans the test text box of the testing frame.
        """
        self.test_text_box.config(state = "normal")
        self.test_text_box.delete('1.0', END)
        self.test_text_box.config(state = "disabled")