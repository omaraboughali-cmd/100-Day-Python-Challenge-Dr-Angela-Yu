from tkinter import *
window = Tk()
window.title("Mile to Km Converter")
window.minsize(150,100)
label1 = Label(text="   is equal to   " , font= "arial")
label1.grid(column=0 , row=1 , pady=10 )
entry1 = Entry(width=10 , font="arial")
entry1.grid(column=1 ,row=0 , pady=10 )
miles = entry1.get()
label3 = Label(text="     Miles     ", font= ("arial",15))

label3.grid(column=2 , row= 0)
label2 = Label(text="     Km     " , font= "arial")
label2.grid(column=2 , row= 1)
label4 = Label(text="         ")
label4.grid(column=1 , row= 1)

def button_clicked():
    a = entry1.get()
    label4.config(text=int(a)*1.60934 ,font=("arial"))
    label4.grid(column=1 , row= 1)
button = Button(text="Calculate" , font= "arial"  , command=button_clicked)
button.grid(column=1 , row = 2 , pady=10)

window.mainloop()