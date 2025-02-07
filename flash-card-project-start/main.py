BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import random
# ---------------------------- LOADING & READING ------------------------------- #
import pandas
df = pandas.read_csv("words_to_learn.csv")
df.to_csv("to_learn_words.csv",index=False)
data = pandas.read_csv("to_learn_words.csv")
#data1 = pandas.read_csv("data/words_to_learn.csv")
french_to_english = {row['French']:row['English'] for (index,row) in data.iterrows()}
french = data['French'].tolist()
english = data['English'].tolist()
# ---------------------------- BUTTONS ------------------------------- #
def next_word(num):
    canvas.itemconfig(card,image=card_front)
    try:
        french_word = random.choice(list(french_to_english.keys()))
        english_word = french_to_english[french_word]
    except IndexError:
        canvas.itemconfig(ftext,text="you have successfully learnt all the words",font=("ariel", 20, "bold"))
        canvas.itemconfig(flanguage,text=" ")
    else:
        canvas.itemconfig(flanguage,text="spanish")
        canvas.itemconfig(ftext,text=f"{french_word}")
        window.after(3000,lambda : canvas.itemconfig(card,image=card_back))
        window.after(3000,lambda :canvas.itemconfig(flanguage,text="english"))
        window.after(3000, lambda: canvas.itemconfig(ftext, text=f"{english_word}"))
        if num==1:
            del french_to_english[french_word]
            new_data = pandas.DataFrame(french_to_english.items(), columns=["French", "English"])
            new_data.to_csv("to_learn_words.csv", index=False)
        if num==0:
            pass




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("FLASHY")
window.config(padx=70, bg=BACKGROUND_COLOR,highlightthickness=0)

canvas = Canvas(width=830, height=650, bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.pack()

card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card = canvas.create_image(425,275, image=card_front)

flanguage = canvas.create_text(425, 200, text="", font=("ariel", 45, "italic"))
ftext = canvas.create_text(425, 275, text="BEGIN", font=("ariel", 60, "bold"))
#elanguage = canvas.create_text(425,200,text="",font=("ariel",45,"italic"))
#etext = canvas.create_text(425,275,text="",font=("ariel",50,"italic"))


right = PhotoImage(file="images/right.png")
know_button = Button(window, image=right,borderwidth=0,command=lambda:next_word(1))
know_button.place(x=575,y=535)
know_button.config(highlightthickness=0)

wrong = PhotoImage(file="images/wrong.png")
unknown_button = Button(window, image=wrong,borderwidth=0,command=lambda:next_word(0))
unknown_button.place(x=160,y=535)
unknown_button.config(highlightthickness=0)







window.mainloop()


