from tkinter import *
import pandas as pd
import random


BACKGROUND_COLOR = "#B1DDC6"

data = None


def read_data():
    global data
    try:
        df = pd.read_csv("data/words_to_learn.csv")
    except FileNotFoundError:
        df = pd.read_csv("data/french_words.csv")
    finally:
        data = df.to_dict(orient="records")


current_card = None


def get_random():
    return random.choice(data)


def right_guess():
    global current_card
    window.after_cancel(flip)
    data.remove(current_card)
    df = pd.DataFrame(data)
    df.to_csv('data/words_to_learn.csv',index=False)
    next_card()


def next_card():
    global current_card
    canvas.itemconfig(card_image, image=card_front)
    canvas.itemconfig(lang, text="French",fill="black")
    current_card = get_random()
    new_word = current_card['French']
    canvas.itemconfigure(word, text=new_word,fill="#000")
    window.after(5000, flip_card)


def flip_card():
    cur = current_card['English']
    canvas.itemconfig(card_image, image=card_back)
    canvas.itemconfig(lang, text="English",fill="white")
    canvas.itemconfig(word,text = cur,fill="white")


read_data()


window = Tk()
window.title("FlashCard - Learn French")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")
img_right = PhotoImage(file="images/right.png")
img_wrong = PhotoImage(file="images/wrong.png")


canvas = Canvas(width=800,height=526, highlightthickness=0,bg=BACKGROUND_COLOR)
card_image = canvas.create_image(400,263,image=card_front,)
canvas.grid(row=0,column=0,columnspan=2)

lang = canvas.create_text(400,150,text="",font=("Arial", 40, "italic"))
word = canvas.create_text(400,263,text="",font=("Arial", 60, "bold"))


flip = window.after(5000,flip_card)

right = Button(image=img_right, highlightthickness=0,command=right_guess)
right.grid(row=1,column=1)
wrong = Button(image=img_wrong, highlightthickness=0,command=next_card)
wrong.grid(row=1,column=0)

next_card()


window.mainloop()