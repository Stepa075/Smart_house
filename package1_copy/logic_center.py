import threading
from threading import Thread
from time import sleep
import requests
import Variables

lock = threading.RLock()
def logicks_Sadok_Light():
    a = 1
    while a == 1:
           lock.acquire()
           try:
               if int(Variables.parsing_ESP) <=100:
                  url= Variables.GPIO_sad_on
                  requests.get(url)
                  print('Night street')
               else:
                   url = Variables.GPIO_sad_off
                   requests.get(url)
                   print('Day street!')
               break
           except:
               print('Except! logics sadok light')
               sleep(5.0)
               pass
           finally:
               lock.release()

def logicks_4relay_Light():
    a = 1
    while a == 1:
        lock.acquire()
        try:
            if int(Variables.parsing_ESP) <= 100:
                url = Variables.GPIO_4relay1_on
                requests.get(url)
                url = Variables.GPIO_4relay2_on
                requests.get(url)
                url = Variables.GPIO_4relay3_on
                requests.get(url)
                url = Variables.GPIO_4relay4_on
                requests.get(url)
                print('4Relay Night')
            else:
                url = Variables.GPIO_4relay1_off
                requests.get(url)
                url = Variables.GPIO_4relay2_off
                requests.get(url)
                url = Variables.GPIO_4relay3_off
                requests.get(url)
                url = Variables.GPIO_4relay4_off
                requests.get(url)
                print('4 Relay Day!')
            break
        except:
            print('Except logics 4 relay!')
            sleep(5.0)
            pass
        finally:
            lock.release()
def change_position_relay():
    print(' написать change_position_relay()')

def remote_control_install():
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
    sleep(20.0)
    remote_control_install()



def get_URL():
    a = 1
    while a == 1:
        try:
            url = Variables.URL
            r = requests.get(url)
            r.encoding = "UTF8"
            with open('response.txt', 'w') as output_file:
              output_file.write(r.text)

            f = open('response.txt')
            response=f.read()
            f.close()
            Variables.Response_URL=f.read()
            break
        except:
            response = '0'
            Variables.Response_URL = '0'
            sleep(5.0)
            pass

        return response
