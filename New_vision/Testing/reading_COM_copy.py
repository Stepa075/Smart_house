import glob
import sys
from time import sleep

import serial


def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    res = result[0]
    print(result[0])
    return res


ser = serial.Serial(str(serial_ports()), baudrate=9600, timeout=2)  # настройка порта


class COMPORTREAD():
    while 1:
        lines = ser.readline()
        print(lines.decode('UTF-8').strip())
        lines1 = str(lines.decode('UTF-8'))
        # print('lines1 = ' + lines1)
        # print( lines1.split('=', 1)[0])
        if lines1.split('=', 1)[0] == 'gerkon_down':
            print('match!!! gerkon_down = ' + str(lines1.split('=', 1)[1]))
        if lines1.split('=', 1)[0] == 'gerkon_up':
            print('match!!! gerkon_up = ' + str(lines1.split('=', 1)[1]))
        if lines1.split('=', 1)[0] == 'gerkon_alarm':
            print('match!!! gerkon_alarm = ' + str(lines1.split('=', 1)[1]))
        if not lines:
            sleep(10.0)
