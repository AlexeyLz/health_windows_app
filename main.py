import importlib
import os
from tkinter import *
from tkinter import messagebox

import styles
import texts
from styles import Colors, Paths
from login_page import login_ui


def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    title_bar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + title_bar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()


window = Tk()

window.geometry('900x800')
# window.iconbitmap(Paths.main_icon)
window.title('Healthy Employer')
window['bg'] = Colors.main_color
center(window)
login_frame = Frame(window, width=700, height=680, bg=Colors.main_color)
login_ui.login_widgets(login_frame, window)
login_frame.pack()
button_forgot = Button(window, font=('', 8), bd=0, text=texts.problem_text, bg=styles.Colors.main_color,
                       fg=styles.Colors.white, activebackground=styles.Colors.main_color,
                       activeforeground=styles.Colors.white,
                       command=lambda: messagebox.showinfo('Возникла проблема?',
                                                           'Напишите на почту:\nhealthyemployer@gmail.com'))
button_forgot.place(rely=1.0, relx=1.0, x=-1, y=-1, anchor=SE)

window.mainloop()
