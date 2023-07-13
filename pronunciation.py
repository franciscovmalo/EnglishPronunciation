import sys
from turtle import bgcolor
import pyttsx3
import tkinter as tk
from tkinter import *
from tkinter import ttk


engine = pyttsx3.init()
engine.setProperty('rate', 125)
COLOR = 'black'

rate = engine.getProperty('rate')
#print(rate)

#Home window class
class Home(Tk):
    def __init__(self):
        super().__init__() 
        
        speak = self.speak
        self.geometry('500x500')
        self.usertext = StringVar()
        self.bg = PhotoImage(file='sound-waves.png')
        self.voice_val = StringVar(value=2)
        self.speed_val = StringVar()
        self.greet = Frame(self)
        menubar = Menu(self, background='orange', foreground='black', 
                       activebackground='orange', activeforeground='black')
        file = Menu(menubar, tearoff=0, background='orange', foreground='black')
        file.add_command(label='Settings', command=self.change_g)
        menubar.add_cascade(label="File", menu=file)
        
        Label(self, image = self.bg).place(relx=.5, rely=.5, anchor= CENTER)
        Label(self.greet, text="Speed").grid(column=1, row=8, pady=10)
        Label(self.greet, text="Voice").grid(column=1, row=4, pady=10)
        #Label(self, bg='orange').place(width=700, relx=1.0, rely=1.0, anchor= SE)
        
        Button(self, text="Pronounce", width=8, height=1, border=False, bg="orange",
                command=self.voices).place(relx=.5, y=400, anchor= CENTER)
        #.place(x=218,y=280)
        Button(self.greet, text="Back", bg='red', border=False, 
               command=self.back).grid(column=2, row=12, pady=10)
        
        self.fild = Entry(self, textvariable=self.usertext, width=54, border=False)
        self.fild.place(relx=.5, rely=.5, anchor= CENTER)
        #.place(x=100, y=250, height=20, anchor= CENTER)       
        self.config(menu=menubar)
        self.bind('<Return>', self.voices) 
        
        self.voice_spb = ttk.Spinbox(self.greet, from_=1, to_=6, textvariable=self.voice_val, wrap=True, width=5)
        self.voice_spb.grid(column=2, row=4, pady=10)
        self.speed_cb = ttk.Combobox(self.greet, textvariable=self.speed_val, state='readonly', width=5, background=COLOR,
                                  values=['0.25x', '0.5x', '0.75x', 'Normal', '1.25x', '1.5x', '2x'])
        self.speed_cb.grid(column=2, row=8, pady=10)
        self.speed_cb.bind('<<ComboboxSelected>>', self.voices)
        
    def change_g(self):
        self.greet.pack(fill='both', expand=1)  
          
    def voices(self, event):
        self.text = self.usertext.get()
        voice_out = engine.getProperty('voices')
        self.speak
        if self.voice_spb.grab_current() == "1":
            engine.setProperty('voice', voice_out[-3].id)
            engine.say(self.text)
            engine.runAndWait()
            
        elif self.voice_spb.get() == "2":
            engine.setProperty('voice', voice_out[-2].id)
            engine.say(self.text)
            engine.runAndWait()
            
        elif self.voice_spb.get() == "3":
            engine.setProperty('voice', voice_out[-1].id)
            
        elif self.voice_spb.get() == "4":
            engine.setProperty('voice', voice_out[0].id)
            
        elif self.voice_spb.grab_current() == "5":
            engine.setProperty('voice', voice_out[1].id)
            
        elif self.voice_spb.get() == "6":
            engine.setProperty('voice', voice_out[2].id)


    def speed(self):
        self.speed_val = StringVar()
        if self.speed_cb.get() == '0.25x':
            print("ON")
        elif self.speed_cb.get() == '0.5x':
            pass
            
        elif self.speed_cb.get() == '0.5x':
            pass
            
        elif self.speed_cb.get() == '0.5x':
            pass
        elif self.speed_cb.get() == '0.5x':
            pass
            
        elif self.speed_cb.get() == '0.5x':
            pass
    
    def back(self):
        self.greet.pack_forget()
        
        
    def speak(self, event):
        self.text = self.usertext.get()
        engine.say(self.text)
        engine.runAndWait()
        self.fild.delete('0', 'end')  
        
    def close(event):

        result = tk.messagebox.askquestion('EXIT', 'Do You Want To Exit?', icon='warning')

        if result == 'yes':
            sys.exit()
        else:
            #tk.messagebox.showinfo('Return')
            window = Home()  
            
    def open_window(self):
        
        window = Settings(self)
        window.grab_set()
        

#Settings window class
class Settings(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.geometry('500x500')
        Button(self, text="Pronounce", width=10, height=1, border=False, bg="orange").place(x=218,y=280)
        
        
        
        
if __name__ == "__main__":
    win = Home()
    win.mainloop()     