import tkinter.constants
from tkinter import *
from PIL import ImageTk, Image
import os

CLICKED_BUTTON_COLOUR = "#79fcf8"
MOVIE_NAME = "Knives Out"
GUESSES_COLOUR = "#fc3d8d"
FONT = "serilic"

guesses = 6


def switch_img(index, image_label, lst):
    image_label.forget()
    image_label = Label(image=lst[index])
    image_label.grid(row=0, column=0, columnspan=3)


def guess(button_list, x_start, image_label, img_list, entry, guess_label, submit_button):
    global guesses
    if button_list:
        if entry.get().lower() == MOVIE_NAME.lower():
            guess_label = Label(text="Correct!", font=FONT, fg=GUESSES_COLOUR)
            guess_label.place(x=359, y=700, width=250, height=50)
            submit_button["state"] = DISABLED
            entry.delete(0, END)
            for i in button_list:
                i[0].place(x=x_start + i[1] * 70, y=620, width=50, height=50)
        else:
            button_list[0][0].place(x=x_start + button_list[0][1]*70, y=620, width=50, height=50)
            image_label.forget()
            image_label = Label(image=img_list[6 - len(button_list)])
            image_label.grid(row=0, column=0, columnspan=3)
            button_list.pop(0)
            guesses -= 1
            guess_label = Label(text=f"You have {guesses} guesses left!", font=FONT, fg=GUESSES_COLOUR)
            guess_label.place(x=359, y=700, width=250, height=50)
            entry.delete(0, END)
    else:
        guess_label = Label(text=f"The movie was \n{MOVIE_NAME}", font=FONT, fg=GUESSES_COLOUR)
        guess_label.place(x=359, y=700, width=250, height=50)



