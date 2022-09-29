from tkinter import *
from tkinter import messagebox

import styles
import texts
from login_page.buttons_choose import choose_buttons, login_identifier_ui
from styles import Colors
from work_test import work_test_ui


def start_test(login_frame, window):
    login_frame.destroy()
    work_test_ui.test_main_page_frame(window)


def back_to_chose_buttons(login_frame, window):
    login_frame.destroy()
    print(1)
    choose_buttons(window)


def login_by_identifier(login_frame, window):
    login_frame.destroy()
    login_frame = Frame(window, width=700, height=680, bg=Colors.main_color)
    login_identifier_ui(login_frame, window)
    login_frame.pack()


def login_check(login, password, login_frame, window):
    login_data = login.get()
    password_data = password.get()
    # тут будет подключение
    if login_data == 'test@gmail.com' and password_data == 'test':
        login_frame.destroy()
        choose_buttons(window)
    else:
        messagebox.showinfo('Ошибка входа', 'Неверный логин или пароль')


def forgot_password():
    messagebox.showinfo('Забыл пароль?', 'Напишите на почту:\nhealthyemployer@gmail.com')
