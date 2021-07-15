import glob
import sys
from time import sleep

import serial
from serial.win32 import ClearCommError

import Variables

# def serial_ports():
#     """ Lists serial port names
#
#         :raises EnvironmentError:
#             On unsupported or unknown platforms
#         :returns:
#             A list of the serial ports available on the system
#     """
#     if sys.platform.startswith('win'):
#         ports = ['COM%s' % (i + 1) for i in range(256)]
#     elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
#         # this excludes your current terminal "/dev/tty"
#         ports = glob.glob('/dev/tty[A-Za-z]*')
#     elif sys.platform.startswith('darwin'):
#         ports = glob.glob('/dev/tty.*')
#     else:
#         raise EnvironmentError('Unsupported platform')
#
#     result = []
#     for port in ports:
#         try:
#             s = serial.Serial(port)
#             s.close()
#             result.append(port)
#         except (OSError, serial.SerialException):
#             pass
#     res = result[0]
#     print(result[0])
#     return res





def COMPORTREAD():
    while True:
        try:
            ser = serial.Serial('COM4', baudrate=9600, timeout=0)
        except Exception as e:
            print('open error', e)
            sleep(1.0)
        while True:
            try:
                lines = ser.readline()
                print(lines.decode('UTF-8').strip())
                lines1 = str(lines.decode('UTF-8'))
                lines1 = lines1.rstrip()
                if lines1.split('=', 1)[0] == 'gerkon_down':
                    print('match!!! gerkon_down = ' + str(lines1.split('=', 1)[1]))
                if lines1.split('=', 1)[0] == 'gerkon_up':
                    print('match!!! gerkon_up = ' + str(lines1.split('=', 1)[1]))
                if lines1.split('=', 1)[0] == 'gerkon_alarm':
                    print('match!!! gerkon_alarm = ' + str(lines1.split('=', 1)[1]))
                if lines1.split('=', 1)[0] == 'Position relay1_on_off':
                    print('match!!! Position relay1_on_off = ' + str(lines1.split('=', 1)[1]))
                if lines1.split('=', 1)[0] == 'Position relay2':
                    print('match!!! Position relay2 = ' + str(lines1.split('=', 1)[1]))
                if lines1.split('=', 1)[0] == 'Position relay3_alarm':
                    print('match!!! Position relay3_alarm = ' + str(lines1.split('=', 1)[1]))
                if lines1.split('=', 1)[0] == 'status':
                    print('match!!! status = ' + str(lines1.split('=', 1)[1]))
                if not lines:
                    sleep(2.0)
            except Exception as e:
                break
                pass
        sleep(5.0)
