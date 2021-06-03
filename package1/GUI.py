from tkinter import *
from tkinter import Tk, BOTH
from tkinter.ttk import Frame, Label, Style

def setwindow(root):
    root.title("Окно программы")
    root.resizable(False, False)

    w = 800
    h = 600
    ws = root.winfo_screenwidth()
    wh = root.winfo_screenheight()

    x = int(ws / 2 - w / 2)
    y = int(wh / 2 - h / 2)

    root.geometry("{0}x{1}+{2}+{3}".format(w, h, x, y))

root = Tk()
setwindow(root)

button = Button(root, text = "ТЫ КНОПКА, БЛЯДЬ!", bg="White", fg="Red", font = "Tahona 18")

label = Label(root, text = "Хрень", font = "Tahona 18")
label.pack(side="left")
button.pack()

root.mainloop()