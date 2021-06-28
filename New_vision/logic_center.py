import gc
import threading
from threading import Thread
from time import sleep
import requests
from Variables import *

lock = threading.RLock()
def logicks_Sadok_Light():
    a = 1
    while a == 1:
           lock.acquire()
           try:
               if int(set_parsing_ESP) <=100:
                  url= set_GPIO_sad_on
                  requests.get(url)
                  print('Night street')
               else:
                   url = set_GPIO_sad_off
                   requests.get(url)
                   print('Day street!')
               break
           except:
               print('Except! logics sadok light')
               sleep(5.0)
               pass
           finally:
               lock.release()
           sleep(20.0)
    gc.collect()

def logicks_4relay_Light():
    a = 1
    while a == 1:
        lock.acquire()
        try:
            if int(set_parsing_ESP) <= 100:
                url = set_4relay1_on
                requests.get(url)
                url = set_4relay2_on
                requests.get(url)
                url = set_4relay3_on
                requests.get(url)
                url = set_4relay4_on
                requests.get(url)
                url = ''
                print('4Relay Night')
            else:
                url = set_4relay1_off
                requests.get(url)
                url = set_4relay2_off
                requests.get(url)
                url = set_4relay3_off
                requests.get(url)
                url = set_4relay4_off
                requests.get(url)
                url = ''
                print('4 Relay Day!')
            break
        except:
            print('Except logics 4 relay!')
            sleep(5.0)
            pass
        finally:
            lock.release()
    sleep(20.0)
    gc.collect()

def change_position_relay():
    print(' написать change_position_relay()')

def remote_control_install():
    x = 1
    while x == 1:
            a = 1
            while a == 1:
                lock.acquire()
                try:
                    logicks_Sadok_Light()
                    logicks_4relay_Light()
                    break
                except:
                    print('except! remote_control_install!')
                    sleep(5.0)
                    pass
                finally:
                   lock.release()
            gc.collect()





def get_URL():
    a = 1
    while a == 1:
        try:
            url = set_URL
            r = requests.get(url)
            r.encoding = "UTF8"
            with open('response.txt', 'w') as output_file:
              output_file.write(r.text)
            output_file.close()
            f = open('response.txt')
            f.close()
            set_Response_URL=f.read()
            break
        except:
            response = '0'
            set_Response_URL = '0'
            sleep(5.0)
            pass

