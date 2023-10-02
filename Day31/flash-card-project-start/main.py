BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas as pd
import random 
import time

try:
    data = pd.read_csv("Day31/flash-card-project-start/data/to_learn.csv")
except:
    data = pd.read_csv("Day31/flash-card-project-start/data/french_words.csv")    
learn = data.to_dict(orient="records")
words = {}

def unknown_button_function(): 
    global words, flip_timer
    window.after_cancel(flip_timer)
    words = random.choice(learn)
    canvas.itemconfig(Title, text = 'French', fill = "black")
    canvas.itemconfig(word, text = words['French'], fill = "black")
    canvas.itemconfig(card_front, image=card_front_page)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(Title, text = 'English', fill = "white")
    canvas.itemconfig(word, text = words['English'], fill = "white")
    canvas.itemconfig(card_front, image=card_back_page)

def is_known():
    learn.remove(words)
    data = pd.DataFrame(learn)
    data.to_csv('Day31/flash-card-project-start/data/to_learn.csv', index=False)
    unknown_button_function()

window = Tk()
window.title("Flash card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_page = PhotoImage(file="Day31/flash-card-project-start/images/card_front.png")
card_back_page = PhotoImage(file="Day31/flash-card-project-start/images/card_back.png")
card_front = canvas.create_image(400, 263, image=card_front_page)
Title = canvas.create_text(400, 150, text='', font=("Arial",40,"italic"))
word = canvas.create_text(400, 263, text="", font=("Arial",60,"bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file="Day31/flash-card-project-start/images/wrong.png")
unknown_button = Button(image=wrong_image, highlightthickness=0, command=unknown_button_function)
unknown_button.grid(row=1, column=0)

right_image = PhotoImage(file="Day31/flash-card-project-start/images/right.png")
known_button = Button(image=right_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

unknown_button_function()

window.mainloop()