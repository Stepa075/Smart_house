import threading
from threading import Thread
from time import sleep
import requests
from package1_copy import Variables

lock = threading.RLock()
def start1():
   sleep(5.0)
   lock.acquire()
   try:
    r4_0 = Variables.parsing_GPIO_4relay
    r4_1 = str(r4_0[0])
    r4_2 = str(r4_0[1])
    r4_3 = str(r4_0[2])
    r4_4 = str(r4_0[3])
    params = {'params': str(Variables.parsing_ESP),
              'params1': str(Variables.Sadok_Light),
              'params2_1': str(Variables.parsing_GPIO_4relay[0]),
              'params2_2': str(Variables.parsing_GPIO_4relay[1]),
              'params2_3': str(Variables.parsing_GPIO_4relay[2]),
              'params2_4': str(Variables.parsing_GPIO_4relay[3]), 'control': 'home'}

    r = requests.get('http://f0555107.xsph.ru/index.php', params=params)
    r.encoding = "UTF8"
    print('start1 = Ok')
    print(r.text)
   except:
    params = {'params': '0', 'params1': '0', 'params2_1': '0', 'params2_2': '0', 'params2_3': '0', 'params2_4': '0', 'control': 'home'}
    r = requests.get('http://f0555107.xsph.ru/index.php', params=params)
    r.encoding = "UTF8"

    # print(r.text)
    pass
   finally:
       lock.release()
   sleep(60.0)
   start1()


def start2():

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

  except:
    lines.append('0')
    pass
  finally:
      lock.release()
  sleep(70.0)
  start2()
  return lines


def parsing_ESP():
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
    print('parsing_ESP = Ok')
  except:
    url= 'http://192.168.0.110/configrst?st=1'
    r.request.get(url)
    str3=110
    Variables.parsing_ESP = int(str3)
    pass
  finally:
      lock.release()
  sleep(60.0)
  parsing_ESP()
  return str3

def parsing_GPIO_Sadok():
  lock.acquire()
  try:

    url = "http://192.168.0.100/gpioprint"
    r = requests.get(url)
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
    print('parsing_GPIO_Sadok = Ok ')
  except:
    str_sad3=1
    Variables.Sadok_Light = str_sad3
    pass
  finally:
      lock.release()
  sleep(30.0)
  parsing_GPIO_Sadok()
  return str_sad3

def parsing_GPIO_4relay11():
  lock.acquire()
  try:
    url = "http://192.168.0.120/gpioprint"
    r = requests.get(url)
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
    print('Variables.parsing_GPIO_4relay =' + str(Variables.parsing_GPIO_4relay))
  except:
      r1 = '0'
      r2 = '0'
      r3 = '0'
      r4 = '0'
      relay_list = [r1, r2, r3, r4]
      Variables.parsing_GPIO_4relay = relay_list
      print('Variables.parsing_GPIO_4relay =' + str(Variables.parsing_GPIO_4relay))
      pass
  finally:
      lock.release()
  sleep(30.0)
  parsing_GPIO_4relay11()
  return relay_list






