import ctypes
import threading, win32gui, win32process, psutil
from ctypes.wintypes import BOOL
from time import sleep
from tkinter import *
import pyautogui
from win32comext.shell.shell import ShellExecuteEx

root = Tk()
s = StringVar()


# BOOL ShellExecuteEx(_Inout_ SHELLEXECUTEINFO nShow=0)

def active_window_process_name():  # Узнаем имя текущего процесса в фокусе...
    try:
        pid = win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow())
        return (psutil.Process(pid[-1]).name())
    except:
        pass


def to_label():
    global s
    while True:
        s.set(active_window_process_name())

        sleep(0.5)
    return


def some():
    while True:

        if active_window_process_name() == 'notepad.exe':  # Проверяем фокус нужного приложения и раскладку,
            if get_name_layout() != 'ru':  # если все соответствует - спим и дальше по циклу...
                while get_name_layout() != 'ru':  # Если нужное приложение в фокусе, но раскладка не та...
                    pyautogui.hotkey('shift', 'alt')  # Меняем ее эмуляцией нужных клавиш.
                    sleep(1)
            else:
                sleep(1.0)
                continue
        else:
            sleep(2.0)
    return


def get_name_layout():  # Определяем раскладку и возвращаем ее...
    user32 = ctypes.WinDLL('user32', use_last_error=True)
    curr_window = user32.GetForegroundWindow()
    thread_id = user32.GetWindowThreadProcessId(curr_window, 0)
    name = user32.GetKeyboardLayout(thread_id)
    if str(name) == '67699721':
        print(name)
        return 'en'
    elif str(name) == '68748313':
        print(name)
        return 'ru'
    elif str(name) == '69338146':
        print(name)
        return 'uk'


Label(root, textvariable=s).pack()  # Отображение активного процесса(опционально)
if __name__ == "__main__":
    t = threading.Thread(target=to_label)
    t.start()
    t1 = threading.Thread(target=some)
    t1.start()
    root.mainloop()
