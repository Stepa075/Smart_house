import gc
import threading
from time import sleep

import requests
from urllib3.exceptions import NewConnectionError

import Variables
global response
lock = threading.RLock()


def logics_Sadok_Light():
    lock.acquire()
    try:
        xxx1 = Variables.parsing_ESP
        print('logic_Sadok_Light xxx1= ' + str(xxx1))
        if int(xxx1) <= 100:
            if int(Variables.Sadok_Light) == 0:
                print('logics_Sadok_Light all Ok, ON!')
            elif int(Variables.Sadok_Light) == 1:
                url = Variables.GPIO_sad_on
                requests.get(url)
                print('Night street')
        elif int(xxx1) >= 100:
            if int(Variables.Sadok_Light) == 1:
                print('logics_Sadok_Light all Ok, OFF!')
            elif int(Variables.Sadok_Light) == 0:
                url = Variables.GPIO_sad_off
                requests.get(url)
                print('Day street!')
        else:
            print('logics_Sadok_Light str value, some error!')

    except TimeoutError:
        print('Except, Timeout error!')
    except requests.ConnectTimeout:
        print('Except, ConnectTimeout error!!')
    except ConnectionError:
        print('Except, Connection error!!')
    except NewConnectionError:
        print('Except, NewConnection error!!')
    finally:
        lock.release()
    gc.collect()


# def logicks_4relay_Light():


# except TimeoutError:
#     print('Except, Timeout error!')
# except requests.ConnectTimeout:
#     print('Except, ConnectTimeout error!!')
# except ConnectionError:
#     print('Except, Connection error!!')
# except NewConnectionError:
#     print('Except, NewConnection error!!')
# finally:
#     lock.release()
# gc.collect()


# a = 1
# while a == 1:
#     lock.acquire()
#     try:
#         if int(set_parsing_ESP) <= 100:
#             url = set_4relay1_on
#             requests.get(url)
#             url = set_4relay2_on
#             requests.get(url)
#             url = set_4relay3_on
#             requests.get(url)
#             url = set_4relay4_on
#             requests.get(url)
#             url = ''
#             print('4Relay Night')
#         else:
#             url = set_4relay1_off
#             requests.get(url)
#             url = set_4relay2_off
#             requests.get(url)
#             url = set_4relay3_off
#             requests.get(url)
#             url = set_4relay4_off
#             requests.get(url)
#             url = ''
#             print('4 Relay Day!')
#         break
def change_position_relay():
    print(' написать change_position_relay()')


def get_URL(set_url, data):
    global response
    lock.acquire()

    try:
        url = set_url
        params = data
        r = requests.get(url, params=params)
        r.encoding = "UTF8"
        with open('response.txt', 'w') as output_file:
            output_file.write(r.text)
        output_file.close()
        response = r.text

    except TimeoutError:
        print('Except, Timeout error!')
    except requests.ConnectTimeout:
        print('Except, ConnectTimeout error!!')
    except ConnectionError:
        print('Except, Connection error!!')
    except NewConnectionError:
        print('Except, NewConnection error!!')
    finally:
        lock.release()
    return response
