from tkinter import *
from tkinter import font

win = Tk()
win.geometry("700x700")

greet = Frame(win)
order = Frame(win)

def change_g():
    greet.pack(fill='both', expand=1)
    order.pack_forget()
    
def change_O():
    order.pack(fill='both', expand=1)
    greet.pack_forget()
    
font1 = font.Font(family='Georgia', size='22', weight='bold')
font2 = font.Font(family='Aerial', size='12')

label1 = Label(greet, text="Welcome", foreground="green3", font=font1)
label1.pack(pady=20)

label2 = Label(order, text="Welcome 2", foreground="blue", font=font2)
label2.pack(pady=20)

btn1 = Button(win, text="Switch to Greet", font=font2, command=change_O)
btn1.pack(pady=20)

btn2 = Button(win, text="Switch to Order", font=font2, command=change_g)
btn2.pack(pady=20)

win.mainloop()