import ctypes
import time
from ctypes import wintypes
from tkinter import *
import parsing_server1
import requests



def start_frame():
    frame_tumblers1_frame.place_forget()
    frame_tumblers2_frame.place_forget()
    frame_tumblers3_frame.place_forget()
    frame_tumblers_frame.place(x=18, y=225, width=765, height=355)
    print('def_start')


def general_menu(*event):
    frame_tumblers1_frame.place_forget()
    frame_tumblers2_frame.place_forget()
    frame_tumblers3_frame.place_forget()
    frame_tumblers_frame.place(x=18, y=225, width=765, height=355)
    print('def1')


def overview(*event):
    frame_tumblers_frame.place_forget()
    frame_tumblers2_frame.place_forget()
    frame_tumblers3_frame.place_forget()
    frame_tumblers1_frame.place(x=18, y=225, width=765, height=355)
    print('def2')


def settings(*event):
    frame_tumblers_frame.place_forget()
    frame_tumblers1_frame.place_forget()
    frame_tumblers3_frame.place_forget()
    frame_tumblers2_frame.place(x=18, y=225, width=765, height=355)
    print('def3')


def reserved(*event):
    frame_tumblers_frame.place_forget()
    frame_tumblers1_frame.place_forget()
    frame_tumblers2_frame.place_forget()
    frame_tumblers3_frame.place(x=18, y=225, width=765, height=355)
    print('def4')


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


def check_Power():
    class SYSTEM_POWER_STATUS(ctypes.Structure):
        _fields_ = [
            ('ACLineStatus', wintypes.BYTE),
            ('BatteryFlag', wintypes.BYTE),
            ('BatteryLifePercent', wintypes.BYTE),
            ('Reserved1', wintypes.BYTE),
            ('BatteryLifeTime', wintypes.DWORD),
            ('BatteryFullLifeTime', wintypes.DWORD),
        ]

    SYSTEM_POWER_STATUS_P = ctypes.POINTER(SYSTEM_POWER_STATUS)

    GetSystemPowerStatus = ctypes.windll.kernel32.GetSystemPowerStatus
    GetSystemPowerStatus.argtypes = [SYSTEM_POWER_STATUS_P]
    GetSystemPowerStatus.restype = wintypes.BOOL

    status = SYSTEM_POWER_STATUS()
    if not GetSystemPowerStatus(ctypes.pointer(status)):
        raise ctypes.WinError()
    if status.ACLineStatus != 0:
        # print('Power Ok!')
        lbl_Power_sensor['text'] = 'Power sensor status: AC power connected, Ok'
    else:
        # print('No Power')
        lbl_Power_sensor['text'] = 'Power sensor status: AC power lost, Battery mode!'
    # print('ACLineStatus', status.ACLineStatus)
    # print('BatteryFlag', status.BatteryFlag)
    # print('BatteryLifePercent', status.BatteryLifePercent)
    # print('BatteryLifeTime', status.BatteryLifeTime)
    # print('BatteryFullLifeTime', status.BatteryFullLifeTime)
    root.after(30000, check_Power)



def xxx():

        try:
            parsing_server1.parsing_ESP()
            xxx1 = parsing_server1.parsing_ESP()
            print(xxx1 +'vot!')
            root.after(3000, xxx)
        except:
            pass
            root.after(3000, xxx)

def check_req():
    try:
        r = requests.get('https://google.com.ua/')  # резервный ('http://httpbin.org/get')
        print(r.status_code)
        lbl_Internet_sensor['text'] = 'Internet sensor status: Connected, Ok'
        root.after(300000, check_req)
    except:
        print('except! Internet')
        lbl_Internet_sensor['text'] = 'Internet sensor status: Disconnected, Error!'
        pass
        root.after(30000, check_req)


def check_Light_sensor_conections():
    try:
        r = requests.get('http://192.168.0.110/')
        print(r.status_code)
        lbl_Light_sensor['text'] = 'Light sensor status: Connected, Ok'
        root.after(600000, check_Light_sensor_conections)
    except:
        print('except! Light sensor')
        lbl_Light_sensor['text'] = 'Light sensor status: Disconnected, Error!'
        pass
        root.after(600000, check_Light_sensor_conections)


def check_Server_sensor_conections():
    try:
        r = requests.get('https://ochre-propulsion.000webhostapp.com/')  # резервный ('http://httpbin.org/get')
        print(r.status_code)
        lbl_Server_sensor['text'] = 'Server sensor status: Connected, Ok'
        root.after(600000, check_Server_sensor_conections)
    except:
        print('except! Server')
        lbl_Server_sensor['text'] = 'Server sensor status: Disconnected, Error!'
        pass
        root.after(600000, check_Server_sensor_conections)


# def check_Light_sensor_conections():
# if pythonping.ping("192.168.0.110", verbose=False).success:
#   print("192.168.0.110 ping Successful!")
#  lbl_Light_sensor['text'] = 'Light sensor status: Connected, Ok'
#  root.after(600000, check_Light_sensor_conections)


# function which changes time on Label
def update_time():
    # change text on Label
    lbl_time['text'] = time.strftime('Current date: %Y-%m-%d Current time: %H:%M:%S')

    # run `update_time` again after 1000ms (1s)
    root.after(1000, update_time)  # function name without ()


root = Tk()
setwindow(root)
frame_main_frame = Frame(master=root, relief=GROOVE, borderwidth=5, bg='#0c47a6')
frame_sensor_frame = Frame(master=frame_main_frame, relief=GROOVE, borderwidth=5, bg='#0f80f2')

frame_tumblers_frame = Frame(master=frame_main_frame, relief=GROOVE, borderwidth=5, bg='#a4aaab')
frame_tumblers1_frame = Frame(master=frame_main_frame, relief=GROOVE, borderwidth=5, bg='#a4aaab')
frame_tumblers2_frame = Frame(master=frame_main_frame, relief=GROOVE, borderwidth=5, bg='#a4aaab')
frame_tumblers3_frame = Frame(master=frame_main_frame, relief=GROOVE, borderwidth=5, bg='#a4aaab')

lbl_time = Label(master=frame_sensor_frame, text='Current time: 00:00:00', font="Tahoma 12", bg='#0f80f2')
lbl_time.pack()

lbl_connections = Label(master=frame_sensor_frame, text='Connections state', font="Tahoma 14", bg='#0f80f2')
lbl_connections.pack()

lbl_Power_sensor = Label(master=frame_sensor_frame, text='Power sensor status: Connected, Power on', font='Tahoma 10',
                         bg='#0f80f2')
lbl_Light_sensor = Label(master=frame_sensor_frame, text='Light sensor status: ', font='Tahoma 10', bg='#0f80f2')
lbl_Water_sensor = Label(master=frame_sensor_frame, text='Water sensor status: Connected, Ok', font='Tahoma 10',
                         bg='#0f80f2')
lbl_Gas_sensor = Label(master=frame_sensor_frame, text='Gas sensor status: Connected, Ok', font='Tahoma 10',
                       bg='#0f80f2')
lbl_Server_sensor = Label(master=frame_sensor_frame, text='Server sensor status: Connected, Ok', font='Tahoma 10',
                          bg='#0f80f2')
lbl_Internet_sensor = Label(master=frame_sensor_frame, text='Internet sensor status: ', font='Tahoma 10', bg='#0f80f2')

lbl_Power_sensor.pack()
lbl_Light_sensor.pack()
lbl_Water_sensor.pack()
lbl_Gas_sensor.pack()
lbl_Server_sensor.pack()
lbl_Internet_sensor.pack()

lbl_general = Label(master=frame_tumblers_frame, text='General', font="Tahoma 14", bg='#a4aaab')
lbl_general.pack()

lbl_overview = Label(master=frame_tumblers1_frame, text='Overview', font="Tahoma 14", bg='#a4aaab')
lbl_overview.pack()

lbl_settings = Label(master=frame_tumblers2_frame, text='Settings', font="Tahoma 16", bg='#a4aaab')
lbl_settings.pack()


lbl_settings_server_IP = Label(master=frame_tumblers2_frame, text='Server IP', font="Tahoma 14", bg='#a4aaab')
lbl_settings_server_IP.place(x=0, y=50)
ent_settings_server_ip = Entry(master=frame_tumblers2_frame, text='', font="Tahoma 14", bg='White', fg='Black')
ent_settings_server_ip.place(x=150, y=50)

lbl_settings_Internet_IP = Label(master=frame_tumblers2_frame, text='Internet IP', font="Tahoma 14", bg='#a4aaab')
lbl_settings_Internet_IP.place(x=0, y=90)
ent_settings_Internet_IP1 = Entry(master=frame_tumblers2_frame, text='', font="Tahoma 14", bg='White', fg='Black')
ent_settings_Internet_IP1.place(x=150, y=90)

lbl_settings_sensor1 = Label(master=frame_tumblers2_frame, text='Sensor Light IP', font="Tahoma 14", bg='#a4aaab')
lbl_settings_sensor1.place(x=0, y=130)
ent_settings_sensor1= Entry(master=frame_tumblers2_frame, text='', font="Tahoma 14", bg='White', fg='Black')
ent_settings_sensor1.place(x=150, y=130)

lbl_settings_ESP1 = Label(master=frame_tumblers2_frame, text='ESP1 IP', font="Tahoma 14", bg='#a4aaab')
lbl_settings_ESP1.place(x=420, y=50)
ent_settings_ESP1= Entry(master=frame_tumblers2_frame, text='', font="Tahoma 14", bg='White', fg='Black')
ent_settings_ESP1.place(x=540, y=50)

lbl_settings_ESP2 = Label(master=frame_tumblers2_frame, text='ESP2 IP', font="Tahoma 14", bg='#a4aaab')
lbl_settings_ESP2.place(x=420, y=90)
ent_settings_ESP2= Entry(master=frame_tumblers2_frame, text='', font="Tahoma 14", bg='White', fg='Black')
ent_settings_ESP2.place(x=540, y=90)

lbl_settings_ESP3 = Label(master=frame_tumblers2_frame, text='ESP3 IP', font="Tahoma 14", bg='#a4aaab')
lbl_settings_ESP3.place(x=420, y=130)
ent_settings_ESP3= Entry(master=frame_tumblers2_frame, text='', font="Tahoma 14", bg='White', fg='Black')
ent_settings_ESP3.place(x=540, y=130)





lbl_reserved = Label(master=frame_tumblers3_frame, text='Reserved', font="Tahoma 14", bg='#a4aaab')
lbl_reserved.pack()

button1 = Button(master=frame_main_frame, text="General", command=general_menu, bg="#adb2b8", fg="Black",
                 font="Tahoma 14")
button2 = Button(master=frame_main_frame, text="Overview", command=overview, bg="#adb2b8", fg="Black", font="Tahoma 14")
button3 = Button(master=frame_main_frame, text="Settings", command=settings, bg="#adb2b8", fg="Black", font="Tahoma 14")
button4 = Button(master=frame_main_frame, text="Reserved", command=reserved, bg="#adb2b8", fg="Black", font="Tahoma 14")

frame_main_frame.place(x=5, y=5, width=790, height=590)
frame_sensor_frame.place(x=150, y=10, width=622, height=195)
frame_tumblers_frame.place(x=18, y=225, width=765, height=355)
frame_tumblers1_frame.place(x=18, y=225, width=765, height=355)
frame_tumblers2_frame.place(x=18, y=225, width=765, height=355)
frame_tumblers3_frame.place(x=18, y=225, width=765, height=355)

button1.place(x=10, y=10, width=130, height=40)
button2.place(x=10, y=60, width=130, height=40)
button3.place(x=10, y=110, width=130, height=40)
button4.place(x=10, y=160, width=130, height=40)

root.after(0, start_frame)
root.after(0, check_Power)
root.after(0, check_req)
root.after(2000, check_Light_sensor_conections)
root.after(2000, check_Server_sensor_conections)
root.after(1000, update_time)
root.title('Control panel')
# root.after(0, parsing_server1.parsing_ESP())
root.after(5000, xxx)
root.mainloop()
