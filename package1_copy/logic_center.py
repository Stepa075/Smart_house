import threading
from threading import Thread
from time import sleep
import requests


from package1_copy import Variables

lock = threading.RLock()
def logicks_Sadok_Light():
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

       except:
           pass
       finally:
           lock.release()

def logicks_4relay_Light():
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

    except:
        print('Except!')
        pass
    finally:
        lock.release()
def remote_control_install():

    logicks_Sadok_Light()
    logicks_4relay_Light()

    sleep(10.0)
    remote_control_install()


def get_URL(URL):
    try:
        url = URL
        r = requests.get(url)
        r.encoding = "UTF8"
        with open('response.txt', 'w') as output_file:
          output_file.write(r.text)

        f = open('response.txt')
        response=f.read()
        f.close()
        return response
    except:
        return None
        pass


