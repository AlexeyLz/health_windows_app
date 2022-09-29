from tkinter import messagebox

import styles
import texts
from tkinter import *
from login_page import login_logic


def login_widgets(login_frame, window):
    greet_label = Label(login_frame, text=texts.greeting, height=5, bg=styles.Colors.main_color, fg=styles.Colors.white,
                        font=('', 15))
    greet_label.pack()
    login_label = Label(login_frame, text=texts.login_text, height=5, bg=styles.Colors.main_color,
                        fg=styles.Colors.white,
                        font=('', 10))
    login_label.pack()
    login_entry = Entry(login_frame, font=('', 15), width=25, justify=CENTER)
    login_entry.pack()

    password_label = Label(login_frame, text=texts.password_text, height=5, bg=styles.Colors.main_color,
                           fg=styles.Colors.white,
                           font=('', 10))
    password_label.pack()
    password_entry = Entry(login_frame, font=('', 15), width=25, justify=CENTER, show="*")
    password_entry.pack()

    free_place = Label(login_frame, height=2, bg=styles.Colors.main_color)
    free_place.pack()

    button_border = Frame(login_frame, highlightbackground=styles.Colors.white,
                          highlightthickness=2, bd=0, height=200)
    button_login = Button(button_border, font=('', 15), bd=0, text=texts.login_button, bg=styles.Colors.main_color,
                          fg=styles.Colors.white, activebackground=styles.Colors.white,
                          activeforeground=styles.Colors.main_color,
                          command=lambda: login_logic.login_check(login_entry, password_entry, login_frame, window))

    button_login.pack()
    button_border.pack()
    free_place = Label(login_frame, height=1, bg=styles.Colors.main_color)
    free_place.pack()
    button_forgot = Button(login_frame, font=('', 10), bd=0, text=texts.forgot_password, bg=styles.Colors.main_color,
                           fg=styles.Colors.white, activebackground=styles.Colors.main_color,
                           activeforeground=styles.Colors.white,
                           command=lambda: login_logic.forgot_password())
    button_forgot.pack()
