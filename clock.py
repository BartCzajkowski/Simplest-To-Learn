"""Najprostszy zegarek"""
import tkinter
from time import strftime

clock = tkinter.Tk()
clock.title("Zegarek")

def czas():
    string = strftime('%H:%M:%S\n%d %m %Y')
    label.config(text=string)
    label.after(1000, czas)

label = tkinter.Label(clock, font=("Arial", 40), background = "black", foreground = "white")
label.pack(anchor = "center")
czas()
tkinter.mainloop()
