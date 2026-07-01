import tkinter as tk
from ttkthemes import ThemedTk
import pandas
import random




# Assuming your CSV is in the 'data' folder
data = pandas.read_csv("data/french_words.csv") 
# df = pandas.DataFrame(data)
# dic = df.to_dict(orient="records")
# df.to_csv("words_to_learn.csv" , index=False)
# words_to_learn = pandas.read_csv("words_to_learn")
new_data = data.to_dict(orient="records") 
# print(new_data)

current_card = random.choice(new_data)

BACKGROUND_COLOR = "#B1DDC6"
flip_timer = None
def next_card():
    global current_card , flip_timer
    if flip_timer is not None:
        window.after_cancel(flip_timer)

    try:
        current_card = random.choice(new_data)
        canvas.itemconfig(photo ,image = photo1)
        canvas.itemconfig(card_title , text = "French" , fill = "black")
        canvas.itemconfig(card_word , text = current_card['French'], fill = "black")    
    
        flip_timer = window.after(3000, flip_card)
    except IndexError:
        canvas.itemconfig(photo ,image = photo1)
        canvas.itemconfig(card_title , text = "Done" , fill = "black")
        canvas.itemconfig(card_word , text = "all words guessed", fill = "black")



def next_card_done():
    global current_card , flip_timer
    if flip_timer is not None:
        window.after_cancel(flip_timer)
    try:
        current_card = random.choice(new_data)
        canvas.itemconfig(photo ,image = photo1)
        canvas.itemconfig(card_title , text = "French" , fill = "black")
        canvas.itemconfig(card_word , text = current_card['French'], fill = "black")    
        new_data.remove(current_card)
        data = pandas.DataFrame(new_data)
        data.to_csv("words_to_learn.csv", index=False)
        flip_timer = window.after(3000, flip_card)
    except IndexError:
        canvas.itemconfig(photo ,image = photo1)
        canvas.itemconfig(card_title , text = "Done" , fill = "black")
        canvas.itemconfig(card_word , text = "all words guessed", fill = "black")


def flip_card():
    global current_card
    canvas.itemconfig(photo ,image = photo2)
    
    canvas.itemconfig(card_title , text = "English", fill = "white")
    
    canvas.itemconfig(card_word , text = current_card['English'] ,fill = "white")















window = ThemedTk(theme="arc")
window.title("Flashy")

# --- Full screen mode ---
window.state('zoomed') 

window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# 1. Load the image
photo1 = tk.PhotoImage(file="images/card_front.png")
photo2 = tk.PhotoImage(file="images/card_back.png")
# 2. Canvas setup
canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
photo = canvas.create_image(400, 263, image=photo1)
canvas.grid(column=0, row=0, columnspan=2)


card_title = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text = current_card['French'], font=("Ariel", 60, "bold"))

# 3. Buttons
wrong_img = tk.PhotoImage(file="images/wrong.png")
button_wrong = tk.Button(image=wrong_img, highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0 , command=next_card)
# Increased padx from 100 to 200
button_wrong.grid(row=1, column=0, pady=20, padx=200, sticky="e")

right_img = tk.PhotoImage(file="images/right.png")
button_right = tk.Button(image=right_img, highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0, command=next_card_done)
# Increased padx from 100 to 200
button_right.grid(row=1, column=1, pady=20, padx=200, sticky="w")

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
flip_timer = window.after(3000, flip_card)
window.mainloop()