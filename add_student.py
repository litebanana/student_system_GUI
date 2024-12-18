from tkinter import *

class Add_Student:

    def __init__(self, student):
        self.student_data = student

    def write_student_info(self, name, age, id_num, email, phone_num):
        with open('student_data.txt', 'a') as file:
            file.write(f"{name}\t{age}\t{id_num}\t{email}\t{phone_num}\n")

    def add_student(self, name, age, id, email, phone, notification_label):
        student = [name, age, id, email, phone]
        self.student_data.student_list.append(student)
        print(f"Added Student {student[0]} to the list.")
        self.write_student_info(name, age, id, email, phone)

        # Update the notification label with the success message
        notification_label.config(text=f"Added Student {student[0]} to the list.", fg="green")

    def register(self, flds, notification_label):
        student = [fld.get() for fld in flds]
        self.add_student(*student, notification_label=notification_label)

    def register_ui(self, frame):
        # Create a container frame for centering the content
        container_frame = Frame(frame)
        container_frame.pack(expand=True, anchor="center", padx=50, pady=50)

        # Create labels and entry fields in the same row
        lbls = ['Name:', 'Age:', 'ID Number:', 'Email Address:', 'Phone Number:']
        flds = []

        # Create a grid layout for labels and fields, and center everything
        for i, txt in enumerate(lbls):
            # Create label with font size 20 and align it to the left
            label = Label(container_frame, text=txt, font=("Arial", 20))
            label.grid(row=i, column=0, padx=10, pady=5, sticky='w')

            # Create the entry field with font size 20 and align it to the left
            fld = Entry(container_frame, font=("Arial", 20))
            fld.grid(row=i, column=1, padx=10, pady=10, sticky='w')
            flds.append(fld)

        # Create and center the REGISTER button
        register_button = Button(container_frame, text="REGISTER", command=lambda: self.register(flds, notification_label), font=("Arial", 20))
        register_button.grid(row=len(lbls), column=0, columnspan=2, pady=10)

        # Create a label for notification (initially empty)
        notification_label = Label(container_frame, text="", font=("Arial", 16), fg="blue")
        notification_label.grid(row=len(lbls) + 1, column=0, columnspan=2, pady=10)

        # Ensure the container frame is centered
        container_frame.grid_columnconfigure(0, weight=1, uniform="equal")
        container_frame.grid_columnconfigure(1, weight=3, uniform="equal")

