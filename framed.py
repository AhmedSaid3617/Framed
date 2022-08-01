import random

from framed_functions import *

movie_index = 0
movies = []

def main():
    global movie_index
    with open("E:\Coding\PythonProjects\Framed\\sol.txt", newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            movies.append(row)
        if movie_index > len(movies):
            movie_index =0
        chosen_row = movies[movie_index]
        movie_index += 1

    PICTURE_DIRECTORY = os.path.dirname(os.path.realpath(__file__)) + f"\images\\{chosen_row[0]}"
    MOVIE_NAME = chosen_row[1]

    # Define window.
    global root
    root = Tk()
    root.title("Framed")
    root.geometry("967x750")

    # Define
    #  List of images
    image_dirs = os.listdir(PICTURE_DIRECTORY) # List of paths to images.
    pictures = [] # List of ImageTk objects.
    for img in image_dirs:
        pictures.append(ImageTk.PhotoImage(Image.open(PICTURE_DIRECTORY + "\\" + img)))

    #  Label for display of images
    img = ImageTk.PhotoImage(Image.open(PICTURE_DIRECTORY + "\\001.jpeg"))
    img_label = Label(image=img)

    #  Entry to enter movie name.
    e = Entry(width=50, bd=4, font=FONT)

    #  Buttons
    button_1 = Button(text="1", bg=CURRENT_BUTTON_COLOUR, activebackground=CLICKED_BUTTON_COLOUR, font=10,
                      command=lambda: switch_img(0, img_label, pictures, button_1, full_buttons_list))
    button_2 = Button(text="2", bg=NORM_BUTTON_COLOUR, activebackground=CLICKED_BUTTON_COLOUR, font=10,
                      command=lambda: switch_img(1, img_label, pictures, button_2, full_buttons_list))
    button_3 = Button(text="3", bg=NORM_BUTTON_COLOUR, activebackground=CLICKED_BUTTON_COLOUR, font=10,
                      command=lambda: switch_img(2, img_label, pictures, button_3, full_buttons_list))
    button_4 = Button(text="4", bg=NORM_BUTTON_COLOUR, activebackground=CLICKED_BUTTON_COLOUR, font=10,
                      command=lambda: switch_img(3, img_label, pictures, button_4, full_buttons_list))
    button_5 = Button(text="5", bg=NORM_BUTTON_COLOUR, activebackground=CLICKED_BUTTON_COLOUR, font=10,
                      command=lambda: switch_img(4, img_label, pictures, button_5, full_buttons_list))
    button_6 = Button(text="6", bg=NORM_BUTTON_COLOUR, activebackground=CLICKED_BUTTON_COLOUR, font=10,
                      command=lambda: switch_img(5, img_label, pictures, button_6, full_buttons_list))

    button_submit = Button(text="Submit", bg=NORM_BUTTON_COLOUR, font=10, activebackground=CLICKED_BUTTON_COLOUR,
                           command=lambda: guess(buttons_list,
                                                 img_label, pictures,
                                                 e, guesses_label,
                                                 button_submit, full_buttons_list, MOVIE_NAME))

    button_replay = Button(text="PLay Again", bg=NORM_BUTTON_COLOUR, font=10, activebackground=CLICKED_BUTTON_COLOUR,
                           command=lambda: [root.destroy(), main()])

    buttons_list = [[button_2, 1], [button_3, 2], [button_4, 3], [button_5, 4], [button_6, 5]]
    full_buttons_list = [button_1, button_2, button_3, button_4, button_5, button_6]

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
    button_replay.place(x=845, y=620, width=120, height=50)


    # Guesses label
    guesses_label.place(x=359, y=700, width=250, height=50)

    root.mainloop()


# Python program to use
# main for function call.
if __name__ == "__main__":
    main()



