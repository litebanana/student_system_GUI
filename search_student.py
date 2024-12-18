from tkinter import *

class Search_Student:
    def __init__(self, student_list):
        self.student_list = student_list
    
    def student_profile(self, id):    
        for student in self.student_list:
            if student[2] == id:
                return f"\nName: {student[0]}\nAge: {student[1]}\nID Number: {student[2]}\nEmail Address: {student[3]}\nPhone Number: {student[4]}"
        return f"Student with ID {id} not found."
    
    def student_exists(self, id):
        for student in self.student_list:
            if student[2] == id:
                return True
        return False
    
    def search_ui(self, frame, id):
        # Create a label with the student profile and center it
        profile_text = self.student_profile(id)
        label = Label(frame, text=profile_text, font=("Arial", 70), justify=LEFT)
        label.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

        # Make the frame expand and center the content
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)
