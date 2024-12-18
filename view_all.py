from tkinter import *

class View_All_Students:
    def __init__(self, student_list):
        self.student_list = student_list
    
    def show_list(self):
        student_info_str = ""
        for student in self.student_list:
            student_info_str += f"\nName: {student[0]}\nAge: {student[1]}\nID Number: {student[2]}\nEmail Address: {student[3]}\nPhone Number: {student[4]}\n"
        return student_info_str

    def list_ui(self, frame):
        # Create a container frame for centering the content
        container_frame = Frame(frame)
        container_frame.pack(expand=True, anchor="center", padx=50, pady=50)  # Adjust padding for centering

        # Create a frame for the Text widget and scrollbar inside the container
        text_frame = Frame(container_frame)
        text_frame.pack(expand=True, fill=BOTH, padx=20, pady=20)

        # Create a Text widget to display the student list
        text_widget = Text(text_frame, wrap=WORD, font=("Arial", 12))
        text_widget.insert(END, self.show_list())
        text_widget.config(state=DISABLED)  # Make it read-only
        text_widget.pack(side=LEFT, fill=BOTH, expand=True)

        # Add a vertical scrollbar to the Text widget
        scrollbar = Scrollbar(text_frame, command=text_widget.yview)
        text_widget.config(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=RIGHT, fill=Y)
