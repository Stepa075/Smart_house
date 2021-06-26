import gc
import threading
from time import sleep
import requests
import Variables

lock = threading.RLock()
def start1():
    a=1
    while a==1:
        lock.acquire()
        try:
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

            r = requests.get('http://f0555107.xsph.ru/index.php', params=params)
            r.encoding = "UTF8"
            print('start1 = Ok')
            print(r.text)
            break
        except:
            params = {'params': '0', 'params1': '0', 'params2_1': '0', 'params2_2': '0', 'params2_3': '0', 'params2_4': '0', 'control': 'home'}
            r = requests.get('http://f0555107.xsph.ru/index.php', params=params)
            r.encoding = "UTF8"
            print('except start1' + r.text)
            sleep(5.0)
            pass
        finally:
          lock.release()
    gc.collect()
    sleep(60.0)
    start1()


def start2():
    a = 1
    while a == 1:
          global lines
          lock.acquire()
          try:
            url = "http://f0555107.xsph.ru/hello.html"
            r = requests.get(url)
            r.encoding = "UTF8"
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
            break

          except:
            lines.append('0')
            print('Except! start2')
            sleep(5.0)
            pass
          finally:
              lock.release()
          return lines
    sleep(70.0)
    start2()



def parsing_ESP():
  global str3
  a = 1
  while a == 1:
          lock.acquire()
          try:
            url = "http://192.168.0.110/sensors/adci1/"
            r = requests.get(url)
            r.encoding = "UTF8"
            # print('r.text= ' + r.text)
            with open('test.html', 'w') as output_file:
              output_file.write(r.text)
            with open('test1.txt', 'w') as output_file:
              output_file.write(r.text)

            f = open('test1.txt')
            str1=f.read()
            f.close()

            str2=str1[str1.find(";") + 1 : ]
            str3=str2[str2.find(":") + 1 : str2.find(";")]
            Variables.parsing_ESP = int(str3)
            Variables.parsing_ESP1 = int(str3)
            print('parsing_ESP = Ok')
            break
          except:
            print(' Except! parsing_ESP')
            url= 'http://192.168.0.110/configrst?st=1'
            r = requests.get(url)
            str3=110
            Variables.parsing_ESP = int(str3)
            Variables.parsing_ESP1 = int(str3)
            sleep(5.0)
            pass
          finally:
              lock.release()
          return str3
  sleep(60.0)
  parsing_ESP()


def parsing_GPIO_Sadok():
   a = 1
   while a == 1:
          lock.acquire()
          try:

            url = "http://192.168.0.100/gpioprint"
            r = requests.get(url)
            Variables.status_code_sadok = r.status_code
            r.encoding = "UTF8"

            with open('sadok.html', 'w') as output_file:
              output_file.write(r.text)
            with open('sadok1.txt', 'w') as output_file:
              output_file.write(r.text)

            f = open('sadok1.txt')
            str_sad = f.read()
            # print(str_sad)
            f.close()
            str_sad2 = str_sad[:str_sad.find(";") + 1]
            str_sad3 = str_sad2[str_sad2.find(":") + 1: str_sad2.find(";")]
            Variables.Sadok_Light=str_sad3
            Variables.Sadok_Light1 = str_sad3
            print('parsing_GPIO_Sadok = Ok ')
            break
          except:
            print(' Except! parsing_GPIO_Sadok')
            str_sad3=1
            Variables.Sadok_Light = str_sad3
            Variables.Sadok_Light1 = str_sad3
            sleep(5.0)
            pass
          finally:
              lock.release()
          return str_sad3
   sleep(30.0)
   parsing_GPIO_Sadok()


def parsing_GPIO_4relay11():
  a = 1
  while a == 1:
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
            break
          except:
              r1 = '0'
              r2 = '0'
              r3 = '0'
              r4 = '0'
              relay_list = [r1, r2, r3, r4]
              Variables.parsing_GPIO_4relay = relay_list
              print('Except! parsing_GPIO_4relay11')
              sleep(5.0)
              pass
          finally:
              lock.release()
          return relay_list
  sleep(30.0)
  parsing_GPIO_4relay11()







