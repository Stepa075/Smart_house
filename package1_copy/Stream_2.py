
import time
from threading import Thread
from time import sleep
import requests
import parsing_server1

# starttime=time.time()



def start1():
   try:
    r4_0 = parsing_server1.parsing_GPIO_4relay()
    r4_1 = str(r4_0[0])
    r4_2 = str(r4_0[1])
    r4_3 = str(r4_0[2])
    r4_4 = str(r4_0[3])
    params = {'params': str(parsing_server1.parsing_ESP()), 'params1': str(parsing_server1.parsing_GPIO_Sadok()), 'params2_1': str(r4_2), 'params2_2': str(r4_2), 'params2_3': str(r4_3), 'params2_4': str(r4_4), 'control': 'home'}

    r = requests.get('http://f0555107.xsph.ru/index.php', params=params)
    r.encoding = "UTF8"
    print(r.text)
   except:
    params = {'params': '0', 'params1': '0', 'params2_1': '0','params2_2': '0', 'params2_3': '0', 'params2_4': '0', 'control': 'home'}
    r = requests.get('http://f0555107.xsph.ru/index.php', params=params)
    r.encoding = "UTF8"
    print(r.text)
    pass
   sleep(15.0)
   start1()


def start2():

  global lines
  try:
    url = "http://f0555107.xsph.ru/hello.html"
    r = requests.get(url)
    r.encoding = "UTF8"
    print('r.text = ' + r.text)
    with open('response_server.html', 'w') as output_file:
      output_file.write(r.text)
    with open('response_server.txt', 'w') as output_file:
      output_file.write(r.text)

    text_file = open("response_server.html", "r")
    lines = text_file.read().split(',')
    print(lines)
    print(len(lines))
    text_file.close()


  except:
    lines.append('0')
    pass
  sleep(15.0)
  start2()
  return lines

th = Thread(target=start1)
th.start()
th = Thread(target=start2)
th.start()




