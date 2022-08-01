from tkinter import *
from PIL import ImageTk, Image
import os
import random
import csv


movie_dirs = os.listdir(os.path.dirname(os.path.realpath(__file__)) + "\images")

# Constants
NORM_BUTTON_COLOUR = "#0342ff"
CLICKED_BUTTON_COLOUR = "#03ffee"
CURRENT_BUTTON_COLOUR = "#03c4ff"
GUESSES_COLOUR = "#fc3d8d"
FONT = "serilic"
X_BUTTON_START = 284


NUMBERS_DICT = {
    1: "first",
    2: "second",
    3: "third",
    4: "fourth",
    5: "fifth",
    6: "sixth"
}

guesses = 6


def switch_img(index, image_label, lst, button, button_list):
    image_label.forget()
    image_label = Label(image=lst[index])
    image_label.grid(row=0, column=0, columnspan=3)
    for b in button_list:
        b["bg"] = NORM_BUTTON_COLOUR
    button["bg"] = CURRENT_BUTTON_COLOUR


def guess(button_list, image_label, img_list, entry, guess_label, submit_button, full_b_list, movie):
    global guesses
    if button_list or entry.get().lower() == movie.lower():
        if entry.get().lower() == movie.lower():
            guess_label = Label(text=f"You got it on the {NUMBERS_DICT[7 - guesses]} guess!", font=FONT, fg=GUESSES_COLOUR)
            guess_label.place(x=359, y=700, width=250, height=50)
            submit_button["state"] = DISABLED
            entry.delete(0, END)
            for i in button_list:
                i[0].place(x=X_BUTTON_START + i[1] * 70, y=620, width=50, height=50)
        else:
            for b in full_b_list:
                b["bg"] = NORM_BUTTON_COLOUR
            button_list[0][0]["bg"] = CURRENT_BUTTON_COLOUR
            button_list[0][0].place(x=X_BUTTON_START + button_list[0][1]*70, y=620, width=50, height=50)
            image_label.forget()
            image_label = Label(image=img_list[6 - len(button_list)])
            image_label.grid(row=0, column=0, columnspan=3)
            button_list.pop(0)
            guesses -= 1
            guess_label = Label(text=f"You have {guesses} guesses left!", font=FONT, fg=GUESSES_COLOUR)
            guess_label.place(x=359, y=700, width=250, height=50)
            entry.delete(0, END)
    else:
        guess_label = Label(text=f"The movie was \n{movie}", font=FONT, fg=GUESSES_COLOUR)
        guess_label.place(x=359, y=700, width=250, height=50)
        submit_button["state"] = DISABLED



