import gc
import threading
from time import sleep

import requests


import Variables

global response
lock = threading.RLock()


def logics_Sadok_Light():

    while True:
        try:
            xxx1 = Variables.parsing_ESP
            print('logic_Sadok_Light xxx1= ' + str(xxx1))
            if isinstance(xxx1, int):
                if xxx1 <= 100:
                    if str(Variables.Sadok_Light) == '0':
                        print('logics_Sadok_Light all Ok, ON!')
                    elif str(Variables.Sadok_Light) == '1':
                        a = Variables.GPIO_sad_on
                        requests.get(a)
                        print('Night street')
                elif xxx1 >= 100:
                    if str(Variables.Sadok_Light) == '1':
                        print('logics_Sadok_Light all Ok, OFF!')
                    elif str(Variables.Sadok_Light) == '0':
                        b = Variables.GPIO_sad_off
                        requests.get(b)
                        print('Day street!')
                    else:
                        print('Error in parsing_GPIO_Sadok: ' + Variables.Sadok_Light)
                else:
                    print('logics_Sadok_Light str value, some error!')
            else:
                print('parsing_ESP str value, some error!')
            sleep(10.0)
        except:
            sleep(20.0)
            continue
            pass

    gc.collect()
    sleep(10.0)


def logics_4relay_Light():

    while True:
        try:

            print('logics_4relay_Light running!')
            if isinstance(Variables.parsing_ESP, int):
                if Variables.status_code_4relay == 200:
                    if str(Variables.GPIO_4Relay1_flag) == '2':
                        if int(Variables.parsing_ESP) <= 100:
                            if Variables.parsing_GPIO_4relay_0 == '0':
                                c = Variables.GPIO_4relay1_on
                                requests.get(c)
                                print('4Relay 1Relay set ON!')
                            else:
                                print('All Ok! 4Relay 1Relay ON!')
                        else:
                            if Variables.parsing_GPIO_4relay_0 == '1':
                                d = Variables.GPIO_4relay1_off
                                requests.get(d)
                                print('4 Relay 1Relay set OFF!')
                            else:
                                print('4 Relay 1Relay OFF!')
                    elif str(Variables.GPIO_4Relay1_flag) == '0':
                        e = Variables.GPIO_4relay1_off
                        requests.get(e)
                        print('4 Relay 1Relay Day MANUAL!')
                    elif str(Variables.GPIO_4Relay1_flag) == '1':
                        f = Variables.GPIO_4relay1_on
                        requests.get(f)
                        print('4Relay 1Relay Night MANUAL')
                    elif isinstance(Variables.GPIO_4Relay1_flag, str):
                        print('4Relay 1Relay manual control Error!')

                    if str(Variables.GPIO_4Relay2_flag) == '2':
                        if int(Variables.parsing_ESP) <= 100:
                            if Variables.parsing_GPIO_4relay_1 == '0':
                                g = Variables.GPIO_4relay2_on
                                requests.get(g)
                                print('4Relay 2Relay set ON!')
                            else:
                                print('All Ok! 4Relay 2Relay ON!')
                        else:
                            if Variables.parsing_GPIO_4relay_1 == '1':
                                h = Variables.GPIO_4relay2_off
                                requests.get(h)
                                print('4 Relay 2Relay set OFF!')
                            else:
                                print('4 Relay 2Relay OFF!')
                    elif str(Variables.GPIO_4Relay2_flag) == '0':
                        r = Variables.GPIO_4relay2_off
                        requests.get(r)
                        print('4 Relay 1Relay Day MANUAL!')
                    elif str(Variables.GPIO_4Relay2_flag) == '1':
                        j = Variables.GPIO_4relay2_on
                        requests.get(j)
                        print('4Relay 2Relay Night MANUAL')
                    elif isinstance(Variables.GPIO_4Relay2_flag, str):
                        print('4Relay 2Relay manual control Error!')

                if str(Variables.GPIO_4Relay3_flag) == '2':
                    if int(Variables.parsing_ESP) <= 100:
                        if Variables.parsing_GPIO_4relay_2 == '0':
                            k = Variables.GPIO_4relay3_on
                            requests.get(k)
                            print('4Relay 3Relay set ON!')
                        else:
                            print('All Ok! 4Relay 3Relay ON!')
                    else:
                        if Variables.parsing_GPIO_4relay_2 == '1':
                            l = Variables.GPIO_4relay3_off
                            requests.get(l)
                            print('4 Relay 3Relay set OFF!')
                        else:
                            print('4 Relay 3Relay OFF!')
                elif str(Variables.GPIO_4Relay3_flag) == '0':
                    m = Variables.GPIO_4relay3_off
                    requests.get(m)
                    print('4 Relay 3Relay Day MANUAL!')
                elif str(Variables.GPIO_4Relay3_flag) == '1':
                    n = Variables.GPIO_4relay3_on
                    requests.get(n)
                    print('4Relay 3Relay Night MANUAL')
                elif isinstance(Variables.GPIO_4Relay3_flag, str):
                    print('4Relay 3Relay manual control Error!')

                if str(Variables.GPIO_4Relay4_flag) == '2':
                    if int(Variables.parsing_ESP) <= 100:
                        if Variables.parsing_GPIO_4relay_3 == '0':
                            o = Variables.GPIO_4relay4_on
                            requests.get(o)
                            print('4Relay 4Relay set ON!')
                        else:
                            print('All Ok! 4Relay 4Relay ON!')
                    else:
                        if Variables.parsing_GPIO_4relay_3 == '1':
                            p = Variables.GPIO_4relay4_off
                            requests.get(p)
                            print('4 Relay 4Relay set OFF!')
                        else:
                            print('4 Relay 4Relay OFF!')
                elif str(Variables.GPIO_4Relay4_flag) == '0':
                    q = Variables.GPIO_4relay4_off
                    requests.get(q)
                    print('4 Relay 4Relay Day MANUAL!')
                elif str(Variables.GPIO_4Relay4_flag) == '1':
                    s = Variables.GPIO_4relay4_on
                    requests.get(s)
                    print('4Relay 4Relay Night MANUAL')
                elif isinstance(Variables.GPIO_4Relay4_flag, str):
                    print('4Relay 4Relay manual control Error!')

                else:
                    print('4Relay 1Relay somesing wrong in parsing_GPIO_4relay11')
            else:
                print('parsing_ESP str value, some error!')

            sleep(20.0)
        except:
            sleep(20.0)
            continue
            pass
    gc.collect()
    sleep(20.0)


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
    except:
        sleep(20.0)
        pass
    gc.collect()
    lock.release()
    return response
