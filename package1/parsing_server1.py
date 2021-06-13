import requests
from bs4 import BeautifulSoup

def parsing_ESP():
  url= "http://192.168.0.110/sensors/adci1/"
  r= requests.get(url)
  r.encoding = "UTF8"

  with open('test.html', 'w') as output_file:
    output_file.write(r.text)
  with open('test1.txt', 'w') as output_file:
    output_file.write(r.text)

  f = open('test1.txt')
  str1=f.read()
  f.close()

  str2=str1[str1.find(";") + 1 : ]
  str3=str2[str2.find(":") + 1 : str2.find(";")]

  return str3

def parsing_GPIO_Sadok():
  url = "http://192.168.0.100/gpioprint"
  r = requests.get(url)
  r.encoding = "UTF8"

  with open('sadok.html', 'w') as output_file:
    output_file.write(r.text)
  with open('sadok1.txt', 'w') as output_file:
    output_file.write(r.text)

  f = open('sadok1.txt')
  str_sad = f.read()
  print(str_sad)
  f.close()
  str_sad2 = str_sad[:str_sad.find(";") + 1]
  str_sad3 = str_sad2[str_sad2.find(":") + 1: str_sad2.find(";")]
  print(str_sad3)
  return str_sad3

# if __name__ == "__main__":
#   parsing_GPIO_Sadok()