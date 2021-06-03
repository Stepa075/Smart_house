from socket import socket
from sys import platform
from tkinter import *
import time
import pythonping
import socket
import subprocess
import os
import requests
from urllib3.connectionpool import xrange


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

def check_req():

     try:
         r = requests.get('https://google.com.ua/')       # резервный ('http://httpbin.org/get')
         print(r.status_code)
         lbl_Internet_sensor['text'] = 'Internet sensor status: Connected, Ok'
         root.after(300000, check_req)
     except:
         print('except!')
         lbl_Internet_sensor['text'] = 'Internet sensor status: Disconnected, Error!'
         pass
         root.after(3000, check_req)


def check_Light_sensor_conections():
    try:
        r = requests.get('http://192.168.0.110/')  # резервный ('http://httpbin.org/get')
        print(r.status_code)
        lbl_Light_sensor['text'] = 'Light sensor status: Connected, Ok'
        root.after(600000, check_req)
    except:
        print('except!')
        lbl_Light_sensor['text'] = 'Light sensor status: Disconnected, Error!'
        pass
        root.after(600000, check_req)


def check_Server_sensor_conections():
    try:
        r = requests.get('https://ochre-propulsion.000webhostapp.com/')  # резервный ('http://httpbin.org/get')
        print(r.status_code)
        lbl_Light_sensor['text'] = 'Server sensor status: Connected, Ok'
        root.after(600000, check_req)
    except:
        print('except!')
        lbl_Light_sensor['text'] = 'Server sensor status: Disconnected, Error!'
        pass
        root.after(600000, check_req)






#def check_Light_sensor_conections():
    #if pythonping.ping("192.168.0.110", verbose=False).success:
     #   print("192.168.0.110 ping Successful!")
      #  lbl_Light_sensor['text'] = 'Light sensor status: Connected, Ok'
      #  root.after(600000, check_Light_sensor_conections)



    # function which changes time on Label
def update_time():
    # change text on Label
    lbl_time['text'] = time.strftime('Current date: %Y-%m-%d Current time: %H:%M:%S')

    # run `update_time` again after 1000ms (1s)
    root.after(1000, update_time) # function name without ()



root = Tk()
setwindow(root)
frame_main_frame = Frame(master=root, relief=GROOVE, borderwidth=5, bg='#0c47a6')
frame_sensor_frame = Frame(master=frame_main_frame, relief=GROOVE, borderwidth=5, bg='#0f80f2')
frame_tumblers_frame = Frame(master=root, relief=GROOVE, borderwidth=5, bg='#a4aaab')

lbl_time = Label(master=frame_sensor_frame, text='Current time: 00:00:00', font="Tahoma 12", bg='#0f80f2')
lbl_time.pack()

lbl_connections = Label(master=frame_sensor_frame, text='Connections state', font="Tahoma 14", bg='#0f80f2')
lbl_connections.pack()

lbl_Power_sensor = Label(master=frame_sensor_frame, text='Power sensor status: Connected, Power on', font='Tahoma 10', bg='#0f80f2')
lbl_Light_sensor = Label(master=frame_sensor_frame, text='Light sensor status: ', font='Tahoma 10', bg='#0f80f2')
lbl_Water_sensor = Label(master=frame_sensor_frame, text='Water sensor status: Connected, Ok', font='Tahoma 10', bg='#0f80f2')
lbl_Gas_sensor = Label(master=frame_sensor_frame, text='Gas sensor status: Connected, Ok', font='Tahoma 10', bg='#0f80f2')
lbl_Server_sensor = Label(master=frame_sensor_frame, text='Server sensor status: Connected, Ok', font='Tahoma 10', bg='#0f80f2')
lbl_Internet_sensor = Label(master=frame_sensor_frame, text='Internet sensor status: ', font='Tahoma 10', bg='#0f80f2')

lbl_Power_sensor.pack()
lbl_Light_sensor.pack()
lbl_Water_sensor.pack()
lbl_Gas_sensor.pack()
lbl_Server_sensor.pack()
lbl_Internet_sensor.pack()





button1 = Button(master=frame_main_frame, text="Моя кнопка 1", bg="#adb2b8", fg="Black", font="Tahoma 14")
button2 = Button(master=frame_main_frame, text="Моя кнопка 2", bg="#adb2b8", fg="Black", font="Tahoma 14")
button3 = Button(master=frame_main_frame, text="Моя кнопка 3", bg="#adb2b8", fg="Black", font="Tahoma 14")
button4 = Button(master=frame_main_frame, text="Моя кнопка 4", bg="#adb2b8", fg="Black", font="Tahoma 14")

frame_main_frame.place(x=5, y=5, width=790, height=590)
frame_sensor_frame.place(x=150, y=10, width=622, height=195)
frame_tumblers_frame.place(x=18, y=225, width=765, height=355)

button1.place(x=10, y=10, width=130, height=40)
button2.place(x=10, y=60, width=130, height=40)
button3.place(x=10, y=110, width=130, height=40)
button4.place(x=10, y=160, width=130, height=40)

root.after(0, check_req)
root.after(2000, check_Light_sensor_conections)
root.after(2000, check_Server_sensor_conections)
root.after(1000, update_time)
root.title('Control panel')

root.mainloop()