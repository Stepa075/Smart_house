
import threading
from time import sleep

import requests

from urllib3.exceptions import MaxRetryError, NewConnectionError, ResponseError

import Variables

lock = threading.RLock()


def start1():
    while True:
        try:
            if Variables.status_code_server_connections == 200:
                r4_0 = Variables.parsing_GPIO_4relay1
                r4_1 = str(r4_0[0])
                r4_2 = str(r4_0[1])
                r4_3 = str(r4_0[2])
                r4_4 = str(r4_0[3])
                params = {'params': str(Variables.parsing_ESP1),
                          'params1': str(Variables.Sadok_Light1),
                          'params2_1': r4_1,
                          'params2_2': r4_2,
                          'params2_3': r4_3,
                          'params2_4': r4_4, 'control': 'home'}
                print(params)
                r = requests.get('http://f0555107.xsph.ru/index.php', params=params, timeout=3.0)
                r.encoding = "UTF8"
                print('start1 = Ok')
                print(r.text)
            else:
                print('start1 ' + Variables.time_now + ' Bad response, status_code= ' + str(
                    Variables.status_code_server_connections))
            sleep(20.0)
        except:
            sleep(20.0)
            continue
            pass
    sleep(20.0)


def start2():
    while True:
        try:
            if Variables.status_code_server_connections == 200:
                url = "http://f0555107.xsph.ru/hello.html"
                r = requests.get(url, timeout=3.00)
                r.encoding = "UTF8"
                if r.status_code == 200:
                    print('start2 = Ok')
                    with open('response_server.html', 'w') as output_file:
                        output_file.write(r.text)
                    with open('response_server.txt', 'w') as output_file:
                        output_file.write(r.text)
                    text_file = open("response_server.html", "r")
                    lines = text_file.read().split(',')
                    print(lines)
                    # print(len(lines))
                    text_file.close()
                    Variables.receive_from_server = lines
                    Variables.receive_from_server1 = lines[0]
                    Variables.receive_from_server1 = lines[1]
                    Variables.receive_from_server1 = lines[2]
                    Variables.receive_from_server1 = lines[3]
                    Variables.receive_from_server1 = lines[4]
                    Variables.receive_from_server1 = lines[5]
                    Variables.receive_from_server1 = lines[6]
                    # with open('controlling.txt', 'a') as output_file:
                    #   output_file.write(Variables.time_now + str(lines) + '\n')
            else:
                with open('controlling.log.txt', 'a') as output_file:
                    output_file.write('start2 ' + Variables.time_now + ' Bad_status_code!' + '\n')
                print('start2 ' + str(Variables.time_now) + ' Bad response, status_code= ' + str(
                    Variables.status_code_server_connections))
            sleep(20.0)
        except:
            sleep(20.0)
            continue
            pass
    sleep(20.0)


def parsing_ESP():
    global str3

    while True:
        try:
            if Variables.status_code_light_sensor == 200:
                url = "http://192.168.0.110/sensors/adci1/"
                r = requests.get(url, timeout=3.0)
                r.encoding = "UTF8"
                with open('test.html', 'w') as output_file:
                    output_file.write(r.text)
                with open('test1.txt', 'w') as output_file:
                    output_file.write(r.text)

                f = open('test1.txt')
                str1 = f.read()
                f.close()

                str2 = str1[str1.find(";") + 1:]
                str3 = str2[str2.find(":") + 1: str2.find(";")]
                Variables.parsing_ESP = int(str3)
                Variables.parsing_ESP1 = int(str3)
                print('parsing_ESP = Ok, Variables.parsing_ESP = ' + str(Variables.parsing_ESP))
            else:
                Variables.parsing_ESP = 'No connect ESP!'
            sleep(10.0)
        except:
            sleep(10.0)
            continue
            pass
    sleep(10.0)


def parsing_GPIO_Sadok():
    global str_sad3
    while True:
        try:

            url = "http://192.168.0.100/gpioprint"
            r = requests.get(url, timeout=3.0)
            Variables.status_code_sadok = r.status_code
            r.encoding = "UTF8"
            if r.status_code == 200:
                with open('sadok.html', 'w') as output_file:
                    output_file.write(r.text)
                with open('sadok1.txt', 'w') as output_file:
                    output_file.write(r.text)

                f = open('sadok1.txt')
                str_sad = f.read()
                f.close()
                str_sad2 = str_sad[:str_sad.find(";") + 1]
                str_sad3 = str_sad2[str_sad2.find(":") + 1: str_sad2.find(";")]
                Variables.Sadok_Light = int(str_sad3)
                Variables.Sadok_Light1 = int(str_sad3)
                print('parsing_GPIO_Sadok = Ok ')
            else:
                Variables.status_code_sadok = 0
                Variables.Sadok_Light = 2
                str_sad3 = 2
                print('parsing_GPIO_Sadok = else(error, can not read)!')
            sleep(10.0)
        except NewConnectionError:
            Variables.Sadok_Light = 'Except, NewConnection error!!'
            str_sad3 = 2
            continue
        except:
            sleep(10.0)
            continue
            pass
    sleep(10.0)


def parsing_GPIO_4relay11():
    while True:

        try:
            url = "http://192.168.0.120/gpioprint"
            r = requests.get(url)
            Variables.status_code_4relay = r.status_code
            r.encoding = "UTF8"
            with open('4relay.txt', 'w') as output_file:
                output_file.write(r.text)
            f = open('4relay.txt')
            str_4relay = f.read()
            f.close()
            print('parsing_GPIO_4relay = Ok')
            str_4relay2 = str_4relay[str_4relay.find(":") + 1:]

            Variables.r1 = str_4relay2[: str_4relay2.find(";")]
            Variables.r2 = str_4relay[10:11]
            Variables.r3 = str_4relay[18:19]
            Variables.r4 = str_4relay[23:24]
            # relay_list = [r1, r2, r3, r4]
            # Variables.parsing_GPIO_4relay = relay_list
            # Variables.parsing_GPIO_4relay1 = relay_list
            # print('Variables.parsing_GPIO_4relay =' + str(Variables.parsing_GPIO_4relay))
            sleep(10.0)
        except:
            sleep(10.0)
            continue
            pass
        # break
    sleep(10.0)
