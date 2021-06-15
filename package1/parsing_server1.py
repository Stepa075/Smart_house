import requests

ESP_Light_Sensor: int=0
Sadok_Light: int=0

def parsing_ESP():
  global ESP_Light_Sensor
  try:
    url= "http://192.168.0.110/sensors/adci1/"
    r= requests.get(url)
    r.encoding = "UTF8"
    # print(r.text)
    with open('test.html', 'w') as output_file:
      output_file.write(r.text)
    with open('test1.txt', 'w') as output_file:
      output_file.write(r.text)

    f = open('test1.txt')
    str1=f.read()
    f.close()

    str2=str1[str1.find(";") + 1 : ]
    str3=str2[str2.find(":") + 1 : str2.find(";")]
    ESP_Light_Sensor = int(str3)

  except:
    str3=-1
    pass

  return str3

def parsing_GPIO_Sadok():
  global Sadok_Light
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
    Sadok_Light=str_sad3
    print('str_sadok3 ' + str(str_sad3))

  except:
    str_sad3=-1
    pass
  return str_sad3

def parsing_GPIO_4relay():

  try:
    url = "http://192.168.0.120/gpioprint"
    r = requests.get(url)
    r.encoding = "UTF8"

    with open('4relay.txt', 'w') as output_file:
     output_file.write(r.text)

    f = open('4relay.txt')
    str_4relay = f.read()
    f.close()
    print('str_4relay= ' + str_4relay)
    str_4relay2 = str_4relay[str_4relay.find(":") + 1:]
    print("str_4relay2= " + str_4relay2)
    str_4relay3 = str_4relay2[: str_4relay2.find(";")]
    print('str_4relay3 exit out ' + str_4relay3)
  except:
    str_4relay3=-1
    pass
  return str_4relay3


# def pr():
#   print(ESP_Light_Sensor)
# if __name__ == "__main__":
#    parsing_GPIO_Sadok()
#    parsing_ESP()
#    pr()