from tkinter import *
from PIL import ImageTk, Image
import os
import csv
import time

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

movie_lst = []
with open("movies.txt") as file:
    for row in file:
        movie_lst.append(row.replace("\n", ''))


def search(entry, listbox, scrollbar):

    global result
    result = []
    count = 0
    query = entry.get()

    if query != '':
        for i in movie_lst:
            if query.lower() in i.lower():
                result.append(i)

        if result:
            for n in range(len(result) - 1):

                if result[n].split()[0].lower().startswith(query.lower()):
                    result[count], result[n] = result[n], result[count]
                    count += 1

        result_var = StringVar()
        result_var.set(result)

        listbox['listvariable'] = result_var

        scrollbar.place(x=819, y=460, height=80, width=15)

        listbox.place(x=134, y=460, width=685, height=90)

    elif query == '':
        listbox.place(x=0, y=0, width=0)
        scrollbar.place(x=0, y=0, width=0)


def select_movie(entry, listbox):
    entry.delete(0, END)
    entry.insert(0, result[int(listbox.curselection()[0])])


def switch_img(index, image_label, lst, button, button_list):
    image_label.forget()
    image_label = Label(image=lst[index])
    image_label.place(x=80, y=15)
    for b in button_list:
        b["bg"] = NORM_BUTTON_COLOUR
    button["bg"] = CURRENT_BUTTON_COLOUR


def guess(button_list, image_label, img_list, entry, guess_label, submit_button, full_b_list, movie, listbox, scrollbar):

    guesses = len(button_list) + 1

    if button_list or entry.get().lower() == movie.lower():
        if entry.get().lower() == movie.lower():
            """guess_label = Label(text=f"You got it on the {NUMBERS_DICT[7 - guesses]} guess!", font=FONT, fg=GUESSES_COLOUR)
            guess_label.place(x=359, y=700, width=250, height=50)"""
            guess_label.config(text=f"You got it on the {NUMBERS_DICT[7 - guesses]} guess!")
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
            image_label.place(x=80, y=15)
            button_list.pop(0)
            guesses -= 1
            """guess_label = Label(text=f"You have {guesses} guesses left!", font=FONT, fg=GUESSES_COLOUR)
            guess_label.place(x=359, y=700, width=250, height=50)"""
            guess_label.config(text=f"You have {guesses} guesses left!")
            entry.delete(0, END)
    else:
        """guess_label = Label(text=f"The movie was \n{movie}", font=FONT, fg=GUESSES_COLOUR)
        guess_label.place(x=359, y=700, width=250, height=50)"""
        guess_label.config(text=f"The movie was \n{movie}")
        submit_button["state"] = DISABLED

    listbox.place(x=0, y=0, width=0)
    scrollbar.place(x=0, y=0, width=0)



