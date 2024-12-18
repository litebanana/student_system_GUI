from student import Student_Info
from search_student import Search_Student
from view_all import View_All_Students
from add_student import Add_Student

from main_menu import Main_Menu
from tkinter import *
from functools import partial

win = Tk()
win.geometry(f"1280x800+{(win.winfo_screenwidth() - 1280)//2}+{(win.winfo_screenheight() - 800)//2}")
win.configure(background="gray")  # Set the background color of the main window

# Initialize components
stu = Student_Info()
addstud = Add_Student(stu)
search = Search_Student(stu.student_list)
view = View_All_Students(stu.student_list)
main = Main_Menu(win)
stu.read_student_info()

def login_check():
    global strikes
    if search.student_exists(stu_id.get()):
        main.main_screen(login_fr)
    else:
        strikes -= 1
        strikes_lbl.config(text=f"Invalid Student ID. You have {strikes} attempt/s remaining.")
    if strikes == 0:
        win.destroy()

# Login frame
login_fr = Frame(win, bg="gray")  # Set background color for login frame
login_lbl = Label(login_fr, text="Welcome! \nLogin to Continue.:)", font=("Arial", 50), bg="gray", fg="white")
stu_id = Entry(login_fr, font=("Arial", 70))
login_btn = Button(login_fr, text="Login", font=("Arial", 20), command=login_check)
strikes_lbl = Label(login_fr, text="", bg="gray", fg="red")
strikes = 4

def clear(): 
    for widget in main.content_contain.winfo_children():
        widget.destroy()

def search_for(student_id):
    clear()
    if search.student_exists(student_id):
        Label(main.content_contain, text=f"{search.student_profile(student_id)}", font=("Arial", 20), bg="gray", fg="white").pack(side=LEFT, expand=True)
    else:
        Label(main.content_contain, text="Student does not exist", bg="gray", fg="red").pack(side=LEFT)

def search_student():
    clear()
    id_entry = Entry(main.content_contain)
    id_entry.pack()
    Button(main.content_contain, text="Search", command=lambda: search_for(id_entry.get())).pack(side=LEFT)

def login():
    login_fr.pack(expand=True)
    login_lbl.pack()
    strikes_lbl.pack()
    stu_id.pack()
    login_btn.pack()

def func1():
    clear()
    search.search_ui(main.content_contain, stu_id.get())

def func2():
    clear()
    search_student()

def func3():
    clear()
    view.list_ui(main.content_contain)

def func4():
    clear()
    addstud.register_ui(main.content_contain)

def func5():
    clear()
    global strikes
    strikes = 4
    strikes_lbl.config(text="")
    stu_id.delete(0, END)
    main.menu_contain.pack_forget()
    main.content_contain.pack_forget()
    login()

main.funcs.extend([func1, func2, func3, func4, func5])

main.make_btns()

login()

win.mainloop()
