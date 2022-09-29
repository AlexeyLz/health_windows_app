from tkinter import messagebox

import styles
import texts
from tkinter import *

from login_page import login_logic


def choose_buttons(window):
    login_frame = Frame(window, width=700, height=680, bg=styles.Colors.main_color)
    free_place = Label(login_frame, height=3, bg=styles.Colors.main_color)
    free_place.pack()

    button_border = Frame(login_frame, highlightbackground=styles.Colors.white,
                          highlightthickness=2, bd=0, height=200)
    button_test_start = Button(button_border, font=('', 15), bd=0, text='Пройти тестирование\nи получить идентификатор',
                               bg=styles.Colors.main_color,
                               fg=styles.Colors.white, activebackground=styles.Colors.white,
                               activeforeground=styles.Colors.main_color,
                               command=lambda: login_logic.start_test(login_frame, window))
    button_test_start.pack()
    button_border.pack()

    free_place = Label(login_frame, height=3, bg=styles.Colors.main_color)
    free_place.pack()

    button_border = Frame(login_frame, highlightbackground=styles.Colors.white,
                          highlightthickness=2, bd=0, height=200)
    button_login_by_id = Button(button_border, font=('', 15), bd=0, text='Войти по идентификатору',
                                bg=styles.Colors.main_color,
                                fg=styles.Colors.white, activebackground=styles.Colors.white,
                                activeforeground=styles.Colors.main_color,
                                command=lambda: login_logic.login_by_identifier(login_frame, window))
    button_login_by_id.pack()
    button_border.pack()

    free_place = Label(login_frame, height=3, bg=styles.Colors.main_color)
    free_place.pack()

    button_border = Frame(login_frame, highlightbackground=styles.Colors.white,
                          highlightthickness=2, bd=0, height=200)
    button_login_boss = Button(button_border, font=('', 15), bd=0, text='Войти как руководитель',
                               bg=styles.Colors.main_color,
                               fg=styles.Colors.white, activebackground=styles.Colors.white,
                               activeforeground=styles.Colors.main_color,
                               command=lambda: messagebox.showinfo("Недоступно", "В разработке"))
    button_login_boss.pack()
    button_border.pack()

    login_frame.pack()


def login_identifier_ui(login_frame, window):
    free_place = Label(login_frame, height=3, bg=styles.Colors.main_color)
    free_place.pack()
    login_label = Label(login_frame, text='Введите идентификатор', height=5, bg=styles.Colors.main_color,
                        fg=styles.Colors.white,
                        font=('', 10))
    login_label.pack()
    free_place = Label(login_frame, height=1, bg=styles.Colors.main_color)
    free_place.pack()
    login_entry = Entry(login_frame, font=('', 15), width=25, justify=CENTER)
    login_entry.pack()
    free_place = Label(login_frame, height=4, bg=styles.Colors.main_color)
    free_place.pack()
    button_border = Frame(login_frame, highlightbackground=styles.Colors.white,
                          highlightthickness=2, bd=0, height=200)
    button_login_accept = Button(button_border, font=('', 15), bd=0, text='Подтвердить вход',
                                 bg=styles.Colors.main_color,
                                 fg=styles.Colors.white, activebackground=styles.Colors.white,
                                 activeforeground=styles.Colors.main_color,
                                 command=lambda: messagebox.showinfo("Недоступно", "Идентификатор вход"))
    button_login_accept.pack()
    button_border.pack()

    free_place = Label(login_frame, height=4, bg=styles.Colors.main_color)
    free_place.pack()
    button_border = Frame(login_frame, highlightbackground=styles.Colors.white,
                          highlightthickness=2, bd=0, height=200)
    button_back = Button(button_border, font=('', 15), bd=0, text='Назад',
                         bg=styles.Colors.main_color,
                         fg=styles.Colors.white, activebackground=styles.Colors.white,
                         activeforeground=styles.Colors.main_color,
                         command=lambda: login_logic.back_to_chose_buttons(login_frame, window))
    button_back.pack()
    button_border.pack()
