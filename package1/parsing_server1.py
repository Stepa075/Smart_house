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
  # print(str3)
  return str3

