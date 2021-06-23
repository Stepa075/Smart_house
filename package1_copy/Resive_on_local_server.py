import requests


def parsing_ESP():

  try:
    url = "http://localhost/test/doc/hello.html"
    r = requests.get(url)
    r.encoding = "UTF8"
    with open('response.html', 'w') as output_file:
     output_file.write(r.text)
    with open('response.txt', 'w') as output_file:
     output_file.write(r.text)

    text_file = open("response.html", "r")
    lines = text_file.read().split(',')
    print(lines)
    print(lines[0])
    print(len(lines))
    text_file.close()


  except:
    # url= 'http://192.168.0.110/configrst?st=1'
    # r.request.get(url)
    # str3=110
    pass

  return lines

if __name__ == "__main__":
 parsing_ESP()