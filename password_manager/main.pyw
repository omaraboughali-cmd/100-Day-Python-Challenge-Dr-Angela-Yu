import random
import string
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    # 1. Clear whatever is currently in the password entry box
    entry3.delete(0, tk.END)
    
    # 2. Define the character pools
    letters = string.ascii_letters  # a-z, A-Z
    digits = string.digits          # 0-9
    symbols = "!@#$%^&*()_+"        # Common symbols
    
    # 3. Create lists of random characters to guarantee a good mix
    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_digits = [random.choice(digits) for _ in range(random.randint(2, 4))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    
    # 4. Combine and shuffle them so the order isn't predictable
    password_list = password_letters + password_digits + password_symbols
    random.shuffle(password_list)
    
    # 5. Join the list into a single string
    generated_password = "".join(password_list)
    
    # 6. Insert it directly into your entry widget
    entry3.insert(0, generated_password)
    window.clipboard_clear()                       # 1. Clear whatever was previously copied
    window.clipboard_append(generated_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_credentials():
    # 1. Fetch the data from each entry box
    web_data = entry1.get()
    email_data = entry2.get()
    pass_data = entry3.get()

    if len(web_data) == 0 or len(email_data) == 0 or len(pass_data) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
        return
    else:
        # 3. Append the data to the text file
        with open("passwords.txt", "a", encoding="utf-8") as file:
            # Formats the line as: Website | Email | Password
            file.write(f"{web_data} | {email_data} | {pass_data}\n")
    # 4. Clear the entry fields for the next input (optional but helpful)
    entry1.delete(0, tk.END)
    entry3.delete(0, tk.END)
    messagebox.showinfo(title="Success", message="Credentials saved successfully!")


# ---------------------------- UI SETUP ------------------------------- #


import tkinter  as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from tkinter import messagebox
window = ThemedTk(theme="arc")
style = ttk.Style(window)
style.configure('TButton' , font=15)

window.title("Password Manager")
window.geometry("")
window.config(padx=30 , pady=20 , bg="white")
        

def focus_next(event, next_widget):
    # Moves the cursor/focus to the specified next widget
    next_widget.focus()
    return "break"


canvas = tk.Canvas(width=350 , height=200 , bg = "white" , highlightthickness=0)
photo = tk.PhotoImage(file="password_manager.png")
photo = photo.subsample(3,3)
canvas.create_image(90 ,100  , image = photo)
canvas.grid(column=1 , row=0  ,columnspan=3)
label1 = ttk.Label(window , text="Website " , font=10, background="white")
label1.grid(column=0 , row=1 , sticky='w', padx=5 , pady=5)
label2 = ttk.Label(window , text="Email or Username " , font=10, background="white")
label2.grid(column=0 , row=2 , sticky='w', padx=5 , pady=5)

label3 = ttk.Label(window , text="Password " , font=10, background="white")
label3.grid(column=0 , row=3 , sticky='w', padx=5 , pady=5)
entry1 = ttk.Entry(window ,width=35 , font=17)
entry1.grid(column=1, row=1, columnspan=2 , sticky='ew' , padx=5 , pady=5)
entry1.focus()
entry2 = ttk.Entry(window ,width=35 , font=17)
entry2.grid(column=1, row=2, columnspan=1 , sticky='ew' , padx=5 , pady=5)
entry2.insert(0,"email@provider.com")
entry3 = ttk.Entry(window ,width=5 , font=17)
entry3.grid(column=1, row=3, columnspan=1 , sticky='ew' , padx=5 , pady=5)
button1 = ttk.Button(window , text="Add", width=35 , command=save_credentials)
button1.grid(column=1 , row = 4 , columnspan=2 , padx=5 , pady=5 ,sticky="ew")

button2 = ttk.Button(window , text="Generate Password", width=20 , command= generate_password)
button2.grid(column=2, row = 3 , columnspan=1, padx=5 , pady=5, sticky="e" )

entry1.bind("<Return>", lambda event: focus_next(event, entry2))
entry2.bind("<Return>", lambda event: focus_next(event, entry3))
# Pressing Enter in the password entry triggers the save function
entry3.bind("<Return>", lambda event: save_credentials())
window.mainloop()