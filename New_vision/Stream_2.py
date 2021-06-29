import gc
import threading
from time import sleep

import requests
from requests import ConnectTimeout
from urllib3.exceptions import MaxRetryError, NewConnectionError

import Variables

lock = threading.RLock()


def start1():
    x = 1
    while x == 1:
        a = 1
        while a == 1:
            lock.acquire()
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
                break
            except TimeoutError:
                print('start1 Timeout Error!')
                sleep(10.0)
            except MaxRetryError:
                print('start1 MaxRetry Error!')
                sleep(600.0)
            except ConnectTimeout:
                print('start1 ConnectTimeout Error!')
                sleep(600.0)
            except ConnectionError:
                print('start1 Connection Error!')
                sleep(600.0)
            except NewConnectionError:
                print('start1 NewConnectionError Error!')
                sleep(600.0)
            finally:
                lock.release()
        gc.collect()
        sleep(120.0)


def start2():
    x = 1
    while x == 1:
        a = 1
        while a == 1:
            global lines
            lock.acquire()
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
                break
            except TimeoutError:
                print('start2 Timeout Error!')
                sleep(10.0)
            except ConnectTimeout:
                print('start2 ConnectTimeout Error!')
                sleep(600.0)
            except ConnectionError:
                print('start2 Connection Error!')
                sleep(600.0)
            except MaxRetryError:
                print('start2 MaxRetry Error!')
                sleep(600.0)
            except NewConnectionError:
                print('start2 NewConnectionError Error!')
                sleep(600.0)
            finally:
                lock.release()
            return lines
        sleep(120.0)


def parsing_ESP():
            global str3


            lock.acquire()
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

            except TimeoutError:
                Variables.parsing_ESP = 'Except, Timeout!'
            except ConnectTimeout:
                Variables.parsing_ESP = 'Except, ConnectTimeout error!!'
            except ConnectionError:
                Variables.parsing_ESP = 'Except, Connection error!!'
            except NewConnectionError:
                Variables.parsing_ESP = 'Except, NewConnection error!!'
            # except:
            #     print(' Except! parsing_ESP')
            #     url = 'http://192.168.0.110/configrst?st=1'
            #     r = requests.get(url)
            #     str3 = 110
            #     Variables.parsing_ESP = int(str3)
            #     Variables.parsing_ESP1 = int(str3)
            #     sleep(5.0)
            finally:
                lock.release()



# def parsing_ESP():
#     global str3
#     x = 1
#     while x == 1:
#         a = 1
#         while a == 1:
#             lock.acquire()
#             try:
#                 if Variables.status_code_light_sensor == 200:
#                     url = "http://192.168.0.110/sensors/adci1/"
#                     r = requests.get(url, timeout=2.0)
#                     r.encoding = "UTF8"
#                     with open('test.html', 'w') as output_file:
#                         output_file.write(r.text)
#                     with open('test1.txt', 'w') as output_file:
#                         output_file.write(r.text)
#
#                     f = open('test1.txt')
#                     str1 = f.read()
#                     f.close()
#
#                     str2 = str1[str1.find(";") + 1:]
#                     str3 = str2[str2.find(":") + 1: str2.find(";")]
#                     Variables.parsing_ESP = int(str3)
#                     Variables.parsing_ESP1 = int(str3)
#                     print('parsing_ESP = Ok, Variables.parsing_ESP = ' + str(Variables.parsing_ESP))
#                 else:
#                     Variables.parsing_ESP = 'No connect ESP!'
#                 break
#             except TimeoutError:
#                 Variables.parsing_ESP = 'Except, Timeout!'
#             except ConnectTimeout:
#                 Variables.parsing_ESP = 'Except, ConnectTimeout error!!'
#             except ConnectionError:
#                 Variables.parsing_ESP = 'Except, Connection error!!'
#             except NewConnectionError:
#                 Variables.parsing_ESP = 'Except, NewConnection error!!'
#             # except:
#             #     print(' Except! parsing_ESP')
#             #     url = 'http://192.168.0.110/configrst?st=1'
#             #     r = requests.get(url)
#             #     str3 = 110
#             #     Variables.parsing_ESP = int(str3)
#             #     Variables.parsing_ESP1 = int(str3)
#             #     sleep(5.0)
#             finally:
#                 lock.release()
#             return str3
#         sleep(60.0)


def parsing_GPIO_Sadok():

            lock.acquire()
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

            except TimeoutError:
                Variables.Sadok_Light = 'Except, Timeout error!'
                str_sad3 = 2
            except ConnectTimeout:
                Variables.Sadok_Light = 'Except, ConnectTimeout error!!'
            except ConnectionError:
                Variables.Sadok_Light = 'Except, Connection error!!'
            except NewConnectionError:
                Variables.Sadok_Light = 'Except, NewConnection error!!'
                str_sad3 = 2
            finally:
                lock.release()




def parsing_GPIO_4relay11():

        lock.acquire()
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

            r1 = str_4relay2[: str_4relay2.find(";")]
            r2 = str_4relay[10:11]
            r3 = str_4relay[18:19]
            r4 = str_4relay[23:24]
            relay_list = [r1, r2, r3, r4]
            Variables.parsing_GPIO_4relay = relay_list
            Variables.parsing_GPIO_4relay1 = relay_list
            print('Variables.parsing_GPIO_4relay =' + str(Variables.parsing_GPIO_4relay))

        except TimeoutError:
            Variables.parsing_GPIO_4relay = [0, 0, 0, 0]
            print('parsing_GPIO_4relay11 except TimeoutError')
        except ConnectTimeout:
            print('parsing_GPIO_4relay11 except ConnectTimeout')
            Variables.parsing_GPIO_4relay = [0, 0, 0, 0]
        except ConnectionError:
            print('parsing_GPIO_4relay11 except ConnectionError')
            Variables.parsing_GPIO_4relay = [0, 0, 0, 0]
        except NewConnectionError:
            print('parsing_GPIO_4relay11 except NewConnectionError')
            Variables.parsing_GPIO_4relay = [0, 0, 0, 0]
        finally:
            lock.release()



