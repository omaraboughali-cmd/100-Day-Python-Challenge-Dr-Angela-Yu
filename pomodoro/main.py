
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
            label.config(text="Work" , font=(FONT_NAME , 40 , "bold") ,foreground=GREEN , background="#FDECF2")
            countdown(work_sec)
    elif reps == 8:
            label.config(text="Long Break" , font=(FONT_NAME , 40 , "bold") ,foreground=GREEN , background="#FDECF2")
            countdown(long_break_sec)
    elif reps == 2 or reps == 4 or reps == 6:
            label.config(text="Short Break" , font=(FONT_NAME , 40 , "bold") ,foreground=GREEN , background="#FDECF2")
            countdown(short_break_sec)

def reset():
    global reps
    global timer
    window.after_cancel(timer)
    reps = 0
    check.config(text="" , foreground= GREEN ,background="#FDECF2")
    label.config(text="Timer" , font=(FONT_NAME , 40 , "bold") ,foreground=GREEN , background="#FDECF2")
    canvas.itemconfig(timer_text , text= "25:00")
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global timer
    count_min = count // 60
    count_sec = count % 60
    if count_sec == 0:
        count_sec ="00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"    
    canvas.itemconfig(timer_text , text= f"{count_min}:{count_sec}")
    if count > 0:
        
        
        timer = window.after(1000 , countdown , count - 1)

    else:
        print("countdown done")
        start_timer()
        window.state('normal')
        window.attributes('-topmost', True)
        window.lift()
        window.focus_force()
        window.attributes('-topmost', False)
    
        if reps % 2 == 0:
            check.config(text="✅"*int(reps/2) , foreground= GREEN ,background="#FDECF2")
        

# ---------------------------- UI SETUP ------------------------------- #
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import time
# 1. Initialize the window window using ThemedTk instead of tk.Tk()
window = ThemedTk(theme="arc")  # 'arc' is a highly recommended clean theme
window.title("Pomodoro")
window.geometry("")


window.config(padx=50 , pady=50 , bg= "#FDECF2")
canvas = tk.Canvas(width=200 , height=224 ,bg= "#FDECF2", highlightthickness=0)
button = ttk.Button(window, text="Start" , command = lambda: start_timer() if reps == 0 else None)
button.grid(column=0 , row=2 , pady=10)
button = ttk.Button(window, text="Reset" , command=reset)
button.grid(column=2 , row=2 , pady=10)
label = ttk.Label(window, text="Timer" , font=(FONT_NAME , 40 , "bold") ,foreground=GREEN , background="#FDECF2")
label.grid(column=1 , row=0 , pady=10)
tomato = tk.PhotoImage(file='tomato.png')
canvas.create_image(100 , 112 , image = tomato)
canvas.grid(column=1 , row=1)
timer_text = canvas.create_text(100, 130 ,text="25:00" , fill="white" , font=(FONT_NAME, 40 ,"bold"),)
check = ttk.Label(text="" , foreground= GREEN ,background="#FDECF2")
check.grid(column=1 , row=3)
# 2. Use TTK widgets so they receive the theme styles

def got_clicked():
    print("click")
# This button will match the 'arc' theme aesthetics
window.mainloop()