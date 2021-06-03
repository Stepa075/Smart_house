from tkinter import *
import time
import datetime

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

# function which changes time on Label
def update_time():
    # change text on Label
    lbl_time['text'] = time.strftime('Current time: %H:%M:%S')

    # run `update_time` again after 1000ms (1s)
    root.after(1000, update_time) # function name without ()

def update_date():
    # change text on Label
    lbl_date['text'] = time.strftime('Current date: %Y-%m-%d')

    # run `update_time` again after 1000ms (1s)
    root.after(1000, update_time) # function name without ()

root = Tk()
setwindow(root)
frame_main_frame = Frame(master=root, relief=GROOVE, borderwidth=5)
frame_sensor_frame = Frame(master=frame_main_frame, relief=GROOVE, borderwidth=5)

lbl_time = Label(master=frame_sensor_frame, text='Current time: 00:00:00')
lbl_time.pack()
lbl_date = Label(master=frame_sensor_frame, text='Current date: 0000-00-00')
lbl_date.pack()
button1 = Button(master=frame_main_frame, text="Моя кнопка 1", bg="White", fg="Green", font="Tahoma 14")
button2 = Button(master=frame_main_frame, text="Моя кнопка 2", bg="White", fg="Green", font="Tahoma 14")
button3 = Button(master=frame_main_frame, text="Моя кнопка 3", bg="White", fg="Green", font="Tahoma 14")
button4 = Button(master=frame_main_frame, text="Моя кнопка 4", bg="White", fg="Green", font="Tahoma 14")

frame_main_frame.place(x=5, y=5, width=790, height=590)
frame_sensor_frame.place(x=150, y=10, width=622, height=195)

button1.place(x=10, y=10, width=130, height=40)
button2.place(x=10, y=60, width=130, height=40)
button3.place(x=10, y=110, width=130, height=40)
button4.place(x=10, y=160, width=130, height=40)

root.after(1000, update_time)
root.after(1000, update_date)
root.mainloop()