import threading
from time import sleep

import requests

from package1_copy import Variables

lock = threading.RLock()
def read_flag_file():

  global lines
  lock.acquire()
  try:
    url = "http://f0555107.xsph.ru/Flag.html"
    r = requests.get(url)
    r.encoding = "UTF8"
    print('start2 = Ok')
    with open('response_flag_server.html', 'w') as output_file:
      output_file.write(r.text)
    with open('response_flag_server.txt', 'w') as output_file:
      output_file.write(r.text)

    text_file = open("response_flag.html", "r")
    lines = text_file.read().split(',')
    print(lines)
    # print(len(lines))
    text_file.close()
    Variables.response_flag = lines
    Variables.response_flag_1 = lines[0]
    Variables.response_flag_2 = lines[1]
    Variables.response_flag_3 = lines[2]
    Variables.response_flag_4 = lines[3]
    Variables.response_flag_5 = lines[4]
    Variables.response_flag_6 = lines[5]
    Variables.response_flag_7 = lines[6]

  except:
    lines.append('0')
    pass
  finally:
      lock.release()
  sleep(70.0)
  read_flag_file()
  return lines