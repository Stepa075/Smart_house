import requests
import parsing_server1
from parsing_server1 import ESP_Light_Sensor
import requests
def logicks_Sadok_Light():
       if int(parsing_server1.parsing_ESP()) <=100:
          url='http://192.168.0.100/gpio?st=0&pin=0'
          requests.get(url)

          print('Night')
       else:
           url = 'http://192.168.0.100/gpio?st=1&pin=0'
           requests.get(url)
           print('Day!')
           # print(ESP_Light_Sensor)


def get_URL(URL):
    url = URL
    r = requests.get(url)
    r.encoding = "UTF8"
    with open('response.txt', 'w') as output_file:
      output_file.write(r.text)

    f = open('response.txt')
    response=f.read()
    f.close()
    return response