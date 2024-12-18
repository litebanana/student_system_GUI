from tkinter import *
from functools import partial

class Main_Menu:
    def __init__(self, window):
        self.win = window
        self.menu_contain = Frame(self.win, borderwidth=1, bg="black", relief="sunken")
        self.menu_lbl = Label(self.menu_contain, text="Main Menu", font=("Century Gothic", 20), fg="white", bg="black", padx=20)
        self.btns = []
        self.btn_txt = ["View Profile", "View Others' Profiles", "View All Student Profiles", "Add New Student", "Logout"]
        self.funcs = []
        self.content_contain = Frame(self.win)

    def make_btns(self):
        for i, txt in enumerate(self.btn_txt):
            btn = Button(self.menu_contain, anchor="w", width=20, text=self.btn_txt[i], font=("Century Gothic", 14), padx=10, pady=15, bg="#FFFFFF")
            btn.config(command=partial(self.funcs[i]))
            self.btns.append(btn)

    def main_screen(self, frame):
        frame.pack_forget()
        self.menu_contain.pack(side = LEFT, anchor="w")
        self.menu_lbl.pack()
        for btn in self.btns:
            btn.pack()
        self.content_contain.pack(side = LEFT, expand = True)
