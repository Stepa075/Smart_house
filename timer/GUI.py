from tkinter import *
from tkinter import IntVar
from tkinter.ttk import Combobox
from typing import Type

import Variables
import Stream




def set_timer():
    lbl['text'] = Variables.set_timer_time
    root.after(1000, set_timer)

root = Tk()

var1 = IntVar()
var1.set(1)
var2 = IntVar()
var2.set(30)
var3 = IntVar()
var3.set(00)
check_cb = BooleanVar()
check_cb.set(False)




root.title("Python TIMER by Stepa075")
root.geometry('300x160')
root.resizable(False, False)
f1 = LabelFrame(root, text='Выбор времени')
f2 = LabelFrame(root, text='Выбор действия')
f3 = LabelFrame(root, text='Таймер')

spin_hour = Spinbox(f1, from_=0, to=24, width=4, textvariable=var1, font=("Arial Bold", 12))
spin_min = Spinbox(f1, from_=0, to=60, width=4, textvariable=var2, font=("Arial Bold", 12))
spin_sec = Spinbox(f1, from_=0, to=60, width=4, textvariable=var3, font=("Arial Bold", 12))
h = spin_hour.get()
m = spin_min.get()
s = spin_sec.get()

def circle_request():
    Variables.h = spin_hour.get()
    Variables.m = spin_min.get()
    Variables.s = spin_sec.get()
    print('Time variables= ' + str(Variables.h) + ' ' +  str(Variables.m) + ' ' +  str(Variables.s))
    Variables.sound = check_cb.get()
    print('cb_sound ' + str(check_cb.get()))
    Variables.input_combo_box = combo_box.current()
    print('combo_box ' + str(combo_box.get()))
    root.after(1000, circle_request)




hours = Label(f1, text=' Часы', font=("Arial Bold", 12))
minutes = Label(f1, text=' Минуты', font=("Arial Bold", 12))
seconds = Label(f1, text=' Секунды', font=("Arial Bold", 12))

combo_box = Combobox(f2, width=16, font=("Arial Bold", 11))
combo_box['values'] = ('Выключить ПК', 'Перезагрузить ПК', 'Гибернация',  'Выполнить файл', 'Завершить файл', 'Выдать напоминание')
combo_box.current(0)
button = Button(f2, text='Пуск', font=("Arial Bold", 12), command=Stream.start_timer)

cb_sound = Checkbutton(f3, text='Звук', font=("Arial Bold", 10), var=check_cb)
lbl = Label(f3, text="00:00:00", font=("Arial Bold", 16))
button1 = Button(f3, text='О авторе', width=13, command=Variables.about)


f1.grid(column=0, row=0, sticky=N, padx=2, pady=2)
f2.grid(column=1, row=0, sticky=N + S + W + E, padx=2, pady=2)
f3.grid(column=0, columnspan=3, row=1, sticky=N + S + W + E, padx=2, pady=2)

spin_hour.grid(column=0, row=0)
spin_min.grid(column=0, row=1)
spin_sec.grid(column=0, row=2)
hours.grid(column=1, row=0)
minutes.grid(column=1, row=1)
seconds.grid(column=1, row=2)
combo_box.grid(column=0, row=0, padx=3, pady=3)
button.grid(column=0, row=1, sticky=N + S + W + E, padx=3, pady=3)
lbl.grid(column=0, row=0, sticky=N + S + W + E, padx=15, pady=3)
cb_sound.grid(column=1, row=0, sticky=N + S + W + E, padx=3, pady=3)
button1.grid(column=2, row=0,  sticky=N + S + W + E, padx=3, pady=3)


root.after(0, circle_request)
root.after(0, set_timer)
root.mainloop()
