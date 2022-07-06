BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas
import random
import json
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("100-days-of-code/day 31/data/words_to_learn.csv")
except FileNotFoundError:
    orignial_data = pandas.read_csv("100-days-of-code/day 31/data/french_words.csv")
    to_learn = orignial_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")



def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    new_word = current_card["French"]
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_text, text=new_word, fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)

    # current_card = random.choice(to_learn)
    # new_word = current_card["French"]
    # canvas.itemconfig(card_title, text="French", fill="black")
    # canvas.itemconfig(card_text, text=new_word, fill="black")

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_text, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

def already_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("100-days-of-code/day 31/data/words_to_learn.csv", index=False)


    next_card()

window = Tk()
window.title("FlashCard")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="100-days-of-code/day 31/images/card_front.png")
card_back_img = PhotoImage(file="100-days-of-code/day 31/images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
card_text = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="100-days-of-code/day 31/images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="100-days-of-code/day 31/images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=already_known)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()
