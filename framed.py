from tkinter import *
from PIL import ImageTk, Image
import os
from framed_functions import *

# Constants
NORM_BUTTON_COLOUR = "#0389ff"
CLICKED_BUTTON_COLOUR = "#79fcf8"
GUESSES_COLOUR = "#fc3d8d"
FONT = "serilic"
X_BUTTON_START = 284
PICTURE_DIRECTORY = os.path.dirname(os.path.realpath(__file__)) + "\images"

# Define window.
root = Tk()
root.title("Framed")
root.geometry("967x750")

# Define
#  List of images
image_dirs = os.listdir(PICTURE_DIRECTORY)
pictures = []
for img in image_dirs:
    pictures.append(ImageTk.PhotoImage(Image.open(PICTURE_DIRECTORY + "\\" + img)))

#  Label for display of images
img = ImageTk.PhotoImage(Image.open(PICTURE_DIRECTORY + "\\001.jpeg"))
img_label = Label(image=img)

#  Entry to enter movie name.
e = Entry(width=50, bd=4, font=FONT)

#  Buttons
button_1 = Button(text="1", bg=NORM_BUTTON_COLOUR, font=10, command=lambda: switch_img(0, img_label, pictures))
button_2 = Button(text="2", bg=NORM_BUTTON_COLOUR, font=10, command=lambda: switch_img(1, img_label, pictures))
button_3 = Button(text="3", bg=NORM_BUTTON_COLOUR, font=10, command=lambda: switch_img(2, img_label, pictures))
button_4 = Button(text="4", bg=NORM_BUTTON_COLOUR, font=10, command=lambda: switch_img(3, img_label, pictures))
button_5 = Button(text="5", bg=NORM_BUTTON_COLOUR, font=10, command=lambda: switch_img(4, img_label, pictures))
button_6 = Button(text="6", bg=NORM_BUTTON_COLOUR, font=10, command=lambda: switch_img(5, img_label, pictures))

button_submit = Button(text="Submit", bg=NORM_BUTTON_COLOUR, font=10, command=lambda: guess(buttons_list, 284,
                                                                                            img_label, pictures,
                                                                                            e, guesses_label,
                                                                                            button_submit))
buttons_list = [[button_2, 1], [button_3, 2], [button_4, 3], [button_5, 4], [button_6, 5]]

# Guesses left label
guesses_label = Label(text="You have 6 guesses left!", font=FONT, fg=GUESSES_COLOUR)


# Display
#  Label
img_label.grid(row=0, column=0, columnspan=3)

#  Entry
e.place(x=134, y=550, width=700, height=50)

#  Button
button_submit.place(x=845, y=550, width=80, height=50)
button_1.place(x=X_BUTTON_START, y=620, width=50, height=50)
x_button = X_BUTTON_START

# Guesses label
guesses_label.place(x=359, y=700, width=250, height=50)


root.mainloop()

