from tkinter import *
from tkinter import ttk


def event1():
    ttk.Label(text='Menu:        ', font='arial 14').place(x=550, y=50)


def event2():
    ttk.Label(text='Браузеры:', font='arial 14').place(x=550, y=50)

def event3():
    ttk.Label(text='Settings:   ', font='arial 14').place(x=550, y=50)

root = Tk()
root.title("Program")
root.geometry('1024x700')
Frame(root, width=260, height=700, bg='#FFEFD5').place(x=0, y=0)  # этот фрейм нужен для раскраски
Button(text="Меню", width=30, height=2, command=event1, activebackground='#FF4500').place(x=20, y=100)
Button(text="Browsers", width=30, height=2, command=event2, activebackground='#FF4500').place(x=20, y=150)
Button(text='Настройки', width=30, height=2, command=event3, activebackground='#FF4500').place(x=20, y=200)
root.mainloop()