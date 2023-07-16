import tkinter as tk
from tkinter import ttk
from pygame import mixer
import pygame
import os
GREY = "#262626"
HIGHLIGHTED_GREY = "#3b3f40"

ORANGE = "#e86b05"
HIGHLIGHTED_ORANGE = "#3b3f40"

GREEN = "#02f713"
RED = "#f70b02"

pygame.mixer.init()
mixer.music.load(f'{os.path.dirname(__file__)}/Sounds/Tic.mp3')
mixer.music.play(-1)


def outer_btn_func(index):
    def btn_func():
        current_btn = button_list[index]
        values_dict = {"X Turn": (GREEN, "X", "O Turn"),
                       "O Turn": (RED, "O", "X Turn")}

        current_tuple_from_dict = values_dict[label_var.get()]

        current_btn["background"] = current_tuple_from_dict[0]
        current_btn["text"] = current_tuple_from_dict[1]
        current_btn["state"] = "disabled"
        label_var.set(current_tuple_from_dict[2])
        win()
    return btn_func


def win():
    some_one_has_won = False
    if not some_one_has_won:
        for i in (0, 3, 6):
            condition_win = button_list[0 + i]["text"] == \
                button_list[1 + i]["text"] == button_list[2 + i]["text"]
            if condition_win and button_list[0 + i]["text"] != "":
                if button_list[0 + i]["text"] == "X":
                    finale_win("X")
                    some_one_has_won = True
                    break
                else:
                    finale_win("O")
                    some_one_has_won = True
                    break
    if not some_one_has_won:
        for i in (0, 1, 2):
            condition_win = button_list[0 + i]["text"] == \
                button_list[3 + i]["text"] == button_list[6 + i]["text"]
            if condition_win and button_list[0 + i]["text"] != "":
                if button_list[0 + i]["text"] == "X":
                    finale_win("X")
                    some_one_has_won = True
                    break
                else:
                    finale_win("O")
                    some_one_has_won = True
                    break
    if not some_one_has_won:
        for i in (0, 2):
            condition_win = button_list[0 + i]["text"] == \
                button_list[4]["text"] == button_list[8 - i]["text"]
            if condition_win and button_list[4]["text"] != "":
                if button_list[4]["text"] == "X":
                    finale_win("X")
                    some_one_has_won = True
                    break
                else:
                    finale_win("O")
                    some_one_has_won = True
                    break
    if not some_one_has_won:
        all_buttons_has_been_pressed = True
        for item in button_list:
            if item["text"] == "":
                all_buttons_has_been_pressed = False
        if all_buttons_has_been_pressed:
            label_var.set("Tie")
            for i in button_list:
                i["state"] = "disable"


def finale_win(winner):
    for item in button_list:
        item["state"] = "disable"
        label_var.set(f"{winner} Won")

# yes
def reset_func():
    label_var.set("X Turn")
    for item in button_list:
        item["text"] = ""
        item["background"] = GREY
        item["activebackground"] = HIGHLIGHTED_GREY
        item["state"] = "normal"


window = tk.Tk()
window.geometry("450x600")
window.title("Tic Tac Toe")
window.resizable(False, False)
window.config(bg="#595958")

label_var = tk.StringVar(value="X Turn")

label = tk.Label(window, textvariable=label_var,
                 bg="#572424", font=("Batang", 23))

button_list = []

for index in range(9):
    btn = tk.Button(
        window,
        text="",
        command=outer_btn_func(index),
        background=GREY,
        font=(23),
        borderwidth=10,
        activebackground=HIGHLIGHTED_GREY)

    button_list.append(btn)


reset_btn = tk.Button(
    window,
    text="Replay",
    command=reset_func,
    background=ORANGE,
    activebackground=HIGHLIGHTED_ORANGE,
    border=10)


label.place(relx=0, rely=0, relwidth=1, relheight=0.125)

for_loop_index = 0
for y_value in (0.125, 0.375, 0.625):
    for x_value in (0, 1/3, 2/3):
        current_button = button_list[for_loop_index]
        current_button.place(relx=x_value, rely=y_value, relwidth=1/3, relheight=0.25)
        for_loop_index += 1
del for_loop_index

reset_btn.place(relx=1/3, rely=7/8, relwidth=1/3, relheight=1/8)

window.bind("<Escape>", lambda event: window.quit())

window.mainloop()
