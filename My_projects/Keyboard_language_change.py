import ctypes
from time import sleep

import win32api
import win32con
import pyautogui
from win32api import GetKeyboardLayout


pyautogui.hotkey('shift', 'alt')

user32 = ctypes.WinDLL('user32', use_last_error=True)
curr_window = user32.GetForegroundWindow()
thread_id = user32.GetWindowThreadProcessId(curr_window, 0)
klid = user32.GetKeyboardLayout(thread_id)
print(klid)
