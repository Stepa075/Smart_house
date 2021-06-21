import requests


def parsing_ESP():

  try:
    url = "http://ochre-propulsion.000webhostapp.com/hello.html"
    r = requests.get(url)
    r.encoding = "UTF8"
    print('r.text = ' + r.text)
    # with open('test.html', 'w') as output_file:
    #   output_file.write(r.text)
    # with open('test1.txt', 'w') as output_file:
    #   output_file.write(r.text)
    #
    # f = open('test1.txt')
    # str1=f.read()
    # f.close()
    #
    # str2=str1[str1.find(";") + 1 : ]
    # str3=str2[str2.find(":") + 1 : str2.find(";")]


  except:
    # url= 'http://192.168.0.110/configrst?st=1'
    # r.request.get(url)
    # str3=110
    pass

  # return str3

if __name__ == "__main__":
 parsing_ESP()