import tkinter
from tkinter import *
from tkinter import ttk, messagebox

from login_page.buttons_choose import choose_buttons
from styles import Colors


class QuestionOneLineCard:
    def __init__(self, frame, text_question):
        self.text_question = text_question
        self.frame = frame
        self.label = Label(self.frame, text=str(text_question) + ':', height=3, bg=Colors.main_color,
                           fg=Colors.white,
                           font=('', 15))
        self.entry = Entry(self.frame, font=('', 15), width=25, justify=CENTER)
        self.free_place = Label(self.frame, height=1, bg=Colors.main_color)

    def draw_card(self):
        self.label.pack()
        self.entry.pack()
        self.free_place.pack()


class QuestionManyLinesCard:
    def __init__(self, frame, text_question):
        self.text_question = text_question
        self.frame = frame
        self.label = Label(self.frame, text=str(text_question) + ':', height=3, bg=Colors.main_color,
                           fg=Colors.white,
                           font=('', 15))
        self.text = Text(self.frame, width=20, height=10)
        self.free_place = Label(self.frame, height=1, bg=Colors.main_color)

    def draw_card(self):
        self.label.pack()
        self.text.pack()
        self.free_place.pack()


class QuestionWithOptionsCard:
    def __init__(self, frame, text_question, answer_variants):
        self.text_question = text_question
        self.frame = frame
        self.label = Label(self.frame, text=str(text_question) + ':', height=3, bg=Colors.main_color,
                           fg=Colors.white,
                           font=('', 15))
        self.label_answer = Label(self.frame, text=str(answer_variants), bg=Colors.main_color,
                                  fg=Colors.white,
                                  font=('', 10))

        self.entry = Entry(self.frame, font=('', 15), width=5, justify=CENTER, validate='key')
        self.entry['validatecommand'] = (self.entry.register(self.validate), '%P', '%d')
        self.free_place = Label(self.frame, height=1, bg=Colors.main_color)

    def validate(self, inStr, acttyp):
        if acttyp == '1':
            if not inStr.isdigit():
                messagebox.showinfo('Ошибка', 'Введите цифру ответа')
                return False
        if len(inStr) == 1:
            print(3)
            return True
        else:
            print(2)
            self.entry.delete(0, END)

    def draw_card(self):
        self.label.pack()
        self.label_answer.pack()
        self.entry.pack()
        self.free_place.pack()


def back(test_frame, window, canvas, vsb):
    test_frame.destroy()
    canvas.unbind_all("<MouseWheel>")
    canvas.destroy()
    vsb.destroy()

    choose_buttons(window)


def onFrameConfigure(canvas):
    canvas.configure(scrollregion=canvas.bbox("all"))
