import random
from tkinter import *

import pandas
import pandas as pd

win = Tk()
win.title("Flash Card App")
win.config(padx=50, pady=50, background="#B1DDC6")
canvas = Canvas(width=850, height=576, background="#B1DDC6", highlightthickness=0)
img = PhotoImage(file="card_front.png")
img2 = PhotoImage(file="card_back.png")
img_container = canvas.create_image(425, 288, image=img)
canvas.grid(column=1, row=0, columnspan=2)
# Flip card function
data = pd.read_csv("translate1.csv")
to_learn = data.to_dict(orient='records')

word = dict(data.sample())
print(word["Tagalog"].to_string())
guessed_list = []

def change_photo():
    canvas.itemconfig(img_container, image=img2)
    canvas.itemconfig(lang_text, text="Tagalog")
    canvas.itemconfig(word_text, text=word["Tagalog"].to_string(index=False))


def generate_new():
    global word
    guessed_list.append(word)
    canvas.itemconfig(img_container, image=img)
    word = data.sample()
    canvas.itemconfig(lang_text, text="Ilonggo")
    canvas.itemconfig(word_text, text=word["Ilonggo"].to_string(index=False))
    check_button.config(state="normal")
    win.after(5000, func=change_photo)


def next_word():
    global word
    to_learn.remove(word)
    word = data.sample()
    canvas.itemconfig(lang_text, text="Ilonggo")
    canvas.itemconfig(word_text, text=word["Ilonggo"].to_string(index=False))
    win.after(5000, func=change_photo)


lang_text = canvas.create_text(425, 150, text="Ilonggo", fill="black", font=("Arial", 40, "italic"))
word_text = canvas.create_text(425, 253, text=word["Ilonggo"].to_string(index=False), fill="black",
                               font=("Arial", 60, "bold"))
win.after(5000, func=change_photo)

check_img = PhotoImage(file="right.png")
check_button = Button(image=check_img, highlightthickness=0, borderwidth=0, command=generate_new)
check_button.grid(column=2, row=1)

wrong_img = PhotoImage(file="wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, borderwidth=0, command=next_word)
wrong_button.grid(row=1, column=1)

win.mainloop()
