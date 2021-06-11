# import ctypes
# from ctypes import wintypes
#
#
# class SYSTEM_POWER_STATUS(ctypes.Structure):
#     _fields_ = [
#         ('ExternalPower', wintypes.BYTE),
#         ('BatteryFlag', wintypes.BYTE),
#         ('BatteryLifePercent', wintypes.BYTE),
#         ('Reserved1', wintypes.BYTE),
#         ('BatteryLifeTime', wintypes.DWORD)
#         ]
#
# SYSTEM_POWER_STATUS_P = ctypes.POINTER(SYSTEM_POWER_STATUS)
# GetSystemPowerStatus = ctypes.windll.kernel32.GetSystemPowerStatus
# GetSystemPowerStatus.argtypes = [SYSTEM_POWER_STATUS_P]
# GetSystemPowerStatus.restype = wintypes.BOOL
#
# status = SYSTEM_POWER_STATUS()
# if not GetSystemPowerStatus(ctypes.pointer(status)):
#         raise cytpes.WinError()
# print 'ExternalPower', status.ExternalPower
# #print 'BatteryFlag', status.BatteryFlag
# print 'BatteryLifePercent', status.BatteryLifePercent
# print 'BatteryLifeTime', status.BatteryLifeTime
#
# if status.ExternalPower == True and status.BatteryLifePercent == 100:
#     print 'Connected to mains and at 100% charge: Begining decharge'
#     # This is where I would like to force battery use. Perhaps with a while
#  #loop (that ticks every 60 seconds or so)
#     if status.BatteryLifePercent > 10 :
#         status.ExternalPower = 0
#
# elif status.ExternalPower == True and status.BatteryLifePercent < 100:
#     print 'Connected to mains and charging up to 100%'
#     status.ExternalPower = 1
#
# elif status.ExternalPower == False:
#     print 'Not connected to mains'
#
# else:
#     print ' Unknown system status'
#
# x = raw_input('Press ENTER to close:')

#
# Get power status of the system using ctypes to call GetSystemPowerStatus

import ctypes
from ctypes import wintypes

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
print ('ACLineStatus', status.ACLineStatus)
print ('BatteryFlag', status.BatteryFlag)
print ('BatteryLifePercent', status.BatteryLifePercent)
print ('BatteryLifeTime', status.BatteryLifeTime)
print ('BatteryFullLifeTime', status.BatteryFullLifeTime)