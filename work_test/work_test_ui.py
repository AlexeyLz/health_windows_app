from tkinter import *

import texts
from login_page import login_logic
from styles import Colors
from work_test.work_test_logic import back, onFrameConfigure, QuestionOneLineCard, QuestionManyLinesCard, \
    QuestionWithOptionsCard


def test_main_page_frame(window):
    canvas = Canvas(window, borderwidth=0, bg=Colors.main_color)
    frame = Frame(window, width=900, height=680, bg=Colors.main_color)
    vsb = Scrollbar(window, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=vsb.set)

    vsb.pack(side="right", fill="y")
    Label(frame, bg=Colors.main_color, text='                    ').pack(side=LEFT)  # MOVING TO LEFT
    canvas.pack(side="right", fill="both", expand=True)
    canvas.create_window((4, 4), window=frame, anchor="nw")

    frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))

    def on_mousewheel(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    canvas.bind_all("<MouseWheel>", on_mousewheel)

    test_main_page(frame, window, canvas, vsb)


def test_main_page(test_frame, window, canvas, vsb):
    login_label = Label(test_frame, text=texts.info_test, height=7, bg=Colors.main_color,
                        fg=Colors.white,
                        font=('', 14, 'bold'))
    login_label.pack()

    button_border = Frame(test_frame, highlightbackground=Colors.white,
                          highlightthickness=2, bd=0, height=200)
    button_back = Button(button_border, font=('', 10), bd=0, text='Назад',
                         bg=Colors.main_color,
                         fg=Colors.white, activebackground=Colors.white,
                         activeforeground=Colors.main_color,
                         command=lambda: back(test_frame, window, canvas, vsb))
    button_back.pack()
    button_border.place(x=10, y=10)

    question = QuestionOneLineCard(test_frame, texts.TestWork.question_name)
    question.draw_card()

    question = QuestionOneLineCard(test_frame, texts.TestWork.question_birthday)
    question.draw_card()

    question = QuestionOneLineCard(test_frame, texts.TestWork.question_word)
    question.draw_card()

    question = QuestionOneLineCard(test_frame, texts.TestWork.question_exp)
    question.draw_card()

    # question = QuestionWithOptionsCard(test_frame, texts.TestWork.question_type_work, texts.TestWork.question_type_work_answers)
    # question.draw_card()
